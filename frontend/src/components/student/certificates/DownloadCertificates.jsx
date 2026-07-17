import { useState } from "react";
import { FiDownload } from "react-icons/fi";
import { Loader2 } from "lucide-react";

export default function DownloadCertificates() {
  const [downloading, setDownloading] = useState(false);

  const handleDownload = async () => {
    setDownloading(true);

    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));

      const link = document.createElement("a");
      link.href = "/documents/Student_Certificates.zip";
      link.download = "Student_Certificates.zip";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } finally {
      setDownloading(false);
    }
  };

  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 text-center shadow-sm">

      <FiDownload className="mx-auto text-6xl text-red-700" />

      <h2 className="mt-6 text-3xl font-bold">
        Download Certificates
      </h2>

      <p className="mt-3 text-gray-500">
        Download all verified certificates as a ZIP file.
      </p>

      <button
        onClick={handleDownload}
        disabled={downloading}
        className="mt-8 rounded-xl bg-red-800 px-8 py-3 font-semibold text-white disabled:opacity-60"
      >
        {downloading ? "Preparing ZIP..." : "Download ZIP"}
      </button>

    </div>
  );
}