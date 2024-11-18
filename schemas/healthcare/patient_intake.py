from datetime import date
from pydantic import BaseModel, Field


class DemographicInformation(BaseModel):
    full_name: str | None = Field(None, description="Full name of the patient.")
    date_of_birth: date | None = Field(None, description="Date of birth of the patient.")
    gender: str | None = Field(None, description="Gender of the patient.")
    contact_number: str | None = Field(
        None, description="Contact number of the patient."
    )
    address: str | None = Field(None, description="Residential address of the patient.")
    email: str | None = Field(None, description="Email address of the patient.")


class MedicalHistory(BaseModel):
    conditions: list[str] | None = Field(None, description="List of known medical conditions.")
    medications: list[str] | None = Field(None, description="List of medications the patient is currently taking.")
    allergies: list[str] | None = Field(None, description="List of allergies the patient has.")
    surgeries: list[str] | None = Field(None, description="List of past surgeries, if any.")
    family_history: str | None = Field(None, description="Family medical history details, if relevant.")


class InsuranceDetails(BaseModel):
    provider: str | None = Field(None, description="Name of the insurance provider.")
    policy_number: str | None = Field(None, description="Insurance policy number.")
    group_number: str | None = Field(None, description="Group number associated with the insurance policy.")
    coverage_start_date: date | None = Field(None, description="Date when the insurance coverage starts.")
    coverage_end_date: date | None = Field(None, description="Date when the insurance coverage ends.")



class ConsentForm(BaseModel):
    form_name: str | None = Field(None, description="Name of the consent form.")
    signed_date: date | None = Field(None, description="Date when the consent form was signed.")
    form_url: str | None = Field(None, description="URL to the digital copy of the signed consent form.")


class PatientImage(BaseModel):
    image_url: str | None = Field(None, description="URL to the patient's image.")
    image_type: str | None = Field(None, description="Type of image, e.g., 'profile photo', 'X-ray'.")
    date_taken: date | None = Field(None, description="Date when the image was taken.")


class PatientIntake(BaseModel):
    demographic_information: DemographicInformation | None = Field(
        None, description="Basic demographic details of the patient."
    )
    medical_history: MedicalHistory | None = Field(
        None, description="Medical history of the patient."
    )
    insurance_details: InsuranceDetails | None = Field(
        None, description="Insurance details of the patient."
    )
    consent_forms: list[ConsentForm] | None = Field(
        None, description="List of signed consent forms by the patient."
    )
    patient_images: list[PatientImage] | None = Field(
        None, description="List of images related to the patient."
    )
