import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { name: "Placed", value: 68 },
  { name: "In Process", value: 22 },
  { name: "Not Applied", value: 10 },
];

const COLORS = ["#16a34a", "#8E1528", "#d1d5db"];

export default function PlacementStats() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">

      <div className="mb-6">
        <h2 className="text-3xl font-bold">
          Placement Statistics
        </h2>

        <p className="text-gray-500">
          Current Placement Season
        </p>
      </div>

      <div className="h-72">

        <ResponsiveContainer width="100%" height="100%">

          <PieChart>

            <Pie
              data={data}
              dataKey="value"
              innerRadius={65}
              outerRadius={95}
              paddingAngle={3}
            >

              {data.map((entry, index) => (
                <Cell
                  key={entry.name}
                  fill={COLORS[index]}
                />
              ))}

            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </div>

      <div className="mt-6 space-y-2">

        {data.map((item, index) => (

          <div
            key={item.name}
            className="flex items-center justify-between"
          >

            <div className="flex items-center gap-3">

              <div
                className="h-3 w-3 rounded-full"
                style={{
                  backgroundColor: COLORS[index],
                }}
              />

              <span>{item.name}</span>

            </div>

            <span className="font-semibold">
              {item.value}%
            </span>

          </div>

        ))}

      </div>

    </div>
  );
}