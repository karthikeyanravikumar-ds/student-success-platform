class NotificationTemplates:

    @staticmethod
    def certificate_verified():
        return (
            "Certificate Verified",
            "Your certificate has been verified successfully.",
        )

    @staticmethod
    def certificate_rejected():
        return (
            "Certificate Rejected",
            "Your certificate has been rejected. Please review the remarks and upload a corrected version if necessary.",
        )

    @staticmethod
    def interview_scheduled(company_name: str):
        return (
            "Interview Scheduled",
            f"Your interview with {company_name} has been scheduled.",
        )

    @staticmethod
    def offer_received(company_name: str):
        return (
            "Offer Received",
            f"Congratulations! You have received an offer from {company_name}.",
        )

    @staticmethod
    def attendance_low(subject_name: str):
        return (
            "Low Attendance",
            f"Your attendance in {subject_name} is below the required threshold.",
        )

    @staticmethod
    def result_published(semester: int):
        return (
            "Result Published",
            f"Semester {semester} results have been published.",
        )