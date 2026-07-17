export default function ParentTab({
  formData,
  setFormData,
}) {
  return (
    <div className="space-y-8">

      {/* Father */}
      <div>

        <h3 className="mb-5 text-lg font-semibold">
          Father Information
        </h3>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              Father's Name
            </label>

            <input
              defaultValue={formData.fatherName}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Occupation
            </label>

            <input
              defaultValue={formData.fatherOccupation}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

        </div>

      </div>

      {/* Mother */}

      <div>

        <h3 className="mb-5 text-lg font-semibold">
          Mother Information
        </h3>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              Mother's Name
            </label>

            <input
              defaultValue={formData.motherName}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Occupation
            </label>

            <input
              defaultValue={formData.motherOccupation}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

        </div>

      </div>

      {/* Contact */}

      <div>

        <h3 className="mb-5 text-lg font-semibold">
          Parent Contact
        </h3>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              Parent Phone
            </label>

            <input
              defaultValue={formData.parentPhone}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Parent Email
            </label>

            <input
              defaultValue={formData.parentEmail}
              className="w-full rounded-xl border border-gray-300 px-4 py-3"
            />
          </div>

        </div>

      </div>

      <div className="rounded-xl bg-yellow-50 p-4 text-sm text-yellow-800">
        Changes to parent information may require approval from the college administration.
      </div>

    </div>
  );
}