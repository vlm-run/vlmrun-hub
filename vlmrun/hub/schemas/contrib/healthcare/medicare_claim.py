from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from enum import Enum

class InsuranceType(str, Enum):
    MEDICARE = "medicare"
    MEDICAID = "medicaid" 
    TRICARE = "tricare"
    CHAMPVA = "champva"
    GROUP_HEALTH = "group_health"
    FECA = "feca"
    OTHER = "other"

class ServiceLine(BaseModel):
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    place_of_service: Optional[str] = Field(None, min_length=2, max_length=2)
    cpt_hcpcs_code: Optional[str] = None
    modifiers: Optional[List[str]] = Field(None, max_items=4)  # Replaces individual modifier fields
    charges: Optional[float] = None
    days_or_units: Optional[int] = None
    epsdt: Optional[bool] = None
    rendering_provider: Optional[str] = None

class MedicareClaim(BaseModel):
    # Insurance Type
    insurance_type: Optional[InsuranceType] = None
    
    # Patient Information
    patient_name: Optional[str] = None
    patient_birth_date: Optional[date] = None
    patient_gender: Optional[str] = None
    patient_address: Optional[str] = None
    patient_city: Optional[str] = None
    patient_state: Optional[str] = Field(None, max_length=2)
    patient_zip: Optional[str] = None
    patient_phone: Optional[str] = None
    patient_relationship_to_insured: Optional[str] = None
    
    # Insured Information
    insured_name: Optional[str] = None
    insured_id: Optional[str] = None
    insured_address: Optional[str] = None
    insured_city: Optional[str] = None
    insured_state: Optional[str] = Field(None, max_length=2)
    insured_zip: Optional[str] = None
    insured_phone: Optional[str] = None
    
    # Condition Information
    employment_related: Optional[bool] = None
    auto_accident: Optional[bool] = None
    auto_accident_state: Optional[str] = Field(None, max_length=2)
    other_accident: Optional[bool] = None
    
    # Diagnosis Codes (ICD-10)
    diagnosis_codes: Optional[List[str]] = None
    
    # Service Lines
    service_lines: Optional[List[ServiceLine]] = None
    
    # Provider Information
    billing_provider_name: Optional[str] = None
    billing_provider_npi: Optional[str] = None
    billing_provider_tax_id: Optional[str] = None
    billing_provider_address: Optional[str] = None
    billing_provider_city: Optional[str] = None
    billing_provider_state: Optional[str] = Field(None, max_length=2)
    billing_provider_zip: Optional[str] = None
    billing_provider_phone: Optional[str] = None
    
    # Additional Information
    total_charges: Optional[float] = None
    amount_paid: Optional[float] = None
    accept_assignment: Optional[bool] = None
    signature_on_file: Optional[bool] = None
    date_of_current_illness: Optional[date] = None
    referring_provider_npi: Optional[str] = None
    prior_authorization_number: Optional[str] = None
