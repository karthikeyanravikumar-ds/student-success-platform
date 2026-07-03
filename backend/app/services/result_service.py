from app.repositories.mark_repository import MarkRepository
from app.repositories.result_repository import ResultRepository
from app.schemas.result import ResultCreate
from app.models.result import ResultStatus


class ResultService:

    @staticmethod
    def generate(
        db,
        request: ResultCreate,
    ):
        marks = MarkRepository.get_student_marks_by_semester(
            db,
            request.student_id,
            request.semester,
        )

        if not marks:
            raise ValueError(
                "No marks found for this student and semester."
            )

        total_marks = sum(
            mark.marks_obtained for mark in marks
        )

        total_max_marks = sum(
            mark.max_marks for mark in marks
        )

        percentage = (
            total_marks / total_max_marks
        ) * 100

        sgpa = round(
            percentage / 10,
            2,
        )

        previous_results = ResultRepository.get_by_student(
            db,
            request.student_id,
        )

        total_sgpa = sgpa

        for result in previous_results:
            total_sgpa += result.sgpa

        cgpa = round(
            total_sgpa / (len(previous_results) + 1),
            2,
        )

        result_status = ResultStatus.PASS

        for mark in marks:
            if mark.grade == "F":
                result_status = ResultStatus.FAIL
                break

        data = {
            "student_id": request.student_id,
            "semester": request.semester,
            "total_marks": total_marks,
            "total_max_marks": total_max_marks,
            "percentage": round(
                percentage,
                2,
            ),
            "sgpa": sgpa,
            "cgpa": cgpa,
            "result_status": result_status,
            "rank": None,
            "remarks": None,
        }

        return ResultRepository.create(
            db,
            data,
        )

    @staticmethod
    def get_all(db):
        return ResultRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        result_id,
    ):
        return ResultRepository.get_by_id(
            db,
            result_id,
        )

    @staticmethod
    def get_by_student(
        db,
        student_id,
    ):
        return ResultRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def get_by_semester(
        db,
        semester,
    ):
        return ResultRepository.get_by_semester(
            db,
            semester,
        )

    @staticmethod
    def delete(
        db,
        result_id,
    ):
        result = ResultRepository.get_by_id(
            db,
            result_id,
        )

        if result is None:
            return False

        ResultRepository.delete(
            db,
            result,
        )

        return True