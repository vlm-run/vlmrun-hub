from datetime import date
from typing import List

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str | None = Field(None, description="Street address")
    city: str | None = Field(None, description="City")
    state: str | None = Field(None, description="State")
    zip_code: str | None = Field(None, description="ZIP code")


class W2Form(BaseModel):
    """W2 Form schema for extracting information from IRS Form W-2 (Wage and Tax Statement)."""

    control_number: str | None = Field(None, description="Control number assigned to the W2 form")
    ein: str = Field(..., description="Employer Identification Number (EIN)")
    ssn: str = Field(..., description="Employee's Social Security Number (SSN)")

    employee_name: str = Field(..., description="Full name of the employee")
    employee_address: Address = Field(..., description="Employee's complete address")
    
    employer_name: str = Field(..., description="Full name of the employer")
    employer_address: Address = Field(..., description="Employer's complete address")

    wages_tips_other_compensation: float = Field(
        ..., description="Wages, tips, and other compensation (Box 1)"
    )
    social_security_wages: float = Field(
        ..., description="Social security wages (Box 3)"
    )
    social_security_tax_withheld: float = Field(
        ..., description="Social security tax withheld (Box 4)"
    )
    medicare_wages_and_tips: float = Field(
        ..., description="Medicare wages and tips (Box 5)"
    )
    medicare_tax_withheld: float = Field(
        ..., description="Medicare tax withheld (Box 6)"
    )
    federal_income_tax_withheld: float = Field(
        ..., description="Federal income tax withheld (Box 2)"
    )

    tax_year: int = Field(..., description="Tax year for which the W2 form is issued")
