from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field

class HealthInformation(BaseModel):
    full_disclosure: Optional[bool] = Field(
        default=None,
        description="Indicates if the full health record is disclosed."
    )
    excluded_information: Optional[List[str]] = Field(
        default=None,
        description="Types of health records excluded from disclosure."
    )
    other_exclusions: Optional[List[str]] = Field(
        default=None,
        description="Additional exclusions specified by the patient."
    )
    disclosure_format: Optional[str] = Field(
        default=None,
        description="The preferred format for disclosing the health records."
    )


class Recipient(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="Name of the recipient."
    )
    organization: Optional[str] = Field(
        default=None,
        description="Organization name if applicable."
    )
    address: Optional[str] = Field(
        default=None,
        description="Recipient's address."
    )


class AuthorizationDuration(BaseModel):
    start_date: Optional[date] = Field(
        default=None,
        description="Start date of authorization."
    )
    end_date: Optional[date] = Field(
        default=None,
        description="End date of authorization."
    )
    all_time: Optional[bool] = Field(
        default=None,
        description="Indicates if authorization applies to all past, present, and future periods."
    )
    event_based: Optional[str] = Field(
        default=None,
        description="Event upon which authorization expires."
    )


class RevocationContact(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="Name of person handling revocation."
    )
    organization: Optional[str] = Field(
        default=None,
        description="Organization responsible for processing revocation."
    )
    address: Optional[str] = Field(
        default=None,
        description="Address for sending revocation requests."
    )


class RevocationDetails(BaseModel):
    revocation_contact: Optional[RevocationContact] = Field(
        default=None,
        description="Details on how the authorization can be revoked."
    )


class LegalRepresentative(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="Name of the legal representative."
    )
    signature: Optional[str] = Field(
        default=None,
        description="Signature of the legal representative."
    )
    authority_description: Optional[str] = Field(
        default=None,
        description="Description of the legal authority under which they are signing."
    )


class Signature(BaseModel):
    signed_by: Optional[str] = Field(
        default=None,
        description="Name of the individual signing the form."
    )
    is_signed: Optional[bool] = Field(
        default=None,
        description="Whether the form has been signed."
    )
    date_signed: Optional[date] = Field(
        default=None,
        description="Date the form was signed."
    )
    legal_representative: Optional[LegalRepresentative] = Field(
        default=None,
        description="Details if signed by a legal representative."
    )


class HIPAARelease(BaseModel):
    """HIPAA Release Form for authorizing disclosure of health information."""
    
    patient_name: Optional[str] = Field(
        default=None,
        description="Full name of the individual authorizing the release."
    )
    authorized_entity: Optional[str] = Field(
        default=None,
        description="Name of the entity or individual authorized to share information."
    )
    health_information: Optional[HealthInformation] = Field(
        default=None,
        description="Details of the health records to be disclosed."
    )
    reason_for_disclosure: Optional[str] = Field(
        default=None,
        description="Reason for sharing the health information."
    )
    recipient: Optional[Recipient] = Field(
        default=None,
        description="Details of the recipient authorized to receive health information."
    )
    authorization_duration: Optional[AuthorizationDuration] = Field(
        default=None,
        description="Duration of authorization for information disclosure."
    )
    revocation_details: Optional[RevocationDetails] = Field(
        default=None,
        description="Details on how the authorization can be revoked."
    )
    signature: Optional[Signature] = Field(
        default=None,
        description="Signature and authorization details."
    )
