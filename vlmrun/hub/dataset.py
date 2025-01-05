from dataclasses import dataclass
from pathlib import Path
from typing import Type

from PIL import Image
from pydantic import BaseModel

from vlmrun.hub.utils import remote_image
from vlmrun.hub.constants import VLMRUN_HUB_CATALOG_PATH
from vlmrun.hub.registry import SchemaCatalogYaml


@dataclass
class HubSample:
    domain: str
    """The domain / identifier of the sample"""
    response_model: Type[BaseModel]
    """The response model to use for the sample"""
    prompt: str
    """The prompt to use for the sample"""
    data: str | Image.Image | Path
    """The images or image URLs associated with the sample"""

    def _handle_image(self, image: str | Image.Image | Path) -> Image.Image:
        if isinstance(image, Path):
            return Image.open(image)
        elif isinstance(image, str) and image.startswith("http"):
            return remote_image(image)
        elif isinstance(image, Image.Image):
            return image
        else:
            raise ValueError(f"Invalid image type: {type(image)}")

    @property
    def image(self) -> Image.Image:
        return self._handle_image(self.data)


catalog = SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CATALOG_PATH)
VLMRUN_HUB_DATASET = {
    schema.domain: HubSample(
        domain=schema.domain,
        response_model=schema.schema_class,
        prompt=schema.prompt,
        data=schema.sample_data,
    )
    for schema in catalog.schemas
}

