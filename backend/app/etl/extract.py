import csv
from pathlib import Path


class CSVExtractor:
    """
    Extracts data from CSV files.

    Supports future extension for:
    - Excel
    - Database
    - APIs
    """

    @staticmethod
    def extract(file_path: str | Path) -> list[dict]:

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"{file_path} does not exist."
            )

        with file_path.open(
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as csvfile:

            reader = csv.DictReader(csvfile)

            if reader.fieldnames is None:
                raise ValueError(
                    "CSV file has no headers."
                )

            reader.fieldnames = [
                field.strip()
                for field in reader.fieldnames
            ]

            data = []

            for row in reader:

                cleaned_row = {
                    key.strip(): (
                        value.strip()
                        if value
                        else ""
                    )
                    for key, value in row.items()
                }

                data.append(cleaned_row)

        return data