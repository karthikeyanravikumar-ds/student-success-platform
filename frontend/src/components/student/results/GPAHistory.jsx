import { TrendingUp } from "lucide-react";

const history = [
  { semester: "Semester I", sgpa: 7.18 },
  { semester: "Semester II", sgpa: 8.27 },
  { semester: "Semester III", sgpa: 8.41 },
  { semester: "Semester IV", sgpa: 8.62 },
  { semester: "Semester V", sgpa: 8.91 },
];

export default function GPAHistory() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center gap-3">

        <TrendingUp
          size={24}
          className="text-[#8E1528]"
        />

        <div>

          <h2 className="text-2xl font-bold">
            GPA History
          </h2>

          <p className="text-gray-500">
            Semester-wise Performance
          </p>

        </div>

      </div>

      <div className="space-y-4">

        {history.map((item) => (

          <div
            key={item.semester}
            className="flex items-center justify-between rounded-xl border p-4"
          >

            <span className="font-medium">
              {item.semester}
            </span>

            <span className="text-lg font-bold text-[#8E1528]">
              {item.sgpa}
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}