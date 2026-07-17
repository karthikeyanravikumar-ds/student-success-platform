import {
  AlertTriangle,
  CalendarDays,
  Briefcase,
} from "lucide-react";

const alerts = [
  {
    icon: CalendarDays,
    title: "Exam Tomorrow",
    color: "text-orange-600",
  },
  {
    icon: Briefcase,
    title: "Placement Deadline",
    color: "text-blue-600",
  },
  {
    icon: AlertTriangle,
    title: "Attendance Below 75%",
    color: "text-red-600",
  },
];

export default function PinnedAlerts() {
  return (
    <div className="mb-6 rounded-3xl border border-red-200 bg-red-50 p-6">

      <h2 className="mb-4 text-lg font-bold text-[#8E1528]">
        📌 Important Alerts
      </h2>

      <div className="flex flex-wrap gap-4">

        {alerts.map((alert) => {

          const Icon = alert.icon;

          return (

            <div
              key={alert.title}
              className="flex items-center gap-3 rounded-xl bg-white px-5 py-3 shadow-sm"
            >
              <Icon
                size={20}
                className={alert.color}
              />

              <span className="font-medium">
                {alert.title}
              </span>

            </div>

          );

        })}

      </div>

    </div>
  );
}