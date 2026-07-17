export default function PersonalTab({
  formData,
  setFormData,
}) {
  return (
    <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

      <div>
        <label className="mb-2 block text-sm font-medium">
          Full Name
        </label>

        <input
          value={formData.fullName}
  onChange={(e) =>
    setFormData({
      ...formData,
      fullName: e.target.value,
    })
  }
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Gender
        </label>

        <select
          defaultValue={formData.gender}
          className="w-full rounded-xl border border-gray-300 px-4 py-3 focus:border-[#8E1528] focus:outline-none"
        >
          <option>Male</option>
          <option>Female</option>
          <option>Other</option>
        </select>
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Date of Birth
        </label>

        <input
          type="date"
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Blood Group
        </label>

        <input
          defaultValue={formData.bloodGroup}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Nationality
        </label>

        <input
          defaultValue={formData.nationality}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

    </div>
  );
}