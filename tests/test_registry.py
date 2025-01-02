import pytest
from loguru import logger
from pydantic import BaseModel

from vlmrun.hub.registry import Registry


class SampleSchema(BaseModel):
    """Sample schema for testing"""

    field1: str
    field2: int


def test_singleton_instance():
    """Test that the instance method returns the same instance"""
    instance1 = Registry.get()
    instance2 = Registry.get()
    assert instance1 is instance2, "Registry should be a singleton"


def test_register_schema():
    """Test registering a schema"""
    registry = Registry.get()
    schema_name = "SampleSchema"
    sample_schema = SampleSchema(field1="test", field2=123)

    registry.register(schema_name, sample_schema)

    assert schema_name in registry.schemas, "Schema should be registered"
    assert registry[schema_name] == sample_schema, "Registered schema should match the input schema"


def test_get_schema():
    """Test retrieving a registered schema"""
    registry = Registry.get()
    schema_name = "SampleSchema"
    sample_schema = SampleSchema(field1="test", field2=123)

    registry.register(schema_name, sample_schema)
    retrieved_schema = registry[schema_name]

    assert retrieved_schema == sample_schema, "Retrieved schema should match the registered schema"


def test_get_nonexistent_schema():
    """Test retrieving a schema that does not exist"""
    registry = Registry.get()
    with pytest.raises(KeyError):
        registry["NonExistentSchema"]


def test_list_schemas():
    """Test listing all registered schemas"""
    registry = Registry.get()
    schema_name = "SampleSchema"
    sample_schema = SampleSchema(field1="test", field2=123)

    registry.register(schema_name, sample_schema)
    assert schema_name in registry.list(), "Schema should be listed"


def test_registry_on_import():
    """Test that the registry is populated on import"""
    from vlmrun.hub import schemas

    schemas.import_all()
    assert len(Registry.get().list()) > 0, "Registry should be populated on import"
    for schema in Registry.get().list():
        logger.debug(f"Schema: {schema}")
