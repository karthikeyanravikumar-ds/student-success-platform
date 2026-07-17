import { useState } from "react";
import { FiUpload } from "react-icons/fi";
import UploadCertificateModal from "./modals/UploadCertificateModal";

export default function UploadCertificate({
  certificates,
  setCertificates,
}) {
  const [showModal, setShowModal] = useState(false);
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-3xl font-bold">
        Upload Certificate
      </h2>

      <p className="mt-2 text-gray-500">
        Upload certificates for faculty verification.
      </p>

      <div className="mt-8 rounded-2xl border-2 border-dashed border-gray-300 p-10 text-center">
        <FiUpload className="mx-auto h-12 w-12 text-red-700" />

        <p className="mt-4 text-lg font-semibold">
          Drag & Drop Certificate
        </p>

        <p className="text-gray-500">
          PDF, JPG or PNG (Max 5 MB)
        </p>

        <button
  onClick={() => setShowModal(true)}
  className="mt-6 rounded-xl bg-red-800 px-6 py-3 font-semibold text-white"
>
  Choose File
</button>
      </div>

      {showModal && (
  <UploadCertificateModal
    certificates={certificates}
    setCertificates={setCertificates}
    onClose={() => setShowModal(false)}
/>
)}

    </div>

    
  );
}