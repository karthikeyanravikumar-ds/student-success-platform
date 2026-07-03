from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:

    @staticmethod
    def create(
        db,
        student: StudentCreate,
    ):
        return StudentRepository.create(
            db,
            student.model_dump(),
        )

    @staticmethod
    def get_profile(
        db,
        user_id,
    ):
        return StudentRepository.get_by_user_id(
            db,
            user_id,
        )

    @staticmethod
    def get_all(
        db,
    ):
        return StudentRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        student_id,
    ):
        return StudentRepository.get_by_id(
            db,
            student_id,
        )

    @staticmethod
    def update(
        db,
        student_id,
        request: StudentUpdate,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(student, key, value)

        return StudentRepository.update(
            db,
            student,
        )

    @staticmethod
    def delete(
        db,
        student_id,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return False

        StudentRepository.delete(
            db,
            student,
        )

        return True