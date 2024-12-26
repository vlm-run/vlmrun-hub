from datetime import date
from typing import Any, List

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str | None = Field(None, description="Street address")
    city: str | None = Field(None, description="City")
    state: str | None = Field(None, description="State")
    postal_code: str | None = Field(None, description="Postal code")
    country: str | None = Field(None, description="Country")


class Item(BaseModel):
    description: str | None = Field(None, description="Description or name of the item")
    quantity: int | None = Field(None, description="Quantity of the item")
    currency: str | None = Field(None, description="3-digit currency code")
    unit_price: float | None = Field(None, description="Unit price of the item")
    total_price: float | None = Field(None, description="Total price of the item")


class Invoice(BaseModel):
    invoice_id: str | None = Field(None, description="Unique invoice identifier")
    period_start: date | None = Field(None, description="Invoice period start date")
    period_end: date | None = Field(None, description="Invoice period end date")
    invoice_issue_date: date | None = Field(None, description="Issue date of the invoice")
    invoice_due_date: date | None = Field(None, description="Due date of the invoice")

    order_id: str | None = Field(None, description="Unique order identifier")
    customer_id: str | None = Field(None, description="Unique customer identifier")
    issuer: str | None = Field(None, description="Issuer of the invoice")
    issuer_address: Address | None = Field(None, description="Issuer's address")

    customer: str | None = Field(None, description="Recipient of the invoice")
    customer_email: str | None = Field(None, description="Recipient's email")
    customer_phone: str | None = Field(None, description="Recipient's phone")
    customer_billing_address: Address | None = Field(None, description="Recipient's billing address")
    customer_shipping_address: Address | None = Field(None, description="Recipient's shipping address")

    items: List[Item] | None = Field(None, description="Items in the invoice")
    subtotal: float | None = Field(None, description="Subtotal of the invoice")
    tax: float | None = Field(None, description="Tax of the invoice")
    total: float | None = Field(None, description="Total of the invoice")
    currency: str | None = Field(None, description="Currency of the invoice")
    notes: str | None = Field(None, description="Notes of the invoice")
    others: dict[str, Any] | None = Field(
        None,
        description="Other information of the invoice not captured by other fields",
    )
