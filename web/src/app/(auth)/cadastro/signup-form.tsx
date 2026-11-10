"use client";

import { Loader2, UserPlus } from "lucide-react";
import Link from "next/link";
import { useActionState } from "react";
import { Alert, Button, Field, inputCls } from "@/components/ui";
import { signup } from "../actions";

export function SignupForm({ invite }: { invite?: string }) {
  const [state, action, pending] = useActionState(signup, undefined);
  return (
    <form action={action} className="space-y-5">
      <div>
        <p className="eyebrow">Acesso por convite</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-none">Criar conta</h1>
        <p className="mt-2 text-sm text-muted">Peça o código a quem administra o site.</p>
      </div>
      {state?.message && <Alert tone="danger">{state.message}</Alert>}
      <Field label="Código de convite" error={state?.errors?.invite}>
        <input name="invite" defaultValue={invite} required autoComplete="off" className={inputCls} />
      </Field>
      <Field label="Nome" error={state?.errors?.name}>
        <input name="name" autoComplete="name" required className={inputCls} />
      </Field>
      <Field label="E-mail" error={state?.errors?.email}>
        <input name="email" type="email" autoComplete="email" required className={inputCls} />
      </Field>
      <Field label="Senha" error={state?.errors?.password} hint="Mínimo de 8 caracteres.">
        <input name="password" type="password" autoComplete="new-password" required minLength={8} className={inputCls} />
      </Field>
      <Button type="submit" size="lg" disabled={pending} className="w-full">
        {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <UserPlus className="h-5 w-5" aria-hidden />}
        {pending ? "Criando…" : "Criar conta"}
      </Button>
      <p className="text-center text-sm text-muted">
        Já tem conta? <Link href="/login" className="font-semibold text-primary hover:underline">Entrar</Link>
      </p>
    </form>
  );
}
