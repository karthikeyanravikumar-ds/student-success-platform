from app.auth.hashing import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def get_all(db):
        return UserRepository.get_all(db)

    @staticmethod
    def create(db, request):
        user = User(
            email=request.email,
            password_hash=hash_password(request.password),
            role_id=request.role_id,
        )

        return UserRepository.create(
            db,
            user,
        )

    @staticmethod
    def update(
        db,
        user_id,
        request,
    ):
        user = UserRepository.get_by_id(
            db,
            user_id,
        )

        if user is None:
            return None

        if request.email is not None:
            user.email = request.email

        if request.password is not None:
            user.password_hash = hash_password(
                request.password
            )

        if request.role_id is not None:
            user.role_id = request.role_id

        if request.is_active is not None:
            user.is_active = request.is_active

        return UserRepository.update(
            db,
            user,
        )

    @staticmethod
    def delete(
        db,
        user_id,
    ):
        user = UserRepository.get_by_id(
            db,
            user_id,
        )

        if user is None:
            return False

        UserRepository.delete(
            db,
            user,
        )

        return True