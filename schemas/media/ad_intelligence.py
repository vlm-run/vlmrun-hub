from typing import List, Optional
from pydantic import BaseModel, Field

class DetectedObject(BaseModel):
    class_name: str | None = Field(None, description="Class name of the detected object, e.g., 'shoe', 'car'.")
    bounding_box: list[int] | None = Field(None, description="Bounding box coordinates for the object in [x1, y1, x2, y2] format.")

class AdIntelligence(BaseModel):
    brands_detected: list[str] = Field(..., description="List of brands identified in the ad.")
    logos_detected: list[str] = Field(..., description="List of logos identified in the ad.")
    text_detected: str = Field(..., description="Text extracted from the ad.")
    price: str | None = Field(None, description="Price detected in the ad.")
    coupon_code: str | None = Field(None, description="Coupon code, if detected.")
    contact_information: str | None = Field(None, description="Contact information, if detected.")
    website_url: str | None = Field(None, description="Website URL, if detected.")
    engagement_metrics: dict | None = Field(None, description="Optional key engagement metrics (e.g., likes, shares, views).")
    industry: str | None = Field(None, description="Industry/category the ad belongs to (e.g., Automotive, Fashion).")
    objects: list[DetectedObject] | None = Field(None, description="List of objects detected in the ad.")
    tags: list[str] | None = Field(None, description="Tags describing the advertisement's themes or focus.")