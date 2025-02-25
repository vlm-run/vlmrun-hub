from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    """Twitter user information."""

    username: str = Field(..., description="The Twitter handle of the user.")
    display_name: str = Field(..., description="The display name of the user.")


class Media(BaseModel):
    """Media content attached to a tweet."""

    description: Optional[str] = Field(default=None, description="A description of the media content linked.")
    type: Optional[Literal["image", "video", "url"]] = Field(
        default=None, description="The type of media (image, video, etc.)."
    )


class Tweet(BaseModel):
    """Individual tweet information including content and engagement metrics."""

    content: Optional[str] = Field(default=None, description="The text content of the tweet.")
    created_at: Optional[date] = Field(default=None, description="The timestamp when the tweet was created.")
    user: Optional[User] = Field(default=None, description="The user who posted the tweet.")
    media: Optional[List[Media]] = Field(default=None, description="List of media items attached to the tweet, if any.")
    retweet_count: Optional[int] = Field(
        default=None, description="The approximate number of times this tweet has been retweeted."
    )
    like_count: Optional[int] = Field(
        default=None, description="The approximate number of likes this tweet has received (icon is a heart)."
    )
    reply_count: Optional[int] = Field(
        default=None, description="The approximate number of replies to this tweet (icon is a reply arrow)."
    )
    view_count: Optional[int] = Field(
        default=None,
        description="The approximate number of views this tweet has received (icon is a vertical bar chart).",
    )
    quote_count: Optional[int] = Field(
        default=None, description="The approximate number of times this tweet has been quoted."
    )


class TwitterCard(BaseModel):
    """A Twitter card containing tweet information and any quoted tweets."""

    tweet: Tweet = Field(..., description="The main tweet content and metadata.")
    quoted_tweet: Optional[Tweet] = Field(default=None, description="A tweet that is quoted by the main tweet, if any.")
