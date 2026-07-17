import { BRAND } from "../../config/branding";

export default function Brand() {
  return (
    <div className="flex flex-col items-center text-center">

      <img
        src={BRAND.logo.white}
        alt="VSIT Logo"
        className="h-14 object-contain"
      />

      <h1 className="mt-4 text-lg font-semibold text-white">
        Student Success Platform
      </h1>

      <p className="mt-2 text-xs leading-5 text-white/70 max-w-[180px]">
        {BRAND.college}
      </p>

    </div>
  );
}