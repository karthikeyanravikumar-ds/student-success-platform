const results = [
  {
    code: "DS501",
    subject: "Python Programming",
    internal: 28,
    external: 58,
    total: 86,
    grade: "A+",
    credits: 4,
    status: "Pass",
  },
  {
    code: "DS502",
    subject: "Machine Learning",
    internal: 27,
    external: 55,
    total: 82,
    grade: "A",
    credits: 4,
    status: "Pass",
  },
  {
    code: "DS503",
    subject: "Statistics",
    internal: 22,
    external: 47,
    total: 69,
    grade: "B+",
    credits: 3,
    status: "Pass",
  },
  {
    code: "DS504",
    subject: "Database Management System",
    internal: 29,
    external: 60,
    total: 89,
    grade: "A+",
    credits: 4,
    status: "Pass",
  },
  {
    code: "DS505",
    subject: "React Development",
    internal: 30,
    external: 58,
    total: 88,
    grade: "A+",
    credits: 3,
    status: "Pass",
  },
  {
    code: "DS506",
    subject: "Power BI",
    internal: 26,
    external: 54,
    total: 80,
    grade: "A",
    credits: 3,
    status: "Pass",
  },
  {
    code: "DS507",
    subject: "Mini Project",
    internal: 48,
    external: 49,
    total: 97,
    grade: "O",
    credits: 3,
    status: "Pass",
  },
];

function gradeColor(grade) {
  switch (grade) {
    case "O":
      return "bg-purple-100 text-purple-700";
    case "A+":
      return "bg-green-100 text-green-700";
    case "A":
      return "bg-blue-100 text-blue-700";
    case "B+":
      return "bg-yellow-100 text-yellow-700";
    default:
      return "bg-gray-100 text-gray-700";
  }
}

export default function ResultTable() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6">
        <h2 className="text-2xl font-bold">
          Subject-wise Results
        </h2>

        <p className="text-gray-500">
          Semester V Examination
        </p>
      </div>

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead className="border-b bg-gray-50">

            <tr>

              <th className="px-4 py-3 text-left">Code</th>
              <th className="px-4 py-3 text-left">Subject</th>
              <th className="px-4 py-3 text-center">IA</th>
              <th className="px-4 py-3 text-center">ESE</th>
              <th className="px-4 py-3 text-center">Total</th>
              <th className="px-4 py-3 text-center">Grade</th>
              <th className="px-4 py-3 text-center">Credits</th>
              <th className="px-4 py-3 text-center">Status</th>

            </tr>

          </thead>

          <tbody className="divide-y divide-gray-100">

            {results.map((item) => (

              <tr
                key={item.code}
                className="hover:bg-red-50 transition"
              >

                <td className="px-4 py-5 font-semibold">
                  {item.code}
                </td>

                <td className="px-4 py-5 font-medium">
                  {item.subject}
                </td>

                <td className="px-4 py-5 text-center">
                  {item.internal}
                </td>

                <td className="px-4 py-5 text-center">
                  {item.external}
                </td>

                <td className="px-4 py-5 text-center font-bold">
                  {item.total}
                </td>

                <td className="px-4 py-5 text-center">

                  <span
                    className={`rounded-full px-3 py-1 text-sm font-semibold ${gradeColor(item.grade)}`}
                  >
                    {item.grade}
                  </span>

                </td>

                <td className="px-4 py-5 text-center">
                  {item.credits}
                </td>

                <td className="px-4 py-5 text-center">

                  <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-semibold text-green-700">
                    {item.status}
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