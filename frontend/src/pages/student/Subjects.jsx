import PageContainer from "../../layouts/PageContainer";

import SubjectSummary from "../../components/student/subjects/SubjectSummary";
import SubjectList from "../../components/student/subjects/SubjectList";
import FacultyCard from "../../components/student/subjects/FacultyCard";
import SyllabusProgress from "../../components/student/subjects/SyllabusProgress";
import SubjectToolbar from "../../components/student/subjects/SubjectToolbar";

export default function Subjects() {
  return (
    <PageContainer>

      <div className="mb-8">
        <h1 className="text-4xl font-bold">Subjects</h1>

        <p className="text-gray-500">
          View enrolled subjects, faculty details and syllabus progress.
        </p>
      </div>

      <SubjectSummary />

      <div className="mt-8">
        <SubjectToolbar />
      </div>

      <div className="mt-8">
        <SubjectList />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <FacultyCard />
        <SyllabusProgress />
      </div>

    </PageContainer>
  );
}