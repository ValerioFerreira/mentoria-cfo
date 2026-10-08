"use client";

import { Check, CircleCheck, Clock3, Loader2, SkipForward, Trash2, Undo2 } from "lucide-react";
import { useRouter } from "next/navigation";
import { useEffect, useOptimistic, useRef, useState, useTransition } from "react";
import { Alert, Button, Card, InfoTip, cx, inputCls } from "@/components/ui";
import { fmtDuration } from "@/lib/ui-format";
import { deleteTimeLog, logManualTime, saveNote, setActivityStatus } from "@/lib/study/actions";

export { TypeBadge } from "@/components/ui";

/** Marcador redondo de conclusão. Atualiza na hora (otimista) e confirma no servidor. */
export function StatusToggle({ id, status, compact }: { id: string; status: string; compact?: boolean }) {
  const [, start] = useTransition();
  const router = useRouter();
  const done = status === "DONE";
  const [shownDone, setShownDone] = useOptimistic(done);
  return (
    <button
      type="button"
      aria-pressed={shownDone}
      aria-label={shownDone ? "Marcar como não concluída" : "Marcar como concluída"}
      onClick={(e) => {
        e.preventDefault();
        e.stopPropagation();
        start(async () => {
          setShownDone(!done);
          await setActivityStatus(id, done ? "PENDING" : "DONE");
          router.refresh();
        });
      }}
      className={cx(
        "group/check flex shrink-0 cursor-pointer items-center justify-center rounded-full border-2 transition duration-200 active:scale-90",
        compact ? "h-7 w-7" : "h-9 w-9",
        shownDone ? "border-ok bg-ok text-white shadow-[0_6px_14px_-6px_var(--ok)]" : "border-border-strong bg-surface hover:border-ok hover:bg-ok/10",
      )}
    >
      {shownDone ? <Check key="on" className="pop h-4 w-4" strokeWidth={3} aria-hidden /> : <Check className="h-4 w-4 text-ok opacity-0 transition group-hover/check:opacity-60" strokeWidth={3} aria-hidden />}
    </button>
  );
}

export function ActivityActions({ id, status }: { id: string; status: string }) {
  const [pending, start] = useTransition();
  const router = useRouter();
  const done = status === "DONE";
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Button
        disabled={pending}
        variant={done ? "secondary" : "primary"}
        onClick={() =>
          start(async () => {
            await setActivityStatus(id, done ? "PENDING" : "DONE");
            router.refresh();
          })
        }
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
