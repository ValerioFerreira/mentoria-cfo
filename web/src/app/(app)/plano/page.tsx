import { CalendarClock, CheckCheck, Gauge, Hourglass, RefreshCw, Sparkles } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { redirect } from "next/navigation";
import type { CSSProperties } from "react";
import { fmtMinutes } from "@/components/activity-row";
import { Alert, BLOCK_COLOR, Badge, Card, Count, InfoTip, LinkButton, PageHeader, Progress, Ring, SectionTitle, TYPE_META, type ActivityType } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { getActivePlan } from "@/lib/data/study";
import { LEVEL_LABEL } from "@/lib/diagnostic";
import { DAY_WEIGHTS } from "@/lib/planner/constants";
import { firstStudyISO, planPosition, todayISO } from "@/lib/plan-time";
import { fmtDate, subjectShort, weekRange } from "@/lib/ui-format";
import type { Level, PlanResult } from "@/lib/planner/types";

export const metadata: Metadata = { title: "Planejamento" };

const TYPES: ActivityType[] = ["TEORIA", "REVISAO", "FIXACAO", "QUESTOES"];
const hm = (min: number) => {
  const h = Math.floor(min / 60);
  const m = Math.round(min % 60);
  return m === 0 ? `${h} h` : `${h}h${String(m).padStart(2, "0")}`;
};

