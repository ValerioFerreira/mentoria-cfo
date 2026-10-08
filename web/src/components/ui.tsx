import Link from "next/link";
import { BookOpen, ClipboardCheck, Info, Repeat, Target, TriangleAlert, OctagonAlert, type LucideIcon } from "lucide-react";
import type { ButtonHTMLAttributes, ComponentProps, CSSProperties, ReactNode } from "react";

export function cx(...c: (string | false | null | undefined)[]) {
  return c.filter(Boolean).join(" ");
}

/* ───────── botões ───────── */
type Variant = "primary" | "secondary" | "ghost" | "danger" | "ink" | "onInk";
type Size = "sm" | "md" | "lg";
const VARIANT: Record<Variant, string> = {
  primary:
    "bg-primary text-on-primary border-transparent shadow-[inset_0_1px_0_rgb(255_255_255/.22),0_8px_18px_-8px_var(--primary)] hover:bg-primary-hover hover:-translate-y-px",
  secondary: "bg-surface text-text border-border shadow-card hover:border-border-strong hover:bg-surface-2",
  ghost: "bg-transparent text-muted border-transparent hover:text-text hover:bg-surface-3/70",
  danger: "bg-danger-soft text-primary border-transparent hover:brightness-95",
  ink: "bg-ink text-on-ink border-transparent hover:bg-ink-2",
  onInk: "bg-white/10 text-on-ink border-white/15 hover:bg-white/20",
};
const SIZE: Record<Size, string> = {
  sm: "px-3 py-1.5 text-[13px] rounded-lg gap-1.5",
  md: "px-4 py-2.5 text-sm rounded-xl gap-2",
  lg: "px-6 py-3.5 text-base rounded-xl gap-2.5",
};
const base =
  "inline-flex items-center justify-center border font-semibold whitespace-nowrap transition duration-200 ease-out active:scale-[0.97] active:translate-y-0 disabled:opacity-50 disabled:pointer-events-none cursor-pointer";

export function Button({ variant = "primary", size = "md", className, ...p }: ButtonHTMLAttributes<HTMLButtonElement> & { variant?: Variant; size?: Size }) {
  return <button className={cx(base, VARIANT[variant], SIZE[size], className)} {...p} />;
}

export function LinkButton({ variant = "primary", size = "md", className, ...p }: ComponentProps<typeof Link> & { variant?: Variant; size?: Size }) {
  return <Link className={cx(base, VARIANT[variant], SIZE[size], className)} {...p} />;
}

/* ───────── cartão ───────── */
export function Card({ className, children, style, tone = "surface" }: { className?: string; children: ReactNode; style?: CSSProperties; tone?: "surface" | "ink" | "soft" }) {
  const t = { surface: "border-border bg-surface", ink: "border-white/10 bg-ink text-on-ink", soft: "border-border bg-surface-2" }[tone];
  return (
    <div style={style} className={cx("rounded-2xl border p-5 shadow-card", t, className)}>
      {children}
    </div>
  );
}

/* ───────── tipos de atividade ───────── */
export type ActivityType = "TEORIA" | "REVISAO" | "FIXACAO" | "QUESTOES";
export const TYPE_META: Record<ActivityType, { label: string; tone: "teoria" | "revisao" | "fixacao" | "questoes"; color: string; Icon: LucideIcon; verb: string }> = {
  TEORIA: { label: "Teoria", tone: "teoria", color: "var(--teoria)", Icon: BookOpen, verb: "Estudar" },
  REVISAO: { label: "Revisão", tone: "revisao", color: "var(--revisao)", Icon: Repeat, verb: "Revisar" },
  FIXACAO: { label: "Fixação", tone: "fixacao", color: "var(--fixacao)", Icon: Target, verb: "Fixar" },
  QUESTOES: { label: "Questões", tone: "questoes", color: "var(--questoes)", Icon: ClipboardCheck, verb: "Resolver" },
};
export const TYPE_LABEL = { TEORIA: "Teoria", REVISAO: "Revisão", FIXACAO: "Fixação", QUESTOES: "Questões" } as const;
export const TYPE_TONE = { TEORIA: "teoria", REVISAO: "revisao", FIXACAO: "fixacao", QUESTOES: "questoes" } as const;

/** Cor por bloco da prova (usada em coberturas e projeções). */
export const BLOCK_COLOR = { I: "#0b8fb0", II: "#d99a00", III: "var(--primary)" } as const;

export function TypeIcon({ type, className = "h-5 w-5", box }: { type: ActivityType; className?: string; box?: boolean }) {
  const { Icon, color } = TYPE_META[type];
  if (!box) return <Icon className={className} style={{ color }} aria-hidden />;
  return (
    <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl" style={{ background: `color-mix(in srgb, ${color} 14%, transparent)`, color }}>
      <Icon className="h-5 w-5" aria-hidden />
    </span>
  );
}

