import hashlib
import importlib
import json
from functools import cached_property
from pathlib import Path
from typing import Dict, List, Literal, Optional, Tuple, Type, Union

from loguru import logger
from pydantic import BaseModel, Field, model_validator
from pydantic_yaml import parse_yaml_raw_as


class Registry:
    """A singleton registry for schemas.

    Examples:
        >>> from vlmrun.hub.registry import registry
        >>> schema = registry["document.invoice"]
        >>> registry.list_schemas()
        ['document.invoice', 'document.receipt', ...]
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._schemas = {}
            cls._instance._initialized = False
            cls._instance._schema_metadata = {}  # Store metadata when registering schemas
        return cls._instance

    @property
    def schemas(self) -> Dict[str, Type[BaseModel]]:
        """Lazily load schemas when first accessed."""
        if not self._initialized:
            self.load_schemas()
        return self._schemas

    def _extract_metadata(self, schema) -> dict:
        return {
            "description": schema.description,
            "supported_inputs": schema.metadata.supported_inputs if schema.metadata else None,
            "tags": schema.metadata.tags if schema.metadata else None,
            "sample_data": ([schema.sample_data] if isinstance(schema.sample_data, str) else schema.sample_data),
        }

    def _load_catalog(self, path: Path) -> None:
        catalog = SchemaCatalogYaml.from_yaml(path)
        for schema in catalog.schemas:
            metadata = self._extract_metadata(schema)
            self.register(schema.domain, schema.schema_class, metadata)
        logger.debug(f"Loaded schemas from {path}")

    def register(self, name: str, schema: Type[BaseModel], metadata: Optional[dict] = None) -> None:
        """Register a schema with the registry."""
        if not issubclass(schema, BaseModel):
            raise ValueError(f"Schema {name} is not a subclass of BaseModel, type={type(schema)}")
        self._schemas[name] = schema
        if metadata:
            self._schema_metadata[name] = metadata

    def load_schemas(self, catalog_paths: Optional[Tuple[Union[str, Path]]] = None) -> None:
        from vlmrun.hub.constants import VLMRUN_HUB_CATALOG_PATH, VLMRUN_HUB_PATH

        if not self._initialized:
            try:
                # Load default catalog
                self._load_catalog(VLMRUN_HUB_CATALOG_PATH)

                # Load contrib catalog if exists
                contrib_path = VLMRUN_HUB_PATH / "schemas/contrib/catalog.yaml"
                if contrib_path.exists():
                    try:
                        self._load_catalog(contrib_path)
                    except Exception as e:
                        logger.error(f"Failed to load contrib schemas: {e}")

                self._initialized = True
            except Exception as e:
                logger.error(f"Failed to load default schemas: {e}")
                raise

        # Load additional catalogs if provided
        if catalog_paths is not None:
            for path in catalog_paths:
                path = Path(path)
                if not path.exists():
                    raise FileNotFoundError(f"Catalog file not found: {path}")
                self._load_catalog(path)

    def get_domain_info(self, domain: str) -> dict:
        """Get metadata for a domain."""
        return self._schema_metadata.get(domain, {})

    def list_schemas(self) -> List[str]:
        return sorted(self.schemas.keys())

    def __contains__(self, name: str) -> bool:
        return name in self.schemas

    def __getitem__(self, name: str) -> Type[BaseModel]:
        try:
            return self.schemas[name]
        except KeyError:
            raise KeyError(f"Schema '{name}' not found. Available schemas: {', '.join(self.list_schemas())}")

    def __repr__(self) -> str:
        repr_str = f"Registry [schemas={len(self.schemas)}]"
        for name, schema in sorted(self.schemas.items()):
            repr_str += f"\n  {name} :: {schema.__name__}"
        return repr_str


registry = Registry()


class SchemaCatalogMetadata(BaseModel):
    """Represents the metadata for a schema in the catalog."""

    supported_inputs: Optional[List[Literal["image", "audio", "video", "document"]]] = Field(
        None, description="List of supported input types"
    )
    tags: Optional[List[str]] = Field(None, description="List of tags")


class SchemaCatalogItem(BaseModel):
    """Represents a single schema entry in the catalog."""

    domain: str = Field(..., description="Domain identifier for the schema")
    schema_path: str = Field(..., alias="schema", description="Fully qualified path to the schema class")
    prompt: str = Field(..., description="Task-specific prompt for the schema")
    description: Optional[str] = Field(None, description="Detailed description of the schema's purpose")
    sample_data: Optional[Union[str, List[str]]] = Field(None, description="URL to sample data for testing")
    version: Optional[str] = Field(None, description="Optional schema version in semver format")
    metadata: Optional[SchemaCatalogMetadata] = Field(None, description="Additional metadata including tags")

    @model_validator(mode="after")
    def validate_supported_inputs(self):
        if self.metadata and self.metadata.supported_inputs:
            assert all(
                input in ["image", "audio", "video", "document"] for input in self.metadata.supported_inputs
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
        return self.schema_path.rsplit(".", 1)[0]

    @property
    def class_name(self) -> str:
        return self.schema_path.rsplit(".", 1)[1]

    @cached_property
    def schema_class(self) -> type[BaseModel]:
        try:
            module = importlib.import_module(self.module_name)
            schema_class = getattr(module, self.class_name)
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Unable to import {self.schema_path}: {e}")
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
