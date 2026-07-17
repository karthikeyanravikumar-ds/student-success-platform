import {
  FiAward,
  FiCalendar,
  FiBookOpen,
  FiBriefcase,
} from "react-icons/fi";

import StatCard from "./StatCard";

export default function DashboardStats() {
  return (
    <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="CGPA"
        value="8.62"
        subtitle="+0.14 from last semester"
        icon={<FiAward className="text-xl text-red-700" />}
      />

      <StatCard
        title="Attendance"
        value="91%"
        subtitle="Excellent attendance"
        icon={<FiCalendar className="text-xl text-red-700" />}
      />

      <StatCard
        title="Credits"
        value="126"
        subtitle="Credits earned"
        icon={<FiBookOpen className="text-xl text-red-700" />}
      />

      <StatCard
        title="Placement"
        value="Eligible"
        subtitle="Ready for placements"
        icon={<FiBriefcase className="text-xl text-red-700" />}
      />

    </div>
  );
}