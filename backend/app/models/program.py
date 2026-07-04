from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Program(BaseModel):
    __tablename__ = "programs"

    department_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False,
    )

    program_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    program_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    duration_years: Mapped[int] = mapped_column(
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    department = relationship(
        "Department",
        back_populates="programs",
    )

    students = relationship(
        "Student",
        back_populates="program",
    )

    subjects = relationship(
        "Subject",
        back_populates="program",
    )