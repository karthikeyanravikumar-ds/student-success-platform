class StudentTransformer:
    """
    Transforms raw student CSV data into
    Student Success Platform format.
    """

    @staticmethod
    def get_semester(year: str) -> int:

        year = year.strip().upper()

        mapping = {
            "FY": 1,
            "SY": 3,
            "TY": 5,
        }

        return mapping.get(year, 1)

    @staticmethod
    def transform(row: dict) -> dict:

        return {
            "roll_no": row["ROLL NO"].strip(),

            "full_name": row["Name"].strip(),

            "email": row["Email"].strip().lower(),

            "phone": row["Phone"]
            .split(".")[0]
            .strip(),

            "semester": StudentTransformer.get_semester(
                row["Year"]
            ),

            "admission_year": 2024,

            "graduation_year": 2027,

            "division": "A",
        }

    @staticmethod
    def transform_many(
        rows: list[dict],
    ) -> list[dict]:

        return [
            StudentTransformer.transform(row)
            for row in rows
        ]