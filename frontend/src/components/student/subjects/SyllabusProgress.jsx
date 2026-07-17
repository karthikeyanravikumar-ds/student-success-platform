const syllabus = [
  {
    subject: "Python Programming",
    progress: 90,
  },
  {
    subject: "Machine Learning",
    progress: 75,
  },
  {
    subject: "Statistics",
    progress: 68,
  },
  {
    subject: "DBMS",
    progress: 85,
  },
  {
    subject: "React Development",
    progress: 60,
  },
  {
    subject: "Power BI",
    progress: 82,
  },
];

function progressColor(progress) {
  if (progress >= 80) return "bg-green-500";
  if (progress >= 70) return "bg-blue-500";
  return "bg-yellow-500";
}

export default function SyllabusProgress() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6">
        <h2 className="text-2xl font-bold">
          Syllabus Progress
        </h2>

        <p className="text-gray-500">
          Current Semester Coverage
        </p>
      </div>

      <div className="space-y-5">

        {syllabus.map((item) => (
          <div key={item.subject}>

            <div className="mb-2 flex justify-between">

              <span className="font-medium">
                {item.subject}
              </span>

              <span className="font-semibold">
                {item.progress}%
              </span>

            </div>

            <div className="h-3 rounded-full bg-gray-200">

              <div
                className={`h-3 rounded-full ${progressColor(
                  item.progress
                )}`}
                style={{
                  width: `${item.progress}%`,
                }}
              />

            </div>

          </div>
        ))}

      </div>

    </div>
  );
}