from datetime import date
from pydantic import BaseModel, Field


class IDImage(BaseModel):
    image_url: str | None = Field(None, description="URL to the image of the ID document.")
    image_type: str | None = Field(None, description="Type of ID image, e.g., 'front', 'back'.")


class PersonalInformation(BaseModel):
    full_name: str | None = Field(None, description="Full name of the person as shown on the ID.")
    date_of_birth: date | None = Field(None, description="Date of birth of the person as shown on the ID.")
    gender: str | None = Field(None, description="Gender of the person, if indicated on the ID.")
    nationality: str | None = Field(None, description="Nationality of the person, if indicated on the ID.")


class IDDocumentDetails(BaseModel):
    document_type: str | None = Field(None, description="Type of ID document, e.g., 'passport', 'driver's license'.")
    document_number: str | None = Field(None, description="Unique number of the ID document.")
    issue_date: date | None = Field(None, description="Issue date of the ID document.")
    expiry_date: date | None = Field(None, description="Expiration date of the ID document, if applicable.")
    issuing_country: str | None = Field(None, description="Country that issued the ID document.")


class IDExtraction(BaseModel):
    id_images: list[IDImage] | None = Field(None, description="Images of the ID document, e.g., front and back.")
    personal_information: PersonalInformation | None = Field(None, description="Extracted personal information from the ID document.")
    document_details: IDDocumentDetails | None = Field(None, description="Details specific to the ID document.")
