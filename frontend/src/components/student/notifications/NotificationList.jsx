import NotificationItem from "./NotificationItem";

const notifications = [
  {
    id: 1,
    type: "placement",
    title: "TCS Placement Drive Open",
    message: "Applications are now open for Data Analyst positions.",
    time: "10 minutes ago",
    action: "Apply",
    read: false,
  },
  {
    id: 2,
    type: "results",
    title: "Semester V Result Published",
    message: "Your semester result has been published.",
    time: "2 hours ago",
    action: "Download",
    read: false,
  },
  {
    id: 3,
    type: "certificate",
    title: "Certificate Verified",
    message: "AWS Cloud Foundations certificate has been verified.",
    time: "Yesterday",
    action: "View",
    read: true,
  },
  {
    id: 4,
    type: "attendance",
    title: "Attendance Updated",
    message: "Attendance has been updated for today's lectures.",
    time: "Yesterday",
    action: "View",
    read: true,
  },
  {
    id: 5,
    type: "examination",
    title: "Hall Ticket Available",
    message: "Semester V Hall Ticket is ready for download.",
    time: "2 days ago",
    action: "Download",
    read: true,
  },
];

export default function NotificationList() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-2xl font-bold">
            Notifications
          </h2>

          <p className="text-gray-500">
            Latest updates from the platform
          </p>
        </div>

      </div>

      {notifications.map((notification) => (
        <NotificationItem
          key={notification.id}
          notification={notification}
        />
      ))}

    </div>
  );
}