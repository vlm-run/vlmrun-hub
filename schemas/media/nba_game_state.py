from datetime import datetime
from pydantic import BaseModel, Field


class TeamInfo(BaseModel):
    name: str | None = Field(None, description="Name of the team")
    score: int | None = Field(None, description="Current score of the team")


class NBAGameState(BaseModel):
    description: str | None = Field(None, description="Text description of the current game state")
    teams: list[TeamInfo] | None = Field(None, description="List of teams playing in the game")
    status: str | None = Field(None, description="Current status of the game, e.g., 'in_progress', 'final'")
    quarter: int | None = Field(None, description="Current quarter of the game (1-4, or 5 for overtime)")
    clock_time: str | None = Field(None, description="Time remaining in the current quarter, e.g., '14:56'")
    possession_team: str | None = Field(None, description="Name of the team currently in possession")
    down: str | None = Field(None, description="Current down (1st, 2nd, 3rd, 4th)")
    distance: int | None = Field(None, description="Yards needed for first down")
    yard_line: int | None = Field(None, description="Current yard line position")
    network: str | None = Field(None, description="TV network broadcasting the game")
    is_shown: bool | None = Field(None, description="Whether the game is currently being shown")
