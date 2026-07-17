import { FiClock } from "react-icons/fi";

const pending = [
  "IBM Data Analytics",
  "Google AI Workshop",
  "Hackathon Participation",
];

export default function PendingCertificates() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">
        Pending Verification
      </h2>

      <div className="mt-8 space-y-5">
        {pending.map((item) => (
          <div
            key={item}
            className="flex items-center justify-between rounded-2xl border p-5"
          >
            <div>
              <h3 className="font-semibold">{item}</h3>

              <p className="text-gray-500">
                Waiting for faculty approval
              </p>
            </div>

            <FiClock className="text-orange-600 text-2xl" />
          </div>
        ))}
      </div>
    </div>
  );
}