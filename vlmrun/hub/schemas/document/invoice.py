from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    postal_code: Optional[str] = Field(None, description="Postal code")
    country: Optional[str] = Field(None, description="Country")


class Item(BaseModel):
    description: Optional[str] = Field(None, description="Description or name of the item")
    quantity: Optional[int] = Field(None, description="Quantity of the item")
    currency: Optional[str] = Field(None, description="3-digit currency code")
    unit_price: Optional[float] = Field(None, description="Unit price of the item")
    total_price: Optional[float] = Field(None, description="Total price of the item")


class Invoice(BaseModel):
    invoice_id: Optional[str] = Field(None, description="Unique invoice identifier")
    period_start: Optional[date] = Field(None, description="Invoice period start date")
    period_end: Optional[date] = Field(None, description="Invoice period end date")
    invoice_issue_date: Optional[date] = Field(None, description="Issue date of the invoice")
    invoice_due_date: Optional[date] = Field(None, description="Due date of the invoice")

    order_id: Optional[str] = Field(None, description="Unique order identifier")
    customer_id: Optional[str] = Field(None, description="Unique customer identifier")
    issuer: Optional[str] = Field(None, description="Issuer of the invoice")
    issuer_address: Optional[Address] = Field(None, description="Issuer's address")

    customer: Optional[str] = Field(None, description="Recipient of the invoice")
    customer_email: Optional[str] = Field(None, description="Recipient's email")
    customer_phone: Optional[str] = Field(None, description="Recipient's phone")
    customer_billing_address: Optional[Address] = Field(None, description="Recipient's billing address")
    customer_shipping_address: Optional[Address] = Field(None, description="Recipient's shipping address")

    items: Optional[List[Item]] = Field(None, description="Items in the invoice")
    subtotal: Optional[float] = Field(None, description="Subtotal of the invoice")
    tax: Optional[float] = Field(None, description="Tax of the invoice")
    total: Optional[float] = Field(None, description="Total of the invoice")
    currency: Optional[str] = Field(None, description="Currency of the invoice")
    notes: Optional[str] = Field(None, description="Notes of the invoice")
