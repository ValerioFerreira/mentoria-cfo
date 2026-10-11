import { ArrowLeft, CheckCircle2, CircleCheck, CircleHelp, CircleX, RefreshCw } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { QuizRunner } from "@/components/quiz-runner";
import { Alert, Badge, Card, Count, LinkButton, PageHeader, Ring } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { score, type AnswerRow } from "@/lib/quiz/logic";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { fmtDuration, subjectName } from "@/lib/ui-format";

export const metadata: Metadata = { title: "Prática de Questões — Missão CBMPE" };

const serverNow = () => Date.now();

export default async function PracticeQuizPage({ params }: { params: Promise<{ id: string }> }) {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role))) {
    redirect("/questoes");
  }

  const { id } = await params;

  const session = await db.quizSession.findFirst({
    where: { id, userId: user.id },
    include: {
      answers: {
        orderBy: { position: "asc" },
        include: {
          question: {
            include: {
              options: { orderBy: { label: "asc" } },
              subject: { select: { name: true } },
            },
          },
        },
      },
    },
  });

  if (!session) notFound();

  const firstQuestion = session.answers[0]?.question;
  const title = firstQuestion?.topic
    ? `${firstQuestion.subject?.name ?? "Questões"} — ${firstQuestion.topic}`
    : `${firstQuestion?.subject?.name ?? "Treino de Questões"}`;

  // ───────── Modo de Resolução (Em Andamento) ─────────
  if (!session.finishedAt) {
    return (
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <Link
            href="/questoes"
            className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text"
          >
            <ArrowLeft className="h-4 w-4" aria-hidden />
            Voltar ao Banco de Questões
          </Link>
          <span className="text-xs font-semibold uppercase tracking-wider text-muted">
            Modo de Treino Livre
          </span>
        </div>

        <QuizRunner
          sessionId={session.id}
          startedAtMs={session.startedAt.getTime()}
          limitSeconds={session.limitSeconds}
          serverNowMs={serverNow()}
          questions={session.answers.map((a) => {
            const isAnswered = a.chosenLabel !== null;
            const correctOpt = a.question.options.find((o) => o.isCorrect);
            return {
              position: a.position,
              topic: a.question.topic,
              support: a.question.support,
              statement: a.question.statement,
              options: a.question.options.map((o) => ({ label: o.label, text: o.text })),
              chosen: a.chosenLabel,
              flagged: a.flagged,
              correctLabel: isAnswered ? (correctOpt?.label ?? null) : null,
              explanation: isAnswered ? a.question.explanation : null,
              isCorrect: isAnswered ? a.isCorrect : null,
            };
          })}
        />
      </div>
    );
  }

  // ───────── Modo de Resultado (Concluído) ─────────
  const rows: AnswerRow[] = session.answers.map((a) => ({
    questionId: a.questionId,
    topic: a.question.topic,
    segmentId: a.question.segmentId,
    pageRef: a.question.pageRef,
    chosen: a.chosenLabel,
    correctLabel: a.question.options.find((o) => o.isCorrect)?.label ?? "",
    seconds: a.secondsSpent,
  }));

  const sc = score(rows);
  const usedSeconds = Math.min(
    session.limitSeconds,
    Math.round((session.finishedAt.getTime() - session.startedAt.getTime()) / 1000)
  );

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <Link
        href="/questoes"
        className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text"
      >
        <ArrowLeft className="h-4 w-4" aria-hidden />
        Voltar ao Banco de Questões
      </Link>

      <PageHeader
        eyebrow="Treino Concluído"
        title="Resultado da Prática"
        description={`Tempo dedicado: ${fmtDuration(usedSeconds)}. Desempenho gravado no seu histórico.`}
      />

      {/* Cartão de Aproveitamento */}
      <Card tone="ink" className="flex flex-wrap items-center gap-7 p-6 sm:p-8 shadow-card">
        <Ring
          value={sc.percent / 100}
          size={140}
          stroke={14}
          color={sc.percent >= 70 ? "var(--ok)" : sc.percent >= 50 ? "var(--gold)" : "var(--primary)"}
          track="rgb(255 255 255 / 0.12)"
          label={`${sc.percent}% de acerto`}
        >
          <span className="font-display text-5xl font-bold leading-none">
            <Count value={sc.percent} suffix="%" />
          </span>
          <span className="mt-1 text-[11px] font-semibold uppercase tracking-widest text-on-ink-muted">
            aproveitamento
          </span>
        </Ring>

        <div className="flex-1 space-y-3 min-w-[200px]">
          <div className="flex items-center gap-2">
            <span className="font-display text-2xl font-bold text-on-ink">
              {sc.correct} de {sc.total} questões corretas
            </span>
          </div>
          <p className="text-sm text-on-ink-muted">
            {sc.percent >= 70
              ? "Excelente rendimento! Você demonstrou forte domínio do conteúdo praticado."
              : sc.percent >= 50
              ? "Bom desempenho. Revise os pontos onde houve dúvida para consolidar o assunto."
              : "Atenção a este assunto. Leia as justificativas e faça novas questões para fixar."}
          </p>

          <div className="pt-2 flex flex-wrap gap-3">
            <LinkButton href="/questoes" variant="primary" size="sm">
              Escolher Novo Assunto
            </LinkButton>
            <LinkButton href="/desempenho" variant="secondary" size="sm">
              Ver Gráficos de Desempenho
            </LinkButton>
          </div>
        </div>
      </Card>

      {/* Detalhamento de Questões */}
      <div className="space-y-4 pt-2">
        <h3 className="font-display text-lg font-bold uppercase tracking-wide text-text">
          Revisão Questão a Questão
        </h3>

        <div className="space-y-3">
          {session.answers.map((a, i) => {
            const correctOpt = a.question.options.find((o) => o.isCorrect);
            const isHit = a.isCorrect === true;

            return (
              <Card key={a.id} className="p-5 space-y-3 border border-border bg-surface">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs font-bold text-muted">
                      Questão {i + 1}
                    </span>
                    {a.question.topic && (
                      <Badge tone="neutral" className="text-[10px]">
                        {a.question.topic}
                      </Badge>
                    )}
                  </div>
                  <Badge tone={isHit ? "ok" : "warn"} className="text-xs font-bold">
                    {isHit ? "Acertou" : "Errou"}
                  </Badge>
                </div>

                <p className="text-sm text-text whitespace-pre-wrap leading-relaxed font-normal">
                  {a.question.statement}
                </p>

                {/* Alternativas */}
                <div className="space-y-1.5 pt-1">
                  {a.question.options.map((opt) => {
                    const isChosen = a.chosenLabel === opt.label;
                    const isRight = opt.isCorrect;

                    let bgClass = "border-border/60 bg-surface-2/40 text-text";
                    if (isRight) {
                      bgClass = "border-ok/40 bg-ok/10 text-ok font-medium";
                    } else if (isChosen && !isRight) {
                      bgClass = "border-primary/40 bg-primary/10 text-primary line-through";
                    }

                    return (
                      <div
                        key={opt.label}
                        className={`flex items-start gap-2.5 rounded-lg border p-2 text-xs transition ${bgClass}`}
                      >
                        <span className="font-bold shrink-0">{opt.label})</span>
                        <span className="flex-1">{opt.text}</span>
                        {isRight && <CircleCheck className="h-4 w-4 shrink-0 text-ok" />}
                        {isChosen && !isRight && <CircleX className="h-4 w-4 shrink-0 text-primary" />}
                      </div>
                    );
                  })}
                </div>

                {/* Justificativa / Comentário */}
                {a.question.explanation && (
                  <div className="rounded-lg bg-surface-3 p-3 text-xs text-text/90 space-y-1 mt-2">
                    <span className="font-bold text-muted block uppercase tracking-wider text-[10px]">
                      Justificativa Oficial
                    </span>
                    <p className="leading-relaxed">{a.question.explanation}</p>
                  </div>
                )}
              </Card>
            );
          })}
        </div>
      </div>
    </div>
  );
}
