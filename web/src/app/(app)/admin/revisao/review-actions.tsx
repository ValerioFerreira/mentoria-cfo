"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Button } from "@/components/ui";
import { approveBatch, approveTecAssunto, moveQuestion, resolveReport, setQuestionStatus } from "@/lib/admin/actions";

export interface SegmentChoice {
  id: string;
  label: string; // "aNN/sNN · tópico inicial"
  group: string; // aula
}

type Props =
  | { kind: "question"; id: string; status: string; segmentId?: string; segments?: SegmentChoice[] }
  | { kind: "batch"; batch: string }
  | { kind: "assunto"; materia: string; assunto: string; count: number }
  | { kind: "report"; reportId: string };

export function ReviewActions(p: Props) {
  const [pending, start] = useTransition();
  const [note, setNote] = useState<string | null>(null);
  const router = useRouter();
  const run = (fn: () => Promise<unknown>) =>
    start(async () => {
      await fn();
      router.refresh();
    });

  if (p.kind === "batch") {
    return (
      <span className="flex items-center gap-2">
        {note && <span className="text-xs text-ok">{note}</span>}
        <Button
          variant="secondary"
          size="sm"
          disabled={pending}
          onClick={() => {
            if (!confirm(`Aprovar TODOS os rascunhos do lote "${p.batch}"? Isso os libera para os alunos.`)) return;
            run(async () => {
              const r = await approveBatch(p.batch);
              setNote(`${r.approved} aprovadas`);
            });
          }}
        >
          Aprovar lote
        </Button>
      </span>
    );
  }
  if (p.kind === "assunto") {
    return (
      <span className="flex items-center gap-2">
        {note && <span className="text-xs text-ok">{note}</span>}
        <Button
          variant="secondary"
          size="sm"
          disabled={pending}
          onClick={() => {
            if (!confirm(`Aprovar os ${p.count} rascunhos do assunto "${p.assunto}" nos trechos sugeridos?`)) return;
            run(async () => {
              const r = await approveTecAssunto(p.materia, p.assunto);
              setNote(`${r.approved} aprovadas`);
            });
          }}
        >
          Aprovar assunto
        </Button>
      </span>
    );
  }
  if (p.kind === "report") {
    return (
      <div className="flex gap-2">
        <Button variant="secondary" size="sm" disabled={pending} onClick={() => run(() => resolveReport(p.reportId, "RESOLVED", true))}>Procede: sinalizar questão</Button>
        <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => resolveReport(p.reportId, "DISMISSED", false))}>Não procede</Button>
      </div>
    );
  }
  const groups = new Map<string, SegmentChoice[]>();
  for (const s of p.segments ?? []) groups.set(s.group, [...(groups.get(s.group) ?? []), s]);
  return (
    <div className="flex flex-wrap gap-2 border-t border-border pt-3">
      {p.segments && p.segments.length > 0 && (
        <label className="flex w-full flex-wrap items-center gap-2 text-xs text-muted">
          Trecho (atividade):
          <select
            className="min-w-0 max-w-full flex-1 rounded-lg border border-border bg-surface px-2 py-1.5 text-sm text-text"
            defaultValue={p.segmentId}
            disabled={pending}
            onChange={(e) => {
              const seg = e.target.value;
              if (seg && seg !== p.segmentId) run(() => moveQuestion(p.id, seg));
            }}
          >
            {[...groups.entries()].map(([g, segs]) => (
              <optgroup key={g} label={g}>
                {segs.map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.label}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </label>
      )}
      {p.status !== "APPROVED" && <Button size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "APPROVED"))}>Aprovar</Button>}
      {p.status !== "FLAGGED" && <Button variant="secondary" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "FLAGGED"))}>Sinalizar</Button>}
      {p.status !== "RETIRED" && <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "RETIRED"))}>Aposentar</Button>}
      {p.status !== "DRAFT" && <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "DRAFT"))}>Voltar a rascunho</Button>}
    </div>
  );
}
