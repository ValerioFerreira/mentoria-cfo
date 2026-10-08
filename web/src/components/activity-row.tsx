import { ChevronRight, Clock3 } from "lucide-react";
import Link from "next/link";
import type { CSSProperties } from "react";
import { QuickTime, StatusToggle } from "@/components/study-controls";
import { Badge, TYPE_META, TypeIcon, cx, type ActivityType } from "@/components/ui";
import { aulaLabel } from "@/lib/directive";
import { fmtDuration, subjectShort } from "@/lib/ui-format";

export interface ActivityRowData {
  id: string;
  type: ActivityType;
  status: string;
  subjectId: string;
  scope: string;
  plannedMinutes: number;
  aula: { number: number; shortTitle: string };
  /** o que fazer, em uma linha: páginas, questões comentadas, tamanho do caderno */
  detail?: string | null;
}

export function activityTitle(a: Pick<ActivityRowData, "scope" | "type" | "aula">) {
  if (a.scope === "FINAL") return a.type === "QUESTOES" ? "Caderno misto da disciplina" : "Revisão geral dos trechos mais importantes";
  return aulaLabel(a.aula);
}

/** "1h05" / "45 min" para minutos planejados. */
export const fmtMinutes = (m: number) => fmtDuration(m * 60);

/**
 * Linha de atividade: marcador, tipo, disciplina/aula e tempo. O cartão inteiro é clicável (link "esticado"),
 * mas o marcador de conclusão e o lançamento de tempo continuam sendo controles independentes.
 */
export function ActivityRow({ a, spent = 0, order, index = 0, quickTime = true }: { a: ActivityRowData; spent?: number; order?: number; index?: number; quickTime?: boolean }) {
  const m = TYPE_META[a.type];
  const done = a.status === "DONE";
  const skipped = a.status === "SKIPPED";
  return (
    <div
      className={cx("card-hover rise group relative flex items-center gap-3.5 overflow-hidden rounded-2xl border border-border bg-surface p-3.5 pl-5 shadow-card sm:gap-4", (done || skipped) && "bg-surface/70")}
      style={{ "--i": index } as CSSProperties}
    >
      <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: m.color, opacity: done || skipped ? 0.35 : 1 }} aria-hidden />
      <span className="relative z-10">
        <StatusToggle id={a.id} status={a.status} compact />
      </span>
      <span className="hidden sm:block"><TypeIcon type={a.type} box /></span>
      <div className={cx("min-w-0 flex-1", (done || skipped) && "opacity-65")}>
        <Link href={`/atividade/${a.id}`} className="block after:absolute after:inset-0 after:content-['']">
          <span className="flex flex-wrap items-center gap-x-2 gap-y-0.5">
            {order !== undefined && <span className="text-xs font-semibold tabular text-muted">{order}.</span>}
            <span className="text-[15px] font-bold leading-tight">{subjectShort(a.subjectId)}</span>
            <span className="text-xs font-semibold" style={{ color: m.color }}>{m.label}</span>
            {a.detail && <span className="text-xs font-semibold text-text/70">· {a.detail}</span>}
            {a.scope === "FINAL" && <Badge tone="gold">geral</Badge>}
            {skipped && <Badge>pulada</Badge>}
          </span>
          <span className="mt-0.5 line-clamp-2 block text-sm text-muted sm:line-clamp-1">{activityTitle(a)}</span>
        </Link>
      </div>
      <div className="relative z-10 flex shrink-0 flex-col items-end gap-1 text-xs text-muted tabular">
        <span className="flex items-center gap-1"><Clock3 className="h-3.5 w-3.5" aria-hidden />{fmtMinutes(a.plannedMinutes)}</span>
        {quickTime && <QuickTime id={a.id} seconds={spent} />}
      </div>
      <ChevronRight className="hidden h-4 w-4 shrink-0 text-muted transition group-hover:translate-x-0.5 group-hover:text-text sm:block" aria-hidden />
    </div>
  );
}

/** Cartão vertical e compacto (colunas da Meta semanal). */
export function ActivityCard({ a, spent = 0, index = 0, late }: { a: ActivityRowData; spent?: number; index?: number; late?: boolean }) {
  const m = TYPE_META[a.type];
  const done = a.status === "DONE";
  const skipped = a.status === "SKIPPED";
  return (
    <div
      className={cx("card-hover rise group relative overflow-hidden rounded-xl border bg-surface p-2.5 pl-3.5 shadow-card", late ? "border-warn/60" : "border-border", (done || skipped) && "bg-surface/60")}
      style={{ "--i": index } as CSSProperties}
    >
      <span className="absolute inset-y-0 left-0 w-1" style={{ background: m.color, opacity: done || skipped ? 0.35 : 1 }} aria-hidden />
      <div className="flex items-start justify-between gap-1.5">
        <span className="flex items-center gap-1 text-[11px] font-bold uppercase tracking-wide" style={{ color: m.color }}>
          <m.Icon className="h-3.5 w-3.5" aria-hidden />
          {m.label}
        </span>
        <span className="relative z-10 -mr-0.5 -mt-0.5">
          <StatusToggle id={a.id} status={a.status} compact />
        </span>
      </div>
      <Link href={`/atividade/${a.id}`} className={cx("block after:absolute after:inset-0 after:content-['']", (done || skipped) && "opacity-65")}>
        <span className="mt-1 block text-[13px] font-bold leading-tight">{subjectShort(a.subjectId)}</span>
        <span className="mt-0.5 line-clamp-3 block text-xs leading-snug text-muted">{activityTitle(a)}</span>
        {a.detail && <span className="mt-0.5 block text-[11px] font-semibold leading-snug text-text/80">{a.detail}</span>}
      </Link>
      <div className="mt-2 flex items-center justify-between text-[11px] text-muted tabular">
        <span className="flex items-center gap-1"><Clock3 className="h-3 w-3" aria-hidden />{fmtMinutes(a.plannedMinutes)}</span>
        {spent > 0 && <span className="font-semibold text-ok">{fmtDuration(spent)} estudados</span>}
        {skipped && <Badge>pulada</Badge>}
      </div>
    </div>
  );
}
