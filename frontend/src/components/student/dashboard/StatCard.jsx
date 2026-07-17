import Card from "../../ui/Card";
export default function StatCard({
  title,
  value,
  subtitle,
  icon,
}) {
  return (
    <Card className="p-6">

      <div className="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-red-50">
        {icon}
      </div>

      <h3 className="text-sm font-medium text-gray-500">
        {title}
      </h3>

      <h2 className="mt-2 text-3xl font-bold text-gray-900">
        {value}
      </h2>

      <p className="mt-2 text-sm text-gray-500">
        {subtitle}
      </p>

    </Card>
  );
}