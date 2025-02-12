from pathlib import Path

import pytest
from pydantic import BaseModel
from ruamel.yaml.parser import ParserError

from vlmrun.hub.registry import Registry, SchemaCatalogItem, SchemaCatalogYaml


@pytest.fixture
def registry():
    """Create a fresh registry instance for each test"""
    return Registry()


def test_registry_singleton():
    """Test that Registry behaves as a singleton"""
    from vlmrun.hub.registry import registry as registry1
    from vlmrun.hub.registry import registry as registry2

    assert registry1 is registry2
    assert isinstance(registry1, Registry)


def test_registry_load_schemas(registry):
    """Test loading schemas from catalog"""
    registry.load_schemas()
    assert len(registry.schemas) > 0

    assert "document.receipt" in registry.schemas
    assert "document.resume" in registry.schemas
    assert "document.us-drivers-license" in registry.schemas


def test_registry_getitem(registry):
    """Test accessing schemas using dictionary syntax"""
    schema = registry["document.receipt"]
    assert issubclass(schema, BaseModel)

    with pytest.raises(KeyError):
        _ = registry["non.existent.schema"]


def test_registry_repr(registry):
    """Test string representation of registry"""
    repr_str = repr(registry)
    assert "Registry [schemas=" in repr_str
    assert "document.receipt" in repr_str
    assert "document.resume" in repr_str


def test_registry_list_schemas(registry):
    """Test listing available schemas"""
    schemas = registry.list_schemas()
    assert isinstance(schemas, list)
    assert len(schemas) > 0
    assert "document.receipt" in schemas
    assert "document.resume" in schemas


def test_schema_catalog_item_validation():
    """Test SchemaCatalogItem validation"""
    item = SchemaCatalogItem(
        domain="test.domain",
        schema="vlmrun.hub.schemas.document.Receipt",
        prompt="Test prompt",
        description="Test description that is sufficiently detailed",
        supported_inputs=["document"],
        tags=["test"],
    )
    assert item.domain == "test.domain"
    assert item.schema == "vlmrun.hub.schemas.document.Receipt"
    assert len(item.prompt) >= 10
    assert len(item.description) >= 20


def test_schema_catalog_yaml_loading():
    """Test loading catalog from YAML"""
    catalog_path = Path(__file__).parent.parent / "vlmrun" / "hub" / "catalog.yaml"
    catalog = SchemaCatalogYaml.from_yaml(catalog_path)

    assert catalog.apiVersion == "v1"
    assert isinstance(catalog.schemas, list)
    assert len(catalog.schemas) > 0

    if catalog.catalogs:
        assert isinstance(catalog.catalogs, list)
        for ref in catalog.catalogs:
            ref_path = Path(__file__).parent.parent / "vlmrun" / "hub" / ref
            assert ref_path.exists()


def test_ensure_schemas_loaded_decorator(registry):
    """Test the ensure_schemas_loaded decorator"""
    schema = registry["document.receipt"]
    assert schema is not None

    assert len(registry.schemas) > 0


def test_registry_load_schemas_with_invalid_path(registry):
    """Test loading schemas from non-existent path raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError, match="Catalog file not found"):
        registry.load_schemas(catalog_paths=("nonexistent.yaml",))


def test_registry_load_schemas_with_invalid_yaml(registry, tmp_path):
    """Test loading schemas with invalid YAML content raises YAMLError"""
    invalid_yaml = tmp_path / "invalid.yaml"
    invalid_yaml.write_text("invalid: [\nyaml: content")

    with pytest.raises(ParserError):
        registry.load_schemas(catalog_paths=(invalid_yaml,))


def test_registry_load_schemas_with_invalid_schema(registry, tmp_path):
    """Test loading schemas with invalid schema definition raises ValueError"""
    invalid_schema_yaml = """
apiVersion: v1
schemas:
- domain: test.invalid
  schema: nonexistent.module.Schema
  prompt: Test prompt
  description: Test description that is sufficiently detailed
  metadata:
    supported_inputs: ["document"]
    tags: ["test"]
"""
    test_yaml = tmp_path / "test.yaml"
    test_yaml.write_text(invalid_schema_yaml)

    with pytest.raises(ValueError, match="Unable to import nonexistent.module.Schema"):
        registry.load_schemas(catalog_paths=(test_yaml,))


def test_registry_detailed_key_error(registry):
    """Test that KeyError includes available schemas in message"""
    with pytest.raises(KeyError) as exc_info:
        _ = registry["non.existent.schema"]

    error_msg = str(exc_info.value)
    assert "Available schemas:" in error_msg
    assert "document.receipt" in error_msg
    assert "document.resume" in error_msg
