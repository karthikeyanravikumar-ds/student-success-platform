import SectionCard from "./SectionCard";

export default function Timetable() {
  const schedule = [
    {
      time: "09:00 - 10:00",
      subject: "Database Management Systems",
      room: "Room 401",
    },
    {
      time: "10:00 - 11:00",
      subject: "Machine Learning",
      room: "Lab 3",
    },
    {
      time: "11:15 - 12:15",
      subject: "Data Visualization",
      room: "Room 502",
    },
  ];

  return (
    <SectionCard title="Today's Timetable">
      <div className="space-y-4">
        {schedule.map((item, index) => (
          <div
            key={index}
            className="border-b border-gray-100 pb-3 last:border-none"
          >
            <p className="font-semibold">
              {item.time}
            </p>

            <p className="text-gray-700">
              {item.subject}
            </p>

            <p className="text-sm text-gray-500">
              {item.room}
            </p>
          </div>
        ))}
      </div>
    </SectionCard>
  );
}