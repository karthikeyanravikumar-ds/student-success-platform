export default function CgpaChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="text-lg font-semibold">
        Semester Performance
      </h2>

      <p className="mt-1 text-sm text-gray-500">
        CGPA Progress
      </p>

      <div className="mt-6 space-y-3">
        <div className="flex justify-between">
          <span>Semester 1</span>
          <span>7.18</span>
        </div>

        <div className="flex justify-between">
          <span>Semester 2</span>
          <span>8.27</span>
        </div>

        <div className="flex justify-between">
          <span>Semester 3</span>
          <span>8.44</span>
        </div>

        <div className="flex justify-between">
          <span>Semester 4</span>
          <span>8.61</span>
        </div>
      </div>
    </div>
  );
}