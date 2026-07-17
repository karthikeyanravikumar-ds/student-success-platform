import { useState } from "react";
import {
  Download,
  FileBadge,
  Loader2,
  Eye,
  Printer,
} from "lucide-react";

export default function HallTicketCard() {
  const [downloading, setDownloading] = useState(false);

  const pdf = "/documents/Semester-V-Hall-Ticket.pdf";

  const handleDownload = async () => {
    setDownloading(true);

    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));

      const link = document.createElement("a");
      link.href = pdf;
      link.download = "Semester-V-Hall-Ticket.pdf";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } finally {
      setDownloading(false);
    }
  };

  const handlePreview = () => {
    window.open(pdf, "_blank");
  };

  const handlePrint = () => {
    window.open(pdf, "_blank");
  };

  return (
    <div className="rounded-2xl bg-white p-8 shadow-sm">

      <div className="flex flex-col items-center">

        <div className="rounded-full bg-red-50 p-5 text-[#8E1528]">
          <FileBadge size={50} />
        </div>

        <h2 className="mt-6 text-3xl font-bold">
          Hall Ticket
        </h2>

        <p className="mt-2 text-center text-gray-500">
          Semester V Examination
        </p>

        <div className="mt-6 w-full rounded-xl bg-gray-50 p-4">

          <div className="flex justify-between py-2">
            <span className="text-gray-500">Status</span>
            <span className="font-semibold text-green-600">
              Available
            </span>
          </div>

          <div className="flex justify-between py-2">
            <span className="text-gray-500">Seat Number</span>
            <span className="font-semibold">
              DS20260045
            </span>
          </div>

          <div className="flex justify-between py-2">
            <span className="text-gray-500">Exam Starts</span>
            <span className="font-semibold">
              20 Jul 2026
            </span>
          </div>

        </div>

        <div className="mt-8 flex w-full flex-wrap gap-3">

          <button
            onClick={handlePreview}
            className="flex flex-1 items-center justify-center gap-2 rounded-xl border px-4 py-3 hover:bg-gray-50"
          >
            <Eye size={18} />
            Preview
          </button>

          <button
            onClick={handlePrint}
            className="flex flex-1 items-center justify-center gap-2 rounded-xl border px-4 py-3 hover:bg-gray-50"
          >
            <Printer size={18} />
            Print
          </button>

        </div>

        <button
          onClick={handleDownload}
          disabled={downloading}
          className="mt-4 flex w-full items-center justify-center gap-2 rounded-xl bg-[#8E1528] px-6 py-3 font-semibold text-white transition hover:bg-[#70111f] disabled:cursor-not-allowed disabled:opacity-60"
        >
          {downloading ? (
            <>
              <Loader2 className="animate-spin" size={18} />
              Downloading...
            </>
          ) : (
            <>
              <Download size={18} />
              Download Hall Ticket
            </>
          )}
        </button>

      </div>

    </div>
  );
}