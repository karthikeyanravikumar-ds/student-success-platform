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
  { semester: "Sem I", sgpa: 7.18 },
  { semester: "Sem II", sgpa: 8.27 },
  { semester: "Sem III", sgpa: 8.41 },
  { semester: "Sem IV", sgpa: 8.62 },
  { semester: "Sem V", sgpa: 8.91 },
];

export default function PerformanceChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6">
        <h2 className="text-2xl font-bold">
          Academic Performance
        </h2>

        <p className="text-gray-500">
          Semester-wise SGPA Trend
        </p>
      </div>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="semester" />

            <YAxis
              domain={[6, 10]}
            />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="sgpa"
              stroke="#8E1528"
              strokeWidth={3}
              dot={{
                r: 6,
                fill: "#8E1528",
              }}
            />

          </LineChart>

        </ResponsiveContainer>
      </div>

    </div>
  );
}