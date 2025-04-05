from pydantic import BaseModel, Field
from typing import Optional, Literal, List

class Address(BaseModel):
    building_street: Optional[str] = Field(default=None, description="The building and street portion of the address.")
    town_city: Optional[str] = Field(default=None, description="The town or city of the address.")
    county_state: Optional[str] = Field(default=None, description="The county or state of the address, if provided.")
    postcode_zip: Optional[str] = Field(default=None, description="The postcode or ZIP code of the address.")

class Party(BaseModel):
    name: Optional[str] = Field(default=None, description="The full name of the claimant or defendant.")
    address: Optional[Address] = Field(default=None, description="The address of the party.")
    phone: Optional[str] = Field(default=None, description="The phone number of the party.")
    email: Optional[str] = Field(default=None, description="The email address of the party, if provided.")

class FinancialDetails(BaseModel):
    amount_claimed: Optional[float] = Field(default=None, description="The amount claimed in the legal action, in the local currency.")
    court_fee: Optional[float] = Field(default=None, description="The court filing fee, if applicable.")
    legal_representative_costs: Optional[float] = Field(default=None, description="Costs associated with legal representation.")
    total_amount: Optional[float] = Field(default=None, description="The total amount including all fees and costs.")

class VulnerabilityDetails(BaseModel):
    is_vulnerable: Optional[bool] = Field(default=None, description="Indicates if the claimant or a witness is vulnerable.")
    details: Optional[str] = Field(default=None, description="Explanation of the vulnerability and requested accommodations.")
    human_rights_issues: Optional[bool] = Field(default=None, description="Indicates if the claim involves Human Rights Act issues.")

class SignatureDetails(BaseModel):
    signatory_type: Optional[Literal["claimant", "litigation_friend", "legal_representative"]] = Field(default=None, description="The type of person signing the form.")
    date: Optional[str] = Field(default=None, description="The date the form was signed, in any format present.")
    full_name: Optional[str] = Field(default=None, description="The full name of the signatory.")
    legal_firm: Optional[str] = Field(default=None, description="The name of the legal firm, if signed by a representative.")
    position: Optional[str] = Field(default=None, description="The position or title of the signatory, if applicable.")

class ContactDetails(BaseModel):
    phone: Optional[str] = Field(default=None, description="Contact phone number for correspondence.")
    dx_number: Optional[str] = Field(default=None, description="Document exchange number, if applicable.")
    reference: Optional[str] = Field(default=None, description="Reference number for correspondence.")
    email: Optional[str] = Field(default=None, description="Contact email address for correspondence.")

# Main schema for legal claim forms
class LegalClaim(BaseModel):
    court_name: Optional[str] = Field(default=None, description="The name of the court handling the claim (e.g., Cambridge County Court).")
    fee_account_number: Optional[str] = Field(default=None, description="The fee account number associated with the claim.")
    # Parties involved in the claim
    claimant: Optional[List[Party]] = Field(default=None, description="Details of the claimant(s) filing the claim.")
    defendant: Optional[List[Party]] = Field(default=None, description="Details of the defendant(s) being sued.")
    brief_details_of_claim: Optional[str] = Field(default=None, description="A brief description of the claim (e.g., breach of contract, damages).")
    claim_value: Optional[float] = Field(default=None, description="The monetary value of the claim, if specified separately from financial details.")
    financial_details: Optional[FinancialDetails] = Field(default=None, description="Breakdown of financial amounts related to the claim.")
    preferred_hearing_centre: Optional[str] = Field(default=None, description="The preferred county court hearing centre for hearings.")
    vulnerability_details: Optional[VulnerabilityDetails] = Field(default=None, description="Details about vulnerability considerations.")
    particulars_of_claim: Optional[str] = Field(default=None, description="Detailed particulars of the claim, if provided or attached.")
    particulars_status: Optional[Literal["attached", "to_follow"]] = Field(default=None, description="Status of the particulars of claim document.")
    signature_details: Optional[SignatureDetails] = Field(default=None, description="Details of the signature on the claim form.")
    contact_details: Optional[ContactDetails] = Field(default=None, description="Contact information for correspondence with the court or entity.")