from app.reports.generators.pdf_generator import PDFGenerator


class TranscriptReport(PDFGenerator):

    def generate(
        self,
        student,
        results,
    ):

        self.title(
            "VIDYALANKAR SCHOOL OF INFORMATION TECHNOLOGY"
        )

        self.heading(
            "Official Academic Transcript"
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

        self.heading(
            "Semester Results"
        )

        for result in results:

            self.paragraph(
                (
                    f"Semester {result.semester}"
                    f" | SGPA: {result.sgpa}"
                    f" | CGPA: {result.cgpa}"
                    f" | Percentage: {result.percentage}%"
                )
            )

        return self.build()