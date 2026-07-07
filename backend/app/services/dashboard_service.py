from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.application import Application, ApplicationStatus
from app.models.attendance import Attendance, AttendanceStatus
from app.models.company import Company
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.interview import Interview
from app.models.mark import Mark
from app.models.offer import Offer
from app.models.placement_drive import DriveStatus, PlacementDrive
from app.models.program import Program
from app.models.result import Result
from app.models.student import Student
from app.models.subject import Subject
from app.models.user import User
from app.models.notification import Notification
from app.models.student_certificate import StudentCertificate


class DashboardService:

    @staticmethod
    def get_admin_dashboard(db: Session):
        total_students = db.query(Student).count()

        active_students = (
            db.query(Student)
            .filter(Student.is_active == True)
            .count()
        )

        inactive_students = total_students - active_students

        total_faculty = db.query(Faculty).count()

        total_departments = db.query(Department).count()

        total_programs = db.query(Program).count()

        total_subjects = db.query(Subject).count()

        total_companies = db.query(Company).count()

        active_drives = (
            db.query(PlacementDrive)
            .filter(
                PlacementDrive.status == DriveStatus.OPEN
            )
            .count()
        )

        total_applications = db.query(Application).count()

        total_offers = db.query(Offer).count()

        pending_certificates = (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Pending"
            )
            .count()
        )

        verified_certificates = (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Verified"
            )
            .count()
        )

        rejected_certificates = (
            db.query(StudentCertificate)
            .filter(
                StudentCertificate.verification_status == "Rejected"
            )
            .count()
        )

        total_notifications = db.query(Notification).count()

        return {
            "students": {
                "total": total_students,
                "active": active_students,
                "inactive": inactive_students,
            },
            "faculty": {
                "total": total_faculty,
            },
            "academic": {
                "departments": total_departments,
                "programs": total_programs,
                "subjects": total_subjects,
            },
            "placement": {
                "companies": total_companies,
                "active_drives": active_drives,
                "applications": total_applications,
                "offers": total_offers,
            },
            "certificates": {
                "pending": pending_certificates,
                "verified": verified_certificates,
                "rejected": rejected_certificates,
            },
            "notifications": {
                "sent": total_notifications,
            },
        }

    @staticmethod
    def get_faculty_dashboard(db: Session):

        return {
            "assigned_subjects": db.query(Subject).count(),
            "total_students": db.query(Student).count(),
            "attendance_records": db.query(Attendance).count(),
            "marks_uploaded": db.query(Mark).count(),
            "results_published": db.query(Result).count(),
        }

    @staticmethod
    def get_placement_dashboard(db: Session):

        highest_package = (
            db.query(func.max(PlacementDrive.package)).scalar() or 0
        )

        average_package = (
            db.query(func.avg(PlacementDrive.package)).scalar() or 0
        )

        return {
            "total_companies": db.query(Company).count(),
            "active_drives": db.query(PlacementDrive)
            .filter(
                PlacementDrive.status == DriveStatus.OPEN
            )
            .count(),
            "total_applications": db.query(Application).count(),
            "selected_students": db.query(Application)
            .filter(
                Application.status == ApplicationStatus.SELECTED
            )
            .count(),
            "highest_package": round(highest_package, 2),
            "average_package": round(average_package, 2),
        }

    @staticmethod
    def get_student_dashboard(db: Session):

        cgpa = db.query(func.avg(Result.cgpa)).scalar() or 0

        current_semester = (
            db.query(func.max(Result.semester)).scalar() or 1
        )

        total_attendance = db.query(Attendance).count()

        present_attendance = (
            db.query(Attendance)
            .filter(
                Attendance.status == AttendanceStatus.PRESENT
            )
            .count()
        )

        attendance_percentage = (
            (present_attendance / total_attendance) * 100
            if total_attendance > 0
            else 0
        )

        return {
            "attendance_percentage": round(attendance_percentage, 2),
            "current_cgpa": round(cgpa, 2),
            "current_semester": current_semester,
            "applied_drives": db.query(Application).count(),
            "interviews": db.query(Interview).count(),
            "offers": db.query(Offer).count(),
        }