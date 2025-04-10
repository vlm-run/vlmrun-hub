from datetime import date
from typing import List, Optional, Literal, Union, Dict, Any
from enum import Enum

from pydantic import BaseModel, Field


class FilingStatus(str, Enum):
    single = "single"
    married_filing_jointly = "married_filing_jointly"
    married_filing_separately = "married_filing_separately" 
    head_of_household = "head_of_household"
    qualifying_widower = "qualifying_widower"


class TaxpayerInfo(BaseModel):
    first_name: Optional[str] = Field(None, description="Taxpayer's first name")
    last_name: Optional[str] = Field(None, description="Taxpayer's last name")
    middle_initial: Optional[str] = Field(None, description="Taxpayer's middle initial")
    social_security_number: Optional[str] = Field(None, description="Taxpayer's social security number, typically formatted as XXX-XX-XXXX")
    occupation: Optional[str] = Field(None, description="Taxpayer's occupation")


class SpouseInfo(BaseModel):
    first_name: Optional[str] = Field(None, description="Spouse's first name")
    last_name: Optional[str] = Field(None, description="Spouse's last name")
    middle_initial: Optional[str] = Field(None, description="Spouse's middle initial")
    social_security_number: Optional[str] = Field(None, description="Spouse's social security number, typically formatted as XXX-XX-XXXX")
    occupation: Optional[str] = Field(None, description="Spouse's occupation")


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address including apartment or suite number")
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State or province abbreviation (e.g., 'CA', 'NY')")
    zip_code: Optional[str] = Field(None, description="ZIP or postal code")
    foreign_country: Optional[str] = Field(None, description="Foreign country name, if applicable")
    foreign_postal_code: Optional[str] = Field(None, description="Foreign postal code, if applicable")


class Dependent(BaseModel):
    first_name: Optional[str] = Field(None, description="Dependent's first name")
    last_name: Optional[str] = Field(None, description="Dependent's last name")
    social_security_number: Optional[str] = Field(None, description="Dependent's social security number")
    relationship: Optional[str] = Field(None, description="Relationship to taxpayer (e.g., 'Child', 'Parent')")
    child_tax_credit: Optional[bool] = Field(None, description="Whether the dependent qualifies for child tax credit")
    credit_for_other_dependents: Optional[bool] = Field(None, description="Whether the dependent qualifies for credit for other dependents")


class Income(BaseModel):
    wages_salaries_tips: Optional[float] = Field(None, description="Wages, salaries, and tips from all W-2 forms")
    taxable_interest: Optional[float] = Field(None, description="Taxable interest income")
    tax_exempt_interest: Optional[float] = Field(None, description="Tax-exempt interest income")
    qualified_dividends: Optional[float] = Field(None, description="Qualified dividends")
    ordinary_dividends: Optional[float] = Field(None, description="Ordinary dividends")
    taxable_refunds: Optional[float] = Field(None, description="Taxable refunds, credits, or offsets of state/local income taxes")
    business_income: Optional[float] = Field(None, description="Business income or loss (attach Schedule C)")
    capital_gain: Optional[float] = Field(None, description="Capital gain or loss (attach Schedule D)")
    other_gains_losses: Optional[float] = Field(None, description="Other gains or losses")
    ira_distributions: Optional[float] = Field(None, description="IRA distributions")
    taxable_ira_distributions: Optional[float] = Field(None, description="Taxable amount of IRA distributions")
    pension_annuities: Optional[float] = Field(None, description="Pensions and annuities")
    taxable_pension_annuities: Optional[float] = Field(None, description="Taxable amount of pensions and annuities")
    rental_income: Optional[float] = Field(None, description="Rental real estate, royalties, partnerships, S corps, trusts")
    unemployment_compensation: Optional[float] = Field(None, description="Unemployment compensation")
    social_security_benefits: Optional[float] = Field(None, description="Social security benefits")
    taxable_social_security: Optional[float] = Field(None, description="Taxable amount of social security benefits")
    other_income: Optional[float] = Field(None, description="Other income")
    total_income: Optional[float] = Field(None, description="Total income")
    virtual_currency_transactions: Optional[bool] = Field(None, description="Whether the taxpayer received, sold, exchanged or otherwise acquired financial interest in virtual currency")


