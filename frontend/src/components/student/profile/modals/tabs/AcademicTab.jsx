import { Lock } from "lucide-react";

export default function AcademicTab({ formData }) {
  const fields = [
    { label: "Roll Number", value: formData.rollNo },
    { label: "Program", value: formData.program },
    { label: "Department", value: formData.department },
    { label: "Division", value: formData.division },
    { label: "Semester", value: formData.semester },
    { label: "Academic Year", value: formData.academicYear },
    { label: "Admission Year", value: formData.admissionYear },
    { label: "Graduation Year", value: formData.graduationYear },
    { label: "Credits", value: formData.credits },
    { label: "CGPA", value: formData.cgpa },
  ];

  return (
    <div>

      <div className="mb-8 flex items-center gap-3 rounded-xl bg-amber-50 p-4 text-amber-700">
        <Lock size={18} />
        <p className="text-sm">
          Academic information is managed by the college and cannot be edited.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

        {fields.map((field) => (
          <div key={field.label}>
            <label className="mb-2 block text-sm font-medium text-gray-500">
              {field.label}
            </label>

            <div className="rounded-xl bg-gray-100 px-4 py-3 font-medium">
              {field.value}
            </div>
          </div>
        ))}

      </div>

    </div>
  );
}