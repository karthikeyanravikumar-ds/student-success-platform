import PageContainer from "../../layouts/PageContainer";
import { useState } from "react";

import ProjectSummary from "../../components/student/projects/ProjectSummary";
import ProjectToolbar from "../../components/student/projects/ProjectToolbar";
import ProjectGrid from "../../components/student/projects/ProjectGrid";
import ProjectDetails from "../../components/student/projects/ProjectDetails";
import GitHubRepositories from "../../components/student/projects/GitHubRepositories";
import FacultyApproval from "../../components/student/projects/FacultyApproval";
import ProjectTimeline from "../../components/student/projects/ProjectTimeline";
import SkillsUsed from "../../components/student/projects/SkillsUsed";
import ProjectDocuments from "../../components/student/projects/ProjectDocuments";
import DownloadPortfolio from "../../components/student/projects/DownloadPortfolio";

export default function Projects() {

  const [projects, setProjects] = useState([
  {
    id: 1,
    title: "Student Success Platform",
    tech: "React • FastAPI • PostgreSQL",
    status: "Ongoing",
  },
  {
    id: 2,
    title: "Urban Flood Risk Mapping",
    tech: "Python • GIS • Power BI",
    status: "Completed",
  },
  {
    id: 3,
    title: "Financial Fraud Detection",
    tech: "Python • ML",
    status: "Planning",
  },
]);

  return (
    <PageContainer>
      <div className="mb-8">
        <h1 className="text-4xl font-bold">
          Projects
        </h1>

        <p className="text-gray-500">
          Manage academic projects, submissions and faculty approvals.
        </p>
      </div>

      <ProjectSummary />

      <div className="mt-8">
        <ProjectToolbar
    projects={projects}
    setProjects={setProjects}
/>
      </div>

      <div className="mt-8">
        <ProjectGrid
    projects={projects}
/>
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <ProjectDetails />
        <GitHubRepositories />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <FacultyApproval />
        <ProjectTimeline />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-3">
  <SkillsUsed />
  <ProjectDocuments />
  <DownloadPortfolio />
</div>
    </PageContainer>
  );
}