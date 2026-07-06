from datetime import datetime
from pathlib import Path

from fastapi import UploadFile

from app.repositories.student_repository import StudentRepository
from app.repositories.student_certificate_repository import (
    StudentCertificateRepository,
)
from app.services.document_service import DocumentService
from app.uploads.validators import validate_pdf


class StudentCertificateService:

    @staticmethod
    def upload(
        db,
        student_id,
        request,
        file: UploadFile,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if student is None:
            return None

        validate_pdf(file)

        file_path = DocumentService.save_document(
            entity="students",
            entity_id=str(student.id),
            document_name=f"certificate_{datetime.now().timestamp()}",
            file=file,
        )

        data = request.model_dump()

        data["student_id"] = student.id
        data["file_path"] = file_path
        data["verification_status"] = "Pending"

        return StudentCertificateRepository.create(
            db,
            data,
        )

    @staticmethod
    def get_all(
        db,
        student_id,
    ):
        return StudentCertificateRepository.get_by_student(
            db,
            student_id,
        )

    @staticmethod
    def get(
        db,
        certificate_id,
    ):
        certificate = StudentCertificateRepository.get_by_id(
            db,
            certificate_id,
        )

        if certificate is None:
            return None

        path = DocumentService.get_document(
            certificate.file_path,
        )

        if path is None:
            return False

        return path

    @staticmethod
    def delete(
        db,
        certificate_id,
    ):
        certificate = StudentCertificateRepository.get_by_id(
            db,
            certificate_id,
        )

        if certificate is None:
            return None

        DocumentService.delete_document(
            certificate.file_path,
        )

        StudentCertificateRepository.delete(
            db,
            certificate,
        )

        return True

    @staticmethod
    def verify(
        db,
        certificate_id,
        faculty_user_id,
        remarks,
    ):
        certificate = StudentCertificateRepository.get_by_id(
            db,
            certificate_id,
        )

        if certificate is None:
            return None

        certificate.verification_status = "Verified"
        certificate.verified_by = faculty_user_id
        certificate.verified_at = datetime.now()
        certificate.verification_remarks = remarks

        return StudentCertificateRepository.update(
            db,
            certificate,
        )

    @staticmethod
    def reject(
        db,
        certificate_id,
        faculty_user_id,
        remarks,
    ):
        certificate = StudentCertificateRepository.get_by_id(
            db,
            certificate_id,
        )

        if certificate is None:
            return None

        certificate.verification_status = "Rejected"
        certificate.verified_by = faculty_user_id
        certificate.verified_at = datetime.now()
        certificate.verification_remarks = remarks

        return StudentCertificateRepository.update(
            db,
            certificate,
        )
    
    @staticmethod
    def get_pending(db):
        return StudentCertificateRepository.get_pending(db)

    @staticmethod
    def get_verified(db):
        return StudentCertificateRepository.get_verified(db)

    @staticmethod
    def get_rejected(db):
        return StudentCertificateRepository.get_rejected(db)