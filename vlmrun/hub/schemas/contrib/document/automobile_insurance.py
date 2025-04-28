from datetime import date
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class OwnershipStatus(str, Enum):
    RENT = "rent"
    OWN = "own"
    # Add capitalized variants
    RENT_CAP = "Rent"
    OWN_CAP = "Own"


class MaritalStatus(str, Enum):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    SEPARATED = "separated"
    # Add capitalized variants
    SINGLE_CAP = "Single"
    MARRIED_CAP = "Married"
    DIVORCED_CAP = "Divorced"
    WIDOWED_CAP = "Widowed"
    SEPARATED_CAP = "Separated"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"
    # Add capitalized variants
    MALE_CAP = "Male"
    FEMALE_CAP = "Female"
    OTHER_CAP = "Other"
    PREFER_NOT_TO_SAY_CAP = "Prefer not to say"


class UsageType(str, Enum):
    BUSINESS = "business"
    PLEASURE = "pleasure"
    CARPOOL = "carpool"
    COMMUTE = "commute"
    # Add capitalized variants
    BUSINESS_CAP = "Business"
    PLEASURE_CAP = "Pleasure"
    CARPOOL_CAP = "Carpool"
    COMMUTE_CAP = "Commute"


class CoverageType(str, Enum):
    COMPREHENSIVE = "comprehensive"
    THIRD_PARTY = "third_party"
    THIRD_PARTY_FIRE_THEFT = "third_party_fire_theft"
    LIABILITY_ONLY = "liability_only"
    # Add capitalized variants
    COMPREHENSIVE_CAP = "Comprehensive"
    THIRD_PARTY_CAP = "Third Party"
    THIRD_PARTY_FIRE_THEFT_CAP = "Third Party Fire & Theft"
    LIABILITY_ONLY_CAP = "Liability Only"


class Address(BaseModel):
    street: str = Field(..., description="Street address (e.g., '123 Elm St Apt 4B')")
    city: str = Field(..., description="City name")
    state: str = Field(..., description="State or province (e.g., 'CA', 'NY', 'TX')")
    zip_code: str = Field(..., description="ZIP or postal code (e.g., '12345-6789')")
    county: Optional[str] = Field(None, description="County name if applicable")


class ContactInfo(BaseModel):
    home_phone: Optional[str] = Field(None, description="Home telephone number")
    business_phone: Optional[str] = Field(None, description="Business or work telephone number")
    email: Optional[str] = Field(None, description="Email address")


class Conviction(BaseModel):
    date: str = Field(..., description="Date of the conviction")
    offense_type: str = Field(..., description="Type of offense (e.g., 'speeding', 'DUI')")
    details: Optional[str] = Field(None, description="Additional details about the conviction")
    points: Optional[int] = Field(None, description="Points assigned to the license for this conviction", ge=0)


class Accident(BaseModel):
    date: str = Field(..., description="Date of the accident")
    description: str = Field(..., description="Brief description of the accident")
    at_fault: Optional[bool] = Field(None, description="Whether the driver was at fault")
    claim_amount: Optional[float] = Field(None, description="Amount claimed for damages", ge=0)
    injuries: Optional[bool] = Field(None, description="Whether the accident involved injuries")


class Driver(BaseModel):
    name: str = Field(..., description="Full name of the driver")
    marital_status: Optional[MaritalStatus] = Field(None, description="Marital status of the driver")
    gender: Optional[Gender] = Field(None, description="Gender of the driver")
    date_of_birth: str = Field(..., description="Driver's date of birth (YYYY-MM-DD)")
    date_licensed: str = Field(..., description="Date when driver was first licensed (YYYY-MM-DD)")
    driver_license_number: str = Field(..., description="Driver's license number")
    license_state: str = Field(..., description="State that issued the driver's license")
    social_security_number: Optional[str] = Field(None, description="Driver's social security number")
    occupation: Optional[str] = Field(None, description="Driver's current occupation")
    medical_conditions: Optional[List[str]] = Field(None, description="List of medical conditions that may affect driving")
    convictions: Optional[List[Conviction]] = Field(None, description="List of motoring or non-motoring offenses")
    accident_history: Optional[List[Accident]] = Field(None, description="History of past accidents")
    previous_insurance_declined: Optional[bool] = Field(None, description="Whether driver has been declined insurance previously")
    license_suspended: Optional[bool] = Field(None, description="Whether driver's license has ever been suspended")


class Vehicle(BaseModel):
    vin: str = Field(..., description="Vehicle Identification Number")
    make_model: str = Field(..., description="Make and model of the vehicle")
    year: str = Field(..., description="Year of manufacture")
    annual_mileage: Optional[int] = Field(None, description="Estimated annual mileage", ge=0)
    usage_type: Optional[UsageType] = Field(None, description="Primary usage of the vehicle")
    anti_theft_devices: Optional[List[str]] = Field(None, description="Anti-theft devices installed in the vehicle")
    airbag_status: Optional[str] = Field(None, description="Airbag availability (e.g., 'Driver & Passenger')")
    garaged_address: Optional[str] = Field(None, description="Address where vehicle is primarily garaged")
    modifications: Optional[List[str]] = Field(None, description="Modifications made to the vehicle")
    purchase_date: Optional[str] = Field(None, description="Date when vehicle was purchased (YYYY-MM-DD)")
    estimated_value: Optional[float] = Field(None, description="Estimated current value of the vehicle", ge=0)


class Deductibles(BaseModel):
    collision: Optional[float] = Field(None, description="Collision deductible amount", ge=0)
    comprehensive: Optional[float] = Field(None, description="Comprehensive deductible amount", ge=0)


class AutomobileInsurance(BaseModel):
    applicant_name: str = Field(..., description="Full name of the primary applicant")
    co_applicant_name: Optional[str] = Field(None, description="Full name of co-applicant, if any")
    address: Address = Field(..., description="Primary residence address of the applicant")
    contact_info: ContactInfo = Field(..., description="Contact information of the applicant")
    ownership_status: Optional[OwnershipStatus] = Field(None, description="Whether applicant rents or owns their residence")
    drivers: List[Driver] = Field(..., description="List of drivers to be covered by the policy")
    vehicles: List[Vehicle] = Field(..., description="List of vehicles to be covered by the policy")