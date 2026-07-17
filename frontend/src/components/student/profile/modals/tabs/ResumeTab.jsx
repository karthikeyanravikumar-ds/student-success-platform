import { FileText, Upload, Eye, Download } from "lucide-react";

export default function ResumeTab({ formData }) {
  return (
    <div>

      <div className="rounded-2xl border border-dashed border-gray-300 p-8">

        <div className="flex items-center gap-4">

          <FileText className="text-[#8E1528]" size={40} />

          <div>

            <h3 className="font-semibold">
              Resume.pdf
            </h3>

            <p className="text-sm text-gray-500">
              Updated on {formData.resumeUpdated}
            </p>

          </div>

        </div>

        <div className="mt-8 flex flex-wrap gap-4">

          <button className="flex items-center gap-2 rounded-xl border px-5 py-3 hover:bg-gray-50">
            <Eye size={18} />
            Preview
          </button>

          <button className="flex items-center gap-2 rounded-xl border px-5 py-3 hover:bg-gray-50">
            <Download size={18} />
            Download
          </button>

          <button className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-5 py-3 text-white">
            <Upload size={18} />
            Replace Resume
          </button>

        </div>

      </div>

    </div>
  );
}