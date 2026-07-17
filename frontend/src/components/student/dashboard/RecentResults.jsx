export default function RecentResults() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="text-lg font-semibold">
        Recent Results
      </h2>

      <table className="mt-6 w-full">
        <tbody>
          <tr>
            <td>Python</td>
            <td>A+</td>
          </tr>

          <tr>
            <td>Statistics</td>
            <td>O</td>
          </tr>

          <tr>
            <td>Machine Learning</td>
            <td>A</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}