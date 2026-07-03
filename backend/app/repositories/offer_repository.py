from uuid import UUID

from sqlalchemy.orm import Session

from app.models.offer import Offer


class OfferRepository:

    @staticmethod
    def create(db: Session, data: dict):
        offer = Offer(**data)

        db.add(offer)
        db.commit()
        db.refresh(offer)

        return offer

    @staticmethod
    def get_all(db: Session):
        return db.query(Offer).all()

    @staticmethod
    def get_by_id(db: Session, offer_id: UUID):
        return (
            db.query(Offer)
            .filter(Offer.id == offer_id)
            .first()
        )

    @staticmethod
    def get_by_interview(
        db: Session,
        interview_id: UUID,
    ):
        return (
            db.query(Offer)
            .filter(
                Offer.interview_id == interview_id
            )
            .first()
        )

    @staticmethod
    def update(db: Session, offer: Offer):
        db.commit()
        db.refresh(offer)
        return offer

    @staticmethod
    def delete(db: Session, offer: Offer):
        db.delete(offer)
        db.commit()