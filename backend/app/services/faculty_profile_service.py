from fastapi import UploadFile

from app.repositories.faculty_repository import FacultyRepository
from app.services.document_service import DocumentService
from app.uploads.validators import validate_image


class FacultyProfileService:

    @staticmethod
    def upload(
        db,
        faculty_id,
        file: UploadFile,
    ):
        faculty = FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

        if faculty is None:
            return None

        validate_image(file)

        profile_photo_path = DocumentService.save_document(
            entity="faculty",
            entity_id=str(faculty.id),
            document_name="profile",
            file=file,
        )

        return FacultyRepository.update_profile_photo_path(
            db,
            faculty,
            profile_photo_path,
        )

    @staticmethod
    def get(
        db,
        faculty_id,
    ):
        faculty = FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

        if faculty is None:
            return None

        if not faculty.profile_photo_path:
            return False

        return DocumentService.get_document(
            faculty.profile_photo_path,
        )

    @staticmethod
    def replace(
        db,
        faculty_id,
        file: UploadFile,
    ):
        return FacultyProfileService.upload(
            db,
            faculty_id,
            file,
        )

    @staticmethod
    def delete(
        db,
        faculty_id,
    ):
        faculty = FacultyRepository.get_by_id(
            db,
            faculty_id,
        )

        if faculty is None:
            return None

        if not faculty.profile_photo_path:
            return False

        DocumentService.delete_document(
            faculty.profile_photo_path,
        )

        faculty.profile_photo_path = None

        return FacultyRepository.update(
            db,
            faculty,
        )