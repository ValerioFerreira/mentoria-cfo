import { segmentAnchors } from "@/lib/directive-anchors";
import { ArrowLeft, Clock3, Lightbulb, NotebookPen, Sparkles } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { CSSProperties, ReactNode } from "react";
import { BizuItems, BizuSummary } from "@/components/bizu";
import { ReadingTabs } from "@/components/reading-tabs";
import { ActivityActions, ManualTime, NotesEditor } from "@/components/study-controls";
import { Alert, Badge, Card, InfoTip, LinkButton, TYPE_META, TypeIcon } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getActivity } from "@/lib/data/study";
import { db } from "@/lib/db";
import {
  aulaLabel, fixacaoMentoria, fixacaoSteps, materialHref, questoesSteps, revisaoFinalSteps, revisaoMentoria, revisaoSteps,
  teoriaDirective, teoriaMentoria, turboDirective, turboMentoriaStep,
  withAnchor, type AulaRef, type FixRange, type MaterialChapter, type SegmentRef,
} from "@/lib/directive";
import { chapterFor, chaptersForAula, getMaterialChoice, volumeInfo } from "@/lib/material";

/** Dados do botão "Reportar erro no PDF" (volume, rótulo e total de páginas). */
function reportFor(volumeId: string, label: string) {
  const info = volumeInfo(volumeId);
  return info ? { volumeId, volumeLabel: label, maxPage: info.paginas } : undefined;
}
import { loadQuizPool, poolSize } from "@/lib/quiz/pool";
import { STATUS_LABEL, subjectShort } from "@/lib/ui-format";
import { MaterialLink } from "@/components/material-link";
import { MaterialTabs, MentoriaPdfLink } from "@/components/material-tabs";
import { packageFor } from "@/lib/contests";

export const metadata: Metadata = { title: "Atividade" };

/** Passos da diretriz: é uma sequência de verdade (a ordem importa), então vai numerada. */
function Steps({ items, color }: { items: string[]; color: string }) {
  return (
    <ol className="space-y-3">
      {items.map((s, i) => (
        <li key={s} className="flex gap-3.5 text-[15px] leading-relaxed">
          <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full font-display text-sm font-bold text-white" style={{ background: color }} aria-hidden>{i + 1}</span>
          <span className="min-w-0">{s}</span>
        </li>
      ))}
    </ol>
  );
}

function Section({ id, icon, title, info }: { id?: string; icon?: ReactNode; title: string; info?: ReactNode }) {
  return (
    <h2 id={id} className="mb-3 flex items-center gap-2 font-display text-2xl font-bold uppercase tracking-wide">
      {icon}
      {title}
      {info && <InfoTip align="start">{info}</InfoTip>}
    </h2>
  );
}

