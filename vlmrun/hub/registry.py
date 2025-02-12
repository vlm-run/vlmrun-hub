import hashlib
import importlib
import json
from functools import cached_property, wraps
from pathlib import Path
from typing import Callable, Dict, List, Literal, Optional, Tuple, Type, TypeVar, Union

from loguru import logger
from pydantic import BaseModel, Field, model_validator
from pydantic_yaml import parse_yaml_raw_as

T = TypeVar("T")


def ensure_schemas_loaded(func: Callable[..., T]) -> Callable[..., T]:
    """Decorator to ensure schemas are loaded before accessing registry."""

    @wraps(func)
    def wrapper(self: "Registry", *args, **kwargs) -> T:
        if not self._initialized:
            self.load_schemas()
        return func(self, *args, **kwargs)

    return wrapper


class Registry:
    """A singleton registry for schemas.

    Examples:
        >>> from vlmrun.hub.registry import registry
        >>> schema = registry["document.invoice"]
        >>> registry.list_schemas()
        ['document.invoice', 'document.receipt', ...]
    """

    def __init__(self):
        self.schemas: Dict[str, Type[BaseModel]] = {}
        self._initialized: bool = False

    def load_schemas(self, catalog_paths: Optional[Tuple[Union[str, Path]]] = None) -> None:
        from vlmrun.hub.constants import VLMRUN_HUB_CATALOG_PATH, VLMRUN_HUB_PATH

        if not self._initialized:
            try:
                catalog = SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CATALOG_PATH)
                for schema in catalog.schemas:
                    self.register(schema.domain, schema.schema_class)

                contrib_path = VLMRUN_HUB_PATH / "schemas/contrib/catalog.yaml"
                if contrib_path.exists():
                    try:
                        contrib_catalog = SchemaCatalogYaml.from_yaml(contrib_path)
                        for schema in contrib_catalog.schemas:
                            self.register(schema.domain, schema.schema_class)
                    except Exception as e:
                        logger.error(f"Failed to load contrib schemas: {e}")

                self._initialized = True
                logger.debug(f"Loaded default and contrib schemas:\n{self}")
            except Exception as e:
                logger.error(f"Failed to load default schemas: {e}")
                raise

        if catalog_paths is not None:
            for path in catalog_paths:
                path = Path(path)
                if not path.exists():
                    raise FileNotFoundError(f"Catalog file not found: {path}")

                catalog = SchemaCatalogYaml.from_yaml(path)
                for schema in catalog.schemas:
                    self.register(schema.domain, schema.schema_class)
                logger.debug(f"Loaded additional schemas from {path}")

    def register(self, name: str, schema: Type[BaseModel]) -> None:
        """Register a schema with the registry."""
        if not issubclass(schema, BaseModel):
            raise ValueError(f"Schema {name} is not a subclass of BaseModel, type={type(schema)}")
        self.schemas[name] = schema

    @ensure_schemas_loaded
    def list_schemas(self) -> List[str]:
        return sorted(self.schemas.keys())

    @ensure_schemas_loaded
    def __contains__(self, name: str) -> bool:
        return name in self.schemas

    @ensure_schemas_loaded
    def __getitem__(self, name: str) -> Type[BaseModel]:
        try:
            return self.schemas[name]
        except KeyError:
            raise KeyError(f"Schema '{name}' not found. Available schemas: {', '.join(self.list_schemas())}")

    def __repr__(self) -> str:
        if not self._initialized:
            self.load_schemas()
        repr_str = f"Registry [schemas={len(self.schemas)}]"
        for name, schema in sorted(self.schemas.items()):
            repr_str += f"\n  {name} :: {schema.__name__}"
        return repr_str


registry = Registry()


class SchemaCatalogMetadata(BaseModel):
    """Represents the metadata for a schema in the catalog."""

    supported_inputs: Optional[List[Literal["image", "video", "document"]]] = Field(
        None, description="List of supported input types"
    )
    tags: Optional[List[str]] = Field(None, description="List of tags")


class SchemaCatalogItem(BaseModel):
    """Represents a single schema entry in the catalog."""

    domain: str = Field(..., description="Domain identifier for the schema")
    schema: str = Field(..., description="Fully qualified path to the schema class")
    prompt: str = Field(..., description="Task-specific prompt for the schema")
    description: Optional[str] = Field(None, description="Detailed description of the schema's purpose")
    sample_data: Optional[Union[str, List[str]]] = Field(None, description="URL to sample data for testing")
    version: Optional[str] = Field(None, description="Optional schema version in semver format")
    metadata: Optional[SchemaCatalogMetadata] = Field(None, description="Additional metadata including tags")

    @model_validator(mode="after")
    def validate_supported_inputs(self):
        if self.metadata and self.metadata.supported_inputs:
            assert all(
                input in ["image", "video", "document"] for input in self.metadata.supported_inputs
            ), "Supported inputs must be valid"
        return self

    @model_validator(mode="after")
    def validate_domain(self):
        assert "." in self.domain, "Domain must be in format: category.name"
        category, name = self.domain.split(".", 1)
        assert category and name, "Both category and name must be non-empty"
        return self

    @property
    def module_name(self) -> str:
        return self.schema.rsplit(".", 1)[0]

    @property
    def class_name(self) -> str:
        return self.schema.rsplit(".", 1)[1]

    @cached_property
    def schema_class(self) -> type[BaseModel]:
        try:
            module = importlib.import_module(self.module_name)
            schema_class = getattr(module, self.class_name)
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Unable to import {self.schema}: {e}")
        return schema_class

    @cached_property
    def schema_hash(self) -> str:
        """Compute a hash of the schema JSON."""
        schema_json: dict = self.schema_class.model_json_schema()
        schema_hash: str = hashlib.sha256(json.dumps(schema_json).encode()).hexdigest()[:8]
        return schema_hash


class SchemaCatalogYaml(BaseModel):
    """Root model for the catalog.yaml file."""

    apiVersion: str = Field(..., description="API version of the catalog format")
    catalogs: Union[List[str], None] = Field(None, description="List of catalog files to include as references")
    schemas: List[SchemaCatalogItem] = Field(default_factory=list, description="List of schema entries")

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "SchemaCatalogYaml":
        if not yaml_path.exists():
            raise FileNotFoundError(f"Catalog file not found: {yaml_path}")
        catalog: SchemaCatalogYaml = parse_yaml_raw_as(cls, yaml_path.read_text())
        catalog = catalog.load_catalogs(yaml_path.parent)
        return catalog

    def load_catalogs(self, subdirectory: Union[str, Path]) -> "SchemaCatalogYaml":
        """Unroll the catalog references into a single list of schemas."""
        if self.catalogs:
            for catalog in self.catalogs:
                logger.debug(f"Loading sub-catalog [catalog={catalog}, dir={subdirectory}]")
                catalog_path = Path(subdirectory) / catalog
                assert catalog_path.exists(), f"Catalog {catalog} not found in schemas"
                catalog_yaml = SchemaCatalogYaml.from_yaml(catalog_path)
                n_schemas = len(catalog_yaml.schemas)
                self.schemas.extend(catalog_yaml.schemas)
                logger.debug(f"Loaded sub-catalog [catalog={catalog}, n_schemas={n_schemas}]")
            logger.debug(f"Loaded full catalog [n_catalogs={len(self.catalogs)}, n_schemas={len(self.schemas)}]")
        return self
