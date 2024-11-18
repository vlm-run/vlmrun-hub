from datetime import datetime,date
from pydantic import BaseModel, Field


class PlayerImage(BaseModel):
    image_url: str | None = Field(None, description="URL of the player's image.")
    player_name: str | None = Field(None, description="Name of the player depicted in the image.")
    team: str | None = Field(None, description="Team the player belongs to.")
    action: str | None = Field(None, description="Action depicted in the image, e.g., 'dunk', 'block', 'steal'.")


class GameContext(BaseModel):
    game_id: str | None = Field(None, description="Unique identifier for the game.")
    game_date: date | None = Field(None, description="Date of the game.")
    teams: list[str] | None = Field(None, description="List of teams participating in the game.")
    score: str | None = Field(None, description="Current score of the game in 'Team A - Team B' format.")
    quarter: int | None = Field(None, description="Current quarter of the game.")
    time_remaining: str | None = Field(None, description="Time remaining in the current quarter, e.g., '2:34'.")


class ActionLabel(BaseModel):
    label: str | None = Field(None, description="Label describing the action, e.g., 'slam dunk', '3-pointer'.")
    confidence: float | None = Field(None, description="Confidence score for the action label, ranging from 0 to 1.")
    timestamp: datetime | None = Field(None, description="Timestamp of the action during the game.")


class SportsNBACaption(BaseModel):
    caption: str | None = Field(None, description="Generated caption for the highlight.")
    player_images: list[PlayerImage] | None = Field(None, description="List of images featuring players involved in the highlight.")
    action_labels: list[ActionLabel] | None = Field(None, description="Action labels describing the key actions in the highlight.")
    game_context: GameContext | None = Field(None, description="Context of the game during the highlight.")
