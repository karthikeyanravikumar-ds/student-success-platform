import {
  Users,
  User,
  Briefcase,
  Phone,
  Mail,
} from "lucide-react";

export default function ParentInfo({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm h-fit">

      <div className="mb-6 flex items-center justify-between">
        <h2 className="text-xl font-bold text-gray-900">
          Parent Information
        </h2>

        <Users className="text-[#8E1528]" size={22} />
      </div>

      <div className="space-y-4">

        <InfoItem
          icon={<User size={18} />}
          label="Father's Name"
          value={student.fatherName}
        />

        <InfoItem
          icon={<Briefcase size={18} />}
          label="Father's Occupation"
          value={student.fatherOccupation}
        />

        <InfoItem
          icon={<User size={18} />}
          label="Mother's Name"
          value={student.motherName}
        />

        <InfoItem
          icon={<Briefcase size={18} />}
          label="Mother's Occupation"
          value={student.motherOccupation}
        />

        <InfoItem
          icon={<Phone size={18} />}
          label="Parent Contact"
          value={student.parentPhone}
        />

        <InfoItem
          icon={<Mail size={18} />}
          label="Parent Email"
          value={student.parentEmail}
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

        <p className="mt-1 text-lg font-semibold text-gray-900 truncate">
          {value}
        </p>
      </div>

    </div>
  );
}