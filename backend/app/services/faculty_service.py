from app.repositories.faculty_repository import FacultyRepository
from app.schemas.faculty import (
    FacultyCreate,
    FacultyUpdate,
)


class FacultyService:

    @staticmethod
    def create(
        db,
        faculty: FacultyCreate,
    ):
        return FacultyRepository.create(
            db,
            faculty.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return FacultyRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        faculty_id,
    ):
        return FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

    @staticmethod
    def update(
        db,
        faculty_id,
        request: FacultyUpdate,
    ):
        faculty = FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

        if faculty is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(faculty, key, value)

        return FacultyRepository.update(
            db,
            faculty,
        )

    @staticmethod
    def delete(
        db,
        faculty_id,
    ):
        faculty = FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

        if faculty is None:
            return False

        FacultyRepository.delete(
            db,
            faculty,
        )

        return True