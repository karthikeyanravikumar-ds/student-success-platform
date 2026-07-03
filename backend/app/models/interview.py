from datetime import date
from enum import Enum
from uuid import UUID

from sqlalchemy import Date, Enum as SQLEnum, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class InterviewType(str, Enum):
    APTITUDE = "Aptitude"
    GROUP_DISCUSSION = "Group Discussion"
    TECHNICAL = "Technical"
    HR = "HR"
    MANAGERIAL = "Managerial"


class InterviewStatus(str, Enum):
    SCHEDULED = "Scheduled"
    PASSED = "Passed"
    FAILED = "Failed"
    ABSENT = "Absent"


class Interview(BaseModel):
    __tablename__ = "interviews"

    application_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("applications.id"),
        nullable=False,
    )

    round_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    interview_type: Mapped[InterviewType] = mapped_column(
        SQLEnum(InterviewType),
        nullable=False,
    )

    interview_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    interviewer: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[InterviewStatus] = mapped_column(
        SQLEnum(InterviewStatus),
        default=InterviewStatus.SCHEDULED,
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    application = relationship(
        "Application",
        back_populates="interviews",
    )

    offer = relationship(
    "Offer",
    back_populates="interview",
    uselist=False,
)