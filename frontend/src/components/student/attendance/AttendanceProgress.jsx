export default function AttendanceProgress({ percentage }) {
  return (
    <div className="bg-white rounded-2xl shadow-sm p-6">

      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold">
          Overall Attendance
        </h2>

        <span className="text-2xl font-bold text-green-600">
          {percentage}%
        </span>
      </div>

      <div className="w-full bg-gray-200 rounded-full h-4 mt-6">

        <div
          className="bg-green-600 h-4 rounded-full transition-all duration-500"
          style={{ width: `${percentage}%` }}
        />

      </div>

      <p className="text-gray-500 mt-4">
        Excellent attendance. Keep maintaining above 90%.
      </p>

    </div>
  );
}