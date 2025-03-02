from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    postal_code: Optional[str] = Field(None, description="Postal code")
    country: Optional[str] = Field(None, description="Country")


class BankInformation(BaseModel):
    name: Optional[str] = Field(None, description="Name of the bank")
    address: Optional[Address] = Field(None, description="Address of the bank")
    routing_number: Optional[str] = Field(None, description="Bank routing number")
    account_number: Optional[str] = Field(None, description="Bank account number")


class BankCheck(BaseModel):
    check_number: Optional[str] = Field(None, description="Check number, typically printed in the top right corner of the check")
    payment_date: Optional[str] = Field(None, description="Date written on the check")
    payee: Optional[str] = Field(None, description="Name of the person or entity to whom the check is payable (Pay to the order of)")
    amount_numeric: Optional[float] = Field(None, description="Amount of the check in numeric form")
    amount_text: Optional[str] = Field(None, description="Amount of the check written out in words")
    bank_info: Optional[BankInformation] = Field(None, description="Information about the bank issuing the check")
    drawer_name: Optional[str] = Field(None, description="Name of the person writing the check (drawer)")
    drawer_address: Optional[Address] = Field(None, description="Address of the person writing the check")
    drawer_signature: Optional[bool] = Field(None, description="Whether the check is signed by the drawer")
    memo: Optional[str] = Field(None, description="Memo or note written on the check")
    micr_line: Optional[str] = Field(None, description="MICR (Magnetic Ink Character Recognition) line at the bottom of the check containing routing and account numbers")
    is_void: Optional[bool] = Field(None, description="Whether the check is marked as void")
    is_post_dated: Optional[bool] = Field(None, description="Whether the check is post-dated (date is in the future)")
    currency: Optional[str] = Field(None, description="Currency of the check")
