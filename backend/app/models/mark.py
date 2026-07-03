from enum import Enum
from uuid import UUID

from sqlalchemy import Enum as SQLEnum, Float, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class ExamType(str, Enum):
    IA1 = "IA1"
    IA2 = "IA2"
    MID = "Mid Semester"
    END = "End Semester"
    PRACTICAL = "Practical"
    VIVA = "Viva"


class Mark(BaseModel):
    __tablename__ = "marks"

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

    semester: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    exam_type: Mapped[ExamType] = mapped_column(
        SQLEnum(ExamType),
        nullable=False,
    )

    max_marks: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    marks_obtained: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    grade: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    student = relationship(
        "Student",
        back_populates="marks",
    )

    subject = relationship(
        "Subject",
        back_populates="marks",
    )

    faculty = relationship(
        "Faculty",
        back_populates="marks",
    )