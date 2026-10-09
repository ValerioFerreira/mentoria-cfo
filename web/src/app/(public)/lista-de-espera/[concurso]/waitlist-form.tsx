"use client";

import { Check, CircleAlert, Copy, Loader2, Send } from "lucide-react";
import Image from "next/image";
import { useActionState, useRef, useState } from "react";
import { Alert, Button, Card, Field, inputCls } from "@/components/ui";
import { checkUsername, joinWaitlist, type UsernameCheck } from "./actions";

export function WaitlistForm({ slug }: { slug: string }) {
  const [state, action, pending] = useActionState(joinWaitlist.bind(null, slug), undefined);
  const [username, setUsername] = useState("");
  const [check, setCheck] = useState<UsernameCheck | null>(null);
  const [checking, setChecking] = useState(false);
  const seq = useRef(0);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);

  // valida o nome de usuário enquanto a pessoa digita (com pequena espera entre as teclas)
  function onUsername(raw: string) {
    const value = raw.toLowerCase().replace(/\s/g, "");
    setUsername(value);
    if (timer.current) clearTimeout(timer.current);
    const id = ++seq.current;
    if (value.length === 0) {
      setCheck(null);
      setChecking(false);
      return;
    }
    setChecking(true);
    timer.current = setTimeout(async () => {
      const r = await checkUsername(value);
      if (id === seq.current) {
        setCheck(r);
        setChecking(false);
      }
    }, 350);
  }

  if (state?.payment) return <Payment p={state.payment} />;

  const usernameError = state?.errors?.username ?? (check && !check.available && !checking ? [check.message] : undefined);
  return (
    <form action={action} className="space-y-5">
      {state?.message && <Alert tone="danger">{state.message}</Alert>}
      <Field label="Nome completo" error={state?.errors?.name}>
        <input name="name" type="text" autoComplete="name" required minLength={5} maxLength={120} className={inputCls} />
      </Field>
      <Field label="E-mail" error={state?.errors?.email} hint="Ele vai na mensagem do Pix para identificarmos o seu pagamento.">
        <input name="email" type="email" autoComplete="email" required maxLength={60} className={inputCls} />
      </Field>
      <Field label="Nome de usuário" error={usernameError} hint={checking ? "Verificando…" : check?.available ? undefined : "De 3 a 20 caracteres: letras minúsculas, números, ponto, hífen ou sublinhado."}>
        <div className="relative">
          <input
            name="username"
            type="text"
            autoComplete="username"
            required
            maxLength={20}
            value={username}
            onChange={(e) => onUsername(e.target.value)}
            className={`${inputCls} pr-10`}
            aria-invalid={Boolean(usernameError)}
          />
          <span className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2" aria-hidden>
            {checking ? <Loader2 className="h-4 w-4 animate-spin text-muted" /> : check?.available ? <Check className="h-4 w-4 text-ok" /> : check ? <CircleAlert className="h-4 w-4 text-primary" /> : null}
          </span>
        </div>
        {check?.available && !checking && <p className="mt-1 text-xs font-semibold text-ok">{check.message}</p>}
      </Field>
      <Button type="submit" size="lg" disabled={pending || checking || (check !== null && !check.available)} className="w-full">
        {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <Send className="h-5 w-5" aria-hidden />}
        {pending ? "Enviando…" : "Entrar na lista de espera"}
      </Button>
    </form>
  );
}

function Payment({ p }: { p: NonNullable<NonNullable<Awaited<ReturnType<typeof joinWaitlist>>>["payment"]> }) {
  const [copied, setCopied] = useState(false);
  async function copy() {
    try {
      await navigator.clipboard.writeText(p.payload);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      /* sem permissão de área de transferência: a pessoa seleciona o código manualmente */
    }
  }
  return (
    <Card className="space-y-5">
      <div className="space-y-1">
        <p className="eyebrow">{p.alreadyJoined ? "Você já está na lista" : "Cadastro recebido"}</p>
        <h2 className="font-display text-3xl font-bold uppercase leading-none">Falta o pagamento</h2>
        <p className="text-sm text-muted">
          Pague por Pix para garantir a sua vaga{p.amount ? ` (R$ ${p.amount.replace(".", ",")})` : ""}. Use o QR Code ou o código copia e cola. A mensagem do Pix já leva o seu e-mail
          (<strong className="break-all text-text">{p.email}</strong>): <strong className="text-text">não altere a mensagem</strong>, é ela que nos mostra de quem é o pagamento.
        </p>
      </div>
      <div className="flex flex-col items-center gap-5 sm:flex-row sm:items-start">
        <Image src={p.qr} alt="QR Code do Pix" width={208} height={208} unoptimized className="h-52 w-52 shrink-0 rounded-xl border border-border bg-white p-1.5" />
        <div className="min-w-0 flex-1 space-y-3">
          <p className="text-xs font-semibold uppercase tracking-wider text-muted">Pix copia e cola</p>
          <textarea readOnly value={p.payload} rows={5} className={`${inputCls} resize-none break-all font-mono text-[11px] leading-snug`} onFocus={(e) => e.currentTarget.select()} aria-label="Código Pix copia e cola" />
          <Button type="button" variant={copied ? "secondary" : "primary"} onClick={copy} className="w-full sm:w-auto">
            {copied ? <Check className="h-4 w-4 text-ok" aria-hidden /> : <Copy className="h-4 w-4" aria-hidden />}
            {copied ? "Código copiado" : "Copiar código Pix"}
          </Button>
        </div>
      </div>
      <p className="text-xs text-muted">Depois que o pagamento for conferido, enviaremos para esse e-mail o convite para criar a sua conta.</p>
    </Card>
  );
}
