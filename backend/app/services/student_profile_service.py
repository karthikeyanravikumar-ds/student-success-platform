from fastapi import UploadFile

from app.repositories.student_repository import StudentRepository
from app.services.document_service import DocumentService
from app.uploads.validators import validate_image


class StudentProfileService:

    @staticmethod
    def upload(
        db,
        student_id,
        file: UploadFile,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        validate_image(file)

        profile_photo_path = DocumentService.save_document(
            entity="students",
            entity_id=str(student.id),
            document_name="profile",
            file=file,
        )

        return StudentRepository.update_profile_photo_path(
            db,
            student,
            profile_photo_path,
        )

    @staticmethod
    def get(
        db,
        student_id,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        if not student.profile_photo_path:
            return False

        return DocumentService.get_document(
            student.profile_photo_path,
        )

    @staticmethod
    def replace(
        db,
        student_id,
        file: UploadFile,
    ):
        return StudentProfileService.upload(
            db,
            student_id,
            file,
        )

    @staticmethod
    def delete(
        db,
        student_id,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        if not student.profile_photo_path:
            return False

        DocumentService.delete_document(
            student.profile_photo_path,
        )

        student.profile_photo_path = None

        return StudentRepository.update(
            db,
            student,
        )