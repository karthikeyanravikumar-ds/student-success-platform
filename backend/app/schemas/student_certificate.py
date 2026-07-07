from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class StudentCertificateCreate(BaseModel):
    certificate_name: str
    certificate_type: str
    issuer: str | None = None
    issue_date: date | None = None


class StudentCertificateResponse(BaseModel):
    id: UUID
    student_id: UUID

    certificate_name: str
    certificate_type: str
    issuer: str | None = None
    issue_date: date | None = None

    file_path: str

    verification_status: str

    verified_by: UUID | None = None
    verified_at: datetime | None = None
    verification_remarks: str | None = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CertificateVerificationRequest(BaseModel):
    verification_remarks: str | None = None