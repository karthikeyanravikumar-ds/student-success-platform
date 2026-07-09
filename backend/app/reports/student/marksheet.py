from app.reports.generators.pdf_generator import PDFGenerator


class MarksheetReport(PDFGenerator):

    def generate(
        self,
        db,
        student,
    ):
        self.title(
            "VIDYALANKAR SCHOOL OF INFORMATION TECHNOLOGY"
        )

        self.heading("Official Semester Marksheet")

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

        self.heading("Academic Performance")

        latest_result = (
            student.results[-1]
            if student.results
            else None
        )

        if latest_result:

            self.paragraph(
                f"<b>Semester:</b> {latest_result.semester}"
            )

            self.paragraph(
                f"<b>Total Marks:</b> {latest_result.total_marks}"
            )

            self.paragraph(
                f"<b>Maximum Marks:</b> {latest_result.total_max_marks}"
            )

            self.paragraph(
                f"<b>Percentage:</b> {latest_result.percentage}%"
            )

            self.paragraph(
                f"<b>SGPA:</b> {latest_result.sgpa}"
            )

            self.paragraph(
                f"<b>CGPA:</b> {latest_result.cgpa}"
            )

            self.paragraph(
                f"<b>Result:</b> {latest_result.result_status.value}"
            )

        else:

            self.paragraph(
                "No result available."
            )

        return self.build()