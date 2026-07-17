import { useState } from "react";
import {
  FiDownload,
} from "react-icons/fi";
import { Loader2 } from "lucide-react";

export default function DownloadPortfolio() {

  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {

    setLoading(true);

    try {

      await new Promise((resolve) =>
        setTimeout(resolve, 1000)
      );

      const link = document.createElement("a");

      link.href =
        "/documents/Student_Project_Portfolio.pdf";

      link.download =
        "Student_Project_Portfolio.pdf";

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 text-center shadow-sm">

      <FiDownload className="mx-auto text-6xl text-red-700" />

      <h2 className="mt-6 text-3xl font-bold">
        Project Portfolio
      </h2>

      <p className="mt-3 text-gray-500">
        Download all project information as a PDF.
      </p>

      <div className="mt-8 grid grid-cols-2 gap-4 text-center">

  <div>
    <p className="text-2xl font-bold">
      3
    </p>
    <p className="text-sm text-gray-500">
      Projects
    </p>
  </div>

  <div>
    <p className="text-2xl font-bold">
      2.8 MB
    </p>
    <p className="text-sm text-gray-500">
      Portfolio Size
    </p>
  </div>

  <div>
    <p className="text-2xl font-bold text-green-600">
      1
    </p>
    <p className="text-sm text-gray-500">
      Completed
    </p>
  </div>

  <div>
    <p className="text-2xl font-bold text-yellow-600">
      1
    </p>
    <p className="text-sm text-gray-500">
      Ongoing
    </p>
  </div>

</div>

      <button
        onClick={handleDownload}
        disabled={loading}
        className="mt-8 rounded-xl bg-red-800 px-8 py-3 font-semibold text-white disabled:opacity-60"
      >
        {loading ? "Generating PDF..." : "Generate Portfolio PDF"}
      </button>

    </div>
  );
}