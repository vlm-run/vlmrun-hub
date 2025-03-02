from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class PatientInformation(BaseModel):
    first_name: Optional[str] = Field(None, description="Patient's first name")
    last_name: Optional[str] = Field(None, description="Patient's last name")
    member_id: Optional[str] = Field(None, description="Patient's member ID or insurance identifier")
    address: Optional[str] = Field(None, description="Patient's street address")
    city: Optional[str] = Field(None, description="Patient's city of residence")
    state: Optional[str] = Field(None, description="Patient's state of residence (2-letter code)")
    zip_code: Optional[str] = Field(None, description="Patient's ZIP code")
    phone: Optional[str] = Field(None, description="Patient's contact phone number")
    date_of_birth: Optional[date] = Field(None, description="Patient's date of birth")
    allergies: Optional[str] = Field(None, description="Patient's known allergies")
    primary_insurance: Optional[str] = Field(None, description="Patient's primary insurance provider")
    policy_number: Optional[str] = Field(None, description="Patient's insurance policy number")
    group_number: Optional[str] = Field(None, description="Patient's insurance group number")
    is_new_therapy: Optional[bool] = Field(None, description="Indicates if this is a new therapy request")
    is_continuation_therapy: Optional[bool] = Field(None, description="Indicates if this is a continuation of existing therapy")
    therapy_start_date: Optional[date] = Field(None, description="Start date of therapy if continuation")
    is_currently_hospitalized: Optional[bool] = Field(None, description="Indicates if the patient is currently hospitalized")


class PhysicianInformation(BaseModel):
    first_name: Optional[str] = Field(None, description="Physician's first name")
    last_name: Optional[str] = Field(None, description="Physician's last name")
    address: Optional[str] = Field(None, description="Physician's office address")
    city: Optional[str] = Field(None, description="Physician's city")
    state: Optional[str] = Field(None, description="Physician's state (2-letter code)")
    zip_code: Optional[str] = Field(None, description="Physician's ZIP code")
    phone: Optional[str] = Field(None, description="Physician's contact phone number")
    fax: Optional[str] = Field(None, description="Physician's fax number")
    npi_number: Optional[str] = Field(None, description="Physician's National Provider Identifier (NPI) number")
    specialty: Optional[str] = Field(None, description="Physician's medical specialty")
    office_contact_name: Optional[str] = Field(None, description="Name of the office contact person")


class MedicationInformation(BaseModel):
    name: Optional[str] = Field(None, description="Name of the medication being requested")
    strength: Optional[str] = Field(None, description="Strength or dosage of the medication")
    directions: Optional[str] = Field(None, description="Directions for use of the medication")


class PreviousMedication(BaseModel):
    name: Optional[str] = Field(None, description="Name of previously tried medication")
    strength: Optional[str] = Field(None, description="Strength or dosage of previously tried medication")
    directions: Optional[str] = Field(None, description="Directions for use of previously tried medication")
    therapy_start_date: Optional[date] = Field(None, description="Start date of previous medication therapy")
    therapy_end_date: Optional[date] = Field(None, description="End date of previous medication therapy")
    reason_for_discontinuation: Optional[str] = Field(None, description="Reason for discontinuing the previous medication")


class DiagnosisInformation(BaseModel):
    diagnosis: Optional[str] = Field(None, description="Patient's diagnosis relevant to the authorization request")
    icd_code: Optional[str] = Field(None, description="ICD-9 or ICD-10 code for the diagnosis")
    has_hiv_aids: Optional[bool] = Field(None, description="Indicates if the patient has HIV/AIDS")
    is_pregnant: Optional[bool] = Field(None, description="Indicates if the patient is pregnant")
    due_date: Optional[date] = Field(None, description="Due date if patient is pregnant")
    justification: Optional[str] = Field(None, description="Justification for why preferred medications would not meet patient's needs")


class PriorAuthorization(BaseModel):
    request_date: Optional[date] = Field(None, description="Date of the prior authorization request")
    patient: Optional[PatientInformation] = Field(None, description="Patient information section")
    physician: Optional[PhysicianInformation] = Field(None, description="Physician information section")
    medication: Optional[MedicationInformation] = Field(None, description="Information about the requested medication")
    diagnosis: Optional[DiagnosisInformation] = Field(None, description="Diagnosis information section")
    previous_medications: Optional[List[PreviousMedication]] = Field(None, description="List of previously tried medications")
    physician_signature_date: Optional[date] = Field(None, description="Date of physician's signature on the form")

    class Config:
        schema_extra = {
            "example": {
                "request_date": "2023-05-15",
                "patient": {
                    "first_name": "John",
                    "last_name": "Williams",
                    "member_id": "123456",
                    "address": "123 Easy Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "zip_code": "94110",
                    "phone": "650-123-4567",
                    "date_of_birth": "1971-06-21",
                    "allergies": "None",
                    "primary_insurance": "Aetna",
                    "policy_number": "09876",
                    "group_number": "436278",
                    "is_new_therapy": True,
                    "is_continuation_therapy": False,
                    "is_currently_hospitalized": False
                },
                "physician": {
                    "first_name": "Leonard",
                    "last_name": "McCoy",
                    "address": "456 West El Camino",
                    "city": "Mountain View",
                    "state": "CA",
                    "zip_code": "73289",
                    "specialty": "Internal Medicine"
                },
                "medication": {
                    "name": "Aspirin",
                    "strength": "500mg",
                    "directions": "Daily with food"
                },
                "diagnosis": {
                    "diagnosis": "Chronic pain",
                    "has_hiv_aids": False,
                    "is_pregnant": False,
                    "justification": "Does not like a specific brand of aspirin"
                },
                "previous_medications": [
                    {
                        "name": "Advil",
                        "strength": "500mg",
                        "directions": "Daily",
                        "therapy_start_date": "2023-04-23",
                        "reason_for_discontinuation": "Ineffective"
                    }
                ]
            }
        }