export default async function ActivityPage({ params }: PageProps<"/atividade/[id]">) {
  const user = await requireUser();
  const { id } = await params;
  const a = await getActivity(user.id, id);
  if (!a) notFound();

  const segs = a.segments.map((x) => x.segment).sort((p, q) => p.aulaId.localeCompare(q.aulaId) || p.sortOrder - q.sortOrder);
  const segIds = segs.map((s) => s.id);
  const anchors = segmentAnchors();
  const segRefs = segs.map<SegmentRef & { aulaId: string }>((s) => withAnchor({
    id: s.id, aulaId: s.aulaId, startPage: s.startPage, endPage: s.endPage, startPrinted: s.startPrinted, endPrinted: s.endPrinted,
    startTopic: s.startTopic, startsMidTopic: s.startsMidTopic, stopBeforeTopic: s.stopBeforeTopic, endsMidTopic: s.endsMidTopic,
    endTopic: s.endTopic, endsTheory: s.endsTheory,
  }, anchors[s.id]));

  // aulas envolvidas (atividades finais podem misturar várias aulas) e aulas de prática citadas na Fixação.
  // As páginas da Fixação vêm do catálogo atual (como no planejador, blueprint.ts): o que o plano gravou pode ter ficado
  // velho depois de uma resegmentação da aula.
  const storedFix = (a.fixRanges as FixRange[] | null) ?? [];
  const fixAula = a.type === "FIXACAO"
    ? await db.aula.findUnique({ where: { id: a.aulaId }, select: { commentedRuns: true, practiceLinks: true } })
    : null;
  const currentFix: FixRange[] = fixAula
    ? [
        ...((fixAula.commentedRuns as [number, number][] | null) ?? []).map(([start, end]) => ({ start, end })),
        ...((fixAula.practiceLinks as { startPage: number; endPage: number; sourceAula: string }[] | null) ?? [])
          .map((l) => ({ start: l.startPage, end: l.endPage, sourceAula: l.sourceAula })),
      ]
    : [];
  const fixRanges = currentFix.length ? currentFix : storedFix;
  const aulaIds = [...new Set([a.aulaId, ...segs.map((s) => s.aulaId), ...fixRanges.map((r) => r.sourceAula).filter(Boolean) as string[]])];
  const [aulas, notes, approvedQuestions, analytics] = await Promise.all([
    db.aula.findMany({ where: { id: { in: aulaIds } }, select: { id: true, number: true, shortTitle: true, printedOffset: true, source: true, materialPath: true, subject: { select: { name: true } } } }),
    db.note.findMany({ where: { userId: user.id, segmentId: { in: segIds } } }),
    a.type === "QUESTOES" ? loadQuizPool(a, a.week.plan.contest).then(poolSize) : Promise.resolve(0),
    a.type === "TEORIA" || a.type === "REVISAO" ? db.analyticSummary.findMany({ where: { segmentId: { in: segIds } }, select: { segmentId: true, markdown: true, status: true, readMinutes: true } }) : Promise.resolve([]),
  ]);
  const analyticBySeg = new Map(analytics.map((x) => [x.segmentId, x]));
  const hasAnalytic = segs.length > 0 && segs.every((s) => analyticBySeg.has(s.id));
  const readMinutes = analytics.reduce((n, x) => n + x.readMinutes, 0);
  const aulaById = new Map(aulas.map((x) => [x.id, x]));
  const toRef = (x: (typeof aulas)[number]): AulaRef => ({ id: x.id, number: x.number, shortTitle: x.shortTitle, subjectName: x.subject.name, printedOffset: x.printedOffset, authored: x.source === "AUTHORED", materialPath: x.materialPath });
  const mainAula = toRef(aulaById.get(a.aulaId)!);
  const noteBySeg = new Map(notes.map((n) => [n.segmentId, n.text]));

  // material próprio MentorIA: o mesmo assunto, nas páginas do capítulo de cada trecho (só quando todos os trechos têm capítulo)
  const materialChoice = await getMaterialChoice();
  const chapters = segs.map((s) => chapterFor(s.id)).filter((c): c is MaterialChapter => Boolean(c));
  const allChapters = segs.length > 0 && chapters.length === segs.length;
  const fixChapters = a.type === "FIXACAO" ? chaptersForAula(a.aulaId) : [];
  const withMaterial = (mentoria: ReactNode, base: ReactNode) => <MaterialTabs initial={materialChoice} mentoria={mentoria} base={base} />;

  const isFinal = a.scope === "FINAL";
  const title = isFinal
    ? a.type === "QUESTOES" ? `Caderno misto — ${subjectShort(a.subjectId)}` : `Revisão geral — ${subjectShort(a.subjectId)}`
    : mainAula.shortTitle;

  // blocos de teoria agrupados por aula
  const byAula = new Map<string, (SegmentRef & { aulaId: string })[]>();
  for (const s of segRefs) byAula.set(s.aulaId, [...(byAula.get(s.aulaId) ?? []), s]);

  /** Resumo analítico dos trechos da atividade, na ordem do curso (concatenados quando a atividade cobre mais de um). */
  const analyticBlocks = (
    <div className="space-y-5">
      {segs.map((s) => {
        const an = analyticBySeg.get(s.id);
        if (!an) return null;
        return (
          <article key={s.id} className="space-y-2">
            <div className="flex flex-wrap items-center gap-2">
              {(segs.length > 1 || s.startTopic) && <p className="eyebrow">{s.startTopic ?? "Assunto"}</p>}
              <span className="text-xs text-muted">≈ {an.readMinutes} min de leitura</span>
              {an.status === "DRAFT" && <Badge tone="neutral">rascunho</Badge>}
            </div>
            <BizuSummary markdown={an.markdown} />
          </article>
        );
      })}
    </div>
  );

  const bizus = segs.filter((s) => s.bizu).map((s) => s.bizu!);
  const bizuSet = a.type === "REVISAO" ? "REVISAO" : "TEORIA";
  const bizuItems = bizus.flatMap((b) => b.items.filter((i) => i.set === bizuSet));
  const limitMin = Math.round((a.quizLimitSec ?? 3600) / 60);
  const meta = TYPE_META[a.type];
  const materialPackage = packageFor(a.week.plan.contest, a.subjectId);
  // Revisão e Caderno de uma aula pressupõem a Teoria feita: avisa (sem bloquear) se alguma ainda está pendente
  const pendingTheory = !isFinal && (a.type === "REVISAO" || a.type === "QUESTOES") ? a.refs.filter((r) => r.refActivity.status !== "DONE") : [];

  const bizuSection = (a.type === "TEORIA" || a.type === "REVISAO") ? (
  <section className="rise" style={{ "--i": 4 } as CSSProperties} aria-labelledby="bizu">
            <Section id="bizu" icon={<Sparkles className="h-5 w-5 text-gold" aria-hidden />} title="Bizu" />
            {bizus.length === 0 ? (
              <Alert tone="info">O Bizu (resumo + itens de Certo/Errado) deste trecho ainda está em produção.</Alert>
            ) : (
              <div className="space-y-4">
                {bizus.map((b) => <BizuSummary key={b.id} markdown={b.summary} />)}
                <BizuItems activityId={a.id} items={bizuItems.map((i) => ({ id: i.id, statement: i.statement, isTrue: i.isTrue, explanation: i.explanation }))} />
              </div>
            )}
          </section>
  ) : null;

  return (
    <div className="mx-auto max-w-3xl space-y-7">
      <nav aria-label="Navegação">
        <Link href={`/semana/${a.week.index}`} className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Meta semanal · semana {a.week.index}
        </Link>
      </nav>

      <header className="rise relative overflow-hidden rounded-3xl border border-border bg-surface p-6 shadow-card sm:p-8">
        <span className="absolute inset-0" style={{ background: `radial-gradient(34rem 14rem at 0% 0%, color-mix(in srgb, ${meta.color} 18%, transparent), transparent 70%)` }} aria-hidden />
        <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: meta.color }} aria-hidden />
        <div className="relative space-y-4">
          <div className="flex flex-wrap items-center gap-2">
            <TypeIcon type={a.type} box />
            <div>
              <p className="eyebrow" style={{ color: meta.color }}>{meta.label}</p>
              <p className="text-sm font-semibold">{subjectShort(a.subjectId)}</p>
            </div>
            <span className="ml-auto flex flex-wrap items-center gap-2">
              {a.turbo && <Badge tone="gold">Modo Turbo</Badge>}
              <Badge tone={a.status === "DONE" ? "ok" : "neutral"}>{STATUS_LABEL[a.status]}</Badge>
              <span className="inline-flex items-center gap-1 text-xs font-semibold text-muted"><Clock3 className="h-3.5 w-3.5" aria-hidden />~{a.plannedMinutes} min</span>
            </span>
          </div>
          <h1 className="font-display text-4xl font-bold uppercase leading-[0.95] sm:text-5xl">{title}</h1>
          {a.editalTopic && (
            <p className="text-sm font-medium text-muted">
              <span className="font-semibold text-text">Assunto do edital:</span> {a.editalTopic}
            </p>
          )}
          <ActivityActions id={a.id} status={a.status} activity={{ subject: subjectShort(a.subjectId), type: meta.label, title }} summaryCheck={a.type === "TEORIA" && segs.length > 0 ? { segmentIds: segIds, filled: segs.filter((s) => (noteBySeg.get(s.id) ?? "").trim()).map((s) => s.id) } : undefined} />
        </div>
      </header>

      {materialPackage && (
        <Card className="space-y-2">
          <h2 className="font-display text-xl font-bold uppercase tracking-wide">Material</h2>
          <p className="text-sm leading-relaxed text-muted">
            As aulas mencionadas na diretriz a seguir são baseadas no pacote{" "}
            <a href={materialPackage.url} target="_blank" rel="noopener noreferrer" className="font-semibold text-primary underline decoration-primary/40 underline-offset-2 hover:decoration-primary">
              {materialPackage.name}
            </a>.
          </p>
        </Card>
      )}

      {pendingTheory.length > 0 && (
        <Alert>
          {a.type === "QUESTOES"
            ? "Este caderno cobre assuntos cuja Teoria você ainda não concluiu. Estude antes para o caderno medir o que você aprendeu:"
            : "Esta Revisão pressupõe a Teoria feita. Conclua antes:"}{" "}
          {pendingTheory.map((r, i) => (
            <span key={r.refActivityId}>
              {i > 0 && ", "}
              <Link href={`/atividade/${r.refActivityId}`} className="font-semibold underline">Teoria · {aulaLabel(r.refActivity.aula)}</Link>
            </span>
          ))}
          .
        </Alert>
      )}

      <section aria-labelledby="dir" className="rise" style={{ "--i": 1 } as CSSProperties}>
        <Section id="dir" icon={<Lightbulb className="h-5 w-5 text-gold" aria-hidden />} title="Diretriz" />
        <Card className="space-y-5">
          {a.type === "TEORIA" && (() => {
            const baseView = (
              <div className="space-y-5">
                {[...byAula].map(([aulaId, list]) => {
                  const d = teoriaDirective(toRef(aulaById.get(aulaId)!), list);
                  return (
                    <div key={aulaId} className="space-y-3">
                      <p className="eyebrow">{d.heading}{d.pages > 0 ? ` · ${d.pages} págs.` : ""}</p>
                      {toRef(aulaById.get(aulaId)!).authored && <MaterialLink path={toRef(aulaById.get(aulaId)!).materialPath} page={list[0].startPage} />}
                      <Steps items={d.steps} color={meta.color} />
                    </div>
                  );
                })}
              </div>
            );
            const mentoriaView = (
              <div className="space-y-5">
                {teoriaMentoria(chapters).map((d) => (
                  <div key={d.volumeId} className="space-y-3">
                    <p className="eyebrow">{d.heading} · {d.pages} págs.</p>
                    <MentoriaPdfLink href={materialHref(d, d.firstPage)} page={d.firstPage} report={reportFor(d.volumeId, d.heading)} />
                    <Steps items={d.steps} color={meta.color} />
                  </div>
                ))}
              </div>
            );
            const pagesView = allChapters ? withMaterial(mentoriaView, baseView) : baseView;
            if (!hasAnalytic) return pagesView; // sem resumo analítico, só a diretriz (nunca no Turbo: ele só troca quem tem resumo)
            const first = [...byAula].map(([aulaId, list]) => turboDirective(toRef(aulaById.get(aulaId)!), list, readMinutes))[0];
            const mentoriaLookup = allChapters ? turboMentoriaStep(chapters) : null;
            const turboSteps = mentoriaLookup && materialChoice === "mentoria"
              ? [...first.steps.filter((s) => !s.startsWith("Se um ponto ficar confuso")), mentoriaLookup]
              : first.steps;
            const summaryView = (
              <div className="space-y-5">
                {a.turbo && <Steps items={turboSteps} color={meta.color} />}
                {!a.turbo && <p className="text-sm text-muted">Prefere ler um resumo em vez do material? Leia o resumo analítico abaixo (≈ {readMinutes} min). O Bizu continua valendo, no fim da página.</p>}
                {analyticBlocks}
              </div>
            );
            return (
              <ReadingTabs
                initial={a.turbo ? "resumo" : "paginas"}
                tabs={[
                  { id: "paginas", label: a.turbo ? "Ver as páginas (opcional)" : "Seguir a diretriz (págs.)", content: pagesView },
                  { id: "resumo", label: "Ler o resumo analítico", content: summaryView },
                ]}
              />
            );
          })()}

          {a.type === "REVISAO" && (
            <>
              <Steps items={isFinal ? revisaoFinalSteps() : revisaoSteps()} color={meta.color} />
              {(() => {
                const baseList = (
                  <div className="rounded-xl bg-surface-2 p-4">
                    <p className="eyebrow mb-2">Trechos a revisar</p>
                    <ul className="space-y-1.5 text-sm">
                      {isFinal
                        ? [...byAula].map(([aulaId, list]) => {
                            const au = aulaById.get(aulaId)!;
                            return <li key={aulaId}>{aulaLabel(toRef(au))} <span className="text-muted">· págs. {list.map((s) => `${s.startPage}–${s.endPage}`).join(", ")}</span></li>;
                          })
                        : a.refs.map((r) => (
                            <li key={r.refActivityId}>
                              <Link href={`/atividade/${r.refActivityId}`} className="font-semibold text-teoria hover:underline">
                                Teoria · {aulaLabel(r.refActivity.aula)}
                              </Link>
                            </li>
                          ))}
                    </ul>
                  </div>
                );
                if (!allChapters) return baseList;
                const mentoriaList = (
                  <div className="space-y-3 rounded-xl bg-surface-2 p-4">
                    <p className="eyebrow">Mapas do material MentorIA</p>
                    <ul className="list-disc space-y-1.5 pl-5 text-sm">{revisaoMentoria(chapters).map((s) => <li key={s}>{s}</li>)}</ul>
                    <MentoriaPdfLink href={materialHref(chapters[0], chapters[0].mapPage)} page={chapters[0].mapPage} report={reportFor(chapters[0].volumeId, chapters[0].volumeTitle)} />
                  </div>
                );
                return withMaterial(mentoriaList, baseList);
              })()}
            </>
          )}

          {a.type === "FIXACAO" && (() => {
            const baseSteps = (
              <Steps
                color={meta.color}
                items={fixacaoSteps(mainAula, fixRanges, (aid) => {
                  const x = aulaById.get(aid);
                  return x ? `Aula ${String(x.number).padStart(2, "0")} (${x.shortTitle})` : aid;
                })}
              />
            );
            const steps = fixacaoMentoria(fixChapters);
            if (!steps.length) return baseSteps;
            const firstQ = fixChapters.find((c) => c.questions);
            return withMaterial(
              <div className="space-y-3">
                <MentoriaPdfLink href={materialHref(firstQ!, firstQ!.questions!.pagina)} page={firstQ!.questions!.pagina} report={reportFor(firstQ!.volumeId, firstQ!.volumeTitle)} />
                <Steps color={meta.color} items={steps} />
              </div>,
              baseSteps,
            );
          })()}

          {a.type === "QUESTOES" && (
            <>
              <Steps items={questoesSteps(a.quizMixed, a.quizQuestions ?? 25, limitMin)} color={meta.color} />
              {approvedQuestions >= 5 ? (
                <LinkButton href={`/caderno/${a.id}`} size="lg">{a.status === "DONE" ? "Ver resultado / novo caderno" : "Abrir caderno"}</LinkButton>
              ) : (
                <Alert tone="info">O banco de questões deste trecho ainda está em produção ({approvedQuestions} disponíveis). Quando houver questões suficientes, o caderno é liberado automaticamente.</Alert>
              )}
            </>
          )}
        </Card>
      </section>

      {a.turbo && bizuSection}

      {a.type === "TEORIA" && segs.length > 0 && (
        <section className="rise" style={{ "--i": 3 } as CSSProperties}>
          <Section id="resumo" icon={<NotebookPen className="h-5 w-5 text-muted" aria-hidden />} title="Meu resumo" info="Escreva com as suas palavras. Este texto aparece na Revisão e em Meus resumos." />
          <Card className="space-y-4">
            <p className="text-sm text-muted">Escreva o seu resumo antes de concluir: é o que você vai reler na Revisão. Sem ele, a Revisão fica sem material seu.</p>
            {segs.map((s, i) => (
              <NotesEditor key={s.id} segmentId={s.id} label={segs.length > 1 ? `Parte ${i + 1}${s.startTopic ? ` · ${s.startTopic}` : ""}` : "Resumo do assunto"} initial={noteBySeg.get(s.id) ?? ""} />
            ))}
          </Card>
        </section>
      )}

      {a.type === "REVISAO" && (() => {
        const mine = (
          <div className="space-y-3">
            {segs.map((s) => (
              <div key={s.id} className="rounded-xl bg-surface-2 p-4 text-sm">
                {s.startTopic && <p className="eyebrow mb-1.5">{s.startTopic}</p>}
                <p className="whitespace-pre-wrap leading-relaxed">{noteBySeg.get(s.id) || <span className="text-muted">Você ainda não escreveu um resumo para este assunto.</span>}</p>
              </div>
            ))}
          </div>
        );
        const tabs = [
          { id: "meus", label: segs.length > 1 ? "Meus resumos" : "Meu resumo", content: mine },
          ...(analytics.length > 0 ? [{ id: "analitico", label: "Resumo analítico", content: analyticBlocks }] : []),
        ];
        const anyNote = segs.some((s) => (noteBySeg.get(s.id) ?? "").trim());
        return (
          <section className="rise" style={{ "--i": 3 } as CSSProperties} aria-labelledby="rev-resumos">
            <Section id="rev-resumos" icon={<NotebookPen className="h-5 w-5 text-muted" aria-hidden />} title="Resumos para revisar" info="Releia o que você mesmo escreveu (os resumos de cada atividade de Teoria, em sequência) ou, se preferir, o resumo analítico do assunto." />
            <Card className="space-y-3">
              <ReadingTabs initial={anyNote || analytics.length === 0 ? "meus" : "analitico"} tabs={tabs} />
            </Card>
          </section>
        );
      })()}

      {!a.turbo && bizuSection}

      <ManualTime id={a.id} logs={a.timeLogs.map((l) => ({ id: l.id, seconds: l.seconds, source: l.source, startedAt: l.startedAt.toISOString() }))} />
    </div>
  );
}
