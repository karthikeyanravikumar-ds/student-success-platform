from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
)
from app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@router.post(
    "",
    response_model=CompanyResponse,
)
def create_company(
    request: CompanyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    return CompanyService.create(
        db,
        request,
    )


@router.get(
    "",
    response_model=list[CompanyResponse],
)
def get_companies(
    db: Session = Depends(get_db),
):
    return CompanyService.get_all(db)


@router.get(
    "/{company_id}",
    response_model=CompanyResponse,
)
def get_company(
    company_id: UUID,
    db: Session = Depends(get_db),
):
    company = CompanyService.get_by_id(
        db,
        company_id,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return company


@router.put(
    "/{company_id}",
    response_model=CompanyResponse,
)
def update_company(
    company_id: UUID,
    request: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    company = CompanyService.update(
        db,
        company_id,
        request,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return company


@router.delete(
    "/{company_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_company(
    company_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Administrator")
    ),
):
    deleted = CompanyService.delete(
        db,
        company_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return None