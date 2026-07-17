import { CalendarDays, Clock3 } from "lucide-react";

const exams = [
  {
    subject: "Python Programming",
    date: "15 Jul 2026",
    days: 4,
  },
  {
    subject: "Machine Learning",
    date: "18 Jul 2026",
    days: 7,
  },
  {
    subject: "Database Management System",
    date: "20 Jul 2026",
    days: 9,
  },
  {
    subject: "Mini Project Viva",
    date: "22 Jul 2026",
    days: 11,
  },
];

export default function ExamSchedule() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center gap-3">

        <div className="rounded-xl bg-red-50 p-3 text-[#8E1528]">
          <CalendarDays size={22} />
        </div>

        <div>
          <h2 className="text-2xl font-bold">
            Exam Countdown
          </h2>

          <p className="text-gray-500">
            Upcoming examinations
          </p>
        </div>

      </div>

      <div className="space-y-5">

        {exams.map((exam) => (

          <div
            key={exam.subject}
            className="flex items-center justify-between rounded-xl border p-5 hover:border-[#8E1528] transition"
          >

            <div>

              <h3 className="text-lg font-semibold">
                {exam.subject}
              </h3>

              <p className="text-gray-500">
                {exam.date}
              </p>

            </div>

            <div className="flex items-center gap-2 rounded-full bg-red-50 px-4 py-2 text-[#8E1528]">

              <Clock3 size={18} />

              <span className="font-semibold">
                {exam.days} Days Left
              </span>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}