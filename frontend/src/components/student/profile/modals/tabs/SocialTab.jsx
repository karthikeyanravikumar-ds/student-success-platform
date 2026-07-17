export default function SocialTab({
  formData,
  setFormData,
}) {
  return (
    <div className="grid grid-cols-1 gap-6">

      <div>
        <label className="mb-2 block text-sm font-medium">
          LinkedIn
        </label>

        <input
          defaultValue={formData.linkedin}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          GitHub
        </label>

        <input
          defaultValue={formData.github}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          Portfolio
        </label>

        <input
          defaultValue={formData.portfolio}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          LeetCode
        </label>

        <input
          defaultValue={formData.leetcode}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

      <div>
        <label className="mb-2 block text-sm font-medium">
          HackerRank
        </label>

        <input
          defaultValue={formData.hackerrank}
          className="w-full rounded-xl border border-gray-300 px-4 py-3"
        />
      </div>

    </div>
  );
}