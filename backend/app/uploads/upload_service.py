import shutil
from pathlib import Path

from fastapi import UploadFile

from app.uploads.file_utils import generate_filename


class UploadService:

    @staticmethod
    def save_entity_file(
        entity: str,
        entity_id: str,
        file_type: str,
        file: UploadFile,
    ):

        filename = generate_filename(file.filename)

        upload_dir = (
            Path("uploads")
            / entity
            / entity_id
        )

        upload_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        filepath = upload_dir / f"{file_type}{Path(filename).suffix}"

        with filepath.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return str(filepath).replace("\\", "/")