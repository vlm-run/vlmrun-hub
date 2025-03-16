from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class USLicensePlate(BaseModel):
    """Schema for extracting standardized information from US vehicle license plates."""

    plate_number: str = Field(..., description="The alphanumeric license plate number")
    state: str = Field(..., description="State that issued the license plate")
    expiration_date: Optional[date] = Field(None, description="Expiration date of the license plate, if visible")
    issue_date: Optional[date] = Field(None, description="Issue date of the license plate, if available")
    plate_type: Optional[str] = Field(None, description="Type of license plate (Standard, Specialty, Commercial, etc.)")
    color_scheme: Optional[str] = Field(None, description="Color scheme or background details of the plate")