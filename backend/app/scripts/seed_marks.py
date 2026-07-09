import random

from app.database.database import SessionLocal
from app.models.mark import ExamType, Mark
from app.models.student import Student
from app.models.subject import Subject


def get_grade(mark):
    if mark >= 90:
        return "O"
    elif mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B+"
    elif mark >= 50:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"


def seed_marks():
    db = SessionLocal()

    try:

        students = (
            db.query(Student)
            .filter(Student.is_active == True)
            .all()
        )

        total_records = 0

        for student in students:

            subjects = (
                db.query(Subject)
                .filter(
                    Subject.program_id == student.program_id,
                    Subject.semester == student.current_semester,
                    Subject.is_active == True,
                )
                .all()
            )

            if not subjects:
                continue

            for subject in subjects:

                for exam in [
                    ExamType.IA1,
                    ExamType.IA2,
                    ExamType.MID,
                    ExamType.END,
                ]:

                    if exam in [
                        ExamType.IA1,
                        ExamType.IA2,
                    ]:
                        max_marks = 20

                    elif exam == ExamType.MID:
                        max_marks = 30

                    else:
                        max_marks = 100

                    obtained = round(
                        random.uniform(
                            max_marks * 0.45,
                            max_marks * 0.95,
                        ),
                        2,
                    )

                    mark = Mark(
                        student_id=student.id,
                        subject_id=subject.id,
                        faculty_id=subject.faculty_id,
                        semester=student.current_semester,
                        exam_type=exam,
                        max_marks=max_marks,
                        marks_obtained=obtained,
                        grade=get_grade(
                            (obtained / max_marks) * 100
                        ),
                        remarks=None,
                    )

                    db.add(mark)
                    total_records += 1

        db.commit()

        print(
            f"Successfully inserted {total_records} marks."
        )

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_marks()