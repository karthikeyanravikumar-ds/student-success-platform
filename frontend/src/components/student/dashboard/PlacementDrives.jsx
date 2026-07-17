import SectionCard from "./SectionCard";

export default function PlacementDrives() {
  const companies = [
    {
      name: "TCS",
      role: "Software Engineer",
      date: "15 July",
    },
    {
      name: "Accenture",
      role: "Associate Engineer",
      date: "18 July",
    },
    {
      name: "Capgemini",
      role: "Analyst",
      date: "22 July",
    },
  ];

  return (
    <SectionCard title="Upcoming Placement Drives">
      <div className="space-y-4">
        {companies.map((company, index) => (
          <div
            key={index}
            className="border-b border-gray-100 pb-3 last:border-none"
          >
            <h3 className="font-semibold">
              {company.name}
            </h3>

            <p className="text-gray-600">
              {company.role}
            </p>

            <p className="text-sm text-gray-500">
              {company.date}
            </p>
          </div>
        ))}
      </div>
    </SectionCard>
  );
}