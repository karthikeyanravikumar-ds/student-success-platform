from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class NotificationCreate(BaseModel):
    user_id: UUID
    title: str
    message: str
    notification_type: str
    data: dict[str, Any] | None = None


class NotificationResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    message: str
    notification_type: str
    is_read: bool
    read_at: datetime | None = None
    data: dict[str, Any] | None = None
    created_at: datetime

    class Config:
        from_attributes = True