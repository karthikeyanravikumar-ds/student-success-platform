from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


class PDFGenerator:
    """
    Base PDF Generator

    Every report (Transcript, Marksheet,
    Attendance, Placement, etc.) should
    inherit from this class.
    """

    def __init__(self):
        self.buffer = BytesIO()

        self.doc = SimpleDocTemplate(
            self.buffer,
        )

        self.styles = getSampleStyleSheet()

        self.story = []

    def title(
        self,
        text: str,
    ):

        style = self.styles["Heading1"]

        style.alignment = TA_CENTER

        style.textColor = HexColor("#A41E22")

        self.story.append(
            Paragraph(text, style)
        )

        self.story.append(
            Spacer(1, 20)
        )

    def heading(
        self,
        text: str,
    ):

        style = self.styles["Heading2"]

        self.story.append(
            Paragraph(text, style)
        )

        self.story.append(
            Spacer(1, 10)
        )

    def paragraph(
        self,
        text: str,
    ):

        style = self.styles["BodyText"]

        self.story.append(
            Paragraph(text, style)
        )

        self.story.append(
            Spacer(1, 8)
        )

    def build(self):

        self.doc.build(
            self.story
        )

        pdf = self.buffer.getvalue()

        self.buffer.close()

        return pdf