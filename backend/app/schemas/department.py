from uuid import UUID

from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    department_name: str
    department_code: str


class DepartmentUpdate(BaseModel):
    department_name: str | None = None
    department_code: str | None = None
    is_active: bool | None = None


class DepartmentResponse(BaseModel):
    id: UUID
    department_name: str
    department_code: str
    is_active: bool

    class Config:
        from_attributes = True