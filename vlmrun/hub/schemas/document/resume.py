from datetime import date
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ContactInfo(BaseModel):
    full_name: str = Field(..., description="Full name of the individual.")
    email: Optional[str] = Field(None, description="Email address.")
    phone: Optional[str] = Field(None, description="Phone number.")
    address: Optional[str] = Field(None, description="Physical address.")
    linkedin: Optional[HttpUrl] = Field(None, description="LinkedIn profile URL.")
    github: Optional[HttpUrl] = Field(None, description="GitHub profile URL.")
    portfolio: Optional[HttpUrl] = Field(None, description="Portfolio website URL.")
    google_scholar: Optional[HttpUrl] = Field(None, description="Google Scholar profile URL.")


class Education(BaseModel):
    institution: Optional[str] = Field(None, description="Name of the educational institution.")
    degree: Optional[str] = Field(None, description="Degree obtained or pursued.")
    field_of_study: Optional[str] = Field(None, description="Field of study or major.")
    graduation_date: Optional[date] = Field(None, description="Date of graduation.")
    gpa: Optional[float] = Field(None, description="Grade Point Average.")
    honors: Optional[List[str]] = Field(None, description="Honors or awards received.")
    relevant_courses: Optional[List[str]] = Field(None, description="Relevant courses taken.")


class WorkExperience(BaseModel):
    company: Optional[str] = Field(None, description="Name of the company.")
    position: Optional[str] = Field(None, description="Job title or position held.")
    start_date: Optional[date] = Field(None, description="Start date of employment.")
    end_date: Optional[date] = Field(None, description="End date of employment.")
    is_current: bool = Field(False, description="Indicates if this is the current job.")
    responsibilities: List[str] = Field(..., description="Key responsibilities and achievements.")
    technologies: Optional[List[str]] = Field(None, description="Technologies or tools used.")


class Skill(BaseModel):
    name: str = Field(..., description="Name of the skill.")
    level: Optional[str] = Field(None, description="Proficiency level (e.g., 'Beginner', 'Intermediate', 'Expert')")
    years_of_experience: Optional[float] = Field(None, description="Years of experience with this skill.")


class TechnicalSkills(BaseModel):
    programming_languages: List[Skill] = Field(..., description="Programming languages.")
    frameworks_libraries: List[Skill] = Field(..., description="Frameworks and libraries.")
    databases: Optional[List[Skill]] = Field(None, description="Database technologies.")
    tools: Optional[List[Skill]] = Field(None, description="Development tools and environments.")
    cloud_platforms: Optional[List[Skill]] = Field(None, description="Cloud platforms and services.")
    other: Optional[List[Skill]] = Field(None, description="Other technical skills.")


class Project(BaseModel):
    name: str = Field(..., description="Name of the project.")
    description: Optional[str] = Field(None, description="Brief description of the project.")
    technologies: Optional[List[str]] = Field(None, description="Technologies or tools used.")
    url: Optional[HttpUrl] = Field(None, description="URL to the project or its repository.")
    github_url: Optional[HttpUrl] = Field(None, description="GitHub repository URL.")
    start_date: Optional[date] = Field(None, description="Start date of the project.")
    end_date: Optional[date] = Field(None, description="End date of the project.")
    role: Optional[str] = Field(None, description="Role in the project.")
    key_achievements: Optional[List[str]] = Field(None, description="Key achievements or features implemented.")


class Certification(BaseModel):
    name: str = Field(..., description="Name of the certification.")
    issuer: str = Field(..., description="Organization that issued the certification.")
    date_obtained: Optional[date] = Field(None, description="Date the certification was obtained.")
    expiration_date: Optional[date] = Field(None, description="Expiration date of the certification.")
    credential_id: Optional[str] = Field(None, description="Credential ID or verification URL.")


class OpenSourceContribution(BaseModel):
    project_name: str = Field(..., description="Name of the open-source project.")
    contribution_type: str = Field(
        ..., description="Type of contribution (e.g., 'Bug fix', 'Feature', 'Documentation')"
    )
    description: str = Field(..., description="Brief description of the contribution.")
    url: Optional[HttpUrl] = Field(None, description="URL to the contribution (e.g., pull request).")


class Resume(BaseModel):
    contact_info: ContactInfo = Field(..., description="Contact information of the individual.")
    summary: Optional[str] = Field(None, description="Professional summary or objective statement.")
    education: List[Education] = Field(..., description="Educational background.")
    work_experience: List[WorkExperience] = Field(..., description="Work experience.")
    technical_skills: TechnicalSkills = Field(..., description="Technical skills.")
    projects: Optional[List[Project]] = Field(None, description="Notable projects")
    open_source_contributions: Optional[List[OpenSourceContribution]] = Field(
        None, description="Open source contributions."
    )
    certifications: Optional[List[Certification]] = Field(None, description="Professional certifications.")
    publications: Optional[List[str]] = Field(None, description="Publications or technical writing.")
    conferences: Optional[List[str]] = Field(None, description="Conferences attended or presented at.")
    languages: Optional[List[Skill]] = Field(None, description="Languages known (natural languages).")
    volunteer_work: Optional[List[str]] = Field(None, description="Volunteer work or community service.")
    interests: Optional[List[str]] = Field(None, description="Personal interests or hobbies.")
    references: Optional[str] = Field(None, description="References or note about references.")
    additional_sections: Optional[Dict[str, List[str]]] = Field(
        None, description="Any additional sections in the resume."
    )
