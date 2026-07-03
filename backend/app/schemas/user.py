from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role_id: UUID


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    role_id: UUID | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role_id: UUID
    is_active: bool

    class Config:
        from_attributes = True