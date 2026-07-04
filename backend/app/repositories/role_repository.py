from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Role)
            .order_by(Role.role_name)
            .all()
        )