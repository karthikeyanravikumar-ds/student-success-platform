from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.schemas.notification import NotificationResponse
from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


@router.get(
    "/me",
    response_model=list[NotificationResponse],
)
def get_my_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return NotificationService.get_user_notifications(
        db,
        current_user.id,
    )


@router.put(
    "/{notification_id}/read",
    response_model=NotificationResponse,
)
def mark_notification_as_read(
    notification_id: UUID,
    db: Session = Depends(get_db),
):
    notification = NotificationService.mark_as_read(
        db,
        notification_id,
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    return notification


@router.delete(
    "/{notification_id}",
)
def delete_notification(
    notification_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = NotificationService.delete(
        db,
        notification_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    return {
        "message": "Notification deleted successfully",
    }