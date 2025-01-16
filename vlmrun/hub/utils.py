from typing import Type, Union, get_origin

from pydantic import BaseModel, create_model

from vlmrun.common.image import encode_image  # noqa: F401
from vlmrun.common.utils import remote_image  # noqa: F401


def patch_response_format(response_format: Type[BaseModel]) -> Type[BaseModel]:
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
    from typing import List

    def patch_pydantic_field_annotation(annotation):
        if annotation in [date, datetime, time, timedelta]:
            return str
        elif get_origin(annotation) is Union:
            return Union[tuple([patch_pydantic_field_annotation(a) for a in annotation.__args__])]
        elif get_origin(annotation) is List:
            return List[patch_pydantic_field_annotation(annotation.__args__[0])]
        elif isinstance(annotation, type) and issubclass(annotation, BaseModel):
            return patch_pydantic_model(annotation)
        else:
            return annotation

    def patch_pydantic_model(model: Type[BaseModel]) -> Type[BaseModel]:
        # Copy the fields from the base class
        fields = model.model_fields.copy()
        new_fields = {
            field_name: (patch_pydantic_field_annotation(field.annotation), field)
            for field_name, field in fields.items()
        }
        # Create a new model with the subset of fields
        return create_model(f"{model.__name__}_patched", __base__=BaseModel, **new_fields)

    return patch_pydantic_model(response_format)
