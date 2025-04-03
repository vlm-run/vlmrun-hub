from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List, Union

from pydantic import BaseModel, Field


class CompanyInfo(BaseModel):
    """Company information header"""
    name: Optional[str] = Field(None, description="Name of the company")
    address: Optional[str] = Field(None, description="Street address of the company")
    suite: Optional[str] = Field(None, description="Suite or unit number")
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State abbreviation")
    zip_code: Optional[str] = Field(None, description="ZIP/Postal code")
    phone: Optional[str] = Field(None, description="Company phone number")
    email: Optional[str] = Field(None, description="Company email address")


class ServiceType(str, Enum):
    """Types of services offered"""
    # Automotive Services
    LUBRICATE = "Lubricate"
    CHANGE_OIL = "Change Oil"
    TRANSMISSION_SERVICE = "Transmission Service"
    BATTERY_SERVICE = "Battery Replacement / Check"
    DIFFERENTIAL_SERVICE = "Differential Service"
    FLAT_TIRE_REPAIR = "Flat Tire Repair"
    ADAS_CALIBRATION = "ADAS Calibration"
    WIPER_REPLACEMENT = "Wiper Replacement"
    CAR_WASH = "Car Wash"
    POLISH_DETAILING = "Polish / Detailing"
    TIRE_SERVICE = "Tire Rotation and Alignment"
    BRAKE_SERVICE = "Brake Inspection / Replacement"
    COOLANT_FLUSH = "Coolant System Flush"
    AIR_FILTER = "Air Filter Replacement"
    SPARK_PLUG = "Spark Plug Replacement"
    EXHAUST_CHECK = "Exhaust System Check"
    ELECTRONICS = "Electronics"
    SUSPENSION_CHECK = "Suspension and Steering Check"
    BATTERY_CHECK = "Electric/Hybrid Vehicle Battery Svc"
    
    # Landscaping Services
    AERATION = "Aeration"
    BORDERS_EDGING = "Borders / Edging"
    FERTILIZATION = "Fertilization"
    GARDEN_DESIGN = "Garden Design"
    GARDEN_INSTALLATION = "Garden Installation"
    HEDGE_TRIMMING = "Hedge Trimming"
    IRRIGATION_INSTALL = "Irrigation Installation"
    IRRIGATION_MAINTENANCE = "Irrigation Maintenance"
    LANDSCAPE_LIGHTING = "Landscape Lighting Installation"
    MOWING = "Mowing"
    TRIM_MOWING = "Trim Mowing"
    MULCHING = "Mulching"
    PATIO_DECK_CONSTRUCTION = "Patio / Deck Construction"
    PATIO_DECK_MAINTENANCE = "Patio / Deck Maintenance"
    PAVING = "Paving / Walkway Installation"
    RETAINING_WALL = "Retaining Wall Construction"
    SEASONAL_CLEANUP = "Seasonal Clean-up"
    SOD_INSTALLATION = "Sod Installation"
    TREE_PRUNING = "Tree Pruning"
    TREE_TRIMMING = "Tree Trimming"
    WEED_CONTROL = "Weed Control"
    WINTERIZING = "Winterizing"

    # Electrical Services
    ELECTRICAL_REPAIR = "Electrical Repair"
    CIRCUIT_BREAKER = "Circuit Breaker Service"
    FAN_INSTALLATION = "Fan Installation"
    OUTLET_REPAIR = "Outlet Repair"
    WIRING_INSTALLATION = "Wiring Installation"


class PriorityLevel(str, Enum):
    """Priority levels for work orders"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class VehicleInfo(BaseModel):
    """Vehicle information for automotive work orders"""
    vin: Optional[str] = Field(None, description="Vehicle Identification Number")
    make_model: Optional[str] = Field(None, description="Make and model of the vehicle")
    year: Optional[int] = Field(None, description="Year of the vehicle")
    odometer: Optional[float] = Field(None, description="Current odometer reading")
    license_number: Optional[str] = Field(None, description="License plate number")
    state: Optional[str] = Field(None, description="State of registration")
    motor_number: Optional[str] = Field(None, description="Motor/Engine number")


class LineItem(BaseModel):
    """Line item for materials, parts, or labor"""
    description: Optional[str] = Field(None, description="Description of the item or service")
    quantity: Optional[Decimal] = Field(None, description="Quantity of the item")
    price_per_unit: Optional[Decimal] = Field(None, description="Price per unit")
    amount: Optional[Decimal] = Field(None, description="Total amount (quantity * price_per_unit)")
    part_number: Optional[str] = Field(None, description="Part number if applicable")


class WorkOrder(BaseModel):
    """Unified schema for all types of work orders"""
    
    # Company Information
    company_info: Optional[CompanyInfo] = Field(None, description="Company information")
    
    # Basic Information
    order_number: Optional[str] = Field(None, description="Work order number/identifier")
    order_type: Optional[str] = Field(None, description="Type of work order (Automotive/Landscaping/Electrical)")
    
    # Client Information
    client_name: Optional[str] = Field(None, description="Name of the client")
    client_phone: Optional[str] = Field(None, description="Client's phone number")
    client_email: Optional[str] = Field(None, description="Client's email address")
    service_location: Optional[str] = Field(None, description="Address where service will be performed")
    
    # Timing Information
    order_date: Optional[datetime] = Field(None, description="Date and time the order was created")
    start_date: Optional[datetime] = Field(None, description="Expected start date")
    end_date: Optional[datetime] = Field(None, description="Expected end date")
    date_completed: Optional[datetime] = Field(None, description="Actual completion date")
    
    # Vehicle Information (for automotive work orders)
    vehicle_info: Optional[VehicleInfo] = Field(None, description="Vehicle information for automotive work orders")
    
    # Service Details
    services_requested: Optional[List[ServiceType]] = Field(default_factory=list, description="List of services requested")
    job_description: Optional[str] = Field(None, description="Detailed description of work to be performed")
    priority_level: Optional[PriorityLevel] = Field(None, description="Priority level of the work order")
    
    # Cost Information
    materials: Optional[List[LineItem]] = Field(default_factory=list, description="List of materials used")
    labor_items: Optional[List[LineItem]] = Field(default_factory=list, description="List of labor charges")
    materials_total: Optional[Decimal] = Field(None, description="Total cost of materials")
    labor_total: Optional[Decimal] = Field(None, description="Total cost of labor")
    subtotal: Optional[Decimal] = Field(None, description="Subtotal before tax")
    tax_rate: Optional[Decimal] = Field(None, description="Tax rate as a percentage")
    tax_amount: Optional[Decimal] = Field(None, description="Calculated tax amount")
    total_amount: Optional[Decimal] = Field(None, description="Final total amount")
