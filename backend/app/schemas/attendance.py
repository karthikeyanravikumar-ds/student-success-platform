from datetime import date
from uuid import UUID

from pydantic import BaseModel

from app.models.attendance import AttendanceStatus


class AttendanceCreate(BaseModel):
    student_id: UUID
    subject_id: UUID
    faculty_id: UUID
    attendance_date: date
    status: AttendanceStatus
    remarks: str | None = None


class AttendanceUpdate(BaseModel):
    status: AttendanceStatus | None = None
    remarks: str | None = None


class AttendanceResponse(BaseModel):
    id: UUID
    student_id: UUID
    subject_id: UUID
    faculty_id: UUID
    attendance_date: date
    status: AttendanceStatus
    remarks: str | None = None

    class Config:
        from_attributes = True