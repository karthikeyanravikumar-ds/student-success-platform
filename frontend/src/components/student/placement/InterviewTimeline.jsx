import {
  FiCalendar,
  FiCheckCircle,
  FiClock,
} from "react-icons/fi";

const timeline = [
  {
    stage: "Application Submitted",
    date: "05 Jul 2026",
    status: "Completed",
  },
  {
    stage: "Resume Shortlisted",
    date: "09 Jul 2026",
    status: "Completed",
  },
  {
    stage: "Technical Interview",
    date: "15 Jul 2026",
    status: "Upcoming",
  },
  {
    stage: "HR Interview",
    date: "18 Jul 2026",
    status: "Pending",
  },
];

function getIcon(status) {
  if (status === "Completed")
    return <FiCheckCircle className="text-green-600" size={22} />;

  if (status === "Upcoming")
    return <FiCalendar className="text-blue-600" size={22} />;

  return <FiClock className="text-orange-600" size={22} />;
}

export default function InterviewTimeline() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-3xl font-bold">
        Interview Timeline
      </h2>

      <p className="mb-6 text-gray-500">
        Recruitment Process
      </p>

      <div className="space-y-5">

        {timeline.map((item) => (

          <div
            key={item.stage}
            className="flex items-start gap-4"
          >

            <div className="mt-1">
              {getIcon(item.status)}
            </div>

            <div className="flex-1 border-l-2 border-gray-200 pl-5 pb-6">

              <h3 className="font-semibold text-lg">
                {item.stage}
              </h3>

              <p className="text-gray-500">
                {item.date}
              </p>

              <span
                className={`mt-2 inline-block rounded-full px-3 py-1 text-sm font-medium ${
                  item.status === "Completed"
                    ? "bg-green-100 text-green-700"
                    : item.status === "Upcoming"
                    ? "bg-blue-100 text-blue-700"
                    : "bg-orange-100 text-orange-700"
                }`}
              >
                {item.status}
              </span>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}