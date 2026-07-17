import Card from "../../ui/Card";
export default function SectionCard({
  title,
  children,
}) {
  return (
    <Card className="overflow-hidden">

      {/* Header */}

      <div className="border-b border-gray-100 px-6 py-4">

        <h2 className="text-lg font-semibold text-gray-900">
          {title}
        </h2>

      </div>

      {/* Content */}

      <div className="p-6">

        {children}

      </div>

    </Card>
  );
}