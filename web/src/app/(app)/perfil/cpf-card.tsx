"use client";

import Link from "next/link";
import { useActionState } from "react";
import { Alert, Button, Card, Field, inputCls } from "@/components/ui";
import { saveCpf, type CpfState } from "./cpf-actions";

export function CpfCard({ masked, name, required }: { masked: string | null; name: string; required: boolean }) {
  const [state, action, pending] = useActionState<CpfState, FormData>(saveCpf, {});
  if (masked) {
    return (
      <Card className="p-5">
        <h2 className="font-display text-xl font-bold uppercase tracking-wide">CPF do titular</h2>
        <p className="mt-1 text-sm text-muted">
          Registrado: <span className="font-semibold text-text">{masked}</span> em nome de <span className="font-semibold uppercase text-text">{name}</span>. Os dois aparecem no rodapé dos PDFs do material.
        </p>
      </Card>
    );
  }
  return (
    <Card className="p-5" tone={required ? "soft" : "surface"}>
      <h2 className="font-display text-xl font-bold uppercase tracking-wide">CPF e nome do titular</h2>
      <p className="mt-1 text-sm text-muted">
        Os PDFs do material MentorIA levam o seu nome completo e o seu CPF no rodapé de cada página: a licença é pessoal. Informe os dois uma única vez para liberar os PDFs. Veja como tratamos esse dado na{" "}
        <Link href="/privacidade" target="_blank" className="font-semibold text-primary underline">
          Política de Privacidade
        </Link>
        .
      </p>
      {required && (
        <div className="mt-3">
          <Alert tone="warn">Para abrir o PDF, informe primeiro o seu CPF e confirme o seu nome completo.</Alert>
        </div>
      )}
      <form action={action} className="mt-4 space-y-4">
        <div className="grid gap-4 sm:grid-cols-2">
          <Field label="Nome completo" hint="Confira e corrija se preciso. Fica em caixa alta na conta e no PDF.">
            <input name="name" defaultValue={name.toUpperCase()} autoComplete="name" autoCapitalize="characters" className={`${inputCls} uppercase`} required />
          </Field>
          <Field label="CPF">
            <input name="cpf" inputMode="numeric" autoComplete="off" placeholder="000.000.000-00" maxLength={14} className={inputCls} required />
          </Field>
        </div>
        <label className="flex cursor-pointer items-start gap-2.5 text-sm leading-relaxed text-text">
          <input type="checkbox" name="confirm" required className="mt-1 h-4 w-4 shrink-0 cursor-pointer accent-[var(--primary)]" />
          <span>Confirmo que o nome e o CPF são meus. Depois de salvos, só o suporte pode alterá-los.</span>
        </label>
        <Button type="submit" disabled={pending}>
          {pending ? "Salvando…" : "Salvar CPF e nome"}
        </Button>
      </form>
      {state.message && <p className={`mt-3 text-sm font-medium ${state.ok ? "text-ok" : "text-primary"}`}>{state.message}</p>}
    </Card>
  );
}
