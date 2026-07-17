import { Search, Filter } from "lucide-react";

export default function SubjectToolbar() {
  return (
    <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">

      <div className="relative w-full md:w-96">

        <Search
          className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"
          size={18}
        />

        <input
          type="text"
          placeholder="Search subject..."
          className="w-full rounded-xl border border-gray-300 py-3 pl-11 pr-4 outline-none transition focus:border-[#8E1528]"
        />

      </div>

      <div className="flex items-center gap-3">

        <Filter
          size={18}
          className="text-gray-500"
        />

        <select className="rounded-xl border border-gray-300 px-4 py-3 outline-none focus:border-[#8E1528]">

          <option>Semester V</option>
          <option>Semester IV</option>
          <option>Semester III</option>

        </select>

      </div>

    </div>
  );
}