export function TypeBadge({ type }: { type: ActivityType }) {
  const m = TYPE_META[type];
  return (
    <Badge tone={m.tone}>
      <m.Icon className="h-3 w-3" aria-hidden />
      {m.label}
    </Badge>
  );
}

/* ───────── selos ───────── */
type Tone = "neutral" | "teoria" | "revisao" | "fixacao" | "questoes" | "ok" | "warn" | "gold" | "primary";
export function Badge({ children, tone = "neutral", className }: { children: ReactNode; tone?: Tone; className?: string }) {
  const tones: Record<Tone, string> = {
    neutral: "bg-surface-3/70 text-muted",
    teoria: "bg-teoria/12 text-teoria",
    revisao: "bg-revisao/12 text-revisao",
    fixacao: "bg-fixacao/12 text-fixacao",
    questoes: "bg-questoes/12 text-questoes",
    ok: "bg-ok/12 text-ok",
    warn: "bg-warn-soft text-warn",
    gold: "bg-gold-soft text-gold-text",
    primary: "bg-primary-soft text-primary",
  };
  return <span className={cx("inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-xs font-semibold leading-5", tones[tone], className)}>{children}</span>;
}

/* ───────── progresso ───────── */
export function Progress({
  value, className, label, color, tape, size = "md", delay,
}: { value: number; className?: string; label?: string; color?: string; tape?: boolean; size?: "sm" | "md" | "lg"; delay?: number }) {
  const v = Math.max(0, Math.min(1, value));
  const pct = Math.round(v * 100);
  const h = { sm: "h-1.5", md: "h-2", lg: "h-3" }[size];
  return (
    <div className={cx("progress", h, className)} role="progressbar" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100} aria-label={label}>
      <div className={cx("progress-fill", tape && "is-tape")} style={{ "--v": v, "--fill": color, "--delay": delay ? `${delay}ms` : undefined } as CSSProperties} />
    </div>
  );
}

/** Anel de progresso (SVG). `children` ocupa o centro. */
export function Ring({
  value, size = 96, stroke = 10, color = "var(--primary)", track = "var(--surface-3)", children, label, className,
}: { value: number; size?: number; stroke?: number; color?: string; track?: string; children?: ReactNode; label?: string; className?: string }) {
  const v = Math.max(0, Math.min(1, value));
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  return (
    <div className={cx("relative shrink-0", className)} style={{ width: size, height: size }} role="img" aria-label={label ?? `${Math.round(v * 100)}%`}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} className="-rotate-90" aria-hidden>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={track} strokeWidth={stroke} />
        <circle
          className="ring-fill"
          cx={size / 2} cy={size / 2} r={r} fill="none" stroke={color} strokeWidth={stroke} strokeLinecap="round"
          style={{ "--c": c.toFixed(2), "--v": v } as CSSProperties}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center text-center">{children}</div>
    </div>
  );
}

/** Número que conta de 0 até o valor (CSS puro, sem flash na hidratação). */
export function Count({ value, suffix = "", className, delay }: { value: number; suffix?: string; className?: string; delay?: number }) {
  const n = Math.max(0, Math.round(value));
  return (
    <span className={cx("tabular", className)}>
      <span className="sr-only">{n}</span>
      <span className="count" aria-hidden style={{ "--target": n, "--delay": delay ? `${delay}ms` : undefined } as CSSProperties} />
      {suffix}
    </span>
  );
}

/* ───────── formulário ───────── */
export function Field({ label, error, hint, children }: { label: string; error?: string[]; hint?: string; children: ReactNode }) {
  return (
    <label className="block space-y-1.5">
      <span className="text-sm font-semibold">{label}</span>
      {children}
      {hint && !error?.length && <span className="block text-xs text-muted">{hint}</span>}
      {error?.map((e) => (
        <span key={e} className="block text-xs font-medium text-primary">
          {e}
        </span>
      ))}
    </label>
  );
}

export const inputCls =
  "w-full rounded-xl border border-border bg-surface px-3.5 py-2.5 text-sm outline-none transition placeholder:text-muted/70 hover:border-border-strong focus:border-primary focus:ring-4 focus:ring-[var(--ring)]/40";

/* ───────── avisos ───────── */
export function Alert({ children, tone = "warn" }: { children: ReactNode; tone?: "warn" | "danger" | "info" }) {
  const t = {
    warn: { cls: "bg-warn-soft text-warn", Icon: TriangleAlert },
    danger: { cls: "bg-danger-soft text-primary", Icon: OctagonAlert },
    info: { cls: "bg-surface-3/60 text-muted", Icon: Info },
  }[tone];
  return (
    <div className={cx("flex items-start gap-3 rounded-xl px-4 py-3 text-sm leading-relaxed", t.cls)} role={tone === "danger" ? "alert" : undefined}>
      <t.Icon className="mt-0.5 h-4 w-4 shrink-0" aria-hidden />
      <div className="min-w-0">{children}</div>
    </div>
  );
}

