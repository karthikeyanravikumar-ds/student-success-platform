import uuid
from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import relationship
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

    gender: Mapped[str | None] = mapped_column(
        String(20),
    )

    dob: Mapped[date | None] = mapped_column(Date)

    phone: Mapped[str | None] = mapped_column(
        String(20),
    )

    division: Mapped[str | None] = mapped_column(
        String(10),
    )

    admission_year: Mapped[int | None] = mapped_column(
        Integer,
    )

    graduation_year: Mapped[int | None] = mapped_column(
        Integer,
    )

    current_semester: Mapped[int | None] = mapped_column(
        Integer,
    )

    profile_photo: Mapped[str | None] = mapped_column(
        Text,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    user = relationship("User")
    department = relationship("Department")
    program = relationship("Program")

    department = relationship(
    "Department",
    back_populates="students",
)

program = relationship(
    "Program",
    back_populates="students",
)

department = relationship(
    "Department",
    back_populates="subjects",
)

program = relationship(
    "Program",
    back_populates="subjects",
)

faculty = relationship(
    "Faculty",
    back_populates="subjects",
)

attendance = relationship(
    "Attendance",
    back_populates="student",
)