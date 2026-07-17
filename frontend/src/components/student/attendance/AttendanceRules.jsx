import { ShieldCheck } from "lucide-react";

export default function AttendanceRules() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center gap-3">
        <ShieldCheck className="text-[#8E1528]" size={24} />

        <div>
          <h2 className="text-xl font-bold">
            Attendance Rules
          </h2>

          <p className="text-sm text-gray-500">
            Eligibility Criteria
          </p>
        </div>
      </div>

      <div className="space-y-5">

        <Rule
          title="Minimum Attendance"
          value="75%"
        />

        <Rule
          title="Current Attendance"
          value="91%"
        />

        <Rule
          title="Exam Eligibility"
          value="Eligible"
          color="text-green-600"
        />

        <Rule
          title="Remaining Allowable Absences"
          value="8 Lectures"
        />

      </div>

    </div>
  );
}

function Rule({ title, value, color = "text-gray-900" }) {
  return (
    <div className="flex items-center justify-between border-b pb-3">

      <p className="text-gray-500">
        {title}
      </p>

      <p className={`font-bold ${color}`}>
        {value}
      </p>

    </div>
  );
}