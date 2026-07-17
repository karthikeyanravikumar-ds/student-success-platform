import {
  FiAlertTriangle,
  FiCalendar,
  FiClock,
} from "react-icons/fi";

const alerts = [
  {
    title: "Exam Tomorrow",
    icon: FiCalendar,
    color: "text-red-600",
  },
  {
    title: "Placement Deadline",
    icon: FiClock,
    color: "text-orange-600",
  },
  {
    title: "Low Attendance Warning",
    icon: FiAlertTriangle,
    color: "text-yellow-600",
  },
];

export default function ImportantAlerts() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">

      <h2 className="text-2xl font-bold mb-6">
        Important Alerts
      </h2>

      <div className="space-y-5">

        {alerts.map((item) => {
          const Icon = item.icon;

          return (
            <div
              key={item.title}
              className="flex items-center gap-4 rounded-2xl bg-gray-50 p-4"
            >
              <Icon className={`h-6 w-6 ${item.color}`} />

              <span className="font-medium">
                {item.title}
              </span>

            </div>
          );
        })}

      </div>

    </div>
  );
}