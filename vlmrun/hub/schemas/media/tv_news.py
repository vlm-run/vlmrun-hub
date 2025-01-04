from pydantic import BaseModel, Field

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
