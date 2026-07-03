from uuid import UUID

from sqlalchemy.orm import Session

from app.models.faculty import Faculty


class FacultyRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        faculty = Faculty(**data)

        db.add(faculty)
        db.commit()
        db.refresh(faculty)

        return faculty

    @staticmethod
    def get_all(
        db: Session,
    ):
        return db.query(Faculty).all()

    @staticmethod
    def get_by_id(
        db: Session,
        faculty_id: UUID,
    ):
        return (
            db.query(Faculty)
            .filter(Faculty.id == faculty_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        faculty: Faculty,
    ):
        db.commit()
        db.refresh(faculty)
        return faculty

    @staticmethod
    def delete(
        db: Session,
        faculty: Faculty,
    ):
        db.delete(faculty)
        db.commit()