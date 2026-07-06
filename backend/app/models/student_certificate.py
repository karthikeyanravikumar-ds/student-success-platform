import uuid
from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class StudentCertificate(BaseModel):
    __tablename__ = "student_certificates"

    student_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("students.id"),
        nullable=False,
    )

    certificate_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    certificate_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    issuer: Mapped[str | None] = mapped_column(
        String(255),
    )

    issue_date: Mapped[date | None] = mapped_column(
        Date,
    )

    file_path: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    verification_status: Mapped[str] = mapped_column(
        String(20),
        default="Pending",
    )

    verified_by: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    verification_remarks: Mapped[str | None] = mapped_column(
        Text,
    )

    student = relationship(
        "Student",
        back_populates="certificates",
    )

    verifier = relationship(
        "User",
    )