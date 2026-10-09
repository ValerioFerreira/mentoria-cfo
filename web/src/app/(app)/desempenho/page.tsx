import { CheckCircle2, ChevronRight, CircleAlert, CircleHelp, ClipboardList, Clock3, Flame, ListChecks, Target } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import type { CSSProperties } from "react";
import { Heatmap } from "@/components/heatmap";
import { Alert, BLOCK_COLOR, Badge, Card, Count, EmptyState, LinkButton, PageHeader, Progress, Ring, SectionTitle, Stat } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getPerformance } from "@/lib/data/performance";
import { getActivePlan } from "@/lib/data/study";
import { MIN_QUESTIONS_FOR_PROJECTION } from "@/lib/metrics";
import { dateOfPlanDay, firstStudyISO, effectiveDays, planPosition, todayISO } from "@/lib/plan-time";
import { fmtDuration, subjectName, subjectShort } from "@/lib/ui-format";

export const metadata: Metadata = { title: "Desempenho" };

const pct = (v: number | null) => (v === null ? "—" : `${Math.round(v * 100)}%`);
const num = (v: number) => (Number.isInteger(v) ? String(v) : v.toFixed(1).replace(".", ","));
const BLOCK = { I: "Bloco I", II: "Bloco II", III: "Bloco III" } as const;
const accColor = (v: number | null) => (v === null ? "var(--surface-3)" : v >= 0.7 ? "var(--ok)" : v >= 0.5 ? "var(--gold)" : "var(--primary)");

/** Faixa de domínio pelo acerto (a partir de 10 questões). A regra aparece no balão de ajuda da tabela. */
function mastery(acc: number | null, total: number): { label: string; tone: "ok" | "gold" | "warn" | "primary" | "neutral" } {
  if (acc === null || total < MIN_QUESTIONS_FOR_PROJECTION) return { label: "Poucos dados", tone: "neutral" };
  if (acc >= 0.85) return { label: "Dominado", tone: "ok" };
  if (acc >= 0.7) return { label: "Sólido", tone: "ok" };
  if (acc >= 0.5) return { label: "Em evolução", tone: "gold" };
  return { label: "Precisa de atenção", tone: "primary" };
}

