from sqlalchemy.orm import Session

from app.auth.hashing import verify_password
from app.auth.jwt import create_access_token
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = UserRepository.get_by_email(
            db,
            email,
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role.role_name,
            }
        )

        return token