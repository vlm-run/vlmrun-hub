from enum import Enum

from pydantic import BaseModel, Field


class RemoteSensingCategory(str, Enum):
    airport = "airport"
    bridge = "bridge"
    baseball_field = "baseball-field"
    commercial_area = "commercial-area"
    residential_area = "residential-area"
    desert = "desert"
    farmlands = "farmlands"
    forest = "forest"
    factory = "factory"
    park = "park"
    parking_lot = "parking-lot"
    port = "port"
    railway_station = "railway-station"
    resort = "resort"
    river = "river"
    industrial_area = "industrial-area"
    stadium = "stadium"
    storage_tanks = "storage-tanks"
    runway = "runway"
    golf_course = "golf-course"
    beach = "beach"
    mountain = "mountain"
    lake = "lake"
    wetland = "wetland"
    solar_farm = "solar-farm"
    mining_site = "mining-site"
    school_campus = "school-campus"
    hospital = "hospital"
    shopping_mall = "shopping-mall"
    power_plant = "power-plant"
    wind_farm = "wind-farm"
    quarry = "quarry"
    military_base = "military-base"
    oil_field = "oil-field"
    vineyard = "vineyard"
    greenhouse = "greenhouse"
    landfill = "landfill"
    water_treatment = "water-treatment"
    dam = "dam"
    cemetery = "cemetery"
    other = "other"


class RemoteSensing(BaseModel):
    description: str = Field(
        ..., description="2-3 sentence description of the overhead image."
    )
    objects: list[str] = Field(..., description="List of unique objects in the scene")
    categories: list[RemoteSensingCategory] = Field(
        ..., description="List of (atmost 5) categories that pertain to the scene."
    )
