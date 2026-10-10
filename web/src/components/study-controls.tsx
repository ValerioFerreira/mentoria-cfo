"use client";

import { Check, CircleCheck, Clock3, Loader2, SkipForward, Trash2, Undo2 } from "lucide-react";
import { useRouter } from "next/navigation";
import { useEffect, useOptimistic, useRef, useState, useTransition } from "react";
import { Alert, Button, Card, InfoTip, cx, inputCls } from "@/components/ui";
import { fmtDuration } from "@/lib/ui-format";
import { completeActivityWithTime, deleteTimeLog, logManualTime, saveNote, setActivityStatus } from "@/lib/study/actions";

export { TypeBadge } from "@/components/ui";

/** Modal obrigatório de tempo ao concluir a atividade */
export function CompleteModal({
  id,
  open,
  onClose,
}: {
  id: string;
  open: boolean;
  onClose: () => void;
}) {
  const [hours, setHours] = useState("");
  const [minutes, setMinutes] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();
  const router = useRouter();

  if (!open) return null;

  const h = hours === "" ? 0 : Number(hours);
  const m = minutes === "" ? 0 : Number(minutes);
  const total = h * 60 + m;

  const setPreset = (hVal: number, mVal: number) => {
    setHours(hVal > 0 ? String(hVal) : "");
    setMinutes(String(mVal));
    setError(null);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (total < 1) {
      setError("Quanto tempo você dedicou a esta atividade? O registro de tempo é obrigatório para concluir (mínimo de 1 minuto).");
      return;
    }
    setError(null);
    start(async () => {
      const res = await completeActivityWithTime(id, h, m);
      if (res.error) {
        setError(res.error);
      } else {
        onClose();
        router.refresh();
      }
    });
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-xs animate-in fade-in"
      onClick={onClose}
    >
      <div
        className="w-full max-w-md rounded-2xl border border-border bg-surface p-6 shadow-lift text-text space-y-4"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby="complete-modal-title"
      >
        <div className="space-y-1">
          <h2 id="complete-modal-title" className="font-display text-2xl font-bold uppercase tracking-wide">
            Concluir Atividade
          </h2>
          <p className="text-sm text-muted">
            Quanto tempo você dedicou a esta atividade? Informe o tempo real de estudo para confirmar a conclusão.
          </p>
        </div>

        {/* Atalhos rápidos */}
        <div className="space-y-1.5">
          <span className="text-xs font-semibold text-muted">Sugestões rápidas:</span>
          <div className="flex flex-wrap gap-2">
            {[
              { label: "30 min", h: 0, m: 30 },
              { label: "45 min", h: 0, m: 45 },
              { label: "1h", h: 1, m: 0 },
              { label: "1h 15m", h: 1, m: 15 },
              { label: "1h 30m", h: 1, m: 30 },
            ].map((preset) => (
              <button
                key={preset.label}
                type="button"
                onClick={() => setPreset(preset.h, preset.m)}
                className="rounded-lg border border-border bg-surface-2 px-2.5 py-1 text-xs font-medium text-text transition hover:border-primary hover:bg-surface-3 cursor-pointer"
              >
                {preset.label}
              </button>
            ))}
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 pt-1">
          <div className="flex items-center gap-3">
            <label className="flex-1">
              <span className="mb-1 block text-xs font-semibold text-muted">Horas (0–16)</span>
              <input
                type="number"
                min={0}
                max={16}
                inputMode="numeric"
                placeholder="0"
                value={hours}
                onChange={(e) => {
                  setHours(e.target.value);
                  setError(null);
                }}
                className={cx(inputCls, "text-center text-base font-semibold")}
                autoFocus
              />
            </label>
            <label className="flex-1">
              <span className="mb-1 block text-xs font-semibold text-muted">Minutos (0–59)</span>
              <input
                type="number"
                min={0}
                max={59}
                inputMode="numeric"
                placeholder="0"
                value={minutes}
                onChange={(e) => {
                  setMinutes(e.target.value);
                  setError(null);
                }}
                className={cx(inputCls, "text-center text-base font-semibold")}
              />
            </label>
          </div>

          {error && <Alert tone="danger">{error}</Alert>}

          <div className="flex items-center justify-end gap-2.5 pt-2">
            <Button type="button" variant="secondary" onClick={onClose} disabled={pending}>
              Cancelar
            </Button>
            <Button type="submit" variant="primary" disabled={pending}>
              {pending ? (
                <>
                  <Loader2 className="h-4 w-4 animate-spin" aria-hidden />
                  Salvando…
                </>
              ) : (
                <>
                  <CircleCheck className="h-4 w-4" aria-hidden />
                  Concluir com {total > 0 ? fmtDuration(total * 60) : "tempo"}
                </>
              )}
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
}

/** Marcador redondo de conclusão. Atualiza na hora (otimista) ou abre modal de tempo se for para concluir. */
export function StatusToggle({ id, status, compact }: { id: string; status: string; compact?: boolean }) {
  const [, start] = useTransition();
  const router = useRouter();
  const done = status === "DONE";
  const [shownDone, setShownDone] = useOptimistic(done);
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <>
      <button
        type="button"
        aria-pressed={shownDone}
        aria-label={shownDone ? "Reabrir atividade" : "Concluir atividade"}
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          if (done) {
            // Reabrir atividade
            start(async () => {
              setShownDone(false);
              await setActivityStatus(id, "PENDING");
              router.refresh();
            });
          } else {
            // Exige tempo para concluir
            setModalOpen(true);
          }
        }}
        className={cx(
          "group/check flex shrink-0 cursor-pointer items-center justify-center rounded-full border-2 transition duration-200 active:scale-90",
          compact ? "h-7 w-7" : "h-9 w-9",
          shownDone ? "border-ok bg-ok text-white shadow-[0_6px_14px_-6px_var(--ok)]" : "border-border-strong bg-surface hover:border-ok hover:bg-ok/10",
        )}
      >
        {shownDone ? <Check key="on" className="pop h-4 w-4" strokeWidth={3} aria-hidden /> : <Check className="h-4 w-4 text-ok opacity-0 transition group-hover/check:opacity-60" strokeWidth={3} aria-hidden />}
      </button>
      <CompleteModal id={id} open={modalOpen} onClose={() => setModalOpen(false)} />
    </>
  );
}

