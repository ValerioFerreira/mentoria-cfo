import { CalendarOff, ChevronLeft, ChevronRight } from "lucide-react";
import type { Metadata } from "next";
import { notFound, redirect } from "next/navigation";
import { ActivityCard, ActivityRow, fmtMinutes } from "@/components/activity-row";
import { Badge, Card, EmptyState, InfoTip, LinkButton, PageHeader, Progress, Ring, TYPE_META, cx, type ActivityType } from "@/components/ui";
import { activityDetail } from "@/lib/activity-detail";
import { requireUser } from "@/lib/auth/dal";
import { getActivePlan, getWeek } from "@/lib/data/study";
import { dateOfPlanDay, firstStudyISO, effectiveDays, planPosition, shortDate, todayISO, weekdayName } from "@/lib/plan-time";
import { fmtDuration, weekRange } from "@/lib/ui-format";

export const metadata: Metadata = { title: "Meta semanal" };

export default async function WeekPage({ params }: PageProps<"/semana/[n]">) {
  const user = await requireUser();
  const { n } = await params;
  const index = Number(n);
  if (!Number.isInteger(index) || index < 1) notFound();
  const plan = await getActivePlan(user.id);
  if (!plan) redirect("/onboarding");
  const data = await getWeek(user.id, plan.id, index);
  if (!data) notFound();
  const { week, seconds } = data;

  const startIso = plan.startDate.toISOString().slice(0, 10);
  const today = todayISO();
  const pos = planPosition(startIso, plan.weeks.length, today, firstStudyISO(plan));
  const nowWeek = pos.week;
  const isNow = pos.state === "during" && index === nowWeek;

  const acts = effectiveDays(week.activities).map((a) => ({ ...a, detail: activityDetail(a) }));
  const done = acts.filter((a) => a.status === "DONE").length;
  const studied = acts.reduce((n2, a) => n2 + (seconds.get(a.id) ?? 0), 0);
  const ratio = acts.length ? done / acts.length : 0;
  const plannedMin = acts.reduce((n2, a) => n2 + a.plannedMinutes, 0);
  const byType = (["TEORIA", "REVISAO", "FIXACAO", "QUESTOES"] as ActivityType[]).map((t) => ({ t, n: acts.filter((a) => a.type === t).length })).filter((x) => x.n > 0);

  const days = Array.from({ length: 7 }, (_, d) => {
    const list = acts.filter((a) => a.day === d);
    const date = dateOfPlanDay(startIso, index, d);
    const dayDone = list.filter((a) => a.status === "DONE").length;
    return { d, date, list, minutes: list.reduce((n2, a) => n2 + a.plannedMinutes, 0), done: dayDone, isToday: date === today, past: date < today };
  });
  const maxMinutes = Math.max(1, ...days.map((x) => x.minutes));

  return (
    <div className="space-y-7">
      <PageHeader
        eyebrow={week.kind === "FINAL_REVIEW" ? "Revisão final" : isNow ? "Semana atual" : weekRange(week.startDate)}
        title={<>Meta semanal</>}
        info="Os dias seguem uma lógica: revisões vêm no dia seguinte à teoria, cadernos de questões depois das revisões e o domingo fica leve. Cada disciplina aparece em dias diferentes para você lembrar melhor."
        actions={
          <nav className="flex flex-wrap items-center gap-2" aria-label="Navegar entre semanas">
            <LinkButton href={`/semana/${Math.max(1, index - 1)}`} variant="secondary" aria-disabled={index === 1} className={index === 1 ? "pointer-events-none opacity-40" : ""}>
              <ChevronLeft className="h-4 w-4" aria-hidden />
              <span className="sr-only">Semana anterior</span>
            </LinkButton>
            <span className="min-w-28 px-1 text-center">
              <span className="block font-display text-2xl font-bold uppercase leading-none tabular">Semana {week.index}<span className="text-muted"> / {plan.weeks.length}</span></span>
              <span className="block text-xs text-muted tabular">{weekRange(week.startDate)}</span>
            </span>
            <LinkButton href={`/semana/${Math.min(plan.weeks.length, index + 1)}`} variant="secondary" aria-disabled={index === plan.weeks.length} className={index === plan.weeks.length ? "pointer-events-none opacity-40" : ""}>
              <ChevronRight className="h-4 w-4" aria-hidden />
              <span className="sr-only">Próxima semana</span>
            </LinkButton>
            {!isNow && pos.state === "during" && <LinkButton href={`/semana/${nowWeek}`} variant="ghost">Ir para a atual</LinkButton>}
          </nav>
        }
      />

      <Card className="rise flex flex-wrap items-center gap-6">
        <Ring value={ratio} size={92} stroke={10} color={ratio >= 1 ? "var(--ok)" : "var(--primary)"} label={`${done} de ${acts.length} atividades concluídas`}>
          <span className="font-display text-3xl font-bold leading-none tabular">{Math.round(ratio * 100)}<span className="text-base text-muted">%</span></span>
        </Ring>
        <div className="min-w-[14rem] flex-1 space-y-2.5">
          <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1 text-sm">
            <span><strong className="font-display text-2xl tabular">{done}</strong> <span className="text-muted">de {acts.length} atividades concluídas</span></span>
            <span className="inline-flex items-center gap-1.5 text-muted tabular">
              <strong className="text-text">{fmtDuration(studied)}</strong> lançados · meta {fmtMinutes(plannedMin)}
              <InfoTip align="end">Soma dos tempos que você lançou nas atividades desta semana, comparada ao tempo planejado.</InfoTip>
            </span>
          </div>
          <Progress value={plannedMin ? studied / (plannedMin * 60) : 0} color="var(--gold)" tape label="Tempo lançado em relação à meta" />
          <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-muted">
            {byType.map(({ t, n: count }) => (
              <span key={t} className="inline-flex items-center gap-1.5">
                <span className="h-2 w-2 rounded-full" style={{ background: TYPE_META[t].color }} aria-hidden />
                {count} {TYPE_META[t].label}
              </span>
            ))}
          </div>
        </div>
      </Card>

      {acts.length === 0 ? (
        <EmptyState icon={<CalendarOff className="h-6 w-6" aria-hidden />} title="Semana livre">
          Esta semana não tem atividades planejadas. Use o tempo para recuperar atrasos.
        </EmptyState>
      ) : (
        <>
          {/* telas largas: cronologia da semana em 7 colunas */}
          <ol className="hidden grid-cols-7 gap-2.5 lg:grid" aria-label="Dias da semana">
            {days.map((day) => (
              <li key={day.d} className={cx("flex min-w-0 flex-col gap-2 rounded-2xl border p-2 pt-0", day.isToday ? "border-gold bg-gold-soft/40" : "border-border bg-surface-2/60")}>
                <div className="px-1.5 pt-2.5">
                  <div className="flex items-baseline justify-between gap-1">
                    <span className="font-display text-lg font-bold uppercase leading-none tracking-wide">{weekdayName(day.d).slice(0, 3)}</span>
                    <span className="text-[11px] font-semibold text-muted tabular">{shortDate(day.date)}</span>
                  </div>
                  <div className="mt-1.5 h-1.5 overflow-hidden rounded-full bg-surface-3" aria-hidden>
                    <div className="h-full rounded-full" style={{ width: `${(day.minutes / maxMinutes) * 100}%`, background: day.isToday ? "var(--gold)" : "var(--primary)", opacity: day.past ? 0.5 : 1 }} />
                  </div>
                  <p className="mt-1 flex items-center justify-between text-[11px] text-muted tabular">
                    <span>{day.minutes ? fmtMinutes(day.minutes) : "livre"}</span>
                    {day.list.length > 0 && <span className={cx(day.done === day.list.length && "font-bold text-ok")}>{day.done}/{day.list.length}</span>}
                  </p>
                  {day.isToday && <Badge tone="gold" className="mt-1.5">hoje</Badge>}
                </div>
                <div className="flex flex-1 flex-col gap-2">
                  {day.list.map((a, i) => (
                    <ActivityCard key={a.id} a={a} spent={seconds.get(a.id) ?? 0} index={day.d + i} late={day.past && (a.status === "PENDING" || a.status === "IN_PROGRESS")} />
                  ))}
                </div>
              </li>
            ))}
          </ol>

          {/* celular e tablet: agenda dia a dia */}
          <ol className="space-y-6 lg:hidden" aria-label="Dias da semana">
            {days.filter((day) => day.list.length > 0).map((day) => (
              <li key={day.d} className="space-y-2.5">
                <div className="flex items-center justify-between gap-3">
                  <h2 className="flex items-center gap-2 font-display text-2xl font-bold uppercase tracking-wide">
                    {weekdayName(day.d)}
                    <span className="text-sm font-semibold text-muted tabular">{shortDate(day.date)}</span>
                    {day.isToday && <Badge tone="gold">hoje</Badge>}
                  </h2>
                  <span className="text-xs font-semibold text-muted tabular">{fmtMinutes(day.minutes)} · {day.done}/{day.list.length}</span>
                </div>
                {day.list.map((a, i) => (
                  <ActivityRow key={a.id} a={a} spent={seconds.get(a.id) ?? 0} index={i} />
                ))}
              </li>
            ))}
          </ol>
        </>
      )}
    </div>
  );
}
