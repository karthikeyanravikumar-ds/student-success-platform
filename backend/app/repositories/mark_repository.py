from uuid import UUID

from sqlalchemy.orm import Session

from app.models.mark import Mark


class MarkRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        mark = Mark(**data)

        db.add(mark)
        db.commit()
        db.refresh(mark)

        return mark

    @staticmethod
    def get_all(db: Session):
        return db.query(Mark).all()

    @staticmethod
    def get_by_id(
        db: Session,
        mark_id: UUID,
    ):
        return (
            db.query(Mark)
            .filter(Mark.id == mark_id)
            .first()
        )

    @staticmethod
    def get_by_student(
        db: Session,
        student_id: UUID,
    ):
        return (
            db.query(Mark)
            .filter(Mark.student_id == student_id)
            .all()
        )

    @staticmethod
    def get_by_subject(
        db: Session,
        subject_id: UUID,
    ):
        return (
            db.query(Mark)
            .filter(Mark.subject_id == subject_id)
            .all()
        )

    @staticmethod
    def get_by_faculty(
        db: Session,
        faculty_id: UUID,
    ):
        return (
            db.query(Mark)
            .filter(Mark.faculty_id == faculty_id)
            .all()
        )

    @staticmethod
    def get_by_semester(
        db: Session,
        semester: int,
    ):
        return (
            db.query(Mark)
            .filter(Mark.semester == semester)
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        mark: Mark,
    ):
        db.commit()
        db.refresh(mark)

        return mark

    @staticmethod
    def delete(
        db: Session,
        mark: Mark,
    ):
        db.delete(mark)
        db.commit()

    @staticmethod
    def get_student_marks_by_semester(
        db: Session,
        student_id: UUID,
        semester: int,
    ):
        return (
            db.query(Mark)
            .filter(
                Mark.student_id == student_id,
                Mark.semester == semester,
            )
            .all()
        )