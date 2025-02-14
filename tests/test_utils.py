from datetime import date, datetime, time, timedelta

import pytest
from loguru import logger
from pydantic import BaseModel

from vlmrun.hub.registry import registry
from vlmrun.hub.utils import jsonschema_to_model, patch_response_format


def test_patch_response_format():
    class OriginalModel(BaseModel):
        date_field: date
        datetime_field: datetime
        time_field: time
        timedelta_field: timedelta

    # Patch the model
    PatchedModel = patch_response_format(OriginalModel)

    # Check that the fields have been converted to str
    assert PatchedModel.model_fields["date_field"].annotation is str
    assert PatchedModel.model_fields["datetime_field"].annotation is str
    assert PatchedModel.model_fields["time_field"].annotation is str
    assert PatchedModel.model_fields["timedelta_field"].annotation is str

    # Check that the patched model can be instantiated with string values
    instance = PatchedModel(
        date_field="2023-01-01",
        datetime_field="2023-01-01T12:00:00",
        time_field="12:00:00",
        timedelta_field="1 day, 0:00:00",
    )

    # Verify the instance is created successfully
    assert instance.date_field == "2023-01-01"
    assert instance.datetime_field == "2023-01-01T12:00:00"
    assert instance.time_field == "12:00:00"
    assert instance.timedelta_field == "1 day, 0:00:00"


def test_patch_response_format_models():
    from typing import Type

    from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

    for sample in VLMRUN_HUB_DATASET.values():
        logger.debug(f"Patching model {sample.response_model.__name__}")
        response_model: Type[BaseModel] = sample.response_model
        patched_model = patch_response_format(response_model)
        assert issubclass(patched_model, BaseModel)


def test_jsonschema_to_model_with_registry_schemas():
    """Test that jsonschema_to_model works with all schemas in the registry."""
    registry.load_schemas()

    for domain, schema_class in registry.schemas.items():
        json_schema = schema_class.model_json_schema()

        try:
            generated_model = jsonschema_to_model(json_schema)

            original_fields = set(schema_class.model_fields.keys())
            generated_fields = set(generated_model.model_fields.keys())

            assert original_fields == generated_fields, (
                f"Field mismatch for {domain}:\n"
                f"Original fields: {original_fields}\n"
                f"Generated fields: {generated_fields}\n"
                f"Missing: {original_fields - generated_fields}\n"
                f"Extra: {generated_fields - original_fields}"
            )

        except Exception as e:
            pytest.fail(f"Failed to process schema for {domain}: {str(e)}")
