from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class Addendum(BaseModel):
    addendum_date: Optional[datetime] = Field(None, description="Date and time the addendum/amendment was created")
    reason: Optional[str] = Field(None, description="Reason for the addendum (e.g., corrected data, additional info)")
    text: Optional[str] = Field(None, description="Content or changes described in the addendum")


class PatientInformation(BaseModel):
    patient_name: Optional[str] = Field(None, description="Full name of the patient")
    patient_id: Optional[str] = Field(None, description="Medical record number or patient identifier")
    date_of_birth: Optional[date] = Field(None, description="Patient's date of birth")
    gender: Optional[str] = Field(None, description="Patient's gender")
    clinical_history: Optional[str] = Field(None, description="Relevant clinical history")


class FacilityInformation(BaseModel):
    facility_name: Optional[str] = Field(None, description="Name of the medical facility")
    facility_address: Optional[str] = Field(None, description="Facility address or contact information")


class GrossExamination(BaseModel):
    description: Optional[str] = Field(None, description="Narrative description of the specimen at gross examination")
    specimen_measurements: Optional[List[str]] = Field(None, description="List of measurement strings (e.g. '3 x 2 x 1 cm')")
    specimen_weight: Optional[float] = Field(None, description="Weight in grams if relevant")
    gross_margins: Optional[str] = Field(None, description="Gross margin description (if applicable)")
    cassette_details: Optional[List[str]] = Field(None, description="Details of cassettes used, how tissue was sectioned")
    gross_findings: Optional[List[str]] = Field(None, description="Key gross findings (e.g., necrosis, hemorrhage)")


class MicroscopicExamination(BaseModel):
    description: Optional[str] = Field(None, description="Detailed microscopic or histological findings")
    cellular_features: Optional[str] = Field(None, description="Cellular characteristics (atypia, pleomorphism, etc.)")
    architectural_features: Optional[str] = Field(None, description="Architecture (glandular, papillary, etc.)")
    microscopic_margins: Optional[str] = Field(None, description="Microscopic margin status or description")
    lymphovascular_invasion: Optional[bool] = Field(None, description="Presence/absence of lymphovascular invasion (LVI)")
    perineural_invasion: Optional[bool] = Field(None, description="Presence/absence of perineural invasion (PNI)")
    additional_findings: Optional[List[str]] = Field(None, description="Other significant findings")


class SpecimenDiagnosis(BaseModel):
    diagnosis_text: Optional[str] = Field(None, description="Summary of the pathological diagnosis or interpretation")
    additional_notes: Optional[str] = Field(None, description="Any extra notes or classification details")


class ImmunohistochemistryResults(BaseModel):
    marker_name: Optional[str] = Field(None, description="Name of IHC marker (e.g., ER, PR, CD20)")
    result: Optional[str] = Field(None, description="Interpretation (Positive, Negative, etc.)")
    percentage: Optional[float] = Field(None, description="Approx. percentage of positive cells if known (value between 0.0 and 1.0)")
    intensity: Optional[str] = Field(None, description="Intensity of staining (e.g., 1+, 2+, 3+)")
    pattern: Optional[str] = Field(None, description="Staining pattern (nuclear, cytoplasmic, membranous)")
    control_validity: Optional[bool] = Field(None, description="Whether control stain was valid")


class MolecularStudies(BaseModel):
    test_name: Optional[str] = Field(None, description="Name of molecular test (e.g., EGFR, KRAS, BRAF)")
    result: Optional[str] = Field(None, description="Result or interpretation (e.g., Mutated, Wild-type, Negative)")
    methodology: Optional[str] = Field(None, description="Method used (PCR, NGS, FISH, etc.)")
    interpretation: Optional[str] = Field(None, description="Clinical or pathological significance if known")


class SpecimenInformation(BaseModel):
    specimen_id: Optional[str] = Field(None, description="Unique identifier or label for the specimen (e.g., 'Specimen A')")
    specimen_source: Optional[str] = Field(None, description="Combined anatomic site/type (e.g., 'Biopsy of right lung')")
    collection_date: Optional[datetime] = Field(None, description="Date/time of specimen collection")
    received_date: Optional[datetime] = Field(None, description="Date/time specimen was received in lab")
    preservation: Optional[str] = Field(None, description="Preservation method if relevant (e.g., Formalin)")

    gross_examination: Optional[List[GrossExamination]] = Field(None, description="List of gross exam details")
    microscopic_examination: Optional[List[MicroscopicExamination]] = Field(None, description="List of microscopic exam details")

    immunohistochemistry: Optional[List[ImmunohistochemistryResults]] = Field(None, description="Any IHC results for this specimen")
    molecular_studies: Optional[List[MolecularStudies]] = Field(None, description="Any molecular tests on this specimen")

    diagnosis: Optional[SpecimenDiagnosis] = Field(None, description="Diagnosis/interpretation specific to this specimen")


class PathologyReport(BaseModel):
    accession_number: Optional[str] = Field(None, description="Unique report identifier (accession)")
    report_type: Optional[str] = Field(None, description="Type of laboratory report (e.g., 'Surgical Pathology', 'Cytology')")
    report_date: Optional[datetime] = Field(None, description="Date/time report was generated or finalized")
    report_status: Optional[str] = Field(None, description="Status of the report")

    patient: Optional[PatientInformation] = Field(None, description="Patient demographics (all optional)")
    facility: Optional[FacilityInformation] = Field(None, description="Facility/lab info, simplified")

    specimens: Optional[List[SpecimenInformation]] = Field(None, description="List of all specimens examined in this report")

    integrated_diagnosis: Optional[str] = Field(None, description="An overall or integrated interpretation across specimens")
    clinical_notes: Optional[str] = Field(None, description="High-level clinical notes, if relevant")
    comments: Optional[str] = Field(None, description="General comments, disclaimers, or remarks")

    pathologist_name: Optional[str] = Field(None, description="Name of the reporting laboratory professional")

    addenda: Optional[List[Addendum]] = Field(None, description="Any amendments or addenda appended to this report")