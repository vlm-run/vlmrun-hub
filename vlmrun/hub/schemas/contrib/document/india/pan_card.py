from typing import List, Optional

from pydantic import BaseModel, Field


class PANCard(BaseModel):
    """PAN (Permanent Account Number) Card schema for extracting information from India's tax identity document."""

    # Core PAN information
    pan_number: str = Field(..., description="10-character alphanumeric PAN (Permanent Account Number)")
    name: str = Field(..., description="Full name of the PAN card holder")
    father_name: Optional[str] = Field(None, description="Father's name as printed on the PAN card")
    date_of_birth: Optional[str] = Field(None, description="Date of birth of the PAN card holder")

    # Security features and visual elements
    has_photo: Optional[bool] = Field(None, description="Whether the card has a photo of the holder")
    has_signature: Optional[bool] = Field(None, description="Whether the card has a signature")
    has_income_tax_logo: Optional[bool] = Field(None, description="Whether the Income Tax Department logo is visible")
    has_govt_of_india_text: Optional[bool] = Field(
        None, description="Whether 'GOVT. OF INDIA' or similar text is visible"
    )

    # Additional information
    languages: List[str] = Field(
        default_factory=list,
        description="Languages in which the card information is printed (e.g., Hindi, English, etc.)",
    )
