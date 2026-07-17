import {
  FiBell,
  FiCheckCircle,
  FiClock,
  FiAlertTriangle,
} from "react-icons/fi";

const stats = [
  {
    title: "Total",
    value: 28,
    icon: FiBell,
    color: "text-blue-600",
    bg: "bg-blue-50",
  },
  {
    title: "Unread",
    value: 7,
    icon: FiClock,
    color: "text-orange-600",
    bg: "bg-orange-50",
  },
  {
    title: "Read",
    value: 19,
    icon: FiCheckCircle,
    color: "text-green-600",
    bg: "bg-green-50",
  },
  {
    title: "Important",
    value: 2,
    icon: FiAlertTriangle,
    color: "text-red-600",
    bg: "bg-red-50",
  },
];

export default function NotificationSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((item) => {
        const Icon = item.icon;

        return (
          <div
            key={item.title}
            className="rounded-3xl bg-white p-8 shadow-sm"
          >
            <div
              className={`mb-5 flex h-14 w-14 items-center justify-center rounded-2xl ${item.bg}`}
            >
              <Icon className={`h-7 w-7 ${item.color}`} />
            </div>

            <p className="text-gray-500">{item.title}</p>

            <h2 className="mt-2 text-5xl font-bold">{item.value}</h2>
          </div>
        );
      })}
    </div>
  );
}