class Adjustments(BaseModel):
    charitable_standard_deduction: Optional[float] = Field(None, description="Charitable contributions if taking the standard deduction")
    total_adjustments: Optional[float] = Field(None, description="Total adjustments to income")
    adjusted_gross_income: Optional[float] = Field(None, description="Adjusted gross income (AGI)")


class Deductions(BaseModel):
    standard_deduction: Optional[float] = Field(None, description="Standard deduction amount")
    itemized_deductions: Optional[float] = Field(None, description="Total itemized deductions amount")
    qualified_business_income: Optional[float] = Field(None, description="Qualified business income deduction")
    total_deductions: Optional[float] = Field(None, description="Total deductions")
    taxable_income: Optional[float] = Field(None, description="Taxable income")
    standard_deduction_checked: Optional[bool] = Field(None, description="Whether standard deduction was selected")
    born_before_cutoff_date: Optional[bool] = Field(None, description="Whether taxpayer was born before the cutoff date for additional standard deduction")
    spouse_born_before_cutoff_date: Optional[bool] = Field(None, description="Whether spouse was born before the cutoff date for additional standard deduction")
    blind: Optional[bool] = Field(None, description="Whether taxpayer is blind (affects standard deduction)")
    spouse_blind: Optional[bool] = Field(None, description="Whether spouse is blind (affects standard deduction)")
    claimed_as_dependent: Optional[bool] = Field(None, description="Whether taxpayer can be claimed as a dependent on another return")
    spouse_claimed_as_dependent: Optional[bool] = Field(None, description="Whether spouse can be claimed as a dependent on another return")


class TaxAndCredits(BaseModel):
    tax: Optional[float] = Field(None, description="Tax amount calculated based on taxable income")
    child_tax_credit: Optional[float] = Field(None, description="Child tax credit/credit for other dependents")
    total_credits: Optional[float] = Field(None, description="Total credits")
    net_tax: Optional[float] = Field(None, description="Tax minus credits")
    forms_8814_tax: Optional[bool] = Field(None, description="Whether tax includes amount from Form 8814")
    form_4972_tax: Optional[bool] = Field(None, description="Whether tax includes amount from Form 4972")


class OtherTaxes(BaseModel):
    self_employment_tax: Optional[float] = Field(None, description="Self-employment tax")
    total_other_taxes: Optional[float] = Field(None, description="Total other taxes")
    total_tax: Optional[float] = Field(None, description="Total tax")


class Payments(BaseModel):
    federal_tax_withheld: Optional[float] = Field(None, description="Federal income tax withheld from Forms W-2 and 1099")
    form_w2_withheld: Optional[float] = Field(None, description="Federal income tax withheld from Forms W-2")
    form_1099_withheld: Optional[float] = Field(None, description="Federal income tax withheld from Forms 1099")
    other_forms_withheld: Optional[float] = Field(None, description="Federal income tax withheld from other forms")
    estimated_tax_payments: Optional[float] = Field(None, description="Estimated tax payments and amount applied from previous year's return")
    earned_income_credit: Optional[float] = Field(None, description="Earned income credit (EIC)")
    additional_child_tax_credit: Optional[float] = Field(None, description="Additional child tax credit")
    american_opportunity_credit: Optional[float] = Field(None, description="American opportunity credit")
    recovery_rebate_credit: Optional[float] = Field(None, description="Recovery rebate credit")
    net_premium_tax_credit: Optional[float] = Field(None, description="Net premium tax credit")
    amount_paid_with_extension: Optional[float] = Field(None, description="Amount paid with request for extension to file")
    excess_social_security: Optional[float] = Field(None, description="Excess social security and tier 1 RRTA tax withheld")
    credit_for_federal_tax: Optional[float] = Field(None, description="Credit for federal tax on fuels")
    total_payments: Optional[float] = Field(None, description="Total payments")


