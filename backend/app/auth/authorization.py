from fastapi import HTTPException, status

from app.models.student import Student


class Authorization:

    @staticmethod
    def is_admin(current_user) -> bool:
        return (
            current_user.role.role_name
            == "Administrator"
        )

    @staticmethod
    def is_student(current_user) -> bool:
        return (
            current_user.role.role_name
            == "Student"
        )

    @staticmethod
    def is_faculty(current_user) -> bool:
        return (
            current_user.role.role_name
            == "Faculty"
        )

    @staticmethod
    def is_placement_officer(current_user) -> bool:
        return (
            current_user.role.role_name
            == "Placement Officer"
        )

    @staticmethod
    def check_student_owner(
        student: Student,
        current_user,
    ):

        if Authorization.is_admin(current_user):
            return

        if (
            Authorization.is_student(current_user)
            and student.user_id == current_user.id
        ):
            return

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )

    @staticmethod
    def check_admin(current_user):

        if Authorization.is_admin(current_user):
            return

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required",
        )