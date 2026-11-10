"use client";

import { FileText } from "lucide-react";
import { useId, useState, type ReactNode } from "react";
import { ReportMaterialError } from "@/components/report-material-error";
import { LinkButton, cx } from "@/components/ui";
import type { MaterialChoice } from "@/lib/directive";

function saveChoice(v: MaterialChoice) {
  try {
    document.cookie = `material=${v}; path=/; max-age=31536000; samesite=lax`;
  } catch {}
}

/**
 * Diretriz nos dois materiais: o material próprio MentorIA e o material-base. A escolha fica num cookie e vale para as
 * próximas atividades (preferência do aluno); a outra aba continua a um clique.
 */
export function MaterialTabs({ initial, mentoria, base }: { initial: MaterialChoice; mentoria: ReactNode; base: ReactNode }) {
  const uid = useId();
  const [current, setCurrent] = useState<MaterialChoice>(initial);
  const choose = (v: MaterialChoice) => {
    setCurrent(v);
    saveChoice(v);
  };
  const tabs: { id: MaterialChoice; label: string; content: ReactNode }[] = [
    { id: "mentoria", label: "Material MentorIA", content: mentoria },
    { id: "base", label: "Material-base", content: base },
  ];
  return (
    <div className="space-y-4">
      <div role="tablist" aria-label="Material de estudo" className="flex flex-wrap gap-1.5 rounded-2xl bg-surface-2 p-1.5">
        {tabs.map((t) => (
          <button
            key={t.id}
            type="button"
            role="tab"
            id={`${uid}-tab-${t.id}`}
            aria-selected={t.id === current}
            aria-controls={`${uid}-panel-${t.id}`}
            onClick={() => choose(t.id)}
            className={cx(
              "flex-1 cursor-pointer rounded-xl px-3.5 py-2 text-sm font-semibold transition",
              t.id === current ? "bg-surface text-text shadow-card" : "text-muted hover:text-text",
            )}
          >
            {t.label}
          </button>
        ))}
      </div>
      {tabs.map((t) => (
        <div key={t.id} role="tabpanel" id={`${uid}-panel-${t.id}`} aria-labelledby={`${uid}-tab-${t.id}`} hidden={t.id !== current} className="space-y-4">
          {t.content}
        </div>
      ))}
    </div>
  );
}

/** Botão que abre o PDF do material próprio já na página indicada, com o atalho para reportar erro nele. */
export function MentoriaPdfLink({ href, page, report }: { href: string; page?: number | null; report?: { volumeId: string; volumeLabel: string; maxPage: number } }) {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <LinkButton href={href} target="_blank" rel="noopener" variant="secondary" size="sm">
        <FileText className="h-4 w-4" aria-hidden />
        Abrir o PDF{page ? `, página ${page}` : ""}
      </LinkButton>
      {report && <ReportMaterialError {...report} defaultPage={page} />}
    </div>
  );
}
