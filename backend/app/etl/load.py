from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.models.student import Student
from app.models.user import User

DEFAULT_PASSWORD = "Student@123"


class StudentLoader:
    """
    Loads validated student data into the database.
    """

    @staticmethod
    def load(
        db: Session,
        students: list[dict],
        role,
        department,
        program,
    ):

        created = 0
        skipped = 0

        for data in students:

            user = (
                db.query(User)
                .filter(
                    User.email == data["email"]
                )
                .first()
            )

            if user is None:

                user = User(
                    role_id=role.id,
                    email=data["email"],
                    password_hash=hash_password(
                        DEFAULT_PASSWORD
                    ),
                    is_active=True,
                )

                db.add(user)
                db.flush()

            student = (
                db.query(Student)
                .filter(
                    Student.roll_no == data["roll_no"]
                )
                .first()
            )

            if student:
                skipped += 1
                continue

            student = Student(
                user_id=user.id,
                department_id=department.id,
                program_id=program.id,
                roll_no=data["roll_no"],
                full_name=data["full_name"],
                gender=None,
                dob=None,
                phone=data["phone"],
                division=data["division"],
                admission_year=data["admission_year"],
                graduation_year=data["graduation_year"],
                current_semester=data["semester"],
                is_active=True,
            )

            db.add(student)
            created += 1

        db.commit()

        return {
            "created": created,
            "skipped": skipped,
        }