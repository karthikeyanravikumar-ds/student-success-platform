class StudentMapping:
    """
    Maps external CSV columns to
    internal Student Success Platform fields.
    """

    COLUMN_MAPPING = {
        "ROLL NO": "roll_no",
        "Name": "full_name",
        "Email": "email",
        "Phone": "phone",
        "Year": "year",
        "Course": "course",
        "Dept": "department",
    }

    @classmethod
    def get(cls):
        return cls.COLUMN_MAPPING