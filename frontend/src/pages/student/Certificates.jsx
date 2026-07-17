import { useState } from "react";
import PageContainer from "../../layouts/PageContainer";

import CertificateSummary from "../../components/student/certificates/CertificateSummary";
import UploadCertificate from "../../components/student/certificates/UploadCertificate";
import UploadedCertificates from "../../components/student/certificates/UploadedCertificates";
import VerificationStatus from "../../components/student/certificates/VerificationStatus";
import PendingCertificates from "../../components/student/certificates/PendingCertificates";
import CertificateStatistics from "../../components/student/certificates/CertificateStatistics";
import DownloadCertificates from "../../components/student/certificates/DownloadCertificates";
import CertificateGuidelines from "../../components/student/certificates/CertificateGuidelines";

export default function Certificates() {
  const [certificates, setCertificates] = useState([
  {
    id: 1,
    name: "NPTEL - Python Programming",
    category: "Course",
    date: "08 Jul 2026",
    status: "Verified",
    file: null,
  },
  {
    id: 2,
    name: "Smart India Hackathon",
    category: "Competition",
    date: "06 Jul 2026",
    status: "Pending",
    file: null,
  },
  {
    id: 3,
    name: "AWS Cloud Foundations",
    category: "Certification",
    date: "02 Jul 2026",
    status: "Rejected",
    file: null,
  },
]);

  return (
    <PageContainer>
      <div className="mb-8">
        <h1 className="text-4xl font-bold">Certificates</h1>

        <p className="text-gray-500">
          Upload, verify and manage your academic and extracurricular certificates.
        </p>
      </div>

      <CertificateSummary />

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <UploadCertificate
  certificates={certificates}
  setCertificates={setCertificates}
/>
        <VerificationStatus />
      </div>

      <div className="mt-8">
        <UploadedCertificates
  certificates={certificates}
  setCertificates={setCertificates}
/>
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <PendingCertificates />
        <CertificateStatistics />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <DownloadCertificates />
        <CertificateGuidelines />
      </div>
    </PageContainer>
  );
}