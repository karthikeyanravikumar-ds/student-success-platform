from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.result import Result
from app.models.student import Student
from app.reports.student.transcript import TranscriptReport


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