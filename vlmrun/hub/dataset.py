from dataclasses import dataclass
from pathlib import Path
from typing import Type

from PIL import Image
from pydantic import BaseModel

from vlmrun.hub.schemas.document.invoice import Invoice
from vlmrun.hub.utils import remote_image


@dataclass
class HubSample:
    domain: str
    """The domain / identifier of the sample"""
    response_model: Type[BaseModel]
    """The response model to use for the sample"""
    prompt: str
    """The prompt to use for the sample"""
    inputs: list[str | Image.Image | Path]
    """The images or image URLs associated with the sample"""

    def _handle_image(self, image: str | Image.Image | Path) -> Image.Image:
        if isinstance(image, Path):
            return Image.open(image)
        elif isinstance(image, str) and image.startswith("http"):
            return remote_image(image)
        return image

    @property
    def images(self) -> list[Image.Image]:
        return [self._handle_image(image) for image in self.inputs]


VLMRUN_HUB_DATASET = {
    "document.invoice": HubSample(
        domain="document.invoice",
        response_model=Invoice,
        prompt="Extract the invoice in JSON format.",
        inputs=[
            "https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.invoice-extraction/invoice_1.jpg",
        ],
    ),
}
