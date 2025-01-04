import importlib
from pathlib import Path
from typing import List

import pytest
from pydantic import BaseModel, Field
from pydantic_yaml import parse_yaml_raw_as


class SchemaCatalogEntry(BaseModel):
    """Represents a single schema entry in the catalog."""

    domain: str = Field(..., description="Domain identifier for the schema")
    schema: str = Field(..., description="Fully qualified path to the schema class")
    prompt: str = Field(..., description="Task-specific prompt for the schema")
    description: str = Field(..., description="Detailed description of the schema's purpose")
    version: str = Field(..., description="Schema version in semver format")
    sample_data: str = Field(..., description="URL to sample data for testing")
    metadata: dict = Field(..., description="Additional metadata including tags")


class CatalogYaml(BaseModel):
    """Root model for the catalog.yaml file."""

    apiVersion: str = Field(..., description="API version of the catalog format")
    schemas: List[SchemaCatalogEntry] = Field(..., description="List of schema entries")


def test_catalog_yaml():
    """Test that catalog.yaml is valid and follows the expected structure."""
    catalog_path = Path(__file__).parent.parent / "vlmrun" / "hub" / "catalog.yaml"
    assert catalog_path.exists(), "catalog.yaml file not found"

    with open(catalog_path, "r") as f:
        catalog = parse_yaml_raw_as(CatalogYaml, f.read())

    # Basic validation
    assert catalog.apiVersion == "v1", "API version must be v1"
    assert len(catalog.schemas) > 0, "Catalog must contain at least one schema"

    # Schema-specific validation
    for entry in catalog.schemas:
        # Domain format validation
        assert "." in entry.domain, "Domain must be in format: category.name"
        category, name = entry.domain.split(".", 1)
        assert category and name, "Both category and name must be non-empty"

        # Schema path validation
        assert entry.schema.startswith("vlmrun.hub.schemas."), "Schema must be in vlmrun.hub.schemas package"

        # Version format validation (basic semver check)
        version_parts = entry.version.split(".")
        assert len(version_parts) == 3, "Version must follow semver format (X.Y.Z)"
        assert all(part.isdigit() for part in version_parts), "Version parts must be numeric"

        # Sample data URL validation
        assert entry.sample_data.startswith(
            "https://storage.googleapis.com/vlm-data-public-prod/"
        ), "Sample data must be in Google Cloud Storage"

        # Metadata validation
        assert "tags" in entry.metadata, "Metadata must include tags"
        assert isinstance(entry.metadata["tags"], list), "Tags must be a list"
        assert len(entry.metadata["tags"]) > 0, "Must have at least one tag"
        assert all(isinstance(tag, str) for tag in entry.metadata["tags"]), "All tags must be strings"

        # Content validation
        assert len(entry.prompt) >= 10, "Prompt must be descriptive (min 10 chars)"
        assert len(entry.description) >= 20, "Description must be detailed (min 20 chars)"

        # Dynamic schema validation
        module_name, class_name = entry.schema.rsplit(".", 1)
        try:
            module = importlib.import_module(module_name)
            schema_class = getattr(module, class_name)
            assert issubclass(schema_class, BaseModel), f"Schema {entry.schema} must be a Pydantic model"
        except (ImportError, AttributeError) as e:
            pytest.fail(f"Unable to import {entry.schema}: {e}")
