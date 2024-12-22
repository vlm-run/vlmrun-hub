from pydantic import BaseModel, Field


class ProviderService(BaseModel):
    provider_service_number: str | None = Field(default=None, description="Provider service number.")
    precertification_number: str | None = Field(default=None, description="Precertification number.")


class MemberInformation(BaseModel):
    member_name: str = Field(..., description="Name of the member.")
    member_id: str | None = Field(default=None, description="Member ID.")
    group_number: str | None = Field(default=None, description="Group number.")


class PharmacyPlan(BaseModel):
    rx_bin: str | None = Field(default=None, description="Rx bin.")
    rx_pcn: str | None = Field(default=None, description="Rx pcn.")
    rx_grp: str | None = Field(default=None, description="Rx grp.")
    pharmacy_help_desk: str | None = Field(default=None, description="Pharmacy help desk.")


class InsuranceProvider(BaseModel):
    provider_name: str = Field(..., description="Provider name.")
    network: str = Field(..., description="Network.")


class Coverage(BaseModel):
    office_visit: str | None = Field(default=None, description="Office visit.")
    specialist_visit: str | None = Field(default=None, description="Specialist visit.")
    urgent_care: str | None = Field(default=None, description="Urgent care.")
    emergency_room: str | None = Field(default=None, description="Emergency room.")
    inpatient_hospital: str | None = Field(default=None, description="Inpatient hospital.")


class MedicalInsuranceCard(BaseModel):
    provider_service: ProviderService = Field(..., description="Provider service information.")
    member_information: MemberInformation = Field(..., description="Member information.")
    pharmacy_plan: PharmacyPlan = Field(..., description="Pharmacy plan information.")
    insurance_provider: InsuranceProvider = Field(..., description="Insurance provider information.")
    coverage: Coverage = Field(..., description="Coverage information.")
