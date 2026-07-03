from uuid import UUID

from sqlalchemy.orm import Session

from app.models.result import Result


class ResultRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        result = Result(**data)

        db.add(result)
        db.commit()
        db.refresh(result)

        return result

    @staticmethod
    def get_all(db: Session):
        return db.query(Result).all()

    @staticmethod
    def get_by_id(
        db: Session,
        result_id: UUID,
    ):
        return (
            db.query(Result)
            .filter(Result.id == result_id)
            .first()
        )

    @staticmethod
    def get_by_student(
        db: Session,
        student_id: UUID,
    ):
        return (
            db.query(Result)
            .filter(Result.student_id == student_id)
            .all()
        )

    @staticmethod
    def get_by_semester(
        db: Session,
        semester: int,
    ):
        return (
            db.query(Result)
            .filter(Result.semester == semester)
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        result: Result,
    ):
        db.delete(result)
        db.commit()