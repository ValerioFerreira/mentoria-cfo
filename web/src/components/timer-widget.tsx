"use client";

import { GripVertical, Pause, Play } from "lucide-react";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState, useSyncExternalStore } from "react";
import { Button, cx } from "@/components/ui";
import { fmtClock } from "@/lib/ui-format";

/**
 * Cronômetro livre (balão flutuante). Não está ligado a nenhuma atividade e o sistema NÃO grava seus tempos:
 * quem quiser registrar o estudo lança as horas e os minutos ao final de cada atividade.
 * O estado fica no navegador (sobrevive a recarregar a página) e o balão pode ser arrastado para qualquer lugar.
 */
type Status = "idle" | "running" | "paused";
interface TimerState {
  status: Status;
  /** instante em que o trecho atual começou (running) */
  startedAt: number | null;
  /** tempo acumulado em trechos anteriores */
  accumulated: number;
  /** instante em que a pausa começou (paused) */
  pausedAt: number | null;
  pos: { x: number; y: number } | null;
}
const KEY = "mentoria:cronometro:v1";
const EVENT = "mentoria:cronometro";
const INITIAL: TimerState = { status: "idle", startedAt: null, accumulated: 0, pausedAt: null, pos: null };
const nowMs = () => Date.now(); // fora do render para satisfazer a regra de pureza do React

function parse(raw: string | null): TimerState {
  if (!raw) return INITIAL;
  try {
    const s = JSON.parse(raw) as Partial<TimerState>;
    if (s.status !== "idle" && s.status !== "running" && s.status !== "paused") return INITIAL;
    return { ...INITIAL, ...s } as TimerState;
  } catch {
    return INITIAL;
  }
}

// o navegador é a "fonte da verdade": useSyncExternalStore evita piscar e mantém abas sincronizadas
let lastRaw: string | null | undefined;
let lastState: TimerState = INITIAL;
function snapshot(): TimerState {
  let raw: string | null = null;
  try {
    raw = window.localStorage.getItem(KEY);
  } catch {}
  if (raw !== lastRaw) {
    lastRaw = raw;
    lastState = parse(raw);
  }
  return lastState;
}
function subscribe(cb: () => void) {
  window.addEventListener(EVENT, cb);
  window.addEventListener("storage", cb);
  return () => {
    window.removeEventListener(EVENT, cb);
    window.removeEventListener("storage", cb);
  };
}
function write(next: TimerState) {
  try {
    window.localStorage.setItem(KEY, JSON.stringify(next));
  } catch {}
  window.dispatchEvent(new Event(EVENT));
}

