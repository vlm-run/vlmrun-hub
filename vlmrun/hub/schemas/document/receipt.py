from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    postal_code: Optional[str] = Field(None, description="Postal code")
    country: Optional[str] = Field(None, description="Country")


class Item(BaseModel):
    description: str = Field(..., description="Description or name of the item")
    quantity: Optional[float] = Field(None, description="Quantity of the item")
    unit_price: Optional[float] = Field(None, description="Unit price of the item")
    total_price: Optional[float] = Field(None, description="Total price of the item")


class PaymentMethod(BaseModel):
    type: str = Field(..., description="Type of payment (e.g., cash, credit card, debit card)")
    card_last_4: Optional[str] = Field(None, description="Last 4 digits of the card if applicable")
    card_type: Optional[str] = Field(None, description="Type of card if applicable")


class Receipt(BaseModel):
    receipt_id: Optional[str] = Field(None, description="Unique receipt identifier")
    transaction_date: Optional[datetime] = Field(None, description="Date and time of the transaction")

    merchant_name: Optional[str] = Field(None, description="Name of the merchant")
    merchant_address: Optional[Address] = Field(None, description="Address of the merchant")
    merchant_phone: Optional[str] = Field(None, description="Phone number of the merchant")

    cashier_name: Optional[str] = Field(None, description="Name of the cashier")
    register_number: Optional[str] = Field(None, description="Register or POS terminal number")

    customer_name: Optional[str] = Field(None, description="Name of the customer if provided")
    customer_id: Optional[str] = Field(None, description="Customer ID or loyalty number if applicable")

    items: List[Item] = Field(..., description="Items purchased")

    subtotal: Optional[float] = Field(None, description="Subtotal of the purchase")
    tax: Optional[float] = Field(None, description="Tax amount")
    total: float = Field(..., description="Total amount of the purchase")
    currency: str = Field(..., description="Currency of the transaction")

    payment_method: PaymentMethod = Field(..., description="Method of payment")

    discount_amount: Optional[float] = Field(None, description="Amount of discount applied")
    discount_description: Optional[str] = Field(None, description="Description of the discount")

    tip_amount: Optional[float] = Field(None, description="Tip amount if applicable")

    return_policy: Optional[str] = Field(None, description="Return policy information")

    barcode: Optional[str] = Field(None, description="Barcode or QR code data if present")

    additional_charges: Optional[List[Dict]] = Field(None, description="Any additional charges (e.g., service fees)")

    notes: Optional[str] = Field(None, description="Any additional notes or comments")
    others: Optional[Dict[str, Any]] = Field(
        None, description="Other information on the receipt not captured by other fields"
    )
