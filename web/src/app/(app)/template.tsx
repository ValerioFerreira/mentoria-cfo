// Re-monta a cada navegação: dá a entrada suave de página sem biblioteca de animação.
export default function AppTemplate({ children }: { children: React.ReactNode }) {
  return <div className="page-in">{children}</div>;
}
