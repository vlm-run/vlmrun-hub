from typing import List

from pydantic import BaseModel, Field


class UtilityBillDetail(BaseModel):
    description: str | None = Field(
        None, description="Description of the specific charge or service."
    )
    amount: float | None = Field(
        None, description="Amount charged for the specific service or item."
    )
    usage: str | None = Field(None, description="Usage details, such as 31 kWh.")
    rate: float | None = Field(
        None, description="Rate per unit for the service or item."
    )


class Address(BaseModel):
    street: str | None = Field(
        None, description="Street address where the service is provided."
    )
    city: str | None = Field(None, description="City of the service address.")
    state: str | None = Field(
        None, description="State or region of the service address."
    )
    zip_code: str | None = Field(
        None, description="Postal code of the service address."
    )


class UtilityBill(BaseModel):
    account_number: str = Field(
        ..., description="The unique identifier for the utility account."
    )
    date_mailed: str | None = Field(
        None, description="The date the bill was issued, in YYYY-MM-DD format."
    )
    service_for: str | None = Field(
        None, description="Name of the entity or person the service is billed to."
    )
    service_address: Address | None = Field(
        None, description="The address where the utility services are provided."
    )
    billing_period: str | None = Field(
        None,
        description="The time span for which the charges apply, in YYYY-MM-DD to YYYY-MM-DD format.",
    )
    date_due: str | None = Field(
        None, description="The due date for bill payment, in YYYY-MM-DD format."
    )
    amount_due: float | None = Field(
        None, description="The total amount payable by the due date."
    )
    previous_balance: float | None = Field(
        None, description="The unpaid balance from the last billing cycle."
    )
    payment_received: float | None = Field(
        None, description="Payments applied since the last bill."
    )
    current_charges: float | None = Field(
        None, description="Total charges for the current billing cycle."
    )
    breakdown_of_charges: List[UtilityBillDetail] | None = Field(
        None,
        description="Itemized charges with descriptions, amounts, and optionally usage/rates.",
    )
    payment_options: List[str] | None = Field(
        None, description="Accepted methods for bill payment."
    )
    contact_information: dict | None = Field(
        None,
        description="Relevant contact numbers for customer support or emergencies.",
    )
    important_notices: List[str] | None = Field(
        None,
        description="Any important notices or announcements from the utility company.",
    )
