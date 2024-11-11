from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class SatelliteType(str, Enum):
    optical = "optical"
    radar = "radar"
    multispectral = "multispectral"
    hyperspectral = "hyperspectral"
    thermal = "thermal"
    infrared = "infrared"


class ResolutionClass(str, Enum):
    very_high = "very_high"  # < 1m
    high = "high"  # 1-5m
    medium = "medium"  # 5-30m
    low = "low"  # > 30m


class WeatherCondition(str, Enum):
    clear = "clear"
    partly_cloudy = "partly_cloudy"
    cloudy = "cloudy"
    hazy = "hazy"
    rain = "rain"
    snow = "snow"


class SpectralBand(str, Enum):
    visible = "visible"
    near_infrared = "near_infrared"
    short_wave_infrared = "short_wave_infrared"
    thermal_infrared = "thermal_infrared"
    microwave = "microwave"


class ObjectDetection(BaseModel):
    object_type: str = Field(
        ...,
        description="Type of object detected, e.g., 'vehicle', 'building', 'forest'.",
    )
    coordinates: List[float] = Field(
        ...,
        description="Coordinates of the detected object in the image, as [latitude, longitude].",
    )
    confidence_score: float = Field(
        ...,
        description="Confidence score of the object detection, ranging from 0 to 1.",
    )
    area: Optional[float] = Field(
        None, description="Area of the detected object in square meters, if applicable."
    )


class EnvironmentalMetrics(BaseModel):
    vegetation_index: Optional[float] = Field(
        None, description="Normalized Difference Vegetation Index (NDVI) value."
    )
    soil_moisture: Optional[float] = Field(
        None, description="Soil moisture level, if measurable."
    )
    air_quality_index: Optional[int] = Field(
        None, description="Air quality index at the location, if available."
    )
    temperature: Optional[float] = Field(
        None, description="Temperature in Celsius at the location."
    )
    precipitation: Optional[float] = Field(
        None, description="Precipitation levels in millimeters, if measurable."
    )


class TerrainData(BaseModel):
    elevation: Optional[float] = Field(
        None, description="Elevation at the location in meters."
    )
    slope: Optional[float] = Field(None, description="Slope of the terrain in degrees.")
    land_cover_type: Optional[str] = Field(
        None, description="Type of land cover, e.g., 'forest', 'urban', 'water'."
    )


class SatelliteImageAnalysis(BaseModel):

    # Technical specifications
    satellite_type: SatelliteType = Field(
        ..., description="Type of satellite sensor used for image capture"
    )
    resolution_class: ResolutionClass = Field(
        ..., description="Spatial resolution classification of the imagery"
    )
    ground_resolution: float = Field(
        ..., description="Ground sample distance in meters per pixel"
    )
    capture_date: date = Field(
        ..., description="Date and time when the imagery was captured"
    )
    weather_conditions: WeatherCondition = Field(
        ..., description="Weather conditions during image capture"
    )
    cloud_cover_percentage: float = Field(
        ..., description="Percentage of cloud cover in the image", ge=0, le=100
    )
    spectral_bands: List[SpectralBand] = Field(
        ..., description="List of spectral bands available in the imagery"
    )

    # Optional technical details
    swath_width: Optional[float] = Field(
        None, description="Width of the image swath in kilometers"
    )
    sun_elevation: Optional[float] = Field(
        None, description="Sun elevation angle during capture in degrees"
    )
    sun_azimuth: Optional[float] = Field(
        None, description="Sun azimuth angle during capture in degrees"
    )
    processing_level: str = Field(
        ..., description="Processing level of the satellite imagery (e.g., L1C, L2A)"
    )
    geometric_accuracy: Optional[float] = Field(
        None, description="Geometric accuracy of the imagery in meters"
    )

    # Analysis results
    object_detections: List[ObjectDetection] = Field(
        ..., description="List of detected objects in the satellite images."
    )
    environmental_metrics: EnvironmentalMetrics = Field(
        ..., description="Environmental metrics calculated from the satellite imagery."
    )
    terrain_data: TerrainData = Field(
        ..., description="Terrain data derived from the satellite imagery."
    )
