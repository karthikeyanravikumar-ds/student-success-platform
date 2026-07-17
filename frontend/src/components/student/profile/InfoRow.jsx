export default function InfoRow({
  label,
  value,
}) {
  return (
    <div className="flex justify-between border-b border-gray-100 py-3">
      <span className="font-medium text-gray-500">
        {label}
      </span>

      <span className="text-gray-900">
        {value}
      </span>
    </div>
  );
}