from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State, province, or region")
    postal_code: Optional[str] = Field(None, description="Postal or ZIP code")
    country: Optional[str] = Field(None, description="Country")


class BankDetails(BaseModel):
    bank_name: Optional[str] = Field(None, description="Name of the bank")
    account_holder_name: Optional[str] = Field(None, description="Name of the account holder")
    account_number: Optional[str] = Field(None, description="Bank account number")
    routing_number: Optional[str] = Field(None, description="Bank routing number (e.g., ABA for US)")
    bsb_number: Optional[str] = Field(None, description="Branch Sort Code (BSB) or similar local bank code")
    iban: Optional[str] = Field(None, description="International Bank Account Number (IBAN)")
    swift_bic: Optional[str] = Field(None, description="SWIFT/BIC code")


class Item(BaseModel):
    description: Optional[str] = Field(None, description="Description or name of the item or service")
    quantity: Optional[float] = Field(None, description="Quantity of the item, which can be a float for hours or partial units")
    unit_price: Optional[float] = Field(None, description="Unit price or rate of the item")
    
    # This is typically quantity * unit_price.
    total_price: Optional[float] = Field(None, description="Total price for this line item, typically quantity multiplied by unit price, before item-specific adjustments/taxes")

    currency: Optional[str] = Field(None, description="3-digit currency code for this item, if it differs from the main invoice currency")

    item_tax_details: Optional[str] = Field(None, description="Tax details or rate specific to this item (e.g., 'VAT 0%[1]', 'Sales Tax Exempt')")
    item_adjustment_details: Optional[str] = Field(None, description="Adjustment or discount details specific to this item (e.g., '10% off promo', 'Volume discount')")
    # If item-level tax/adjustment amounts are needed, they can be added:
    # item_tax_amount: Optional[float] = Field(None, description="Tax amount for this specific item")
    # item_adjustment_amount: Optional[float] = Field(None, description="Adjustment/discount amount for this specific item")


class Invoice(BaseModel):
    # Core Invoice Information
    invoice_id: Optional[str] = Field(None, description="Unique invoice identifier or number")
    invoice_issue_date: Optional[date] = Field(None, description="Date when the invoice was issued")
    invoice_due_date: Optional[date] = Field(None, description="Date by which the invoice payment is due")
    period_start: Optional[date] = Field(None, description="Start date of the billing period covered by the invoice, if applicable")
    period_end: Optional[date] = Field(None, description="End date of the billing period covered by the invoice, if applicable")

    # Related Identifiers
    order_id: Optional[str] = Field(None, description="Unique order identifier related to this invoice, if applicable")
    customer_id: Optional[str] = Field(None, description="Unique customer identifier, if applicable")

    # Issuer Details
    issuer_name: Optional[str] = Field(None, description="Name of the invoice issuer (company or individual)")
    issuer_address: Optional[Address] = Field(None, description="Address of the invoice issuer")
    issuer_email: Optional[str] = Field(None, description="Email address of the invoice issuer")
    issuer_phone: Optional[str] = Field(None, description="Phone number of the invoice issuer")
    issuer_vat_id: Optional[str] = Field(None, description="VAT identification number or other tax ID of the issuer")
    issuer_website: Optional[str] = Field(None, description="Website of the invoice issuer")

    # Customer/Recipient Details
    customer_name: Optional[str] = Field(None, description="Name of the invoice recipient (company or individual)")
    customer_email: Optional[str] = Field(None, description="Email address of the recipient")
    customer_phone: Optional[str] = Field(None, description="Phone number of the recipient")
    customer_billing_address: Optional[Address] = Field(None, description="Billing address of the recipient")
    customer_shipping_address: Optional[Address] = Field(None, description="Shipping address of the recipient, if different from billing")
    customer_vat_id: Optional[str] = Field(None, description="VAT identification number or other tax ID of the customer")

    # Invoice Line Items
    items: Optional[List[Item]] = Field(None, description="List of items or services detailed in the invoice")

    # Financial Summary
    currency: Optional[str] = Field(None, description="Primary 3-digit currency code for the invoice amounts (e.g., USD, EUR)")
    subtotal: Optional[float] = Field(None, description="Total amount of all line items before any discounts, taxes, and shipping")
    
    discount_amount: Optional[float] = Field(None, description="Total discount amount applied to the invoice subtotal")
    discount_percentage: Optional[float] = Field(None, description="Overall discount percentage applied to the invoice")
    discount_description: Optional[str] = Field(None, description="Description of the discount applied (e.g., 'Early payment discount', 'Volume discount')")

    shipping_cost: Optional[float] = Field(None, description="Shipping and handling charges")
    shipping_description: Optional[str] = Field(None, description="Description of shipping charges or method")

    tax_amount: Optional[float] = Field(None, description="Total tax amount for the invoice")
    tax_percentage: Optional[float] = Field(None, description="Overall tax rate percentage applied to the taxable amount")
    tax_description: Optional[str] = Field(None, description="Description of the tax applied, such as type, rate, or jurisdiction")
    overall_tax_notes: Optional[str] = Field(None, description="Additional notes regarding taxes for the entire invoice (e.g., 'Tax to be paid on reverse charge basis')")

    total_amount: Optional[float] = Field(None, description="The final total amount of the invoice after all deductions and additions (subtotal - discounts + shipping + taxes)")
    amount_paid: Optional[float] = Field(None, description="Amount already paid by the customer towards this invoice")
    balance_due: Optional[float] = Field(None, description="Remaining amount due for payment (total_amount - amount_paid)")

    # Payment Information
    payment_terms: Optional[str] = Field(None, description="Payment terms and conditions (e.g., 'Net 30 days', 'Due upon receipt')")
    payment_instructions: Optional[str] = Field(None, description="Specific instructions for making payment")
    payment_link: Optional[str] = Field(None, description="A URL for online payment, if available")
    bank_details: Optional[BankDetails] = Field(None, description="Bank account details for payment transfers")

    # Miscellaneous
    notes: Optional[str] = Field(None, description="General notes, comments, or miscellaneous information on the invoice")
    terms_and_conditions: Optional[str] = Field(None, description="General terms and conditions related to the invoice or service")
    footer_text: Optional[str] = Field(None, description="Text appearing in the footer of the invoice (e.g., thank you message, company slogan)")
    page_information: Optional[str] = Field(None, description="Page numbering or other page-specific information (e.g., 'Page 1 of 1')")
    logo_url: Optional[str] = Field(None, description="URL of the company logo displayed on the invoice")
