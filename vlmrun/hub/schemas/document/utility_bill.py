from datetime import date
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ChargeDetail(BaseModel):
    description: Optional[str] = Field(None, description="Description of the specific charge or service.")
    amount: Optional[float] = Field(None, description="Amount charged for the specific service or item.")
    currency: Optional[str] = Field(None, description="3-letter currency code for the amount, if different from the main bill currency.")
    usage: Optional[str] = Field(None, description="Usage details, such as '31 kWh' or '10 CCF'.")
    rate: Optional[float] = Field(None, description="Rate per unit for the service or item.")
    period_start: Optional[date] = Field(None, description="Start date for this specific charge, if applicable.")
    period_end: Optional[date] = Field(None, description="End date for this specific charge, if applicable.")


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address, including apartment or suite number.")
    city: Optional[str] = Field(None, description="City of the address.")
    state: Optional[str] = Field(None, description="State, province, or region of the address.")
    zip_code: Optional[str] = Field(None, description="Postal or ZIP code of the address.")
    country: Optional[str] = Field(None, description="Country of the address.")


class ProviderContactInfo(BaseModel):
    phone_numbers: Optional[List[str]] = Field(None, description="List of contact phone numbers for the provider.")
    email_addresses: Optional[List[str]] = Field(None, description="List of contact email addresses for the provider.")
    websites: Optional[List[str]] = Field(
        None, description="List of relevant websites for the provider (e.g., customer portal, payment page)."
    )
    customer_service_hours: Optional[str] = Field(None, description="Operating hours for customer service.")


class UsageDetail(BaseModel):
    period_description: str = Field(
        ..., description="Description of the period (e.g., 'Current Period', 'Last Period', 'Year Ago Period')."
    )
    usage_value: float = Field(..., description="The usage value for that period.")
    # unit is part of the parent UsageSummary


class UsageSummary(BaseModel):
    service_type: str = Field(..., description="Type of service (e.g., 'Electric', 'Gas', 'Water').")
    unit: str = Field(..., description="Unit of measurement for the usage_value (e.g., 'kWh', 'Therms', 'Gallons').")
    details: List[UsageDetail] = Field(..., description="List of usage details for different periods or categories.")
    meter_number: Optional[str] = Field(None, description="Identifier for the meter associated with this usage.")
    reading_type: Optional[str] = Field(None, description="Type of reading (e.g., 'Actual', 'Estimated').")


class UtilityBill(BaseModel):
    # Provider Information
    provider_name: Optional[str] = Field(None, description="Name of the utility provider .")
    provider_address: Optional[Address] = Field(None, description="Address of the utility provider.")
    provider_logo_description: Optional[str] = Field(None, description="Textual description of the provider's logo if present.")
    contact_information: Optional[ProviderContactInfo] = Field(
        None, description="Contact details for the utility provider."
    )

    # Account and Statement Information
    account_number: Optional[str] = Field(None, description="The unique identifier for the utility account.")
    statement_date: Optional[date] = Field(None, description="The date the bill or statement was issued (previously date_mailed).")
    statement_title: Optional[str] = Field(None, description="Title of the statement (e.g., 'ENERGY STATEMENT', 'Water Bill').")
    invoice_number: Optional[str] = Field(None, description="Invoice or bill number, if different from account number.") # Added for completeness

    # Customer Information
    service_for: Optional[str] = Field(None, description="Name of the entity or person the service is billed to.")
    service_address: Optional[Address] = Field(None, description="The address where the utility services are provided.")
    billing_address: Optional[Address] = Field(None, description="The mailing address for the bill, if different from service address.") # Added for completeness

    # Billing Period and Due Dates
    billing_period_start: Optional[date] = Field(None, description="The start date of the billing period covered by this bill.")
    billing_period_end: Optional[date] = Field(None, description="The end date of the billing period covered by this bill.")
    date_due: Optional[date] = Field(None, description="The due date for bill payment.")

    # Financial Summary
    currency: Optional[str] = Field(None, description="3-letter currency code for amounts on the bill (e.g., USD, CAD, EUR).")
    amount_due: Optional[float] = Field(None, description="The total amount payable by the due date.")
    previous_balance: Optional[float] = Field(None, description="The balance carried over from the previous billing cycle.")
    previous_unpaid_balance: Optional[float] = Field(
        None, description="Balance remaining from previous periods after payments were applied."
    )
    payment_received: Optional[float] = Field(None, description="Total payments received and applied since the last bill.")
    adjustments_credits: Optional[float] = Field(None, description="Total adjustments or credits applied during this billing period.") # Added for completeness
    current_charges: Optional[float] = Field(None, description="Total new charges for the current billing cycle.")
    
    # Charges Breakdown
    breakdown_of_charges: Optional[List[ChargeDetail]] = Field(
        None, description="Itemized list of charges, services, taxes, and fees with descriptions and amounts."
    )

    # Usage Information
    usage_summaries: Optional[List[UsageSummary]] = Field(
        None, description="Summaries of utility usage, possibly comparing different periods or types of service."
    )

    # Payment Information
    payment_options: Optional[List[str]] = Field(
        None, description="Accepted methods for bill payment (e.g., 'Online at provider.com/pay', 'Mail-in check')."
    )
    payment_instructions: Optional[str] = Field(
        None, description="Specific instructions for making a payment (e.g., 'Return this portion with your payment')."
    )
    payment_remittance_address: Optional[Address] = Field(None, description="Address to mail payments to.")

    # Miscellaneous
    important_messages: Optional[List[str]] = Field(
        None, description="List of important messages, announcements, or regulatory notices on the bill."
    )
    page_information: Optional[str] = Field(
        None, description="Page numbering or other page-specific information (e.g., 'Page 1 of 2')."
    )
    notes: Optional[str] = Field(None, description="General notes or miscellaneous information on the bill.") # Added for completeness
