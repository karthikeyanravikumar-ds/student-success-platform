import random
from datetime import date, timedelta

from app.database.database import SessionLocal
from app.models.application import (
    Application,
    ApplicationStatus,
)
from app.models.interview import (
    Interview,
    InterviewStatus,
    InterviewType,
)


def seed_interviews():
    db = SessionLocal()

    try:

        applications = (
            db.query(Application)
            .filter(
                Application.status.in_(
                    [
                        ApplicationStatus.SHORTLISTED,
                        ApplicationStatus.SELECTED,
                    ]
                )
            )
            .all()
        )

        total = 0

        for application in applications:

            exists = (
                db.query(Interview)
                .filter(
                    Interview.application_id == application.id
                )
                .first()
            )

            if exists:
                continue

            db.add(
                Interview(
                    application_id=application.id,
                    round_number=1,
                    interview_type=random.choice(
                        list(InterviewType)
                    ),
                    interview_date=date.today()
                    + timedelta(
                        days=random.randint(1, 10)
                    ),
                    interviewer="HR Team",
                    status=random.choices(
                        [
                            InterviewStatus.PASSED,
                            InterviewStatus.FAILED,
                            InterviewStatus.SCHEDULED,
                        ],
                        weights=[40, 30, 30],
                    )[0],
                )
            )

            total += 1

        db.commit()

        print(f"Inserted {total} interviews.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_interviews()