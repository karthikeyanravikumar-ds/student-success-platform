from uuid import UUID

from sqlalchemy.orm import Session

from app.models.subject import Subject


class SubjectRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        subject = Subject(**data)

        db.add(subject)
        db.commit()
        db.refresh(subject)

        return subject

    @staticmethod
    def get_all(
        db: Session,
    ):
        return db.query(Subject).all()

    @staticmethod
    def get_by_id(
        db: Session,
        subject_id: UUID,
    ):
        return (
            db.query(Subject)
            .filter(Subject.id == subject_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        subject: Subject,
    ):
        db.commit()
        db.refresh(subject)
        return subject

    @staticmethod
    def delete(
        db: Session,
        subject: Subject,
    ):
        db.delete(subject)
        db.commit()