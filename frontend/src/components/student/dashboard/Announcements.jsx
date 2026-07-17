import SectionCard from "./SectionCard";
import Badge from "../../ui/Badge";

export default function Announcements() {
  const announcements = [
  {
    category: "Academic",
    color: "blue",
    title: "Internal Assessment Schedule Released",
    date: "Today",
  },
  {
    category: "Placement",
    color: "green",
    title: "Placement Orientation on Friday",
    date: "Yesterday",
  },
  {
    category: "General",
    color: "gray",
    title: "Semester Registration Starts Next Week",
    date: "2 days ago",
  },
  ];

  return (
    <SectionCard title="Announcements">
      <div className="space-y-4">
        {announcements.map((item, index) => (
          <div
            key={index}
            className="border-b border-gray-100 pb-3 last:border-none"
          >
            <div className="mb-2">
                <Badge color={item.color}>
                    {item.category}
                </Badge>
            </div>
            
            <h3 className="font-medium text-gray-800">
                {item.title}
            </h3>

            <p className="mt-1 text-sm text-gray-500">
              {item.date}
            </p>
          </div>
        ))}
      </div>
    </SectionCard>
  );
}