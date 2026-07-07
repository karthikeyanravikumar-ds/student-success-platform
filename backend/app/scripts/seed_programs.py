from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.department import Department
from app.models.program import Program


PROGRAMS = [
    {
        "department_code": "315",
        "program_name": "B.Sc Data Science",
        "program_code": "BSDS",
        "duration_years": 3,
    },
    {
        "department_code": "205",
        "program_name": "B.Sc Information Technology",
        "program_code": "BSIT",
        "duration_years": 3,
    },
    {
        "department_code": "206",
        "program_name": "B.Sc Computer Science (AI & ML)",
        "program_code": "BSAIML",
        "duration_years": 3,
    },
    {
        "department_code": "204",
        "program_name": "B.Sc Computer Science (Software Engineering)",
        "program_code": "BSSE",
        "duration_years": 3,
    },
    {
        "department_code": "203",
        "program_name": "B.Sc Data Science & Artificial Intelligence",
        "program_code": "BSDSAI",
        "duration_years": 3,
    },
]


def seed_programs():
    db: Session = SessionLocal()

    try:

        for program in PROGRAMS:

            department = (
                db.query(Department)
                .filter(
                    Department.department_code == program["department_code"]
                )
                .first()
            )

            if department is None:
                print(
                    f"❌ Department {program['department_code']} not found."
                )
                continue

            exists = (
                db.query(Program)
                .filter(
                    Program.program_code == program["program_code"]
                )
                .first()
            )

            if exists:
                continue

            db.add(
                Program(
                    department_id=department.id,
                    program_name=program["program_name"],
                    program_code=program["program_code"],
                    duration_years=program["duration_years"],
                    is_active=True,
                )
            )

        db.commit()

        print("✅ Programs seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_programs()