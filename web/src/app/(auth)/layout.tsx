import Link from "next/link";
import { AppearanceMenu } from "@/components/appearance-menu";
import { Brand } from "@/components/brand";
import { getTheme } from "@/lib/theme";

const OPTIONS = ["A", "B", "C", "D", "E"];
const MARKED = "C";

/** Fileira de alternativas de um cartão-resposta: uma delas é preenchida assim que a página abre. */
function AnswerBubbles() {
  return (
    <div className="flex items-center gap-2.5 sm:gap-3.5" aria-hidden>
      {OPTIONS.map((letter) => (
        <span
          key={letter}
          className="relative grid h-10 w-10 place-items-center rounded-full border-2 border-on-ink-muted/45 font-display text-xl font-bold text-on-ink-muted sm:h-14 sm:w-14 sm:text-2xl"
        >
          {letter}
          {letter === MARKED && <span className="pop absolute -inset-0.5 rounded-full bg-gold shadow-[0_0_22px_-2px_var(--gold)]" style={{ animationDelay: "900ms" }} />}
        </span>
      ))}
    </div>
  );
}

export default async function AuthLayout({ children }: LayoutProps<"/">) {
  const theme = await getTheme();
  return (
    <div className="grid min-h-screen lg:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)]">
      {/* coluna de marca */}
      <aside className="relative flex flex-col overflow-hidden bg-ink px-6 pb-11 pt-6 text-on-ink sm:px-12 sm:pb-16 sm:pt-8 lg:justify-between lg:p-14 lg:pb-20">
        <div className="pointer-events-none absolute -left-24 -top-24 h-96 w-96 rounded-full bg-primary/25 blur-3xl" aria-hidden />
        <div className="pointer-events-none absolute -bottom-40 right-0 h-96 w-96 rounded-full bg-teoria/15 blur-3xl" aria-hidden />
        <div className="relative">
          <Link href="/" aria-label="MentorIA — início" className="inline-block">
            <Brand inverse size="lg" />
          </Link>
        </div>
        <div className="relative mt-7 space-y-5 sm:mt-10 sm:space-y-7 lg:mt-0 lg:space-y-9">
          <h2 className="font-display text-[clamp(3.75rem,11vw,9rem)] font-bold uppercase leading-[0.84]">
            Cada dia
            <br />
            conta.
          </h2>
          <AnswerBubbles />
          <p className="max-w-md text-sm leading-relaxed text-on-ink-muted sm:text-base lg:text-lg">
            Tenha um plano de estudos exclusivo, individualizado, com direcionamento detalhado, resumos, e questões com a pegada da banca. Você só precisa sentar e estudar, o resto deixa com a gente!
          </p>
        </div>
        <div className="tape tape-rule absolute inset-x-0 bottom-0 !rounded-none" aria-hidden />
      </aside>

      {/* folha do formulário (borda com as marcas do cartão-resposta) */}
      <main className="omr-edge relative flex flex-col justify-center bg-surface py-8 pl-12 pr-6 shadow-[-28px_0_48px_-24px_rgb(0_0_0/0.55)] sm:py-12 sm:pl-16 sm:pr-14 lg:py-10">
        <div className="absolute right-4 top-4">
          <AppearanceMenu initial={theme} />
        </div>
        <div className="mx-auto w-full max-w-sm">
          <div className="page-in">{children}</div>
        </div>
      </main>
    </div>
  );
}
