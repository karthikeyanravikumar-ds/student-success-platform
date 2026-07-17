import {
  FiCheckCircle,
  FiClock,
  FiXCircle,
} from "react-icons/fi";



export default function UploadedCertificates({
    certificates,
}) {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">Uploaded Certificates</h2>

      <table className="mt-8 w-full">
        <thead className="border-b">
          <tr className="text-left text-gray-500">
            <th className="pb-4">Certificate</th>
            <th>Category</th>
            <th>Date</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {certificates.map((item) => (
            <tr key={item.name} className="border-b last:border-none">
              <td className="py-5 font-semibold">{item.name}</td>

              <td>{item.category}</td>

              <td>{item.date}</td>

              <td>
                {item.status === "Verified" && (
                  <span className="inline-flex items-center gap-2 rounded-full bg-green-100 px-4 py-2 text-green-700">
                    <FiCheckCircle />
                    Verified
                  </span>
                )}

                {item.status === "Pending" && (
                  <span className="inline-flex items-center gap-2 rounded-full bg-orange-100 px-4 py-2 text-orange-700">
                    <FiClock />
                    Pending
                  </span>
                )}

                {item.status === "Rejected" && (
                  <span className="inline-flex items-center gap-2 rounded-full bg-red-100 px-4 py-2 text-red-700">
                    <FiXCircle />
                    Rejected
                  </span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}