export default function AttendanceChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="text-lg font-semibold text-gray-900">
        Attendance Overview
      </h2>

      <p className="mt-1 text-sm text-gray-500">
        Subject-wise attendance summary
      </p>

      <div className="mt-6 space-y-4">
        <div className="flex justify-between">
          <span>Python</span>
          <span className="font-semibold text-green-600">95%</span>
        </div>

        <div className="flex justify-between">
          <span>Machine Learning</span>
          <span className="font-semibold text-green-600">89%</span>
        </div>

        <div className="flex justify-between">
          <span>Statistics</span>
          <span className="font-semibold text-yellow-600">82%</span>
        </div>

        <div className="flex justify-between">
          <span>DBMS</span>
          <span className="font-semibold text-green-600">91%</span>
        </div>
      </div>
    </div>
  );
}