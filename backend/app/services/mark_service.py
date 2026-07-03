from app.repositories.mark_repository import MarkRepository
from app.schemas.mark import MarkCreate, MarkUpdate


class MarkService:

    @staticmethod
    def calculate_grade(
        marks_obtained: float,
        max_marks: int,
    ) -> str:

        percentage = (marks_obtained / max_marks) * 100

        if percentage >= 90:
            return "O"

        if percentage >= 80:
            return "A+"

        if percentage >= 70:
            return "A"

        if percentage >= 60:
            return "B+"

        if percentage >= 50:
            return "B"

        if percentage >= 40:
            return "C"

        return "F"

    @staticmethod
    def create(
        db,
        request: MarkCreate,
    ):

        if request.marks_obtained > request.max_marks:
            raise ValueError(
                "Marks obtained cannot exceed maximum marks."
            )

        data = request.model_dump()

        data["grade"] = MarkService.calculate_grade(
            request.marks_obtained,
            request.max_marks,
        )

        return MarkRepository.create(
            db,
            data,
        )

    @staticmethod
    def get_all(db):
        return MarkRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        mark_id,
    ):
        return MarkRepository.get_by_id(
            db,
            mark_id,
        )

    @staticmethod
    def get_by_student(
        db,
        student_id,
    ):
        return MarkRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def get_by_subject(
        db,
        subject_id,
    ):
        return MarkRepository.get_by_subject(
            db,
            subject_id,
        )

    @staticmethod
    def get_by_faculty(
        db,
        faculty_id,
    ):
        return MarkRepository.get_by_faculty(
            db,
            faculty_id,
        )

    @staticmethod
    def get_by_semester(
        db,
        semester,
    ):
        return MarkRepository.get_by_semester(
            db,
            semester,
        )

    @staticmethod
    def update(
        db,
        mark_id,
        request: MarkUpdate,
    ):

        mark = MarkRepository.get_by_id(
            db,
            mark_id,
        )

        if mark is None:
            return None

        data = request.model_dump(
            exclude_unset=True,
        )

        if (
            "marks_obtained" in data
            or "max_marks" in data
        ):

            marks = data.get(
                "marks_obtained",
                mark.marks_obtained,
            )

            maximum = data.get(
                "max_marks",
                mark.max_marks,
            )

            if marks > maximum:
                raise ValueError(
                    "Marks obtained cannot exceed maximum marks."
                )

            data["grade"] = (
                MarkService.calculate_grade(
                    marks,
                    maximum,
                )
            )

        for key, value in data.items():
            setattr(
                mark,
                key,
                value,
            )

        return MarkRepository.update(
            db,
            mark,
        )

    @staticmethod
    def delete(
        db,
        mark_id,
    ):

        mark = MarkRepository.get_by_id(
            db,
            mark_id,
        )

        if mark is None:
            return False

        MarkRepository.delete(
            db,
            mark,
        )

        return True