import {
  CalendarDays,
  CheckCircle,
  Clock3,
  Award,
} from "lucide-react";

const cards = [
  {
    title: "Upcoming Exams",
    value: "3",
    icon: <CalendarDays size={24} />,
    bg: "bg-blue-50",
    color: "text-blue-600",
  },
  {
    title: "Completed",
    value: "4",
    icon: <CheckCircle size={24} />,
    bg: "bg-green-50",
    color: "text-green-600",
  },
  {
    title: "Next Exam",
    value: "15 Jul",
    icon: <Clock3 size={24} />,
    bg: "bg-red-50",
    color: "text-[#8E1528]",
  },
  {
    title: "Average Score",
    value: "84%",
    icon: <Award size={24} />,
    bg: "bg-yellow-50",
    color: "text-yellow-600",
  },
];

export default function ExamSummary() {
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

          <p className="text-gray-500">
            {card.title}
          </p>

          <h2 className="mt-2 text-4xl font-bold">
            {card.value}
          </h2>

        </div>

      ))}

    </div>
  );
}