import { useState } from "react";
import {
  FiMonitor,
  FiGlobe,
  FiCalendar,
} from "react-icons/fi";

export default function AppearanceSettings() {
  const [theme, setTheme] = useState("light");
  const [language, setLanguage] = useState("English");
  const [dateFormat, setDateFormat] = useState("DD/MM/YYYY");

  return (
    <section className="rounded-2xl border border-gray-200 bg-white">

      <div className="border-b px-8 py-6">
        <h2 className="text-2xl font-bold">
          Appearance & Preferences
        </h2>

        <p className="mt-1 text-gray-500">
          Customize your application experience.
        </p>
      </div>

      {/* Theme */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiMonitor className="text-2xl text-[#8E1528]" />

          <div>

            <h3 className="font-semibold">
              Theme
            </h3>

            <p className="text-sm text-gray-500">
              Select your preferred appearance.
            </p>

          </div>

        </div>

        <select
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
          className="rounded-xl border px-4 py-2"
        >
          <option value="light">Light</option>
          <option value="dark">Dark</option>
          <option value="system">System Default</option>
        </select>

      </div>

      {/* Language */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiGlobe className="text-2xl text-[#8E1528]" />

          <div>

            <h3 className="font-semibold">
              Language
            </h3>

            <p className="text-sm text-gray-500">
              Choose your preferred language.
            </p>

          </div>

        </div>

        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          className="rounded-xl border px-4 py-2"
        >
          <option>English</option>
          <option>Hindi</option>
          <option>Tamil</option>
          <option>Marathi</option>
        </select>

      </div>

      {/* Date Format */}

      <div className="flex items-center justify-between px-8 py-5">

        <div className="flex items-center gap-4">

          <FiCalendar className="text-2xl text-[#8E1528]" />

          <div>

            <h3 className="font-semibold">
              Date Format
            </h3>

            <p className="text-sm text-gray-500">
              Select your preferred date format.
            </p>

          </div>

        </div>

        <select
          value={dateFormat}
          onChange={(e) => setDateFormat(e.target.value)}
          className="rounded-xl border px-4 py-2"
        >
          <option>DD/MM/YYYY</option>
          <option>MM/DD/YYYY</option>
          <option>YYYY-MM-DD</option>
        </select>

      </div>

    </section>
  );
}