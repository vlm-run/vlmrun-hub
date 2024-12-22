from dataclasses import dataclass
from pathlib import Path
from PIL import Image
from vlmrun.hub.utils import remote_image
from pydantic import BaseModel
from typing import Type

from vlmrun import hub


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
        response_model=hub.schemas.document.invoice.Invoice,
        prompt="Extract the invoice in JSON format.",
        inputs=[
            "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg",
        ],
    ),
}
