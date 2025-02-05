from typing import List, Optional

from pydantic import BaseModel, Field


class TeamInfo(BaseModel):
    name: Optional[str] = Field(None, description="Name of the team")
    score: Optional[int] = Field(None, description="Current score of the team")


class NFLGameState(BaseModel):
    description: Optional[str] = Field(None, description="Text description of the current game state")
    teams: Optional[List[TeamInfo]] = Field(None, description="List of teams playing in the game")
    status: Optional[str] = Field(None, description="Current status of the game, e.g., 'in_progress', 'final'")
    quarter: Optional[int] = Field(None, description="Current quarter of the game (1-4, or 5 for overtime)")
    clock_time: Optional[str] = Field(None, description="Time remaining in the current quarter, e.g., '14:56'")
    possession_team: Optional[str] = Field(None, description="Name of the team currently in possession")
    down: Optional[str] = Field(None, description="Current down (1st, 2nd, 3rd, 4th)")
    distance: Optional[int] = Field(None, description="Yards needed for first down")
    yard_line: Optional[int] = Field(None, description="Current yard line position")
    network: Optional[str] = Field(None, description="TV network broadcasting the game")
    is_shown: Optional[bool] = Field(None, description="Whether the game is currently being shown")
