import { FiMapPin, FiCalendar, FiDollarSign } from "react-icons/fi";

const drives = [
  {
    company: "TCS",
    role: "Data Analyst",
    package: "₹7 LPA",
    location: "Mumbai",
    date: "18 Jul 2026",
    status: "Open",
  },
  {
    company: "Accenture",
    role: "Business Analyst",
    package: "₹6.5 LPA",
    location: "Pune",
    date: "22 Jul 2026",
    status: "Open",
  },
  {
    company: "Capgemini",
    role: "Software Engineer",
    package: "₹5.5 LPA",
    location: "Mumbai",
    date: "28 Jul 2026",
    status: "Upcoming",
  },
];

export default function UpcomingDrives({
  onApply,
  applications,
}) {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">Upcoming Drives</h2>

      <p className="mb-6 text-gray-500">
        Companies currently hiring
      </p>

      <div className="space-y-5">
        {drives.map((drive) => {
          const alreadyApplied = applications.some(
            (item) => item.company === drive.company
          );

          return (
            <div
              key={drive.company}
              className="rounded-2xl border p-5"
            >
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-xl font-semibold">
                    {drive.company}
                  </h3>

                  <p className="text-gray-500">
                    {drive.role}
                  </p>
                </div>

                <span className="rounded-full bg-green-100 px-4 py-1 text-green-700">
                  {drive.status}
                </span>
              </div>

              <div className="mt-4 flex flex-wrap gap-6 text-gray-600">
                <span className="flex items-center gap-2">
                  <FiDollarSign />
                  {drive.package}
                </span>

                <span className="flex items-center gap-2">
                  <FiMapPin />
                  {drive.location}
                </span>

                <span className="flex items-center gap-2">
                  <FiCalendar />
                  {drive.date}
                </span>
              </div>

              <div className="mt-6 flex justify-end">
                {alreadyApplied ? (
                  <span className="rounded-full bg-green-100 px-5 py-2 font-medium text-green-700">
                    Applied
                  </span>
                ) : (
                  <button
                    onClick={() => onApply(drive)}
                    className="rounded-xl bg-[#8E1528] px-5 py-2 font-medium text-white transition hover:bg-[#73111f]"
                  >
                    Apply Now
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}