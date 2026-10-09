"use client";

import { Check, CircleAlert, Copy, Loader2, Send } from "lucide-react";
import Image from "next/image";
import { useActionState, useRef, useState } from "react";
import { Star } from "@/components/brand";
import { RouteNavigationTrap } from "@/components/route-navigation-trap";
import { Alert, Button, Card, Field, inputCls } from "@/components/ui";
import { WAITLIST_PLANS } from "@/lib/plans";
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
      <PlanChoice error={state?.errors?.plan} />
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

/* O radio nativo fica escondido (sr-only) e o card inteiro é o rótulo: teclado e leitor de tela funcionam como num radio comum. */
const RADIO_DOT = "absolute right-4 top-4 grid h-6 w-6 place-items-center rounded-full border-2 transition";
const FOCUS = "has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-offset-2 has-[:focus-visible]:outline-primary";

function PlanChoice({ error }: { error?: string[] }) {
  const until = WAITLIST_PLANS.UNTIL_EXAM;
  const monthly = WAITLIST_PLANS.MONTHLY;
  return (
    <fieldset className="space-y-2">
      <legend className="text-sm font-semibold">Escolha o seu plano</legend>
      <div className="grid gap-3 sm:grid-cols-5">
        {/* oferta em destaque */}
        <label
          className={`group relative flex cursor-pointer flex-col gap-4 overflow-hidden rounded-2xl border border-gold/60 bg-ink p-5 pt-6 text-on-ink shadow-lift transition hover:-translate-y-0.5 has-[:checked]:ring-2 has-[:checked]:ring-gold sm:col-span-3 ${FOCUS}`}
        >
          <input type="radio" name="plan" value={until.key} defaultChecked className="sr-only" />
          <div className="tape tape-rule absolute inset-x-0 top-0 !rounded-none" aria-hidden />
          <span className={`${RADIO_DOT} border-on-ink-muted group-has-[:checked]:border-gold group-has-[:checked]:bg-gold`} aria-hidden>
            <Check className="h-3.5 w-3.5 text-ink opacity-0 transition group-has-[:checked]:opacity-100" />
          </span>
          <span className="inline-flex w-fit items-center gap-1.5 rounded-full bg-gold px-2.5 py-1 text-xs font-bold text-ink">
            <Star className="h-3 w-3" />
            Melhor oferta
          </span>
          <span className="space-y-1">
            <span className="block font-display text-2xl font-bold uppercase leading-none">{until.name}</span>
            <span className="flex items-baseline gap-1.5">
              <span className="font-display text-xl font-semibold text-gold">R$</span>
              <span className="tabular font-display text-6xl font-bold leading-none">{until.price.split(",")[0]}</span>
              <span className="text-sm font-semibold text-on-ink-muted">pagamento único</span>
            </span>
          </span>
          <span className="space-y-1 text-sm text-on-ink-muted">
            <span className="block">Acesso liberado até o dia da prova, sem nenhuma mensalidade.</span>
            <span className="block font-semibold text-gold">Menos que o valor de 3 mensalidades.</span>
          </span>
        </label>

        {/* mensalidade */}
        <label
          className={`group relative flex cursor-pointer flex-col gap-4 rounded-2xl border border-border bg-surface p-5 shadow-card transition hover:border-border-strong has-[:checked]:border-primary has-[:checked]:ring-2 has-[:checked]:ring-primary/40 sm:col-span-2 ${FOCUS}`}
        >
          <input type="radio" name="plan" value={monthly.key} className="sr-only" />
          <span className={`${RADIO_DOT} border-border-strong group-has-[:checked]:border-primary group-has-[:checked]:bg-primary`} aria-hidden>
            <Check className="h-3.5 w-3.5 text-on-primary opacity-0 transition group-has-[:checked]:opacity-100" />
          </span>
          <span className="space-y-1 pt-1 sm:pt-9">
            <span className="block font-display text-2xl font-bold uppercase leading-none">{monthly.name}</span>
            <span className="flex items-baseline gap-1.5">
              <span className="font-display text-xl font-semibold text-muted">R$</span>
              <span className="tabular font-display text-5xl font-bold leading-none">{monthly.price.split(",")[0]}</span>
              <span className="text-sm font-semibold text-muted">por mês</span>
            </span>
          </span>
          <span className="text-sm text-muted">Pague mês a mês.</span>
        </label>
      </div>
      {error?.map((e) => (
        <p key={e} className="text-xs font-medium text-primary">
          {e}
        </p>
      ))}
    </fieldset>
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
    <Card className="space-y-6">
      <RouteNavigationTrap targetUrl="/concursos" />
      <div className="space-y-2">
        {p.alreadyJoined && <p className="eyebrow">Você já está na lista</p>}
        <h2 className="font-display text-5xl font-bold uppercase leading-none">Falta pouco!</h2>
        <p className="text-sm leading-relaxed text-muted">
          Efetue o pagamento via PIX, usando o QR Code ou o código copia e cola. <strong className="text-text">Não altere a mensagem do PIX:</strong> Ela contém o e-mail que será utilizado pela plataforma para confirmar seu acesso!
        </p>
      </div>
      <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-1 rounded-xl bg-surface-2 px-4 py-3">
        <p className="text-sm font-semibold">{p.plan}</p>
        <p className="tabular font-display text-3xl font-bold leading-none">R$ {p.amount}</p>
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
          <p className="text-xs text-muted">
            E-mail na mensagem do Pix: <strong className="break-all text-text">{p.email}</strong>
          </p>
        </div>
      </div>
      <p className="border-t border-dashed border-border-strong pt-4 text-sm text-muted">Assim que seu pagamento for confirmado, você receberá no seu e-mail as credenciais de acesso à plataforma.</p>
    </Card>
  );
}
