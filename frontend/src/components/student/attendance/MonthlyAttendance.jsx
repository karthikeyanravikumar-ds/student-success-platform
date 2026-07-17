const months = [
  ["Jan", "92%"],
  ["Feb", "95%"],
  ["Mar", "90%"],
  ["Apr", "88%"],
  ["May", "93%"],
  ["Jun", "91%"],
];

export default function MonthlyAttendance() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-bold">
        Monthly Attendance
      </h2>

      <div className="space-y-4">
        {months.map(([month, value]) => (
          <div key={month}>
            <div className="mb-1 flex justify-between">
              <span>{month}</span>
              <span>{value}</span>
            </div>

            <div className="h-3 rounded-full bg-gray-200">
              <div
                className="h-3 rounded-full bg-[#8E1528]"
                style={{ width: value }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}