import { CalendarRange, ClipboardCheck, PartyPopper, Rocket, Target, TriangleAlert } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import type { CSSProperties } from "react";
import { AdvanceBox } from "@/components/advance-box";
import { ActivityRow, activityTitle, fmtMinutes } from "@/components/activity-row";
import { Card, EmptyState, LinkButton, PageHeader, Progress } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getMission } from "@/lib/data/mission";
import { getActivePlan } from "@/lib/data/study";
import { dayOfWeekIndex, longDate, shortDate, weekdayName } from "@/lib/plan-time";

export const metadata: Metadata = { title: "Missão de hoje" };

export default async function MissionPage() {
  const user = await requireUser();
  const first = user.name?.split(" ")[0] ?? "aluno";
  const plan = await getActivePlan(user.id);

  if (!plan) {
    return (
      <div className="mx-auto max-w-3xl space-y-8 py-6">
        <section className="relative overflow-hidden rounded-3xl bg-ink p-8 text-on-ink sm:p-12">
          <div className="pointer-events-none absolute -right-24 -top-24 h-80 w-80 rounded-full bg-primary/30 blur-3xl" aria-hidden />
          <div className="tape tape-rule absolute inset-x-0 top-0 !rounded-none" aria-hidden />
          <p className="eyebrow !text-on-ink-muted">Bem-vindo, {first}</p>
          <h1 className="mt-2 font-display text-5xl font-bold uppercase leading-[0.95] sm:text-7xl">Monte a sua<br />missão oficial</h1>
          <p className="mt-4 max-w-lg text-on-ink-muted">Escolha as disciplinas, conte o que já estudou e o tempo que tem por semana. O MentorIA monta cada dia até a prova, com o que estudar em cada atividade.</p>
          <LinkButton href="/onboarding" size="lg" className="mt-7">
            <Rocket className="h-5 w-5" aria-hidden />
            Montar meu plano
          </LinkButton>
        </section>
        <ul className="grid gap-3 sm:grid-cols-3">
          {[
            ["Anamnese rápida", "O que você já estudou encurta o plano.", Target],
            ["Missão de cada dia", "Poucas atividades, na ordem que mais fixa.", CalendarRange],
            ["Cadernos de 25 questões", "5 alternativas, 60 minutos, como na prova.", ClipboardCheck],
          ].map(([t, d, Icon], i) => {
            const I = Icon as typeof Target;
            return (
              <li key={String(t)} className="rise" style={{ "--i": i + 2 } as CSSProperties}>
                <Card className="h-full space-y-2 p-4">
                  <I className="h-5 w-5 text-primary" aria-hidden />
                  <p className="font-display text-lg font-bold uppercase tracking-wide">{String(t)}</p>
                  <p className="text-sm text-muted">{String(d)}</p>
                </Card>
              </li>
            );
          })}
        </ul>
      </div>
    );
  }

  const m = await getMission(user.id, plan);
  const done = m.rows.filter((r) => r.status === "DONE").length;
  const total = m.rows.length;
  const open = m.rows.filter((r) => r.status === "PENDING" || r.status === "IN_PROGRESS");
  const plannedMin = m.rows.reduce((n, r) => n + r.plannedMinutes, 0);
  const shownLate = m.overdue.slice(0, 5);
  const upLabel = m.upcomingDate ? `${weekdayName((m.upcoming[0]?.day ?? 0))}, ${shortDate(m.upcomingDate)}` : "";
  const upItems = m.upcoming.map((r) => ({ id: r.id, type: r.type, subjectId: r.subjectId, title: activityTitle(r), minutes: r.plannedMinutes }));

  return (
    <div className="mx-auto max-w-3xl space-y-7">
      <PageHeader
        eyebrow={longDate(m.today)}
        title="Missão de hoje"
        info="Cada dia do plano foi montado para intercalar disciplinas diferentes, revisar no dia seguinte à teoria e deixar as questões para depois da revisão. Siga a ordem da lista."
      />

      {m.pos.state === "before" && (
        <Card tone="soft" className="rise">
          <p className="font-display text-2xl font-bold uppercase tracking-wide">O plano começa em {weekdayName(dayOfWeekIndex(m.firstStudy)).toLowerCase()}, {shortDate(m.firstStudy)}</p>
          <p className="mt-1 text-sm text-muted">Até lá, descanse ou adiante com calma o primeiro dia.</p>
        </Card>
      )}

      {m.pos.state === "after" && (
        <Card tone="soft" className="rise">
          <p className="font-display text-2xl font-bold uppercase tracking-wide">O plano terminou</p>
          <p className="mt-1 text-sm text-muted">A data da prova passou. Confira o seu desempenho final.</p>
          <LinkButton href="/desempenho" variant="secondary" className="mt-3">Ver desempenho</LinkButton>
        </Card>
      )}

      {m.overdue.length > 0 && (
        <section aria-labelledby="late" className="space-y-2.5">
          <div className="flex items-start gap-3 rounded-xl bg-warn-soft px-4 py-3 text-sm text-warn" role="note">
            <TriangleAlert className="mt-0.5 h-4 w-4 shrink-0" aria-hidden />
            <div>
              <h2 id="late" className="font-semibold">{m.overdue.length} {m.overdue.length === 1 ? "atividade atrasada" : "atividades atrasadas"}</h2>
              <p>Faça estas primeiro: a revisão perde efeito quanto mais tarde acontece.</p>
            </div>
          </div>
          {[...new Set(shownLate.map((r) => r.date))].map((date) => {
            const dayRows = shownLate.filter((r) => r.date === date);
            return (
              <div key={date} className="space-y-2">
                <p className="px-1 text-[11px] font-semibold uppercase tracking-wider text-muted">{weekdayName(dayRows[0].day)}, {shortDate(date)}</p>
                {dayRows.map((r, i) => (
                  <ActivityRow key={r.id} a={r} spent={r.spent} index={i} />
                ))}
              </div>
            );
          })}
          {m.overdue.length > shownLate.length && (
            <p className="px-1 text-sm text-muted">
              e mais {m.overdue.length - shownLate.length} na <Link href="/semana" className="font-semibold text-primary hover:underline">Meta semanal</Link>.
            </p>
          )}
        </section>
      )}

      {m.pos.state === "during" && (
        <section aria-labelledby="hoje" className="space-y-3">
          <h2 id="hoje" className="sr-only">Atividades de hoje</h2>
          {total > 0 && (
            <div className="flex items-center gap-4">
              <Progress value={total ? done / total : 0} color={done === total ? "var(--ok)" : "var(--primary)"} size="md" label="Atividades de hoje concluídas" className="flex-1" />
              <p className="shrink-0 text-sm font-semibold text-muted tabular">
                <span className="text-text">{done}</span> de {total} · {fmtMinutes(plannedMin)}
              </p>
            </div>
          )}
          {total === 0 ? (
            <EmptyState icon={<PartyPopper className="h-6 w-6" aria-hidden />} title="Dia livre">Nada planejado para hoje. Descanse: o sono também consolida o que você estudou.</EmptyState>
          ) : (
            <ol className="space-y-2.5">
              {m.rows.map((r, i) => (
                <li key={r.id}>
                  <ActivityRow a={r} spent={r.spent} order={i + 1} index={i} />
                </li>
              ))}
            </ol>
          )}
          {total > 0 && open.length === 0 && (
            <Card className="rise flex items-center gap-4" style={{ "--i": 3 } as CSSProperties}>
              <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-ok/12 text-ok"><PartyPopper className="h-6 w-6" aria-hidden /></span>
              <div>
                <p className="font-display text-2xl font-bold uppercase tracking-wide">Missão cumprida</p>
                <p className="text-sm text-muted">Bom trabalho, {first}. Lance o tempo estudado em cada atividade e descanse.</p>
              </div>
            </Card>
          )}
        </section>
      )}

      <AdvanceBox items={upItems} label={upLabel} />
    </div>
  );
}
