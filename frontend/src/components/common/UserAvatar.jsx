export default function UserAvatar() {
  return (
    <div className="flex items-center gap-3">
      <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[var(--primary)] text-white font-semibold">
        A
      </div>

      <div>
        <p className="text-sm font-semibold">
          Angel
        </p>

        <p className="text-xs text-gray-500">
          Student
        </p>
      </div>
    </div>
  );
}