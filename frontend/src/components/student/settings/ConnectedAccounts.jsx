import {
  FiGithub,
  FiLinkedin,
  FiChrome,
} from "react-icons/fi";

const accounts = [
  {
    name: "GitHub",
    icon: <FiGithub />,
    status: "Connected",
  },
  {
    name: "LinkedIn",
    icon: <FiLinkedin />,
    status: "Not Connected",
  },
  {
    name: "Google",
    icon: <FiChrome />,
    status: "Connected",
  },
];

export default function ConnectedAccounts() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-3xl font-bold">
        Connected Accounts
      </h2>

      <div className="mt-8 space-y-5">

        {accounts.map((account) => (

          <div
            key={account.name}
            className="flex items-center justify-between rounded-2xl border p-5"
          >

            <div className="flex items-center gap-4">

              <div className="text-2xl text-[#8E1528]">
                {account.icon}
              </div>

              <div>
                <h3 className="font-semibold">
                  {account.name}
                </h3>

                <p className="text-gray-500">
                  {account.status}
                </p>
              </div>

            </div>

            <button className="rounded-xl border px-5 py-2">
              {account.status === "Connected"
                ? "Disconnect"
                : "Connect"}
            </button>

          </div>

        ))}

      </div>

    </div>
  );
}