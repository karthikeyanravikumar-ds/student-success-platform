from enum import Enum
from uuid import UUID

from sqlalchemy import Enum as SQLEnum, Float, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class ResultStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


class Result(BaseModel):
    __tablename__ = "results"

    student_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("students.id"),
        nullable=False,
    )

    semester: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    total_marks: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    total_max_marks: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    percentage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    sgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    cgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    result_status: Mapped[ResultStatus] = mapped_column(
        SQLEnum(ResultStatus),
        nullable=False,
    )

    rank: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    student = relationship(
        "Student",
        back_populates="results",
    )