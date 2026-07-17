import {
  FiUpload,
  FiClock,
  FiCheckCircle,
} from "react-icons/fi";

const steps = [
  {
    title: "Certificate Uploaded",
    date: "10 Jul 2026",
    icon: FiUpload,
    status: "Completed",
    color: "bg-green-100 text-green-700",
  },
  {
    title: "Faculty Verification",
    date: "11 Jul 2026",
    icon: FiClock,
    status: "In Review",
    color: "bg-orange-100 text-orange-700",
  },
  {
    title: "Verification Complete",
    date: "-",
    icon: FiCheckCircle,
    status: "Pending",
    color: "bg-gray-100 text-gray-600",
  },
];

export default function VerificationStatus() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">
        Verification Status
      </h2>

      <div className="mt-8 space-y-8">
        {steps.map((step) => {
          const Icon = step.icon;

          return (
            <div key={step.title} className="flex gap-4">
              <Icon className="mt-1 h-7 w-7 text-red-700" />

              <div>
                <h3 className="text-xl font-semibold">
                  {step.title}
                </h3>

                <p className="text-gray-500">
                  {step.date}
                </p>

                <span className={`mt-2 inline-block rounded-full px-4 py-1 text-sm ${step.color}`}>
                  {step.status}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}