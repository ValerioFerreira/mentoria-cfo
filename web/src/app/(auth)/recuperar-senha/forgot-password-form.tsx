"use client";

import { ArrowLeft, CheckCircle2, Loader2, Mail } from "lucide-react";
import Link from "next/link";
import { useActionState } from "react";
import { Alert, Button, Field, LinkButton, inputCls } from "@/components/ui";
import { requestPasswordReset } from "../actions";

export function ForgotPasswordForm() {
  const [state, action, pending] = useActionState(requestPasswordReset, undefined);

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="font-display text-4xl font-bold uppercase leading-none sm:text-5xl">Recuperar Senha</h1>
        <p className="text-sm text-muted">
          Informe seu e-mail cadastrado para receber uma nova senha temporária.
        </p>
      </div>

      {state?.success ? (
        <div className="space-y-6">
          <div className="flex items-start gap-3 rounded-2xl border border-ok/30 bg-ok-soft p-4 text-sm text-text">
            <CheckCircle2 className="h-5 w-5 shrink-0 text-ok" />
            <p className="leading-relaxed">{state.message}</p>
          </div>
          <p className="text-xs text-muted leading-relaxed">
            Abra a mensagem recebida, copie a senha temporária e entre na plataforma. No primeiro acesso com ela, você poderá cadastrar sua nova senha pessoal.
          </p>
          <LinkButton href="/login" size="lg" className="w-full">
            Ir para o Login
          </LinkButton>
        </div>
      ) : (
        <form action={action} className="space-y-5">
          {state?.message && <Alert tone="danger">{state.message}</Alert>}

          <Field label="E-mail Cadastrado" error={state?.errors?.email}>
            <input
              name="email"
              type="email"
              autoComplete="email"
              required
              placeholder="seu-email@exemplo.com"
              className={inputCls}
            />
          </Field>

          <Button type="submit" size="lg" disabled={pending} className="w-full">
            {pending ? <Loader2 className="h-5 w-5 animate-spin" /> : <Mail className="h-5 w-5" />}
            {pending ? "Enviando…" : "Enviar Senha Temporária"}
          </Button>

          <div className="text-center pt-2">
            <Link
              href="/login"
              className="inline-flex items-center gap-1.5 text-xs font-semibold text-muted transition hover:text-text"
            >
              <ArrowLeft className="h-3.5 w-3.5" />
              Lembrou a senha? Voltar ao login
            </Link>
          </div>
        </form>
      )}
    </div>
  );
}
