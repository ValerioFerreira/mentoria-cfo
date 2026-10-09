import { ArrowLeft, CircleCheck, CircleHelp, CircleX } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { CSSProperties } from "react";
import { QuizRunner } from "@/components/quiz-runner";
import { QuizStart } from "@/components/quiz-start";
import { ReportButton } from "@/components/report-button";
import { Alert, Badge, Card, Count, InfoTip, Kbd, LinkButton, PageHeader, Ring, SectionTitle } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { attentionPoints, score, type AnswerRow } from "@/lib/quiz/logic";
import { servableStatuses } from "@/lib/quiz/servable";
import { fmtDuration, subjectShort } from "@/lib/ui-format";

export const metadata: Metadata = { title: "Caderno de questões" };

const serverNow = () => Date.now();

function BackLink({ href, label }: { href: string; label: string }) {
  return (
    <Link href={href} className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
      <ArrowLeft className="h-4 w-4" aria-hidden />
      {label}
    </Link>
  );
}

export default async function QuizPage({ params }: PageProps<"/caderno/[id]">) {
  const user = await requireUser();
  const { id } = await params; // id da atividade
  const activity = await db.activity.findFirst({
    where: { id, type: "QUESTOES", week: { plan: { userId: user.id } } },
    include: { aula: { select: { number: true, shortTitle: true } }, segments: { select: { segmentId: true } }, week: { select: { index: true } } },
  });
  if (!activity) notFound();

  const session = await db.quizSession.findFirst({
    where: { userId: user.id, activityId: id },
    orderBy: { startedAt: "desc" },
    include: { answers: { orderBy: { position: "asc" }, include: { question: { include: { options: { orderBy: { label: "asc" } } } } } } },
  });

  const title = activity.scope === "FINAL" ? `Caderno misto — ${subjectShort(activity.subjectId)}` : `Aula ${String(activity.aula.number).padStart(2, "0")} — ${activity.aula.shortTitle}`;

  // ───────── execução ─────────
  if (session && !session.finishedAt) {
    return (
      <div className="space-y-3">
        <BackLink href={`/atividade/${id}`} label={title} />
        <QuizRunner
          sessionId={session.id}
          startedAtMs={session.startedAt.getTime()}
          limitSeconds={session.limitSeconds}
          serverNowMs={serverNow()}
          questions={session.answers.map((a) => ({
            position: a.position,
            topic: a.question.topic,
            support: a.question.support,
            statement: a.question.statement,
            options: a.question.options.map((o) => ({ label: o.label, text: o.text })), // sem isCorrect
            chosen: a.chosenLabel,
            flagged: a.flagged,
          }))}
        />
      </div>
    );
  }

  // ───────── resultado ─────────
  if (session && session.finishedAt) {
    const rows: AnswerRow[] = session.answers.map((a) => ({
      questionId: a.questionId, topic: a.question.topic, segmentId: a.question.segmentId, pageRef: a.question.pageRef,
      chosen: a.chosenLabel, correctLabel: a.question.options.find((o) => o.isCorrect)?.label ?? "", seconds: a.secondsSpent,
    }));
    const sc = score(rows);
    const points = attentionPoints(rows);
    const used = Math.min(session.limitSeconds, Math.round((session.finishedAt.getTime() - session.startedAt.getTime()) / 1000));
    const segInfo = new Map((await db.segment.findMany({ where: { id: { in: [...new Set(rows.map((r) => r.segmentId))] } }, select: { id: true, aula: { select: { number: true, shortTitle: true } } } })).map((s) => [s.id, s.aula]));

    return (
      <div className="mx-auto max-w-3xl space-y-6">
        <BackLink href={`/atividade/${id}`} label={title} />
        <PageHeader
          eyebrow={session.autoSubmitted ? "Encerrado ao fim do tempo" : "Finalizado por você"}
          title="Resultado do caderno"
          description={`Tempo usado: ${fmtDuration(used)}.`}
        />

        <Card tone="ink" className="rise flex flex-wrap items-center gap-7 p-6 sm:p-8">
          <Ring value={sc.percent / 100} size={150} stroke={14} color={sc.percent >= 70 ? "var(--ok)" : sc.percent >= 50 ? "var(--gold)" : "var(--primary)"} track="rgb(255 255 255 / 0.12)" label={`${sc.percent}% de acerto`}>
            <span className="font-display text-6xl font-bold leading-none"><Count value={sc.percent} suffix="%" /></span>
            <span className="mt-1 text-[11px] font-semibold uppercase tracking-widest text-on-ink-muted">de acerto</span>
          </Ring>
          <div className="grid flex-1 grid-cols-3 gap-4 min-w-[16rem]">
            {[
              [CircleCheck, "Acertos", sc.correct, "text-ok"],
              [CircleX, "Erros", sc.wrong, "text-primary"],
              [CircleHelp, "Em branco", sc.blank, "text-on-ink-muted"],
            ].map(([I, label, n, cls]) => {
              const Icon = I as typeof CircleCheck;
              return (
                <div key={String(label)}>
                  <Icon className={`h-5 w-5 ${cls}`} aria-hidden />
                  <p className="mt-1 font-display text-5xl font-bold leading-none tabular">{String(n)}</p>
                  <p className="eyebrow !text-on-ink-muted">{String(label)}</p>
                </div>
              );
            })}
          </div>
          <p className="w-full text-sm text-on-ink-muted">{sc.correct} de {sc.total} questões. {sc.percent >= 70 ? "Ótimo desempenho: siga para a próxima atividade." : sc.percent >= 50 ? "Bom caminho. Reveja os pontos de atenção abaixo." : "Vale uma revisão dirigida dos pontos de atenção antes de avançar."}</p>
        </Card>

        <section aria-labelledby="att" className="space-y-3">
          <SectionTitle id="att">Pontos de atenção</SectionTitle>
          {points.length === 0 ? (
            <Alert tone="info">Nenhum assunto ficou abaixo de 60% de acerto neste caderno. Siga para a próxima atividade.</Alert>
          ) : (
            <Card className="divide-y divide-border p-0">
              {points.map((p) => {
                const aula = segInfo.get(p.segmentId);
                return (
                  <div key={`${p.segmentId}-${p.topic}`} className="flex flex-wrap items-center justify-between gap-2 px-5 py-3">
                    <div>
                      <p className="font-semibold">{p.topic}</p>
                      <p className="text-xs text-muted">
                        {aula ? aula.shortTitle : ""}
                      </p>
                    </div>
                    <div className="flex items-center gap-2 text-sm">
                      <Badge tone="warn">{p.reason}</Badge>
                      <span className="tabular text-muted">{p.correct}/{p.attempts} · {p.avgSeconds}s por questão</span>
                    </div>
                  </div>
                );
              })}
            </Card>
          )}
        </section>

        <section aria-labelledby="rev" className="space-y-3">
          <SectionTitle id="rev" aside={`${session.answers.length} questões`}>Revisão das questões</SectionTitle>
          {session.answers.map((a, i) => {
            const correct = a.question.options.find((o) => o.isCorrect)?.label;
            const ok = a.chosenLabel === correct;
            const blank = a.chosenLabel === null;
            const edge = blank ? "var(--border-strong)" : ok ? "var(--ok)" : "var(--primary)";
            return (
              <Card key={a.id} className="rise relative space-y-3 overflow-hidden pl-7" style={{ "--i": Math.min(i, 8) } as CSSProperties}>
                <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: edge }} aria-hidden />
                <div className="flex items-center justify-between">
                  <span className="font-display text-xl font-bold uppercase tracking-wide">Questão {a.position}</span>
                  <Badge tone={blank ? "neutral" : ok ? "ok" : "warn"}>{blank ? "Em branco" : ok ? "Acertou" : "Errou"}</Badge>
                </div>
                {a.question.support && <div className="whitespace-pre-line rounded-xl border-l-4 border-border-strong bg-surface-2 p-3.5 text-sm leading-relaxed">{a.question.support}</div>}
                <p className="whitespace-pre-line text-[15px] leading-relaxed">{a.question.statement}</p>
                <ul className="space-y-1.5 text-sm">
                  {a.question.options.map((o) => (
                    <li key={o.label} className={`flex gap-2.5 rounded-lg px-3 py-2 ${o.isCorrect ? "bg-ok/12 text-ok" : o.label === a.chosenLabel ? "bg-danger-soft text-primary" : "text-muted"}`}>
                      <strong className="font-display text-base">{o.label}</strong><span>{o.text}</span>
                      {o.isCorrect && <CircleCheck className="ml-auto h-4 w-4 shrink-0" aria-label="alternativa correta" />}
                    </li>
                  ))}
                </ul>
                <p className="rounded-xl bg-surface-2 p-3.5 text-sm leading-relaxed text-muted"><strong className="text-text">Comentário: </strong>{a.question.explanation}</p>
                <ReportButton questionId={a.questionId} />
              </Card>
            );
          })}
        </section>

        <div className="flex flex-wrap gap-2 border-t border-border pt-4">
          <LinkButton href={`/atividade/${id}`} variant="secondary">Voltar à atividade</LinkButton>
          <LinkButton href={`/semana/${activity.week.index}`} variant="secondary">Voltar à semana</LinkButton>
          <QuizStart activityId={id} label="Fazer outro caderno" />
        </div>
      </div>
    );
  }

  // ───────── introdução ─────────
  const available = await db.question.count({ where: { segmentId: { in: activity.segments.map((s) => s.segmentId) }, status: { in: servableStatuses() } } });
  const n = Math.min(activity.quizQuestions ?? 25, available);
  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <BackLink href={`/atividade/${id}`} label={title} />
      <PageHeader eyebrow={title} title="Caderno de questões" />
      <Card className="rise space-y-4">
        <dl className="grid grid-cols-3 divide-x divide-border text-center">
          {[
            ["Questões", String(n)],
            ["Tempo limite", ],
            ["Alternativas", "5"],
          ].map(([label, value]) => (
            <div key={label} className="px-2">
              <dt className="eyebrow">{label}</dt>
              <dd className="font-display text-4xl font-bold leading-tight tabular">{value}</dd>
            </div>
          ))}
        </dl>
        <p className="flex flex-wrap items-center justify-center gap-x-3 gap-y-1.5 text-xs text-muted">
          <span className="inline-flex items-center gap-1.5">
            Regras do caderno
            <InfoTip align="center">Padrão da banca AOCP: uma alternativa correta entre cinco. Ao zerar o tempo, o caderno é encerrado e corrigido automaticamente. Questão em branco conta como erro e não há desconto por erro, como na prova. O resultado fica salvo e aponta os assuntos em que você mais precisa melhorar.</InfoTip>
          </span>
          <span className="inline-flex items-center gap-1.5"><Kbd>A</Kbd>–<Kbd>E</Kbd> responder <Kbd>←</Kbd><Kbd>→</Kbd> navegar</span>
        </p>
      </Card>
      {available >= 5 ? <QuizStart activityId={id} /> : <Alert tone="info">O banco de questões deste trecho ainda está em produção.</Alert>}
    </div>
  );
}
