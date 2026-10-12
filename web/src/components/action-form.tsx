"use client";

import { Loader2 } from "lucide-react";
import { startTransition, useActionState, useRef, type FormEvent, type ReactNode } from "react";
import { Button } from "@/components/ui";
import type { ActionResult } from "@/lib/commerce/errors";

type Action = (prev: ActionResult | null, fd: FormData) => Promise<ActionResult>;

/**
 * Formulário de server action com retorno na tela. Não limpa os campos quando há erro (o administrador corrige
 * e reenvia); limpa após o sucesso. `confirmText` pede confirmação antes de operações sensíveis.
 */
export function ActionForm({
  action,
  children,
  submitLabel,
  pendingLabel = "Salvando…",
  className,
  submitVariant = "primary",
  submitSize = "md",
  confirmText,
  resetOnSuccess = true,
}: {
  action: Action;
  children?: ReactNode;
  submitLabel: string;
  pendingLabel?: string;
  className?: string;
  submitVariant?: "primary" | "secondary" | "ghost" | "danger" | "ink";
  submitSize?: "sm" | "md" | "lg";
  confirmText?: string;
  resetOnSuccess?: boolean;
}) {
  const ref = useRef<HTMLFormElement>(null);
  const [state, run, pending] = useActionState(async (prev: ActionResult | null, fd: FormData) => {
    const r = await action(prev, fd);
    if (r.ok && resetOnSuccess) ref.current?.reset();
    return r;
  }, null);

  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (pending) return;
    if (confirmText && !window.confirm(confirmText)) return;
    const fd = new FormData(e.currentTarget);
    startTransition(() => run(fd));
  }

  return (
    <form ref={ref} onSubmit={onSubmit} className={className ?? "space-y-3"}>
      {children}
      <div className="flex flex-wrap items-center gap-3">
        <Button type="submit" disabled={pending} variant={submitVariant} size={submitSize}>
          {pending && <Loader2 className="h-4 w-4 animate-spin" aria-hidden />}
          {pending ? pendingLabel : submitLabel}
        </Button>
        {state && (
          <p role="status" className={`text-sm font-medium ${state.ok ? "text-ok" : "text-primary"}`}>
            {state.message}
          </p>
        )}
      </div>
    </form>
  );
}
