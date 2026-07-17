import { FiRotateCcw, FiSave, FiX } from "react-icons/fi";

export default function SettingsActions() {
  return (
    <section className="sticky bottom-4 z-10 rounded-2xl border border-gray-200 bg-white p-6 shadow-lg">

      <div className="flex flex-col items-center justify-between gap-4 md:flex-row">

        <div>

          <h2 className="text-lg font-semibold text-gray-900">
            Save Your Changes
          </h2>

          <p className="text-sm text-gray-500">
            Your updates will only be applied after clicking <strong>Save Changes</strong>.
          </p>

        </div>

        <div className="flex flex-wrap gap-3">

          <button
            className="flex items-center gap-2 rounded-xl border border-gray-300 px-5 py-2.5 font-medium text-gray-700 transition hover:bg-gray-100"
          >
            <FiRotateCcw />
            Reset
          </button>

          <button
            className="flex items-center gap-2 rounded-xl border border-gray-300 px-5 py-2.5 font-medium text-gray-700 transition hover:bg-gray-100"
          >
            <FiX />
            Cancel
          </button>

          <button
            className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-6 py-2.5 font-medium text-white transition hover:bg-[#731120]"
          >
            <FiSave />
            Save Changes
          </button>

        </div>

      </div>

    </section>
  );
}