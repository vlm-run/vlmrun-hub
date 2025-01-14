from pathlib import Path

import pytest
from pydantic import BaseModel

from vlmrun.hub.registry import SchemaCatalogYaml


@pytest.mark.parametrize(
    "catalog_path",
    [
        Path(__file__).parent.parent / "vlmrun" / "hub" / "catalog.yaml",
        Path(__file__).parent.parent / "vlmrun" / "hub" / "schemas" / "contrib" / "catalog.yaml",
    ],
)
def test_catalog_yaml(catalog_path):
    """Test that catalog.yaml is valid and follows the expected structure."""
    assert catalog_path.exists(), "catalog.yaml file not found"

    # Load the catalog
    catalog = SchemaCatalogYaml.from_yaml(catalog_path)

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
        if entry.version:
            version_parts = entry.version.split(".")
            assert len(version_parts) == 3, "Version must follow semver format (X.Y.Z)"
            assert all(part.isdigit() for part in version_parts), "Version parts must be numeric"

        # Sample data URL validation
        assert entry.sample_data.startswith(
            "https://storage.googleapis.com/vlm-data-public-prod/"
        ), "Sample data must be in Google Cloud Storage"

        # Metadata validation
        if entry.metadata:
            if entry.metadata.supported_inputs:
                assert isinstance(entry.metadata.supported_inputs, list), "Supported inputs must be a list"
                assert len(entry.metadata.supported_inputs) > 0, "Must have at least one supported input"
            if entry.metadata.tags:
                assert isinstance(entry.metadata.tags, list), "Tags must be a list"
                assert len(entry.metadata.tags) > 0, "Must have at least one tag"
                assert all(isinstance(tag, str) for tag in entry.metadata.tags), "All tags must be strings"

        # Content validation
        assert len(entry.prompt) >= 10, "Prompt must be descriptive (min 10 chars)"
        assert len(entry.description) >= 20, "Description must be detailed (min 20 chars)"

        # Dynamic schema validation
        try:
            schema_class = entry.schema_class
            assert issubclass(schema_class, BaseModel), f"Schema {entry.schema} must be a Pydantic model"
        except Exception as e:
            pytest.fail(f"Unable to import {entry.schema}: {e}")


def test_catalog_yaml_with_refs():
    """Test that catalog.yaml with refs is valid and follows the expected structure."""
    catalog_path = Path(__file__).parent.parent / "vlmrun" / "hub" / "full-catalog.yaml"
    assert catalog_path.exists(), "full-catalog.yaml file not found"

    # Load the catalog
    catalog = SchemaCatalogYaml.from_yaml(catalog_path)

    # Basic validation
    assert catalog.apiVersion == "v1", "API version must be v1"

    n_schemas = len(
        SchemaCatalogYaml.from_yaml(Path(__file__).parent.parent / "vlmrun" / "hub" / "catalog.yaml").schemas
    ) + len(
        SchemaCatalogYaml.from_yaml(
            Path(__file__).parent.parent / "vlmrun" / "hub" / "schemas" / "contrib" / "catalog.yaml"
        ).schemas
    )
    assert len(catalog.schemas) == n_schemas, "Catalog must contain the correct number of schemas"
