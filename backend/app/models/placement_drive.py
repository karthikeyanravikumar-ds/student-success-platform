from datetime import date
from enum import Enum
from uuid import UUID

from sqlalchemy import Boolean, Date, Enum as SQLEnum, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class EmploymentType(str, Enum):
    FULL_TIME = "Full Time"
    INTERNSHIP = "Internship"


class DriveStatus(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    COMPLETED = "Completed"


class PlacementDrive(BaseModel):
    __tablename__ = "placement_drives"

    company_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("companies.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    job_role: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    employment_type: Mapped[EmploymentType] = mapped_column(
        SQLEnum(EmploymentType),
        nullable=False,
    )

    package: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    drive_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    registration_deadline: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    minimum_cgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    minimum_attendance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=75.0,
    )

    backlog_allowed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    vacancies: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    required_skills: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    status: Mapped[DriveStatus] = mapped_column(
        SQLEnum(DriveStatus),
        nullable=False,
        default=DriveStatus.OPEN,
    )

    company = relationship(
        "Company",
        back_populates="placement_drives",
    )

    applications = relationship(
        "Application",
        back_populates="drive",
    )