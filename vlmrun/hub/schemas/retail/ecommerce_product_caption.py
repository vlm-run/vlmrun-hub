"""Schema for retail product captions."""
from pydantic import BaseModel, Field


class RetailEcommerceProductCaption(BaseModel):
    description: str = Field(
        ...,
        description="A 2-sentence general visual description of the product embedded as an image.",
    )
    rating: int = Field(
        ...,
        description="The visual rating or appeal of the product between 0 and 100.",
        ge=0,
        le=100,
    )
    name: str = Field(..., description="The name of the product.")
    brand: str = Field(..., description="The brand of the product.")
    category: str = Field(..., description="The category of the product, e.g. 'Electronics / E-readers'.")
    price: str = Field(..., description="The price of the product.")
    color: str = Field(..., description="The color of the product.")

    class Config:
        schema_extra = {
            "example": {
                "description": "The Kindle Paperwhite e-reader features a sleek black design with a 6.8-inch glare-free display. The device appears slim and lightweight with a modern, minimalist aesthetic.",
                "rating": 95,
                "name": "Kindle Paperwhite (8 GB)",
                "brand": "Amazon",
                "category": "Electronics / E-readers / Kindle",
                "price": "$139.99",
                "color": "Black"
            }
        }
