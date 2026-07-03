from app.repositories.department_repository import DepartmentRepository
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
)


class DepartmentService:

    @staticmethod
    def create(
        db,
        department: DepartmentCreate,
    ):
        return DepartmentRepository.create(
            db,
            department.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return DepartmentRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        department_id,
    ):
        return DepartmentRepository.get_by_id(
            db,
            department_id,
        )

    @staticmethod
    def update(
        db,
        department_id,
        request: DepartmentUpdate,
    ):
        department = DepartmentRepository.get_by_id(
            db,
            department_id,
        )

        if department is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(department, key, value)

        return DepartmentRepository.update(
            db,
            department,
        )

    @staticmethod
    def delete(
        db,
        department_id,
    ):
        department = DepartmentRepository.get_by_id(
            db,
            department_id,
        )

        if department is None:
            return False

        DepartmentRepository.delete(
            db,
            department,
        )

        return True