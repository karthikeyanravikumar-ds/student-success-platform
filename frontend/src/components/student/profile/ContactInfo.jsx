import {
  Mail,
  Phone,
  MapPin,
  ShieldAlert,
  Building2,
  Map,
} from "lucide-react";

export default function ContactInfo({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm h-fit">
      <div className="mb-6 flex items-center justify-between">
        <h2 className="text-xl font-bold text-gray-900">
          Contact Information
        </h2>

        <Mail className="text-[#8E1528]" size={22} />
      </div>

      <div className="space-y-4">

        <InfoItem
          icon={<Mail size={18} />}
          label="Email Address"
          value={student.email}
        />

        <InfoItem
          icon={<Phone size={18} />}
          label="Mobile Number"
          value={student.phone}
        />

        <InfoItem
          icon={<ShieldAlert size={18} />}
          label="Emergency Contact"
          value={student.emergencyContact}
        />

        <InfoItem
          icon={<MapPin size={18} />}
          label="Address"
          value={student.address}
        />

        <InfoItem
          icon={<Building2 size={18} />}
          label="City"
          value={student.city}
        />

        <InfoItem
          icon={<Map size={18} />}
          label="State"
          value={student.state}
        />

      </div>
    </div>
  );
}

function InfoItem({ icon, label, value }) {
  return (
    <div className="flex items-start gap-4 min-w-0">

      <div className="rounded-xl bg-red-50 p-3 text-[#8E1528] shrink-0">
        {icon}
      </div>

      <div className="flex-1 min-w-0">

        <p className="text-sm text-gray-500">
          {label}
        </p>

        <p
          className="mt-1 font-semibold text-gray-900 break-all"
          title={value}
        >
          {value}
        </p>

      </div>

    </div>
  );
}