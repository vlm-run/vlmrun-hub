from enum import Enum

from pydantic import BaseModel, Field


class RemoteSensingCategory(str, Enum):
    airport = "airport"
    baseball_field = "baseball-field"
    beach = "beach"
    bridge = "bridge"
    cemetery = "cemetery"
    commercial_area = "commercial-area"
    dam = "dam"
    desert = "desert"
    factory = "factory"
    farmlands = "farmlands"
    forest = "forest"
    golf_course = "golf-course"
    greenhouse = "greenhouse"
    hospital = "hospital"
    industrial_area = "industrial-area"
    lake = "lake"
    landfill = "landfill"
    military_base = "military-base"
    mining_site = "mining-site"
    mountain = "mountain"
    oil_field = "oil-field"
    other = "other"
    park = "park"
    parking_lot = "parking-lot"
    port = "port"
    power_plant = "power-plant"
    quarry = "quarry"
    railway_station = "railway-station"
    residential_area = "residential-area"
    resort = "resort"
    river = "river"
    runway = "runway"
    school_campus = "school-campus"
    shopping_mall = "shopping-mall"
    solar_farm = "solar-farm"
    stadium = "stadium"
    storage_tanks = "storage-tanks"
    vineyard = "vineyard"
    water_treatment = "water-treatment"
    wetland = "wetland"
    wind_farm = "wind-farm"


class RemoteSensing(BaseModel):
    description: str = Field(..., description="2-3 sentence description of the satellite image.")
    objects: list[str] | None = Field(..., description="List of unique objects in the scene")
    categories: list[RemoteSensingCategory] | None = Field(
        ...,
        description="List of (atmost 10) categories that pertain to the scene.",
        min_length=1,
        max_length=10,
    )
    is_visible: bool | None = Field(
        ...,
        description="Whether the land mass is visible from space, or if it is obscured by clouds.",
    )
