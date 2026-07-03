from app.repositories.subject_repository import SubjectRepository
from app.schemas.subject import (
    SubjectCreate,
    SubjectUpdate,
)


class SubjectService:

    @staticmethod
    def create(
        db,
        subject: SubjectCreate,
    ):
        return SubjectRepository.create(
            db,
            subject.model_dump(),
        )

    @staticmethod
    def get_all(
        db,
    ):
        return SubjectRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        subject_id,
    ):
        return SubjectRepository.get_by_id(
            db,
            subject_id,
        )

    @staticmethod
    def update(
        db,
        subject_id,
        request: SubjectUpdate,
    ):
        subject = SubjectRepository.get_by_id(
            db,
            subject_id,
        )

        if subject is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(subject, key, value)

        return SubjectRepository.update(
            db,
            subject,
        )

    @staticmethod
    def delete(
        db,
        subject_id,
    ):
        subject = SubjectRepository.get_by_id(
            db,
            subject_id,
        )

        if subject is None:
            return False

        SubjectRepository.delete(
            db,
            subject,
        )

        return True