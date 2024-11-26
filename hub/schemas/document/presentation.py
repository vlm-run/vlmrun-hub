from pydantic import BaseModel, Field


class Table(BaseModel):
    description: str | None = Field(None, description="Description of the table.")
    title: str | None = Field(None, description="Title of the table.")
    caption: str | None = Field(None, description="Caption for the table, if available.")
    markdown: str | None = Field(None, description="Table content in markdown format.")


class Chart(BaseModel):
    type: str | None = Field(None, description="Type of the chart, e.g., 'pie', 'bar', 'line'.")
    description: str | None = Field(None, description="Description of the chart.")
    title: str | None = Field(None, description="Title of the chart.")
    caption: str | None = Field(None, description="Caption for the chart, if available.")
    markdown: str | None = Field(None, description="Chart data in markdown format.")


class Slide(BaseModel):
    slide_number: int | None = Field(None, description="Slide number in the presentation.")
    title: str | None = Field(None, description="Title of the slide.")
    bullet_points: list[str] | None = Field(None, description="List of bullet points on the slide.")
    speaker_notes: str | None = Field(None, description="Speaker notes for the slide.")
    images: list[str] | None = Field(None, description="URLs of images included on the slide.")
    tables: list[Table] | None = Field(None, description="Tables included on the slide.")
    charts: list[Chart] | None = Field(None, description="Charts included on the slide.")


class Presentation(BaseModel):
    description: str | None = Field(None, description="Description of the presentation document.")
    title: str | None = Field(None, description="Title of the presentation.")
    page_number: int | None = Field(None, description="Page number within the document where the content is located.")
    slides: list[Slide] | None = Field(None, description="List of slides in the presentation.")
