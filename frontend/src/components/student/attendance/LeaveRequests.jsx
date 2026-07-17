import { useState } from "react";
import ApplyLeaveModal from "./modals/ApplyLeaveModal";

const leaves = [
  {
    date: "10 Jul 2026",
    type: "Medical",
    reason: "Fever",
    status: "Pending",
  },
  {
    date: "28 Jun 2026",
    type: "On Duty",
    reason: "Hackathon",
    status: "Approved",
  },
  {
    date: "11 Jun 2026",
    type: "Personal",
    reason: "Family Function",
    status: "Rejected",
  },
];

function getStatusClass(status) {
  switch (status) {
    case "Approved":
      return "bg-green-100 text-green-700";
    case "Pending":
      return "bg-yellow-100 text-yellow-700";
    case "Rejected":
      return "bg-red-100 text-red-700";
    default:
      return "bg-gray-100 text-gray-700";
  }
}

export default function LeaveRequests() {

  const [showModal, setShowModal] = useState(false);

  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-xl font-bold">
            Leave Requests
          </h2>

          <p className="text-sm text-gray-500">
            View your leave request history
          </p>
        </div>

        <button
        onClick={() => setShowModal(true)}
        className="rounded-lg bg-[#8E1528] px-5 py-2 text-white transition hover:bg-[#73111f]"
        >
          Apply Leave
        </button>

      </div>

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead className="border-b bg-gray-50">

            <tr>

              <th className="px-4 py-3 text-left">Date</th>
              <th className="px-4 py-3 text-left">Type</th>
              <th className="px-4 py-3 text-left">Reason</th>
              <th className="px-4 py-3 text-center">Status</th>

            </tr>

          </thead>

          <tbody>

            {leaves.map((leave) => (

              <tr
                key={`${leave.date}-${leave.type}`}
                className="border-b hover:bg-gray-50"
              >

                <td className="px-4 py-4">{leave.date}</td>

                <td className="px-4 py-4">{leave.type}</td>

                <td className="px-4 py-4">{leave.reason}</td>

                <td className="px-4 py-4 text-center">

                  <span
                    className={`rounded-full px-3 py-1 text-sm font-medium ${getStatusClass(
                      leave.status
                    )}`}
                  >
                    {leave.status}
                  </span>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

      {showModal && (
        <ApplyLeaveModal
          onClose={() => setShowModal(false)}
        />
      )}

    </div>
  );
}