import {
  FiHome,
  FiUser,
  FiCalendar,
  FiBook,
  FiFileText,
  FiBriefcase,
  FiBell,
  FiSettings,
  FiLogOut,
  FiClipboard,
  FiAward,
} from "react-icons/fi";

export const navigation = [
  {
    title: "MAIN",
    items: [
      { name: "Dashboard", icon: FiHome, path: "/student" },
    ],
  },
  {
    title: "ACADEMICS",
    items: [
      { name: "My Profile", icon: FiUser, path: "/student/profile" },
      { name: "Attendance", icon: FiCalendar, path: "/student/attendance" },
      { name: "Subjects", icon: FiBook, path: "/student/subjects" },
      { name: "Results", icon: FiClipboard, path: "/student/results" },
      { name: "Examinations", icon: FiFileText, path: "/student/exams" },
      { name: "Certificates", icon: FiAward, path: "/student/certificates" },
      { name: "Projects", icon: FiAward, path: "/student/projects" },
    ],
  },
  {
    title: "PLACEMENT",
    items: [
      { name: "Opportunities", icon: FiBriefcase, path: "/student/placement" },
    ],
  },
  {
    title: "OTHERS",
    items: [
      { name: "Notifications", icon: FiBell, path: "/student/notifications" },
      { name: "Settings", icon: FiSettings, path: "/student/settings" },
      { name: "Logout", icon: FiLogOut, path: "/student/logout" },
    ],
  },
];