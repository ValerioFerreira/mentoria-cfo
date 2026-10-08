"use client";

import { Flag, Send } from "lucide-react";
import { useState, useTransition } from "react";
import { Button, inputCls } from "@/components/ui";
import { reportQuestion } from "@/lib/admin/actions";

export function ReportButton({ questionId }: { questionId: string }) {
  const [open, setOpen] = useState(false);
  const [text, setText] = useState("");
  const [msg, setMsg] = useState<string | null>(null);
  const [pending, start] = useTransition();
  if (msg === "ok") return <p className="pop text-xs font-semibold text-ok">Obrigado! Sua observação foi enviada para revisão.</p>;
  return (
    <div className="space-y-2">
      {!open ? (
        <button type="button" onClick={() => setOpen(true)} className="inline-flex cursor-pointer items-center gap-1.5 text-xs font-semibold text-muted transition hover:text-text">
          <Flag className="h-3.5 w-3.5" aria-hidden />
          Reportar problema nesta questão
        </button>
      ) : (
        <form
          className="page-in space-y-2"
          onSubmit={(e) => {
            e.preventDefault();
            start(async () => {
              const r = await reportQuestion(questionId, text);
              setMsg(r.ok ? "ok" : (r.error ?? "Erro ao enviar."));
            });
          }}
        >
          <label className="sr-only" htmlFor={`rep-${questionId}`}>Descreva o problema</label>
          <textarea id={`rep-${questionId}`} value={text} onChange={(e) => setText(e.target.value)} rows={2} placeholder="Ex.: gabarito errado, duas alternativas corretas, enunciado ambíguo…" className={inputCls} required />
          {msg && msg !== "ok" && <p className="text-xs font-medium text-primary">{msg}</p>}
          <div className="flex gap-2">
            <Button type="submit" variant="secondary" size="sm" disabled={pending}>
              <Send className="h-3.5 w-3.5" aria-hidden />
              Enviar
            </Button>
            <Button type="button" variant="ghost" size="sm" onClick={() => setOpen(false)}>Cancelar</Button>
          </div>
        </form>
      )}
    </div>
  );
}
