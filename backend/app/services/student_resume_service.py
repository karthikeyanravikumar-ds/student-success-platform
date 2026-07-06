
from fastapi import UploadFile

from app.repositories.student_repository import StudentRepository
from app.services.document_service import DocumentService
from app.uploads.validators import validate_pdf


class StudentResumeService:

    @staticmethod
    def upload(db, student_id, file: UploadFile):
        student = StudentRepository.get_by_id(db, student_id)

        if student is None:
            return None

        validate_pdf(file)

        resume_path = DocumentService.save_document(
            entity="students",
            entity_id=str(student.id),
            document_name="resume",
            file=file,
        )

        return StudentRepository.update_resume_path(
            db,
            student,
            resume_path,
        )
    
    @staticmethod
    def get(db, student_id):
        student = StudentRepository.get_by_id(db, student_id)

        if student is None:
            return None

        if not student.resume_path:
            return False

        return DocumentService.get_document(
            student.resume_path,
        )

    @staticmethod
    def download(db, student_id):
        return StudentResumeService.get(
            db,
            student_id,
        )

    @staticmethod
    def replace(
        db,
        student_id,
        file: UploadFile,
    ):
        return StudentResumeService.upload(
            db,
            student_id,
            file,
        )

    @staticmethod
    def delete(db, student_id):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        if not student.resume_path:
            return False

        DocumentService.delete_document(
            student.resume_path,
        )

        student.resume_path = None

        return StudentRepository.update(
            db,
            student,
        )