from uuid import UUID
from sqlalchemy.orm import Session
from app.models.student import Student
from sqlalchemy import or_
from app.utils.pagination import paginate
from app.utils.search import apply_search
from app.utils.filtering import apply_filters
from app.utils.sorting import apply_sort

class StudentRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        student = Student(**data)

        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def get_by_user_id(
        db: Session,
        user_id: UUID,
    ):
        return (
            db.query(Student)
            .filter(Student.user_id == user_id)
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        page: int = 1,
        size: int = 10,
        search: str | None = None,
        department_id: UUID | None = None,
        program_id: UUID | None = None,
        semester: int | None = None,
        is_active: bool | None = None,
        sort: str = "full_name",
    ):
        query = db.query(Student)

        # Search
        query = apply_search(
            query=query,
            model=Student,
            search=search,
            fields=[
                "full_name",
                "roll_no",
            ],
        )

        # Filters
        query = apply_filters(
            query=query,
            model=Student,
            department_id=department_id,
            program_id=program_id,
            current_semester=semester,
            is_active=is_active,
        )

        # Sorting
        query = apply_sort(
            query=query,
            model=Student,
            sort=sort,
        )

        # Pagination
        return paginate(
            query=query,
            page=page,
            size=size,
        )

    @staticmethod
    def update_profile_photo_path(
        db: Session,
        student: Student,
        profile_photo_path: str,
    ):
        student.profile_photo_path = profile_photo_path

        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def get_by_id(
        db: Session,
        student_id: UUID,
    ):
        return (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        student: Student,
    ):
        db.commit()
        db.refresh(student)
        return student
    
    @staticmethod
    def update_resume_path(
    db: Session,
    student: Student,
    resume_path: str,
    ):
      student.resume_path = resume_path

      db.commit()
      db.refresh(student)

      return student

    @staticmethod
    def delete(
        db: Session,
        student: Student,
    ):
        db.delete(student)
        db.commit()