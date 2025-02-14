import importlib
import json
import sys
from functools import lru_cache
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, List, Tuple, Type, Union, get_args, get_origin

from datamodel_code_generator import DataModelType, InputFileType, generate
from pydantic import BaseModel, create_model
from typing_extensions import TypeAlias

ResponseFormat: TypeAlias = Type[BaseModel]
AnnotationType: TypeAlias = Union[Type, Any]


def patch_response_format(response_format: ResponseFormat) -> ResponseFormat:
    """Patch the OpenAI response format to handle Pydantic models, including nested models.

    The following fields are not supported by OpenAI:
    - date
    - datetime
    - time
    - timedelta

    This function patches the response format to handle these fields. We convert them to strings and
    then convert them back to the original type.
    """
    from datetime import date, datetime, time, timedelta

    def patch_pydantic_field_annotation(annotation: AnnotationType) -> AnnotationType:
        if annotation in [date, datetime, time, timedelta]:
            return str
        elif get_origin(annotation) is Union:
            return Union[tuple([patch_pydantic_field_annotation(a) for a in get_args(annotation)])]
        elif get_origin(annotation) is List:
            return List[patch_pydantic_field_annotation(get_args(annotation)[0])]
        elif isinstance(annotation, type) and issubclass(annotation, BaseModel):
            return patch_pydantic_model(annotation)
        else:
            return annotation

    def patch_pydantic_model(model: Type[BaseModel]) -> Type[BaseModel]:
        # Copy the fields from the base class
        fields = model.model_fields.copy()
        new_fields: Dict[str, Tuple[AnnotationType, Any]] = {
            field_name: (patch_pydantic_field_annotation(field.annotation), field)
            for field_name, field in fields.items()
        }
        # Create a new model with the subset of fields
        return create_model(f"{model.__name__}_patched", __base__=BaseModel, **new_fields)

    return patch_pydantic_model(response_format)


def jsonschema_to_model(schema: Dict) -> Type[BaseModel]:
    """Generate a Pydantic Model from a json schema.

    Args:
    schema: Source json schema to create Pydantic model from

    Returns:
    The newly created and loaded Pydantic class
    """
    class_name = schema.get("title", "Model")
    json_schema = json.dumps(schema)
    model = jsonschemastr_to_model(json_schema, class_name)
    return model


@lru_cache(maxsize=16)
def jsonschemastr_to_model(json_schema: str, class_name: str) -> Type[BaseModel]:
    """Generate a Pydantic Model from a json schema string.

    Note (spillai): We use this to cache the generated models to avoid recompiling them.

    Args:
    schema: Source json schema to create Pydantic model from

    Returns:
    The newly created and loaded Pydantic class
    """
    # Ref: https://github.com/koxudaxi/datamodel-code-generator/issues/278
    with TemporaryDirectory() as tmp_dirname:
        tmp_dir = Path(tmp_dirname)
        tmp_path = Path(tmp_dir / "tempmodel.py")
        generate(
            json_schema,
            input_file_type=InputFileType.JsonSchema,
            class_name=class_name,
            output=tmp_path,
            output_model_type=DataModelType.PydanticV2BaseModel,
        )
        spec = importlib.util.spec_from_file_location("models", str(tmp_path))
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            return getattr(module, class_name)
        raise ImportError("Failed to import generated model")  # pragma: no cover
