import { useState } from "react";
import { FiX, FiUpload } from "react-icons/fi";

export default function UploadCertificateModal({
    certificates,
    setCertificates,
    onClose,
}) {
  const [formData, setFormData] = useState({
    title: "",
    category: "",
    issueDate: "",
    issuer: "",
    file: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <>
      {/* Overlay */}
      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">

        <div className="flex max-h-[90vh] w-full max-w-2xl flex-col overflow-hidden rounded-3xl bg-white shadow-xl">

          {/* Header */}
          <div className="flex items-center justify-between border-b px-8 py-6">

            <div>
              <h2 className="text-2xl font-bold">
                Upload Certificate
              </h2>

              <p className="text-gray-500">
                Upload a certificate for faculty verification.
              </p>
            </div>

            <button
              onClick={onClose}
              className="rounded-lg p-2 hover:bg-gray-100"
            >
              <FiX size={22} />
            </button>

          </div>

          {/* Body */}
          <div className="flex-1 space-y-6 overflow-y-auto p-8">

            <div>

              <label className="mb-2 block text-sm font-medium">
                Certificate Title
              </label>

              <input
                name="title"
                value={formData.title}
                onChange={handleChange}
                className="w-full rounded-xl border px-4 py-3"
              />

            </div>

            <div className="grid gap-6 md:grid-cols-2">

              <div>

                <label className="mb-2 block text-sm font-medium">
                  Category
                </label>

                <select
                  name="category"
                  value={formData.category}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                >
                  <option value="">Select</option>
                  <option>Internship</option>
                  <option>Workshop</option>
                  <option>Course</option>
                  <option>Hackathon</option>
                  <option>Sports</option>
                  <option>Achievement</option>
                  <option>Other</option>
                </select>

              </div>

              <div>

                <label className="mb-2 block text-sm font-medium">
                  Issue Date
                </label>

                <input
                  type="date"
                  name="issueDate"
                  value={formData.issueDate}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />

              </div>

            </div>

            <div>

              <label className="mb-2 block text-sm font-medium">
                Issued By
              </label>

              <input
                name="issuer"
                value={formData.issuer}
                onChange={handleChange}
                className="w-full rounded-xl border px-4 py-3"
              />

            </div>

            <label className="flex cursor-pointer items-center gap-3 rounded-xl border-2 border-dashed p-6 hover:bg-gray-50">

              <FiUpload size={24} />

              <span>
                {formData.file
                  ? formData.file.name
                  : "Choose PDF / JPG / PNG"}
              </span>

              <input
                hidden
                type="file"
                accept=".pdf,.jpg,.jpeg,.png"
                onChange={(e) =>
                  setFormData((prev) => ({
                    ...prev,
                    file: e.target.files[0],
                  }))
                }
              />

            </label>

          </div>

          {/* Footer */}
          <div className="flex justify-end gap-4 border-t px-8 py-6">

            <button
              onClick={onClose}
              className="rounded-xl border px-6 py-3"
            >
              Cancel
            </button>

            <button
  onClick={() => {
    const newCertificate = {
      id: Date.now(),
      name: formData.title,
      category: formData.category,
      date: new Date().toLocaleDateString("en-GB"),
      status: "Pending",
      file: formData.file,
    };

    setCertificates([
      newCertificate,
      ...certificates,
    ]);

    onClose();
  }}
  className="rounded-xl bg-red-800 px-6 py-3 text-white"
>
  Upload Certificate
</button>

          </div>

        </div>

      </div>
    </>
  );
}