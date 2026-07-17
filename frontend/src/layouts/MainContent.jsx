export default function MainContent({ children }) {
  return (
    <main
      className="flex-1 overflow-y-auto"
      style={{
        background: "var(--background)",
      }}
    >
      {children}
    </main>
  );
}