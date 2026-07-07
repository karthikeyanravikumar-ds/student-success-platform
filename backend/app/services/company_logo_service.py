from fastapi import UploadFile

from app.repositories.company_repository import CompanyRepository
from app.services.document_service import DocumentService
from app.uploads.validators import validate_image


class CompanyLogoService:

    @staticmethod
    def upload(
        db,
        company_id,
        file: UploadFile,
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id,
        )

        if company is None:
            return None

        validate_image(file)

        logo_path = DocumentService.save_document(
            entity="companies",
            entity_id=str(company.id),
            document_name="logo",
            file=file,
        )

        return CompanyRepository.update_logo_path(
            db,
            company,
            logo_path,
        )

    @staticmethod
    def get(
        db,
        company_id,
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id,
        )

        if company is None:
            return None

        if not company.logo_path:
            return False

        return DocumentService.get_document(
            company.logo_path,
        )

    @staticmethod
    def replace(
        db,
        company_id,
        file: UploadFile,
    ):
        return CompanyLogoService.upload(
            db,
            company_id,
            file,
        )

    @staticmethod
    def delete(
        db,
        company_id,
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id,
        )

        if company is None:
            return None

        if not company.logo_path:
            return False

        DocumentService.delete_document(
            company.logo_path,
        )

        company.logo_path = None

        return CompanyRepository.update(
            db,
            company,
        )