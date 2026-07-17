import { useState } from "react";
import { FiX, FiUpload } from "react-icons/fi";

export default function AddProjectModal({
    projects,
    setProjects,
    onClose,
}) {
  const [project, setProject] = useState({
    title: "",
    type: "",
    technologies: "",
    role: "",
    github: "",
    demo: "",
    startDate: "",
    endDate: "",
    description: "",
    report: null,
    presentation: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setProject((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <>
      {/* Overlay */}
      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">

        <div className="flex max-h-[90vh] w-full max-w-4xl flex-col overflow-hidden rounded-3xl bg-white shadow-xl">

          {/* Header */}

          <div className="flex items-center justify-between border-b px-8 py-6">

            <div>

              <h2 className="text-2xl font-bold">
                Add Project
              </h2>

              <p className="text-gray-500">
                Add a new academic or personal project.
              </p>

            </div>

            <button
              onClick={onClose}
              className="rounded-lg p-2 hover:bg-gray-100"
            >
              <FiX size={22} />
            </button>

          </div>

          {/* Body */}

          <div className="flex-1 overflow-y-auto p-8">

            <div className="grid gap-6 md:grid-cols-2">

              <div>
                <label className="mb-2 block font-medium">
                  Project Title
                </label>

                <input
                  name="title"
                  value={project.title}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Project Type
                </label>

                <select
                  name="type"
                  value={project.type}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                >
                  <option value="">Select</option>
                  <option>Academic</option>
                  <option>Personal</option>
                  <option>Research</option>
                  <option>Hackathon</option>
                  <option>Internship</option>
                </select>
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Technology Stack
                </label>

                <input
                  name="technologies"
                  value={project.technologies}
                  onChange={handleChange}
                  placeholder="React, FastAPI, PostgreSQL..."
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Role
                </label>

                <input
                  name="role"
                  value={project.role}
                  onChange={handleChange}
                  placeholder="Team Leader"
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  GitHub Repository
                </label>

                <input
                  name="github"
                  value={project.github}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Live Demo
                </label>

                <input
                  name="demo"
                  value={project.demo}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Start Date
                </label>

                <input
                  type="date"
                  name="startDate"
                  value={project.startDate}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  End Date
                </label>

                <input
                  type="date"
                  name="endDate"
                  value={project.endDate}
                  onChange={handleChange}
                  className="w-full rounded-xl border px-4 py-3"
                />
              </div>

            </div>

            <div className="mt-6">

              <label className="mb-2 block font-medium">
                Description
              </label>

              <textarea
                rows={5}
                name="description"
                value={project.description}
                onChange={handleChange}
                className="w-full rounded-xl border px-4 py-3 resize-none"
              />

            </div>

            <div className="mt-8 grid gap-5 md:grid-cols-2">

              <label className="flex cursor-pointer items-center gap-3 rounded-xl border-2 border-dashed p-5 hover:bg-gray-50">

                <FiUpload />

                Upload Project Report

                <input hidden type="file" />

              </label>

              <label className="flex cursor-pointer items-center gap-3 rounded-xl border-2 border-dashed p-5 hover:bg-gray-50">

                <FiUpload />

                Upload Presentation

                <input hidden type="file" />

              </label>

            </div>

          </div>

          {/* Footer */}

          <div className="flex justify-end gap-4 border-t px-8 py-6">

            <button
              onClick={onClose}
              className="rounded-xl border px-6 py-3"
            >
              Cancel
            </button>

            <button
  onClick={() => {
    const newProject = {
      id: Date.now(),
      title: project.title,
      tech: project.technologies,
      status: "Ongoing",
    };

    setProjects([newProject, ...projects]);

    onClose();
  }}
  className="rounded-xl bg-red-800 px-6 py-3 text-white"
>
  Save Project
</button>

          </div>

        </div>

      </div>
    </>
  );
}