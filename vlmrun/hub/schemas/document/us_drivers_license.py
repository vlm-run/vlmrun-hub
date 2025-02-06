from datetime import date
from enum import Enum
from typing import Optional

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


class Address(BaseModel):
    street: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    state: str = Field(..., description="Two-letter state code")
    zip_code: str = Field(..., description="ZIP code")


class USDriversLicense(BaseModel):
    issuing_state: str = Field(..., description="Two-letter code of the issuing state")
    license_number: str = Field(..., description="Driver's license number")

    full_name: str = Field(..., description="Full name of the license holder")
    first_name: Optional[str] = Field(None, description="First name of the license holder")
    middle_name: Optional[str] = Field(None, description="Middle name of the license holder")
    last_name: Optional[str] = Field(None, description="Last name of the license holder")

    address: Address = Field(..., description="Address of the license holder")

    date_of_birth: date = Field(..., description="Date of birth")
    gender: Gender = Field(..., description="Gender of the license holder")

    height: Optional[str] = Field(None, description="Height of the license holder in the format X'Y\" (e.g. 5'7\")")
    weight: Optional[float] = Field(None, description="Weight (in lbs) of the license holder (e.g. 150.5 lbs)")
    eye_color: Optional[str] = Field(None, description="Eye color code of the license holder")
    hair_color: Optional[str] = Field(None, description="Hair color code of the license holder")

    issue_date: date = Field(..., description="Date the license was issued")
    expiration_date: date = Field(..., description="Expiration date of the license")

    license_class: LicenseClass = Field(..., description="Class of the driver's license")

    donor: Optional[bool] = Field(None, description="Indicates if the holder is an organ donor")
    veteran: Optional[bool] = Field(None, description="Indicates if the holder is a veteran")
