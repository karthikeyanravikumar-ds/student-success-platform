import random

from app.database.database import SessionLocal
from app.models.application import Application, ApplicationStatus
from app.models.placement_drive import DriveStatus, PlacementDrive
from app.models.result import Result
from app.models.student import Student


def seed_applications():
    db = SessionLocal()

    try:
        students = db.query(Student).filter(Student.is_active == True).all()

        drives = (
            db.query(PlacementDrive)
            .filter(PlacementDrive.status == DriveStatus.OPEN)
            .all()
        )

        total = 0

        for student in students:

            latest_result = (
                db.query(Result)
                .filter(Result.student_id == student.id)
                .order_by(Result.semester.desc())
                .first()
            )

            cgpa = latest_result.cgpa if latest_result else 0

            for drive in drives:

                if cgpa < drive.minimum_cgpa:
                    continue

                if random.random() > 0.45:
                    continue

                exists = (
                    db.query(Application)
                    .filter(
                        Application.student_id == student.id,
                        Application.drive_id == drive.id,
                    )
                    .first()
                )

                if exists:
                    continue

                status = random.choices(
                    [
                        ApplicationStatus.APPLIED,
                        ApplicationStatus.SHORTLISTED,
                        ApplicationStatus.REJECTED,
                        ApplicationStatus.SELECTED,
                    ],
                    weights=[50, 20, 20, 10],
                    k=1,
                )[0]

                db.add(
                    Application(
                        student_id=student.id,
                        drive_id=drive.id,
                        status=status,
                    )
                )

                total += 1

        db.commit()

        print(f"Inserted {total} applications.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_applications()