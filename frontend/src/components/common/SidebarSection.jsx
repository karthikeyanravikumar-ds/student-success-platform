import SidebarItem from "./SidebarItem";

export default function SidebarSection({ title, items }) {
  return (
    <section className="mt-8">
      <h2 className="mb-3 px-4 text-xs font-semibold uppercase tracking-wider text-white/50">
        {title}
      </h2>

      <div className="space-y-2">
        {items.map((item) => (
          <SidebarItem
            key={item.path}
            item={item}
          />
        ))}
      </div>
    </section>
  );
}