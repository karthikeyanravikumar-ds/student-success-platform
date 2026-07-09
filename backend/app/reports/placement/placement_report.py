from app.models.application import Application
from app.models.interview import Interview
from app.models.offer import Offer
from app.reports.generators.pdf_generator import PDFGenerator


class PlacementReport(PDFGenerator):

    def generate(
        self,
        db,
        student,
    ):

        self.title(
            "VIDYALANKAR SCHOOL OF INFORMATION TECHNOLOGY"
        )

        self.heading(
            "Student Placement Report"
        )

        self.paragraph(
            f"<b>Name:</b> {student.full_name}"
        )

        self.paragraph(
            f"<b>Roll No:</b> {student.roll_no}"
        )

        self.paragraph(
            f"<b>Department:</b> {student.department.department_name}"
        )

        self.paragraph(
            f"<b>Program:</b> {student.program.program_name}"
        )

        self.paragraph(
            f"<b>Current Semester:</b> {student.current_semester}"
        )

        applied = (
            db.query(Application)
            .filter(
                Application.student_id == student.id
            )
            .count()
        )

        interviews = (
            db.query(Interview)
            .join(
                Application,
                Interview.application_id == Application.id,
            )
            .filter(
                Application.student_id == student.id,
            )
            .count()
        )

        offers = (
            db.query(Offer)
            .join(
                Interview,
                Offer.interview_id == Interview.id,
            )
            .join(
                Application,
                Interview.application_id == Application.id,
            )
            .filter(
                Application.student_id == student.id,
            )
            .count()
        )

        self.heading("Placement Summary")

        self.paragraph(
            f"<b>Applied Drives:</b> {applied}"
        )

        self.paragraph(
            f"<b>Interviews:</b> {interviews}"
        )

        self.paragraph(
            f"<b>Offers:</b> {offers}"
        )

        status = (
            "Placed"
            if offers > 0
            else "Not Placed"
        )

        self.paragraph(
            f"<b>Placement Status:</b> {status}"
        )

        return self.build()