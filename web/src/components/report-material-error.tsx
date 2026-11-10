"use client";

import { Flag, X } from "lucide-react";
import { useActionState, useState } from "react";
import { Button, Field, inputCls } from "@/components/ui";
import { reportMaterialError, type MaterialReportState } from "@/lib/material-report-actions";

/** "Reportar erro no PDF": o aluno informa a página e explica o problema. */
export function ReportMaterialError({ volumeId, volumeLabel, defaultPage, maxPage }: { volumeId: string; volumeLabel: string; defaultPage?: number | null; maxPage: number }) {
  const [open, setOpen] = useState(false);
  const [state, action, pending] = useActionState<MaterialReportState, FormData>(reportMaterialError.bind(null, volumeId), {});
  return (
    <>
      <Button type="button" variant="ghost" size="sm" onClick={() => setOpen(true)}>
        <Flag className="h-4 w-4" aria-hidden />
        Reportar erro no PDF
      </Button>
      {open && (
        <div role="dialog" aria-modal="true" aria-label="Reportar erro no PDF" className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4" onClick={() => setOpen(false)}>
          <div className="w-full max-w-md space-y-4 rounded-2xl bg-surface p-5 shadow-card" onClick={(e) => e.stopPropagation()}>
            <div className="flex items-start justify-between gap-3">
              <div>
                <h2 className="font-display text-2xl font-bold uppercase tracking-wide">Reportar erro no PDF</h2>
                <p className="text-sm text-muted">{volumeLabel}</p>
              </div>
              <button type="button" onClick={() => setOpen(false)} aria-label="Fechar" className="cursor-pointer rounded-lg p-1 text-muted hover:text-text">
                <X className="h-5 w-5" aria-hidden />
              </button>
            </div>
            {state.ok ? (
              <>
                <p className="text-sm font-medium text-ok">{state.message}</p>
                <Button type="button" onClick={() => setOpen(false)}>Fechar</Button>
              </>
            ) : (
              <form action={action} className="space-y-4">
                <Field label="Página do PDF onde está o erro" hint={`Número da página no leitor do PDF (de 1 a ${maxPage}).`}>
                  <input name="page" type="number" min={1} max={maxPage} defaultValue={defaultPage ?? undefined} required className={inputCls} />
                </Field>
                <Field label="O que está errado?" hint="Diga o trecho e o que deveria estar escrito. Máximo de 1.000 caracteres.">
                  <textarea name="message" rows={5} minLength={10} maxLength={1000} required className={inputCls} />
                </Field>
                {state.message && <p className="text-sm font-medium text-primary">{state.message}</p>}
                <div className="flex justify-end gap-2">
                  <Button type="button" variant="secondary" onClick={() => setOpen(false)}>Cancelar</Button>
                  <Button type="submit" disabled={pending}>{pending ? "Enviando…" : "Enviar"}</Button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}
    </>
  );
}
