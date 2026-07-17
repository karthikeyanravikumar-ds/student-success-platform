import PageContainer from "../../layouts/PageContainer";

import ResultSummary from "../../components/student/results/ResultSummary";
import PerformanceChart from "../../components/student/results/PerformanceChart";
import SemesterSelector from "../../components/student/results/SemesterSelector";
import ResultTable from "../../components/student/results/ResultTable";
import GPAHistory from "../../components/student/results/GPAHistory";
import DownloadMarksheet from "../../components/student/results/DownloadMarksheet";

export default function Results() {
  return (
    <PageContainer>

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Results
        </h1>

        <p className="text-gray-500">
          View your semester-wise academic performance and marks.
        </p>

      </div>

      <ResultSummary />

      <div className="mt-8">
        <PerformanceChart />
      </div>

      <div className="mt-8">
        <SemesterSelector />
      </div>

      <div className="mt-6">
        <ResultTable />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <GPAHistory />
        <DownloadMarksheet />
      </div>

    </PageContainer>
  );
}