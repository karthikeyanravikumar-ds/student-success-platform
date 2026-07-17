import { FiExternalLink } from "react-icons/fi";

function getStatusColor(status) {
  switch (status) {
    case "Applied":
      return "bg-blue-100 text-blue-700";

    case "Under Review":
      return "bg-yellow-100 text-yellow-700";

    case "Interview Scheduled":
      return "bg-purple-100 text-purple-700";

    case "Shortlisted":
      return "bg-green-100 text-green-700";

    case "Selected":
      return "bg-emerald-100 text-emerald-700";

    case "Rejected":
      return "bg-red-100 text-red-700";

    default:
      return "bg-gray-100 text-gray-700";
  }
}

export default function AppliedCompanies({
  applications,
}) {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">Applied Companies</h2>
      <p className="mb-6 text-gray-500">
        Track your placement applications
      </p>

      {applications.length === 0 ? (

  <div className="rounded-2xl border border-dashed p-10 text-center">

    <h3 className="text-xl font-semibold">
      No Applications Yet
    </h3>

    <p className="mt-2 text-gray-500">
      Apply to a placement drive to see your applications here.
    </p>

  </div>

) : (

  <div className="space-y-4">

    {applications.map((company) => (

      <div
        key={company.id || company.company}
        className="flex items-center justify-between rounded-2xl border p-5"
      >

        <div>

          <h3 className="text-xl font-semibold">
            {company.company}
          </h3>

          <p className="text-gray-500">
            {company.role}
          </p>

          <p className="mt-1 text-sm text-gray-400">
            Applied on {company.appliedDate}
          </p>

        </div>

        <div className="flex items-center gap-4">

          <span
            className={`rounded-full px-4 py-2 text-sm font-medium ${getStatusColor(
              company.applicationStatus
            )}`}
          >
            {company.applicationStatus}
          </span>

          <button className="rounded-xl border p-2 hover:bg-gray-100">
            <FiExternalLink className="text-lg" />
          </button>

        </div>

      </div>

    ))}

  </div>

)}
    </div>
  );
}