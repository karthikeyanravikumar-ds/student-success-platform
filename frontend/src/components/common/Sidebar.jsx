import SidebarHeader from "./SidebarHeader";
import SidebarSection from "./SidebarSection";
import { navigation } from "../../utils/navigation";

export default function Sidebar() {
  return (
    <aside
      className="flex h-screen w-[260px] flex-col"
      style={{
        backgroundColor: "var(--primary-dark)",
      }}
    >
      {/* Header */}
      <SidebarHeader />

      {/* Navigation */}
      <div className="flex-1 overflow-y-auto px-4 py-2">
        {navigation.map((section) => (
          <SidebarSection
            key={section.title}
            title={section.title}
            items={section.items}
          />
        ))}
      </div>
    </aside>
  );
}