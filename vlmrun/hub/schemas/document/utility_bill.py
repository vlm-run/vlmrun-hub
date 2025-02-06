from datetime import date
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ChargeDetail(BaseModel):
    description: Optional[str] = Field(None, description="Description of the specific charge or service.")
    amount: Optional[float] = Field(None, description="Amount charged for the specific service or item.")
    usage: Optional[str] = Field(None, description="Usage details, such as 31 kWh.")
    rate: Optional[float] = Field(None, description="Rate per unit for the service or item.")


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address where the service is provided.")
    city: Optional[str] = Field(None, description="City of the service address.")
    state: Optional[str] = Field(None, description="State or region of the service address.")
    zip_code: Optional[str] = Field(None, description="Postal code of the service address.")


class UtilityBill(BaseModel):
    account_number: Optional[str] = Field(None, description="The unique identifier for the utility account.")
    date_mailed: Optional[date] = Field(None, description="The date the bill was issued.")
    service_for: Optional[str] = Field(None, description="Name of the entity or person the service is billed to.")
    service_address: Optional[Address] = Field(None, description="The address where the utility services are provided.")
    billing_period_start: Optional[date] = Field(None, description="The start date of the billing period.")
    billing_period_end: Optional[date] = Field(None, description="The end date of the billing period.")
    date_due: Optional[date] = Field(None, description="The due date for bill payment.")
    amount_due: Optional[float] = Field(None, description="The total amount payable by the due date.")
    previous_balance: Optional[float] = Field(None, description="The unpaid balance from the last billing cycle.")
    payment_received: Optional[float] = Field(None, description="Payments applied since the last bill.")
    current_charges: Optional[float] = Field(None, description="Total charges for the current billing cycle.")
    breakdown_of_charges: Optional[List[ChargeDetail]] = Field(
        None, description="Itemized charges with descriptions, amounts, and optionally usage/rates."
    )
    payment_options: Optional[List[str]] = Field(None, description="Accepted methods for bill payment.")
    contact_information: Optional[Dict] = Field(
        None, description="Relevant contact numbers for customer support or emergencies."
    )
