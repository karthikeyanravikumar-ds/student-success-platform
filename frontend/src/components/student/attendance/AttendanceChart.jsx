import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", attendance: 92 },
  { month: "Feb", attendance: 95 },
  { month: "Mar", attendance: 90 },
  { month: "Apr", attendance: 88 },
  { month: "May", attendance: 93 },
  { month: "Jun", attendance: 91 },
];

export default function AttendanceChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-bold">
        Attendance Trend
      </h2>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis domain={[70, 100]} />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="attendance"
              stroke="#8E1528"
              strokeWidth={3}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}