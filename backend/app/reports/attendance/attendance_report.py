from app.models.attendance import Attendance, AttendanceStatus
from app.reports.generators.pdf_generator import PDFGenerator


class AttendanceReport(PDFGenerator):

    def generate(
        self,
        db,
        student,
    ):

        self.title(
            "VIDYALANKAR SCHOOL OF INFORMATION TECHNOLOGY"
        )

        self.heading(
            "Student Attendance Report"
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

        total_classes = (
            db.query(Attendance)
            .filter(
                Attendance.student_id == student.id
            )
            .count()
        )

        present_classes = (
            db.query(Attendance)
            .filter(
                Attendance.student_id == student.id,
                Attendance.status == AttendanceStatus.PRESENT,
            )
            .count()
        )

        absent_classes = (
            db.query(Attendance)
            .filter(
                Attendance.student_id == student.id,
                Attendance.status == AttendanceStatus.ABSENT,
            )
            .count()
        )

        percentage = (
            (present_classes / total_classes) * 100
            if total_classes > 0
            else 0
        )

        self.heading("Attendance Summary")

        self.paragraph(
            f"<b>Total Classes:</b> {total_classes}"
        )

        self.paragraph(
            f"<b>Present:</b> {present_classes}"
        )

        self.paragraph(
            f"<b>Absent:</b> {absent_classes}"
        )

        self.paragraph(
            f"<b>Attendance Percentage:</b> {percentage:.2f}%"
        )

        status = (
            "Eligible"
            if percentage >= 75
            else "Defaulter"
        )

        self.paragraph(
            f"<b>Status:</b> {status}"
        )

        return self.build()