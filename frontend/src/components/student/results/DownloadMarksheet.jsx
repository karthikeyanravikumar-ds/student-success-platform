import { useState } from "react";
import { Download, Loader2 } from "lucide-react";

export default function DownloadMarksheet() {
  const [downloading, setDownloading] = useState(false);

  const handleDownload = async () => {
    setDownloading(true);

    try {
      // Simulate loading
      await new Promise((resolve) => setTimeout(resolve, 1000));

      const link = document.createElement("a");
      link.href = "/documents/Semester-V-Marksheet.pdf";
      link.download = "Semester-V-Marksheet.pdf";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } finally {
      setDownloading(false);
    }
  };

  return (
    <div className="flex h-full flex-col justify-center rounded-2xl bg-white p-6 shadow-sm">

      <div className="text-center">

        <Download
          size={52}
          className="mx-auto mb-5 text-[#8E1528]"
        />

        <h2 className="text-2xl font-bold">
          Semester V Marksheet
        </h2>

        <p className="mt-2 text-gray-500">
          Download your official semester marksheet.
        </p>

        <button
          onClick={handleDownload}
          disabled={downloading}
          className="mt-8 inline-flex items-center justify-center gap-2 rounded-xl bg-[#8E1528] px-8 py-3 font-medium text-white transition hover:bg-[#741120] disabled:cursor-not-allowed disabled:opacity-60"
        >
          {downloading ? (
            <>
              <Loader2 size={18} className="animate-spin" />
              Downloading...
            </>
          ) : (
            <>
              <Download size={18} />
              Download PDF
            </>
          )}
        </button>

      </div>

    </div>
  );
}