from typing import List, Literal

from pydantic import BaseModel, Field


class User(BaseModel):
    """Twitter user information."""
    username: str = Field(..., description="The Twitter handle of the user.")
    display_name: str = Field(..., description="The display name of the user.")


class Media(BaseModel):
    """Media content attached to a tweet."""
    description: str | None = Field(default=None, description="A description of the media content linked.")
    type: Literal["image", "video", "url"] | None = Field(
        default=None, description="The type of media (image, video, etc.)."
    )


class Tweet(BaseModel):
    """Individual tweet information including content and engagement metrics."""
    content: str | None = Field(default=None, description="The text content of the tweet.")
    created_at: str | None = Field(default=None, description="The timestamp when the tweet was created.")
    user: User | None = Field(default=None, description="The user who posted the tweet.")
    media: str | None = Field(default=None, description="List of media items attached to the tweet, if any.")
    retweet_count: int | None = Field(
        None, description="The approximate number of times this tweet has been retweeted."
    )
    like_count: int | None = Field(
        default=None, description="The approximate number of likes this tweet has received."
    )
    reply_count: int | None = Field(default=None, description="The approximate number of replies to this tweet.")
    view_count: str | None = Field(
        None, description="The approximate number of views this tweet has received (icon is a vertical bar chart)."
    )
    quote_count: int | None = Field(
        default=None, description="The approximate number of times this tweet has been quoted."
    )


class TwitterCard(BaseModel):
    """A Twitter card containing tweet information and any quoted tweets."""
    tweet: Tweet = Field(..., description="The main tweet content and metadata.")
    quoted_tweet: Tweet | None = Field(default=None, description="A tweet that is quoted by the main tweet, if any.")

    class Config:
        """Configuration for the TwitterCard model."""
        schema_extra = {
            "example": {
                "tweet": {
                    "content": "Introducing GPT-4 Turbo with vision",
                    "created_at": "2023-11-06T18:00:00Z",
                    "user": {
                        "username": "OpenAI",
                        "display_name": "OpenAI"
                    },
                    "media": "Image of GPT-4 Turbo announcement",
                    "retweet_count": 5421,
                    "like_count": 28900,
                    "reply_count": 1234,
                    "view_count": "2.1M",
                    "quote_count": 892
                },
                "quoted_tweet": None
            }
        }
