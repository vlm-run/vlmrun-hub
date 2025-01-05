from datetime import datetime
from typing import Any, List

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str | None = Field(None, description="Street address")
    city: str | None = Field(None, description="City")
    state: str | None = Field(None, description="State")
    postal_code: str | None = Field(None, description="Postal code")
    country: str | None = Field(None, description="Country")


class Item(BaseModel):
    description: str = Field(..., description="Description or name of the item")
    quantity: float | None = Field(None, description="Quantity of the item")
    unit_price: float | None = Field(None, description="Unit price of the item")
    total_price: float | None = Field(None, description="Total price of the item")


class PaymentMethod(BaseModel):
    type: str = Field(..., description="Type of payment (e.g., cash, credit card, debit card)")
    card_last_4: str | None = Field(None, description="Last 4 digits of the card if applicable")
    card_type: str | None = Field(None, description="Type of card if applicable")


class Receipt(BaseModel):
    receipt_id: str | None = Field(None, description="Unique receipt identifier")
    transaction_date: datetime | None = Field(None, description="Date and time of the transaction")

    merchant_name: str | None = Field(None, description="Name of the merchant")
    merchant_address: Address | None = Field(None, description="Address of the merchant")
    merchant_phone: str | None = Field(None, description="Phone number of the merchant")

    cashier_name: str | None = Field(None, description="Name of the cashier")
    register_number: str | None = Field(None, description="Register or POS terminal number")

    customer_name: str | None = Field(None, description="Name of the customer if provided")
    customer_id: str | None = Field(None, description="Customer ID or loyalty number if applicable")

    items: List[Item] = Field(..., description="Items purchased")

    subtotal: float | None = Field(None, description="Subtotal of the purchase")
    tax: float | None = Field(None, description="Tax amount")
    total: float = Field(..., description="Total amount of the purchase")
    currency: str = Field(..., description="Currency of the transaction")

    payment_method: PaymentMethod = Field(..., description="Method of payment")

    discount_amount: float | None = Field(None, description="Amount of discount applied")
    discount_description: str | None = Field(None, description="Description of the discount")

    tip_amount: float | None = Field(None, description="Tip amount if applicable")

    return_policy: str | None = Field(None, description="Return policy information")

    barcode: str | None = Field(None, description="Barcode or QR code data if present")

    additional_charges: List[dict] | None = Field(None, description="Any additional charges (e.g., service fees)")

    notes: str | None = Field(None, description="Any additional notes or comments")
    others: dict[str, Any] | None = Field(
        None, description="Other information on the receipt not captured by other fields"
    )
