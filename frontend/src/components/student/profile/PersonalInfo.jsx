import {
  User,
  Calendar,
  Heart,
  Flag,
  BadgeCheck,
  IdCard,
} from "lucide-react";

export default function PersonalInfo({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">
        <h2 className="text-xl font-bold text-gray-900">
          Personal Information
        </h2>

        <User className="text-[#8E1528]" size={22} />
      </div>

      <div className="grid gap-x-10 gap-y-6 md:grid-cols-2">

        <InfoItem
          icon={<User size={18} />}
          label="Full Name"
          value={student.fullName}
        />

        <InfoItem
          icon={<BadgeCheck size={18} />}
          label="Gender"
          value={student.gender}
        />

        <InfoItem
          icon={<Calendar size={18} />}
          label="Date of Birth"
          value={student.dob}
        />

        <InfoItem
          icon={<Heart size={18} />}
          label="Blood Group"
          value={student.bloodGroup}
        />

        <InfoItem
          icon={<Flag size={18} />}
          label="Nationality"
          value={student.nationality}
        />

        <InfoItem
          icon={<IdCard size={18} />}
          label="Aadhaar Number"
          value={student.aadhaar}
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

        <p className="mt-1 text-lg font-semibold text-gray-900 break-all">
          {value}
        </p>

      </div>

    </div>
  );
}