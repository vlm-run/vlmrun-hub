from typing import List, Optional

from pydantic import BaseModel, Field


class TVNews(BaseModel):
    description: Optional[str] = Field(None, description="Description of the scene contents and visual elements")
    chyron: Optional[str] = Field(
        None, description="Text displayed in the lower third of the screen (chyron/news ticker)"
    )
    network: Optional[str] = Field(None, description="Name of the news network broadcasting the content")
    reporters: Optional[List[str]] = Field(None, description="List of reporter names appearing in the news broadcast")