export default async function PerformancePage() {
  const user = await requireUser();
  const plan = await getActivePlan(user.id);
  const planSubjects = plan?.subjects.map((s) => s.subjectId) ?? [];
  const totalWeeks = plan?.weeks.length ?? 0;
  const perf = await getPerformance(user.id, plan?.startDate ?? null, totalWeeks, planSubjects);
  const startIso = plan?.startDate.toISOString().slice(0, 10) ?? "";
  const today = todayISO();
  const pos = plan ? planPosition(startIso, totalWeeks, today, firstStudyISO(plan)) : null;
  const nowWeek = pos?.week ?? 0;
  const weekTarget = (i: number) => (plan?.weeks[i]?.targetMinutes ?? 0) * 60;
  const maxBar = Math.max(1, ...perf.byWeekSeconds, ...(plan?.weeks.map((w) => w.targetMinutes * 60) ?? [0]));
  const thisWeekSec = perf.thisWeekSeconds;

  // aderência: das atividades que já deveriam ter sido feitas (até hoje), quantas foram concluídas
  const due = plan ? plan.weeks.flatMap((w) => effectiveDays(w.activities).map((a) => ({ ...a, date: dateOfPlanDay(startIso, w.index, a.day) }))).filter((a) => a.date <= today) : [];
  const dueDone = due.filter((a) => a.status === "DONE").length;
  const adherence = due.length ? dueDone / due.length : null;
  const doneBySubject = new Map<string, { done: number; total: number }>();
  for (const a of plan?.weeks.flatMap((w) => w.activities) ?? []) {
    const c = doneBySubject.get(a.subjectId) ?? { done: 0, total: 0 };
    c.total++;
    if (a.status === "DONE") c.done++;
    doneBySubject.set(a.subjectId, c);
  }

  const rows = perf.subjects
    .filter((s) => planSubjects.includes(s.id) || perf.bySubjectSeconds.has(s.id) || perf.quizStats.has(s.id))
    .map((s) => ({ ...s, seconds: perf.bySubjectSeconds.get(s.id) ?? 0, q: perf.quizStats.get(s.id), act: doneBySubject.get(s.id) }));
  const unattached = perf.bySubjectSeconds.get("_none") ?? 0;
  const activeDays = perf.daily.filter((d) => d.seconds > 0).length;

  const totalPoints = perf.projection.reduce((n, b) => n + b.points, 0);
  const projectedTotal = perf.projection.every((b) => b.projected !== null) ? perf.projection.reduce((n, b) => n + b.projected!, 0) : null;
  const zeroed = perf.projection.flatMap((b) => b.subjects).filter((s) => s.projected !== null && s.projected === 0);

  return (
    <div className="space-y-10">
      <PageHeader
        eyebrow="Seus números"
        title="Desempenho"
        info="Tudo aqui nasce do que você registra: tempo lançado nas atividades, atividades concluídas e cadernos de questões finalizados."
        actions={!plan ? <LinkButton href="/onboarding">Montar meu plano</LinkButton> : undefined}
      />

      <div className="grid grid-cols-2 gap-3 lg:grid-cols-5">
        <Stat
          label="Tempo estudado"
          value={fmtDuration(perf.totalSeconds)}
          hint={plan ? `${fmtDuration(thisWeekSec)} esta semana · meta ${fmtDuration(weekTarget(nowWeek - 1))}` : unattached ? `${fmtDuration(unattached)} sem atividade` : "no total"}
          info="Soma dos tempos que você lançou nas atividades. O cronômetro flutuante não entra: ele é só um apoio."
          icon={<Clock3 className="h-4 w-4" aria-hidden />}
          delay={0}
          className="col-span-2 lg:col-span-1"
        />
        <Stat
          label="Aderência ao plano"
          value={adherence === null ? "—" : <Count value={Math.round(adherence * 100)} suffix="%" />}
          hint={due.length ? `${dueDone} de ${due.length} atividades vencidas` : "o plano ainda não começou"}
          info="Das atividades que já deveriam ter sido feitas até hoje, quantas você concluiu. Seguir o plano é o que mais pesa no resultado."
          icon={<ListChecks className="h-4 w-4" aria-hidden />}
          delay={1}
        />
        <Stat
          label="Questões resolvidas"
          value={<Count value={perf.questionsTotal} />}
          hint={perf.avgSecondsPerQuestion ? `${fmtDuration(perf.avgSecondsPerQuestion)} por questão` : "nos cadernos finalizados"}
          info="Questões apresentadas em cadernos finalizados, incluindo as deixadas em branco. O tempo por questão é a média."
          icon={<ClipboardList className="h-4 w-4" aria-hidden />}
          delay={2}
        />
        <Stat
          label="Taxa de acerto"
          value={perf.accuracy === null ? "—" : <Count value={Math.round(perf.accuracy * 100)} suffix="%" />}
          hint={perf.questionsTotal ? `${perf.questionsCorrect} acertos em ${perf.questionsTotal}` : "faça um caderno"}
          info="Acertos divididos por todas as questões apresentadas. Questão em branco conta como erro, como na prova."
          icon={<Target className="h-4 w-4" aria-hidden />}
          delay={3}
        />
        <Stat
          label="Sequência"
          value={<><Count value={perf.streak} /> <span className="text-xl text-muted">{perf.streak === 1 ? "dia" : "dias"}</span></>}
          hint="de estudo seguidos"
          info="Dias consecutivos com tempo lançado em alguma atividade."
          icon={<Flame className={`h-4 w-4 ${perf.streak ? "flame text-primary" : ""}`} aria-hidden />}
          delay={4}
          className="col-span-2 lg:col-span-1"
        />
      </div>

      <section aria-labelledby="edital" className="space-y-3">
        <SectionTitle
          id="edital"
          info="O edital elimina quem ficar abaixo de 30% dos pontos em qualquer bloco, quem zerar alguma disciplina ou quem ficar abaixo de 30% do total. Aqui estimamos seus acertos se você fizesse a prova hoje: seu percentual de acerto em cada disciplina (mínimo de 10 questões) vezes as questões que ela tem na prova. A linha marca o mínimo exigido (30%); quanto mais cadernos você fizer, mais precisa fica a estimativa."
        >
          Você passaria hoje? Critérios do edital
        </SectionTitle>
        <div className="grid gap-3 md:grid-cols-3">
          {perf.projection.map((b, i) => {
            const floor = b.points * 0.3;
            const ratio = b.projected === null || !b.points ? 0 : b.projected / b.points;
            return (
              <Card key={b.block} className="rise space-y-3" style={{ "--i": i + 1 } as CSSProperties}>
                <div className="flex items-center justify-between gap-2">
                  <h3 className="flex items-center gap-2 font-display text-2xl font-bold uppercase tracking-wide">
                    <span className="h-3 w-3 rounded-[4px]" style={{ background: BLOCK_COLOR[b.block] }} aria-hidden />
                    {BLOCK[b.block]}
                  </h3>
                  <Badge tone={b.status === "ok" ? "ok" : b.status === "risco" ? "warn" : "neutral"}>
                    {b.status === "ok" ? "acima do mínimo" : b.status === "risco" ? "abaixo do mínimo" : "sem dados"}
                  </Badge>
                </div>
                <p className="font-display text-4xl font-bold leading-none tabular">
                  {b.projected === null ? "—" : num(b.projected)}
                  <span className="text-base font-medium text-muted"> de {b.points} questões</span>
                </p>
                <div className="relative pb-5 pt-1">
                  <Progress value={ratio} color={b.status === "risco" ? "var(--primary)" : "var(--ok)"} size="lg" label={`Acertos estimados no ${BLOCK[b.block]}`} />
                  <span className="absolute top-0 h-5 w-px bg-text/70" style={{ left: "30%" }} aria-hidden />
                  <span className="absolute bottom-0 -translate-x-1/2 whitespace-nowrap text-[11px] font-semibold text-muted" style={{ left: "30%" }}>mínimo: {num(floor)} questões</span>
                </div>
                <ul className="divide-y divide-border text-sm">
                  {b.subjects.map((s) => (
                    <li key={s.id} className="flex items-center justify-between gap-3 py-1.5">
                      <span className="min-w-0">{subjectName(s.id)}</span>
                      <span className="max-w-[55%] text-right text-xs text-muted tabular">
                        {s.accuracy === null ? `faltam ${Math.max(0, MIN_QUESTIONS_FOR_PROJECTION - s.total)} questões para estimar` : <><strong className="text-text">{pct(s.accuracy)}</strong> → {num(s.projected!)} de {s.examQuestions}</>}
                      </span>
                    </li>
                  ))}
                </ul>
              </Card>
            );
          })}
        </div>
        <Card tone="soft" className="rise flex flex-wrap items-center gap-x-8 gap-y-2 py-3.5 text-sm" style={{ "--i": 4 } as CSSProperties}>
          <span className="flex items-center gap-2">
            {projectedTotal === null ? <CircleHelp className="h-4 w-4 text-muted" aria-hidden /> : projectedTotal / totalPoints >= 0.3 ? <CheckCircle2 className="h-4 w-4 text-ok" aria-hidden /> : <CircleAlert className="h-4 w-4 text-primary" aria-hidden />}
            <span><strong className="tabular">{projectedTotal === null ? "—" : num(projectedTotal)}</strong> de {totalPoints} questões no total · mínimo {num(totalPoints * 0.3)}</span>
          </span>
          <span className="flex items-center gap-2 text-muted">
            {zeroed.length ? <CircleAlert className="h-4 w-4 text-primary" aria-hidden /> : <CheckCircle2 className="h-4 w-4 text-ok" aria-hidden />}
            {zeroed.length ? `Disciplina zerada: ${zeroed.map((s) => subjectShort(s.id)).join(", ")}` : "Nenhuma disciplina zerada"}
          </span>
        </Card>
      </section>

      <section aria-labelledby="sub">
        <SectionTitle
          id="sub"
          info={`Faixas de domínio pela taxa de acerto, a partir de ${MIN_QUESTIONS_FOR_PROJECTION} questões: 85% ou mais = Dominado; 70% a 84% = Sólido; 50% a 69% = Em evolução; abaixo de 50% = Precisa de atenção.`}
        >
          Por disciplina
        </SectionTitle>
        {rows.length === 0 ? (
          <EmptyState icon={<ClipboardList className="h-6 w-6" aria-hidden />} title="Sem dados ainda">Lance o tempo das atividades e resolva cadernos para ver sua evolução por disciplina.</EmptyState>
        ) : (
          <Card className="rise overflow-x-auto p-0" style={{ "--i": 1 } as CSSProperties}>
            <table className="w-full min-w-[46rem] text-left text-sm">
              <thead>
                <tr className="border-b border-border text-xs uppercase tracking-wider text-muted">
                  <th className="px-5 py-3 font-semibold">Disciplina</th>
                  <th className="px-3 py-3 text-right font-semibold">Tempo estudado</th>
                  <th className="px-3 py-3 text-right font-semibold">Atividades concluídas</th>
                  <th className="px-3 py-3 text-right font-semibold">Questões resolvidas</th>
                  <th className="px-3 py-3 text-right font-semibold">Acertos</th>
                  <th className="w-48 px-3 py-3 font-semibold">Taxa de acerto</th>
                  <th className="px-5 py-3 font-semibold">Situação</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {rows.map((r, i) => {
                  const acc = r.q?.accuracy ?? null;
                  const mst = mastery(acc, r.q?.total ?? 0);
                  return (
                    <tr key={r.id} className="transition hover:bg-surface-2/60">
                      <td className="px-5 py-3.5 font-semibold">
                        <span className="flex items-center gap-2">
                          <span className="h-2.5 w-2.5 shrink-0 rounded-[3px]" style={{ background: BLOCK_COLOR[r.block as "I" | "II" | "III"] }} aria-hidden />
                          {r.name}
                        </span>
                      </td>
                      <td className="px-3 py-3.5 text-right tabular text-muted">{r.seconds ? fmtDuration(r.seconds) : "—"}</td>
                      <td className="px-3 py-3.5 text-right tabular text-muted">{r.act ? <>{r.act.done} <span className="opacity-70">de {r.act.total}</span></> : "—"}</td>
                      <td className="px-3 py-3.5 text-right tabular text-muted">{r.q?.total ?? 0}</td>
                      <td className="px-3 py-3.5 text-right tabular text-muted">{r.q?.correct ?? 0}</td>
                      <td className="px-3 py-3.5">
                        <div className="flex items-center gap-3">
                          <Progress value={acc ?? 0} color={accColor(acc)} delay={i * 30} label={`Taxa de acerto em ${r.name}`} className="flex-1" />
                          <span className="w-11 text-right font-display text-xl font-bold tabular">{pct(acc)}</span>
                        </div>
                      </td>
                      <td className="px-5 py-3.5"><Badge tone={mst.tone}>{mst.label}</Badge></td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </Card>
        )}
      </section>

      <div className="grid gap-6 lg:grid-cols-2">
        <section aria-labelledby="trend">
          <SectionTitle id="trend" info="Acerto de cada caderno finalizado, do mais antigo ao mais recente. A linha tracejada marca 70%, a meta para ficar tranquilo na prova." aside={`${perf.trend.length} ${perf.trend.length === 1 ? "caderno" : "cadernos"}`}>
            Evolução do acerto
          </SectionTitle>
          <Card className="rise" style={{ "--i": 2 } as CSSProperties}>
            {perf.trend.length === 0 ? (
              <p className="py-10 text-center text-sm text-muted">Finalize um caderno de questões para começar a ver sua evolução.</p>
            ) : (
              <>
                <div className="relative flex h-40 items-end gap-1.5" role="img" aria-label="Taxa de acerto por caderno finalizado">
                  <div className="absolute inset-x-0 border-t border-dashed border-muted/60" style={{ bottom: "70%" }} aria-hidden />
                  <span className="absolute -top-1 right-0 rounded bg-surface px-1 text-[10px] font-semibold text-muted" style={{ bottom: "70%" }}>70%</span>
                  {perf.trend.map((t, i) => (
                    <div key={t.id} className="group flex h-full flex-1 flex-col justify-end" title={`${subjectShort(t.subjectId ?? "")} · ${Math.round(t.ratio * 100)}%`}>
                      <div className="bar-grow w-full rounded-t-md" style={{ height: `${Math.max(4, t.ratio * 100)}%`, background: accColor(t.ratio), "--delay": `${i * 40}ms` } as CSSProperties} />
                    </div>
                  ))}
                </div>
                <div className="mt-2 flex justify-between text-xs font-semibold text-muted tabular">
                  <span>{perf.trend[0].at.toLocaleDateString("pt-BR", { day: "2-digit", month: "2-digit" })}</span>
                  <span>{perf.trend.at(-1)!.at.toLocaleDateString("pt-BR", { day: "2-digit", month: "2-digit" })}</span>
                </div>
              </>
            )}
          </Card>
        </section>

        <section aria-labelledby="heat">
          <SectionTitle id="heat" info="Cada quadrado é um dia; quanto mais escuro, mais tempo lançado. Constância vale mais do que maratonas isoladas." aside={`${activeDays} ${activeDays === 1 ? "dia" : "dias"} com estudo`}>Constância</SectionTitle>
          <Card className="rise" style={{ "--i": 3 } as CSSProperties}>
            <Heatmap days={perf.daily} />
          </Card>
        </section>
      </div>

      {plan && perf.byWeekSeconds.length > 0 && (
        <section aria-labelledby="wk">
          <SectionTitle id="wk" info="Horas lançadas em cada semana do plano. A linha tracejada é a meta daquela semana." aside="tracejado = meta">Horas por semana</SectionTitle>
          <Card className="rise" style={{ "--i": 3 } as CSSProperties}>
            <div className="flex h-40 items-end gap-[3px]" role="img" aria-label="Horas estudadas por semana em relação à meta">
              {perf.byWeekSeconds.map((sec, i) => (
                <div key={i} className="group relative flex h-full flex-1 flex-col justify-end" title={`Semana ${i + 1}: ${fmtDuration(sec)} (meta ${fmtDuration(weekTarget(i))})`}>
                  <div className="absolute inset-x-0 border-t border-dashed border-muted/60" style={{ bottom: `${(weekTarget(i) / maxBar) * 100}%` }} />
                  <div
                    className="bar-grow w-full rounded-t-md transition-[filter] group-hover:brightness-110"
                    style={{ height: `${(sec / maxBar) * 100}%`, minHeight: sec > 0 ? 3 : 0, background: i + 1 === nowWeek ? "var(--gold)" : "var(--primary)", opacity: i + 1 === nowWeek ? 1 : 0.7, "--delay": `${i * 35}ms` } as CSSProperties}
                  />
                </div>
              ))}
            </div>
            <div className="mt-2 flex justify-between text-xs font-semibold text-muted tabular"><span>Semana 1</span><span className="text-gold-text">● semana atual</span><span>Semana {totalWeeks}</span></div>
          </Card>
        </section>
      )}

      <div className="grid gap-6 lg:grid-cols-2">
        <section aria-labelledby="weak">
          <SectionTitle id="weak" info="Assuntos com menos de 70% de acerto em pelo menos 3 questões respondidas. São os melhores candidatos a revisão extra.">Assuntos para reforçar</SectionTitle>
          {perf.weak.length === 0 ? (
            <Alert tone="info">Ainda não há dados suficientes. Faça alguns cadernos de questões para identificar seus pontos fracos.</Alert>
          ) : (
            <Card className="divide-y divide-border p-0">
              {perf.weak.map((w) => (
                <div key={`${w.subjectId}-${w.topic}`} className="flex items-center justify-between gap-3 px-5 py-3 text-sm">
                  <div className="min-w-0"><p className="truncate font-semibold">{w.topic}</p><p className="text-xs text-muted">{subjectShort(w.subjectId)} · {w.attempts} questões</p></div>
                  <Badge tone="warn" className="tabular">{pct(w.accuracy)}</Badge>
                </div>
              ))}
            </Card>
          )}
        </section>

        <section aria-labelledby="rec">
          <SectionTitle id="rec">Últimos cadernos</SectionTitle>
          {perf.recentSessions.length === 0 ? (
            <Alert tone="info">Nenhum caderno finalizado ainda.</Alert>
          ) : (
            <Card className="divide-y divide-border p-0">
              {perf.recentSessions.map((s) => {
                const r = (s.score ?? 0) / s.total;
                return (
                  <Link key={s.id} href={`/caderno/${s.activityId}`} className="group flex items-center gap-4 px-5 py-3 text-sm transition first:rounded-t-2xl last:rounded-b-2xl hover:bg-surface-2">
                    <Ring value={r} size={42} stroke={5} color={accColor(r)} label={`${Math.round(r * 100)}% de acerto`}>
                      <span className="text-[10px] font-bold tabular">{Math.round(r * 100)}</span>
                    </Ring>
                    <div className="min-w-0 flex-1">
                      <p className="truncate font-semibold">{s.activity ? subjectShort(s.activity.subjectId) : "Caderno"}{s.activity ? ` · Aula ${String(s.activity.aula.number).padStart(2, "0")}` : ""}</p>
                      <p className="text-xs text-muted">{s.finishedAt?.toLocaleDateString("pt-BR")}</p>
                    </div>
                    <span className="font-display text-xl font-bold tabular">{s.score ?? 0}<span className="text-muted">/{s.total}</span></span>
                    <ChevronRight className="h-4 w-4 text-muted transition group-hover:translate-x-0.5" aria-hidden />
                  </Link>
                );
              })}
            </Card>
          )}
        </section>
      </div>

      {perf.bizuAnswered > 0 && <p className="text-sm text-muted">Itens Certo/Errado dos Bizus: <strong className="text-text">{perf.bizuCorrect}</strong> acertos em {perf.bizuAnswered} respondidos.</p>}
    </div>
  );
}
