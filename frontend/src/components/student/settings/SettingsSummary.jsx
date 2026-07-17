import {
  FiUser,
  FiShield,
  FiBell,
  FiMonitor,
} from "react-icons/fi";

const cards = [
  {
    title: "Profile Completion",
    value: "95%",
    icon: <FiUser />,
    color: "bg-blue-50 text-blue-600",
  },
  {
    title: "Security Score",
    value: "Strong",
    icon: <FiShield />,
    color: "bg-green-50 text-green-600",
  },
  {
    title: "Notifications",
    value: "Enabled",
    icon: <FiBell />,
    color: "bg-yellow-50 text-yellow-600",
  },
  {
    title: "Theme",
    value: "Light",
    icon: <FiMonitor />,
    color: "bg-purple-50 text-purple-600",
  },
];

export default function SettingsSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="rounded-3xl border border-gray-200 bg-white p-6 shadow-sm"
        >
          <div
            className={`mb-6 flex h-14 w-14 items-center justify-center rounded-2xl text-2xl ${card.color}`}
          >
            {card.icon}
          </div>

          <p className="text-gray-500">{card.title}</p>

          <h3 className="mt-2 text-3xl font-bold">
            {card.value}
          </h3>
        </div>
      ))}
    </div>
  );
}