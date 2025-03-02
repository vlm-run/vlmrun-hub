from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State or province")
    postal_code: Optional[str] = Field(None, description="Postal code or ZIP code")
    country: Optional[str] = Field(None, description="Country")


class Contact(BaseModel):
    phone: Optional[str] = Field(None, description="Phone number")
    email: Optional[str] = Field(None, description="Email address")
    fax: Optional[str] = Field(None, description="Fax number")


class Party(BaseModel):
    name: Optional[str] = Field(None, description="Name of the party")
    address: Optional[Address] = Field(None, description="Address of the party")
    contact: Optional[Contact] = Field(None, description="Contact information (phone, email, etc.)")
    reference: Optional[str] = Field(None, description="Reference number or identifier")


class Container(BaseModel):
    number: Optional[str] = Field(None, description="Container number")
    seal_number: Optional[str] = Field(None, description="Seal number")
    type: Optional[str] = Field(None, description="Container type")
    weight: Optional[float] = Field(None, description="Weight of the container")
    measurement: Optional[str] = Field(None, description="Measurement or dimensions of the container")


class Goods(BaseModel):
    description: Optional[str] = Field(None, description="Description of the goods")
    packages: Optional[int] = Field(None, description="Number of packages")
    package_type: Optional[str] = Field(None, description="Type of packages (cartons, pallets, etc.)")
    weight: Optional[float] = Field(None, description="Weight of the goods")
    weight_unit: Optional[str] = Field(None, description="Unit of weight measurement (kg, lb, etc.)")
    volume: Optional[float] = Field(None, description="Volume of the goods")
    volume_unit: Optional[str] = Field(None, description="Unit of volume measurement (cbm, cft, etc.)")
    marks_and_numbers: Optional[str] = Field(None, description="Marks and numbers on the packages")
    dangerous_goods_info: Optional[str] = Field(None, description="Information about dangerous goods, if applicable")


class FreightDetails(BaseModel):
    freight_terms: Optional[str] = Field(None, description="Terms of freight (prepaid, collect, etc.)")
    freight_charges: Optional[float] = Field(None, description="Freight charges amount")
    currency: Optional[str] = Field(None, description="Currency of the freight charges")
    additional_charges: Optional[List[dict]] = Field(None, description="Additional charges or fees")
    payment_method: Optional[str] = Field(None, description="Method of payment")


class BillOfLading(BaseModel):
    bill_number: Optional[str] = Field(None, description="Bill of Lading number")
    booking_number: Optional[str] = Field(None, description="Booking or reference number")
    issue_date: Optional[date] = Field(None, description="Date of issue of the Bill of Lading")
    
    shipper: Optional[Party] = Field(None, description="Shipper or exporter information")
    consignee: Optional[Party] = Field(None, description="Consignee or importer information")
    notify_party: Optional[Party] = Field(None, description="Notify party information")
    forwarding_agent: Optional[Party] = Field(None, description="Forwarding agent information")
    
    vessel_name: Optional[str] = Field(None, description="Name of the vessel")
    voyage_number: Optional[str] = Field(None, description="Voyage number")
    carrier: Optional[str] = Field(None, description="Carrier or shipping line")
    
    port_of_loading: Optional[str] = Field(None, description="Port of loading")
    port_of_discharge: Optional[str] = Field(None, description="Port of discharge")
    place_of_receipt: Optional[str] = Field(None, description="Place of receipt")
    place_of_delivery: Optional[str] = Field(None, description="Place of delivery")
    
    containers: Optional[List[Container]] = Field(None, description="List of containers")
    goods: Optional[Goods] = Field(None, description="Details of the goods being shipped")
    
    freight_details: Optional[FreightDetails] = Field(None, description="Freight and payment details")
    
    special_instructions: Optional[str] = Field(None, description="Special instructions or remarks")
    
    number_of_original_bills: Optional[int] = Field(None, description="Number of original Bills of Lading issued")
    
    signature_place: Optional[str] = Field(None, description="Place of signature")
    signature_date: Optional[date] = Field(None, description="Date of signature")
    signatory: Optional[str] = Field(None, description="Name or title of the signatory")
