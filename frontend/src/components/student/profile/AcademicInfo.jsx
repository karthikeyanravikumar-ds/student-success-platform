import {
  GraduationCap,
  BookOpen,
  School,
  Calendar,
  Hash,
  BadgeCheck,
} from "lucide-react";

export default function AcademicInfo({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">
        <h2 className="text-xl font-bold text-gray-900">
          Academic Information
        </h2>

        <GraduationCap className="text-[#8E1528]" size={22} />
      </div>

      <div className="grid gap-x-10 gap-y-6 md:grid-cols-2">

        <InfoItem
          icon={<Hash size={18} />}
          label="Roll Number"
          value={student.rollNo}
        />

        <InfoItem
          icon={<BookOpen size={18} />}
          label="Program"
          value={student.program}
        />

        <InfoItem
          icon={<School size={18} />}
          label="Department"
          value={student.department}
        />

        <InfoItem
          icon={<BadgeCheck size={18} />}
          label="Division"
          value={student.division}
        />

        <InfoItem
          icon={<Calendar size={18} />}
          label="Current Semester"
          value={`Semester ${student.semester}`}
        />

        <InfoItem
          icon={<Calendar size={18} />}
          label="Academic Year"
          value={student.academicYear}
        />

        <InfoItem
          icon={<Calendar size={18} />}
          label="Admission Year"
          value={student.admissionYear}
        />

        <InfoItem
          icon={<Calendar size={18} />}
          label="Expected Graduation"
          value={student.graduationYear}
        />

        <InfoItem
          icon={<GraduationCap size={18} />}
          label="Current CGPA"
          value={student.cgpa}
        />

        <InfoItem
          icon={<BookOpen size={18} />}
          label="Credits Earned"
          value={student.credits}
        />

      </div>

    </div>
  );
}

function InfoItem({ icon, label, value }) {
  return (
    <div className="flex items-start gap-4">

      <div className="rounded-xl bg-red-50 p-3 text-[#8E1528]">
        {icon}
      </div>

      <div>
        <p className="text-sm text-gray-500">
          {label}
        </p>

        <p className="mt-1 font-semibold text-gray-900">
          {value}
        </p>
      </div>

    </div>
  );
}