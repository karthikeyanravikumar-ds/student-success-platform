from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.auth.dependencies import require_roles
from app.database.database import get_db
from app.schemas.student_certificate import (
    StudentCertificateCreate,
    StudentCertificateResponse,
    CertificateVerificationRequest,
)
from app.services.student_certificate_service import StudentCertificateService

router = APIRouter(
    prefix="/students",
    tags=["Student Certificates"],
)

@router.post(
    "/{student_id}/certificates",
    response_model=StudentCertificateResponse,
)
def upload_certificate(
    student_id: UUID,
    certificate_name: str = Form(...),
    certificate_type: str = Form(...),
    issuer: str = Form(None),
    issue_date: str = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Student", "Administrator")),
):
    request = StudentCertificateCreate(
        certificate_name=certificate_name,
        certificate_type=certificate_type,
        issuer=issuer,
        issue_date=issue_date,
    )

    certificate = StudentCertificateService.upload(
        db,
        student_id,
        request,
        file,
    )

    if certificate is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return certificate

@router.get(
    "/{student_id}/certificates",
    response_model=list[StudentCertificateResponse],
)
def get_certificates(
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
    return StudentCertificateService.get_all(
        db,
        student_id,
    )

@router.get(
    "/certificates/{certificate_id}",
)
def view_certificate(
    certificate_id: UUID,
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
    path = StudentCertificateService.get(
        db,
        certificate_id,
    )

    if path is None:
        raise HTTPException(404, "Certificate not found")

    if path is False:
        raise HTTPException(404, "File not found")

    return FileResponse(
        str(path),
        filename="certificate.pdf",
    )

@router.delete(
    "/certificates/{certificate_id}",
)
def delete_certificate(
    certificate_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Student", "Administrator")),
):
    result = StudentCertificateService.delete(
        db,
        certificate_id,
    )

    if result is None:
        raise HTTPException(404, "Certificate not found")

    return {
        "message": "Certificate deleted successfully",
    }

@router.put(
    "/certificates/{certificate_id}/verify",
    response_model=StudentCertificateResponse,
)
def verify_certificate(
    certificate_id: UUID,
    request: CertificateVerificationRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Faculty")),
):
    certificate = StudentCertificateService.verify(
        db,
        certificate_id,
        current_user.id,
        request.verification_remarks,
    )

    if certificate is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found",
        )

    return certificate

@router.put(
    "/certificates/{certificate_id}/reject",
    response_model=StudentCertificateResponse,
)
def reject_certificate(
    certificate_id: UUID,
    request: CertificateVerificationRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Faculty")),
):
    certificate = StudentCertificateService.reject(
        db,
        certificate_id,
        current_user.id,
        request.verification_remarks,
    )

    if certificate is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found",
        )

    return certificate

@router.get(
    "/certificates/pending",
    response_model=list[StudentCertificateResponse],
    summary="Pending Certificates",
)
def get_pending_certificates(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Faculty",
            "Administrator",
        )
    ),
):
    return StudentCertificateService.get_pending(db)

@router.get(
    "/certificates/verified",
    response_model=list[StudentCertificateResponse],
    summary="Verified Certificates",
)
def get_verified_certificates(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Faculty",
            "Administrator",
        )
    ),
):
    return StudentCertificateService.get_verified(db)

@router.get(
    "/certificates/rejected",
    response_model=list[StudentCertificateResponse],
    summary="Rejected Certificates",
)
def get_rejected_certificates(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Faculty",
            "Administrator",
        )
    ),
):
    return StudentCertificateService.get_rejected(db)

@router.get(
    "/certificates/{certificate_id}/download",
    summary="Download Certificate",
)
def download_certificate(
    certificate_id: UUID,
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
    path = StudentCertificateService.get(
        db,
        certificate_id,
    )

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found",
        )

    if path is False:
        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    return FileResponse(
        path=str(path),
        media_type="application/pdf",
        filename="certificate.pdf",
        headers={
            "Content-Disposition": 'attachment; filename="certificate.pdf"',
        },
    )