export function TimerWidget() {
  const pathname = usePathname();
  const s = useSyncExternalStore(subscribe, snapshot, () => null);
  const [now, setNow] = useState(nowMs);
  const [confirming, setConfirming] = useState(false);
  const [dragPos, setDragPos] = useState<{ x: number; y: number } | null>(null);
  const box = useRef<HTMLDivElement>(null);
  const drag = useRef<{ dx: number; dy: number } | null>(null);

  const active = s?.status === "running" || s?.status === "paused";
  useEffect(() => {
    if (!active) return;
    const id = setInterval(() => setNow(nowMs()), 250);
    return () => clearInterval(id);
  }, [active]);

  // mantém o balão dentro da tela quando a janela muda de tamanho
  useEffect(() => {
    const onResize = () => {
      const el = box.current;
      const cur = snapshot();
      if (!el || !cur.pos) return;
      const r = el.getBoundingClientRect();
      const x = Math.min(Math.max(0, cur.pos.x), Math.max(0, window.innerWidth - r.width));
      const y = Math.min(Math.max(0, cur.pos.y), Math.max(0, window.innerHeight - r.height));
      if (x !== cur.pos.x || y !== cur.pos.y) write({ ...cur, pos: { x, y } });
    };
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);

  // o caderno de questões tem cronômetro regressivo próprio
  // O cronômetro só surge quando o usuário estiver em uma página de atividade (/atividade/[id])
  if (!s || !pathname.startsWith("/atividade/")) return null;

  const t = Math.max(now, s.startedAt ?? 0, s.pausedAt ?? 0);
  const elapsed = s.accumulated + (s.status === "running" && s.startedAt ? Math.max(0, t - s.startedAt) : 0);
  const pauseMs = s.status === "paused" && s.pausedAt ? Math.max(0, t - s.pausedAt) : 0;
  const running = s.status === "running";
  const paused = s.status === "paused";

  const start = () => write({ ...s, status: "running", startedAt: nowMs(), pausedAt: null });
  const pause = () => write({ ...s, status: "paused", accumulated: s.accumulated + (s.startedAt ? nowMs() - s.startedAt : 0), startedAt: null, pausedAt: nowMs() });
  const reset = () => {
    write({ ...INITIAL, pos: s.pos });
    setConfirming(false);
  };

  // arrastar: só pelo corpo do balão (os botões continuam clicáveis)
  const onPointerDown = (e: React.PointerEvent<HTMLDivElement>) => {
    if ((e.target as HTMLElement).closest("button")) return;
    const el = box.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    drag.current = { dx: e.clientX - r.left, dy: e.clientY - r.top };
    setDragPos({ x: r.left, y: r.top });
    el.setPointerCapture(e.pointerId);
  };
  const onPointerMove = (e: React.PointerEvent<HTMLDivElement>) => {
    const d = drag.current;
    const el = box.current;
    if (!d || !el) return;
    const r = el.getBoundingClientRect();
    setDragPos({
      x: Math.min(Math.max(0, e.clientX - d.dx), Math.max(0, window.innerWidth - r.width)),
      y: Math.min(Math.max(0, e.clientY - d.dy), Math.max(0, window.innerHeight - r.height)),
    });
  };
  const onPointerUp = (e: React.PointerEvent<HTMLDivElement>) => {
    if (!drag.current) return;
    drag.current = null;
    box.current?.releasePointerCapture(e.pointerId);
    if (dragPos) write({ ...s, pos: dragPos });
    setDragPos(null);
  };

  const pos = dragPos ?? s.pos;
  // a pausa abre ao lado do balão principal, para o lado que tem mais espaço
  const auxOnLeft = !!pos && pos.x > (typeof window !== "undefined" ? window.innerWidth / 2 : 0);

  return (
    <>
      <div
        ref={box}
        role="group"
        aria-label="Cronômetro de estudo"
        style={pos ? { left: pos.x, top: pos.y } : undefined}
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onPointerCancel={onPointerUp}
        className={cx("fixed z-50 flex touch-none select-none items-stretch gap-2", !pos && "bottom-24 left-4 lg:bottom-6 lg:left-72", auxOnLeft ? "flex-row-reverse" : "flex-row")}
      >
        <div className={cx("flex cursor-grab items-center gap-1.5 rounded-2xl border border-white/10 bg-ink py-2 pl-1.5 pr-2.5 text-on-ink shadow-lift active:cursor-grabbing", running && "pulse-ring")}>
          <GripVertical className="h-4 w-4 shrink-0 text-on-ink-muted" aria-hidden />
          <span className={cx("min-w-[4.6ch] font-display text-[1.9rem] font-bold leading-none tabular", paused && "text-on-ink/80")} role="timer" aria-live="off">
            {fmtClock(elapsed)}
          </span>
          <div className="flex gap-1.5">
            {running ? (
              <Button variant="onInk" size="sm" onClick={pause}>
                <Pause className="h-3.5 w-3.5" aria-hidden />
                Pausar
              </Button>
            ) : (
              <Button size="sm" onClick={start}>
                <Play className="h-3.5 w-3.5 fill-current" aria-hidden />
                {paused ? "Retomar" : "Iniciar"}
              </Button>
            )}
            {(running || paused) && (
              <Button variant="onInk" size="sm" onClick={() => setConfirming(true)}>
                Zerar
              </Button>
            )}
          </div>
        </div>

        {paused && (
          <div className="pop flex flex-col justify-center rounded-2xl border border-white/10 bg-ink-2 px-3.5 py-2 text-on-ink shadow-lift" aria-live="off">
            <span className="eyebrow !text-on-ink-muted">Tempo de pausa</span>
            <span className="font-display text-2xl font-bold leading-none tabular text-gold">{fmtClock(pauseMs)}</span>
          </div>
        )}
      </div>

      {confirming && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center bg-black/50 px-4 backdrop-blur-sm" role="dialog" aria-modal="true" aria-labelledby="zerar-titulo">
          <div className="pop w-full max-w-sm space-y-4 rounded-2xl border border-border bg-surface p-6 text-text shadow-lift">
            <h2 id="zerar-titulo" className="font-display text-2xl font-bold uppercase tracking-wide">Zerar o cronômetro?</h2>
            <p className="text-sm text-muted">Todo o tempo será reiniciado e o cronômetro irá zerar. Essa ação não pode ser desfeita.</p>
            <div className="flex justify-end gap-2">
              <Button variant="ghost" onClick={() => setConfirming(false)} autoFocus>Cancelar</Button>
              <Button variant="danger" onClick={reset}>Zerar</Button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
