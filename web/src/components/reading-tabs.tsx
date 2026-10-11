"use client";

import { useId, useState, type ReactNode } from "react";
import { cx } from "@/components/ui";

export interface ReadingTab {
  id: string;
  label: string;
  content: ReactNode;
}

/** Alternância entre formas de estudar o mesmo assunto (ex.: seguir as páginas × ler o resumo analítico). */
export function ReadingTabs({ tabs, initial }: { tabs: ReadingTab[]; initial?: string }) {
  const uid = useId();
  const [current, setCurrent] = useState(tabs.some((t) => t.id === initial) ? initial! : tabs[0].id);
  return (
    <div className="space-y-4">
      <div role="tablist" aria-label="Forma de estudo" className="flex flex-wrap gap-1.5 rounded-2xl bg-surface-2 p-1.5">
        {tabs.map((t) => {
          const active = t.id === current;
          return (
            <button
              key={t.id}
              type="button"
              role="tab"
              id={`${uid}-tab-${t.id}`}
              aria-selected={active}
              aria-controls={`${uid}-panel-${t.id}`}
              onClick={() => setCurrent(t.id)}
              className={cx(
                "flex-1 cursor-pointer rounded-xl px-3.5 py-2 text-sm font-semibold transition",
                active ? "bg-surface text-text shadow-card" : "text-muted hover:text-text",
              )}
            >
              {t.label}
            </button>
          );
        })}
      </div>
      {tabs.map((t) => (
        <div key={t.id} role="tabpanel" id={`${uid}-panel-${t.id}`} aria-labelledby={`${uid}-tab-${t.id}`} hidden={t.id !== current} className="space-y-4">
          {t.content}
        </div>
      ))}
    </div>
  );
}
