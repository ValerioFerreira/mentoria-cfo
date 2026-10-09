import Link from "next/link";
import { AppearanceMenu } from "@/components/appearance-menu";
import { Brand } from "@/components/brand";
import { VaporCountdown } from "@/components/countdown-vapor-digits";
import { getTheme } from "@/lib/theme";

const WEEK_DAYS = [
  { label: "D", title: "Domingo" },
  { label: "S", title: "Segunda-feira" },
  { label: "T", title: "Terça-feira" },
  { label: "Q", title: "Quarta-feira" },
  { label: "Q", title: "Quinta-feira" },
  { label: "S", title: "Sexta-feira" },
  { label: "S", title: "Sábado" },
];

/** Retorna o índice do dia de hoje no fuso de Recife (0 = Domingo ... 6 = Sábado). */
function getTodayDayOfWeek(): number {
  const short = new Intl.DateTimeFormat("en-US", { timeZone: "America/Recife", weekday: "short" }).format(new Date());
  const idx = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(short);
  return idx >= 0 ? idx : new Date().getDay();
}

/** Fileira dos dias da semana (D S T Q Q S S): o marcador percorre do Domingo até o dia atual e nele fica piscando. */
function WeekdayBubbles() {
  const currentDayIndex = getTodayDayOfWeek();

  return (
    <div className="flex items-center gap-2 sm:gap-3" aria-label="Dias da semana">
      {WEEK_DAYS.map((day, i) => {
        const isPastOrToday = i <= currentDayIndex;
        const isToday = i === currentDayIndex;
        // Intervalo de 220ms entre cada dia percorrido; o dia atual para e entra em pulso contínuo
        const sweepDelay = `${i * 220 + 200}ms`;

        return (
          <span
            key={`${day.label}-${i}`}
            title={day.title}
            className={`relative grid h-10 w-10 place-items-center rounded-full border-2 font-display text-xl font-bold transition-colors sm:h-12 sm:w-12 sm:text-2xl ${
              isPastOrToday ? "border-gold/60 text-on-ink" : "border-on-ink-muted/30 text-on-ink-muted/60"
            }`}
          >
            {/* Letra do dia da semana (fica na frente da bolinha) */}
            <span className="relative z-10">{day.label}</span>

            {/* Bolinha dourada preenchida: dias anteriores animam e ficam fixos */}
            {isPastOrToday && !isToday && (
              <span
                className="absolute inset-0 rounded-full bg-gold/30 shadow-[0_0_10px_-2px_var(--gold)]"
                style={{
                  animation: `day-fill-sweep 0.4s var(--ease-spring) both`,
                  animationDelay: sweepDelay,
                }}
              />
            )}

            {/* Bolinha dourada do dia atual: percorre, preenche e fica pulsando/piscando sem parar */}
            {isToday && (
              <span
                className="absolute -inset-0.5 rounded-full bg-gold"
                style={{
                  animation: `day-fill-sweep 0.4s var(--ease-spring) both, day-pulse-active 1.4s ease-in-out infinite ${
                    i * 220 + 600
                  }ms`,
                  animationDelay: `${sweepDelay}, ${i * 220 + 600}ms`,
                }}
              />
            )}
          </span>
        );
      })}
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

        {/* Cronômetro moderno sem fundo, centralizado no espaço entre a marca e CADA DIA CONTA */}
        <div className="relative my-auto flex flex-col items-center justify-center py-4 text-center">
          <p className="mb-2 font-display text-xs sm:text-sm font-bold uppercase tracking-[0.25em] text-gold">
            Lançamento Oficial
          </p>
          <VaporCountdown targetDate="2026-10-09T22:00:00-03:00" />
        </div>

        <div className="relative space-y-5 sm:space-y-7 lg:space-y-9">
          <h2 className="font-display text-[clamp(3.75rem,11vw,9rem)] font-bold uppercase leading-[0.84]">
            Cada dia
            <br />
            conta.
          </h2>
          <WeekdayBubbles />
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
