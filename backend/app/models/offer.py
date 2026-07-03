from datetime import date
from enum import Enum
from uuid import UUID

from sqlalchemy import Date, Enum as SQLEnum, Float, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class OfferStatus(str, Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class Offer(BaseModel):
    __tablename__ = "offers"

    interview_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("interviews.id"),
        nullable=False,
    )

    offer_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    joining_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    package: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    status: Mapped[OfferStatus] = mapped_column(
        SQLEnum(OfferStatus),
        default=OfferStatus.PENDING,
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    interview = relationship(
        "Interview",
        back_populates="offer",
    )