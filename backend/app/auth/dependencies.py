from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.jwt import verify_access_token
from app.auth.oauth2 import oauth2_scheme
from app.database.database import get_db
from app.repositories.user_repository import UserRepository

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    print("=" * 50)
    print("TOKEN:", token)

    payload = verify_access_token(token)
    print("PAYLOAD:", payload)

    email = payload.get("sub")
    print("EMAIL:", email)

    user = UserRepository.get_by_email(db, email)
    print("USER:", user)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user

    payload = verify_access_token(token)

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    user = UserRepository.get_by_email(
        db,
        email,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user

def require_roles(*allowed_roles):
    def checker(current_user=Depends(get_current_user)):
        if current_user.role.role_name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )

        return current_user

    return checker