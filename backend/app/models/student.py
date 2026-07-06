import uuid
from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("programs.id"),
        nullable=False,
    )

    department_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False,
    )

    roll_no: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    gender: Mapped[str | None] = mapped_column(String(20))

    dob: Mapped[date | None] = mapped_column(Date)

    phone: Mapped[str | None] = mapped_column(String(20))

    division: Mapped[str | None] = mapped_column(String(10))

    admission_year: Mapped[int | None] = mapped_column(Integer)

    graduation_year: Mapped[int | None] = mapped_column(Integer)

    current_semester: Mapped[int | None] = mapped_column(Integer)

    resume_path: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)

    profile_photo_path: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    # Relationships

    user = relationship(
    "User",
    back_populates="student",
)

    department = relationship(
        "Department",
        back_populates="students",
    )

    program = relationship(
        "Program",
        back_populates="students",
    )

    attendance = relationship(
        "Attendance",
        back_populates="student",
    )

    marks = relationship(
        "Mark",
        back_populates="student",
    )

    results = relationship(
        "Result",
        back_populates="student",
    )

    applications = relationship(
        "Application",
        back_populates="student",
    )

    certificates = relationship(
    "StudentCertificate",
    back_populates="student",
    cascade="all, delete-orphan",
)