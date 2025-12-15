from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MaritalStatus(str, Enum):
    SINGLE = "single"
    SINGLE_CAP = "Single"
    MARRIED = "married"
    MARRIED_CAP = "Married"
    SEPARATED = "separated"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    COMMON_LAW = "common_law"


class ContactMethod(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    CELL_PHONE = "cell_phone"
    MAIL = "mail"


class ResidenceStatus(str, Enum):
    OWN = "own"
    RENT = "rent"
    LIVE_WITH_PARENTS = "live_with_parents"
    OTHER = "other"


class EmploymentType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    SELF_EMPLOYED = "self_employed"
    CONTRACT = "contract"
    RETIRED = "retired"
    UNEMPLOYED = "unemployed"


class IncomeType(str, Enum):
    SALARY = "salary"
    HOURLY = "hourly"
    COMMISSION = "commission"
    SELF_EMPLOYED = "self_employed"
    PENSION = "pension"
    DISABILITY = "disability"
    OTHER = "other"


class HomeType(str, Enum):
    SINGLE_FAMILY = "single_family"
    CONDO = "condo"
    TOWNHOUSE = "townhouse"
    MULTI_FAMILY = "multi_family"
    MOBILE_HOME = "mobile_home"
    OTHER = "other"


class MortgageType(str, Enum):
    FIXED = "fixed"
    VARIABLE = "variable"
    ADJUSTABLE = "adjustable"
    INTEREST_ONLY = "interest_only"
    CONVENTIONAL = "Conventional 30yr Fixed"
    HELOC = "HELOC"
    OTHER = "other"


class CreditStatus(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    UNKNOWN = "unknown"


class Address(BaseModel):
    unit_number: Optional[str] = Field(None, description="Unit or apartment number")
    street: str = Field(..., description="Street address including house number and street name")
    city: str = Field(..., description="City name")
    province_or_state: str = Field(..., description="Province or state")
    postal_code_or_zip: str = Field(..., description="Postal code or ZIP code")
    residence_status: Optional[ResidenceStatus] = Field(None, description="Current residence status: own, rent, etc.")
    rent_payment: Optional[float] = Field(None, description="Monthly rent payment if applicable", ge=0)
    time_at_residence_years: Optional[int] = Field(None, description="Time at residence in years", ge=0)
    time_at_residence_months: Optional[int] = Field(None, description="Additional months at residence", ge=0, lt=12)


class EmploymentHistory(BaseModel):
    employer_name: str = Field(..., description="Name of the employer")
    employer_address: Optional[str] = Field(None, description="Address of the employer")
    employer_city: Optional[str] = Field(None, description="City where employer is located")
    employer_province_or_state: Optional[str] = Field(None, description="Province or state where employer is located")
    employer_postal_code: Optional[str] = Field(None, description="Postal code or ZIP code of employer")
    employment_type: EmploymentType = Field(..., description="Type of employment: full-time, part-time, etc.")
    job_title: str = Field(..., description="Current job title")
    occupation: str = Field(..., description="Occupation or profession")
    industry_sector: Optional[str] = Field(None, description="Industry sector of employment")
    income_type: IncomeType = Field(..., description="Type of income: salary, hourly, etc.")
    income_amount: float = Field(..., description="Annual income amount", ge=0)
    time_at_job_years: Optional[int] = Field(None, description="Years at current job", ge=0)
    time_at_job_months: Optional[int] = Field(None, description="Additional months at current job", ge=0, lt=12)
    time_in_industry_years: Optional[int] = Field(None, description="Years of experience in the industry", ge=0)
    time_in_industry_months: Optional[int] = Field(None, description="Additional months of experience in the industry", ge=0, lt=12)


class PreviousEmploymentHistory(BaseModel):
    employer_name: Optional[str] = Field(None, description="Name of the employer")
    employer_address: Optional[str] = Field(None, description="Address of the employer")
    employer_city: Optional[str] = Field(None, description="City where employer is located")
    employer_province_or_state: Optional[str] = Field(None, description="Province or state where employer is located")
    employer_postal_code: Optional[str] = Field(None, description="Postal code or ZIP code of employer")
    employment_type: Optional[EmploymentType] = Field(None, description="Type of employment: full-time, part-time, etc.")
    job_title: Optional[str] = Field(None, description="Current job title")
    occupation: Optional[str] = Field(None, description="Occupation or profession")
    industry_sector: Optional[str] = Field(None, description="Industry sector of employment")
    income_type: Optional[IncomeType] = Field(None, description="Type of income: salary, hourly, etc.")
    income_amount: Optional[float] = Field(None, description="Annual income amount", ge=0)
    time_at_job_years: Optional[int] = Field(None, description="Years at current job", ge=0)
    time_at_job_months: Optional[int] = Field(None, description="Additional months at current job", ge=0, lt=12)
    time_in_industry_years: Optional[int] = Field(None, description="Years of experience in the industry", ge=0)
    time_in_industry_months: Optional[int] = Field(None, description="Additional months of experience in the industry", ge=0, lt=12)


class PropertyInformation(BaseModel):
    home_type: Optional[HomeType] = Field(None, description="Type of home: single family, condo, etc.")
    property_address: Optional[Address] = Field(None, description="Address of the property being mortgaged")
    estimated_market_value: Optional[float] = Field(None, description="Estimated current market value of the property", ge=0)
    tax_value: Optional[float] = Field(None, description="Assessed value for tax purposes", ge=0)
    year_purchased: Optional[int] = Field(None, description="Year the property was purchased")
    year_built: Optional[int] = Field(None, description="Year the property was built")
    original_cost: Optional[float] = Field(None, description="Original purchase price of the property", ge=0)
    years_in_home: Optional[int] = Field(None, description="Number of years living in the property", ge=0)
    has_escrow: Optional[bool] = Field(None, description="Whether the mortgage includes an escrow account")
    has_mortgage_insurance: Optional[bool] = Field(None, description="Whether the mortgage has mortgage insurance")
    monthly_mortgage_payment: Optional[float] = Field(None, description="Current monthly mortgage payment", ge=0)


class MortgageDetails(BaseModel):
    mortgage_holder: Optional[str] = Field(None, description="Name of the current mortgage holder")
    mortgage_type: Optional[MortgageType] = Field(None, description="Type of mortgage: fixed, variable, etc.")
    interest_rate: Optional[float] = Field(None, description="Current interest rate of the mortgage", ge=0)
    mortgage_term_years: Optional[int] = Field(None, description="Original term of the mortgage in years", ge=0)
    mortgage_years_left: Optional[int] = Field(None, description="Remaining years on the mortgage", ge=0)
    mortgage_balance: Optional[float] = Field(None, description="Current balance on the mortgage", ge=0)
    mortgage_monthly_payment: Optional[float] = Field(None, description="Current monthly mortgage payment", ge=0)
    second_mortgage_holder: Optional[str] = Field(None, description="Name of the second mortgage holder, if applicable")
    second_mortgage_type: Optional[MortgageType] = Field(None, description="Type of second mortgage")
    second_interest_rate: Optional[float] = Field(None, description="Interest rate of the second mortgage", ge=0)
    second_term_years: Optional[int] = Field(None, description="Original term of the second mortgage in years", ge=0)
    second_years_left: Optional[int] = Field(None, description="Remaining years on the second mortgage", ge=0)
    second_balance: Optional[float] = Field(None, description="Current balance on the second mortgage", ge=0)
    second_monthly_payment: Optional[float] = Field(None, description="Monthly payment for the second mortgage", ge=0)


class FinancialObligations(BaseModel):
    child_support_or_alimony: Optional[float] = Field(None, description="Monthly child support or alimony payments", ge=0)
    real_estate_taxes_yearly: Optional[float] = Field(None, description="Annual real estate taxes", ge=0)
    real_estate_taxes_monthly: Optional[float] = Field(None, description="Monthly real estate taxes", ge=0)
    home_insurance_yearly: Optional[float] = Field(None, description="Annual home insurance premium", ge=0)
    home_insurance_monthly: Optional[float] = Field(None, description="Monthly home insurance payment", ge=0)
    credit_score: Optional[int] = Field(None, description="Current credit score", ge=300, le=850)
    credit_status: Optional[CreditStatus] = Field(None, description="Status of credit: excellent, good, fair, etc.")
    agreed_to_credit_check: Optional[bool] = Field(None, description="Whether applicant has agreed to a credit check")
    credit_check_date: Optional[date] = Field(None, description="Date of the credit check")
    mortgage_late_payments: Optional[int] = Field(None, description="Number of late mortgage payments", ge=0)
    credit_issues_description: Optional[str] = Field(None, description="Description of any credit issues or concerns")


class Assets(BaseModel):
    cash_in_bank: Optional[float] = Field(None, description="Amount of cash in bank accounts", ge=0)
    investments: Optional[float] = Field(None, description="Value of investments", ge=0)
    owned_property: Optional[float] = Field(None, description="Value of other owned property", ge=0)


class ApplicantInformation(BaseModel):
    salutation: Optional[str] = Field(None, description="Applicant's salutation (Mr., Mrs., Ms., etc.)")
    first_name: str = Field(..., description="Applicant's first name")
    middle_initial: Optional[str] = Field(None, description="Applicant's middle initial")
    last_name: str = Field(..., description="Applicant's last name")
    date_of_birth: date = Field(..., description="Applicant's date of birth")
    sin: Optional[str] = Field(None, description="Social Insurance Number (SIN)")
    marital_status: Optional[MaritalStatus] = Field(None, description="Applicant's marital status")
    contact_method: Optional[ContactMethod] = Field(None, description="Preferred contact method")
    dependents: Optional[int] = Field(None, description="Number of dependents", ge=0)
    email: Optional[str] = Field(None, description="Email address")
    work_phone: Optional[str] = Field(None, description="Work phone number")
    home_phone: Optional[str] = Field(None, description="Home phone number")
    cell_phone: Optional[str] = Field(None, description="Cell phone number")
    current_address: Address = Field(..., description="Current residential address")
    previous_address: Optional[Address] = Field(None, description="Previous address if less than 3 years at current address")
    current_employment: EmploymentHistory = Field(..., description="Current employment details")
    previous_employment: Optional[PreviousEmploymentHistory] = Field(None, description="Previous employment if less than 3 years with current employer")


class ApplicationMeta(BaseModel):
    application_date: Optional[date] = Field(None, description="Date of mortgage application")
    application_time: Optional[str] = Field(None, description="Time of mortgage application")
    loan_officer: Optional[str] = Field(None, description="Name of the loan officer")
    purpose_of_loan: str = Field(..., description="Purpose of the mortgage loan (purchase, refinance, etc.)")
    referred_by: Optional[str] = Field(None, description="Person or entity who referred the applicant")


class MortgageApplication(BaseModel):    
    application_meta: ApplicationMeta = Field(..., description="Metadata about the mortgage application")
    primary_applicant: ApplicantInformation = Field(..., description="Information about the primary applicant")
    co_applicant: Optional[ApplicantInformation] = Field(None, description="Information about the co-applicant, if applicable")
    property_information: PropertyInformation = Field(..., description="Information about the property being mortgaged")
    mortgage_details: Optional[MortgageDetails] = Field(None, description="Details about current and second mortgages, if applicable")
    financial_obligations: Optional[FinancialObligations] = Field(None, description="Information about financial obligations and credit")
    assets: Optional[Assets] = Field(None, description="Information about assets and investments")