from app.repositories.program_repository import ProgramRepository
from app.schemas.program import (
    ProgramCreate,
    ProgramUpdate,
)


class ProgramService:

    @staticmethod
    def create(
        db,
        program: ProgramCreate,
    ):
        return ProgramRepository.create(
            db,
            program.model_dump(),
        )

    @staticmethod
    def get_all(
        db,
    ):
        return ProgramRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        program_id,
    ):
        return ProgramRepository.get_by_id(
            db,
            program_id,
        )

    @staticmethod
    def update(
        db,
        program_id,
        request: ProgramUpdate,
    ):
        program = ProgramRepository.get_by_id(
            db,
            program_id,
        )

        if program is None:
            return None

        data = request.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(program, key, value)

        return ProgramRepository.update(
            db,
            program,
        )

    @staticmethod
    def delete(
        db,
        program_id,
    ):
        program = ProgramRepository.get_by_id(
            db,
            program_id,
        )

        if program is None:
            return False

        ProgramRepository.delete(
            db,
            program,
        )

        return True