from uuid import UUID

from pydantic import BaseModel


class ProgramCreate(BaseModel):
    department_id: UUID
    program_name: str
    program_code: str
    duration_years: int


class ProgramUpdate(BaseModel):
    program_name: str | None = None
    program_code: str | None = None
    duration_years: int | None = None
    is_active: bool | None = None


class ProgramResponse(BaseModel):
    id: UUID
    department_id: UUID
    program_name: str
    program_code: str
    duration_years: int
    is_active: bool

    class Config:
        from_attributes = True