/* ───────── balão informativo (?) ───────── */
/** Explicações longas ficam recolhidas: aparecem ao passar o mouse, focar (teclado) ou tocar no "?". */
export function InfoTip({ children, label = "Mais informações", align = "center", className }: { children: ReactNode; label?: string; align?: "start" | "center" | "end"; className?: string }) {
  const pos = { start: "left-0", center: "left-1/2 -translate-x-1/2", end: "right-0" }[align];
  return (
    <span className={cx("group/tip relative inline-flex align-middle", className)}>
      <button
        type="button"
        aria-label={label}
        className="flex h-[18px] w-[18px] cursor-help items-center justify-center rounded-full border border-border-strong bg-surface-2 font-sans text-[11px] font-bold leading-none text-muted transition hover:border-primary hover:bg-primary hover:text-on-primary focus-visible:border-primary focus-visible:bg-primary focus-visible:text-on-primary"
      >
        ?
      </button>
      <span
        role="tooltip"
        className={cx(
          "pointer-events-none invisible absolute top-full z-40 mt-2 w-64 max-w-[78vw] translate-y-1 rounded-xl border border-border bg-surface p-3 text-left font-sans text-[12.5px] font-normal normal-case leading-snug tracking-normal text-text opacity-0 shadow-lift transition duration-150",
          "group-hover/tip:visible group-hover/tip:translate-y-0 group-hover/tip:opacity-100 group-focus-within/tip:visible group-focus-within/tip:translate-y-0 group-focus-within/tip:opacity-100",
          pos,
        )}
      >
        {children}
      </span>
    </span>
  );
}

/* ───────── estrutura de página ───────── */
export function PageHeader({ eyebrow, title, description, info, actions, className }: { eyebrow?: ReactNode; title: ReactNode; description?: ReactNode; info?: ReactNode; actions?: ReactNode; className?: string }) {
  return (
    <header className={cx("flex flex-wrap items-end justify-between gap-4", className)}>
      <div className="min-w-0">
        {eyebrow && <p className="eyebrow mb-1">{eyebrow}</p>}
        <h1 className="flex items-center gap-3 font-display text-[2.25rem] font-bold uppercase leading-none tracking-tight sm:text-5xl">
          {title}
          {info && <InfoTip align="start" className="mt-1">{info}</InfoTip>}
        </h1>
        {description && <p className="mt-2 max-w-2xl text-sm text-muted">{description}</p>}
      </div>
      {actions && <div className="flex flex-wrap gap-2">{actions}</div>}
    </header>
  );
}

export function SectionTitle({ id, children, aside, info }: { id?: string; children: ReactNode; aside?: ReactNode; info?: ReactNode }) {
  return (
    <div className="mb-3 flex items-end justify-between gap-3">
      <h2 id={id} className="flex items-center gap-2 font-display text-2xl font-bold uppercase tracking-wide">
        {children}
        {info && <InfoTip align="start">{info}</InfoTip>}
      </h2>
      {aside && <div className="text-xs text-muted">{aside}</div>}
    </div>
  );
}

export function Stat({ label, value, hint, icon, info, delay = 0, className }: { label: string; value: ReactNode; hint?: ReactNode; icon?: ReactNode; info?: ReactNode; delay?: number; className?: string }) {
  return (
    <Card className={cx("rise relative overflow-hidden p-4", className)} style={{ "--i": delay } as CSSProperties}>
      <p className="eyebrow flex items-center gap-1.5">
        {label}
        {info && <InfoTip align="start">{info}</InfoTip>}
      </p>
      <div className="mt-1 flex items-end justify-between gap-2">
        <p className="font-display text-4xl font-bold leading-none tabular">{value}</p>
        {icon && <span className="mb-0.5 text-muted">{icon}</span>}
      </div>
      {hint && <p className="mt-1.5 text-xs text-muted">{hint}</p>}
    </Card>
  );
}

export function EmptyState({ icon, title, children, action }: { icon?: ReactNode; title: string; children?: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex flex-col items-center gap-3 rounded-2xl border border-dashed border-border-strong bg-surface/60 px-6 py-10 text-center">
      {icon && <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-surface-3 text-muted">{icon}</span>}
      <p className="font-display text-xl font-bold uppercase tracking-wide">{title}</p>
      {children && <p className="max-w-md text-sm text-muted">{children}</p>}
      {action}
    </div>
  );
}

export function Kbd({ children }: { children: ReactNode }) {
  return <kbd className="inline-flex min-w-5 items-center justify-center rounded-md border border-border-strong bg-surface-2 px-1.5 text-[11px] font-semibold leading-5 text-muted shadow-[0_1px_0_var(--border-strong)]">{children}</kbd>;
}
