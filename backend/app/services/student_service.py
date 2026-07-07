from math import ceil
from pathlib import Path
from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate

from fastapi import UploadFile
from app.uploads.upload_service import UploadService
from app.uploads.validators import validate_pdf

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
        page: int = 1,
        size: int = 10,
        search: str | None = None,
        department_id=None,
        program_id=None,
        semester: int | None = None,
        is_active: bool | None = None,
        sort: str = "full_name",
    ):
        return StudentRepository.get_all(
            db=db,
            page=page,
            size=size,
            search=search,
            department_id=department_id,
            program_id=program_id,
            semester=semester,
            is_active=is_active,
            sort=sort,
        )

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
    
    