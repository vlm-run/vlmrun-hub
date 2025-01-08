from datetime import date
from typing import List

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str | None = Field(None, description="Street address")
    city: str | None = Field(None, description="City")
    state: str | None = Field(None, description="State/Province code or name")
    zip_code: str | None = Field(None, description="Postal code", min_length=2, max_length=10)


class BankTransaction(BaseModel):
    transaction_deposit: float | None = Field(None, description="Deposit amount")
    transaction_deposit_date: date | None = Field(None, description="Date of the deposit")
    transaction_deposit_description: str | None = Field(None, description="Description of the deposit")
    transaction_withdrawal: float | None = Field(None, description="Withdrawal amount")
    transaction_withdrawal_date: date | None = Field(None, description="Date of the withdrawal")
    transaction_withdrawal_description: str | None = Field(None, description="Description of the withdrawal")


class BankStatement(BaseModel):
    account_number: str | None = Field(None, description="Bank account number")
    account_type: str | None = Field(None, description="Type of the bank account (e.g. Checking/Savings)")
    bank_address: Address | None = Field(None, description="Address of the bank")
    bank_name: str | None = Field(None, description="Name of the bank")
    client_address: Address | None = Field(None, description="Address of the client")
    client_name: str | None = Field(None, description="Name of the client")
    ending_balance: float | None = Field(None, description="Ending balance for the period")
    starting_balance: float | None = Field(None, description="Starting balance for the period")
    statement_date: date | None = Field(None, description="Overall statement date if applicable")
    statement_start_date: date | None = Field(None, description="Start date of the bank statement")
    statement_end_date: date | None = Field(None, description="End date of the bank statement")
    table_item: List[BankTransaction] | None = Field(None, description="List of transactions in the statement")
    others: dict | None = Field(None, description="Any other additional data from the statement")
