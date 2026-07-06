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
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

from app.services.company_logo_service import CompanyLogoService

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

@router.post(
    "/{company_id}/logo",
    summary="Upload Company Logo",
)
def upload_company_logo(
    company_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Placement Officer",
            "Administrator",
        )
    ),
):
    company = CompanyLogoService.upload(
        db,
        company_id,
        file,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return {
        "message": "Company logo uploaded successfully",
        "company": company,
    }

@router.get(
    "/{company_id}/logo",
    summary="View Company Logo",
)
def view_company_logo(
    company_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Student",
            "Faculty",
            "Placement Officer",
            "Administrator",
        )
    ),
):
    path = CompanyLogoService.get(
        db,
        company_id,
    )

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    if path is False:
        raise HTTPException(
            status_code=404,
            detail="Logo not found",
        )

    return FileResponse(
        path=str(path),
        headers={
            "Content-Disposition": "inline",
        },
    )

@router.put(
    "/{company_id}/logo",
    summary="Replace Company Logo",
)
def replace_company_logo(
    company_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Placement Officer",
            "Administrator",
        )
    ),
):
    company = CompanyLogoService.replace(
        db,
        company_id,
        file,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return {
        "message": "Company logo replaced successfully",
        "company": company,
    }

@router.delete(
    "/{company_id}/logo",
    summary="Delete Company Logo",
)
def delete_company_logo(
    company_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Placement Officer",
            "Administrator",
        )
    ),
):
    result = CompanyLogoService.delete(
        db,
        company_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Logo not found",
        )

    return {
        "message": "Company logo deleted successfully",
    }