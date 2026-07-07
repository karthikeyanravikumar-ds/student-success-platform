from datetime import datetime
from uuid import UUID

from app.repositories.notification_repository import NotificationRepository
from app.schemas.notification import NotificationCreate


class NotificationService:

    @staticmethod
    def create(
        db,
        notification: NotificationCreate,
    ):
        return NotificationRepository.create(
            db,
            notification.model_dump(),
        )

    @staticmethod
    def get_user_notifications(
        db,
        user_id: UUID,
    ):
        return NotificationRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    def mark_as_read(
        db,
        notification_id: UUID,
    ):
        notification = NotificationRepository.get_by_id(
            db,
            notification_id,
        )

        if notification is None:
            return None

        notification.is_read = True
        notification.read_at = datetime.now()

        return NotificationRepository.update(
            db,
            notification,
        )

    @staticmethod
    def delete(
        db,
        notification_id: UUID,
    ):
        notification = NotificationRepository.get_by_id(
            db,
            notification_id,
        )

        if notification is None:
            return False

        NotificationRepository.delete(
            db,
            notification,
        )

        return True