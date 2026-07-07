from pathlib import Path

from sqlalchemy.orm import Session

from app.etl.extract import CSVExtractor
from app.etl.load import StudentLoader
from app.etl.transform import StudentTransformer
from app.etl.validators import StudentValidator


class StudentImportPipeline:
    """
    End-to-end ETL pipeline for
    importing students.
    """

    @staticmethod
    def run(
        db: Session,
        csv_file: str | Path,
        role,
        department,
        program,
    ):

        # Extract
        raw_students = CSVExtractor.extract(
            csv_file
        )

        # Transform
        transformed_students = (
            StudentTransformer.transform_many(
                raw_students
            )
        )

        # Validate
        (
            valid_students,
            rejected_students,
        ) = StudentValidator.validate_many(
            transformed_students
        )

        # Load
        summary = StudentLoader.load(
            db=db,
            students=valid_students,
            role=role,
            department=department,
            program=program,
        )

        summary["rejected"] = len(
            rejected_students
        )

        summary["errors"] = (
            rejected_students
        )

        return summary