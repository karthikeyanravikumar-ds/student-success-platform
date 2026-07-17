export default function Button({
  children,
  onClick,
  variant = "primary",
  type = "button",
}) {
  const styles = {
    primary:
      "bg-red-800 text-white hover:bg-red-900",

    secondary:
      "border border-gray-300 bg-white text-gray-700 hover:bg-gray-100",
  };

  return (
    <button
      type={type}
      onClick={onClick}
      className={`rounded-xl px-5 py-2.5 font-medium transition ${styles[variant]}`}
    >
      {children}
    </button>
  );
}