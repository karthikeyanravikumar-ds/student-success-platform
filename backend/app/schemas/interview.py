from datetime import date
from uuid import UUID

from pydantic import BaseModel

from app.models.interview import (
    InterviewStatus,
    InterviewType,
)


class InterviewCreate(BaseModel):
    application_id: UUID
    round_number: int
    interview_type: InterviewType
    interview_date: date
    interviewer: str
    remarks: str | None = None


class InterviewUpdate(BaseModel):
    interview_date: date | None = None
    interviewer: str | None = None
    status: InterviewStatus | None = None
    remarks: str | None = None


class InterviewResponse(BaseModel):
    id: UUID
    application_id: UUID
    round_number: int
    interview_type: InterviewType
    interview_date: date
    interviewer: str
    status: InterviewStatus
    remarks: str | None = None

    class Config:
        from_attributes = True