import { useState } from "react";
import { X, Upload } from "lucide-react";

export default function ApplyLeaveModal({ onClose }) {
  const [formData, setFormData] = useState({
    leaveType: "",
    fromDate: "",
    toDate: "",
    duration: "Full Day",
    reason: "",
    attachment: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleFile = (e) => {
    setFormData((prev) => ({
      ...prev,
      attachment: e.target.files[0],
    }));
  };

  const handleSubmit = () => {
    console.log(formData);

    onClose();
  };

  return (
    <>
      {/* Background */}

      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}

      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div className="flex max-h-[90vh] w-full max-w-3xl flex-col overflow-hidden rounded-3xl bg-white shadow-xl">

          {/* Header */}

          <div className="flex items-center justify-between border-b px-8 py-6">

            <div>

              <h2 className="text-2xl font-bold">
                Apply Leave
              </h2>

              <p className="text-gray-500">
                Submit a new leave request.
              </p>

            </div>

            <button
              onClick={onClose}
              className="rounded-xl p-2 hover:bg-gray-100"
            >
              <X />
            </button>

          </div>

          {/* Body */}

          <div className="flex-1 overflow-y-auto space-y-6 p-8">

            <div className="grid gap-6 md:grid-cols-2">

              <div>

                <label className="mb-2 block text-sm font-medium">
                  Leave Type
                </label>

                <select
                  name="leaveType"
                  value={formData.leaveType}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                >
                  <option value="">Select Leave</option>
                  <option>Medical Leave</option>
                  <option>Personal Leave</option>
                  <option>On Duty</option>
                  <option>Sports</option>
                  <option>NSS / NCC</option>
                  <option>Internship</option>
                </select>

              </div>

              <div>

                <label className="mb-2 block text-sm font-medium">
                  Duration
                </label>

                <select
                  name="duration"
                  value={formData.duration}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                >
                  <option>Full Day</option>
                  <option>Half Day</option>
                </select>

              </div>

              <div>

                <label className="mb-2 block text-sm font-medium">
                  From Date
                </label>

                <input
                  type="date"
                  name="fromDate"
                  value={formData.fromDate}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />

              </div>

              <div>

                <label className="mb-2 block text-sm font-medium">
                  To Date
                </label>

                <input
                  type="date"
                  name="toDate"
                  value={formData.toDate}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />

              </div>

            </div>

            <div>

              <label className="mb-2 block text-sm font-medium">
                Reason
              </label>

              <textarea
                rows="4"
                name="reason"
                value={formData.reason}
                onChange={handleChange}
                className="w-full rounded-xl border px-4 py-3 resize-none"
              />

            </div>

            <div>

              <label className="mb-3 block text-sm font-medium">
                Attachment (Optional)
              </label>

              <label className="flex cursor-pointer items-center gap-3 rounded-xl border border-dashed p-5 hover:bg-gray-50">

                <Upload />

                <span>

                  {formData.attachment
                    ? formData.attachment.name
                    : "Choose Supporting Document"}

                </span>

                <input
                  type="file"
                  hidden
                  onChange={handleFile}
                />

              </label>

            </div>

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
              onClick={handleSubmit}
              className="rounded-xl bg-[#8E1528] px-6 py-3 text-white hover:bg-[#73111f]"
            >
              Submit Request
            </button>

          </div>

        </div>

      </div>

    </>
  );
}