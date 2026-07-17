import { CheckCheck } from "lucide-react";

export default function NotificationToolbar() {
  return (
    <div className="mb-6 flex items-center justify-between rounded-3xl border border-gray-200 bg-white p-6 shadow-sm">
      <div>
        <h2 className="text-2xl font-bold">
          28 Notifications
        </h2>

        <p className="mt-1 text-gray-500">
          7 Unread • 2 Important
        </p>
      </div>

      <button className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-5 py-3 font-medium text-white transition hover:bg-[#73111f]">
        <CheckCheck size={18} />
        Mark all as read
      </button>
    </div>
  );
}