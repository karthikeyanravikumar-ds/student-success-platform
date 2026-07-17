import { GraduationCap } from "lucide-react";

const faculty = [
  {
    subject: "Python Programming",
    name: "Dr. Priya Sharma",
    cabin: "A-302",
  },
  {
    subject: "Machine Learning",
    name: "Prof. Amit Verma",
    cabin: "B-204",
  },
  {
    subject: "Statistics",
    name: "Dr. Neha Patil",
    cabin: "A-118",
  },
  {
    subject: "DBMS",
    name: "Prof. Rohan Shah",
    cabin: "C-110",
  },
  {
    subject: "React Development",
    name: "Prof. Karan Mehta",
    cabin: "Lab-2",
  },
];

export default function FacultyCard() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold">
            Faculty Details
          </h2>

          <p className="text-gray-500">
            Subject Coordinators
          </p>
        </div>

        <GraduationCap className="text-[#8E1528]" size={28} />
      </div>

      <div className="space-y-4">

        {faculty.map((item) => (
          <div
            key={item.subject}
            className="rounded-xl border p-4"
          >
            <h3 className="font-semibold text-lg">
              {item.subject}
            </h3>

            <p className="text-gray-600">
              {item.name}
            </p>

            <p className="text-sm text-gray-500">
              Cabin: {item.cabin}
            </p>
          </div>
        ))}

      </div>

    </div>
  );
}