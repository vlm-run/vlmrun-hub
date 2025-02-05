from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class USPassport(BaseModel):
    """US Passport schema for extracting information from passport documents."""

    family_name: str = Field(..., description="Family name (surname) of the passport holder")
    given_names: str = Field(..., description="Given names (first and middle names) of the passport holder")
    document_id: str = Field(..., description="Passport document identification number")
    expiration_date: date = Field(..., description="Expiration date of the passport")
    date_of_birth: date = Field(..., description="Date of birth of the passport holder")
    issue_date: date = Field(..., description="Issue date of the passport")
    mrz_code: str = Field(..., description="Machine Readable Zone (MRZ) code from the passport")

    # Additional optional fields that might be present
    nationality: Optional[str] = Field(None, description="Nationality of the passport holder")
    place_of_birth: Optional[str] = Field(None, description="Place of birth of the passport holder")
    sex: Optional[str] = Field(None, description="Sex of the passport holder (M/F)")
    authority: Optional[str] = Field(None, description="Issuing authority of the passport")
    place_of_issue: Optional[str] = Field(None, description="Place where the passport was issued")
