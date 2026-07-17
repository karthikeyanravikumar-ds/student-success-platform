import SectionCard from "./SectionCard";

export default function QuickActions() {
  const actions = [
    "View Results",
    "Download Hall Ticket",
    "Pay Fees",
    "Apply for Placement",
    "Request Bonafide Certificate",
    "View Attendance",
  ];

  return (
    <SectionCard title="Quick Actions">
      <div className="grid grid-cols-2 gap-4">
        {actions.map((action) => (
          <button
            key={action}
            className="rounded-xl border border-gray-200 p-4 text-left transition hover:border-red-700 hover:bg-red-50"
          >
            {action}
          </button>
        ))}
      </div>
    </SectionCard>
  );
}