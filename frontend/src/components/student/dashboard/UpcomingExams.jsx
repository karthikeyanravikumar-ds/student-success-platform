export default function UpcomingExams() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h2 className="text-lg font-semibold">
        Upcoming Exams
      </h2>

      <table className="mt-6 w-full">
        <tbody>
          <tr>
            <td>Machine Learning</td>
            <td>15 Jul</td>
          </tr>

          <tr>
            <td>Python</td>
            <td>18 Jul</td>
          </tr>

          <tr>
            <td>Statistics</td>
            <td>22 Jul</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}