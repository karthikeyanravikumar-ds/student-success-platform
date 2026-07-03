from uuid import UUID

from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRepository:

    @staticmethod
    def create(db: Session, data: dict):
        application = Application(**data)

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    @staticmethod
    def get_all(db: Session):
        return db.query(Application).all()

    @staticmethod
    def get_by_id(db: Session, application_id: UUID):
        return (
            db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

    @staticmethod
    def get_by_student(db: Session, student_id: UUID):
        return (
            db.query(Application)
            .filter(Application.student_id == student_id)
            .all()
        )

    @staticmethod
    def get_by_drive(db: Session, drive_id: UUID):
        return (
            db.query(Application)
            .filter(Application.drive_id == drive_id)
            .all()
        )

    @staticmethod
    def get_existing_application(
        db: Session,
        student_id: UUID,
        drive_id: UUID,
    ):
        return (
            db.query(Application)
            .filter(
                Application.student_id == student_id,
                Application.drive_id == drive_id,
            )
            .first()
        )

    @staticmethod
    def update(db: Session, application: Application):
        db.commit()
        db.refresh(application)
        return application

    @staticmethod
    def delete(db: Session, application: Application):
        db.delete(application)
        db.commit()