from typing import Optional

from pydantic import BaseModel, Field


class ProviderService(BaseModel):
    provider_service_number: Optional[str] = Field(None, description="Provider service number.")
    precertification_number: Optional[str] = Field(None, description="Precertification number.")


class MemberInformation(BaseModel):
    member_name: str = Field(..., description="Name of the member.")
    member_id: Optional[str] = Field(None, description="Member ID.")
    group_number: Optional[str] = Field(None, description="Group number.")


class PharmacyPlan(BaseModel):
    rx_bin: Optional[str] = Field(None, description="Rx bin.")
    rx_pcn: Optional[str] = Field(None, description="Rx pcn.")
    rx_grp: Optional[str] = Field(None, description="Rx grp.")
    pharmacy_help_desk: Optional[str] = Field(None, description="Pharmacy help desk.")


class InsuranceProvider(BaseModel):
    provider_name: Optional[str] = Field(None, description="Provider name.")
    network: Optional[str] = Field(None, description="Network.")


class Coverage(BaseModel):
    office_visit: Optional[str] = Field(None, description="Office visit.")
    specialist_visit: Optional[str] = Field(None, description="Specialist visit.")
    urgent_care: Optional[str] = Field(None, description="Urgent care.")
    emergency_room: Optional[str] = Field(None, description="Emergency room.")
    inpatient_hospital: Optional[str] = Field(None, description="Inpatient hospital.")


class MedicalInsuranceCard(BaseModel):
    provider_service: Optional[ProviderService] = Field(None, description="Provider service information.")
    member_information: Optional[MemberInformation] = Field(None, description="Member information.")
    pharmacy_plan: Optional[PharmacyPlan] = Field(None, description="Pharmacy plan information.")
    insurance_provider: Optional[InsuranceProvider] = Field(None, description="Insurance provider information.")
    coverage: Optional[Coverage] = Field(None, description="Coverage information.")
