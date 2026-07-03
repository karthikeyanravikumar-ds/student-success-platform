from uuid import UUID

from pydantic import BaseModel

from app.models.application import ApplicationStatus


class ApplicationCreate(BaseModel):
    student_id: UUID
    drive_id: UUID


class ApplicationUpdate(BaseModel):
    status: ApplicationStatus | None = None
    remarks: str | None = None


class ApplicationResponse(BaseModel):
    id: UUID

    student_id: UUID

    drive_id: UUID

    status: ApplicationStatus

    remarks: str | None = None

    applied_at: str

    class Config:
        from_attributes = True