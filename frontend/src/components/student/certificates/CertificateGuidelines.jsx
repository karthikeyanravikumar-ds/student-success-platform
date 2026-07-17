import {
  FiCheckCircle,
} from "react-icons/fi";

const rules = [
  "Upload only PDF, JPG or PNG files.",
  "Maximum file size: 5 MB.",
  "Faculty verification is mandatory.",
  "Duplicate certificates are not allowed.",
  "Only verified certificates are used for placements.",
];

export default function CertificateGuidelines() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">
        Guidelines
      </h2>

      <div className="mt-8 space-y-5">
        {rules.map((rule) => (
          <div
            key={rule}
            className="flex gap-3"
          >
            <FiCheckCircle className="mt-1 text-green-600" />

            <p>{rule}</p>
          </div>
        ))}
      </div>
    </div>
  );
}