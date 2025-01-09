"""Schema for retail product captions."""
from pydantic import BaseModel, Field


class RetailEcommerceProductCaption(BaseModel):
    """Schema for extracting product information from retail e-commerce product images."""

    description: str = Field(
        ...,
        description="A detailed 2-sentence visual description of the product's appearance, features, and packaging as shown in the image.",
    )
    rating: int = Field(
        ...,
        description="The visual rating or appeal of the product between 0 and 100, based on image quality and presentation.",
        ge=0,
        le=100,
    )
    name: str = Field(
        ..., 
        description="The complete product name including model or version information if visible in the image.",
    )
    brand: str = Field(
        ..., 
        description="The manufacturer or brand name of the product as shown in the image or product packaging.",
    )
    category: str = Field(
        ..., 
        description="The hierarchical product category using forward slashes, e.g. 'Electronics / E-readers / Kindle'.",
    )
    price: str = Field(
        ..., 
        description="The product price as displayed, including currency symbol and any decimal places.",
    )
    color: str = Field(
        ..., 
        description="The primary color or color scheme of the product as visible in the image.",
    )

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
