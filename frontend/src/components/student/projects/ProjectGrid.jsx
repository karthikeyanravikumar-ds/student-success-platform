
export default function ProjectGrid({
    projects,
}) {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      {projects.map((project) => (
        <div
          key={project.title}
          className="rounded-3xl border border-gray-200 bg-white p-6 shadow-sm"
        >
          <h3 className="text-xl font-bold">{project.title}</h3>

          <p className="mt-2 text-gray-500">{project.tech}</p>

          <span className="mt-5 inline-block rounded-full bg-red-100 px-4 py-1 text-sm text-red-700">
            {project.status}
          </span>
        </div>
      ))}
    </div>
  );
}