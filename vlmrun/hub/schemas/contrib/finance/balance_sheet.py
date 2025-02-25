from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


class HeaderInformation(BaseModel):
    company_name: Optional[str] = Field(None, description="Name of the company")
    report_title: Optional[str] = Field(None, description="Title of the report (e.g., 'Consolidated Balance Sheet')")
    reporting_date: Optional[date] = Field(None, description="Date of the balance sheet")
    reporting_period: Optional[str] = Field(None, description="Period covered by the report (e.g., 'As of December 31, 2023')")
    currency: Optional[str] = Field(None, description="Currency used in the report (e.g., 'USD', 'EUR')")
    units: Optional[str] = Field(None, description="Units of measurement (e.g., 'in millions', 'in thousands')")
    accounting_standard: Optional[str] = Field(None, description="Accounting standard used (e.g., 'IFRS', 'GAAP')")
    is_consolidated: Optional[bool] = Field(None, description="Whether this is a consolidated statement")
    auditor: Optional[str] = Field(None, description="Name of the auditing firm")
    audit_opinion: Optional[str] = Field(None, description="Type of audit opinion (e.g., 'Unqualified', 'Qualified')")


class CurrentAssets(BaseModel):
    cash_and_equivalents: Optional[float] = Field(None, description="Cash and highly liquid assets convertible to cash within 90 days")
    marketable_securities: Optional[float] = Field(None, description="Short-term investments that can be readily converted to cash")
    accounts_receivable: Optional[float] = Field(None, description="Money owed to the company by customers for goods/services delivered")
    inventories: Optional[float] = Field(None, description="Raw materials, work-in-progress, and finished goods held for sale")
    prepaid_expenses: Optional[float] = Field(None, description="Expenses paid in advance that haven't yet been incurred")
    other_current_assets: Optional[float] = Field(None, description="Any other assets expected to be converted to cash within one year")
    total_current_assets: Optional[float] = Field(None, description="Sum of all current assets")


class NonCurrentAssets(BaseModel):
    property_plant_equipment: Optional[float] = Field(None, description="Net value of physical assets like buildings, machinery, and equipment")  
    intangible_assets: Optional[float] = Field(None, description="Non-physical assets like patents, trademarks, goodwill, and software")
    long_term_investments: Optional[float] = Field(None, description="Investments intended to be held for more than one year")
    other_non_current_assets: Optional[float] = Field(None, description="Any other assets not expected to be converted to cash within one year")
    total_non_current_assets: Optional[float] = Field(None, description="Sum of all non-current assets")


class Assets(BaseModel):
    current_assets: Optional[CurrentAssets] = Field(None, description="Assets expected to be converted to cash within one year")
    non_current_assets: Optional[NonCurrentAssets] = Field(None, description="Assets expected to provide economic benefits beyond one year")
    total_assets: Optional[float] = Field(None, description="Sum of all assets (current and non-current)")


class CurrentLiabilities(BaseModel):
    accounts_payable: Optional[float] = Field(None, description="Money owed to suppliers for goods/services received")
    short_term_debt: Optional[float] = Field(None, description="Debt due within one year, including current portion of long-term debt")            
    accrued_expenses: Optional[float] = Field(None, description="Expenses recognized but not yet paid")
    income_taxes_payable: Optional[float] = Field(None, description="Taxes owed but not yet paid")
    deposits: Optional[float] = Field(None, description="Customer deposits or other funds held temporarily")                   
    other_current_liabilities: Optional[float] = Field(None, description="Any other obligations due within one year")
    total_current_liabilities: Optional[float] = Field(None, description="Sum of all current liabilities")


class NonCurrentLiabilities(BaseModel):
    long_term_debt: Optional[float] = Field(None, description="Debt obligations due beyond one year")
    lease_liabilities: Optional[float] = Field(None, description="Long-term lease obligations")
    other_non_current_liabilities: Optional[float] = Field(None, description="Any other obligations due beyond one year")
    total_non_current_liabilities: Optional[float] = Field(None, description="Sum of all non-current liabilities")


class Liabilities(BaseModel):
    current_liabilities: Optional[CurrentLiabilities] = Field(None, description="Obligations due within one year")
    non_current_liabilities: Optional[NonCurrentLiabilities] = Field(None, description="Obligations due beyond one year")
    total_liabilities: Optional[float] = Field(None, description="Sum of all liabilities (current and non-current)")


class ShareholdersEquity(BaseModel):
    common_stock: Optional[float] = Field(None, description="Par value of issued common shares")
    preferred_stock: Optional[float] = Field(None, description="Par value of issued preferred shares")
    additional_paid_in_capital: Optional[float] = Field(None, description="Amount paid by shareholders above par value")
    retained_earnings: Optional[float] = Field(None, description="Accumulated profits not distributed to shareholders")
    total_equity: Optional[float] = Field(None, description="Sum of all shareholders' equity components")


class BalanceSheet(BaseModel):
    header: Optional[HeaderInformation] = Field(None, description="General information about the company and report")
    assets: Optional[Assets] = Field(None, description="Resources owned or controlled by the company")
    liabilities: Optional[Liabilities] = Field(None, description="Obligations and debts owed by the company")
    equity: Optional[ShareholdersEquity] = Field(None, description="Residual interest in the assets after deducting liabilities")
