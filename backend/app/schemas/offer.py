from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.offer import OfferStatus


class OfferCreate(BaseModel):
    interview_id: UUID
    offer_date: date
    joining_date: date
    package: float = Field(..., ge=0)
    remarks: str | None = None


class OfferUpdate(BaseModel):
    joining_date: date | None = None
    package: float | None = Field(None, ge=0)
    status: OfferStatus | None = None
    remarks: str | None = None


class OfferResponse(BaseModel):
    id: UUID
    interview_id: UUID
    offer_date: date
    joining_date: date
    package: float
    status: OfferStatus
    remarks: str | None = None

    class Config:
        from_attributes = True