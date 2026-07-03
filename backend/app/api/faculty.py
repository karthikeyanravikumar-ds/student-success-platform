from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.faculty import (
    FacultyCreate,
    FacultyResponse,
    FacultyUpdate,
)
from app.services.faculty_service import FacultyService

router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"],
)


@router.get(
    "",
    response_model=list[FacultyResponse],
)
def get_faculty(
    db: Session = Depends(get_db),
):
    return FacultyService.get_all(db)


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