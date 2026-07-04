from uuid import UUID
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.pagination import PaginatedResponse
from app.auth.dependencies import get_current_user, require_roles
from app.database.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentProfile,
    StudentResponse,
    StudentUpdate,
)
from app.services.student_service import StudentService

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get(
    "/me",
    response_model=StudentProfile,
)
def get_my_profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    student = StudentService.get_profile(
        db=db,
        user_id=current_user.id,
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found",
        )

    return student


@router.post(
    "",
    response_model=StudentResponse,
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    return StudentService.create(
        db=db,
        student=student,
    )

@router.get(
    "",
    response_model=PaginatedResponse[StudentResponse],
)
def get_students(
    page: int = 1,
    size: int = 10,
    search: Optional[str] = None,
    department_id: Optional[UUID] = None,
    program_id: Optional[UUID] = None,
    semester: Optional[int] = None,
    is_active: Optional[bool] = None,
    sort: str = "full_name",
    db: Session = Depends(get_db),
):
    return StudentService.get_all(
        db=db,
        page=page,
        size=size,
        search=search,
        department_id=department_id,
        program_id=program_id,
        semester=semester,
        is_active=is_active,
        sort=sort,
    )

@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
def get_student(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    student = StudentService.get_by_id(
        db,
        student_id,
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student

@router.put(
    "/{student_id}",
    response_model=StudentResponse,
)
def update_student(
    student_id: UUID,
    request: StudentUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    student = StudentService.update(
        db,
        student_id,
        request,
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student

@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    deleted = StudentService.delete(
        db,
        student_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return None