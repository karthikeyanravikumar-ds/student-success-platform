from uuid import UUID

from sqlalchemy.orm import Session

from app.models.program import Program


class ProgramRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        program = Program(**data)

        db.add(program)
        db.commit()
        db.refresh(program)

        return program

    @staticmethod
    def get_all(
        db: Session,
    ):
        return db.query(Program).all()

    @staticmethod
    def get_by_id(
        db: Session,
        program_id: UUID,
    ):
        return (
            db.query(Program)
            .filter(Program.id == program_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        program: Program,
    ):
        db.commit()
        db.refresh(program)
        return program

    @staticmethod
    def delete(
        db: Session,
        program: Program,
    ):
        db.delete(program)
        db.commit()