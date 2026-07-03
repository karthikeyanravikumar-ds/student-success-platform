from uuid import UUID

from pydantic import BaseModel, EmailStr


class CompanyBase(BaseModel):
    name: str
    website: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    industry: str | None = None
    location: str | None = None
    description: str | None = None
    is_active: bool = True


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: str | None = None
    website: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    industry: str | None = None
    location: str | None = None
    description: str | None = None
    is_active: bool | None = None


class CompanyResponse(CompanyBase):
    id: UUID

    class Config:
        from_attributes = True