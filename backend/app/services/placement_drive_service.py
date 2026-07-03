from app.repositories.company_repository import CompanyRepository
from app.repositories.placement_drive_repository import (
    PlacementDriveRepository,
)
from app.schemas.placement_drive import (
    PlacementDriveCreate,
    PlacementDriveUpdate,
)


class PlacementDriveService:

    @staticmethod
    def create(
        db,
        request: PlacementDriveCreate,
    ):
        company = CompanyRepository.get_by_id(
            db,
            request.company_id,
        )

        if company is None:
            return None

        return PlacementDriveRepository.create(
            db,
            request.model_dump(),
        )

    @staticmethod
    def get_all(db):
        return PlacementDriveRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        drive_id,
    ):
        return PlacementDriveRepository.get_by_id(
            db,
            drive_id,
        )

    @staticmethod
    def update(
        db,
        drive_id,
        request: PlacementDriveUpdate,
    ):
        drive = PlacementDriveRepository.get_by_id(
            db,
            drive_id,
        )

        if drive is None:
            return None

        data = request.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(
                drive,
                key,
                value,
            )

        return PlacementDriveRepository.update(
            db,
            drive,
        )

    @staticmethod
    def delete(
        db,
        drive_id,
    ):
        drive = PlacementDriveRepository.get_by_id(
            db,
            drive_id,
        )

        if drive is None:
            return False

        PlacementDriveRepository.delete(
            db,
            drive,
        )

        return True