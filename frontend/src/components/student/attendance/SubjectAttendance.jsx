const subjects = [
  { name: "Python", attendance: 95 },
  { name: "Machine Learning", attendance: 89 },
  { name: "Statistics", attendance: 72 },
  { name: "DBMS", attendance: 91 },
  { name: "React", attendance: 93 },
  { name: "Power BI", attendance: 87 },
];

function getStatus(value) {
  if (value >= 90)
    return {
      text: "Excellent",
      color: "bg-green-100 text-green-700",
    };

  if (value >= 75)
    return {
      text: "Good",
      color: "bg-blue-100 text-blue-700",
    };

  return {
    text: "Shortage",
    color: "bg-red-100 text-red-700",
  };
}

export default function SubjectAttendance() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-bold">
        Subject Wise Attendance
      </h2>

      <div className="space-y-6">
        {subjects.map((subject) => {
          const status = getStatus(subject.attendance);

          return (
            <div key={subject.name}>
              <div className="mb-2 flex items-center justify-between">
                <h3 className="font-semibold">
                  {subject.name}
                </h3>

                <span className="font-semibold">
                  {subject.attendance}%
                </span>
              </div>

              <div className="h-3 rounded-full bg-gray-200">
                <div
                  className="h-3 rounded-full bg-[#8E1528]"
                  style={{ width: `${subject.attendance}%` }}
                />
              </div>

              <div className="mt-2">
                <span
                  className={`rounded-full px-3 py-1 text-sm font-medium ${status.color}`}
                >
                  {status.text}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}