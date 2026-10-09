"use client";

import { Eye, EyeOff, KeyRound, Loader2 } from "lucide-react";
import { useActionState, useState } from "react";
import { Alert, Button, inputCls } from "@/components/ui";
import { changePassword } from "../actions";

export function ChangePasswordForm() {
  const [state, action, pending] = useActionState(changePassword, undefined);
  const [show, setShow] = useState(false);

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="font-display text-4xl font-bold uppercase leading-none sm:text-5xl">Trocar Senha</h1>
        <p className="text-sm text-muted">
          Cadastre uma nova senha pessoal definitiva para continuar navegando no MentorIA.
        </p>
      </div>

      <div className="rounded-xl border border-primary/20 bg-primary-soft p-3 text-xs leading-relaxed text-text">
        <strong>Atenção:</strong> Você entrou com uma senha temporária. Para a sua segurança, defina uma nova senha de no mínimo 8 caracteres.
      </div>

      <form action={action} className="space-y-5">
        {state?.message && <Alert tone="danger">{state.message}</Alert>}

        <div className="space-y-1.5">
          <label htmlFor="password" className="block text-sm font-semibold">
            Nova Senha
          </label>
          <div className="relative">
            <input
              id="password"
              name="password"
              type={show ? "text" : "password"}
              autoComplete="new-password"
              required
              minLength={8}
              placeholder="No mínimo 8 caracteres"
              className={`${inputCls} pr-11`}
              aria-invalid={Boolean(state?.errors?.password)}
            />
            <button
              type="button"
              onClick={() => setShow((v) => !v)}
              aria-label={show ? "Ocultar senha" : "Ver senha"}
              className="absolute right-1.5 top-1/2 flex h-8 w-8 -translate-y-1/2 cursor-pointer items-center justify-center rounded-lg text-muted transition hover:bg-surface-3/70 hover:text-text"
            >
              {show ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
            </button>
          </div>
          {state?.errors?.password?.map((e) => (
            <span key={e} className="block text-xs font-medium text-primary">
              {e}
            </span>
          ))}
        </div>

        <div className="space-y-1.5">
          <label htmlFor="confirmPassword" className="block text-sm font-semibold">
            Confirmar Nova Senha
          </label>
          <input
            id="confirmPassword"
            name="confirmPassword"
            type={show ? "text" : "password"}
            autoComplete="new-password"
            required
            minLength={8}
            placeholder="Repita a nova senha"
            className={inputCls}
            aria-invalid={Boolean(state?.errors?.confirmPassword)}
          />
          {state?.errors?.confirmPassword?.map((e) => (
            <span key={e} className="block text-xs font-medium text-primary">
              {e}
            </span>
          ))}
        </div>

        <Button type="submit" size="lg" disabled={pending} className="w-full">
          {pending ? <Loader2 className="h-5 w-5 animate-spin" /> : <KeyRound className="h-5 w-5" />}
          {pending ? "Salvando nova senha…" : "Salvar e Continuar"}
        </Button>
      </form>
    </div>
  );
}
