export default function AttendanceWarning({ subjects }) {
  const lowAttendance = subjects.filter(
    (subject) => subject.attendance < 75
  );

  if (lowAttendance.length === 0) {
    return (
      <div className="bg-green-50 border border-green-200 rounded-2xl p-6">
        <h2 className="text-xl font-semibold text-green-700">
          Great Job!
        </h2>

        <p className="mt-2 text-green-600">
          You have no attendance shortage.
        </p>
      </div>
    );
  }

  return (
    <div className="bg-red-50 border border-red-200 rounded-2xl p-6">
      <h2 className="text-xl font-semibold text-red-700">
        Attendance Warning
      </h2>

      <ul className="mt-4 space-y-2">
        {lowAttendance.map((subject) => (
          <li key={subject.name}>
            {subject.name} — {subject.attendance}%
          </li>
        ))}
      </ul>
    </div>
  );
}