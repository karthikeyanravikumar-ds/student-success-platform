from app.repositories.application_repository import (
    ApplicationRepository,
)
from app.repositories.interview_repository import (
    InterviewRepository,
)
from app.schemas.interview import (
    InterviewCreate,
    InterviewUpdate,
)


class InterviewService:

    @staticmethod
    def create(
        db,
        request: InterviewCreate,
    ):
        application = ApplicationRepository.get_by_id(
            db,
            request.application_id,
        )

        if application is None:
            return None

        return InterviewRepository.create(
            db,
            request.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return InterviewRepository.get_all(db)

    @staticmethod
    def get_by_application(
        db,
        application_id,
    ):
        return InterviewRepository.get_by_application(
            db,
            application_id,
        )

    @staticmethod
    def update(
        db,
        interview_id,
        request: InterviewUpdate,
    ):
        interview = InterviewRepository.get_by_id(
            db,
            interview_id,
        )

        if interview is None:
            return None

        data = request.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(interview, key, value)

        return InterviewRepository.update(
            db,
            interview,
        )

    @staticmethod
    def delete(
        db,
        interview_id,
    ):
        interview = InterviewRepository.get_by_id(
            db,
            interview_id,
        )

        if interview is None:
            return False

        InterviewRepository.delete(
            db,
            interview,
        )

        return True