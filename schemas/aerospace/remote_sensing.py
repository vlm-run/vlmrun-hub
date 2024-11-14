from enum import Enum

from pydantic import BaseModel, Field


class RemoteSensingCategory(str, Enum):
    airport = "airport"
    baseball_field = "baseball_field"
    beach = "beach"
    bridge = "bridge"
    cemetery = "cemetery"
    commercial_area = "commercial_area"
    dam = "dam"
    desert = "desert"
    factory = "factory"
    farmlands = "farmlands"
    forest = "forest"
    golf_course = "golf_course"
    greenhouse = "greenhouse"
    hospital = "hospital"
    industrial_area = "industrial_area"
    lake = "lake"
    landfill = "landfill"
    military_base = "military_base"
    mining_site = "mining-site"
    mountain = "mountain"
    oil_field = "oil_field"
    other = "other"
    park = "park"
    parking_lot = "parking_lot"
    port = "port"
    power_plant = "power_plant"
    quarry = "quarry"
    railway_station = "railway_station"
    residential_area = "residential_area"
    resort = "resort"
    river = "river"
    runway = "runway"
    school_campus = "school_campus"
    shopping_mall = "shopping_mall"
    solar_farm = "solar_farm"
    stadium = "stadium"
    storage_tanks = "storage_tanks"
    vineyard = "vineyard"
    water_treatment = "water_treatment"
    wetland = "wetland"
    wind_farm = "wind_farm"


class RemoteSensing(BaseModel):
    description: str = Field(
        ..., description="2-3 sentence description of the satellite image."
    )
    objects: list[str] = Field(..., description="List of unique objects in the scene")
    categories: list[RemoteSensingCategory] = Field(
        ..., description="List of (atmost 10) categories that pertain to the scene."
    )
