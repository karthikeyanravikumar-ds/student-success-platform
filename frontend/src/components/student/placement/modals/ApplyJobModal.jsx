import { X } from "lucide-react";

export default function ApplyJobModal({
    company,
    applications,
    setApplications,
    onClose,
}) {
  return (
    <>
      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
      />

      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">

        <div className="w-full max-w-2xl rounded-3xl bg-white shadow-xl">

          <div className="flex items-center justify-between border-b px-8 py-6">

            <div>
              <h2 className="text-2xl font-bold">
                Apply for Placement
              </h2>

              <p className="text-gray-500">
                Submit your application.
              </p>
            </div>

            <button
              onClick={onClose}
              className="rounded-lg p-2 hover:bg-gray-100"
            >
              <X />
            </button>

          </div>

          <div className="p-8">

            <div className="space-y-5">

  <div className="rounded-xl bg-gray-50 p-5">

    <h3 className="text-xl font-bold">
      {company.company}
    </h3>

    <p className="mt-2 text-gray-600">
      {company.role}
    </p>

    <div className="mt-4 grid grid-cols-2 gap-4">

      <div>
        <p className="text-sm text-gray-500">
          Package
        </p>

        <p className="font-semibold">
          {company.package}
        </p>
      </div>

      <div>
        <p className="text-sm text-gray-500">
          Location
        </p>

        <p className="font-semibold">
          {company.location}
        </p>
      </div>

      <div>
        <p className="text-sm text-gray-500">
          Drive Date
        </p>

        <p className="font-semibold">
          {company.date}
        </p>
      </div>

      <div>
        <p className="text-sm text-gray-500">
          Status
        </p>

        <p className="font-semibold text-green-600">
          {company.status}
        </p>
      </div>

    </div>

  </div>

</div>

          </div>

          <div className="flex justify-end gap-3 border-t px-8 py-6">

            <button
              onClick={onClose}
              className="rounded-xl border px-5 py-2"
            >
              Cancel
            </button>

            <button
onClick={() => {

    const exists = applications.find(
    item => item.company === company.company
);

if (exists) {
    alert("You have already applied.");
    return;
}

const application = {
        id: Date.now(),
        ...company,
        appliedDate: new Date().toLocaleDateString(),
        applicationStatus: "Applied",
    };

    setApplications([
        application,
        ...applications,
    ]);

    onClose();

}}
className="rounded-xl bg-[#8E1528] px-6 py-3 text-white"
>
Submit Application
</button>

          </div>

        </div>

      </div>
    </>
  );
}