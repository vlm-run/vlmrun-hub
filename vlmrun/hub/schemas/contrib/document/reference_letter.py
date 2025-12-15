from datetime import date
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, description="Street address including building/apartment number")
    city: Optional[str] = Field(None, description="City or town name")
    state: Optional[str] = Field(None, description="State, province, or region")
    zip_code: Optional[str] = Field(None, description="ZIP or postal code")
    country: Optional[str] = Field(None, description="Country name")


class ContactInformation(BaseModel):
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number including country/area code if available")
    alternative_phone: Optional[str] = Field(None, description="Alternative phone number")
    website: Optional[str] = Field(None, description="Personal or professional website")
    social_media: Optional[Dict[str, str]] = Field(None, description="Social media handles/URLs keyed by platform name")


class RelationshipType(str, Enum):
    """Types of professional relationships between referee and candidate."""

    SUPERVISOR = "supervisor"
    MANAGER = "manager"
    PROFESSOR = "professor"
    TEACHER = "teacher"
    MENTOR = "mentor"
    COLLEAGUE = "colleague"
    ADVISOR = "advisor"
    CLIENT = "client"
    OTHER = "other"


class RecommendationStrength(str, Enum):
    """Strength of the recommendation provided."""

    HIGHEST = "highest"
    STRONG = "strong"
    MODERATE = "moderate"
    NEUTRAL = "neutral"
    RESERVED = "reserved"
    UNKNOWN = "unknown"


class SkillAssessment(BaseModel):
    """Assessment of a specific skill or quality."""

    skill_name: Optional[str] = Field(None, description="Name of the skill or quality being assessed")
    description: Optional[str] = Field(None, description="Description of how the candidate demonstrates this skill")
    rating: Optional[str] = Field(None, description="Qualitative rating of the skill (e.g., 'excellent', 'good')")
    context: Optional[str] = Field(None, description="Context or situation where this skill was demonstrated")


class Achievement(BaseModel):
    """Specific achievement mentioned in the letter."""

    description: Optional[str] = Field(None, description="Description of the achievement")
    impact: Optional[str] = Field(None, description="Impact or result of the achievement")
    date_or_period: Optional[str] = Field(None, description="When the achievement occurred")


class ReferenceLetter(BaseModel):

    # Document metadata
    letterhead_present: Optional[bool] = Field(None, description="Indicates if the letter is on official letterhead")
    letter_date: Optional[date] = Field(None, description="Date when the letter was written")
    letter_format: Optional[str] = Field(
        None, description="Format of the letter (e.g., 'formal', 'academic', 'business')"
    )

    # Referee (person writing the letter) information
    referee_name: str = Field(..., description="Full name of the person writing the reference letter")
    referee_title: Optional[str] = Field(None, description="Job title or position of the referee")
    referee_credentials: Optional[List[str]] = Field(
        None, description="Academic or professional credentials of the referee (e.g., 'PhD', 'CPA')"
    )
    referee_organization: Optional[str] = Field(None, description="Organization or company where the referee works")
    referee_department: Optional[str] = Field(None, description="Department or division within the organization")
    referee_address: Optional[Address] = Field(None, description="Address of the referee or their organization")
    referee_contact: Optional[ContactInformation] = Field(None, description="Contact information of the referee")

    # Candidate (person being recommended) information
    candidate_name: str = Field(..., description="Full name of the person being recommended")
    candidate_title: Optional[str] = Field(None, description="Current or former job title of the candidate")
    candidate_organization: Optional[str] = Field(None, description="Organization where the candidate works/worked")

    # Relationship information
    relationship_type: Optional[RelationshipType] = Field(
        None, description="Type of professional relationship between referee and candidate"
    )
    relationship_duration: Optional[str] = Field(
        None, description="Duration of the professional relationship (e.g., '2 years', 'seven semesters')"
    )
    relationship_context: Optional[str] = Field(
        None,
        description="Context in which the referee knows the candidate (e.g., 'supervised at Central College's student café')",
    )
    relationship_custom_description: Optional[str] = Field(
        None, description="Custom description of the relationship if it doesn't fit standard categories"
    )

    # Recipient information
    recipient_name: Optional[str] = Field(None, description="Name of the person to whom the letter is addressed")
    recipient_title: Optional[str] = Field(None, description="Job title or position of the recipient")
    recipient_organization: Optional[str] = Field(None, description="Organization or company where the recipient works")
    recipient_department: Optional[str] = Field(
        None, description="Department or division within the recipient's organization"
    )
    recipient_address: Optional[Address] = Field(None, description="Address of the recipient or their organization")
    is_open_letter: Optional[bool] = Field(
        None,
        description="Indicates if this is an open 'To Whom It May Concern' letter rather than addressed to a specific person",
    )

    # Detailed assessment
    skills_assessment: Optional[List[SkillAssessment]] = Field(
        None, description="Detailed assessment of candidate's skills and qualities"
    )
    achievements: Optional[List[Achievement]] = Field(
        None, description="Specific achievements or accomplishments mentioned"
    )
    strengths_mentioned: Optional[List[str]] = Field(None, description="List of strengths attributed to the candidate")
    areas_for_improvement: Optional[List[str]] = Field(
        None, description="Areas where the candidate could improve, if mentioned"
    )

    # Recommendation details
    position_recommended_for: Optional[str] = Field(
        None, description="Specific position or role the candidate is being recommended for"
    )
    recommendation_strength: Optional[RecommendationStrength] = Field(
        None, description="Overall strength of the recommendation"
    )
    recommendation_statement: Optional[str] = Field(
        None, description="Direct quote of the recommendation statement (e.g., 'I enthusiastically recommend Daniel')"
    )

    # Additional information
    has_signature: Optional[bool] = Field(None, description="Indicates if the letter contains a signature")
    signature_type: Optional[str] = Field(
        None, description="Type of signature (e.g., 'handwritten', 'digital', 'typed')"
    )
    contact_offer: Optional[bool] = Field(
        None, description="Indicates if the referee offers to be contacted for further information"
    )
    contact_statement: Optional[str] = Field(
        None, description="Statement about contacting for more information (e.g., 'Please call me at 555-555-5555')"
    )

    # Extracted quotes
    notable_quotes: Optional[List[str]] = Field(
        None, description="Notable or particularly strong quotes from the letter"
    )
