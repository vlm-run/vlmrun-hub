from typing import Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    zip_code: Optional[str] = Field(None, description="ZIP code")


class W2Form(BaseModel):
    """W2 Form schema for extracting information from IRS Form W-2 (Wage and Tax Statement)."""

    ssn: Optional[str] = Field(None, description="Employee's Social Security Number (SSN) (Box a)")
    ein: Optional[str] = Field(None, description="Employer Identification Number (EIN) (Box b)")

    employer_name: Optional[str] = Field(None, description="Full name of the employer (Box c)")
    employer_address: Optional[Address] = Field(None, description="Employer's complete address (Box c)")

    control_number: Optional[str] = Field(None, description="Control number assigned to the W2 form (Box d)")

    employee_name: Optional[str] = Field(None, description="Full name of the employee (Box e)")
    employee_address: Optional[Address] = Field(None, description="Employee's complete address (Box e)")

    wages_tips_other_compensation: Optional[float] = Field(
        None, description="Wages, tips, and other compensation (Box 1)"
    )
    federal_income_tax_withheld: Optional[float] = Field(None, description="Federal income tax withheld (Box 2)")
    social_security_wages: Optional[float] = Field(None, description="Social security wages (Box 3)")
    social_security_tax_withheld: Optional[float] = Field(None, description="Social security tax withheld (Box 4)")
    medicare_wages_and_tips: Optional[float] = Field(None, description="Medicare wages and tips (Box 5)")
    medicare_tax_withheld: Optional[float] = Field(None, description="Medicare tax withheld (Box 6)")
    social_security_tips: Optional[float] = Field(None, description="Social security tips (Box 7)")
    allocated_tips: Optional[float] = Field(None, description="Allocated tips (Box 8)")
    dependent_care_benefits: Optional[float] = Field(None, description="Dependent care benefits (Box 10)")
    nonqualified_plans: Optional[float] = Field(None, description="Nonqualified plans (Box 11)")
    total_wages: Optional[float] = Field(None, description="Total wages (Box 12)")

    statutory_employee: Optional[bool] = Field(None, description="Statutory employee checkbox value (Box 13)")
    retirement_plan: Optional[bool] = Field(None, description="Retirement plan checkbox value (Box 13)")
    third_party_sick_pay: Optional[bool] = Field(None, description="Third party sick pay checkbox value (Box 13)")
    other_wages: Optional[bool] = Field(None, description="Other wages checkbox value (Box 14)")

    employers_state_id_number: Optional[str] = Field(None, description="Employer's state ID number (Box 15)")
    state_wages: Optional[float] = Field(None, description="State wages (Box 16)")
    state_income_tax_withheld: Optional[float] = Field(None, description="State income tax withheld (Box 17)")
    local_wages: Optional[float] = Field(None, description="Local wages (Box 18)")
    local_income_tax_withheld: Optional[float] = Field(None, description="Local income tax withheld (Box 19)")
    locality_name: Optional[str] = Field(None, description="Locality name (Box 20)")

    form_year: Optional[int] = Field(
        None, description="Tax year for which the W2 form is issued, usually on the bottom in bold."
    )

    a_code: Optional[str] = Field(None, description="Code entered on the left side of Box 12a (Box 12a)")
    a_value: Optional[float] = Field(None, description="Value entered on the right side of Box 12a (Box 12a)")
    b_code: Optional[str] = Field(None, description="Code entered on the left side of Box 12b (Box 12b)")
    b_value: Optional[float] = Field(None, description="Value entered on the right side of Box 12b (Box 12b)")
    c_code: Optional[str] = Field(None, description="Code entered on the left side of Box 12c (Box 12c)")
    c_value: Optional[float] = Field(None, description="Value entered on the right side of Box 12c (Box 12c)")
    d_code: Optional[str] = Field(None, description="Code entered on the left side of Box 12d (Box 12d)")
    d_value: Optional[float] = Field(None, description="Value entered on the right side of Box 12d (Box 12d)")
