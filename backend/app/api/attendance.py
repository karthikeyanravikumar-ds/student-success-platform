from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceResponse,
    AttendanceUpdate,
)
from app.services.attendance_service import AttendanceService

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"],
)


@router.get(
    "",
    response_model=list[AttendanceResponse],
)
def get_attendance(
    db: Session = Depends(get_db),
):
    return AttendanceService.get_all(db)


@router.get(
    "/{attendance_id}",
    response_model=AttendanceResponse,
)
def get_attendance_by_id(
    attendance_id: UUID,
    db: Session = Depends(get_db),
):
    attendance = AttendanceService.get_by_id(
        db,
        attendance_id,
    )

    if attendance is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return attendance


@router.post(
    "",
    response_model=AttendanceResponse,
)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator", "Faculty")),
):
    return AttendanceService.create(
        db,
        attendance,
    )


@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponse,
)
def update_attendance(
    attendance_id: UUID,
    request: AttendanceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator", "Faculty")),
):
    attendance = AttendanceService.update(
        db,
        attendance_id,
        request,
    )

    if attendance is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return attendance


@router.delete(
    "/{attendance_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_attendance(
    attendance_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    deleted = AttendanceService.delete(
        db,
        attendance_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return None


@router.get(
    "/student/{student_id}",
    response_model=list[AttendanceResponse],
)
def get_student_attendance(
    student_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_by_student(
        db,
        student_id,
    )


@router.get(
    "/subject/{subject_id}",
    response_model=list[AttendanceResponse],
)
def get_subject_attendance(
    subject_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_by_subject(
        db,
        subject_id,
    )


@router.get(
    "/faculty/{faculty_id}",
    response_model=list[AttendanceResponse],
)
def get_faculty_attendance(
    faculty_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_by_faculty(
        db,
        faculty_id,
    )


@router.get(
    "/date/{attendance_date}",
    response_model=list[AttendanceResponse],
)
def get_date_attendance(
    attendance_date: date,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_by_date(
        db,
        attendance_date,
    )