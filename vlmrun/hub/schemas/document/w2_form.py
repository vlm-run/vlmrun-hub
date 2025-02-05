from typing import Optional

from pydantic import BaseModel, Field
from pydantic import BaseModel, SkipValidation


class Address(BaseModel):
    street: str | None = Field(None, description="Street address")
    city: str | None = Field(None, description="City")
    state: SkipValidation[str] | None = Field(None, description="State", min_length=2, max_length=2)
    zip_code: SkipValidation[str] | None = Field(None, description="ZIP code", min_length=5, max_length=10)


class W2Form(BaseModel):
    """W2 Form schema for extracting information from IRS Form W-2 (Wage and Tax Statement)."""

    ssn: str | None = Field(None, description="Employee's Social Security Number (SSN) (Box a)")
    ein: str | None = Field(None, description="Employer Identification Number (EIN) (Box b)")

    employer_name: str | None = Field(None, description="Full name of the employer (Box c)")
    employer_address: Address | None = Field(None, description="Employer's complete address (Box c)")

    control_number: str | None = Field(None, description="Control number assigned to the W2 form (Box d)")

    employee_name: str | None = Field(None, description="Full name of the employee (Box e)")
    employee_address: Address | None = Field(None, description="Employee's complete address (Box e)")

    wages_tips_other_compensation: float | None = Field(None, description="Wages, tips, and other compensation (Box 1)")
    federal_income_tax_withheld: float | None = Field(None, description="Federal income tax withheld (Box 2)")
    social_security_wages: float | None = Field(None, description="Social security wages (Box 3)")
    social_security_tax_withheld: float | None = Field(None, description="Social security tax withheld (Box 4)")
    medicare_wages_and_tips: float | None = Field(None, description="Medicare wages and tips (Box 5)")
    medicare_tax_withheld: float | None = Field(None, description="Medicare tax withheld (Box 6)")
    social_security_tips: float | None = Field(None, description="Social security tips (Box 7)")
    allocated_tips: float | None = Field(None, description="Allocated tips (Box 8)")
    dependent_care_benefits: float | None = Field(None, description="Dependent care benefits (Box 10)")
    nonqualified_plans: float | None = Field(None, description="Nonqualified plans (Box 11)")
    total_wages: float | None = Field(None, description="Total wages (Box 12)")

    statutory_employee: bool | None = Field(None, description="Statutory employee checkbox value (Box 13)")
    retirement_plan: bool | None = Field(None, description="Retirement plan checkbox value (Box 13)")
    third_party_sick_pay: bool | None = Field(None, description="Third party sick pay checkbox value (Box 13)")
    other_wages: bool | None = Field(None, description="Other wages checkbox value (Box 14)")

    employers_state_id_number: str | None = Field(None, description="Employer's state ID number (Box 15)")
    state_wages: float | None = Field(None, description="State wages (Box 16)")
    state_income_tax_withheld: float | None = Field(None, description="State income tax withheld (Box 17)")
    local_wages: float | None = Field(None, description="Local wages (Box 18)")
    local_income_tax_withheld: float | None = Field(None, description="Local income tax withheld (Box 19)")
    locality_name: str | None = Field(None, description="Locality name (Box 20)")

    form_year: int | None = Field(None, description="Tax year for which the W2 form is issued, usually on the bottom in bold.")

    a_code: str | None = Field(None, description="Code entered on the left side of Box 12a (Box 12a)")
    a_value: float | None = Field(None, description="Value entered on the right side of Box 12a (Box 12a)")
    b_code: str | None = Field(None, description="Code entered on the left side of Box 12b (Box 12b)")
    b_value: float | None = Field(None, description="Value entered on the right side of Box 12b (Box 12b)")
    c_code: str | None = Field(None, description="Code entered on the left side of Box 12c (Box 12c)")
    c_value: float | None = Field(None, description="Value entered on the right side of Box 12c (Box 12c)")
    d_code: str | None = Field(None, description="Code entered on the left side of Box 12d (Box 12d)")
    d_value: float | None = Field(None, description="Value entered on the right side of Box 12d (Box 12d)")
