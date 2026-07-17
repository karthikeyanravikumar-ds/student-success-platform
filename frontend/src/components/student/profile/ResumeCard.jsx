import {
  FileText,
  Eye,
  Download,
  Upload,
  Calendar,
} from "lucide-react";

export default function ResumeCard({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-xl font-bold text-gray-900">
            Resume
          </h2>

          <p className="text-sm text-gray-500">
            Manage your latest uploaded resume
          </p>
        </div>

        <div className="rounded-xl bg-red-50 p-3">
          <FileText className="text-[#8E1528]" size={24} />
        </div>

      </div>

      <div className="rounded-xl border border-gray-200 p-5">

        <div className="flex items-center justify-between">

          <div>

            <h3 className="font-semibold text-gray-900">
              Resume.pdf
            </h3>

            <div className="mt-2 flex items-center gap-2 text-sm text-gray-500">

              <Calendar size={16} />

              Last Updated:
              {student.resumeUpdated}

            </div>

          </div>

          <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
            Uploaded
          </span>

        </div>

      </div>

      <div className="mt-6 flex flex-wrap gap-3">

        <button className="flex items-center gap-2 rounded-xl border px-4 py-2 transition hover:bg-gray-50">

          <Eye size={18} />

          Preview

        </button>

        <button className="flex items-center gap-2 rounded-xl border px-4 py-2 transition hover:bg-gray-50">

          <Download size={18} />

          Download

        </button>

        <button className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-4 py-2 text-white transition hover:bg-[#73111f]">

          <Upload size={18} />

          Replace Resume

        </button>

      </div>

    </div>
  );
}