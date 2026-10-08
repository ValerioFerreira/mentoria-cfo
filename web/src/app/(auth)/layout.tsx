import { AppearanceMenu } from "@/components/appearance-menu";
import { Brand, Star } from "@/components/brand";
import { getTheme } from "@/lib/theme";

const WEEKS = 20;

export default async function AuthLayout({ children }: LayoutProps<"/">) {
  const theme = await getTheme();
  return (
    <div className="grid min-h-screen lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)]">
      {/* painel de marca */}
      <aside className="relative hidden overflow-hidden bg-ink p-12 text-on-ink lg:flex lg:flex-col lg:justify-between" aria-hidden>
        <div className="pointer-events-none absolute -left-24 -top-24 h-96 w-96 rounded-full bg-primary/30 blur-3xl" />
        <div className="pointer-events-none absolute -bottom-32 right-0 h-96 w-96 rounded-full bg-teoria/20 blur-3xl" />
        <div className="tape tape-rule absolute inset-x-0 top-0 !rounded-none" />
        <Brand inverse size="lg" />
        <div className="relative space-y-6">
          <p className="eyebrow !text-on-ink-muted">Missão Oficial · CBMPE · AOCP</p>
          <h2 className="font-display text-[5.5rem] font-bold uppercase leading-[0.88]">
            Cada dia<br />
            <span className="text-primary">conta.</span>
          </h2>
          <p className="max-w-md text-on-ink-muted">Plano de estudos montado de trás para frente a partir da data da prova, com a missão de cada dia, a aula e a página exatas, bizus e cadernos de questões.</p>
          <div>
            <div className="flex items-end gap-1">
              {Array.from({ length: WEEKS }, (_, i) => (
                <span key={i} className="relative flex-1">
                  {i === WEEKS - 1 && <Star className="absolute -top-6 left-1/2 h-4 w-4 -translate-x-1/2 text-gold" />}
                  <span className="rise flex h-14 items-end rounded-md bg-white/10" style={{ ["--i" as string]: i * 0.4 }}>
                    <span className={`block w-full rounded-md ${i === WEEKS - 1 ? "bg-gold" : "bg-primary"}`} style={{ height: `${20 + (i / (WEEKS - 1)) * 80}%` }} />
                  </span>
                </span>
              ))}
            </div>
            <p className="mt-2 flex justify-between text-[11px] font-semibold text-on-ink-muted"><span>{WEEKS} semanas</span><span>Prova · 28/02/2027</span></p>
          </div>
        </div>
        <p className="relative text-xs text-on-ink-muted">Acesso por convite.</p>
      </aside>

      {/* formulário */}
      <main className="relative flex flex-col justify-center px-5 py-10 sm:px-10">
        <div className="absolute right-4 top-4"><AppearanceMenu initial={theme} /></div>
        <div className="mx-auto w-full max-w-md space-y-8">
          <div className="lg:hidden">
            <Brand size="lg" />
          </div>
          <div className="page-in">{children}</div>
        </div>
      </main>
    </div>
  );
}
