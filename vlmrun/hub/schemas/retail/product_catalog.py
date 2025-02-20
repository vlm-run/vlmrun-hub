from typing import Literal

from pydantic import BaseModel, Field


class ProductCatalog(BaseModel):
    description: str = Field(
        ..., description="A 2-sentence general visual description of the product embedded as an image."
    )
    category: str = Field(
        ..., description="One or two-word category of the product (i.e, apparel, accessories, footwear etc)."
    )
    season: Literal["fall", "spring", "summer", "winter"] = Field(
        ..., description="The season the product is intended for."
    )
    gender: Literal["men", "women", "boys", "girls"] = Field(
        ..., description="Gender or audience the product is intended for."
    )
