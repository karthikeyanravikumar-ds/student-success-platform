from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.placement_drive import (
    DriveStatus,
    EmploymentType,
)


class PlacementDriveBase(BaseModel):
    company_id: UUID
    title: str
    job_role: str
    employment_type: EmploymentType
    package: float = Field(..., ge=0)
    location: str
    drive_date: date
    registration_deadline: date
    minimum_cgpa: float = Field(0.0, ge=0, le=10)
    minimum_attendance: float = Field(75.0, ge=0, le=100)
    backlog_allowed: bool = False
    vacancies: int = Field(..., ge=1)
    required_skills: str | None = None
    status: DriveStatus = DriveStatus.OPEN


class PlacementDriveCreate(PlacementDriveBase):
    pass


class PlacementDriveUpdate(BaseModel):
    title: str | None = None
    job_role: str | None = None
    employment_type: EmploymentType | None = None
    package: float | None = Field(None, ge=0)
    location: str | None = None
    drive_date: date | None = None
    registration_deadline: date | None = None
    minimum_cgpa: float | None = Field(None, ge=0, le=10)
    minimum_attendance: float | None = Field(None, ge=0, le=100)
    backlog_allowed: bool | None = None
    vacancies: int | None = Field(None, ge=1)
    required_skills: str | None = None
    status: DriveStatus | None = None


class PlacementDriveResponse(PlacementDriveBase):
    id: UUID

    class Config:
        from_attributes = True