export default async function PlanPage() {
  const user = await requireUser();
  const plan = await getActivePlan(user.id);
  if (!plan) redirect("/onboarding");

  const params = plan.params as unknown as PlanResult["params"];
  const coverage = plan.coverage as unknown as PlanResult["coverage"];
  // avisos antigos que repetiam o que os cartões já mostram não aparecem mais
  const warnings = (plan.warnings as unknown as string[]).filter((w) => !w.startsWith("Lacuna no material") && !w.startsWith("O tempo é curto") && !w.startsWith("Cobertura estimada de"));
  const pos = planPosition(plan.startDate.toISOString().slice(0, 10), plan.weeks.length, todayISO(), firstStudyISO(plan));
  const levelOf = new Map(plan.subjects.map((s) => [s.subjectId, s.level as Level]));
  const blockOf = new Map(plan.subjects.map((s) => [s.subjectId, s.subject.block as "I" | "II" | "III"]));
  const authored = new Set((await db.aula.findMany({ where: { source: "AUTHORED" }, select: { id: true } })).map((a) => a.id));

  const all = plan.weeks.flatMap((w) => w.activities);
  const doneActs = all.filter((a) => a.status === "DONE");
  const plannedMin = all.reduce((n, a) => n + a.plannedMinutes, 0);
  const doneMin = doneActs.reduce((n, a) => n + a.plannedMinutes, 0);
  const byType = TYPES.map((t) => ({ t, min: all.filter((a) => a.type === t).reduce((n, a) => n + a.plannedMinutes, 0) }));
  const weeklyMin = params.weeklyMinutes ?? Math.round(params.slotsPerWeek * 60);
  const completion = all.length ? doneActs.length / all.length : 0;
  // prática (fixação + cadernos, inclusive os cadernos mistos da revisão final) por disciplina
  const minutesBy = new Map<string, { practice: number; total: number }>();
  for (const a of all) {
    const m = minutesBy.get(a.subjectId) ?? { practice: 0, total: 0 };
    m.total += a.plannedMinutes;
    if (a.type === "FIXACAO" || a.type === "QUESTOES") m.practice += a.plannedMinutes;
    minutesBy.set(a.subjectId, m);
  }

  return (
    <div className="space-y-9">
      <PageHeader
        eyebrow={`Prova em ${fmtDate(plan.examDate)}`}
        title="Planejamento"
        actions={
          <>
            <LinkButton href="/semana">Ver a semana atual</LinkButton>
            <LinkButton href="/onboarding" variant="secondary">
              <RefreshCw className="h-4 w-4" aria-hidden />
              Refazer plano
            </LinkButton>
          </>
        }
      />

      <div className="grid gap-4 lg:grid-cols-[minmax(0,19rem)_1fr]">
        <Card tone="ink" className="rise flex flex-col items-center gap-3 text-center">
          <Ring value={coverage.selected} size={150} stroke={14} color="var(--gold)" track="rgb(255 255 255 / 0.12)" label={`Cobertura estimada do edital: ${Math.round(coverage.selected * 100)}%`}>
            <span className="font-display text-6xl font-bold leading-none"><Count value={Math.round(coverage.selected * 100)} suffix="%" /></span>
          </Ring>
          <p className="eyebrow flex items-center gap-1.5 !text-on-ink-muted">
            Cobertura estimada do edital
            <InfoTip align="center">
              Parte do edital das suas disciplinas que o plano faz você estudar até a prova, ponderada pelo número de questões de cada uma. Aulas que você marcou como dominadas já contam como cobertas.
            </InfoTip>
          </p>
        </Card>

        <div className="grid gap-3 sm:grid-cols-3">
          {/* meta semanal */}
          <Card className="rise flex flex-col justify-between gap-4 p-5" style={{ "--i": 1 } as CSSProperties}>
            <div className="flex items-start justify-between">
              <p className="eyebrow flex items-center gap-1.5">
                Meta semanal
                <InfoTip align="start">Horas que o plano separa por semana: as {params.hoursPerWeek} h que você informou, menos 10% de folga para imprevistos. O domingo é o dia mais leve.</InfoTip>
              </p>
              <Gauge className="h-4 w-4 text-muted" aria-hidden />
            </div>
            <div>
              <p className="font-display text-5xl font-bold leading-none tabular">{hm(weeklyMin)}</p>
              <p className="mt-1.5 text-xs text-muted">por semana · de {params.hoursPerWeek} h disponíveis</p>
            </div>
            <div className="flex h-10 items-end gap-1" role="img" aria-label="Distribuição da meta pelos dias da semana">
              {DAY_WEIGHTS.map((w, d) => (
                <div key={d} className="flex h-full flex-1 flex-col items-center justify-end gap-1">
                  <div className="bar-grow w-full rounded-sm bg-primary" style={{ height: `${w * 100}%`, opacity: w < 1 ? 0.45 : 0.9, "--delay": `${d * 50}ms` } as CSSProperties} />
                </div>
              ))}
            </div>
            <div className="-mt-3 flex gap-1 text-[10px] font-semibold text-muted">
              {["S", "T", "Q", "Q", "S", "S", "D"].map((l, i) => <span key={i} className="flex-1 text-center">{l}</span>)}
            </div>
          </Card>

          {/* estudo planejado */}
          <Card className="rise flex flex-col justify-between gap-4 p-5" style={{ "--i": 2 } as CSSProperties}>
            <div className="flex items-start justify-between">
              <p className="eyebrow flex items-center gap-1.5">
                Estudo planejado
                <InfoTip align="start">Total de horas de todas as atividades do plano ({params.contentWeeks} semanas de conteúdo e {params.reviewWeeks} de revisão geral), separado por tipo.</InfoTip>
              </p>
              <Hourglass className="h-4 w-4 text-muted" aria-hidden />
            </div>
            <div>
              <p className="font-display text-5xl font-bold leading-none tabular">{hm(plannedMin)}</p>
              <p className="mt-1.5 text-xs text-muted">{all.length} atividades</p>
            </div>
            <div className="space-y-2">
              <div className="flex h-2.5 overflow-hidden rounded-full bg-surface-3" role="img" aria-label="Horas planejadas por tipo de atividade">
                {byType.map(({ t, min }) => (
                  <span key={t} className="h-full" style={{ width: `${plannedMin ? (min / plannedMin) * 100 : 0}%`, background: TYPE_META[t].color }} />
                ))}
              </div>
              <ul className="grid grid-cols-2 gap-x-3 gap-y-0.5 text-[11px] text-muted">
                {byType.map(({ t, min }) => (
                  <li key={t} className="flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full" style={{ background: TYPE_META[t].color }} aria-hidden />
                    {TYPE_META[t].label} <span className="ml-auto whitespace-nowrap font-semibold text-text tabular">{hm(min)}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Card>

          {/* concluído */}
          <Card className="rise flex flex-col justify-between gap-4 p-5" style={{ "--i": 3 } as CSSProperties}>
            <div className="flex items-start justify-between">
              <p className="eyebrow flex items-center gap-1.5">
                Concluído
                <InfoTip align="end">Atividades marcadas como concluídas e as horas que elas representam no plano (não é o tempo lançado).</InfoTip>
              </p>
              <CheckCheck className="h-4 w-4 text-muted" aria-hidden />
            </div>
            <div className="flex items-center gap-4">
              <Ring value={completion} size={84} stroke={9} color={completion >= 1 ? "var(--ok)" : "var(--primary)"} label={`${doneActs.length} de ${all.length} atividades concluídas`}>
                <span className="font-display text-2xl font-bold leading-none tabular">{Math.round(completion * 100)}<span className="text-sm text-muted">%</span></span>
              </Ring>
              <div>
                <p className="font-display text-4xl font-bold leading-none tabular">{doneActs.length}<span className="text-xl text-muted">/{all.length}</span></p>
                <p className="mt-1 text-xs text-muted">atividades</p>
              </div>
            </div>
            <p className="text-xs text-muted"><strong className="text-text tabular">{hm(doneMin)}</strong> de {hm(plannedMin)} do plano</p>
          </Card>
        </div>
      </div>

      {warnings.length > 0 && (
        <div className="space-y-2">
          {warnings.map((w) => (
            <Alert key={w}>{w}</Alert>
          ))}
        </div>
      )}

      <section aria-labelledby="cov">
        <SectionTitle
          id="cov"
          info="Cobertura é a parte do edital da disciplina que o plano faz você ver. Prática soma as horas de fixação e de cadernos de questões (inclusive os cadernos mistos da revisão final); a barra cheia equivale a metade do tempo da disciplina. Disciplinas com mais questões na prova têm prioridade."
        >
          Cobertura por disciplina
        </SectionTitle>
        <div className="grid gap-3 md:grid-cols-2">
          {coverage.subjects
            .slice()
            .sort((a, b) => b.examQuestions - a.examQuestions || b.plannedHours - a.plannedHours)
            .map((s, i) => {
              const color = BLOCK_COLOR[blockOf.get(s.subjectId) ?? "I"];
              const hasAuthored = s.aulas.some((a) => authored.has(a.aulaId));
              const mins = minutesBy.get(s.subjectId) ?? { practice: 0, total: 0 };
              const practiceMin = mins.practice;
              const practiceShare = mins.total ? Math.min(1, (mins.practice / mins.total) * 2) : 0; // barra cheia = metade do tempo em prática
              return (
                <Card key={s.subjectId} className="rise space-y-3 p-4" style={{ "--i": Math.min(i, 10) } as CSSProperties}>
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <p className="flex items-center gap-2 font-display text-2xl font-bold uppercase leading-none tracking-wide">
                        <span className="h-3 w-3 shrink-0 rounded-[4px]" style={{ background: color }} aria-hidden />
                        {subjectShort(s.subjectId)}
                      </p>
                      <p className="mt-1.5 text-xs text-muted">{s.examQuestions} {s.examQuestions === 1 ? "questão" : "questões"} na prova · {s.aulas.length} aulas · {Math.round(s.plannedHours)} h planejadas</p>
                    </div>
                    <div className="text-right">
                      <p className="font-display text-3xl font-bold leading-none tabular">{Math.round(s.coverage * 100)}%</p>
                      <p className="mt-0.5 text-xs text-muted">cobertura</p>
                    </div>
                  </div>
                  <Progress value={s.coverage} color={color} delay={i * 40} label={`Cobertura de ${subjectShort(s.subjectId)}`} />
                  <div className="flex items-center gap-3">
                    <Progress value={practiceShare} color="var(--questoes)" size="sm" className="flex-1" label={`Prática em ${subjectShort(s.subjectId)}`} />
                    <span className="shrink-0 text-xs text-muted tabular">{hm(practiceMin)} de prática</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5">
                    <Badge>{LEVEL_LABEL[levelOf.get(s.subjectId) ?? 0]}</Badge>
                    {hasAuthored && (
                      <Badge tone="gold">
                        <Sparkles className="h-3 w-3" aria-hidden />
                        material complementar MentorIA
                      </Badge>
                    )}
                  </div>
                </Card>
              );
            })}
        </div>
      </section>

      <section aria-labelledby="sem">
        <SectionTitle id="sem" aside={<span className="inline-flex items-center gap-1"><CalendarClock className="h-3.5 w-3.5" aria-hidden />{plan.weeks.length} semanas</span>}>Semanas</SectionTitle>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
          {plan.weeks.map((w, i) => {
            const subjects = [...new Set(w.activities.map((a) => a.subjectId))];
            const wDone = w.activities.filter((a) => a.status === "DONE").length;
            const ratio = w.activities.length ? wDone / w.activities.length : 0;
            const isNow = pos.state === "during" && w.index === pos.week;
            const wMin = w.activities.reduce((n, a) => n + a.plannedMinutes, 0);
            return (
              <Link
                key={w.id}
                href={`/semana/${w.index}`}
                className={`card-hover rise group relative block overflow-hidden rounded-2xl border bg-surface p-4 shadow-card ${isNow ? "border-gold ring-2 ring-gold/40" : "border-border"}`}
                style={{ "--i": Math.min(i, 12) } as CSSProperties}
              >
                {w.kind === "FINAL_REVIEW" && <span className="tape-soft absolute inset-x-0 top-0 h-1.5" aria-hidden />}
                <div className="flex items-start justify-between gap-2">
                  <div>
                    <p className="eyebrow">Semana</p>
                    <p className="font-display text-5xl font-bold leading-[0.9] tabular">{w.index}</p>
                  </div>
                  <Ring value={ratio} size={44} stroke={5} color={ratio >= 1 ? "var(--ok)" : "var(--primary)"} label={`${wDone} de ${w.activities.length} concluídas`}>
                    <span className="text-[10px] font-bold tabular">{wDone}/{w.activities.length}</span>
                  </Ring>
                </div>
                <p className="mt-2 text-xs text-muted tabular">{weekRange(w.startDate)} · {fmtMinutes(wMin)}</p>
                <p className="mt-1 line-clamp-2 min-h-8 text-xs font-medium leading-4">{subjects.map(subjectShort).join(" · ")}</p>
                <div className="mt-2 flex gap-1">
                  {isNow && <Badge tone="gold">agora</Badge>}
                  {w.kind === "FINAL_REVIEW" && <Badge tone="revisao">revisão final</Badge>}
                  {ratio >= 1 && <Badge tone="ok">completa</Badge>}
                </div>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
