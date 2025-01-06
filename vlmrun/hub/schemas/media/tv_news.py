from pydantic import BaseModel, Field

class Table(BaseModel):
    """A table extracted from a scene."""
    title: str | None = Field(default=None, description="Title of the table, if any")
    content: str = Field(..., description="Content of the table in markdown format")


class Chart(BaseModel):
    """A chart or graph extracted from a scene."""
    title: str | None = Field(default=None, description="Title of the chart, if any")
    description: str = Field(..., description="Description of what the chart shows")
    type: str = Field(..., description="Type of chart (e.g. bar chart, line graph, pie chart)")


class Reporter(BaseModel):
    """A reporter appearing in a scene."""
    name: str = Field(..., description="Name of the reporter")
    role: str | None = Field(default=None, description="Role or title of the reporter, if shown")
    description: str | None = Field(default=None, description="Description of the reporter's appearance or context")


class Speaker(BaseModel):
    """A non-reporter speaker appearing in a scene."""
    name: str = Field(..., description="Name of the speaker")
    title: str | None = Field(default=None, description="Title or role of the speaker")
    affiliation: str | None = Field(default=None, description="Organization or group the speaker is affiliated with")
    description: str | None = Field(default=None, description="Description of the speaker's appearance or context")


class Quote(BaseModel):
    """A quote from a speaker in the scene."""
    text: str = Field(..., description="The quoted text")
    speaker: str = Field(..., description="Name of the person being quoted")


class Markdown(BaseModel):
    """Generic markdown content."""
    content: str = Field(..., description="Content in markdown format")


class Scene(BaseModel):
    description: str = Field(..., description="Detailed description of the scene")
    chyron: str | None = Field(default=None, description="Chyron text, if any, otherwise None.")

    tables: list[Table] | None = Field(
        default=None, description="List of tables in the scene, if any, otherwise if no tables, None."
    )
    charts: list[Chart] | None = Field(
        default=None, description="List of charts in the scene, if any, otherwise if no charts, None."
    )
    reporters: list[Reporter] | None = Field(
        default=None, description="List of reporters in the scene, if any, otherwise if no reporters, None."
    )
    speakers: list[Speaker] | None = Field(default=None, description="List of speakers (non-reporters) in the scene")
    quotes: list[Quote] | None = Field(
        default=None, description="List of quotes in the scene, if any, otherwise if no quotes, None."
    )
    others: list[Markdown] | None = Field(
        default=None,
        description="List of other elements in the scene representing each element in markdown. Do not miss any other content in the scene. Do not include any links or references. If no other elements are visible, None.",
    )