from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address including building number")
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State or province")
    zip_code: Optional[str] = Field(None, description="ZIP or postal code")


class EmployerInfo(BaseModel):
    name: Optional[str] = Field(None, description="Name of the employer or company")
    address: Optional[Address] = Field(None, description="Employer's address")


class EmployeeInfo(BaseModel):
    name: Optional[str] = Field(None, description="Full name of the employee")
    employee_id: Optional[str] = Field(None, description="Employee identification number")
    department: Optional[str] = Field(None, description="Employee's department")
    position: Optional[str] = Field(None, description="Employee's job title or position")
    date_of_joining: Optional[date] = Field(None, description="Date when employee joined the company")


class PayPeriod(BaseModel):
    period: Optional[str] = Field(None, description="Pay period (e.g., 'August 2021')")
    days_worked: Optional[int] = Field(None, description="Number of days worked in the period")


class EarningsItem(BaseModel):
    description: str = Field(..., description="Description of the earnings (e.g., 'Basic', 'Incentive Pay')")
    amount: Optional[float] = Field(None, description="Amount for this earnings type")


class DeductionItem(BaseModel):
    description: str = Field(..., description="Description of the deduction (e.g., 'Provident Fund', 'Tax')")
    amount: Optional[float] = Field(None, description="Amount deducted")


class Payslip(BaseModel):
    employer: Optional[EmployerInfo] = Field(None, description="Information about the employer")
    employee: Optional[EmployeeInfo] = Field(None, description="Information about the employee")
    pay_period: Optional[PayPeriod] = Field(None, description="Pay period details")
    earnings: Optional[List[EarningsItem]] = Field(None, description="List of earnings items")
    deductions: Optional[List[DeductionItem]] = Field(None, description="List of deduction items")
    total_earnings: Optional[float] = Field(None, description="Total earnings amount")
    total_deductions: Optional[float] = Field(None, description="Total deductions amount")
    net_pay: Optional[float] = Field(None, description="Net pay amount after all deductions")
    currency: Optional[str] = Field(None, description="Currency code (e.g., 'USD', 'EUR', 'INR')")
    net_pay_in_words: Optional[str] = Field(None, description="Net pay amount expressed in words")