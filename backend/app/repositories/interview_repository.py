from uuid import UUID

from sqlalchemy.orm import Session

from app.models.interview import Interview


class InterviewRepository:

    @staticmethod
    def create(db: Session, data: dict):
        interview = Interview(**data)

        db.add(interview)
        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def get_all(db: Session):
        return db.query(Interview).all()

    @staticmethod
    def get_by_id(db: Session, interview_id: UUID):
        return (
            db.query(Interview)
            .filter(Interview.id == interview_id)
            .first()
        )

    @staticmethod
    def get_by_application(
        db: Session,
        application_id: UUID,
    ):
        return (
            db.query(Interview)
            .filter(
                Interview.application_id == application_id
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        interview: Interview,
    ):
        db.commit()
        db.refresh(interview)
        return interview

    @staticmethod
    def delete(
        db: Session,
        interview: Interview,
    ):
        db.delete(interview)
        db.commit()