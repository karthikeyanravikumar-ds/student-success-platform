import { useState } from "react";
import {
  FiEye,
  FiUsers,
  FiBookOpen,
  FiShield,
} from "react-icons/fi";

export default function PrivacySettings() {
  const [privacy, setPrivacy] = useState({
    profile: true,
    classmates: true,
    academic: false,
    analytics: true,
  });

  const toggle = (key) => {
    setPrivacy((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const items = [
    {
      key: "profile",
      icon: <FiEye className="text-2xl text-[#8E1528]" />,
      title: "Profile Visibility",
      description: "Allow faculty and authorized staff to view your profile.",
    },
    {
      key: "classmates",
      icon: <FiUsers className="text-2xl text-blue-600" />,
      title: "Class Directory",
      description: "Display your name in the student directory.",
    },
    {
      key: "academic",
      icon: <FiBookOpen className="text-2xl text-green-600" />,
      title: "Academic Record Sharing",
      description: "Share academic achievements for placement purposes.",
    },
    {
      key: "analytics",
      icon: <FiShield className="text-2xl text-purple-600" />,
      title: "Usage Analytics",
      description: "Help improve the platform with anonymous usage data.",
    },
  ];

  return (
    <section className="rounded-2xl border border-gray-200 bg-white">

      <div className="border-b px-8 py-6">
        <h2 className="text-2xl font-bold">
          Privacy
        </h2>

        <p className="mt-1 text-gray-500">
          Control who can access your information.
        </p>
      </div>

      {items.map((item, index) => (
        <div
          key={item.key}
          className={`flex items-center justify-between px-8 py-5 ${
            index !== items.length - 1
              ? "border-b border-gray-100"
              : ""
          }`}
        >
          <div className="flex items-center gap-4">

            {item.icon}

            <div>

              <h3 className="font-semibold">
                {item.title}
              </h3>

              <p className="mt-1 text-sm text-gray-500">
                {item.description}
              </p>

            </div>

          </div>

          <button
            onClick={() => toggle(item.key)}
            className={`relative h-7 w-14 rounded-full transition ${
              privacy[item.key]
                ? "bg-[#8E1528]"
                : "bg-gray-300"
            }`}
          >
            <span
              className={`absolute top-1 h-5 w-5 rounded-full bg-white transition-all ${
                privacy[item.key]
                  ? "left-8"
                  : "left-1"
              }`}
            />
          </button>

        </div>
      ))}

    </section>
  );
}