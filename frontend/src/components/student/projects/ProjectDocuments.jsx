import {
  FiDownload,
  FiEye,
  FiFileText,
} from "react-icons/fi";

const docs = [
  {
    name: "Synopsis.pdf",
    file: "/documents/Synopsis.pdf",
  },
  {
    name: "SRS.pdf",
    file: "/documents/SRS.pdf",
  },
  {
    name: "Presentation.pptx",
    file: "/documents/Presentation.pptx",
  },
  {
    name: "Final Report.pdf",
    file: "/documents/Final-Report.pdf",
  },
];

export default function ProjectDocuments() {
  const previewFile = (file) => {
    window.open(file, "_blank");
  };

  const downloadFile = (file, filename) => {
    const link = document.createElement("a");
    link.href = file;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-2xl font-bold">
        Project Documents
      </h2>

      <div className="mt-6 space-y-4">

        {docs.map((doc) => (

          <div
  key={doc.name}
  className="rounded-xl border p-4"
>

  <div className="flex items-start justify-between">

    <div className="flex gap-3">

      <FiFileText
        size={22}
        className="mt-1 text-red-700"
      />

      <div>

        <p className="font-semibold">
          {doc.name}
        </p>

        <p className="text-sm text-gray-500">
          Project Document
        </p>

      </div>

    </div>

  </div>

  <div className="mt-4 flex gap-3">

    <button
      onClick={() => previewFile(doc.file)}
      className="rounded-lg border px-4 py-2 hover:bg-gray-50"
    >
      Preview
    </button>

    <button
      onClick={() => downloadFile(doc.file, doc.name)}
      className="rounded-lg bg-red-800 px-4 py-2 text-white"
    >
      Download
    </button>

  </div>

</div>

        ))}

      </div>

    </div>
  );
}