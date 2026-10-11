"use client";

import { useCallback, useEffect, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import {
  AlertTriangle,
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  Clock,
  Flag,
  HelpCircle,
  ListFilter,
  Loader2,
  Send,
  ShieldAlert,
} from "lucide-react";
import { Badge, Button, Card } from "@/components/ui";
import { fmtClock } from "@/lib/ui-format";
import { finishSimulado, saveSimuladoAnswer } from "@/lib/quiz/simulado-actions";

export interface SimuladoQuestionItem {
  position: number;
  subjectName: string;
  block: "I" | "II" | "III";
  topic: string | null;
  statement: string;
  support: string | null;
  options: { label: string; text: string }[];
  chosenLabel: string | null;
  flagged: boolean;
}

interface Props {
  sessionId: string;
  title: string;
  startedAtMs: number;
  limitSeconds: number;
  serverNowMs: number;
  questions: SimuladoQuestionItem[];
}

export function SimuladoRunner({
  sessionId,
  title,
  startedAtMs,
  limitSeconds,
  serverNowMs,
  questions: initialQuestions,
}: Props) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  // Estado das respostas do aluno
  const [questions, setQuestions] = useState<SimuladoQuestionItem[]>(initialQuestions);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [showConfirmModal, setShowConfirmModal] = useState<boolean>(false);
  const [saveStatus, setSaveStatus] = useState<"idle" | "saving" | "saved" | "error">("idle");

  // Cronômetro
  const elapsedOnMount = Math.max(0, Math.floor((serverNowMs - startedAtMs) / 1000));
  const [secondsRemaining, setSecondsRemaining] = useState<number>(
    Math.max(0, limitSeconds - elapsedOnMount)
  );

  const currentQ = questions[currentIndex];

  // Auto-entrega ao esgotar o tempo
  const autoFinishTriggered = useRef(false);

  const handleFinish = useCallback(async () => {
    startTransition(async () => {
      const res = await finishSimulado(sessionId);
      if (res.ok) {
        router.push(`/simulados/resultado/${sessionId}`);
      }
    });
  }, [sessionId, router]);

  useEffect(() => {
    if (secondsRemaining <= 0) {
      if (!autoFinishTriggered.current) {
        autoFinishTriggered.current = true;
        handleFinish();
      }
      return;
    }

    const interval = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          if (!autoFinishTriggered.current) {
            autoFinishTriggered.current = true;
            handleFinish();
          }
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [secondsRemaining, handleFinish]);

  // Salvar resposta no servidor de forma contínua
  const handleSelectOption = (label: string) => {
    const newChosen = currentQ.chosenLabel === label ? null : label;

    // Atualiza estado local imediatamente (otimista)
    setQuestions((prev) =>
      prev.map((q, idx) =>
        idx === currentIndex ? { ...q, chosenLabel: newChosen } : q
      )
    );

    setSaveStatus("saving");

    startTransition(async () => {
      const res = await saveSimuladoAnswer({
        sessionId,
        position: currentQ.position,
        chosenLabel: newChosen,
      });

      if (res.ok) {
        setSaveStatus("saved");
        setTimeout(() => setSaveStatus("idle"), 2000);
      } else {
        setSaveStatus("error");
      }
    });
  };

  // Alternar marcação para revisão (flagged)
  const handleToggleFlag = () => {
    const newFlagged = !currentQ.flagged;

    setQuestions((prev) =>
      prev.map((q, idx) =>
        idx === currentIndex ? { ...q, flagged: newFlagged } : q
      )
    );

    startTransition(async () => {
      await saveSimuladoAnswer({
        sessionId,
        position: currentQ.position,
        chosenLabel: currentQ.chosenLabel,
        flagged: newFlagged,
      });
    });
  };

  // Contadores de progresso
  const totalQuestions = questions.length;
  const answeredCount = questions.filter((q) => q.chosenLabel !== null).length;
  const flaggedCount = questions.filter((q) => q.flagged).length;
  const unansweredCount = totalQuestions - answeredCount;

  const isLowTime = secondsRemaining < 900; // Menos de 15 min

  return (
    <div className="space-y-6">
      {/* Barra Superior Fixa do Simulado */}
      <div className="sticky top-0 z-20 flex flex-col sm:flex-row sm:items-center justify-between gap-3 rounded-2xl border border-border bg-ink p-4 text-on-ink shadow-lg">
        <div className="flex items-center gap-3 min-w-0">
          <div className="h-3 w-3 rounded-full bg-primary animate-pulse shrink-0" />
          <div className="min-w-0">
            <h1 className="font-display text-sm font-bold uppercase tracking-wide truncate text-on-ink">
              {title}
            </h1>
            <p className="text-xs text-on-ink-muted">
              {answeredCount} de {totalQuestions} respondidas · {flaggedCount} para revisar
            </p>
          </div>
        </div>

        {/* Cronômetro e Botão de Entrega */}
        <div className="flex items-center gap-4 self-end sm:self-auto">
          {/* Indicador de Salvamento */}
          <div className="hidden md:flex items-center text-[11px] text-on-ink-muted">
            {saveStatus === "saving" && <span>Salvando...</span>}
            {saveStatus === "saved" && <span className="text-ok">✓ Resposta salva</span>}
            {saveStatus === "error" && <span className="text-primary">Erro ao salvar</span>}
          </div>

          <div
            className={`flex items-center gap-2 rounded-xl px-3 py-1.5 font-mono text-sm font-bold tabular transition ${
              isLowTime
                ? "bg-primary text-on-primary animate-pulse"
                : "bg-white/10 text-on-ink"
            }`}
          >
            <Clock className="h-4 w-4" />
            <span>{fmtClock(secondsRemaining)}</span>
          </div>

          <Button
            size="sm"
            variant="primary"
            onClick={() => setShowConfirmModal(true)}
            disabled={isPending}
            className="gap-1.5"
          >
            <Send className="h-3.5 w-3.5" />
            <span>Entregar Prova</span>
          </Button>
        </div>
      </div>

      {/* Conteúdo Principal: Questão + Grade de Navegação */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
        {/* Painel Central: A Questão Atual */}
        <div className="lg:col-span-3 space-y-4">
          <Card className="p-6 sm:p-8 space-y-6 border border-border bg-surface shadow-card">
            {/* Metadados da Questão */}
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-border/70 pb-4">
              <div className="flex flex-wrap items-center gap-2">
                <span className="font-display text-lg font-bold text-text">
                  Questão {currentQ.position} de {totalQuestions}
                </span>
                <Badge tone="neutral" className="text-xs font-semibold">
                  Bloco {currentQ.block}
                </Badge>
                <Badge tone="primary" className="text-xs font-semibold">
                  {currentQ.subjectName}
                </Badge>
                {currentQ.topic && (
                  <span className="text-xs text-muted font-medium truncate max-w-xs">
                    · {currentQ.topic}
                  </span>
                )}
              </div>

              <button
                type="button"
                onClick={handleToggleFlag}
                className={`flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-semibold transition cursor-pointer ${
                  currentQ.flagged
                    ? "bg-gold text-on-gold font-bold shadow-xs"
                    : "bg-surface-2 text-muted hover:bg-surface-3 hover:text-text"
                }`}
                title="Marcar questão para revisar antes de entregar"
              >
                <Flag className="h-3.5 w-3.5" />
                <span>{currentQ.flagged ? "Marcada para Revisão" : "Marcar para Revisar"}</span>
              </button>
            </div>

            {/* Texto de Apoio (se houver) */}
            {currentQ.support && (
              <div className="rounded-xl border border-border/70 bg-surface-2/40 p-4 text-xs text-text leading-relaxed whitespace-pre-wrap">
                <span className="font-bold text-muted uppercase tracking-wider text-[10px] block mb-1">
                  Texto de Referência
                </span>
                {currentQ.support}
              </div>
            )}

            {/* Enunciado */}
            <p className="text-sm sm:text-base font-normal text-text leading-relaxed whitespace-pre-wrap">
              {currentQ.statement}
            </p>

            {/* Alternativas de A a E */}
            <div className="space-y-2.5 pt-2">
              {currentQ.options.map((opt) => {
                const isSelected = currentQ.chosenLabel === opt.label;

                return (
                  <button
                    key={opt.label}
                    type="button"
                    onClick={() => handleSelectOption(opt.label)}
                    className={`w-full flex items-start gap-3.5 rounded-xl border p-3.5 text-left text-sm transition cursor-pointer select-none ${
                      isSelected
                        ? "border-primary bg-primary/10 text-text font-medium shadow-xs"
                        : "border-border/70 bg-surface-2/30 hover:border-border hover:bg-surface-2 text-text"
                    }`}
                  >
                    <span
                      className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-lg font-bold text-xs transition ${
                        isSelected
                          ? "bg-primary text-on-primary"
                          : "bg-surface-3 text-muted"
                      }`}
                    >
                      {opt.label}
                    </span>
                    <span className="flex-1 leading-snug pt-0.5">{opt.text}</span>
                  </button>
                );
              })}
            </div>

            {/* Navegação Entre Questões */}
            <div className="flex items-center justify-between border-t border-border/70 pt-5">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
                disabled={currentIndex === 0}
                className="gap-1.5"
              >
                <ArrowLeft className="h-4 w-4" />
                <span>Anterior</span>
              </Button>

              <div className="text-xs font-semibold text-muted">
                {currentQ.chosenLabel ? (
                  <span className="text-ok font-bold">Alternativa {currentQ.chosenLabel} assinalada</span>
                ) : (
                  <span>Em branco</span>
                )}
              </div>

              <Button
                variant="primary"
                size="sm"
                onClick={() =>
                  setCurrentIndex((prev) => Math.min(totalQuestions - 1, prev + 1))
                }
                disabled={currentIndex === totalQuestions - 1}
                className="gap-1.5"
              >
                <span>Próxima</span>
                <ArrowRight className="h-4 w-4" />
              </Button>
            </div>
          </Card>
        </div>

        {/* Barra Lateral: Grade de Navegação das Questões */}
        <div className="space-y-4">
          <Card className="p-4 space-y-4 border border-border bg-surface shadow-xs">
            <div className="flex items-center justify-between border-b border-border/70 pb-2">
              <span className="text-xs font-bold uppercase tracking-wider text-muted">
                Grade de Questões
              </span>
              <span className="text-xs font-mono font-semibold text-text">
                {answeredCount}/{totalQuestions}
              </span>
            </div>

            {/* Legenda */}
            <div className="grid grid-cols-2 gap-2 text-[11px] text-muted pb-1 border-b border-border/50">
              <div className="flex items-center gap-1.5">
                <div className="h-3 w-3 rounded bg-primary/20 border border-primary/60" />
                <span>Respondida</span>
              </div>
              <div className="flex items-center gap-1.5">
                <div className="h-3 w-3 rounded bg-surface-3 border border-border/60" />
                <span>Em branco</span>
              </div>
              <div className="flex items-center gap-1.5 col-span-2">
                <div className="h-3 w-3 rounded bg-gold text-on-gold font-bold flex items-center justify-center text-[8px]">
                  F
                </div>
                <span>Marcada para revisar</span>
              </div>
            </div>

            {/* Grade com Todos os Botões */}
            <div className="grid grid-cols-5 sm:grid-cols-6 lg:grid-cols-5 gap-1.5 max-h-96 overflow-y-auto pr-1">
              {questions.map((q, idx) => {
                const isCurrent = idx === currentIndex;
                const isAnswered = q.chosenLabel !== null;
                const isFlagged = q.flagged;

                let btnClass = "bg-surface-2 text-muted border-border/70 hover:bg-surface-3";
                if (isAnswered) {
                  btnClass = "bg-primary/20 text-primary border-primary/50 font-bold";
                }
                if (isFlagged) {
                  btnClass = "bg-gold text-on-gold border-gold font-bold";
                }
                if (isCurrent) {
                  btnClass += " ring-2 ring-primary ring-offset-1 ring-offset-surface font-extrabold";
                }

                return (
                  <button
                    key={q.position}
                    type="button"
                    onClick={() => setCurrentIndex(idx)}
                    className={`flex h-8 w-full items-center justify-center rounded-lg border text-xs transition cursor-pointer ${btnClass}`}
                    title={`Questão ${q.position} (${q.subjectName})`}
                  >
                    {q.position}
                  </button>
                );
              })}
            </div>
          </Card>
        </div>
      </div>

      {/* Modal de Confirmação de Entrega */}
      {showConfirmModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-xs">
          <div className="relative w-full max-w-md rounded-2xl border border-border bg-surface p-6 text-text shadow-2xl space-y-4">
            <div className="flex items-center gap-3 text-primary">
              <ShieldAlert className="h-6 w-6 shrink-0" />
              <h3 className="font-display text-lg font-bold uppercase tracking-wide text-text">
                Confirmar Entrega do Simulado
              </h3>
            </div>

            <p className="text-sm text-text leading-relaxed">
              Você tem certeza de que deseja finalizar e entregar seu simulado agora?
            </p>

            <div className="rounded-xl border border-border bg-surface-2/40 p-3 space-y-1.5 text-xs">
              <div className="flex justify-between">
                <span className="text-muted">Questões respondidas:</span>
                <span className="font-bold text-ok">{answeredCount}</span>
              </div>
              {unansweredCount > 0 && (
                <div className="flex justify-between">
                  <span className="text-muted">Questões em branco:</span>
                  <span className="font-bold text-primary">{unansweredCount}</span>
                </div>
              )}
              {flaggedCount > 0 && (
                <div className="flex justify-between">
                  <span className="text-muted">Marcadas para revisão:</span>
                  <span className="font-bold text-gold">{flaggedCount}</span>
                </div>
              )}
              <div className="flex justify-between border-t border-border/50 pt-1">
                <span className="text-muted">Tempo restante:</span>
                <span className="font-mono font-bold text-text">
                  {fmtClock(secondsRemaining)}
                </span>
              </div>
            </div>

            {unansweredCount > 0 && (
              <p className="text-xs text-primary font-medium">
                Atenção: você ainda possui {unansweredCount} questão(ões) sem resposta. As questões não respondidas serão computadas como erro.
              </p>
            )}

            <div className="flex items-center justify-end gap-3 pt-2">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setShowConfirmModal(false)}
                disabled={isPending}
              >
                Continuar Fazendo
              </Button>
              <Button
                variant="primary"
                size="sm"
                onClick={handleFinish}
                disabled={isPending}
                className="gap-1.5"
              >
                {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
                <span>Confirmar e Finalizar</span>
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
