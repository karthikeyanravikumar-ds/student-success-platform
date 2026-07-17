import { Search } from "lucide-react";

const filters = [
  "All",
  "Unread",
  "Placement",
  "Results",
  "Attendance",
  "Certificates",
  "Projects",
  "Exams",
];

export default function NotificationFilters() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-6 shadow-sm">

      <div className="relative">

        <Search
          size={18}
          className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"
        />

        <input
          type="text"
          placeholder="Search notifications..."
          className="w-full rounded-xl border border-gray-300 py-3 pl-11 pr-4 outline-none focus:border-[#8E1528]"
        />

      </div>

      <div className="mt-5 flex flex-wrap gap-3">

        {filters.map((filter) => (

          <button
            key={filter}
            className={`rounded-full px-5 py-2 text-sm font-medium transition
            ${
              filter === "All"
                ? "bg-[#8E1528] text-white"
                : "border border-gray-300 hover:border-[#8E1528]"
            }`}
          >
            {filter}
          </button>

        ))}

      </div>

    </div>
  );
}