import { useState } from "react";

export default function NotificationSettings() {
  const [settings, setSettings] = useState({
    email: true,
    sms: false,
    push: true,
    placement: true,
    attendance: true,
    results: true,
    exams: true,
    certificates: true,
  });

  const toggle = (key) => {
    setSettings((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const options = [
    {
      label: "Email Notifications",
      description: "Receive important updates by email.",
      key: "email",
    },
    {
      label: "SMS Notifications",
      description: "Receive urgent SMS alerts.",
      key: "sms",
    },
    {
      label: "Push Notifications",
      description: "Receive browser notifications.",
      key: "push",
    },
    {
      label: "Placement Alerts",
      description: "Placement drives and company updates.",
      key: "placement",
    },
    {
      label: "Attendance Alerts",
      description: "Attendance shortage and updates.",
      key: "attendance",
    },
    {
      label: "Result Notifications",
      description: "Semester result announcements.",
      key: "results",
    },
    {
      label: "Examination Alerts",
      description: "Exam schedules and hall tickets.",
      key: "exams",
    },
    {
      label: "Certificate Verification",
      description: "Faculty certificate approval updates.",
      key: "certificates",
    },
  ];

  return (
    <section className="rounded-2xl border border-gray-200 bg-white">
      <div className="border-b px-8 py-6">
        <h2 className="text-2xl font-bold text-gray-900">
          Notification Preferences
        </h2>

        <p className="mt-1 text-gray-500">
          Choose how you'd like to receive notifications.
        </p>
      </div>

      <div>

        {options.map((item, index) => (

          <div
            key={item.key}
            className={`flex items-center justify-between px-8 py-5 ${
              index !== options.length - 1
                ? "border-b border-gray-100"
                : ""
            }`}
          >

            <div>

              <h3 className="font-semibold text-gray-900">
                {item.label}
              </h3>

              <p className="mt-1 text-sm text-gray-500">
                {item.description}
              </p>

            </div>

            <button
              onClick={() => toggle(item.key)}
              className={`relative h-7 w-14 rounded-full transition ${
                settings[item.key]
                  ? "bg-[#8E1528]"
                  : "bg-gray-300"
              }`}
            >

              <span
                className={`absolute top-1 h-5 w-5 rounded-full bg-white transition-all ${
                  settings[item.key]
                    ? "left-8"
                    : "left-1"
                }`}
              />

            </button>

          </div>

        ))}

      </div>
    </section>
  );
}