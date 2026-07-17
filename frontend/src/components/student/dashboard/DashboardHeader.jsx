import PageHeader from "../../ui/PageHeader";

export default function DashboardHeader({ student }) {
  return (
    <div className="mb-8">
      <PageHeader
        title={`Good Morning, ${student?.full_name || "Student"}`}
        subtitle="Welcome back! Here's your academic overview for today."
      />

      <div className="mt-6 flex flex-wrap gap-3">
        <span className="rounded-full border bg-white px-4 py-2 text-sm shadow-sm">
          Roll No : {student?.roll_no || "-"}
        </span>

        <span className="rounded-full border bg-white px-4 py-2 text-sm shadow-sm">
          Semester : {student?.current_semester || "-"}
        </span>

        <span className="rounded-full border bg-white px-4 py-2 text-sm shadow-sm">
          Admission : {student?.admission_year || "-"}
        </span>

        <span className="rounded-full border bg-white px-4 py-2 text-sm shadow-sm">
          Graduation : {student?.graduation_year || "-"}
        </span>
      </div>
    </div>
  );
}