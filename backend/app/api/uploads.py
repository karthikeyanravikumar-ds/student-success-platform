from fastapi import APIRouter, File, UploadFile

from app.uploads.upload_service import UploadService
from app.uploads.validators import (
    validate_image,
    validate_pdf,
)

router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"],
)



@router.post("/profile-photo")
def upload_profile_photo_path(
    file: UploadFile = File(...),
):
    validate_image(file)

    filepath = UploadService.save_file(
        file=file,
        folder="profile_photo_paths",
    )

    return {
        "message": "Profile photo uploaded successfully",
        "path": filepath,
    }


@router.post("/certificate")
def upload_certificate(
    file: UploadFile = File(...),
):
    validate_pdf(file)

    filepath = UploadService.save_file(
        file=file,
        folder="certificates",
    )

    return {
        "message": "Certificate uploaded successfully",
        "path": filepath,
    }


@router.post("/company-logo")
def upload_company_logo(
    file: UploadFile = File(...),
):
    validate_image(file)

    filepath = UploadService.save_file(
        file=file,
        folder="company_logos",
    )

    return {
        "message": "Company logo uploaded successfully",
        "path": filepath,
    }