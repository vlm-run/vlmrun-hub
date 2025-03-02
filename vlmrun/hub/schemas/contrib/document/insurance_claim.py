from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ClaimStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in-progress"
    CLOSED = "closed"
    DENIED = "denied"
    APPROVED = "approved"


class ClaimType(str, Enum):
    AUTO = "auto"
    HOME = "home"
    COMMERCIAL_PROPERTY = "commercial-property"
    LIABILITY = "liability"
    OTHER = "other"


class PolicyHolderType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"


class PaymentMethod(str, Enum):
    BANK_TRANSFER = "bank-transfer"
    CHECK = "check"
    DIRECT_DEPOSIT = "direct-deposit"
    WIRE_TRANSFER = "wire-transfer"


class InvolvementType(str, Enum):
    AUTO = "auto"
    PROPERTY = "property"
    BODILY_INJURY = "bodily_injury"
    LIABILITY = "liability"
    WORKERS_COMP = "workers_comp"
    OTHER = "other"


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address (e.g., '123 Elm St Apt 4B')")
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State or province (e.g., 'CA', 'NY', 'TX')")
    zip_code: Optional[str] = Field(None, description="ZIP or postal code (e.g., '12345-6789')")


class ContactInfo(BaseModel):
    phone: Optional[str] = Field(None, description="Primary contact phone number")
    email: Optional[str] = Field(None, description="Primary contact email address")
    additional: Optional[str] = Field(None, description="Additional contact details (fax, secondary phone, etc.)")


class Party(BaseModel):
    name: Optional[str] = Field(None, description="Name of the individual or organization")
    address: Optional[Address] = Field(None, description="Physical address of the party")
    contact: Optional[ContactInfo] = Field(None, description="Contact details of the party")
    identifier: Optional[str] = Field(None, description="Unique identifier (e.g., SSN, Tax ID, registration number)")
    party_type: Optional[PolicyHolderType] = Field(None, description="Type of party: INDIVIDUAL or BUSINESS")


class Parties(BaseModel):
    insured: Optional[Party] = Field(None, description="The insured individual or entity")
    claimant: Optional[Party] = Field(None, description="The claimant (if different from the insured)")
    insurance_company: Optional[Party] = Field(None, description="The insurance company handling the claim")
    other_involved_parties: Optional[List[Party]] = Field(
        None, description="Other parties involved (e.g., at-fault driver)"
    )


class PolicyDetails(BaseModel):
    policy_number: Optional[str] = Field(None, description="Unique identifier for the policy")
    policy_holder_type: Optional[PolicyHolderType] = Field(
        None, description="Type of policyholder (individual or business)"
    )
    policy_type: Optional[str] = Field(None, description="Policy type (e.g., 'auto', 'home', 'commercial')")
    coverage_start_date: Optional[date] = Field(None, description="Coverage start date")
    coverage_end_date: Optional[date] = Field(None, description="Coverage end date")
    coverage_limit: Optional[float] = Field(None, description="Maximum coverage amount under the policy", ge=0)
    currency: Optional[str] = Field(
        None, description="Currency code (e.g., 'USD') for coverage amounts", pattern="^[A-Z]{3}$"
    )
    deductible: Optional[float] = Field(None, description="Policy deductible amount", ge=0)
    additional_coverage_details: Optional[str] = Field(
        None, description="Additional policy coverage details (exclusions, riders, etc.)"
    )


class CoverageItem(BaseModel):
    coverage_type: Optional[str] = Field(None, description="Type of coverage (e.g., 'collision', 'fire damage')")
    coverage_limit: Optional[float] = Field(None, description="Coverage limit for this item", ge=0)
    deductible: Optional[float] = Field(None, description="Deductible for this coverage item", ge=0)
    currency: Optional[str] = Field(
        None, description="Currency code for this coverage (e.g., 'USD')", pattern="^[A-Z]{3}$"
    )
    notes: Optional[str] = Field(None, description="Additional details about this coverage item")


class ClaimDetails(BaseModel):
    claim_number: Optional[str] = Field(None, description="Unique identifier for the claim")
    claim_type: Optional[ClaimType] = Field(
        None, description="Classification of the claim (auto, home, liability, etc.)"
    )
    claim_status: Optional[ClaimStatus] = Field(None, description="Current status of the claim")
    date_reported: Optional[date] = Field(None, description="Date when the claim was reported")
    loss_description: Optional[str] = Field(None, description="Brief description of the loss or incident")


class VehicleInfo(BaseModel):
    make: Optional[str] = Field(None, description="Vehicle make (e.g., 'Toyota')")
    model: Optional[str] = Field(None, description="Vehicle model (e.g., 'Camry')")
    year: Optional[int] = Field(None, description="Model year (e.g., 2025)")
    license_plate: Optional[str] = Field(None, description="License plate number")
    vin: Optional[str] = Field(None, description="Vehicle Identification Number (VIN)")


