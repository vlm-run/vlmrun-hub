from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field


class MediaSegment(BaseModel):
    start_time: str | None = Field(None, description="Start time of the segment in HH:MM:SS format.")
    end_time: str | None = Field(None, description="End time of the segment in HH:MM:SS format.")
    transcription: str | None = Field(None, description="Speech-to-text transcription for the segment.")
    speaker: str | None = Field(None, description="Speaker's name or identifier, if available.")
    confidence_score: float | None = Field(None, description="Confidence score of the transcription.")


class MediaMetadata(BaseModel):
    duration: str | None = Field(None, description="Total duration of the media in HH:MM:SS format.")
    language: str | None = Field(None, description="Language of the media content.")


class DetectedObject(BaseModel):
    class_name: str | None = Field(None, description="Class name of the detected object, e.g., 'microphone', 'screens'.")


class TVCaption(BaseModel):
    metadata: MediaMetadata | None = Field(None, description="Metadata for the media content.")
    segments: list[MediaSegment] | None = Field(None, description="List of timestamped segments with transcriptions.")
    generated_caption: str | None = Field(None, description="Final generated caption for the media content.")
    description: str | None = Field(None, description="Detailed description of the media content.")
    chyron: str | None = Field(None, description="Text displayed on the chyron (lower third of the screen).")
    objects: list[DetectedObject] | None = Field(None, description="List of detected objects in the media.")
    persons: list[str] | None = Field(None, description="List of detected persons in the media.")
    logos: list[str] | None = Field(None, description="List of detected logos in the media.")
    texts: list[str] | None = Field(None, description="List of detected texts in the media.")
    tags: list[str] | None = Field(None, description="Tags associated with the media content.")
