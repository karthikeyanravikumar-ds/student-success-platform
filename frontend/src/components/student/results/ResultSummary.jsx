import {
  GraduationCap,
  Award,
  CheckCircle,
  Trophy,
} from "lucide-react";

const cards = [
  {
    title: "CGPA",
    value: "8.62",
    icon: <GraduationCap size={24} />,
    bg: "bg-blue-50",
    color: "text-blue-600",
  },
  {
    title: "Current SGPA",
    value: "8.91",
    icon: <Award size={24} />,
    bg: "bg-green-50",
    color: "text-green-600",
  },
  {
    title: "Subjects Passed",
    value: "35",
    icon: <CheckCircle size={24} />,
    bg: "bg-emerald-50",
    color: "text-emerald-600",
  },
  {
    title: "Class Rank",
    value: "12",
    icon: <Trophy size={24} />,
    bg: "bg-yellow-50",
    color: "text-yellow-600",
  },
];

export default function ResultSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="rounded-2xl bg-white p-6 shadow-sm"
        >
          <div
            className={`mb-6 flex h-14 w-14 items-center justify-center rounded-2xl ${card.bg} ${card.color}`}
          >
            {card.icon}
          </div>

          <p className="text-gray-500">{card.title}</p>

          <h2 className="mt-2 text-4xl font-bold">
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}