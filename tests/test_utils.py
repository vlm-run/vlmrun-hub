from datetime import date, datetime, time, timedelta

from loguru import logger
from pydantic import BaseModel

from vlmrun.hub.utils import patch_response_format


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
