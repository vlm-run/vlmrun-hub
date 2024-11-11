from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class DemographicInformation(BaseModel):
    full_name: str = Field(..., description="Full name of the patient.")
    date_of_birth: date = Field(..., description="Date of birth of the patient.")
    gender: Optional[str] = Field(None, description="Gender of the patient.")
    contact_number: Optional[str] = Field(
        None, description="Contact number of the patient."
    )
    address: Optional[str] = Field(
        None, description="Residential address of the patient."
    )
    email: Optional[str] = Field(None, description="Email address of the patient.")


class MedicalHistory(BaseModel):
    conditions: List[str] = Field(..., description="List of known medical conditions.")
    medications: List[str] = Field(
        ..., description="List of medications the patient is currently taking."
    )
    allergies: List[str] = Field(..., description="List of allergies the patient has.")
    surgeries: Optional[List[str]] = Field(
        None, description="List of past surgeries, if any."
    )
    family_history: Optional[str] = Field(
        None, description="Family medical history details, if relevant."
    )


class InsuranceDetails(BaseModel):
    provider: str = Field(..., description="Name of the insurance provider.")
    policy_number: str = Field(..., description="Insurance policy number.")
    group_number: Optional[str] = Field(
        None, description="Group number associated with the insurance policy."
    )
    coverage_start_date: Optional[date] = Field(
        None, description="Date when the insurance coverage starts."
    )
    coverage_end_date: Optional[date] = Field(
        None, description="Date when the insurance coverage ends."
    )


class ConsentForm(BaseModel):
    form_name: str = Field(..., description="Name of the consent form.")
    signed_date: date = Field(..., description="Date when the consent form was signed.")
    form_url: Optional[str] = Field(
        None, description="URL to the digital copy of the signed consent form."
    )


class PatientImage(BaseModel):
    image_url: str = Field(..., description="URL to the patient's image.")
    image_type: str = Field(
        ..., description="Type of image, e.g., 'profile photo', 'X-ray'."
    )
    date_taken: Optional[date] = Field(
        None, description="Date when the image was taken."
    )


class PatientIntake(BaseModel):
    demographic_information: DemographicInformation = Field(
        ..., description="Basic demographic details of the patient."
    )
    medical_history: MedicalHistory = Field(
        ..., description="Medical history of the patient."
    )
    insurance_details: InsuranceDetails = Field(
        ..., description="Insurance details of the patient."
    )
    consent_forms: List[ConsentForm] = Field(
        ..., description="List of signed consent forms by the patient."
    )
    patient_images: List[PatientImage] = Field(
        ..., description="List of images related to the patient."
    )
