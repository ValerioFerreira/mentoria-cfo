"use client";

import { ArrowLeft, ArrowRight, CheckCircle2, CircleCheck, CircleX, Flag, HelpCircle, Loader2, Sparkles, Timer, XCircle } from "lucide-react";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useMemo, useRef, useState, useTransition, type ReactNode } from "react";
import { Alert, Badge, Button, Card, Kbd, cx } from "@/components/ui";
import { fmtClock } from "@/lib/ui-format";
import { finishQuiz, saveAnswer } from "@/lib/quiz/actions";

export interface RunnerQuestion {
  position: number;
  topic: string | null;
  support: string | null;
  statement: string;
  options: { label: string; text: string }[];
  chosen: string | null;
  flagged: boolean;
  correctLabel?: string | null;
  explanation?: string | null;
  isCorrect?: boolean | null;
}

interface QuestionState {
  chosen: string | null;
  staged: string | null;
  confirmed: boolean;
  flagged: boolean;
  isCorrect: boolean | null;
  correctLabel: string | null;
  explanation: string | null;
}

interface Props {
  sessionId: string;
  startedAtMs: number;
  limitSeconds: number;
  serverNowMs: number;
  questions: RunnerQuestion[];
}

function formatInlineMarkdown(text: string): ReactNode {
  const parts = text.split(/(\*\*.*?\*\*|\*.*?\*|`.*?`)/g);
  return parts.map((part, idx) => {
    if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
      return (
        <strong key={idx} className="font-semibold text-text">
          {part.slice(2, -2)}
        </strong>
      );
    }
    if (part.startsWith("*") && part.endsWith("*") && part.length > 2) {
      return (
        <em key={idx} className="italic text-text">
          {part.slice(1, -1)}
        </em>
      );
    }
    if (part.startsWith("`") && part.endsWith("`") && part.length > 2) {
      return (
        <code key={idx} className="rounded bg-surface-3 px-1.5 py-0.5 font-mono text-xs font-semibold text-text">
          {part.slice(1, -1)}
        </code>
      );
    }
    return <span key={idx}>{part}</span>;
  });
}

