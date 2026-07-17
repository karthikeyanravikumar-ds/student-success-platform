import {
  Linkedin,
  Github,
  Globe,
  Code2,
  Trophy,
  ExternalLink,
} from "lucide-react";

export default function SocialLinks({ student }) {
  const links = [
    {
      title: "LinkedIn",
      value: student.linkedin,
      icon: <Linkedin size={20} />,
      color: "text-blue-600",
    },
    {
      title: "GitHub",
      value: student.github,
      icon: <Github size={20} />,
      color: "text-gray-900",
    },
    {
      title: "Portfolio",
      value: student.portfolio,
      icon: <Globe size={20} />,
      color: "text-green-600",
    },
    {
      title: "LeetCode",
      value: student.leetcode,
      icon: <Code2 size={20} />,
      color: "text-yellow-600",
    },
    {
      title: "HackerRank",
      value: student.hackerrank,
      icon: <Trophy size={20} />,
      color: "text-emerald-600",
    },
  ];

  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-xl font-bold text-gray-900">
            Social Links
          </h2>

          <p className="text-sm text-gray-500">
            Professional Profiles
          </p>
        </div>

        <Globe className="text-[#8E1528]" size={24} />

      </div>

      <div className="space-y-4">

        {links.map((item) => (
          <div
            key={item.title}
            className="flex items-center justify-between rounded-xl border border-gray-200 p-4 transition hover:border-[#8E1528] hover:shadow"
          >

            <div className="flex items-center gap-4">

              <div className={`${item.color}`}>
                {item.icon}
              </div>

              <div>

                <p className="text-sm text-gray-500">
                  {item.title}
                </p>

                <p className="font-medium text-gray-900">
                  {item.value}
                </p>

              </div>

            </div>

            <button className="rounded-lg border p-2 hover:bg-gray-50">
              <ExternalLink size={18} />
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}