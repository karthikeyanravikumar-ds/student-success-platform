import {
  FiBriefcase,
  FiCheckCircle,
  FiClock,
  FiAward,
} from "react-icons/fi";

const stats = [
  {
    title: "Eligible Drives",
    value: 12,
    icon: FiBriefcase,
    iconBg: "bg-blue-50",
    iconColor: "text-blue-600",
  },
  {
    title: "Applications",
    value: 8,
    icon: FiCheckCircle,
    iconBg: "bg-green-50",
    iconColor: "text-green-600",
  },
  {
    title: "Upcoming Interviews",
    value: 3,
    icon: FiClock,
    iconBg: "bg-orange-50",
    iconColor: "text-orange-600",
  },
  {
    title: "Offers Received",
    value: 1,
    icon: FiAward,
    iconBg: "bg-yellow-50",
    iconColor: "text-yellow-600",
  },
];

export default function PlacementSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((item) => {
        const Icon = item.icon;

        return (
          <div
            key={item.title}
            className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm"
          >
            <div
              className={`mb-6 flex h-14 w-14 items-center justify-center rounded-2xl ${item.iconBg}`}
            >
              <Icon className={`h-7 w-7 ${item.iconColor}`} />
            </div>

            <p className="text-gray-500">{item.title}</p>

            <h2 className="mt-3 text-5xl font-bold">
              {item.value}
            </h2>
          </div>
        );
      })}
    </div>
  );
}