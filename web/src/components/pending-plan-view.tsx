import { Clock, CheckCircle2, ShieldCheck, LogOut, RefreshCw } from "lucide-react";
import Link from "next/link";
import { logout } from "@/app/(auth)/actions";
import { fmtDate } from "@/lib/ui-format";

interface PendingPlanViewProps {
  userName?: string | null;
  createdAt?: Date | null;
  examDate?: Date | null;
  hoursPerWeek?: number | null;
}

export function PendingPlanView({
  userName,
  createdAt,
  examDate,
  hoursPerWeek,
}: PendingPlanViewProps) {
  const firstName = userName ? userName.split(" ")[0] : "aluno";

  const requestDateFormatted = createdAt
    ? new Intl.DateTimeFormat("pt-BR", {
        timeZone: "America/Recife",
        dateStyle: "long",
        timeStyle: "short",
      }).format(new Date(createdAt))
    : "Recentemente";

  return (
    <div className="mx-auto max-w-3xl space-y-8 py-4 sm:py-8">
      {/* Banner de status */}
      <div className="relative overflow-hidden rounded-3xl bg-ink p-7 text-on-ink sm:p-11 shadow-xl border border-gold/20">
        <div
          className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-gold/15 blur-3xl"
          aria-hidden
        />
        <div
          className="pointer-events-none absolute -left-20 -bottom-20 h-72 w-72 rounded-full bg-primary/20 blur-3xl"
          aria-hidden
        />

        <div className="relative space-y-6">
          <div className="inline-flex items-center gap-2 rounded-full border border-gold/40 bg-gold/10 px-3.5 py-1 text-xs sm:text-sm font-semibold text-gold">
            <span className="relative flex h-2 w-2">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-gold opacity-75" />
              <span className="relative inline-flex h-2 w-2 rounded-full bg-gold" />
            </span>
            Perfil em calibração individual
          </div>

          <div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold uppercase leading-tight tracking-tight">
              Olá, {firstName}!
            </h1>
            <p className="mt-4 text-base sm:text-lg leading-relaxed text-on-ink-muted">
              Estamos analisando suas informações e seu perfil de estudos para preparar um planejamento personalizado para você. Seu plano estará disponível na plataforma em até 24 horas. Você poderá retornar a esta página para acompanhar a disponibilização.
            </p>
          </div>

          <div className="grid gap-3 pt-2 sm:grid-cols-2">
            <div className="rounded-xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm">
              <div className="flex items-center gap-2.5 text-xs uppercase tracking-wider text-on-ink-muted">
                <Clock className="h-4 w-4 text-gold" aria-hidden />
                Horário da solicitação
              </div>
              <p className="mt-1.5 font-display text-base font-bold text-on-ink">
                {requestDateFormatted}
              </p>
            </div>

            <div className="rounded-xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm">
              <div className="flex items-center gap-2.5 text-xs uppercase tracking-wider text-on-ink-muted">
                <ShieldCheck className="h-4 w-4 text-emerald-400" aria-hidden />
                Previsão de disponibilização
              </div>
              <p className="mt-1.5 font-display text-base font-bold text-on-ink">
                Em até 24 horas
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Cartão de confirmação de dados salvos */}
      <div className="rounded-2xl border border-border bg-surface p-6 sm:p-8 shadow-sm space-y-5">
        <div className="flex items-start gap-3.5">
          <CheckCircle2 className="mt-0.5 h-6 w-6 shrink-0 text-emerald-600" aria-hidden />
          <div className="space-y-1">
            <h2 className="font-display text-xl font-bold uppercase text-text">
              Suas informações foram registradas com segurança
            </h2>
            <p className="text-sm text-muted leading-relaxed">
              Todos os seus dados de anamnese, disciplinas selecionadas, carga horária pretendida e data da prova foram salvos. Você não precisará preencher o formulário novamente.
            </p>
          </div>
        </div>

        {(examDate || hoursPerWeek) && (
          <div className="rounded-xl bg-surface-muted/60 p-4 text-sm flex flex-wrap gap-x-8 gap-y-2 border border-border/60">
            {examDate && (
              <div>
                <span className="text-muted">Data da prova cadastrada: </span>
                <span className="font-semibold text-text">{fmtDate(examDate)}</span>
              </div>
            )}
            {hoursPerWeek && (
              <div>
                <span className="text-muted">Ritmo semanal: </span>
                <span className="font-semibold text-text">{hoursPerWeek} horas semanais</span>
              </div>
            )}
          </div>
        )}

        <div className="flex flex-wrap items-center justify-between gap-3 pt-2 border-t border-border/80">
          <Link
            href="/plano"
            className="inline-flex items-center gap-2 rounded-xl bg-primary px-4 py-2.5 text-sm font-bold uppercase text-on-primary shadow-sm hover:opacity-90 transition"
          >
            <RefreshCw className="h-4 w-4" aria-hidden />
            Verificar disponibilidade
          </Link>

          <form action={logout}>
            <button
              type="submit"
              className="inline-flex items-center gap-2 rounded-xl border border-border px-4 py-2.5 text-sm font-semibold text-muted hover:bg-surface-muted hover:text-text transition cursor-pointer"
            >
              <LogOut className="h-4 w-4" aria-hidden />
              Sair da plataforma
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
