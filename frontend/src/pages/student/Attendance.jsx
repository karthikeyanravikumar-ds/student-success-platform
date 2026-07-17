import PageContainer from "../../layouts/PageContainer";

import AttendanceSummary from "../../components/student/attendance/AttendanceSummary";
import AttendanceChart from "../../components/student/attendance/AttendanceChart";
import SubjectAttendance from "../../components/student/attendance/SubjectAttendance";
import MonthlyAttendance from "../../components/student/attendance/MonthlyAttendance";
import LeaveRequests from "../../components/student/attendance/LeaveRequests";
import AttendanceRules from "../../components/student/attendance/AttendanceRules";
import TodayClasses from "../../components/student/attendance/TodayClasses";

export default function Attendance() {
  return (
    <PageContainer>

      <div className="mb-8">
        <h1 className="text-3xl font-bold">Attendance</h1>
        <p className="text-gray-500">
          Track your attendance across all subjects.
        </p>
      </div>

      <AttendanceSummary />

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <AttendanceChart />
        <MonthlyAttendance />
      </div>

      <div className="mt-8">
        <SubjectAttendance />
      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">
        <AttendanceRules />
        <TodayClasses />
      </div>

      <div className="mt-8">
        <LeaveRequests />
      </div>

    </PageContainer>
  );
}