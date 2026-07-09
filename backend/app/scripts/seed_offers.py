import random
from datetime import date, timedelta

from app.database.database import SessionLocal
from app.models.interview import (
    Interview,
    InterviewStatus,
)
from app.models.offer import (
    Offer,
    OfferStatus,
)


def seed_offers():
    db = SessionLocal()

    try:

        interviews = (
            db.query(Interview)
            .filter(
                Interview.status == InterviewStatus.PASSED
            )
            .all()
        )

        total = 0

        for interview in interviews:

            if interview.offer:
                continue

            package = random.choice(
                [4.5, 6, 8, 10, 12, 15]
            )

            db.add(
                Offer(
                    interview_id=interview.id,
                    offer_date=date.today(),
                    joining_date=date.today()
                    + timedelta(days=60),
                    package=package,
                    status=random.choice(
                        list(OfferStatus)
                    ),
                )
            )

            total += 1

        db.commit()

        print(f"Inserted {total} offers.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_offers()