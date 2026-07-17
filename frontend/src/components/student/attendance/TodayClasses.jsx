import { Clock } from "lucide-react";

const classes = [
  {
    subject: "Python",
    time: "09:00 - 10:00",
    status: "Present",
  },
  {
    subject: "Machine Learning",
    time: "10:00 - 11:00",
    status: "Present",
  },
  {
    subject: "DBMS",
    time: "12:00 - 01:00",
    status: "Upcoming",
  },
  {
    subject: "Statistics",
    time: "02:00 - 03:00",
    status: "Absent",
  },
];

function badge(status) {
  switch (status) {
    case "Present":
      return "bg-green-100 text-green-700";

    case "Upcoming":
      return "bg-blue-100 text-blue-700";

    case "Absent":
      return "bg-red-100 text-red-700";

    default:
      return "bg-gray-100 text-gray-700";
  }
}

export default function TodayClasses() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center gap-3">

        <Clock
          size={22}
          className="text-[#8E1528]"
        />

        <div>
          <h2 className="text-xl font-bold">
            Today's Classes
          </h2>

          <p className="text-sm text-gray-500">
            Daily Schedule
          </p>
        </div>

      </div>

      <div className="space-y-4">

        {classes.map((item) => (

          <div
            key={item.subject}
            className="flex items-center justify-between rounded-xl border p-4"
          >

            <div>

              <p className="font-semibold">
                {item.subject}
              </p>

              <p className="text-sm text-gray-500">
                {item.time}
              </p>

            </div>

            <span
              className={`rounded-full px-3 py-1 text-sm font-medium ${badge(item.status)}`}
            >
              {item.status}
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}