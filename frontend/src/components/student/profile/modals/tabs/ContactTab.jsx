export default function ContactTab({
  formData,
  setFormData,
}) {
  return (
    <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

      <div>
        <label className="mb-2 block text-sm font-medium">
          Email Address
        </label>

        <input
          type="email"
          defaultValue={formData.email}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Mobile Number
        </label>

        <input
          defaultValue={formData.phone}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Emergency Contact
        </label>

        <input
          defaultValue={formData.emergencyContact}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          City
        </label>

        <input
          defaultValue={formData.city}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

      <div className="md:col-span-2">
        <label className="mb-2 block text-sm font-medium">
          Address
        </label>

        <textarea
          rows={3}
          defaultValue={formData.address}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none resize-none"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          State
        </label>

        <input
          defaultValue={formData.state}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

    </div>
  );
}