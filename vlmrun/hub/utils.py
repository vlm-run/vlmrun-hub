from typing import Any, Dict, List, Tuple, Type, Union, get_args, get_origin

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
