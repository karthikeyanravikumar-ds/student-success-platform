from uuid import UUID

from sqlalchemy.orm import Session

from app.models.placement_drive import PlacementDrive


class PlacementDriveRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict,
    ):
        drive = PlacementDrive(**data)

        db.add(drive)
        db.commit()
        db.refresh(drive)

        return drive

    @staticmethod
    def get_all(db: Session):
        return db.query(PlacementDrive).all()

    @staticmethod
    def get_by_id(
        db: Session,
        drive_id: UUID,
    ):
        return (
            db.query(PlacementDrive)
            .filter(PlacementDrive.id == drive_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        drive: PlacementDrive,
    ):
        db.commit()
        db.refresh(drive)
        return drive

    @staticmethod
    def delete(
        db: Session,
        drive: PlacementDrive,
    ):
        db.delete(drive)
        db.commit()