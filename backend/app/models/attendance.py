from datetime import date
from enum import Enum
from uuid import UUID

from sqlalchemy import Date, Enum as SQLEnum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AttendanceStatus(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    LEAVE = "Leave"


class Attendance(BaseModel):
    __tablename__ = "attendance"

    student_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("students.id"),
        nullable=False,
    )

    subject_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("subjects.id"),
        nullable=False,
    )

    faculty_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("faculty.id"),
        nullable=False,
    )

    attendance_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[AttendanceStatus] = mapped_column(
        SQLEnum(AttendanceStatus),
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    student = relationship(
        "Student",
        back_populates="attendance",
    )

    faculty = relationship(
        "Faculty",
        back_populates="attendance",
    )

    subject = relationship(
        "Subject",
        back_populates="attendance",
    )