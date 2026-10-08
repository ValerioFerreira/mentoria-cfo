"use client";

import { ArrowLeft, ArrowRight, Flag, Loader2, Timer } from "lucide-react";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
import { Alert, Button, Card, Kbd, cx } from "@/components/ui";
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
}

interface Props {
  sessionId: string;
  startedAtMs: number;
  limitSeconds: number;
  serverNowMs: number;
  questions: RunnerQuestion[];
}

export function QuizRunner({ sessionId, startedAtMs, limitSeconds, serverNowMs, questions }: Props) {
  const router = useRouter();
  const offset = useRef(0); // diferença entre o relógio do servidor e o do navegador (definida ao montar)
  const [idx, setIdx] = useState(0);
  const [state, setState] = useState(() => new Map(questions.map((q) => [q.position, { chosen: q.chosen, flagged: q.flagged }])));
  const [remaining, setRemaining] = useState(() => Math.max(0, limitSeconds - Math.floor((serverNowMs - startedAtMs) / 1000)));
  const [confirming, setConfirming] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();
  const enteredAt = useRef(0);
  const finished = useRef(false);

  const q = questions[idx];
  const cur = state.get(q.position)!;
  const answered = useMemo(() => [...state.values()].filter((s) => s.chosen).length, [state]);
  const blanks = questions.length - answered;

  const flush = useCallback(
    (position: number, chosen: string | null, flagged: boolean) => {
      const delta = (Date.now() - enteredAt.current) / 1000;
      enteredAt.current = Date.now();
      saveAnswer({ sessionId, position, label: chosen, flagged, secondsDelta: delta }).then((r) => {
        if ("error" in r && r.error) setError(r.error);
      });
    },
    [sessionId],
  );

  const finish = useCallback(
    (auto: boolean) => {
      if (finished.current) return;
      finished.current = true;
      const s = state.get(q.position)!;
      flush(q.position, s.chosen, s.flagged);
      start(async () => {
        await finishQuiz(sessionId, auto);
        router.refresh();
      });
    },
    [flush, q.position, router, sessionId, state],
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

  function choose(label: string | null) {
    setState((m) => new Map(m).set(q.position, { ...cur, chosen: label }));
    flush(q.position, label, cur.flagged);
  }
  function toggleFlag() {
    const flagged = !cur.flagged;
    setState((m) => new Map(m).set(q.position, { ...cur, flagged }));
    flush(q.position, cur.chosen, flagged);
  }
  function go(i: number) {
    if (i < 0 || i >= questions.length || i === idx) return;
    flush(q.position, cur.chosen, cur.flagged);
    setIdx(i);
    setError(null);
  }

  // atalhos: A–E marcam, ←/→ navegam, F marca para revisar
  const keys = useRef<(e: KeyboardEvent) => void>(() => {});
  useEffect(() => {
    keys.current = (e) => {
      if (confirming || e.metaKey || e.ctrlKey || e.altKey) return;
      const t = e.target as HTMLElement | null;
      if (t && (t.tagName === "TEXTAREA" || t.tagName === "INPUT")) return;
      const k = e.key.toUpperCase();
      const opt = q.options.find((o) => o.label === k);
      if (opt) choose(cur.chosen === opt.label ? null : opt.label);
      else if (e.key === "ArrowRight") go(idx + 1);
      else if (e.key === "ArrowLeft") go(idx - 1);
      else if (k === "F") toggleFlag();
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
          <p className="text-sm font-semibold text-muted tabular"><span className="font-display text-xl text-text">{answered}</span>/{questions.length} respondidas</p>
          <p className={cx("flex items-center gap-2 font-display text-3xl font-bold leading-none tabular", low && "text-primary", low && remaining > 0 && "blink")} role="timer" aria-label="Tempo restante">
            <Timer className="h-5 w-5" aria-hidden />
            {fmtClock(remaining * 1000)}
          </p>
          <Button variant="secondary" size="sm" onClick={() => setConfirming(true)} disabled={pending}>Finalizar</Button>
        </div>
        <div className="mt-2 h-1 overflow-hidden rounded-full bg-surface-3" aria-hidden>
          <div className="h-full rounded-full transition-[width] duration-1000 ease-linear" style={{ width: `${timeLeft * 100}%`, background: low ? "var(--primary)" : "var(--gold)" }} />
        </div>
      </div>

      {confirming && (
        <Card className="page-in space-y-3 border-primary">
          <p className="font-display text-2xl font-bold uppercase tracking-wide">Finalizar o caderno?</p>
          <p className="text-sm text-muted">{blanks > 0 ? `Você deixou ${blanks} questão(ões) em branco. Elas contarão como erro.` : "Todas as questões foram respondidas."} Depois de finalizar, não é possível alterar as respostas.</p>
          <div className="flex flex-wrap gap-2">
            <Button onClick={() => finish(false)} disabled={pending}>
              {pending && <Loader2 className="h-4 w-4 animate-spin" aria-hidden />}
              {pending ? "Corrigindo…" : "Sim, finalizar"}
            </Button>
            <Button variant="ghost" onClick={() => setConfirming(false)} disabled={pending}>Continuar respondendo</Button>
          </div>
        </Card>
      )}

      <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_16rem]">
        <Card key={q.position} className="swap-in space-y-5 sm:p-7">
          <div className="flex items-center justify-between gap-3">
            <div>
              <p className="eyebrow">Questão</p>
              <p className="font-display text-4xl font-bold leading-none tabular">{idx + 1}<span className="text-xl text-muted"> / {questions.length}</span></p>
            </div>
            <button
              type="button"
              onClick={toggleFlag}
              aria-pressed={cur.flagged}
              className={cx("inline-flex cursor-pointer items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-sm font-semibold transition active:scale-95", cur.flagged ? "border-warn bg-warn-soft text-warn" : "border-border text-muted hover:border-border-strong hover:text-text")}
            >
              <Flag className={cx("h-4 w-4", cur.flagged && "fill-current")} aria-hidden />
              {cur.flagged ? "Marcada para revisar" : "Marcar para revisar"}
            </button>
          </div>
          {q.support && <div className="whitespace-pre-line rounded-xl border-l-4 border-border-strong bg-surface-2 p-4 text-sm leading-relaxed">{q.support}</div>}
          <p className="whitespace-pre-line text-[17px] leading-relaxed">{q.statement}</p>
          <div className="space-y-2.5" role="radiogroup" aria-label={`Alternativas da questão ${idx + 1}`}>
            {q.options.map((o) => {
              const on = cur.chosen === o.label;
              return (
                <button
                  key={o.label}
                  type="button"
                  role="radio"
                  aria-checked={on}
                  onClick={() => choose(on ? null : o.label)}
                  className={cx(
                    "group flex w-full cursor-pointer items-start gap-3.5 rounded-xl border-2 p-3.5 text-left text-[15px] leading-relaxed transition duration-200 active:scale-[0.995]",
                    on ? "border-primary bg-primary-soft shadow-[0_8px_20px_-12px_var(--primary)]" : "border-border bg-surface hover:-translate-y-px hover:border-border-strong hover:bg-surface-2",
                  )}
                >
                  <span className={cx("mt-px flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border font-display text-lg font-bold transition", on ? "border-primary bg-primary text-on-primary" : "border-border-strong bg-surface-2 text-muted group-hover:text-text")}>{o.label}</span>
                  <span className="pt-1">{o.text}</span>
                </button>
              );
            })}
          </div>
          {cur.chosen && (
            <button type="button" onClick={() => choose(null)} className="cursor-pointer text-xs font-semibold text-muted underline-offset-2 hover:text-text hover:underline">Limpar resposta</button>
          )}
          {error && <Alert tone="danger">{error}</Alert>}
          <div className="flex items-center justify-between gap-3 border-t border-border pt-4">
            <Button variant="secondary" onClick={() => go(idx - 1)} disabled={idx === 0}>
              <ArrowLeft className="h-4 w-4" aria-hidden />
              Anterior
            </Button>
            <p className="hidden items-center gap-1.5 text-xs text-muted md:flex"><Kbd>A</Kbd>–<Kbd>E</Kbd> responder <Kbd>←</Kbd><Kbd>→</Kbd> navegar <Kbd>F</Kbd> marcar</p>
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
                return (
                  <button
                    key={qq.position}
                    type="button"
                    onClick={() => go(i)}
                    aria-label={`Questão ${i + 1}${s.chosen ? ", respondida" : ""}${s.flagged ? ", marcada" : ""}`}
                    aria-current={i === idx}
                    className={cx(
                      "relative cursor-pointer rounded-lg border py-1.5 font-display text-base font-bold tabular transition duration-150 hover:-translate-y-px",
                      s.chosen ? "border-primary bg-primary text-on-primary" : "border-border bg-surface text-muted hover:text-text",
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
              <span className="inline-flex items-center gap-1"><span className="h-2.5 w-2.5 rounded bg-primary" />respondida</span>
              <span className="inline-flex items-center gap-1"><Flag className="h-3 w-3 fill-warn text-warn" />marcada</span>
            </p>
          </Card>
        </nav>
      </div>
    </div>
  );
}
