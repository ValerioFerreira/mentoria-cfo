import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import {
  AlertTriangle,
  ArrowLeft,
  Award,
  CheckCircle2,
  CircleCheck,
  CircleX,
  Clock,
  ExternalLink,
  Flag,
  HelpCircle,
  RotateCcw,
  ShieldAlert,
  ShieldCheck,
  Trophy,
  XCircle,
} from "lucide-react";
import { Badge, Card, Count, LinkButton, PageHeader, Progress, Ring } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { EXAM_CONFIGS } from "@/lib/data/simulados";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { fmtDuration } from "@/lib/ui-format";

export const metadata: Metadata = {
  title: "Resultado do Simulado Oficial — Missão CBMPE 2026",
};

export default async function SimuladoResultadoPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role))) {
    redirect("/simulados");
  }

  const { id } = await params;

  const session = await db.quizSession.findFirst({
    where: {
      id,
      userId: user.id,
      kind: "SIMULADO",
    },
    include: {
      answers: {
        orderBy: { position: "asc" },
        include: {
          question: {
            include: {
              options: { orderBy: { label: "asc" } },
              subject: { select: { id: true, name: true, block: true } },
            },
          },
        },
      },
    },
  });

  if (!session) notFound();

  // Se a prova ainda estiver em andamento, redireciona para a execução
  if (!session.finishedAt) {
    redirect(`/simulados/${session.id}`);
  }

  const contestKey = (session.contest as import("@/lib/data/simulados").SupportedSimuladoContest) || "CBMPE_OFICIAL";
  const config = EXAM_CONFIGS[contestKey] || EXAM_CONFIGS.CBMPE_OFICIAL;

  const totalQuestions = session.total || session.answers.length;
  const totalCorrect = session.score ?? session.answers.filter((a) => a.isCorrect).length;
  const totalPercent = totalQuestions > 0 ? Math.round((totalCorrect / totalQuestions) * 100) : 0;

  const usedSeconds = Math.min(
    session.limitSeconds,
    Math.max(1, Math.round((session.finishedAt.getTime() - session.startedAt.getTime()) / 1000))
  );

  // ───────── AVALIAÇÃO DAS REGRAS OFICIAIS DE CORTE DO EDITAL ─────────
  // 1. Desempenho por Bloco
  const blockStats: Record<
    "I" | "II" | "III",
    { total: number; correct: number; requiredMin: number }
  > = {
    I: { total: 0, correct: 0, requiredMin: config.blocks.I.minQuestions },
    II: { total: 0, correct: 0, requiredMin: config.blocks.II.minQuestions },
    III: { total: 0, correct: 0, requiredMin: config.blocks.III.minQuestions },
  };

  // 2. Desempenho por Disciplina
  const subjectStats = new Map<
    string,
    { id: string; name: string; block: "I" | "II" | "III"; total: number; correct: number }
  >();

  for (const a of session.answers) {
    const s = a.question.subject;
    const blk = (s.block as "I" | "II" | "III") || "I";

    // Acumular bloco
    blockStats[blk].total++;
    if (a.isCorrect) {
      blockStats[blk].correct++;
    }

    // Acumular disciplina
    let curSub = subjectStats.get(s.id);
    if (!curSub) {
      curSub = { id: s.id, name: s.name, block: blk, total: 0, correct: 0 };
      subjectStats.set(s.id, curSub);
    }
    curSub.total++;
    if (a.isCorrect) curSub.correct++;
  }

  const blockI = blockStats.I;
  const blockII = blockStats.II;
  const blockIII = blockStats.III;

  const blockIPct = blockI.total > 0 ? Math.round((blockI.correct / blockI.total) * 100) : 0;
  const blockIIPct = blockII.total > 0 ? Math.round((blockII.correct / blockII.total) * 100) : 0;
  const blockIIIPct = blockIII.total > 0 ? Math.round((blockIII.correct / blockIII.total) * 100) : 0;

  const blockIPassed = blockI.correct >= blockI.requiredMin;
  const blockIIPassed = blockII.correct >= blockII.requiredMin;
  const blockIIIPassed = blockIII.correct >= blockIII.requiredMin;

  // Verificar se zerou alguma matéria
  const zeroedSubjects: string[] = [];
  for (const sub of subjectStats.values()) {
    if (sub.correct === 0) {
      zeroedSubjects.push(sub.name);
    }
  }
  const noZeroPassed = zeroedSubjects.length === 0;

  // Nota geral mínima de 30%
  const minTotalPassed = totalPercent >= config.minPercentTotal;

  // Aprovado no critério oficial do edital?
  const passedCutoff =
    blockIPassed && blockIIPassed && blockIIIPassed && noZeroPassed && minTotalPassed;

  // Identificação de pontos fortes (>= 70%) e a reforçar (< 50% ou zerada)
  const subjectsList = Array.from(subjectStats.values());
  const strongSubjects = subjectsList.filter(
    (s) => s.total > 0 && s.correct / s.total >= 0.7
  );
  const weakSubjects = subjectsList.filter(
    (s) => s.total > 0 && s.correct / s.total < 0.5
  );

  return (
    <div className="mx-auto max-w-4xl space-y-8">
      {/* Botão Voltar */}
      <div className="flex items-center justify-between">
        <Link
          href="/simulados"
          className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text"
        >
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Voltar para Central de Simulados
        </Link>
        <span className="text-xs font-semibold uppercase tracking-wider text-muted">
          {session.finishedAt.toLocaleDateString("pt-BR")}
        </span>
      </div>

      {/* Cabeçalho da Página */}
      <PageHeader
        eyebrow="Resultado Oficial da Prova"
        title={session.title ?? config.title}
        description={`Tempo total de realização: ${fmtDuration(usedSeconds)} de ${fmtDuration(session.limitSeconds)} regulamentares.`}
      />

      {/* Cartão Oficial de Veredito / Perfil de Aprovação */}
      <Card
        className={`p-6 sm:p-8 space-y-6 border shadow-lg ${
          passedCutoff
            ? "border-ok/40 bg-gradient-to-br from-ok/10 via-surface to-surface"
            : "border-primary/40 bg-gradient-to-br from-primary/10 via-surface to-surface"
        }`}
      >
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="flex items-center gap-5">
            <Ring
              value={totalPercent / 100}
              size={110}
              stroke={11}
              color={passedCutoff ? "var(--ok)" : "var(--primary)"}
              track="rgb(255 255 255 / 0.12)"
              label={`${totalPercent}% de aproveitamento`}
            >
              <span className="font-display text-3xl font-bold leading-none">
                <Count value={totalPercent} suffix="%" />
              </span>
            </Ring>

            <div>
              <div className="flex items-center gap-2">
                {passedCutoff ? (
                  <Badge tone="ok" className="text-xs font-bold gap-1 py-1 px-2.5">
                    <ShieldCheck className="h-4 w-4" />
                    <span>APROVADO NO PERFIL MÍNIMO DO EDITAL</span>
                  </Badge>
                ) : (
                  <Badge tone="primary" className="text-xs font-bold gap-1 py-1 px-2.5">
                    <ShieldAlert className="h-4 w-4" />
                    <span>REPROVADO NOS CRITÉRIOS DE CORTE</span>
                  </Badge>
                )}
              </div>
              <h2 className="font-display text-2xl font-bold text-text mt-2">
                {totalCorrect} de {totalQuestions} pontos
              </h2>
              <p className="text-xs text-muted mt-0.5">
                {passedCutoff
                  ? "Parabéns! Você superou todas as barreiras de corte do edital (30% por bloco e sem zerar disciplinas)."
                  : "Atenção: você não atingiu o perfil mínimo de classificação por corte regulamentar do edital."}
              </p>
            </div>
          </div>

          <div className="flex flex-wrap sm:flex-col gap-2 shrink-0">
            <LinkButton href="/simulados" variant="secondary" size="sm">
              Novo Simulado
            </LinkButton>
            <LinkButton href="/desempenho" variant="primary" size="sm">
              Ver no Desempenho
            </LinkButton>
          </div>
        </div>

        {/* Diagnóstico das Regras de Corte do Edital */}
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 pt-4 border-t border-border/70">
          {/* Bloco I */}
          <div
            className={`rounded-xl border p-3.5 space-y-1 ${
              blockIPassed
                ? "border-ok/30 bg-ok/5 text-ok"
                : "border-primary/30 bg-primary/5 text-primary"
            }`}
          >
            <div className="flex items-center justify-between text-xs font-bold">
              <span>Bloco I</span>
              <span>{blockIPassed ? "Aprovado" : "Reprovado"}</span>
            </div>
            <p className="text-lg font-bold text-text tabular">
              {blockI.correct}/{blockI.total}{" "}
              <span className="text-xs font-normal text-muted">({blockIPct}%)</span>
            </p>
            <p className="text-[11px] text-muted">Mínimo: {blockI.requiredMin} acertos (30%)</p>
          </div>

          {/* Bloco II */}
          <div
            className={`rounded-xl border p-3.5 space-y-1 ${
              blockIIPassed
                ? "border-ok/30 bg-ok/5 text-ok"
                : "border-primary/30 bg-primary/5 text-primary"
            }`}
          >
            <div className="flex items-center justify-between text-xs font-bold">
              <span>Bloco II</span>
              <span>{blockIIPassed ? "Aprovado" : "Reprovado"}</span>
            </div>
            <p className="text-lg font-bold text-text tabular">
              {blockII.correct}/{blockII.total}{" "}
              <span className="text-xs font-normal text-muted">({blockIIPct}%)</span>
            </p>
            <p className="text-[11px] text-muted">Mínimo: {blockII.requiredMin} acertos (30%)</p>
          </div>

          {/* Bloco III */}
          <div
            className={`rounded-xl border p-3.5 space-y-1 ${
              blockIIIPassed
                ? "border-ok/30 bg-ok/5 text-ok"
                : "border-primary/30 bg-primary/5 text-primary"
            }`}
          >
            <div className="flex items-center justify-between text-xs font-bold">
              <span>Bloco III</span>
              <span>{blockIIIPassed ? "Aprovado" : "Reprovado"}</span>
            </div>
            <p className="text-lg font-bold text-text tabular">
              {blockIII.correct}/{blockIII.total}{" "}
              <span className="text-xs font-normal text-muted">({blockIIIPct}%)</span>
            </p>
            <p className="text-[11px] text-muted">Mínimo: {blockIII.requiredMin} acertos (30%)</p>
          </div>

          {/* Regra de Não Zerar Matéria */}
          <div
            className={`rounded-xl border p-3.5 space-y-1 ${
              noZeroPassed
                ? "border-ok/30 bg-ok/5 text-ok"
                : "border-primary/30 bg-primary/5 text-primary"
            }`}
          >
            <div className="flex items-center justify-between text-xs font-bold">
              <span>Não Zerar</span>
              <span>{noZeroPassed ? "OK" : "Eliminado"}</span>
            </div>
            <p className="text-sm font-bold text-text">
              {noZeroPassed ? "Nenhuma zerada" : `${zeroedSubjects.length} zerada(s)`}
            </p>
            <p className="text-[11px] text-muted">
              {noZeroPassed
                ? "Pontuou em todas as matérias"
                : `Zerou: ${zeroedSubjects.join(", ")}`}
            </p>
          </div>
        </div>
      </Card>

      {/* Análise de Pontos Fortes e Fracos */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {/* Pontos Fortes */}
        <Card className="p-5 space-y-3 border border-border bg-surface">
          <div className="flex items-center gap-2 text-ok">
            <Trophy className="h-5 w-5" />
            <h3 className="font-display text-sm font-bold uppercase tracking-wider text-text">
              Pontos Fortes (Aproveitamento ≥ 70%)
            </h3>
          </div>
          {strongSubjects.length === 0 ? (
            <p className="text-xs text-muted">
              Nenhuma disciplina atingiu 70% de acerto neste simulado.
            </p>
          ) : (
            <div className="space-y-2">
              {strongSubjects.map((s) => (
                <div
                  key={s.id}
                  className="flex items-center justify-between text-xs p-2 rounded-lg bg-ok/10 border border-ok/20"
                >
                  <span className="font-semibold text-text">{s.name}</span>
                  <span className="font-bold text-ok">
                    {s.correct}/{s.total} ({Math.round((s.correct / s.total) * 100)}%)
                  </span>
                </div>
              ))}
            </div>
          )}
        </Card>

        {/* Pontos a Reforçar */}
        <Card className="p-5 space-y-3 border border-border bg-surface">
          <div className="flex items-center gap-2 text-primary">
            <AlertTriangle className="h-5 w-5" />
            <h3 className="font-display text-sm font-bold uppercase tracking-wider text-text">
              Pontos de Atenção (Aproveitamento &lt; 50%)
            </h3>
          </div>
          {weakSubjects.length === 0 ? (
            <p className="text-xs text-muted">
              Excelente! Nenhuma disciplina ficou abaixo de 50% de acerto.
            </p>
          ) : (
            <div className="space-y-2">
              {weakSubjects.map((s) => (
                <div
                  key={s.id}
                  className="flex items-center justify-between text-xs p-2 rounded-lg bg-primary/10 border border-primary/20"
                >
                  <span className="font-semibold text-text">{s.name}</span>
                  <span className="font-bold text-primary">
                    {s.correct}/{s.total} ({Math.round((s.correct / s.total) * 100)}%)
                  </span>
                </div>
              ))}
            </div>
          )}
        </Card>
      </div>

      {/* Desempenho Detalhado por Disciplina */}
      <Card className="p-6 space-y-4 border border-border bg-surface">
        <h3 className="font-display text-base font-bold uppercase tracking-wide text-text">
          Desempenho por Disciplina
        </h3>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="border-b border-border bg-surface-2/60 text-muted uppercase font-bold tracking-wider">
              <tr>
                <th className="py-2.5 px-3">Disciplina</th>
                <th className="py-2.5 px-2">Bloco</th>
                <th className="py-2.5 px-2 text-right">Acertos</th>
                <th className="py-2.5 px-2 text-right">Taxa</th>
                <th className="py-2.5 px-3 text-right">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/60">
              {subjectsList.map((sub) => {
                const subPct = sub.total > 0 ? Math.round((sub.correct / sub.total) * 100) : 0;
                const isZero = sub.correct === 0;

                return (
                  <tr key={sub.id} className="hover:bg-surface-2/40">
                    <td className="py-2.5 px-3 font-semibold text-text">{sub.name}</td>
                    <td className="py-2.5 px-2">
                      <Badge tone="neutral" className="text-[10px]">
                        Bloco {sub.block}
                      </Badge>
                    </td>
                    <td className="py-2.5 px-2 text-right font-mono font-bold">
                      {sub.correct}/{sub.total}
                    </td>
                    <td className="py-2.5 px-2 text-right font-mono font-bold">
                      <span
                        className={
                          subPct >= 70 ? "text-ok" : subPct >= 50 ? "text-gold" : "text-primary"
                        }
                      >
                        {subPct}%
                      </span>
                    </td>
                    <td className="py-2.5 px-3 text-right">
                      {isZero ? (
                        <Badge tone="primary" className="text-[10px]">
                          Zerada
                        </Badge>
                      ) : subPct >= 70 ? (
                        <Badge tone="ok" className="text-[10px]">
                          Forte
                        </Badge>
                      ) : (
                        <Badge tone="neutral" className="text-[10px]">
                          Regular
                        </Badge>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Revisão Completa da Prova (Questão a Questão) */}
      <div className="space-y-4 pt-4">
        <div className="flex items-center justify-between border-b border-border pb-2">
          <h3 className="font-display text-lg font-bold uppercase tracking-wide text-text">
            Gabarito Completo e Comentários da Prova
          </h3>
          <span className="text-xs text-muted font-semibold">
            {totalQuestions} questões comentadas
          </span>
        </div>

        <div className="space-y-4">
          {session.answers.map((a, i) => {
            const correctOpt = a.question.options.find((o) => o.isCorrect);
            const isHit = a.isCorrect === true;
            const isBlank = a.chosenLabel === null;

            return (
              <Card key={a.id} className="p-5 space-y-3.5 border border-border bg-surface">
                {/* Cabeçalho da Questão */}
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-border/60 pb-2">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs font-bold text-muted">
                      Questão {i + 1}
                    </span>
                    <Badge tone="neutral" className="text-[10px]">
                      Bloco {a.question.subject.block}
                    </Badge>
                    <Badge tone="primary" className="text-[10px]">
                      {a.question.subject.name}
                    </Badge>
                    {a.question.topic && (
                      <span className="text-xs text-muted truncate max-w-xs">
                        · {a.question.topic}
                      </span>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    {a.flagged && (
                      <Badge tone="neutral" className="text-[10px] gap-1">
                        <Flag className="h-3 w-3" />
                        <span>Revisada</span>
                      </Badge>
                    )}
                    <Badge
                      tone={isHit ? "ok" : isBlank ? "neutral" : "primary"}
                      className="text-xs font-bold"
                    >
                      {isHit ? "Acertou" : isBlank ? "Em Branco" : "Errou"}
                    </Badge>
                  </div>
                </div>

                {/* Texto de Apoio (se houver) */}
                {a.question.support && (
                  <div className="rounded-xl border border-border/60 bg-surface-2/40 p-3.5 text-xs text-text leading-relaxed whitespace-pre-wrap">
                    <span className="font-bold text-muted uppercase tracking-wider text-[10px] block mb-1">
                      Texto de Apoio
                    </span>
                    {a.question.support}
                  </div>
                )}

                {/* Enunciado */}
                <p className="text-sm text-text whitespace-pre-wrap leading-relaxed font-normal">
                  {a.question.statement}
                </p>

                {/* Alternativas */}
                <div className="space-y-1.5 pt-1">
                  {a.question.options.map((opt) => {
                    const isChosen = a.chosenLabel === opt.label;
                    const isRight = opt.isCorrect;

                    let bgClass = "border-border/60 bg-surface-2/30 text-text";
                    if (isRight) {
                      bgClass = "border-ok/50 bg-ok/10 text-ok font-medium";
                    } else if (isChosen && !isRight) {
                      bgClass = "border-primary/50 bg-primary/10 text-primary line-through";
                    }

                    return (
                      <div
                        key={opt.label}
                        className={`flex items-start gap-2.5 rounded-lg border p-2.5 text-xs transition ${bgClass}`}
                      >
                        <span className="font-bold shrink-0">{opt.label})</span>
                        <span className="flex-1 leading-snug">{opt.text}</span>
                        {isRight && (
                          <CircleCheck className="h-4 w-4 shrink-0 text-ok" aria-hidden />
                        )}
                        {isChosen && !isRight && (
                          <CircleX className="h-4 w-4 shrink-0 text-primary" aria-hidden />
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Justificativa / Comentário */}
                {a.question.explanation && (
                  <div className="rounded-xl bg-surface-3/80 p-3.5 text-xs text-text/90 space-y-1 mt-2">
                    <span className="font-bold text-muted block uppercase tracking-wider text-[10px]">
                      Justificativa Oficial do Gabarito
                    </span>
                    <p className="leading-relaxed whitespace-pre-wrap">{a.question.explanation}</p>
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
