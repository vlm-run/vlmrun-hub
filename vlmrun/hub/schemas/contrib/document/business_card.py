from typing import Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    """Address information that may be present on a business card."""
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State or province")
    postal_code: Optional[str] = Field(None, description="Postal or ZIP code")
    country: Optional[str] = Field(None, description="Country")


class BusinessCard(BaseModel):
    """Business card schema for extracting information from business card images or documents."""
    
    # Personal information
    name: Optional[str] = Field(None, description="Full name of the person on the business card")
    job_title: Optional[str] = Field(None, description="Job title or position of the person")
    
    # Company information
    company_name: Optional[str] = Field(None, description="Name of the company or organization")
    
    # Contact information
    phone: Optional[str] = Field(None, description="Phone number, may include country code and formatting")
    email: Optional[str] = Field(None, description="Email address")
    website: Optional[str] = Field(None, description="Website URL")
    address: Optional[Address] = Field(None, description="Physical address information")
    
    # Visual elements
    has_logo: Optional[bool] = Field(None, description="Indicates if the business card has a company logo")
    has_photo: Optional[bool] = Field(None, description="Indicates if the business card has a photo of the person")
    
    # Additional information
    social_media: Optional[dict] = Field(None, description="Dictionary of social media handles or URLs")
    additional_info: Optional[str] = Field(None, description="Any additional information present on the card")
