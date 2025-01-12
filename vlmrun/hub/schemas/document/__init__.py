"""
Document schemas for extracting structured data from various document types.

This package contains Pydantic models for parsing different types of documents
such as invoices, receipts, driver's licenses, etc.
"""

from vlmrun.hub.schemas.document.invoice import Invoice

__all__ = ["Invoice"]
