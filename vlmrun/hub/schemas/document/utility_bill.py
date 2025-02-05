from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class ChargeDetail(BaseModel):
    description: Optional[str] = Field(None, description="Description of the specific charge or service.")
    amount: Optional[float] = Field(None, description="Amount charged for the specific service or item.")
    usage: Optional[str] = Field(None, description="Usage details, such as 31 kWh.")
    rate: Optional[float] = Field(None, description="Rate per unit for the service or item.")


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address where the service is provided.", max_length=128)
    city: Optional[str] = Field(None, description="City of the service address.", max_length=50)
    state: Optional[str] = Field(None, description="State or region of the service address.", max_length=2)
    zip_code: Optional[str] = Field(
        None, description="Postal code of the service address.", min_length=5, max_length=10
    )


class UtilityBill(BaseModel):
    account_number: str | None = Field(None, description="The unique identifier for the utility account.")
    date_mailed: date | None = Field(None, description="The date the bill was issued.")
    service_for: str | None = Field(None, description="Name of the entity or person the service is billed to.")
    service_address: Address | None = Field(None, description="The address where the utility services are provided.")
    billing_period_start: date | None = Field(None, description="The start date of the billing period.")
    billing_period_end: date | None = Field(None, description="The end date of the billing period.")
    date_due: date | None = Field(None, description="The due date for bill payment.")
    amount_due: float | None = Field(None, description="The total amount payable by the due date.")
    previous_balance: float | None = Field(None, description="The unpaid balance from the last billing cycle.")
    payment_received: float | None = Field(None, description="Payments applied since the last bill.")
    current_charges: float | None = Field(None, description="Total charges for the current billing cycle.")
    breakdown_of_charges: List[ChargeDetail] | None = Field(
        None, description="Itemized charges with descriptions, amounts, and optionally usage/rates."
    )
    payment_options: List[str] | None = Field(None, description="Accepted methods for bill payment.")
    contact_information: dict | None = Field(
        None, description="Relevant contact numbers for customer support or emergencies."
    )
