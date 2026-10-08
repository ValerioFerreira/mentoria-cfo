"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Button } from "@/components/ui";
import { approveBatch, resolveReport, setQuestionStatus } from "@/lib/admin/actions";

type Props =
  | { kind: "question"; id: string; status: string }
  | { kind: "batch"; batch: string }
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
  if (p.kind === "report") {
    return (
      <div className="flex gap-2">
        <Button variant="secondary" size="sm" disabled={pending} onClick={() => run(() => resolveReport(p.reportId, "RESOLVED", true))}>Procede: sinalizar questão</Button>
        <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => resolveReport(p.reportId, "DISMISSED", false))}>Não procede</Button>
      </div>
    );
  }
  return (
    <div className="flex flex-wrap gap-2 border-t border-border pt-3">
      {p.status !== "APPROVED" && <Button size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "APPROVED"))}>Aprovar</Button>}
      {p.status !== "FLAGGED" && <Button variant="secondary" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "FLAGGED"))}>Sinalizar</Button>}
      {p.status !== "RETIRED" && <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "RETIRED"))}>Aposentar</Button>}
      {p.status !== "DRAFT" && <Button variant="ghost" size="sm" disabled={pending} onClick={() => run(() => setQuestionStatus(p.id, "DRAFT"))}>Voltar a rascunho</Button>}
    </div>
  );
}
