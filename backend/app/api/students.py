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
from app.services.student_resume_service import StudentResumeService
from app.services.student_profile_service import StudentProfileService



from fastapi import File, UploadFile
from fastapi.responses import FileResponse

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

@router.post(
    "/{student_id}/resume",
    summary="Upload Student Resume",
)
def upload_student_resume(
    student_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    student = StudentResumeService.upload(
        db,
        student_id,
        file,
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return {
        "message": "Resume uploaded successfully",
        "student": student,
    }

@router.get(
    "/{student_id}/resume",
    summary="View Student Resume",
)
def view_student_resume(
    student_id: UUID,
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
    path = StudentResumeService.get(
        db,
        student_id,
    )

    if path is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    if path is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found",
        )

    return FileResponse(
        path=path,
        media_type="application/pdf",
        filename=f"{student_id}_resume.pdf",
        headers={
            "Content-Disposition": "inline"
        },
    )
@router.get(
    "/{student_id}/resume/download",
    summary="Download Student Resume",
)
def download_student_resume(
    student_id: UUID,
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
    path = StudentResumeService.download(
        db,
        student_id,
    )

    if path is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    if path is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found",
        )

    student = StudentService.get_by_id(
        db,
        student_id,
    )

    return FileResponse(
        path=path,
        media_type="application/pdf",
        filename=f"{student.roll_no}_Resume.pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{student.roll_no}_Resume.pdf"'
        },
    )
@router.put(
    "/{student_id}/resume",
    summary="Replace Student Resume",
)
def replace_student_resume(
    student_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    student = StudentResumeService.replace_resume(
        db,
        student_id,
        file,
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Resume replaced successfully",
        "student": student,
    }

@router.delete(
    "/{student_id}/resume",
    summary="Delete Student Resume",
)
def delete_student_resume(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Administrator",
        )
    ),
):
    result = StudentResumeService.delete_resume(
        db,
        student_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    return {
        "message": "Resume deleted successfully",
    }

@router.post(
    "/{student_id}/profile-photo",
    summary="Upload Student Profile Photo",
)
def upload_student_profile_photo(
    student_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    student = StudentProfileService.upload(
        db,
        student_id,
        file,
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Profile photo uploaded successfully",
        "student": student,
    }

@router.get(
    "/{student_id}/profile-photo",
    summary="View Student Profile Photo",
)
def view_student_profile_photo(
    student_id: UUID,
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
    path = StudentProfileService.get(
        db,
        student_id,
    )

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
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
    "/{student_id}/profile-photo",
    summary="Replace Student Profile Photo",
)
def replace_student_profile_photo(
    student_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    student = StudentProfileService.replace(
        db,
        student_id,
        file,
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Profile photo replaced successfully",
        "student": student,
    }

@router.delete(
    "/{student_id}/profile-photo",
    summary="Delete Student Profile Photo",
)
def delete_student_profile_photo(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Administrator")),
):
    result = StudentProfileService.delete(
        db,
        student_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Profile photo not found",
        )

    return {
        "message": "Profile photo deleted successfully",
    }