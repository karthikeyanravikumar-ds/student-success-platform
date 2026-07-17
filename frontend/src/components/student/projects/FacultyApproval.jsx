export default function FacultyApproval() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-2xl font-bold">
        Faculty Approval
      </h2>

      <div className="mt-6 flex items-center justify-between rounded-xl border p-5">
        <div>
          <h3 className="font-semibold">
            Project Guide
          </h3>

          <p className="text-gray-500">
            Approved
          </p>
        </div>

        <span className="rounded-full bg-green-100 px-4 py-2 text-green-700">
          Verified
        </span>
      </div>
    </div>
  );
}