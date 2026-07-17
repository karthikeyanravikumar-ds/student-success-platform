import { useState, useEffect } from "react";
import { FiX } from "react-icons/fi";

export default function EditProfileModal({
  isOpen,
  onClose,
  student,
  onSave,
}) {
  const [formData, setFormData] = useState(student);

  useEffect(() => {
    setFormData(student);
  }, [student]);

  if (!isOpen) return null;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = () => {
    onSave(formData);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">

      <div className="w-full max-w-2xl rounded-2xl bg-white shadow-2xl">

        {/* Header */}

        <div className="flex items-center justify-between border-b px-6 py-5">

          <h2 className="text-2xl font-bold">
            Edit Profile
          </h2>

          <button
            onClick={onClose}
            className="rounded-lg p-2 hover:bg-gray-100"
          >
            <FiX size={22} />
          </button>

        </div>

        {/* Form */}

        <div className="grid gap-5 p-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              Full Name
            </label>

            <input
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full rounded-xl border p-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Roll Number
            </label>

            <input
              value={formData.roll}
              disabled
              className="w-full rounded-xl border bg-gray-100 p-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Email
            </label>

            <input
              value={formData.email}
              disabled
              className="w-full rounded-xl border bg-gray-100 p-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Phone
            </label>

            <input
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              className="w-full rounded-xl border p-3"
            />
          </div>

          <div className="md:col-span-2">
            <label className="mb-2 block text-sm font-medium">
              Department
            </label>

            <input
              name="department"
              value={formData.department}
              onChange={handleChange}
              className="w-full rounded-xl border p-3"
            />
          </div>

        </div>

        {/* Footer */}

        <div className="flex justify-end gap-3 border-t px-6 py-5">

          <button
            onClick={onClose}
            className="rounded-xl border px-5 py-2 hover:bg-gray-100"
          >
            Cancel
          </button>

          <button
            onClick={handleSubmit}
            className="rounded-xl bg-[#8E1528] px-5 py-2 text-white hover:bg-[#731120]"
          >
            Save Changes
          </button>

        </div>

      </div>

    </div>
  );
}