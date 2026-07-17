import { FiCheckCircle } from "react-icons/fi";

const eligibility = [
  { title: "CGPA", value: "8.62", required: "7.00+", status: true },
  { title: "Attendance", value: "91%", required: "75%+", status: true },
  { title: "Active Backlogs", value: "0", required: "0", status: true },
  { title: "Eligible Companies", value: "12", required: "-", status: true },
];

export default function EligibilityCard() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">Placement Eligibility</h2>
      <p className="mb-6 text-gray-500">
        Eligibility status for current placement season
      </p>

      <div className="space-y-4">
        {eligibility.map((item) => (
          <div
            key={item.title}
            className="flex items-center justify-between rounded-2xl border p-4"
          >
            <div>
              <h3 className="font-semibold">{item.title}</h3>
              <p className="text-sm text-gray-500">
                Required: {item.required}
              </p>
            </div>

            <div className="flex items-center gap-3">
              <span className="font-semibold">{item.value}</span>

              <FiCheckCircle className="text-2xl text-green-600" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}