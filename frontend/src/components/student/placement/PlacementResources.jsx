import {
  FiBook,
  FiFileText,
  FiVideo,
  FiExternalLink,
} from "react-icons/fi";

const resources = [
  {
    title: "Aptitude Preparation",
    icon: FiBook,
    link: "https://www.indiabix.com/",
  },
  {
    title: "Resume Templates",
    icon: FiFileText,
    link: "/documents/Resume-Template.docx",
  },
  {
    title: "Interview Preparation",
    icon: FiVideo,
    link: "https://www.interviewbit.com/",
  },
];

export default function PlacementResources() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">
      <div className="mb-6">
        <h2 className="text-3xl font-bold">
          Placement Resources
        </h2>

        <p className="text-gray-500">
          Improve your placement readiness
        </p>
      </div>

      <div className="space-y-5">
        {resources.map((resource) => {
          const Icon = resource.icon;

          return (
            <a
              key={resource.title}
              href={resource.link}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-between rounded-2xl border p-5 transition hover:border-[#8E1528] hover:bg-red-50"
            >
              <div className="flex items-center gap-4">
                <div className="rounded-xl bg-red-50 p-3 text-[#8E1528]">
                  <Icon size={24} />
                </div>

                <div>
                  <h3 className="text-lg font-semibold">
                    {resource.title}
                  </h3>

                  <p className="text-sm text-gray-500">
                    Click to open resource
                  </p>
                </div>
              </div>

              <FiExternalLink
                size={22}
                className="text-gray-500"
              />
            </a>
          );
        })}
      </div>
    </div>
  );
}