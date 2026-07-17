import {
  FiDownload,
  FiFileText,
  FiFolder,
  FiTrash2,
} from "react-icons/fi";

const actions = [
  {
    title: "Download My Data",
    description: "Download your complete student profile.",
    icon: <FiDownload />,
    button: "Download",
  },
  {
    title: "Export Certificates",
    description: "Download all verified certificates.",
    icon: <FiFileText />,
    button: "Export",
  },
  {
    title: "Export Projects",
    description: "Download all submitted projects.",
    icon: <FiFolder />,
    button: "Export",
  },
  {
    title: "Delete Account Request",
    description: "Request permanent account deletion.",
    icon: <FiTrash2 />,
    button: "Request",
  },
];

export default function DataManagement() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-3xl font-bold">
        Data Management
      </h2>

      <p className="mb-8 text-gray-500">
        Manage and export your account data.
      </p>

      <div className="space-y-5">

        {actions.map((item) => (

          <div
            key={item.title}
            className="flex items-center justify-between rounded-2xl border p-5"
          >

            <div className="flex items-center gap-4">

              <div className="rounded-xl bg-red-50 p-3 text-2xl text-[#8E1528]">
                {item.icon}
              </div>

              <div>
                <h3 className="font-semibold">
                  {item.title}
                </h3>

                <p className="text-sm text-gray-500">
                  {item.description}
                </p>
              </div>

            </div>

            <button className="rounded-xl bg-[#8E1528] px-5 py-2 text-white hover:bg-[#741120]">
              {item.button}
            </button>

          </div>

        ))}

      </div>

    </div>
  );
}