export function ActivityActions({ id, status }: { id: string; status: string }) {
  const [pending, start] = useTransition();
  const router = useRouter();
  const done = status === "DONE";
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <>
      <div className="flex flex-wrap items-center gap-2">
        <Button
          disabled={pending}
          variant={done ? "secondary" : "primary"}
          onClick={() => {
            if (done) {
              start(async () => {
                await setActivityStatus(id, "PENDING");
                router.refresh();
              });
            } else {
              setModalOpen(true);
            }
          }}
        >
          {done ? <Undo2 className="h-4 w-4" aria-hidden /> : <CircleCheck className="h-4 w-4" aria-hidden />}
          {done ? "Reabrir atividade" : "Concluir atividade"}
        </Button>
        {!done && status !== "SKIPPED" && (
          <Button
            variant="ghost"
            disabled={pending}
            onClick={() =>
              start(async () => {
                await setActivityStatus(id, "SKIPPED");
                router.refresh();
              })
            }
          >
            <SkipForward className="h-4 w-4" aria-hidden />
            Pular
          </Button>
        )}
      </div>
      <CompleteModal id={id} open={modalOpen} onClose={() => setModalOpen(false)} />
    </>
  );
}

/** Campos de tempo: total de horas e total de minutos. */
function TimeFields({ id, onDone, compact }: { id: string; onDone?: () => void; compact?: boolean }) {
  const [hours, setHours] = useState("");
  const [minutes, setMinutes] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();
  const router = useRouter();
  const h = hours === "" ? 0 : Number(hours);
  const m = minutes === "" ? 0 : Number(minutes);
  const total = h * 60 + m;
  return (
    <form
      className="space-y-2"
      onSubmit={(e) => {
        e.preventDefault();
        start(async () => {
          const r = await logManualTime(id, h, m);
          if (r.error) setError(r.error);
          else {
            setError(null);
            setHours("");
            setMinutes("");
            router.refresh();
            onDone?.();
          }
        });
      }}
    >
      <div className="flex flex-wrap items-end gap-2">
        <label className="block">
          <span className="mb-1 block text-xs font-semibold text-muted">Horas</span>
          <input type="number" min={0} max={16} inputMode="numeric" placeholder="0" value={hours} onChange={(e) => setHours(e.target.value)} className={cx(inputCls, "w-20 text-center")} />
        </label>
        <label className="block">
          <span className="mb-1 block text-xs font-semibold text-muted">Minutos</span>
          <input type="number" min={0} max={59} inputMode="numeric" placeholder="0" value={minutes} onChange={(e) => setMinutes(e.target.value)} className={cx(inputCls, "w-20 text-center")} />
        </label>
        <Button type="submit" variant={compact ? "primary" : "secondary"} disabled={pending || total < 1}>
          {pending && <Loader2 className="h-4 w-4 animate-spin" aria-hidden />}
          Lançar {total >= 1 ? fmtDuration(total * 60) : "tempo"}
        </Button>
      </div>
      {error && <Alert tone="danger">{error}</Alert>}
    </form>
  );
}

