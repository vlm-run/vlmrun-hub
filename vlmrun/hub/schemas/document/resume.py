from datetime import date
from typing import Dict, List

from pydantic import BaseModel, Field, HttpUrl


class ContactInfo(BaseModel):
    full_name: str = Field(..., description="Full name of the individual.")
    email: str | None = Field(None, description="Email address.")
    phone: str | None = Field(None, description="Phone number.")
    address: str | None = Field(None, description="Physical address.")
    linkedin: HttpUrl | None = Field(None, description="LinkedIn profile URL.")
    github: HttpUrl | None = Field(None, description="GitHub profile URL.")
    portfolio: HttpUrl | None = Field(None, description="Portfolio website URL.")
    google_scholar: HttpUrl | None = Field(None, description="Google Scholar profile URL.")


class Education(BaseModel):
    institution: str | None = Field(None, description="Name of the educational institution.")
    degree: str | None = Field(None, description="Degree obtained or pursued.")
    field_of_study: str | None = Field(None, description="Field of study or major.")
    graduation_date: date | None = Field(None, description="Date of graduation.")
    gpa: float | None = Field(None, description="Grade Point Average.")
    honors: List[str] | None = Field(None, description="Honors or awards received.")
    relevant_courses: List[str] | None = Field(None, description="Relevant courses taken.")


class WorkExperience(BaseModel):
    company: str | None = Field(None, description="Name of the company.")
    position: str | None = Field(None, description="Job title or position held.")
    start_date: date | None = Field(None, description="Start date of employment.")
    end_date: date | None = Field(None, description="End date of employment.")
    is_current: bool = Field(False, description="Indicates if this is the current job.")
    responsibilities: List[str] = Field(..., description="Key responsibilities and achievements.")
    technologies: List[str] | None = Field(None, description="Technologies or tools used.")


class Skill(BaseModel):
    name: str = Field(..., description="Name of the skill.")
    level: str | None = Field(None, description="Proficiency level (e.g., 'Beginner', 'Intermediate', 'Expert')")
    years_of_experience: float | None = Field(None, description="Years of experience with this skill.")


class TechnicalSkills(BaseModel):
    programming_languages: List[Skill] = Field(..., description="Programming languages.")
    frameworks_libraries: List[Skill] = Field(..., description="Frameworks and libraries.")
    databases: List[Skill] | None = Field(None, description="Database technologies.")
    tools: List[Skill] | None = Field(None, description="Development tools and environments.")
    cloud_platforms: List[Skill] | None = Field(None, description="Cloud platforms and services.")
    other: List[Skill] | None = Field(None, description="Other technical skills.")


class Project(BaseModel):
    name: str = Field(..., description="Name of the project.")
    description: str | None = Field(None, description="Brief description of the project.")
    technologies: List[str] | None = Field(None, description="Technologies or tools used.")
    url: HttpUrl | None = Field(None, description="URL to the project or its repository.")
    github_url: HttpUrl | None = Field(None, description="GitHub repository URL.")
    start_date: date | None = Field(None, description="Start date of the project.")
    end_date: date | None = Field(None, description="End date of the project.")
    role: str | None = Field(None, description="Role in the project.")
    key_achievements: List[str] | None = Field(None, description="Key achievements or features implemented.")


class Certification(BaseModel):
    name: str = Field(..., description="Name of the certification.")
    issuer: str = Field(..., description="Organization that issued the certification.")
    date_obtained: date | None = Field(None, description="Date the certification was obtained.")
    expiration_date: date | None = Field(None, description="Expiration date of the certification.")
    credential_id: str | None = Field(None, description="Credential ID or verification URL.")


class OpenSourceContribution(BaseModel):
    project_name: str = Field(..., description="Name of the open-source project.")
    contribution_type: str = Field(
        ..., description="Type of contribution (e.g., 'Bug fix', 'Feature', 'Documentation')"
    )
    description: str = Field(..., description="Brief description of the contribution.")
    url: HttpUrl | None = Field(None, description="URL to the contribution (e.g., pull request).")


class Resume(BaseModel):
    contact_info: ContactInfo = Field(..., description="Contact information of the individual.")
    summary: str | None = Field(None, description="Professional summary or objective statement.")
    education: List[Education] = Field(..., description="Educational background.")
    work_experience: List[WorkExperience] = Field(..., description="Work experience.")
    technical_skills: TechnicalSkills = Field(..., description="Technical skills.")
    projects: List[Project] | None = Field(None, description="Notable projects")
    open_source_contributions: List[OpenSourceContribution] | None = Field(
        None, description="Open source contributions."
    )
    certifications: List[Certification] | None = Field(None, description="Professional certifications.")
    publications: List[str] | None = Field(None, description="Publications or technical writing.")
    conferences: List[str] | None = Field(None, description="Conferences attended or presented at.")
    languages: List[Skill] | None = Field(None, description="Languages known (natural languages).")
    volunteer_work: List[str] | None = Field(None, description="Volunteer work or community service.")
    interests: List[str] | None = Field(None, description="Personal interests or hobbies.")
    references: str | None = Field(None, description="References or note about references.")
    additional_sections: Dict[str, List[str]] | None = Field(None, description="Any additional sections in the resume.")
