import PageContainer from "../../layouts/PageContainer";

import { useState } from "react";

import ApplyJobModal from "../../components/student/placement/modals/ApplyJobModal";

import PlacementSummary from "../../components/student/placement/PlacementSummary";
import UpcomingDrives from "../../components/student/placement/UpcomingDrives";
import AppliedCompanies from "../../components/student/placement/AppliedCompanies";
import EligibilityCard from "../../components/student/placement/EligibilityCard";
import InterviewTimeline from "../../components/student/placement/InterviewTimeline";
import OfferLetters from "../../components/student/placement/OfferLetters";
import PlacementResources from "../../components/student/placement/PlacementResources";
import PlacementStats from "../../components/student/placement/PlacementStats";

export default function Placement() {
  const [showApplyModal, setShowApplyModal] = useState(false);
  const [selectedCompany, setSelectedCompany] = useState(null);

const [applications, setApplications] = useState([]);
  return (
    <PageContainer>

      <div className="mb-8">
        <h1 className="text-3xl font-bold">Placement</h1>
        <p className="text-gray-500">
          Track placement drives, applications, interviews and offers.
        </p>
      </div>

      <PlacementSummary />

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <UpcomingDrives
  applications={applications}
  onApply={(company) => {
    setSelectedCompany(company);
    setShowApplyModal(true);
  }}
/>
        <EligibilityCard />
      </div>

      <div className="mt-8">
        <AppliedCompanies
    applications={applications}
/>
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <InterviewTimeline />
        <PlacementStats />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <OfferLetters />
        <PlacementResources />
      </div>

      {showApplyModal && (
  <ApplyJobModal
    company={selectedCompany}
    applications={applications}
    setApplications={setApplications}
    onClose={() => setShowApplyModal(false)}
/>
)}

    </PageContainer>
  );
}