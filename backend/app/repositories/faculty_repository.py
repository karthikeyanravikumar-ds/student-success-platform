from uuid import UUID
from sqlalchemy.orm import Session
from app.models.faculty import Faculty
from app.utils.pagination import paginate
from app.utils.search import apply_search
from app.utils.filtering import apply_filters
from app.utils.sorting import apply_sort

class FacultyRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        faculty = Faculty(**data)

        db.add(faculty)
        db.commit()
        db.refresh(faculty)

        return faculty

    @staticmethod
    def get_all(
        db: Session,
        page: int = 1,
        size: int = 10,
        search: str | None = None,
        department_id: UUID | None = None,
        is_active: bool | None = None,
        sort: str = "full_name",
    ):
        query = db.query(Faculty)

        # Search
        query = apply_search(
            query=query,
            model=Faculty,
            search=search,
            fields=[
                "full_name",
                "employee_id",
                "designation",
            ],
        )

        # Filters
        query = apply_filters(
            query=query,
            model=Faculty,
            department_id=department_id,
            is_active=is_active,
        )

        # Sorting
        query = apply_sort(
            query=query,
            model=Faculty,
            sort=sort,
        )

        # Pagination
        return paginate(
            query=query,
            page=page,
            size=size,
        )

    @staticmethod
    def get_by_id(
        db: Session,
        faculty_id: UUID,
    ):
        return (
            db.query(Faculty)
            .filter(Faculty.id == faculty_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        faculty: Faculty,
    ):
        db.commit()
        db.refresh(faculty)
        return faculty

    @staticmethod
    def delete(
        db: Session,
        faculty: Faculty,
    ):
        db.delete(faculty)
        db.commit()

    @staticmethod
    def update_profile_photo_path(
        db: Session,
        faculty: Faculty,
        profile_photo_path: str,
    ):
        faculty.profile_photo_path = profile_photo_path

        db.commit()
        db.refresh(faculty)

        return faculty