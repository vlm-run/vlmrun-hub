from dataclasses import dataclass
from pathlib import Path
from typing import List, Type, Union

from PIL import Image
from pydantic import BaseModel
from typing_extensions import TypeAlias

from vlmrun.common.pdf import pdf_images
from vlmrun.common.utils import download_artifact, remote_image
from vlmrun.hub.constants import (
    VLMRUN_HUB_CATALOG_PATH,
    VLMRUN_HUB_CONTRIB_CATALOG_PATH,
)
from vlmrun.hub.registry import SchemaCatalogYaml

ImageType: TypeAlias = Union[str, Path]
PDFType: TypeAlias = Union[str, Path]


@dataclass
class HubSample:
    domain: str
    """The domain / identifier of the sample"""
    response_model: Type[BaseModel]
    """The response model to use for the sample"""
    prompt: str
    """The prompt to use for the sample"""
    data: str
    """The images or image URLs associated with the sample"""

    def _handle_image(self, image: ImageType) -> Image.Image:
        if isinstance(image, str):
            if image.startswith("http"):
                return remote_image(image)
            return Image.open(image)
        else:
            raise ValueError(f"Invalid image type: {type(image)}")

    def _handle_pdf(self, url: PDFType) -> List[Image.Image]:
        if url.endswith(".pdf"):
            if url.startswith("http"):
                path: Path = download_artifact(url, format="file")
            else:
                path: Path = Path(str(url))
            return [p.image for p in pdf_images(path, dpi=72)]
        else:
            raise ValueError(f"Invalid PDF type: {type(url)}")

    def _handle_url(self, url: str) -> List[Image.Image]:
        if url.endswith(".pdf"):
            return self._handle_pdf(url)
        elif url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".png") or url.endswith(".webp"):
            return [self._handle_image(url)]
        else:
            raise ValueError(f"Invalid data extension: {url}")

    @property
    def images(self) -> List[Image.Image]:
        return self._handle_url(self.data)


catalog = SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CATALOG_PATH)
VLMRUN_HUB_DATASET = {
    schema.domain: HubSample(
        domain=schema.domain,
        response_model=schema.schema_class,
        prompt=schema.prompt,
        data=schema.sample_data,
    )
    for schema in catalog.schemas
} | {
    schema.domain: HubSample(
        domain=schema.domain,
        response_model=schema.schema_class,
        prompt=schema.prompt,
        data=schema.sample_data,
    )
    for schema in SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CONTRIB_CATALOG_PATH).schemas
}
