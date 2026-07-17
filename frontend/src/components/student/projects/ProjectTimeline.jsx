const steps = [
  "Proposal Submitted",
  "Faculty Approved",
  "Development",
  "Testing",
  "Final Submission",
];

export default function ProjectTimeline() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">
      <h2 className="text-2xl font-bold">
        Timeline
      </h2>

      <div className="mt-6 space-y-5">
        {steps.map((step, index) => (
          <div key={step}>
            {index + 1}. {step}
          </div>
        ))}
      </div>
    </div>
  );
}