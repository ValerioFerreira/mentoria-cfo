"use client";

import Link from "next/link";
import { useActionState } from "react";
import { Alert, Button, Card, Field, inputCls } from "@/components/ui";
import { saveCpf, type CpfState } from "./cpf-actions";

export function CpfCard({ masked, required }: { masked: string | null; required: boolean }) {
  const [state, action, pending] = useActionState<CpfState, FormData>(saveCpf, {});
  if (masked) {
    return (
      <Card className="p-5">
        <h2 className="font-display text-xl font-bold uppercase tracking-wide">CPF do titular</h2>
        <p className="mt-1 text-sm text-muted">
          Registrado: <span className="font-semibold text-text">{masked}</span>. Ele aparece no rodapé dos PDFs do material, junto com o seu nome.
        </p>
      </Card>
    );
  }
  return (
    <Card className="p-5" tone={required ? "soft" : "surface"}>
      <h2 className="font-display text-xl font-bold uppercase tracking-wide">CPF do titular</h2>
      <p className="mt-1 text-sm text-muted">
        Os PDFs do material MentorIA levam o seu nome e o seu CPF no rodapé de cada página: a licença é pessoal. Informe o CPF uma única vez para liberar os PDFs. Veja como tratamos esse dado na{" "}
        <Link href="/privacidade" target="_blank" className="font-semibold text-primary underline">
          Política de Privacidade
        </Link>
        .
      </p>
      {required && (
        <div className="mt-3">
          <Alert tone="warn">Para abrir o PDF, informe primeiro o seu CPF.</Alert>
        </div>
      )}
      <form action={action} className="mt-4 flex flex-wrap items-end gap-3">
        <div className="w-full max-w-xs">
          <Field label="CPF">
            <input name="cpf" inputMode="numeric" autoComplete="off" placeholder="000.000.000-00" maxLength={14} className={inputCls} required />
          </Field>
        </div>
        <Button type="submit" disabled={pending}>
          {pending ? "Salvando…" : "Salvar CPF"}
        </Button>
      </form>
      {state.message && <p className={`mt-3 text-sm font-medium ${state.ok ? "text-ok" : "text-primary"}`}>{state.message}</p>}
    </Card>
  );
}
