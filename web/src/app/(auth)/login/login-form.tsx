"use client";

import { Eye, EyeOff, Loader2, LogIn } from "lucide-react";
import Link from "next/link";
import { useActionState, useState } from "react";
import { Alert, Button, Field, LinkButton, inputCls } from "@/components/ui";
import { login } from "../actions";

export function LoginForm() {
  const [state, action, pending] = useActionState(login, undefined);
  const [show, setShow] = useState(false);
  return (
    <div className="space-y-8">
      <form id="login-form" method="POST" action={action} className="space-y-5">
        <div className="space-y-1">
          <h1 className="font-display text-5xl font-bold uppercase leading-none sm:text-6xl">Entrar</h1>
          <p className="text-sm text-muted">Acesse o seu plano de estudos.</p>
        </div>
        {state?.message && <Alert tone="danger">{state.message}</Alert>}
        <Field label="E-mail" error={state?.errors?.email}>
          <input id="email" name="email" type="email" autoComplete="username email" required className={inputCls} />
        </Field>
        <div className="space-y-1.5">
          <div className="flex items-center justify-between">
            <label htmlFor="password" className="block text-sm font-semibold">
              Senha
            </label>
            <Link href="/recuperar-senha" className="text-xs font-semibold text-primary transition hover:underline">
              Esqueci minha senha
            </Link>
          </div>
          <div className="relative">
            <input id="password" name="password" type={show ? "text" : "password"} autoComplete="current-password" required className={`${inputCls} pr-11`} aria-invalid={Boolean(state?.errors?.password)} />
            <button
              type="button"
              onClick={() => setShow((v) => !v)}
              aria-label={show ? "Ocultar a senha" : "Mostrar a senha"}
              aria-pressed={show}
              className="absolute right-1.5 top-1/2 flex h-8 w-8 -translate-y-1/2 cursor-pointer items-center justify-center rounded-lg text-muted transition hover:bg-surface-3/70 hover:text-text"
            >
              {show ? <EyeOff className="h-4 w-4" aria-hidden /> : <Eye className="h-4 w-4" aria-hidden />}
            </button>
          </div>
          {state?.errors?.password?.map((e) => (
            <span key={e} className="block text-xs font-medium text-primary">
              {e}
            </span>
          ))}
        </div>
        <Button type="submit" size="lg" disabled={pending} className="w-full">
          {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <LogIn className="h-5 w-5" aria-hidden />}
          {pending ? "Entrando…" : "Entrar"}
        </Button>
      </form>

      <div className="space-y-3 border-t border-dashed border-border-strong pt-6">
        <p className="text-center text-sm text-muted">Ainda não tem conta?</p>
        <LinkButton href="/concursos" variant="secondary" size="lg" className="w-full">
          Criar conta
        </LinkButton>
      </div>
    </div>
  );
}
