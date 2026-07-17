import {
  FiInfo,
  FiBookOpen,
  FiShield,
  FiMail,
} from "react-icons/fi";

export default function AboutSSP() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-3xl font-bold">
        About Student Success Platform
      </h2>

      <p className="mt-3 text-gray-500">
        Student Success Platform (SSP) helps students manage academics,
        placements, projects and campus activities from a single dashboard.
      </p>

      <div className="mt-8 space-y-5">

        <div className="flex items-center justify-between rounded-2xl border p-5">
          <div className="flex items-center gap-4">
            <FiInfo className="text-2xl text-[#8E1528]" />
            <span>Version</span>
          </div>

          <span className="font-semibold">
            v1.0.0
          </span>
        </div>

        <div className="flex items-center justify-between rounded-2xl border p-5">
          <div className="flex items-center gap-4">
            <FiBookOpen className="text-2xl text-[#8E1528]" />
            <span>Terms & Conditions</span>
          </div>

          <button className="text-[#8E1528]">
            View
          </button>
        </div>

        <div className="flex items-center justify-between rounded-2xl border p-5">
          <div className="flex items-center gap-4">
            <FiShield className="text-2xl text-[#8E1528]" />
            <span>Privacy Policy</span>
          </div>

          <button className="text-[#8E1528]">
            View
          </button>
        </div>

        <div className="flex items-center justify-between rounded-2xl border p-5">
          <div className="flex items-center gap-4">
            <FiMail className="text-2xl text-[#8E1528]" />
            <span>Support</span>
          </div>

          <button className="text-[#8E1528]">
            Contact
          </button>
        </div>

      </div>

    </div>
  );
}