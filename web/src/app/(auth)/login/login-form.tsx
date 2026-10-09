"use client";

import { Loader2, LogIn } from "lucide-react";
import Link from "next/link";
import { useActionState } from "react";
import { Alert, Button, Field, inputCls } from "@/components/ui";
import { login } from "../actions";

export function LoginForm() {
  const [state, action, pending] = useActionState(login, undefined);
  return (
    <form action={action} className="space-y-5">
      <div>
        <p className="eyebrow">Bem-vindo de volta</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-none">Entrar</h1>
      </div>
      {state?.message && <Alert tone="danger">{state.message}</Alert>}
      <Field label="E-mail" error={state?.errors?.email}>
        <input name="email" type="email" autoComplete="email" required className={inputCls} />
      </Field>
      <Field label="Senha" error={state?.errors?.password}>
        <input name="password" type="password" autoComplete="current-password" required className={inputCls} />
      </Field>
      <Button type="submit" size="lg" disabled={pending} className="w-full">
        {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <LogIn className="h-5 w-5" aria-hidden />}
        {pending ? "Entrando…" : "Entrar"}
      </Button>
      <p className="text-center text-sm text-muted">
        Tem um convite? <Link href="/cadastro" className="font-semibold text-primary hover:underline">Criar conta</Link>
      </p>
      <p className="text-center text-sm text-muted">
        Ainda não tem acesso? <Link href="/concursos" className="font-semibold text-primary hover:underline">Entrar na lista de espera</Link>
      </p>
    </form>
  );
}
