from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class ContactPerson(BaseModel):
    name: Optional[str] = Field(None, description="Name of the contact person for the RFP")
    title: Optional[str] = Field(None, description="Title or position of the contact person")
    email: Optional[str] = Field(None, description="Email address of the contact person")
    phone: Optional[str] = Field(None, description="Phone number of the contact person")


class Responsibility(BaseModel):
    description: str = Field(..., description="Description of the contractor responsibility")


class EvaluationCriterion(BaseModel):
    description: str = Field(..., description="Description of the evaluation criterion")
    weight: Optional[float] = Field(None, description="Weight or importance of this criterion (if specified)")


class RFP(BaseModel):
    """Request for Proposal (RFP) schema for extracting information from RFP documents."""

    title: Optional[str] = Field(None, description="Title of the Request for Proposal")

    submission_deadline: Optional[date] = Field(None, description="Deadline date for proposal submissions")

    governing_law: Optional[str] = Field(None, description="Governing law or jurisdiction that applies to the contract")

    duration_of_contract: Optional[str] = Field(None, description="Overall period of performance for the contract")

    budget_cost_estimate: Optional[str] = Field(None, description="Estimated budget or cost range for the project")

    rfp_contact_person: Optional[ContactPerson] = Field(
        None, description="Contact person information for inquiries about the RFP"
    )

    responsibilities_of_contractor: Optional[List[Responsibility]] = Field(
        None, description="List of responsibilities expected from the contractor"
    )

    evaluation_criteria: Optional[List[EvaluationCriterion]] = Field(
        None, description="Criteria used to evaluate and score proposals"
    )

    proposal_submission_location: Optional[str] = Field(
        None, description="Physical or electronic location where proposals should be submitted"
    )

    insurance_requirements: Optional[str] = Field(None, description="Insurance requirements for the contractor")

    project_timeline: Optional[str] = Field(None, description="Expected timeline for project completion")

    eligibility_requirements: Optional[str] = Field(
        None, description="Requirements that bidders must meet to be eligible"
    )

    proposal_format_requirements: Optional[str] = Field(
        None, description="Required format, structure, or content for submitted proposals"
    )

    question_submission_deadline: Optional[date] = Field(
        None, description="Deadline for potential bidders to submit questions"
    )

    pre_proposal_conference_details: Optional[str] = Field(
        None, description="Details about any pre-proposal meetings or conferences"
    )

    issuing_organization: Optional[str] = Field(None, description="Organization that issued the RFP")

    amendment_history: Optional[List[str]] = Field(
        None, description="History of amendments or changes to the original RFP"
    )
