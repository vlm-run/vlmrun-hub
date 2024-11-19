from pydantic import BaseModel, Field



class ProductImage(BaseModel):
    """Details about a product image including URL and display properties"""

    alt_text: str | None = Field(None, description="Alternative text for accessibility")
    is_primary: bool | None = Field(None, description="Indicates if this is the main display image")
    dimensions: dict[str, int] | None = Field(None, description="Image dimensions in pixels (width, height)")


class ProductFeature(BaseModel):
    """Key features and specifications of the product"""

    name: str | None = Field(None, description="Name of the feature")
    description: str | None = Field(None, description="Detailed description of the feature")
    is_key_feature: bool | None = Field(None, description="Indicates if it's a key selling point")


class StyleDescriptor(BaseModel):
    """Style and design characteristics of the product"""

    category: str | None = Field(None, description="Style category (e.g., Modern, Casual, Formal)")
    details: str | None = Field(None, description="Additional style details")
    color_palette: list[str] | None = Field(None, description="List of colors used in the product")


class KeyBenefit(BaseModel):
    """Core benefits and value propositions of the product"""

    benefit: str | None = Field(None, description="Primary benefit statement")
    description: str | None = Field(None, description="Detailed explanation of the benefit")
    impact_score: int | None = Field(None, description="Priority score (1-10) for the benefit")


class PricingInfo(BaseModel):
    """Pricing and availability information"""

    currency: str | None = Field(None, description="Three-letter currency code (e.g., USD)")
    price: float | None = Field(None, description="Current selling price")
    discount: float | None = Field(None, description="Discount amount if applicable")
    original_price: float | None = Field(None, description="Price before any discounts")
    availability: str | None = Field(None, description="Current stock status")


class Review(BaseModel):
    """Customer review and rating information"""

    rating: float | None = Field(None, description="Average rating out of 5")
    review_count: int | None = Field(None, description="Total number of customer reviews")
    top_review: str | None = Field(None, description="Featured customer review")


class SEOInfo(BaseModel):
    """Search engine optimization metadata"""

    keywords: list[str] | None = Field(None, description="SEO keywords for search visibility")
    meta_description: str | None = Field(None, description="SEO-optimized product description")


class ShippingInfo(BaseModel):
    """Shipping and delivery specifications"""

    weight: float | None = Field(None, description="Product weight in kilograms")
    dimensions: dict[str, float] | None = Field(None, description="Product dimensions in centimeters")
    delivery_estimate: str | None = Field(None, description="Estimated delivery timeframe")
    shipping_cost: float | None = Field(None, description="Standard shipping cost")


class ProductCategory(BaseModel):
    """Product categorization information"""

    main_category: str | None = Field(None, description="Primary product category")
    sub_categories: list[str] | None = Field(None, description="List of subcategories")


class EcommerceProductCaption(BaseModel):
    """Complete product information for e-commerce listing"""

    product_id: str | None = Field(None, description="Unique identifier for the product")
    product_name: str | None = Field(None, description="Name of the product")
    product_images: list[ProductImage] | None = Field(None, description="List of product images")
    product_features: list[ProductFeature] | None = Field(None, description="List of product features")
    style_descriptors: list[StyleDescriptor] | None = Field(None, description="Style and design information")
    key_benefits: list[KeyBenefit] | None = Field(None, description="Core product benefits")
    pricing_info: PricingInfo | None = Field(None, description="Pricing and availability details")
    reviews: Review | None = Field(None, description="Customer review information")
    seo_info: SEOInfo | None = Field(None, description="SEO metadata")
    shipping_info: ShippingInfo | None = Field(None, description="Shipping specifications")
    product_category: ProductCategory | None = Field(None, description="Product categorization")
    generated_caption: str | None = Field(None, description="AI-generated marketing caption")
    additional_info: dict[str, str] | None = Field(None, description="Additional product metadata")