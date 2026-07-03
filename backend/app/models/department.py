from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    department_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    department_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
    )

    programs = relationship(
    "Program",
    back_populates="department",
)

students = relationship(
    "Student",
    back_populates="department",
)

faculty = relationship(
    "Faculty",
    back_populates="department",
)

subjects = relationship(
    "Subject",
    back_populates="department",
)