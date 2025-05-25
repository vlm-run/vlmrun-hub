from datetime import date
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State/Province code or name")
    zip_code: Optional[str] = Field(None, description="Postal code")


class BankTransaction(BaseModel):
    # Original fields - descriptions updated for clarity
    transaction_deposit: Optional[float] = Field(None, description="Deposit amount, if this transaction is a deposit.")
    transaction_deposit_date: Optional[date] = Field(None, description="Date of the deposit, if this transaction is a deposit.")
    transaction_deposit_description: Optional[str] = Field(None, description="Description of the deposit, if this transaction is a deposit.")
    transaction_withdrawal: Optional[float] = Field(None, description="Withdrawal amount, if this transaction is a withdrawal.")
    transaction_withdrawal_date: Optional[date] = Field(None, description="Date of the withdrawal, if this transaction is a withdrawal.")
    transaction_withdrawal_description: Optional[str] = Field(None, description="Description of the withdrawal, if this transaction is a withdrawal.")

    # New fields added based on examples
    check_number: Optional[str] = Field(None, description="Check number associated with the transaction, if applicable (e.g., for check payments or cashed checks).")
    ending_daily_balance: Optional[float] = Field(None, description="The running daily balance of the account after this transaction, if provided on the transaction line.")
    reference_number: Optional[str] = Field(None, description="A specific reference number or transaction ID for this item, if provided in the transaction line (e.g., for deposits, ATM transactions).")


class BankStatement(BaseModel):
    # Existing fields - descriptions may be slightly enhanced for clarity
    account_number: Optional[str] = Field(None, description="Bank account number associated with the statement.")
    account_type: Optional[str] = Field(None, description="Type of the bank account (e.g., Checking, Savings, 'CONNECTIONS CHECKING').")
    bank_address: Optional[Address] = Field(None, description="Address of the banking institution.")
    bank_name: Optional[str] = Field(None, description="Name of the banking institution.")
    client_address: Optional[Address] = Field(None, description="Address of the account holder(s).")
    client_name: Optional[str] = Field(None, description="Name of the account holder(s). If multiple, may be a concatenated string (e.g., 'Rachael Dean, Calvin Carrillo').")
    ending_balance: Optional[float] = Field(None, description="The final balance of the account at the end of the statement period.")
    starting_balance: Optional[float] = Field(None, description="The balance of the account at the beginning of the statement period.")
    statement_date: Optional[date] = Field(None, description="The date the statement was issued or generated.")
    statement_start_date: Optional[date] = Field(None, description="The first day of the period covered by this statement.")
    statement_end_date: Optional[date] = Field(None, description="The last day of the period covered by this statement.")
    table_item: Optional[List[BankTransaction]] = Field(None, description="A list of individual financial transactions (deposits, withdrawals, checks, etc.) detailed in the statement.")
    
    # New fields added based on examples
    routing_number: Optional[str] = Field(None, description="Bank's routing transit number (RTN), if provided on the statement.")
    total_deposits: Optional[float] = Field(None, description="Summary total of all deposits and other credits for the statement period, as per the statement's summary section.")
    total_withdrawals: Optional[float] = Field(None, description="Summary total of all withdrawals, payments, and other debits for the statement period, as per the statement's summary section.")
    
    # More specific summary totals if available 
    summary_total_atm_withdrawals: Optional[float] = Field(None, description="Total amount of ATM withdrawals as reported in a summary section of the statement, if available.")
    summary_total_debit_card_purchases: Optional[float] = Field(None, description="Total amount of debit card purchases (e.g., VISA Check Card) as reported in a summary section, if available.")
    summary_total_checks_paid: Optional[float] = Field(None, description="Total amount of checks paid as reported in a summary section, if available (this may differ from a sum of individual check transactions if the summary is specific).")
    
    monthly_service_fee: Optional[float] = Field(None, description="Amount of the monthly service fee charged during the statement period, if any.")
    overdraft_protection_status: Optional[str] = Field(None, description="Textual description of the overdraft protection status or related services on the account, if mentioned.")

    # Existing 'others' field for flexibility
    others: Optional[Dict] = Field(None, description="A dictionary for any other relevant data extracted from the statement that does not fit into the predefined fields.")
