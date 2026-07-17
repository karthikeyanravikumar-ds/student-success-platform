import { FiMonitor, FiSmartphone, FiX } from "react-icons/fi";

const sessions = [
  {
    id: 1,
    device: "Windows 11",
    browser: "Google Chrome",
    location: "Mumbai, India",
    lastActive: "Active Now",
    current: true,
    icon: <FiMonitor />,
  },
  {
    id: 2,
    device: "Android",
    browser: "Chrome Mobile",
    location: "Mumbai, India",
    lastActive: "2 hours ago",
    current: false,
    icon: <FiSmartphone />,
  },
  {
    id: 3,
    device: "Windows 10",
    browser: "Microsoft Edge",
    location: "Pune, India",
    lastActive: "Yesterday",
    current: false,
    icon: <FiMonitor />,
  },
];

export default function ActiveSessionsModal({
  isOpen,
  onClose,
}) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center overflow-y-auto bg-black/40 p-6">

      <div className="my-8 w-full max-w-2xl rounded-2xl bg-white shadow-2xl max-h-[90vh] overflow-y-auto">

        <div className="flex items-center justify-between border-b px-6 py-5">

          <h2 className="text-2xl font-bold">
            Active Sessions
          </h2>

          <button
            onClick={onClose}
            className="rounded-lg p-2 hover:bg-gray-100"
          >
            <FiX size={20} />
          </button>

        </div>

        <div className="p-6 space-y-4">

          {sessions.map((session) => (
            <div
              key={session.id}
              className="rounded-xl border p-4 flex justify-between items-center"
            >
              <div className="flex gap-4">

                <div className="flex h-12 w-12 items-center justify-center rounded-full bg-red-100 text-[#8E1528] text-xl">
                  {session.icon}
                </div>

                <div>

                  <h3 className="font-semibold">
                    {session.device}
                  </h3>

                  <p className="text-sm text-gray-500">
                    {session.browser}
                  </p>

                  <p className="text-sm text-gray-500">
                    {session.location}
                  </p>

                </div>

              </div>

              <div className="text-right">

                {session.current ? (
                  <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
                    Current Session
                  </span>
                ) : (
                  <span className="text-sm text-gray-500">
                    {session.lastActive}
                  </span>
                )}

              </div>

            </div>
          ))}

        </div>

        <div className="flex justify-end gap-3 border-t px-6 py-5">

          <button className="rounded-xl border px-5 py-2 hover:bg-gray-100">
            Logout Other Devices
          </button>

          <button
            onClick={onClose}
            className="rounded-xl bg-[#8E1528] px-5 py-2 text-white hover:bg-[#731120]"
          >
            Close
          </button>

        </div>

      </div>

    </div>
  );
}