class RefundOrAmountOwed(BaseModel):
    overpaid_amount: Optional[float] = Field(None, description="Amount overpaid (if total payments > total tax)")
    refund_amount: Optional[float] = Field(None, description="Amount to be refunded")
    routing_number: Optional[str] = Field(None, description="Bank routing number for direct deposit of refund")
    account_number: Optional[str] = Field(None, description="Bank account number for direct deposit of refund")
    account_type: Optional[Literal["Checking", "Savings"]] = Field(None, description="Bank account type for direct deposit")
    applied_to_next_year: Optional[float] = Field(None, description="Amount applied to next year's estimated tax")
    amount_owed: Optional[float] = Field(None, description="Amount owed (if total tax > total payments)")
    estimated_tax_penalty: Optional[float] = Field(None, description="Estimated tax penalty")


class ThirdPartyDesignee(BaseModel):
    allow_discussion: Optional[bool] = Field(None, description="Whether taxpayer allows a third party to discuss the return with the IRS")
    name: Optional[str] = Field(None, description="Name of third party designee")
    phone_number: Optional[str] = Field(None, description="Phone number of third party designee")
    personal_identification_number: Optional[str] = Field(None, description="Personal identification number (PIN) for third party designee")


class Form1040TaxStatement(BaseModel):
    tax_year: Optional[int] = Field(None, description="Tax year for which the return is filed, e.g., 2023")
    filing_status: Optional[FilingStatus] = Field(None, description="Filing status for tax return")
    taxpayer: Optional[TaxpayerInfo] = Field(None, description="Information about the primary taxpayer")
    spouse: Optional[SpouseInfo] = Field(None, description="Information about the spouse, if applicable")
    address: Optional[Address] = Field(None, description="Mailing address for the taxpayer")
    dependents: Optional[List[Dependent]] = Field(None, description="List of dependents claimed on the tax return")
    income: Optional[Income] = Field(None, description="Income information from various sources")
    adjustments: Optional[Adjustments] = Field(None, description="Adjustments to income")
    deductions: Optional[Deductions] = Field(None, description="Standard or itemized deductions")
    tax_and_credits: Optional[TaxAndCredits] = Field(None, description="Tax calculation and credits")
    other_taxes: Optional[OtherTaxes] = Field(None, description="Additional taxes owed")
    payments: Optional[Payments] = Field(None, description="Tax payments already made")
    refund_or_amount_owed: Optional[RefundOrAmountOwed] = Field(None, description="Final calculation of refund or amount owed")
    third_party_designee: Optional[ThirdPartyDesignee] = Field(None, description="Information about third party authorized to discuss the return with the IRS")
    preparer_name: Optional[str] = Field(None, description="Tax preparer's name if prepared by someone other than taxpayer")
    preparer_signature: Optional[str] = Field(None, description="Tax preparer's signature")
    preparer_ptin: Optional[str] = Field(None, description="Tax preparer's PTIN (Preparer Tax Identification Number)")
    preparer_self_employed: Optional[bool] = Field(None, description="Whether the tax preparer is self-employed")
    preparer_firm_name: Optional[str] = Field(None, description="Name of tax preparer's firm")
    preparer_firm_ein: Optional[str] = Field(None, description="EIN of tax preparer's firm")
    preparer_firm_address: Optional[str] = Field(None, description="Address of tax preparer's firm")
    preparer_firm_phone: Optional[str] = Field(None, description="Phone number of tax preparer's firm")
    daytime_phone_number: Optional[str] = Field(None, description="Taxpayer's daytime phone number")
    email_address: Optional[str] = Field(None, description="Taxpayer's email address")
    presidential_election_fund_taxpayer: Optional[bool] = Field(None, description="Whether taxpayer wants $3 to go to the Presidential Election Campaign Fund")
    presidential_election_fund_spouse: Optional[bool] = Field(None, description="Whether spouse wants $3 to go to the Presidential Election Campaign Fund")
    identity_protection_pin: Optional[str] = Field(None, description="Identity Protection PIN provided by the IRS")
    spouse_identity_protection_pin: Optional[str] = Field(None, description="Identity Protection PIN provided by the IRS for spouse")
    