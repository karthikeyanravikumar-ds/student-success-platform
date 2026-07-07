import re


class StudentValidator:
    """
    Validates transformed student data
    before loading into the database.
    """

    EMAIL_PATTERN = re.compile(
        r"^[a-zA-Z0-9._%+-]+@vsit\.edu\.in$"
    )

    PHONE_PATTERN = re.compile(
        r"^\d{10}$"
    )

    @staticmethod
    def validate(
        student: dict,
    ) -> tuple[bool, list[str]]:

        errors = []

        if not student["roll_no"]:
            errors.append("Roll number is required.")

        if not student["full_name"]:
            errors.append("Student name is required.")

        if not StudentValidator.EMAIL_PATTERN.match(
            student["email"]
        ):
            errors.append(
                "Invalid VSIT email address."
            )

        if not StudentValidator.PHONE_PATTERN.match(
            student["phone"]
        ):
            errors.append(
                "Phone number must contain exactly 10 digits."
            )

        if student["semester"] not in [
            1,
            3,
            5,
        ]:
            errors.append(
                "Invalid semester."
            )

        return (
            len(errors) == 0,
            errors,
        )

    @staticmethod
    def validate_many(
        students: list[dict],
    ):

        valid_students = []

        rejected_students = []

        for student in students:

            is_valid, errors = (
                StudentValidator.validate(
                    student
                )
            )

            if is_valid:
                valid_students.append(
                    student
                )
            else:
                rejected_students.append(
                    {
                        "student": student,
                        "errors": errors,
                    }
                )

        return (
            valid_students,
            rejected_students,
        )