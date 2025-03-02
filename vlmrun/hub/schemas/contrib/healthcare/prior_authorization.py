from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from enum import Enum

class ServiceType(str, Enum):
    INPATIENT = "Inpatient"
    OUTPATIENT = "Outpatient"
    HOME_HEALTH = "Home Health"
    DME = "DME"
    PHARMACY = "Pharmacy"
    OTHER = "Other"

class PriorityType(str, Enum):
    ROUTINE = "Routine"
    URGENT = "Urgent"
    EXPEDITED = "Expedited"

class MemberInformation(BaseModel):
    member_id: str = Field(..., description="Member's insurance ID number")
    first_name: str
    last_name: str
    date_of_birth: date
    phone: str

class RequestingProvider(BaseModel):
    npi: str = Field(..., description="National Provider Identifier")
    tax_id: str
    provider_name: str
    contact_name: str
    phone: str
    fax: Optional[str]
    address: str
    city: str
    state: str
    zip_code: str

class ServicingProvider(BaseModel):
    same_as_requesting: bool = Field(False, description="Check if same as requesting provider")
    npi: Optional[str] = Field(None, description="National Provider Identifier")
    tax_id: Optional[str]
    provider_name: Optional[str]
    contact_name: Optional[str]
    phone: Optional[str]
    fax: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

class ServiceInformation(BaseModel):
    service_type: ServiceType
    priority_type: PriorityType
    start_date: date
    end_date: Optional[date]
    diagnosis_codes: List[str] = Field(..., description="ICD-10 diagnosis codes")
    cpt_hcpcs_codes: List[str] = Field(..., description="CPT/HCPCS codes")
    number_of_visits: Optional[int]
    frequency: Optional[str]
    clinical_reason: str = Field(..., description="Clinical reason for request")
    supporting_documents: List[str] = Field([], description="List of attached supporting documents")

class PriorAuthorization(BaseModel):
    member: MemberInformation
    requesting_provider: RequestingProvider
    servicing_provider: ServicingProvider
    service_info: ServiceInformation
    submission_date: date = Field(..., description="Date of submission")