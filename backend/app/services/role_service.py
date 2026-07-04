from sqlalchemy.orm import Session

from app.repositories.role_repository import RoleRepository


class RoleService:

    @staticmethod
    def get_all(db: Session):
        return RoleRepository.get_all(db)