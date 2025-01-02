from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class DocumentType(str, Enum):
    passport = "passport"
    drivers_license = "drivers-license"
    national_id = "national-id"
    utility_bill = "utility-bill"
    bank_statement = "bank-statement"
    tax_return = "tax-return"
    payslip = "payslip"
    social_security_card = "social-security-card"
    birth_certificate = "birth-certificate"
    residence_permit = "residence-permit"
    other = "other"


class DocumentVerificationStatus(str, Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"
    requires_review = "requires-review"


class UserData(BaseModel):
    user_id: str | None = Field(None, description="Unique identifier for the user.")
    full_name: str | None = Field(None, description="Full name of the user.")
    date_of_birth: date | None = Field(None, description="User's date of birth.")
    nationality: str | None = Field(None, description="User's nationality.")
    address: str | None = Field(None, description="User's residential address.")


class DocumentVerification(BaseModel):
    document_type: DocumentType | None = Field(None, description="Type of the document being verified")
    document_number: str | None = Field(None, description="Unique identifier or number on the document")
    issuing_authority: str | None = Field(None, description="Name of the authority that issued the document")
    issue_date: date | None = Field(None, description="Date when the document was issued")
    expiry_date: date | None = Field(None, description="Expiration date of the document, if applicable")
    verification_status: DocumentVerificationStatus | None = Field(
        None, description="Current status of the document verification process"
    )
    verification_notes: str | None = Field(None, description="Additional notes or comments about the verification")
    is_original: bool | None = Field(None, description="Indicates if the document is original or a copy")
    user_data: UserData | None = Field(None, description="User data associated with the document verification process.")
