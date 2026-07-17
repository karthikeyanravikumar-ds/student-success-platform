import PageContainer from "../../layouts/PageContainer";

import ExamSummary from "../../components/student/examinations/ExamSummary";
import UpcomingExams from "../../components/student/examinations/UpcomingExams";
import ExamSchedule from "../../components/student/examinations/ExamSchedule";
import HallTicketCard from "../../components/student/examinations/HallTicketCard";
import ExamRules from "../../components/student/examinations/ExamRules";
import PreviousExams from "../../components/student/examinations/PreviousExams";

export default function Examinations() {
  return (
    <PageContainer>

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Examinations
        </h1>

        <p className="text-gray-500">
          View exam schedules, hall tickets and important instructions.
        </p>

      </div>

      <ExamSummary />

      <div className="mt-8">
        <UpcomingExams />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <ExamSchedule />
        <HallTicketCard />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <ExamRules />
        <PreviousExams />
      </div>

    </PageContainer>
  );
}