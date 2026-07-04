from datetime import date
from uuid import UUID

from sqlalchemy import Boolean, Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Faculty(BaseModel):
    __tablename__ = "faculty"

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    department_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False,
    )

    employee_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    designation: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    qualification: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    joining_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    profile_photo_path: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)

    user = relationship(
    "User",
    back_populates="faculty",
)

    department = relationship(
        "Department",
        back_populates="faculty",
    )

    subjects = relationship(
        "Subject",
        back_populates="faculty",
    )

    attendance = relationship(
        "Attendance",
        back_populates="faculty",
    )

    marks = relationship(
        "Mark",
        back_populates="faculty",
    )