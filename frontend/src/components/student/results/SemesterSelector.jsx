import { Filter } from "lucide-react";

export default function SemesterSelector() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">

        <div>
          <h2 className="text-2xl font-bold">
            Semester Results
          </h2>

          <p className="text-gray-500">
            Select a semester to view detailed results
          </p>
        </div>

        <div className="flex items-center gap-3">

          <Filter
            size={18}
            className="text-gray-500"
          />

          <select className="rounded-xl border border-gray-300 px-4 py-3 outline-none transition focus:border-[#8E1528]">

            <option>Semester V</option>
            <option>Semester IV</option>
            <option>Semester III</option>
            <option>Semester II</option>
            <option>Semester I</option>

          </select>

        </div>

      </div>

    </div>
  );
}