export default function ProjectDetails() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-2xl font-bold">
        Project Details
      </h2>

      <div className="mt-6 space-y-3">
        <p>
          <strong>Current Project</strong>
        </p>

        <p className="text-gray-600">
          Student Success Platform is a centralized academic
          management platform developed for VSIT.
        </p>

        <p>
          Duration : January 2026 - Present
        </p>

        <p>
          Guide : Dr. Faculty Name
        </p>
      </div>
    </div>
  );
}