class Involvement(BaseModel):
    involvement_type: InvolvementType = Field(
        ..., description="Type of involvement (auto, property, bodily_injury, etc.)"
    )
    description: Optional[str] = Field(None, description="Description of the involvement")
    location: Optional[Address] = Field(None, description="Location related to this involvement")
    date_of_involvement: Optional[date] = Field(None, description="Date when this involvement occurred")
    time_of_involvement: Optional[datetime] = Field(None, description="Time when this involvement occurred")
    police_report_number: Optional[str] = Field(
        None, description="Police report number associated with this involvement"
    )
    vehicles_involved: Optional[List[VehicleInfo]] = Field(None, description="Vehicles involved (for auto claims)")
    traffic_violation_code: Optional[str] = Field(
        None, description="Traffic violation code (e.g., '101A') if applicable"
    )
    structural_damage_description: Optional[str] = Field(
        None, description="Description of structural damage (for property claims)"
    )
    inventory_loss_description: Optional[str] = Field(
        None, description="Description of lost or damaged inventory (if applicable)"
    )
    repair_cost_estimate: Optional[float] = Field(None, ge=0, description="Estimated cost for repairs or replacement")
    injury_description: Optional[str] = Field(None, description="Description of any injuries sustained")
    medical_expenses_estimate: Optional[float] = Field(None, ge=0, description="Estimated medical expenses, if any")
    additional_info: Optional[str] = Field(None, description="Additional information relevant to this involvement")


class IncidentDetails(BaseModel):
    incident_date: Optional[date] = Field(None, description="Date when the incident occurred")
    incident_time: Optional[datetime] = Field(None, description="Time when the incident occurred")
    incident_location: Optional[Address] = Field(None, description="Location where the incident took place")
    incident_description: Optional[str] = Field(None, description="Detailed narrative of the incident or loss event")
    police_report_number: Optional[str] = Field(None, description="Police report number, if available")
    fire_report_number: Optional[str] = Field(None, description="Fire department report number, if applicable")
    incident_involvements: Optional[List[Involvement]] = Field(
        None, description="List of involvement entries related to the incident"
    )


class Damages(BaseModel):
    property_damage_amount: Optional[float] = Field(None, description="Claimed amount for property damage", ge=0)
    bodily_injury_amount: Optional[float] = Field(None, description="Claimed amount for bodily injury", ge=0)
    other_damage_amount: Optional[float] = Field(None, description="Other claimed damages (e.g., lost wages)", ge=0)
    currency: Optional[str] = Field(
        None, description="Currency code for the damage amounts (e.g., 'USD')", pattern="^[A-Z]{3}$"
    )
    damage_details: Optional[str] = Field(None, description="Additional details or breakdown of damages claimed")


class Witness(BaseModel):
    name: Optional[str] = Field(None, description="Witness name")
    contact: Optional[ContactInfo] = Field(None, description="Witness contact information")
    statement: Optional[str] = Field(None, description="Witness statement or testimony")


class ClaimAdjuster(BaseModel):
    name: Optional[str] = Field(None, description="Name of the claim adjuster")
    contact: Optional[ContactInfo] = Field(None, description="Contact information for the adjuster")
    assigned_date: Optional[date] = Field(None, description="Date the adjuster was assigned")


class ClaimFinancials(BaseModel):
    reserve_amount: Optional[float] = Field(None, description="Reserve amount set aside for the claim", ge=0)
    settlement_amount: Optional[float] = Field(None, description="Settled or proposed settlement amount", ge=0)
    paid_amount: Optional[float] = Field(None, description="Amount already paid on the claim", ge=0)
    payment_method: Optional[PaymentMethod] = Field(None, description="Method of payment for settlement")
    currency: Optional[str] = Field(
        None, description="Currency code for payment amounts (e.g., 'USD')", pattern="^[A-Z]{3}$"
    )
    payment_date: Optional[date] = Field(None, description="Date when the payment was made")


class ClaimDocument(BaseModel):
    document_type: Optional[str] = Field(
        None, description="Type of document (e.g., 'police report', 'repair estimate', 'photos')"
    )
    reference_number: Optional[str] = Field(None, description="Document reference or identifier")
    notes: Optional[str] = Field(None, description="Additional details regarding the document")


class InsuranceClaim(BaseModel):
    parties: Parties = Field(
        ..., description="Details of the insured, claimant, insurance company, and other involved parties"
    )
    policy_details: Optional[PolicyDetails] = Field(None, description="Information regarding the insurance policy")
    claim_details: Optional[ClaimDetails] = Field(None, description="Basic information about the claim")
    incident_details: Optional[IncidentDetails] = Field(None, description="Details of the incident or loss event")
    coverage_items: Optional[List[CoverageItem]] = Field(
        None, description="Breakdown of coverage items relevant to the claim"
    )
    damages: Optional[Damages] = Field(None, description="Details of the damages or losses claimed")
    witnesses: Optional[List[Witness]] = Field(None, description="List of witnesses related to the incident")
    claim_adjuster: Optional[ClaimAdjuster] = Field(None, description="Information about the claim adjuster")
    financials: Optional[ClaimFinancials] = Field(
        None, description="Financial details including reserves, settlements, and payments"
    )
    claim_documents: Optional[List[ClaimDocument]] = Field(
        None, description="Supporting documents submitted with the claim"
    )
    notes: Optional[str] = Field(None, description="Additional free-text notes or remarks regarding the claim")
