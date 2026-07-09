from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.result import Result
from app.models.student import Student
from app.reports.student.transcript import TranscriptReport
from app.reports.student.marksheet import MarksheetReport
from app.reports.attendance.attendance_report import AttendanceReport
from app.reports.placement.placement_report import PlacementReport
from app.reports.placement.company_report import CompanyReport
from app.models.company import Company

class ReportService:

    @staticmethod
    def generate_transcript(
        db: Session,
        student_id,
    ):

        student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found",
            )

        results = (
            db.query(Result)
            .filter(
                Result.student_id == student.id
            )
            .order_by(Result.semester)
            .all()
        )

        report = TranscriptReport()

        return report.generate(
            student,
            results,
        )
    
    @staticmethod
    def generate_marksheet(
        db: Session,
        student_id,
    ):
        student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found",
            )

        report = MarksheetReport()

        return report.generate(
            db,
            student,
        )
    
    @staticmethod
    def generate_attendance_report(
        db: Session,
        student_id,
    ):
        student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found",
            )

        report = AttendanceReport()

        return report.generate(
            db,
            student,
        )
    @staticmethod
    def generate_placement_report(
        db: Session,
        student_id,
    ):
        student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found",
            )

        report = PlacementReport()

        return report.generate(
            db,
            student,
        )
    
    @staticmethod
    def generate_company_report(
        db: Session,
        company_id,
    ):
        company = (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

        if company is None:
            raise HTTPException(
                status_code=404,
                detail="Company not found",
            )

        report = CompanyReport()

        return report.generate(
            db,
            company,
        )
    
