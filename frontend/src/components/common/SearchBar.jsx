import { FiSearch } from "react-icons/fi";

export default function SearchBar() {
  return (
    <div className="flex items-center gap-2 rounded-xl border border-gray-200 bg-gray-50 px-4 py-2">
      <FiSearch className="text-gray-400" />
      <input
        type="text"
        placeholder="Search..."
        className="bg-transparent outline-none text-sm w-48"
      />
    </div>
  );
}