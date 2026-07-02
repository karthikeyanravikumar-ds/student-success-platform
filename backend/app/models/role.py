from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    role_name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(Text)

    users = relationship(
        "User",
        back_populates="role",
    )