import { FiBell, FiMenu } from "react-icons/fi";
import SearchBar from "./SearchBar";
import UserAvatar from "./UserAvatar";

export default function Navbar() {
  return (
    <header className="flex h-[72px] items-center justify-between border-b border-gray-200 bg-white px-8">

      {/* Left */}
      <div className="flex items-center gap-4">
        <button className="rounded-lg p-2 hover:bg-gray-100 transition">
          <FiMenu size={20} />
        </button>

        <h1 className="text-2xl font-semibold text-gray-900">
          Dashboard
        </h1>
      </div>

      {/* Right */}
      <div className="flex items-center gap-6">
        <SearchBar />

        <button className="rounded-full p-2 hover:bg-gray-100 transition">
          <FiBell size={20} />
        </button>

        <UserAvatar />
      </div>

    </header>
  );
}