/** Botão compacto "Tempo" para lançar o estudo direto de um cartão (Missão de hoje, Meta semanal). */
export function QuickTime({ id, seconds }: { id: string; seconds: number }) {
  const [open, setOpen] = useState(false);
  const box = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!open) return;
    const away = (e: MouseEvent) => !box.current?.contains(e.target as Node) && setOpen(false);
    const esc = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("mousedown", away);
    document.addEventListener("keydown", esc);
    return () => {
      document.removeEventListener("mousedown", away);
      document.removeEventListener("keydown", esc);
    };
  }, [open]);
  return (
    <div ref={box} className="relative">
      <button
        type="button"
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          setOpen((v) => !v);
        }}
        aria-expanded={open}
        aria-label="Lançar tempo estudado"
        className={cx("inline-flex cursor-pointer items-center gap-1.5 rounded-lg border px-2.5 py-1.5 text-xs font-semibold transition active:scale-95", seconds > 0 ? "border-ok/40 bg-ok/10 text-ok" : "border-border text-muted hover:border-border-strong hover:text-text")}
      >
        <Clock3 className="h-3.5 w-3.5" aria-hidden />
        {seconds > 0 ? fmtDuration(seconds) : "Tempo"}
      </button>
      {open && (
        <div className="pop absolute right-0 top-full z-40 mt-2 w-72 origin-top-right rounded-2xl border border-border bg-surface p-4 text-text shadow-lift" onClick={(e) => e.stopPropagation()}>
          <p className="mb-2 font-display text-lg font-bold uppercase tracking-wide">Tempo gasto</p>
          <TimeFields id={id} onDone={() => setOpen(false)} compact />
        </div>
      )}
    </div>
  );
}

export function ManualTime({ id, logs }: { id: string; logs: { id: string; seconds: number; source: string; startedAt: string }[] }) {
  const [, start] = useTransition();
  const router = useRouter();
  const total = logs.reduce((n, l) => n + l.seconds, 0);
  return (
    <Card className="space-y-4">
      <div className="flex items-center justify-between gap-3">
        <h2 className="flex items-center gap-2 font-display text-xl font-bold uppercase tracking-wide">
          <Clock3 className="h-5 w-5 text-muted" aria-hidden />
          Tempo gasto
          <InfoTip align="start">Ao terminar a atividade, informe quantas horas e minutos você estudou. O cronômetro flutuante é livre: ele não grava nada sozinho.</InfoTip>
        </h2>
        <span className="font-display text-3xl font-bold leading-none tabular">{fmtDuration(total)}</span>
      </div>
      <TimeFields id={id} />
      {logs.length > 0 && (
        <ul className="divide-y divide-border text-sm">
          {logs.map((l) => (
            <li key={l.id} className="flex items-center justify-between py-2">
              <span className="text-muted">{new Date(l.startedAt).toLocaleString("pt-BR", { day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit" })}</span>
              <span className="flex items-center gap-3">
                <span className="font-semibold tabular">{fmtDuration(l.seconds)}</span>
                <button
                  type="button"
                  aria-label="Remover registro"
                  title="Remover registro"
                  className="cursor-pointer rounded-md p-1 text-muted transition hover:bg-danger-soft hover:text-primary"
                  onClick={() => start(async () => { await deleteTimeLog(l.id); router.refresh(); })}
                >
                  <Trash2 className="h-4 w-4" aria-hidden />
                </button>
              </span>
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}

export function NotesEditor({ segmentId, label, initial }: { segmentId: string; label: string; initial: string }) {
  const [text, setText] = useState(initial);
  const [state, setState] = useState<"idle" | "saving" | "saved">("idle");
  const lastSaved = useRef(initial);
  useEffect(() => {
    if (text === lastSaved.current) return;
    setState("saving");
    const t = setTimeout(async () => {
      await saveNote(segmentId, text);
      lastSaved.current = text;
      setState("saved");
    }, 700);
    return () => clearTimeout(t);
  }, [text, segmentId]);
  return (
    <div className="space-y-1.5">
      <div className="flex items-center justify-between">
        <label htmlFor={`note-${segmentId}`} className="text-sm font-semibold">{label}</label>
        <span className="flex items-center gap-1 text-xs text-muted" aria-live="polite">
          {state === "saving" && <><Loader2 className="h-3 w-3 animate-spin" aria-hidden />Salvando…</>}
          {state === "saved" && <><Check className="pop h-3 w-3 text-ok" aria-hidden /><span className="text-ok">Salvo</span></>}
        </span>
      </div>
      <textarea id={`note-${segmentId}`} value={text} onChange={(e) => setText(e.target.value)} rows={5} placeholder="Escreva aqui, com as suas palavras, os conceitos principais deste trecho. Você vai reler isto na Revisão." className={cx(inputCls, "resize-y leading-relaxed")} />
    </div>
  );
}
