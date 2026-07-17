import { useState } from "react";
import AddProjectModal from "./modals/AddProjectModal";

export default function ProjectToolbar({
    projects,
    setProjects,
}) {
  const [showModal, setShowModal] = useState(false);
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <input
          type="text"
          placeholder="Search projects..."
          className="rounded-xl border border-gray-300 px-4 py-2 outline-none focus:border-red-700"
        />

        <button
  onClick={() => setShowModal(true)}
  className="rounded-xl bg-red-800 px-5 py-2 text-white hover:bg-red-900"
>
  + Add Project
</button>
      </div>

      {showModal && (
  <AddProjectModal
    projects={projects}
    setProjects={setProjects}
    onClose={() => setShowModal(false)}
/>
)}

    </div>
  );
}