from pathlib import Path

from fastapi import UploadFile

from app.uploads.upload_service import UploadService


class DocumentService:

    @staticmethod
    def save_document(
        entity: str,
        entity_id: str,
        document_name: str,
        file: UploadFile,
    ):
        return UploadService.save_entity_file(
            entity=entity,
            entity_id=entity_id,
            file_type=document_name,
            file=file,
        )

    @staticmethod
    def get_document(
        file_path: str,
    ):
        if not file_path:
            return None

        path = Path(file_path)

        if not path.exists():
            return None

        return path

    @staticmethod
    def replace_document(
        entity: str,
        entity_id: str,
        document_name: str,
        file: UploadFile,
    ):
        return UploadService.save_entity_file(
            entity=entity,
            entity_id=entity_id,
            file_type=document_name,
            file=file,
        )

    @staticmethod
    def delete_document(
        file_path: str,
    ):
        if not file_path:
            return False

        path = Path(file_path)

        if path.exists():
            path.unlink()

        return True