from app.models.application import Application
from app.models.placement_drive import PlacementDrive
from app.models.application import ApplicationStatus
from app.reports.generators.pdf_generator import PDFGenerator


class CompanyReport(PDFGenerator):

    def generate(
        self,
        db,
        company,
    ):

        self.title(
            "VIDYALANKAR SCHOOL OF INFORMATION TECHNOLOGY"
        )

        self.heading(
            "Company Placement Report"
        )

        self.paragraph(
            f"<b>Company:</b> {company.name}"
        )

        self.paragraph(
            f"<b>Industry:</b> {company.industry}"
        )

        drives = (
            db.query(PlacementDrive)
            .filter(
                PlacementDrive.company_id == company.id
            )
            .all()
        )

        total_drives = len(drives)

        total_applications = (
            db.query(Application)
            .join(
                PlacementDrive,
                Application.drive_id == PlacementDrive.id,
            )
            .filter(
                PlacementDrive.company_id == company.id
            )
            .count()
        )

        selected_students = (
            db.query(Application)
            .join(
                PlacementDrive,
                Application.drive_id == PlacementDrive.id,
            )
            .filter(
                PlacementDrive.company_id == company.id,
                Application.status == ApplicationStatus.SELECTED,
            )
            .count()
        )

        rejected_students = (
            db.query(Application)
            .join(
                PlacementDrive,
                Application.drive_id == PlacementDrive.id,
            )
            .filter(
                PlacementDrive.company_id == company.id,
                Application.status == ApplicationStatus.REJECTED,
            )
            .count()
        )

        pending_students = (
            total_applications
            - selected_students
            - rejected_students
        )

        self.heading("Drive Summary")

        self.paragraph(
            f"<b>Total Drives:</b> {total_drives}"
        )

        self.paragraph(
            f"<b>Total Applications:</b> {total_applications}"
        )

        self.paragraph(
            f"<b>Selected Students:</b> {selected_students}"
        )

        self.paragraph(
            f"<b>Rejected Students:</b> {rejected_students}"
        )

        self.paragraph(
            f"<b>Pending Applications:</b> {pending_students}"
        )

        return self.build()