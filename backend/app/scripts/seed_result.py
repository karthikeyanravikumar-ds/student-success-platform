import csv
from pathlib import Path

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.result import Result, ResultStatus
from app.models.student import Student

CSV_FILE = Path("app/seed_data/semester_results.csv")


def seed_results():
    db: Session = SessionLocal()

    try:

        created = 0
        skipped = 0

        with CSV_FILE.open(
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as csvfile:

            reader = csv.DictReader(csvfile)

            reader.fieldnames = [
                field.strip()
                for field in reader.fieldnames
            ]

            for row in reader:

                row = {
                    key.strip(): value.strip()
                    for key, value in row.items()
                }

                roll_no = row["ROLL NO"]
                semester = int(row["SEMESTER"])
                cgpa = float(row["CGPA"])

                student = (
                    db.query(Student)
                    .filter(Student.roll_no == roll_no)
                    .first()
                )

                if student is None:
                    print(f"⚠️ Student not found: {roll_no}")
                    continue

                existing = (
                    db.query(Result)
                    .filter(
                        Result.student_id == student.id,
                        Result.semester == semester,
                    )
                    .first()
                )

                if existing:
                    skipped += 1
                    continue

                total_max_marks = 1000.0
                total_marks = round((cgpa / 10) * total_max_marks, 2)
                percentage = round(
                    (total_marks / total_max_marks) * 100,
                    2,
                )

                result = Result(
                    student_id=student.id,
                    semester=semester,
                    total_marks=total_marks,
                    total_max_marks=total_max_marks,
                    percentage=percentage,
                    sgpa=cgpa,
                    cgpa=cgpa,
                    result_status=ResultStatus.PASS,
                    rank=None,
                    remarks=None,
                )

                db.add(result)
                created += 1

        db.commit()

        print("\n========== Seed Summary ==========")
        print(f"✅ Results Created : {created}")
        print(f"⏭️ Results Skipped : {skipped}")
        print("==================================")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_results()