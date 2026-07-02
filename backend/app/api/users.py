from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user),
):
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "role": current_user.role.role_name,
        "active": current_user.is_active,
    }