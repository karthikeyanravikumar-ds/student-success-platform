import {
  Award,
  CheckCircle2,
  Clock3,
  Eye,
  Download,
} from "lucide-react";

export default function CertificatesCard() {
  const certificates = [
    {
      id: 1,
      title: "Python Programming",
      issuer: "Coursera",
      date: "May 2026",
      status: "Verified",
    },
    {
      id: 2,
      title: "Machine Learning",
      issuer: "NPTEL",
      date: "June 2026",
      status: "Verified",
    },
    {
      id: 3,
      title: "Power BI",
      issuer: "Microsoft",
      date: "July 2026",
      status: "Pending",
    },
  ];

  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-xl font-bold text-gray-900">
            Certificates
          </h2>

          <p className="text-sm text-gray-500">
            Academic & Professional Certifications
          </p>
        </div>

        <div className="rounded-xl bg-red-50 p-3">
          <Award className="text-[#8E1528]" size={24} />
        </div>

      </div>

      <div className="space-y-4">

        {certificates.map((certificate) => (

          <div
            key={certificate.id}
            className="rounded-xl border border-gray-200 p-5 transition hover:border-[#8E1528] hover:shadow-md"
          >

            <div className="flex items-start justify-between">

              <div>

                <h3 className="text-lg font-semibold text-gray-900">
                  {certificate.title}
                </h3>

                <p className="mt-1 text-sm text-gray-500">
                  Issued by {certificate.issuer}
                </p>

                <p className="mt-1 text-sm text-gray-500">
                  Issued: {certificate.date}
                </p>

              </div>

              {certificate.status === "Verified" ? (
                <span className="flex items-center gap-2 rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
                  <CheckCircle2 size={16} />
                  Verified
                </span>
              ) : (
                <span className="flex items-center gap-2 rounded-full bg-yellow-100 px-3 py-1 text-sm font-medium text-yellow-700">
                  <Clock3 size={16} />
                  Pending
                </span>
              )}

            </div>

            <div className="mt-5 flex gap-3">

              <button className="flex items-center gap-2 rounded-lg border px-4 py-2 hover:bg-gray-50">

                <Eye size={18} />

                View

              </button>

              <button className="flex items-center gap-2 rounded-lg border px-4 py-2 hover:bg-gray-50">

                <Download size={18} />

                Download

              </button>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}