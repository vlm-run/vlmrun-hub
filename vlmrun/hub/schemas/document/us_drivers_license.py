from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "X"


class LicenseClass(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    M = "M"


class Restriction(BaseModel):
    code: str = Field(..., description="Restriction code")
    description: str | None = Field(None, description="Description of the restriction")


class Endorsement(BaseModel):
    code: str = Field(..., description="Endorsement code")
    description: str | None = Field(None, description="Description of the endorsement")


class Address(BaseModel):
    street: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    state: str = Field(..., description="Two-letter state code", max_length=2)
    zip_code: str = Field(..., description="ZIP code", min_length=5, max_length=10)


class USDriversLicense(BaseModel):
    document_type: str = Field("DRIVER LICENSE", description="Type of document")
    issuing_state: str = Field(..., description="Two-letter code of the issuing state", max_length=2)
    license_number: str = Field(..., description="Driver's license number")

    full_name: str = Field(..., description="Full name of the license holder")
    first_name: str | None = Field(None, description="First name of the license holder")
    middle_name: str | None = Field(None, description="Middle name of the license holder")
    last_name: str | None = Field(None, description="Last name of the license holder")

    address: Address = Field(..., description="Address of the license holder")

    date_of_birth: date = Field(..., description="Date of birth")
    gender: Gender = Field(..., description="Gender of the license holder")

    height: str | None = Field(None, description="Height of the license holder")
    weight: str | None = Field(None, description="Weight of the license holder")
    eye_color: str | None = Field(None, description="Eye color of the license holder")
    hair_color: str | None = Field(None, description="Hair color of the license holder")

    issue_date: date = Field(..., description="Date the license was issued")
    expiration_date: date = Field(..., description="Expiration date of the license")

    license_class: LicenseClass = Field(..., description="Class of the driver's license")
    restrictions: List[Restriction] | None = Field(None, description="List of license restrictions")
    endorsements: List[Endorsement] | None = Field(None, description="List of license endorsements")

    donor: bool | None = Field(None, description="Indicates if the holder is an organ donor")
    veteran: bool | None = Field(None, description="Indicates if the holder is a veteran")

    document_discriminator: str | None = Field(None, description="Unique identifier for the document")
    inventory_control_number: str | None = Field(None, description="Inventory control number")
    audit_number: str | None = Field(None, description="Audit number for the document")

    pdf417_barcode: str | None = Field(None, description="Data from the PDF417 barcode if available")

    others: dict | None = Field(None, description="Additional fields not captured in the standard model")
