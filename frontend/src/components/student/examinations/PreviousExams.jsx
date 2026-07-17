import { FileText } from "lucide-react";

const exams = [
  {
    semester: "Semester IV",
    sgpa: "8.62",
    status: "Completed",
  },
  {
    semester: "Semester III",
    sgpa: "8.41",
    status: "Completed",
  },
  {
    semester: "Semester II",
    sgpa: "8.27",
    status: "Completed",
  },
  {
    semester: "Semester I",
    sgpa: "7.18",
    status: "Completed",
  },
];

export default function PreviousExams() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6">

        <h2 className="text-2xl font-bold">
          Previous Examinations
        </h2>

        <p className="text-gray-500">
          Academic History
        </p>

      </div>

      <div className="space-y-4">

        {exams.map((exam) => (

          <div
            key={exam.semester}
            className="flex items-center justify-between rounded-xl border p-4 hover:bg-gray-50"
          >

            <div className="flex items-center gap-4">

              <div className="rounded-xl bg-red-50 p-3 text-[#8E1528]">
                <FileText size={22} />
              </div>

              <div>

                <h3 className="font-semibold">
                  {exam.semester}
                </h3>

                <p className="text-sm text-gray-500">
                  SGPA : {exam.sgpa}
                </p>

              </div>

            </div>

            <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
              {exam.status}
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}