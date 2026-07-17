export default function CertificateStatistics() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">
        Certificate Statistics
      </h2>

      <div className="mt-10 flex justify-center">
        <div className="flex h-52 w-52 items-center justify-center rounded-full border-[20px] border-green-600 border-r-red-500 border-b-orange-400">
          <span className="text-3xl font-bold">
            18
          </span>
        </div>
      </div>

      <div className="mt-8 space-y-4">
        <div className="flex justify-between">
          <span>Verified</span>
          <span>14</span>
        </div>

        <div className="flex justify-between">
          <span>Pending</span>
          <span>3</span>
        </div>

        <div className="flex justify-between">
          <span>Rejected</span>
          <span>1</span>
        </div>
      </div>
    </div>
  );
}