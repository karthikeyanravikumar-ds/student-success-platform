from uuid import UUID

from sqlalchemy.orm import Session, joinedload

from app.models.mark import Mark
from app.models.result import Result
from app.models.student import Student


class ReportService:

    @staticmethod
    def get_student_transcript(
        db: Session,
        student_id: UUID,
    ):

        student = (
            db.query(Student)
            .options(
                joinedload(Student.department),
                joinedload(Student.program),
            )
            .filter(Student.id == student_id)
            .first()
        )

        if not student:
            return None

        results = (
            db.query(Result)
            .filter(Result.student_id == student.id)
            .order_by(Result.semester)
            .all()
        )

        marks = (
            db.query(Mark)
            .options(
                joinedload(Mark.subject),
            )
            .filter(Mark.student_id == student.id)
            .all()
        )

        semester_data = []

        for result in results:
            semester_data.append(
                {
                    "semester": result.semester,
                    "sgpa": result.sgpa,
                    "cgpa": result.cgpa,
                    "percentage": result.percentage,
                }
            )

        subject_data = []

        for mark in marks:
            subject_data.append(
                {
                    "subject_code": mark.subject.subject_code,
                    "subject_name": mark.subject.subject_name,
                    "exam_type": mark.exam_type.value,
                    "marks_obtained": mark.marks_obtained,
                    "max_marks": mark.max_marks,
                    "grade": mark.grade,
                }
            )

        return {
            "student_name": student.full_name,
            "roll_no": student.roll_no,
            "department": student.department.department_name,
            "program": student.program.program_name,
            "current_semester": student.current_semester,
            "semesters": semester_data,
            "subjects": subject_data,
        }