from app.notifications.notification_types import NotificationType
from app.notifications.templates import NotificationTemplates
from app.schemas.notification import NotificationCreate
from app.services.notification_service import NotificationService


class NotificationManager:

    @staticmethod
    def certificate_verified(
        db,
        user_id,
        certificate_id,
    ):
        title, message = NotificationTemplates.certificate_verified()

        NotificationService.create(
            db,
            NotificationCreate(
                user_id=user_id,
                title=title,
                message=message,
                notification_type=NotificationType.CERTIFICATE,
                data={
                    "certificate_id": str(certificate_id),
                },
            ),
        )

    @staticmethod
    def certificate_rejected(
        db,
        user_id,
        certificate_id,
        remarks: str,
    ):
        title, message = NotificationTemplates.certificate_rejected()

        NotificationService.create(
            db,
            NotificationCreate(
                user_id=user_id,
                title=title,
                message=message,
                notification_type=NotificationType.CERTIFICATE,
                data={
                    "certificate_id": str(certificate_id),
                    "remarks": remarks,
                },
            ),
        )