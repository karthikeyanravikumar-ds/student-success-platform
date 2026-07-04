from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.application import Application, ApplicationStatus
from app.models.attendance import Attendance, AttendanceStatus
from app.models.company import Company
from app.models.department import Department
from app.models.placement_drive import PlacementDrive, DriveStatus
from app.models.result import Result, ResultStatus
from app.models.student import Student


class AnalyticsService:

    @staticmethod
    def placement_analytics(db: Session):

        total_students = db.query(Student).count()

        placed_students = (
            db.query(Application)
            .filter(
                Application.status == ApplicationStatus.SELECTED
            )
            .count()
        )

        active_drives = (
            db.query(PlacementDrive)
            .filter(
                PlacementDrive.status == DriveStatus.OPEN
            )
            .count()
        )

        total_companies = db.query(Company).count()

        placement_percentage = (
            (placed_students / total_students) * 100
            if total_students > 0
            else 0
        )

        return {
            "total_students": total_students,
            "placed_students": placed_students,
            "placement_percentage": round(
                placement_percentage,
                2,
            ),
            "active_drives": active_drives,
            "total_companies": total_companies,
        }

    @staticmethod
    def attendance_analytics(db: Session):

        present = (
            db.query(Attendance)
            .filter(
                Attendance.status == AttendanceStatus.PRESENT
            )
            .count()
        )

        absent = (
            db.query(Attendance)
            .filter(
                Attendance.status == AttendanceStatus.ABSENT
            )
            .count()
        )

        late = (
            db.query(Attendance)
            .filter(
                Attendance.status == AttendanceStatus.LATE
            )
            .count()
        )

        leave = (
            db.query(Attendance)
            .filter(
                Attendance.status == AttendanceStatus.LEAVE
            )
            .count()
        )

        total = present + absent + late + leave

        attendance_percentage = (
            (present / total) * 100
            if total > 0
            else 0
        )

        return {
            "overall_attendance": round(
                attendance_percentage,
                2,
            ),
            "present": present,
            "absent": absent,
            "late": late,
            "leave": leave,
        }

    @staticmethod
    def result_analytics(db: Session):

        average_cgpa = (
            db.query(func.avg(Result.cgpa)).scalar() or 0
        )

        highest_cgpa = (
            db.query(func.max(Result.cgpa)).scalar() or 0
        )

        passed = (
            db.query(Result)
            .filter(
                Result.result_status == ResultStatus.PASS
            )
            .count()
        )

        failed = (
            db.query(Result)
            .filter(
                Result.result_status == ResultStatus.FAIL
            )
            .count()
        )

        total = passed + failed

        pass_percentage = (
            (passed / total) * 100
            if total > 0
            else 0
        )

        return {
            "average_cgpa": round(average_cgpa, 2),
            "highest_cgpa": round(highest_cgpa, 2),
            "pass_percentage": round(pass_percentage, 2),
            "failed_students": failed,
        }

    @staticmethod
    def package_analytics(db: Session):

        highest = (
            db.query(func.max(PlacementDrive.package)).scalar() or 0
        )

        lowest = (
            db.query(func.min(PlacementDrive.package)).scalar() or 0
        )

        average = (
            db.query(func.avg(PlacementDrive.package)).scalar() or 0
        )

        return {
            "highest_package": round(highest, 2),
            "lowest_package": round(lowest, 2),
            "average_package": round(average, 2),
        }

    @staticmethod
    def department_analytics(db: Session):

        departments = db.query(Department).all()

        data = []

        for department in departments:

            total_students = (
                db.query(Student)
                .filter(
                    Student.department_id == department.id
                )
                .count()
            )

            placed_students = (
                db.query(Application)
                .join(Student)
                .filter(
                    Student.department_id == department.id,
                    Application.status == ApplicationStatus.SELECTED,
                )
                .count()
            )

            percentage = (
                (placed_students / total_students) * 100
                if total_students > 0
                else 0
            )

            data.append(
                {
                    "department_name": department.department_name,
                    "total_students": total_students,
                    "placed_students": placed_students,
                    "placement_percentage": round(
                        percentage,
                        2,
                    ),
                }
            )

        return data