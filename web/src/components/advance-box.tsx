"use client";

import { ChevronDown, FastForward, TriangleAlert } from "lucide-react";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { Button, TYPE_META, TypeIcon, cx, type ActivityType } from "@/components/ui";
import { fmtDuration, subjectShort } from "@/lib/ui-format";

export interface AdvanceItem {
  id: string;
  type: ActivityType;
  subjectId: string;
  title: string;
  minutes: number;
}

/**
 * "Adiantar": permitido, mas desencorajado. O plano espaça revisões e questões de propósito; antecipar uma atividade
 * quebra esse espaçamento. Por isso o aviso aparece ao abrir a lista e de novo antes de cada atividade.
 */
export function AdvanceBox({ items, label }: { items: AdvanceItem[]; label: string }) {
  const [open, setOpen] = useState(false);
  const [target, setTarget] = useState<AdvanceItem | null>(null);
  const router = useRouter();
  if (items.length === 0) return null;
  return (
    <section aria-label="Adiantar atividades" className="space-y-3">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
        className="flex w-full cursor-pointer items-center justify-between gap-3 rounded-2xl border border-dashed border-border-strong px-4 py-3 text-left text-sm font-semibold text-muted transition hover:border-primary hover:text-text"
      >
        <span className="flex items-center gap-2">
          <FastForward className="h-4 w-4" aria-hidden />
          Adiantar atividades · {label}
        </span>
        <ChevronDown className={cx("h-4 w-4 transition-transform", open && "rotate-180")} aria-hidden />
      </button>

      {open && (
        <div className="swap-in space-y-3">
          <div className="flex items-start gap-3 rounded-xl bg-warn-soft px-4 py-3 text-sm leading-relaxed text-warn" role="note">
            <TriangleAlert className="mt-0.5 h-4 w-4 shrink-0" aria-hidden />
            <p>O ideal é seguir o plano na ordem de cada dia: as revisões e os cadernos foram espaçados de propósito para fixar o conteúdo. Adiantar é possível, mas tire o máximo da missão de hoje primeiro.</p>
          </div>
          <ul className="space-y-2">
            {items.map((a) => (
              <li key={a.id}>
                <button
                  type="button"
                  onClick={() => setTarget(a)}
                  className="flex w-full cursor-pointer items-center gap-3 rounded-xl border border-border bg-surface px-3.5 py-3 text-left transition hover:border-border-strong hover:bg-surface-2"
                >
                  <TypeIcon type={a.type} box />
                  <span className="min-w-0 flex-1">
                    <span className="block text-sm font-bold">{subjectShort(a.subjectId)} <span className="text-xs font-semibold" style={{ color: TYPE_META[a.type].color }}>{TYPE_META[a.type].label}</span></span>
                    <span className="block truncate text-sm text-muted">{a.title}</span>
                  </span>
                  <span className="text-xs font-semibold text-muted tabular">{fmtDuration(a.minutes * 60)}</span>
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      {target && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center bg-black/50 px-4 backdrop-blur-sm" role="dialog" aria-modal="true" aria-labelledby="adiantar-titulo">
          <div className="pop w-full max-w-md space-y-4 rounded-2xl border border-border bg-surface p-6 text-text shadow-lift">
            <h2 id="adiantar-titulo" className="font-display text-2xl font-bold uppercase tracking-wide">Adiantar esta atividade?</h2>
            <p className="text-sm text-muted">
              {subjectShort(target.subjectId)} · {TYPE_META[target.type].label} faz parte do próximo dia do plano. Seguir a ordem garante o espaçamento entre teoria, revisão e questões, que é o que mais ajuda a lembrar na prova. Se mesmo assim quiser adiantar, tudo bem.
            </p>
            <div className="flex flex-wrap justify-end gap-2">
              <Button variant="ghost" onClick={() => setTarget(null)} autoFocus>Voltar à missão de hoje</Button>
              <Button variant="secondary" onClick={() => router.push(`/atividade/${target.id}`)}>Adiantar mesmo assim</Button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
