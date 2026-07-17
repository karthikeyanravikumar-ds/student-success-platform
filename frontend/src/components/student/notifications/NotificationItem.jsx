import {
  Bell,
  Briefcase,
  GraduationCap,
  Award,
  Calendar,
  CheckCircle,
  Download,
  Eye,
} from "lucide-react";

function getIcon(type) {
  switch (type) {
    case "placement":
      return <Briefcase className="h-6 w-6 text-blue-600" />;

    case "results":
      return <GraduationCap className="h-6 w-6 text-green-600" />;

    case "certificate":
      return <Award className="h-6 w-6 text-yellow-600" />;

    case "attendance":
      return <CheckCircle className="h-6 w-6 text-emerald-600" />;

    case "examination":
      return <Calendar className="h-6 w-6 text-red-600" />;

    default:
      return <Bell className="h-6 w-6 text-gray-600" />;
  }
}

export default function NotificationItem({ notification }) {
  const handleAction = () => {
    switch (notification.action) {
      case "Download":
        window.open("/documents/Semester-V-Marksheet.pdf", "_blank");
        break;

      case "Apply":
        window.location.href = "/student/placement";
        break;

      case "View":
        alert(notification.title);
        break;

      default:
        break;
    }
  };

  return (
    <div className="group flex items-start justify-between border-b border-gray-100 py-4 transition hover:bg-gray-50 last:border-b-0">
      {/* Left Section */}
      <div className="flex items-start gap-4">
        {/* Unread Dot */}
        {!notification.read && (
          <div className="mt-5 h-3 w-3 rounded-full bg-blue-600" />
        )}

        {/* Icon */}
        <div
          className={`flex h-14 w-14 items-center justify-center rounded-2xl ${
            notification.type === "placement"
              ? "bg-blue-50"
              : notification.type === "results"
              ? "bg-green-50"
              : notification.type === "certificate"
              ? "bg-yellow-50"
              : notification.type === "attendance"
              ? "bg-emerald-50"
              : "bg-red-50"
          }`}
        >
          {getIcon(notification.type)}
        </div>

        {/* Notification Content */}
        <div>
          <span className="mb-2 inline-block rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-gray-500">
            {notification.type}
          </span>

          <h3 className="text-lg font-semibold text-gray-900">
            {notification.title}
          </h3>

          <p className="mt-1 text-gray-600">
            {notification.message}
          </p>

          <p className="mt-2 text-sm text-gray-400">
            {notification.time}
          </p>
        </div>
      </div>

      {/* Action Button */}
      <button
        onClick={handleAction}
        className="flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium transition hover:border-[#8E1528] hover:text-[#8E1528]"
      >
        {notification.action === "Download" && <Download size={16} />}
        {notification.action === "View" && <Eye size={16} />}
        {notification.action}
      </button>
    </div>
  );
}