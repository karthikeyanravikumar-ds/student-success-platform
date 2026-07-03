from datetime import date

from app.models.application import ApplicationStatus
from app.repositories.application_repository import ApplicationRepository
from app.repositories.placement_drive_repository import PlacementDriveRepository
from app.repositories.result_repository import ResultRepository
from app.repositories.student_repository import StudentRepository
from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
)

class ApplicationService:

    @staticmethod
    def apply(
        db,
        request: ApplicationCreate,
    ):
        student = StudentRepository.get_by_id(
            db,
            request.student_id,
        )

        if student is None:
            raise ValueError("Student not found")

        drive = PlacementDriveRepository.get_by_id(
            db,
            request.drive_id,
        )

        if drive is None:
            raise ValueError("Placement drive not found")

        existing = (
            ApplicationRepository.get_existing_application(
                db,
                request.student_id,
                request.drive_id,
            )
        )

        if existing:
            raise ValueError(
                "Student has already applied for this drive"
            )

        if drive.status.value != "Open":
            raise ValueError(
                "Placement drive is not open"
            )

        if drive.registration_deadline < date.today():
            raise ValueError(
                "Registration deadline has passed"
            )

        results = ResultRepository.get_by_student(
            db,
            request.student_id,
        )

        if not results:
            raise ValueError(
                "No result available for this student"
            )

        latest_result = max(
            results,
            key=lambda r: r.semester,
        )

        if latest_result.cgpa < drive.minimum_cgpa:
            raise ValueError(
                f"Minimum CGPA required is {drive.minimum_cgpa}"
            )

        data = {
            "student_id": request.student_id,
            "drive_id": request.drive_id,
            "status": ApplicationStatus.APPLIED,
            "remarks": None,
        }

        return ApplicationRepository.create(
            db,
            data,
        )

    @staticmethod
    def get_all(db):
        return ApplicationRepository.get_all(db)

    @staticmethod
    def get_by_student(
        db,
        student_id,
    ):
        return ApplicationRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def get_by_drive(
        db,
        drive_id,
    ):
        return ApplicationRepository.get_by_drive(
            db,
            drive_id,
        )

    @staticmethod
    def update(
        db,
        application_id,
        request: ApplicationUpdate,
    ):
        application = ApplicationRepository.get_by_id(
            db,
            application_id,
        )

        if application is None:
            return None

        data = request.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(application, key, value)

        return ApplicationRepository.update(
            db,
            application,
        )

    @staticmethod
    def delete(
        db,
        application_id,
    ):
        application = ApplicationRepository.get_by_id(
            db,
            application_id,
        )

        if application is None:
            return False

        ApplicationRepository.delete(
            db,
            application,
        )

        return True