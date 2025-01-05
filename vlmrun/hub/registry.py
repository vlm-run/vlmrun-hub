import hashlib
import importlib
import json
from functools import cached_property
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, model_validator
from pydantic_yaml import parse_yaml_raw_as


class Registry:
    """Registry for schemas."""

    _instance: "Registry" = None
    """Singleton instance of the registry."""

    schemas: dict[str, BaseModel] = {}
    """Dictionary of registered schemas."""

    @classmethod
    def get(cls) -> "Registry":
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def register(cls, name: str, schema: type[BaseModel]):
        if not issubclass(schema, BaseModel):
            raise ValueError(f"Schema {name} is not a subclass of BaseModel, type={type(schema)}")
        cls.get().schemas[name] = schema

    def __contains__(self, name: str) -> bool:
        return name in self.schemas

    def __getitem__(self, name: str) -> BaseModel:
        return self.schemas[name]

    @classmethod
    def list(cls) -> list[str]:
        return list(cls.schemas.keys())


class SchemaCatalogMetadata(BaseModel):
    """Represents the metadata for a schema in the catalog."""

    supported_inputs: list[Literal["image", "video", "document"]] | None = Field(
        None, description="List of supported input types"
    )
    tags: list[str] | None = Field(None, description="List of tags")


class SchemaCatalogItem(BaseModel):
    """Represents a single schema entry in the catalog."""

    domain: str = Field(..., description="Domain identifier for the schema")
    schema: str = Field(..., description="Fully qualified path to the schema class")
    prompt: str = Field(..., description="Task-specific prompt for the schema")
    description: str = Field(..., description="Detailed description of the schema's purpose")
    sample_data: str = Field(..., description="URL to sample data for testing")
    version: str | None = Field(None, description="Optional schema version in semver format")
    metadata: SchemaCatalogMetadata | None = Field(None, description="Additional metadata including tags")

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
    schemas: list[SchemaCatalogItem] = Field(..., description="List of schema entries")

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "SchemaCatalogYaml":
        if not yaml_path.exists():
            raise FileNotFoundError(f"Catalog file not found: {yaml_path}")
        return parse_yaml_raw_as(cls, yaml_path.read_text())
