from fastapi import HTTPException, UploadFile, status

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
}

ALLOWED_PDF_TYPES = {
    "application/pdf",
}


def validate_pdf(file: UploadFile):

    if file.content_type not in ALLOWED_PDF_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed.",
        )


def validate_image(file: UploadFile):

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPG and PNG images are allowed.",
        )