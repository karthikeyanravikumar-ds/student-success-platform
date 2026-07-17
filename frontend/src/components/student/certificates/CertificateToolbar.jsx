import { FiSearch, FiFilter, FiUpload } from "react-icons/fi";

export default function CertificateToolbar() {
  return (
    <div className="flex flex-col gap-4 rounded-3xl border border-gray-200 bg-white p-6 shadow-sm md:flex-row md:items-center md:justify-between">

      <div className="relative w-full md:w-96">
        <FiSearch className="absolute left-4 top-3.5 text-gray-400" />

        <input
          type="text"
          placeholder="Search certificates..."
          className="w-full rounded-xl border border-gray-200 py-3 pl-11 pr-4 outline-none focus:border-red-700"
        />
      </div>

      <div className="flex gap-3">

        <button className="flex items-center gap-2 rounded-xl border border-gray-200 px-5 py-3 hover:bg-gray-50">
          <FiFilter />
          Filter
        </button>

        <button className="flex items-center gap-2 rounded-xl bg-red-800 px-5 py-3 text-white hover:bg-red-900">
          <FiUpload />
          Upload
        </button>

      </div>

    </div>
  );
}