import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import Login from "../pages/auth/Login";
import StudentDashboard from "../pages/student/StudentDashboard";
import FacultyDashboard from "../pages/faculty/FacultyDashboard";
import PlacementDashboard from "../pages/placement/PlacementDashboard";
import AdminDashboard from "../pages/admin/AdminDashboard";
import StudentProfile from "../pages/student/StudentProfile";
import Attendance from "../pages/student/Attendance";
import Subjects from "../pages/student/Subjects";
import Results from "../pages/student/Results";
import Examinations from "../pages/student/Examinations";
import Placement from "../pages/student/Placement";
import Certificates from "../pages/student/Certificates";
import Projects from "../pages/student/Projects";
import Notifications from "../pages/student/Notifications";
import Settings from "../pages/student/Settings";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Redirect */}
        <Route path="/" element={<Navigate to="/login" replace />} />

        {/* Login */}
        <Route path="/login" element={<Login />} />

        {/* Dashboard Layout */}
        <Route element={<DashboardLayout />}>
          <Route path="/student" element={<StudentDashboard />} />
          <Route path="/faculty" element={<FacultyDashboard />} />
          <Route path="/placement" element={<PlacementDashboard />} />
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/student/profile" element={<StudentProfile />} />
          <Route path="/student/attendance" element={<Attendance />} />
          <Route path="/student/subjects" element={<Subjects />} />
          <Route path="/student/results" element={<Results />} />
          <Route path="/student/exams" element={<Examinations />} />
          <Route path="/student/placement" element={<Placement />} />
          <Route path="/student/certificates" element={<Certificates />} />
          <Route path="/student/projects" element={<Projects />} />
          <Route path="/student/notifications" element={<Notifications />} />
          <Route path="/student/settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}