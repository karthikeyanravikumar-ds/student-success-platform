const exams = [
  {
    date: "15 Jul 2026",
    subject: "Python Programming",
    time: "09:00 AM - 12:00 PM",
    hall: "A-301",
    type: "Theory",
  },
  {
    date: "18 Jul 2026",
    subject: "Machine Learning",
    time: "02:00 PM - 05:00 PM",
    hall: "B-204",
    type: "Theory",
  },
  {
    date: "20 Jul 2026",
    subject: "Database Management System",
    time: "09:00 AM - 12:00 PM",
    hall: "A-102",
    type: "Theory",
  },
  {
    date: "22 Jul 2026",
    subject: "Mini Project Viva",
    time: "10:00 AM - 11:00 AM",
    hall: "Seminar Hall",
    type: "Viva",
  },
];

export default function UpcomingExams() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6">
        <h2 className="text-2xl font-bold">
          Upcoming Exam Schedule
        </h2>

        <p className="text-gray-500">
          Semester V Examination Timetable
        </p>
      </div>

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead className="border-b bg-gray-50">

            <tr>
              <th className="px-4 py-3 text-left">Date</th>
              <th className="px-4 py-3 text-left">Subject</th>
              <th className="px-4 py-3 text-left">Time</th>
              <th className="px-4 py-3 text-center">Hall</th>
              <th className="px-4 py-3 text-center">Type</th>
            </tr>

          </thead>

          <tbody className="divide-y divide-gray-100">

            {exams.map((exam) => (

              <tr
                key={exam.subject}
                className="hover:bg-red-50 transition"
              >

                <td className="px-4 py-5">
                  {exam.date}
                </td>

                <td className="px-4 py-5 font-semibold">
                  {exam.subject}
                </td>

                <td className="px-4 py-5">
                  {exam.time}
                </td>

                <td className="px-4 py-5 text-center">
                  {exam.hall}
                </td>

                <td className="px-4 py-5 text-center">

                  <span
                    className={`rounded-full px-3 py-1 text-sm font-medium ${
                      exam.type === "Theory"
                        ? "bg-blue-100 text-blue-700"
                        : "bg-purple-100 text-purple-700"
                    }`}
                  >
                    {exam.type}
                  </span>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}