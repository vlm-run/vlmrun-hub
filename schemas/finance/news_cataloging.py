from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class ImageData(BaseModel):
    url: str = Field(..., description="URL of the image related to the news article.")
    description: Optional[str] = Field(
        None, description="Description of the image content."
    )
    date_taken: Optional[date] = Field(
        None, description="Date when the image was taken or published."
    )
    source: Optional[str] = Field(None, description="Source or provider of the image.")


class CompanyLogo(BaseModel):
    company_name: str = Field(
        ..., description="Name of the company whose logo is displayed."
    )
    logo_url: str = Field(..., description="URL to the company logo image.")
    detected_date: Optional[date] = Field(
        None,
        description="Date when the logo was detected in the context of the article.",
    )


class EventKeyword(BaseModel):
    keyword: str = Field(
        ...,
        description="Relevant keyword describing an event, e.g., 'earnings', 'merger', 'acquisition'.",
    )
    relevance_score: Optional[float] = Field(
        None, description="Relevance score of the keyword in relation to the article."
    )
    associated_date: Optional[date] = Field(
        None, description="Date associated with the keyword event, if applicable."
    )


class NewsArticleMetadata(BaseModel):
    title: str = Field(..., description="Title of the news article.")
    url: str = Field(..., description="URL to the full news article.")
    publication_date: date = Field(
        ..., description="Date the news article was published."
    )
    author: Optional[str] = Field(None, description="Author of the news article.")
    summary: Optional[str] = Field(
        None, description="Brief summary of the news article content."
    )
    category: Optional[str] = Field(
        None, description="Category of the news article, e.g., 'finance', 'technology'."
    )


class NewsCataloging(BaseModel):
    article_metadata: NewsArticleMetadata = Field(
        ..., description="Metadata for the news article."
    )
    images: List[ImageData] = Field(
        ..., description="List of images related to the news article."
    )
    company_logos: List[CompanyLogo] = Field(
        ..., description="Detected company logos in the article context."
    )
    event_keywords: List[EventKeyword] = Field(
        ..., description="Keywords related to events or topics in the news article."
    )
