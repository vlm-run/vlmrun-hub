from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field

class DetectedObject(BaseModel):
    class_name: str | None = Field(None, description="Class name of the detected object, e.g., 'microphone', 'screens'.")


class TVCaption(BaseModel):
    generated_caption: str | None = Field(None, description="Final generated caption for the media content.")
    description: str | None = Field(None, description="Detailed description of the media content.")
    chyron: str | None = Field(None, description="Text displayed on the chyron (lower third of the screen).")
    objects: list[DetectedObject] | None = Field(None, description="List of detected objects in the media.")
    persons: list[str] | None = Field(None, description="List of detected persons in the media.")
    logos: list[str] | None = Field(None, description="List of detected logos in the media.")
    texts: list[str] | None = Field(None, description="List of detected texts in the media.")
    tags: list[str] | None = Field(None, description="Tags associated with the media content.")
