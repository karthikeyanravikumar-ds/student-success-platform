from pathlib import Path

from sqlalchemy.orm import Session

from app.etl.pipeline import StudentImportPipeline


class StudentImporter:

    @staticmethod
    def run(
        db: Session,
        role,
        department,
        program,
    ):

        csv_file = Path(
            "app/seed_data/students_dataset_draft_1.csv"
        )

        return StudentImportPipeline.run(
            db=db,
            csv_file=csv_file,
            role=role,
            department=department,
            program=program,
        )