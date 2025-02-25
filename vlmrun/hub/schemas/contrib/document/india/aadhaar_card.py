from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    """Address structure found on Aadhaar PVC cards."""

    full_address: str = Field(..., description="Complete address as printed on the card")
    pin_code: Optional[str] = Field(None, description="PIN code (postal code) extracted from the address")
    state: Optional[str] = Field(None, description="State extracted from the address")
    district: Optional[str] = Field(None, description="District extracted from the address")


class CardSide(Enum):
    FRONT = "front"
    BACK = "back"
    BOTH = "both"
    UNKNOWN = "unknown"


class AadhaarCard(BaseModel):
    """Aadhaar PVC Card schema for extracting information from India's national identity document."""

    # Metadata about the extraction
    detected_side: CardSide = Field(
        ..., description="Which side of the Aadhaar card is visible in the image (front/back/both/unknown)"
    )

    # Front side information
    aadhaar_number: Optional[str] = Field(
        None, description="12-digit unique Aadhaar identification number (may be partially masked)"
    )
    name: Optional[str] = Field(None, description="Full name of the Aadhaar card holder")
    date_of_birth: Optional[str] = Field(None, description="Date of birth of the Aadhaar card holder")
    gender: Optional[str] = Field(None, description="Gender of the Aadhaar card holder (Male/Female/Transgender)")

    # Back side information
    address: Optional[Address] = Field(None, description="Address details as printed on the back of the card")

    # Security features and other elements
    has_photo: Optional[bool] = Field(None, description="Whether the card has a photo of the holder (front side)")
    has_qr_code: Optional[bool] = Field(None, description="Whether the card has a QR code")
    has_emblem: Optional[bool] = Field(None, description="Whether the card has the Government of India emblem")
    has_uidai_logo: Optional[bool] = Field(None, description="Whether the UIDAI logo is visible")

    # Additional information
    issue_date: Optional[str] = Field(None, description="Date of issue if visible on the card")
    print_date: Optional[str] = Field(None, description="Date when the PVC card was printed, if visible")

    # Language information
    languages: List[str] = Field(
        default_factory=list,
        description="Languages in which the card information is printed (e.g., Hindi, English, etc.)",
    )
