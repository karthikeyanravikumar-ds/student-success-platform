from uuid import UUID
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.pagination import PaginatedResponse
from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.faculty import (
    FacultyCreate,
    FacultyResponse,
    FacultyUpdate,
)
from app.services.faculty_service import FacultyService
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

from app.services.faculty_profile_service import FacultyProfileService

router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"],
)


@router.get(
    "",
    response_model=PaginatedResponse[FacultyResponse],
)
def get_faculty(
    page: int = 1,
    size: int = 10,
    search: Optional[str] = None,
    department_id: Optional[UUID] = None,
    is_active: Optional[bool] = None,
    sort: str = "full_name",
    db: Session = Depends(get_db),
):
    return FacultyService.get_all(
        db=db,
        page=page,
        size=size,
        search=search,
        department_id=department_id,
        is_active=is_active,
        sort=sort,
    )


@router.get(
    "/{faculty_id}",
    response_model=FacultyResponse,
)
def get_faculty_by_id(
    faculty_id: UUID,
    db: Session = Depends(get_db),
):
    faculty = FacultyService.get_by_id(
        db,
        faculty_id,
    )

    if faculty is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found",
        )

    return faculty


@router.post(
    "",
    response_model=FacultyResponse,
)
def create_faculty(
    faculty: FacultyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    return FacultyService.create(
        db,
        faculty,
    )


@router.put(
    "/{faculty_id}",
    response_model=FacultyResponse,
)
def update_faculty(
    faculty_id: UUID,
    request: FacultyUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    faculty = FacultyService.update(
        db,
        faculty_id,
        request,
    )

    if faculty is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found",
        )

    return faculty


@router.delete(
    "/{faculty_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_faculty(
    faculty_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    deleted = FacultyService.delete(
        db,
        faculty_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found",
        )

    return None
@router.post(
    "/{faculty_id}/profile-photo",
    summary="Upload Faculty Profile Photo",
)
def upload_faculty_profile_photo(
    faculty_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    faculty = FacultyProfileService.upload(
        db,
        faculty_id,
        file,
    )

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found",
        )

    return {
        "message": "Profile photo uploaded successfully",
        "faculty": faculty,
    }

@router.get(
    "/{faculty_id}/profile-photo",
    summary="View Faculty Profile Photo",
)
def view_faculty_profile_photo(
    faculty_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Faculty",
            "Administrator",
        )
    ),
):
    path = FacultyProfileService.get(
        db,
        faculty_id,
    )

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found",
        )

    if path is False:
        raise HTTPException(
            status_code=404,
            detail="Profile photo not found",
        )

    return FileResponse(
        path=str(path),
        headers={
            "Content-Disposition": "inline",
        },
    )

@router.put(
    "/{faculty_id}/profile-photo",
    summary="Replace Faculty Profile Photo",
)
def replace_faculty_profile_photo(
    faculty_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    faculty = FacultyProfileService.replace(
        db,
        faculty_id,
        file,
    )

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found",
        )

    return {
        "message": "Profile photo replaced successfully",
        "faculty": faculty,
    }

@router.delete(
    "/{faculty_id}/profile-photo",
    summary="Delete Faculty Profile Photo",
)
def delete_faculty_profile_photo(
    faculty_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    result = FacultyProfileService.delete(
        db,
        faculty_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found",
        )

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Profile photo not found",
        )

    return {
        "message": "Profile photo deleted successfully",
    }