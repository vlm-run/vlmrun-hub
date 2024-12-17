from datetime import date
from vlmrun.hub.schemas.banking.document_verification import (
    DocumentVerification,
    DocumentType,
    DocumentVerificationStatus,
    UserData,
)


def test_document_verification_schema():
    # Test valid data
    user_data = {
        "user_id": "123",
        "full_name": "John Doe",
        "date_of_birth": date(1990, 1, 1),
        "nationality": "US",
        "address": "123 Main St",
    }

    data = {
        "document_type": "passport",
        "document_number": "AB123456",
        "issuing_authority": "US Department of State",
        "issue_date": "2020-01-01",
        "expiry_date": date(2030, 1, 1),
        "is_original": True,
        "user_data": user_data,
    }

    doc = DocumentVerification(**data)
    assert doc.document_type == DocumentType.passport
    assert doc.verification_status == DocumentVerificationStatus.pending