function renderMarkdownExplanation(markdown: string): ReactNode {
  if (!markdown) return null;
  const blocks = markdown.split(/\n\s*\n/).map((b) => b.trim()).filter(Boolean);

  return (
    <div className="space-y-3 text-[14px] leading-relaxed text-text/90">
      {blocks.map((block, bIdx) => {
        // Tabela markdown
        if (block.includes("|") && block.split("\n").length >= 2) {
          const lines = block.split("\n").map((l) => l.trim()).filter(Boolean);
          const header = lines[0];
          const rows = lines.slice(1).filter((l) => !/^\|?[\s|:-]+\|?$/.test(l));
          const parseRow = (r: string) =>
            r.replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
          const headers = parseRow(header);

          return (
            <div key={bIdx} className="my-2.5 overflow-x-auto rounded-xl border border-border/70 bg-surface shadow-xs">
              <table className="w-full text-left text-xs">
                <thead className="border-b border-border/70 bg-surface-2 text-muted font-bold uppercase tracking-wider">
                  <tr>
                    {headers.map((h, i) => (
                      <th key={i} className="px-3 py-2">
                        {formatInlineMarkdown(h)}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-border/40">
                  {rows.map((row, rIdx) => (
                    <tr key={rIdx} className="hover:bg-surface-2/40">
                      {parseRow(row).map((cell, cIdx) => (
                        <td key={cIdx} className="px-3 py-2 align-top">
                          {formatInlineMarkdown(cell)}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }

        // Listas não ordenadas
        if (block.startsWith("- ") || block.startsWith("* ")) {
          const items = block.split("\n").map((l) => l.replace(/^[-*]\s+/, "").trim()).filter(Boolean);
          return (
            <ul key={bIdx} className="space-y-1.5 pl-4 list-disc marker:text-primary">
              {items.map((item, iIdx) => (
                <li key={iIdx}>{formatInlineMarkdown(item)}</li>
              ))}
            </ul>
          );
        }

        // Títulos
        if (block.startsWith("### ")) {
          return (
            <h4 key={bIdx} className="font-display text-base font-bold text-text pt-1">
              {formatInlineMarkdown(block.replace(/^###\s+/, ""))}
            </h4>
          );
        }
        if (block.startsWith("## ")) {
          return (
            <h3 key={bIdx} className="font-display text-lg font-bold text-text pt-2">
              {formatInlineMarkdown(block.replace(/^##\s+/, ""))}
            </h3>
          );
        }

        // Parágrafo padrão com preservação de quebras simples
        const lines = block.split("\n");
        return (
          <p key={bIdx}>
            {lines.map((line, lIdx) => (
              <span key={lIdx}>
                {lIdx > 0 && <br />}
                {formatInlineMarkdown(line)}
              </span>
            ))}
          </p>
        );
      })}
    </div>
  );
}

export function QuizRunner({ sessionId, startedAtMs, limitSeconds, serverNowMs, questions }: Props) {
  const router = useRouter();
  const offset = useRef(0);
  const [idx, setIdx] = useState(0);
  const [state, setState] = useState<Map<number, QuestionState>>(() =>
    new Map(
      questions.map((q) => [
        q.position,
        {
          chosen: q.chosen,
          staged: q.chosen,
          confirmed: Boolean(q.chosen),
          flagged: q.flagged,
          isCorrect: q.isCorrect ?? null,
          correctLabel: q.correctLabel ?? null,
          explanation: q.explanation ?? null,
        },
      ]),
    ),
  );
  const [remaining, setRemaining] = useState(() => Math.max(0, limitSeconds - Math.floor((serverNowMs - startedAtMs) / 1000)));
  const [confirming, setConfirming] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [pending, start] = useTransition();
  const enteredAt = useRef(0);
  const finished = useRef(false);

  const q = questions[idx];
  const cur = state.get(q.position)!;
  const answered = useMemo(() => [...state.values()].filter((s) => s.confirmed && s.chosen).length, [state]);
  const blanks = questions.length - answered;

  const finish = useCallback(
    (auto: boolean) => {
      if (finished.current) return;
      finished.current = true;
      start(async () => {
        await finishQuiz(sessionId, auto);
        router.refresh();
      });
    },
    [router, sessionId],
  );

  useEffect(() => {
    offset.current = serverNowMs - Date.now();
    enteredAt.current = Date.now();
  }, [serverNowMs]);

  useEffect(() => {
    const id = setInterval(() => {
      const left = Math.max(0, limitSeconds - Math.floor((Date.now() + offset.current - startedAtMs) / 1000));
      setRemaining(left);
      if (left === 0) finish(true);
    }, 1000);
    return () => clearInterval(id);
  }, [finish, limitSeconds, startedAtMs]);

  function selectOption(label: string) {
    if (cur.confirmed || submitting) return;
    setError(null);
    setState((m) => {
      const copy = new Map(m);
      copy.set(q.position, { ...cur, staged: cur.staged === label ? null : label });
      return copy;
    });
  }

  function clearStaged() {
    if (cur.confirmed || submitting) return;
    setError(null);
    setState((m) => {
      const copy = new Map(m);
      copy.set(q.position, { ...cur, staged: null });
      return copy;
    });
  }

  async function handleConfirmAnswer() {
    if (cur.confirmed || !cur.staged || submitting) return;
    setSubmitting(true);
    setError(null);

    const delta = (Date.now() - enteredAt.current) / 1000;
    enteredAt.current = Date.now();

    try {
      const res = await saveAnswer({
        sessionId,
        position: q.position,
        label: cur.staged,
        flagged: cur.flagged,
        secondsDelta: delta,
      });

      if ("error" in res && res.error) {
        setError(res.error);
        setSubmitting(false);
        return;
      }

      if ("ok" in res && res.ok) {
        setState((m) => {
          const copy = new Map(m);
          copy.set(q.position, {
            ...cur,
            chosen: cur.staged,
            confirmed: true,
            isCorrect: res.isCorrect,
            correctLabel: res.correctLabel,
            explanation: res.explanation,
          });
          return copy;
        });
      }
    } catch {
      setError("Erro ao salvar resposta. Tente novamente.");
    } finally {
      setSubmitting(false);
    }
  }

  function toggleFlag() {
    const flagged = !cur.flagged;
    setState((m) => new Map(m).set(q.position, { ...cur, flagged }));
    if (cur.confirmed) {
      const delta = (Date.now() - enteredAt.current) / 1000;
      enteredAt.current = Date.now();
      saveAnswer({ sessionId, position: q.position, label: cur.chosen, flagged, secondsDelta: delta });
    }
  }

  function go(i: number) {
    if (i < 0 || i >= questions.length || i === idx) return;
    setIdx(i);
    setError(null);
    enteredAt.current = Date.now();
  }

  // Atalhos de teclado
  const keys = useRef<(e: KeyboardEvent) => void>(() => {});
  useEffect(() => {
    keys.current = (e) => {
      if (confirming || e.metaKey || e.ctrlKey || e.altKey) return;
      const t = e.target as HTMLElement | null;
      if (t && (t.tagName === "TEXTAREA" || t.tagName === "INPUT")) return;
      const k = e.key.toUpperCase();
      const opt = q.options.find((o) => o.label === k);
      if (opt && !cur.confirmed) {
        selectOption(opt.label);
      } else if (e.key === "Enter" && cur.staged && !cur.confirmed) {
        e.preventDefault();
        handleConfirmAnswer();
      } else if (e.key === "ArrowRight") {
        go(idx + 1);
      } else if (e.key === "ArrowLeft") {
        go(idx - 1);
      } else if (k === "F") {
        toggleFlag();
      }
    };
  });

  useEffect(() => {
    const h = (e: KeyboardEvent) => keys.current(e);
    window.addEventListener("keydown", h);
    return () => window.removeEventListener("keydown", h);
  }, []);

  const low = remaining <= 300;
  const timeLeft = limitSeconds ? remaining / limitSeconds : 0;

  return (
    <div className="mx-auto max-w-5xl space-y-5">
      <div className="sticky top-[3.6rem] z-20 -mx-4 border-b border-border bg-bg/90 px-4 py-2.5 backdrop-blur lg:top-0 lg:-mx-10 lg:px-10">
        <div className="flex items-center justify-between gap-3">
          <p className="text-sm font-semibold text-muted tabular">
            <span className="font-display text-xl text-text">{answered}</span>/{questions.length} respondidas
          </p>
          <p
            className={cx("flex items-center gap-2 font-display text-3xl font-bold leading-none tabular", low && "text-primary", low && remaining > 0 && "blink")}
            role="timer"
            aria-label="Tempo restante"
          >
            <Timer className="h-5 w-5" aria-hidden />
            {fmtClock(remaining * 1000)}
          </p>
          <Button variant="secondary" size="sm" onClick={() => setConfirming(true)} disabled={pending}>
            Finalizar
          </Button>
        </div>
        <div className="mt-2 h-1 overflow-hidden rounded-full bg-surface-3" aria-hidden>
          <div
            className="h-full rounded-full transition-[width] duration-1000 ease-linear"
            style={{ width: `${timeLeft * 100}%`, background: low ? "var(--primary)" : "var(--gold)" }}
          />
        </div>
      </div>

      {confirming && (
        <Card className="page-in space-y-3 border-primary">
          <p className="font-display text-2xl font-bold uppercase tracking-wide">Finalizar o caderno?</p>
          <p className="text-sm text-muted">
            {blanks > 0 ? `Você deixou ${blanks} questão(ões) em branco. Elas contarão como erro.` : "Todas as questões foram respondidas."} Depois de finalizar, não é possível alterar as respostas.
          </p>
          <div className="flex flex-wrap gap-2">
            <Button onClick={() => finish(false)} disabled={pending}>
              {pending && <Loader2 className="h-4 w-4 animate-spin" aria-hidden />}
              {pending ? "Corrigindo…" : "Sim, finalizar"}
            </Button>
            <Button variant="ghost" onClick={() => setConfirming(false)} disabled={pending}>
              Continuar respondendo
            </Button>
          </div>
        </Card>
      )}

      <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_16rem]">
        <Card key={q.position} className="swap-in space-y-5 sm:p-7">
          <div className="flex items-center justify-between gap-3">
            <div>
              <p className="eyebrow">Questão</p>
              <p className="font-display text-4xl font-bold leading-none tabular">
                {idx + 1}
                <span className="text-xl text-muted"> / {questions.length}</span>
              </p>
            </div>
            <div className="flex items-center gap-2">
              {cur.confirmed && (
                <Badge tone={cur.isCorrect ? "ok" : "warn"}>
                  {cur.isCorrect ? "Correta" : "Incorreta"}
                </Badge>
              )}
              <button
                type="button"
                onClick={toggleFlag}
                aria-pressed={cur.flagged}
                className={cx(
                  "inline-flex cursor-pointer items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-sm font-semibold transition active:scale-95",
                  cur.flagged ? "border-warn bg-warn-soft text-warn" : "border-border text-muted hover:border-border-strong hover:text-text",
                )}
              >
                <Flag className={cx("h-4 w-4", cur.flagged && "fill-current")} aria-hidden />
                {cur.flagged ? "Marcada" : "Marcar para revisar"}
              </button>
            </div>
          </div>

          {q.support && (
            <div className="whitespace-pre-line rounded-xl border-l-4 border-border-strong bg-surface-2 p-4 text-sm leading-relaxed text-text/90">
              {q.support}
            </div>
          )}

          <div className="whitespace-pre-line text-[16px] leading-relaxed text-text font-normal">
            {q.statement}
          </div>

          <div className="space-y-2.5" role="radiogroup" aria-label={`Alternativas da questão ${idx + 1}`}>
            {q.options.map((o) => {
              const isStaged = cur.staged === o.label;
              const isChosen = cur.chosen === o.label;
              const isCorrectOpt = cur.correctLabel === o.label;

              let cardStyle = "border-border bg-surface hover:-translate-y-px hover:border-border-strong hover:bg-surface-2";
              let badgeStyle = "border-border-strong bg-surface-2 text-muted group-hover:text-text";

              if (!cur.confirmed) {
                if (isStaged) {
                  cardStyle = "border-primary bg-primary-soft shadow-[0_8px_20px_-12px_var(--primary)] ring-2 ring-primary/40";
                  badgeStyle = "border-primary bg-primary text-on-primary";
                }
              } else {
                if (isCorrectOpt) {
                  cardStyle = "border-ok bg-ok/10 text-text ring-1 ring-ok/50 shadow-xs";
                  badgeStyle = "border-ok bg-ok text-white font-bold";
                } else if (isChosen && !cur.isCorrect) {
                  cardStyle = "border-primary bg-danger-soft text-text ring-1 ring-primary/50";
                  badgeStyle = "border-primary bg-primary text-on-primary font-bold";
                } else {
                  cardStyle = "border-border/60 bg-surface/60 opacity-60";
                  badgeStyle = "border-border bg-surface-2 text-muted";
                }
              }

              return (
                <button
                  key={o.label}
                  type="button"
                  role="radio"
                  aria-checked={cur.confirmed ? isChosen : isStaged}
                  disabled={cur.confirmed}
                  onClick={() => selectOption(o.label)}
                  className={cx(
                    "group flex w-full items-start gap-3.5 rounded-xl border-2 p-3.5 text-left text-[15px] leading-relaxed transition duration-200",
                    !cur.confirmed ? "cursor-pointer active:scale-[0.995]" : "cursor-default",
                    cardStyle,
                  )}
                >
                  <span className={cx("mt-px flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border font-display text-lg font-bold transition", badgeStyle)}>
                    {o.label}
                  </span>
                  <span className="pt-1 flex-1">{o.text}</span>
                  {cur.confirmed && isCorrectOpt && (
                    <CircleCheck className="mt-1 h-5 w-5 shrink-0 text-ok" aria-label="Alternativa correta" />
                  )}
                  {cur.confirmed && isChosen && !cur.isCorrect && (
                    <CircleX className="mt-1 h-5 w-5 shrink-0 text-primary" aria-label="Sua resposta incorreta" />
                  )}
                </button>
              );
            })}
          </div>

          {/* Área de Resposta e Feedback */}
          {!cur.confirmed ? (
            <div className="flex flex-wrap items-center gap-3 pt-2">
              <Button
                variant="primary"
                onClick={handleConfirmAnswer}
                disabled={!cur.staged || submitting}
                className="min-w-[8rem] text-sm font-bold shadow-md"
              >
                {submitting ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" aria-hidden />
                    Enviando…
                  </>
                ) : (
                  "Responder"
                )}
              </Button>
              {cur.staged && !submitting && (
                <button
                  type="button"
                  onClick={clearStaged}
                  className="cursor-pointer text-xs font-semibold text-muted underline-offset-2 hover:text-text hover:underline"
                >
                  Limpar seleção
                </button>
              )}
            </div>
          ) : (
            <div className="space-y-4 pt-2">
              {/* Feedback do resultado */}
              {cur.isCorrect ? (
                <div className="flex items-center gap-3 rounded-xl border border-ok/40 bg-ok/10 p-4 text-ok">
                  <CheckCircle2 className="h-5 w-5 shrink-0" />
                  <div>
                    <p className="font-display font-bold text-base">Resposta correta!</p>
                    <p className="text-xs text-text/80">Parabéns, você acertou a questão.</p>
                  </div>
                </div>
              ) : (
                <div className="flex items-center gap-3 rounded-xl border border-primary/40 bg-danger-soft p-4 text-primary">
                  <XCircle className="h-5 w-5 shrink-0" />
                  <div>
                    <p className="font-display font-bold text-base">Resposta incorreta</p>
                    <p className="text-xs text-text/90">
                      A alternativa correta é a <strong className="text-ok font-bold underline">Alternativa {cur.correctLabel}</strong>.
                    </p>
                  </div>
                </div>
              )}

              {/* Comentário explicativo com renderização em Markdown */}
              {cur.explanation && (
                <div className="space-y-2 rounded-2xl border border-border bg-surface-2 p-5 shadow-xs">
                  <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-muted">
                    <Sparkles className="h-4 w-4 text-gold" />
                    <span>Comentário do Professor</span>
                  </div>
                  <div className="pt-1 border-t border-border/60">
                    {renderMarkdownExplanation(cur.explanation)}
                  </div>
                </div>
              )}
            </div>
          )}

          {error && <Alert tone="danger">{error}</Alert>}

          <div className="flex items-center justify-between gap-3 border-t border-border pt-4">
            <Button variant="secondary" onClick={() => go(idx - 1)} disabled={idx === 0}>
              <ArrowLeft className="h-4 w-4" aria-hidden />
              Anterior
            </Button>
            <p className="hidden items-center gap-1.5 text-xs text-muted md:flex">
              <Kbd>A</Kbd>–<Kbd>E</Kbd> selecionar <Kbd>Enter</Kbd> responder <Kbd>←</Kbd><Kbd>→</Kbd> navegar <Kbd>F</Kbd> marcar
            </p>
            <Button onClick={() => go(idx + 1)} disabled={idx === questions.length - 1}>
              Próxima
              <ArrowRight className="h-4 w-4" aria-hidden />
            </Button>
          </div>
        </Card>

        <nav aria-label="Navegador de questões" className="lg:sticky lg:top-24 lg:self-start">
          <Card className="space-y-3 p-4">
            <p className="eyebrow">Navegador</p>
            <div className="grid grid-cols-5 gap-1.5 sm:grid-cols-10 lg:grid-cols-5">
              {questions.map((qq, i) => {
                const s = state.get(qq.position)!;
                let navBg = "border-border bg-surface text-muted hover:text-text";
                if (s.confirmed) {
                  if (s.isCorrect === true) {
                    navBg = "border-ok bg-ok text-white font-bold";
                  } else if (s.isCorrect === false) {
                    navBg = "border-primary bg-primary text-on-primary font-bold";
                  } else {
                    navBg = "border-primary bg-primary text-on-primary";
                  }
                } else if (s.staged) {
                  navBg = "border-primary/60 bg-primary/20 text-text font-bold";
                }

                return (
                  <button
                    key={qq.position}
                    type="button"
                    onClick={() => go(i)}
                    aria-label={`Questão ${i + 1}${s.confirmed ? ", respondida" : s.staged ? ", selecionada" : ""}${s.flagged ? ", marcada" : ""}`}
                    aria-current={i === idx}
                    className={cx(
                      "relative cursor-pointer rounded-lg border py-1.5 font-display text-base font-bold tabular transition duration-150 hover:-translate-y-px",
                      navBg,
                      i === idx && "ring-2 ring-gold ring-offset-2 ring-offset-surface",
                    )}
                  >
                    {i + 1}
                    {s.flagged && <Flag className="absolute -right-1 -top-1.5 h-3 w-3 fill-warn text-warn" aria-hidden />}
                  </button>
                );
              })}
            </div>
            <p className="flex flex-wrap gap-x-3 gap-y-1 text-[11px] text-muted">
              <span className="inline-flex items-center gap-1">
                <span className="h-2.5 w-2.5 rounded bg-ok" />
                acerto
              </span>
              <span className="inline-flex items-center gap-1">
                <span className="h-2.5 w-2.5 rounded bg-primary" />
                erro
              </span>
              <span className="inline-flex items-center gap-1">
                <Flag className="h-3 w-3 fill-warn text-warn" />
                marcada
              </span>
            </p>
          </Card>
        </nav>
      </div>
    </div>
  );
}
