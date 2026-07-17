const subjects = [
  {
    code: "DS501",
    name: "Python Programming",
    faculty: "Dr. Priya Sharma",
    credits: 4,
    attendance: "95%",
    status: "Excellent",
  },
  {
    code: "DS502",
    name: "Machine Learning",
    faculty: "Prof. Amit Verma",
    credits: 4,
    attendance: "89%",
    status: "Good",
  },
  {
    code: "DS503",
    name: "Statistics",
    faculty: "Dr. Neha Patil",
    credits: 3,
    attendance: "72%",
    status: "Shortage",
  },
  {
    code: "DS504",
    name: "DBMS",
    faculty: "Prof. Rohan Shah",
    credits: 4,
    attendance: "91%",
    status: "Excellent",
  },
  {
    code: "DS505",
    name: "React Development",
    faculty: "Prof. Karan Mehta",
    credits: 3,
    attendance: "93%",
    status: "Excellent",
  },
  {
    code: "DS506",
    name: "Power BI",
    faculty: "Dr. Sneha Kulkarni",
    credits: 3,
    attendance: "87%",
    status: "Good",
  },
  {
    code: "DS507",
    name: "Mini Project",
    faculty: "Prof. Rahul Nair",
    credits: 3,
    attendance: "100%",
    status: "Excellent",
  },
];

export default function SubjectList() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <div className="mb-6">
        <h2 className="text-2xl font-bold">
          Enrolled Subjects
        </h2>

        <p className="text-gray-500">
          Semester V
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b text-left">
              <th className="pb-4">Code</th>
              <th className="pb-4">Subject</th>
              <th className="pb-4">Faculty</th>
              <th className="pb-4 text-center">Credits</th>
              <th className="pb-4">Attendance</th>
              <th className="pb-4">Status</th>
            </tr>
          </thead>

          <tbody className="divide-y divide-gray-100">
            {subjects.map((subject) => (
              <tr
                key={subject.code}
                className="border-b hover:bg-gray-50"
              >
                <td className="py-5 font-medium">
                  {subject.code}
                </td>

                <td>{subject.name}</td>

                <td>

                  <div className="flex items-center gap-3">

                    <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[#8E1528] text-sm font-bold text-white">

                      {subject.faculty
                        .split(" ")
                        .map((n) => n[0])
                        .join("")
                        .slice(0, 2)}

                    </div>

                    <span>{subject.faculty}</span>

                  </div>

                </td>

                <td className="text-center">
                {subject.credits}
                </td>

                <td>{subject.attendance}</td>

                <td>
                  <span
                    className={`rounded-full px-3 py-1 text-sm ${
                      subject.status === "Excellent"
                        ? "bg-green-100 text-green-700"
                        : subject.status === "Good"
                        ? "bg-blue-100 text-blue-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {subject.status}
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