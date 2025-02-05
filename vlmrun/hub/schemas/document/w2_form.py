from typing import Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State", min_length=2, max_length=2)
    zip_code: Optional[str] = Field(None, description="ZIP code", min_length=5, max_length=10)


class W2Form(BaseModel):
    """W2 Form schema for extracting information from IRS Form W-2 (Wage and Tax Statement)."""

    control_number: Optional[str] = Field(None, description="Control number assigned to the W2 form")
    ein: Optional[str] = Field(None, description="Employer Identification Number (EIN)")
    ssn: Optional[str] = Field(None, description="Employee's Social Security Number (SSN)")

    employee_name: Optional[str] = Field(None, description="Full name of the employee")
    employee_address: Optional[Address] = Field(None, description="Employee's complete address")

    employer_name: Optional[str] = Field(None, description="Full name of the employer")
    employer_address: Optional[Address] = Field(None, description="Employer's complete address")

    wages_tips_other_compensation: Optional[float] = Field(
        None, description="Wages, tips, and other compensation (Box 1)"
    )
    federal_income_tax_withheld: Optional[float] = Field(None, description="Federal income tax withheld (Box 2)")
    social_security_wages: Optional[float] = Field(None, description="Social security wages (Box 3)")
    social_security_tax_withheld: Optional[float] = Field(None, description="Social security tax withheld (Box 4)")
    medicare_wages_and_tips: Optional[float] = Field(None, description="Medicare wages and tips (Box 5)")
    medicare_tax_withheld: Optional[float] = Field(None, description="Medicare tax withheld (Box 6)")

    tax_year: Optional[int] = Field(None, description="Tax year for which the W2 form is issued")
