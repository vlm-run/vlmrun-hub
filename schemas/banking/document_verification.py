from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class DocumentType(str, Enum):
    passport = "passport"
    drivers_license = "drivers_license"
    national_id = "national_id"
    utility_bill = "utility_bill"
    bank_statement = "bank_statement"
    tax_return = "tax_return"
    payslip = "payslip"
    social_security_card = "social_security_card"
    birth_certificate = "birth_certificate"
    residence_permit = "residence_permit"
    other = "other"


class DocumentVerificationStatus(str, Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"
    requires_review = "requires_review"


class UserData(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user.")
    full_name: str = Field(..., description="Full name of the user.")
    date_of_birth: Optional[date] = Field(None, description="User's date of birth.")
    nationality: Optional[str] = Field(None, description="User's nationality.")
    address: Optional[str] = Field(None, description="User's residential address.")


class DocumentVerification(BaseModel):
    document_type: DocumentType = Field(
        ..., description="Type of the document being verified"
    )
    document_number: str = Field(
        ..., description="Unique identifier or number on the document"
    )
    issuing_authority: str = Field(
        ..., description="Name of the authority that issued the document"
    )
    issue_date: str = Field(..., description="Date when the document was issued")
    expiry_date: date | None = Field(
        None, description="Expiration date of the document, if applicable"
    )
    verification_status: DocumentVerificationStatus = Field(
        default=DocumentVerificationStatus.pending,
        description="Current status of the document verification process",
    )
    verification_notes: str | None = Field(
        None, description="Additional notes or comments about the verification"
    )
    is_original: bool = Field(
        ..., description="Indicates if the document is original or a copy"
    )
    user_data: UserData = Field(
        ..., description="User data associated with the document verification process."
    )
