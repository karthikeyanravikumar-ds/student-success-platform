import { Calendar, BookOpen, CheckCircle, AlertTriangle } from "lucide-react";

const cards = [
  {
    title: "Overall Attendance",
    value: "91%",
    icon: Calendar,
    color: "bg-blue-50 text-blue-600",
  },
  {
    title: "Subjects Above 75%",
    value: "6",
    icon: CheckCircle,
    color: "bg-green-50 text-green-600",
  },
  {
    title: "Subjects Below 75%",
    value: "1",
    icon: AlertTriangle,
    color: "bg-red-50 text-red-600",
  },
  {
    title: "Total Subjects",
    value: "7",
    icon: BookOpen,
    color: "bg-yellow-50 text-yellow-600",
  },
];

export default function AttendanceSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => {
        const Icon = card.icon;

        return (
          <div
            key={card.title}
            className="rounded-2xl bg-white p-6 shadow-sm"
          >
            <div className={`mb-4 inline-flex rounded-xl p-3 ${card.color}`}>
              <Icon size={22} />
            </div>

            <p className="text-gray-500">{card.title}</p>

            <h2 className="mt-2 text-3xl font-bold">{card.value}</h2>
          </div>
        );
      })}
    </div>
  );
}