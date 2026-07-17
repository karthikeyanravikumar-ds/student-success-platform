import {
  BookOpen,
  GraduationCap,
  Clock3,
  Award,
} from "lucide-react";

const cards = [
  {
    title: "Total Subjects",
    value: "7",
    icon: <BookOpen size={28} />,
    bg: "bg-blue-50",
    color: "text-blue-600",
  },
  {
    title: "Total Credits",
    value: "24",
    icon: <GraduationCap size={28} />,
    bg: "bg-green-50",
    color: "text-green-600",
  },
  {
    title: "Completed",
    value: "5",
    icon: <Award size={28} />,
    bg: "bg-yellow-50",
    color: "text-yellow-600",
  },
  {
    title: "Ongoing",
    value: "2",
    icon: <Clock3 size={28} />,
    bg: "bg-red-50",
    color: "text-[#8E1528]",
  },
];

export default function SubjectSummary() {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="rounded-2xl bg-white p-7 shadow-sm"
        >
          <div
            className={`mb-6 inline-flex rounded-xl p-4 ${card.bg} ${card.color}`}
          >
            {card.icon}
          </div>

          <p className="text-gray-500">{card.title}</p>

          <h2 className="mt-2 text-5xl font-bold">
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}