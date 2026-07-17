import { NavLink } from "react-router-dom";

export default function SidebarItem({ item }) {
  const Icon = item.icon;

  return (
    <NavLink
      to={item.path}
      className={({ isActive }) =>
        `flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all duration-200 ${
          isActive
            ? "bg-white text-[var(--primary-dark)] shadow-sm"
            : "text-white/80 hover:bg-white/10 hover:text-white"
        }`
      }
    >
      <Icon size={18} />
      <span>{item.name}</span>
    </NavLink>
  );
}