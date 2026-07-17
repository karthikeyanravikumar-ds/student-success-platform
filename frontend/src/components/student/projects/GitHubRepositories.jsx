const repos = [
  "Student Success Platform",
  "Flood Risk Mapping",
  "Fraud Detection",
];

export default function GitHubRepositories() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-2xl font-bold">
        GitHub Repositories
      </h2>

      <div className="mt-6 space-y-4">
        {repos.map((repo) => (
          <div
            key={repo}
            className="rounded-xl border p-4"
          >
            {repo}
          </div>
        ))}
      </div>
    </div>
  );
}