from app.repositories.interview_repository import InterviewRepository
from app.repositories.offer_repository import OfferRepository
from app.schemas.offer import OfferCreate, OfferUpdate


class OfferService:

    @staticmethod
    def create(db, request: OfferCreate):
        interview = InterviewRepository.get_by_id(
            db,
            request.interview_id,
        )

        if interview is None:
            return None

        existing = OfferRepository.get_by_interview(
            db,
            request.interview_id,
        )

        if existing:
            raise ValueError(
                "Offer already exists for this interview"
            )

        return OfferRepository.create(
            db,
            request.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return OfferRepository.get_all(db)

    @staticmethod
    def get_by_interview(
        db,
        interview_id,
    ):
        return OfferRepository.get_by_interview(
            db,
            interview_id,
        )

    @staticmethod
    def update(
        db,
        offer_id,
        request: OfferUpdate,
    ):
        offer = OfferRepository.get_by_id(
            db,
            offer_id,
        )

        if offer is None:
            return None

        data = request.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(
                offer,
                key,
                value,
            )

        return OfferRepository.update(
            db,
            offer,
        )

    @staticmethod
    def delete(
        db,
        offer_id,
    ):
        offer = OfferRepository.get_by_id(
            db,
            offer_id,
        )

        if offer is None:
            return False

        OfferRepository.delete(
            db,
            offer,
        )

        return True