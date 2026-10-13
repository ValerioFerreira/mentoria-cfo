"use client";

import { AlertTriangle, Check, CheckCircle2, CircleAlert, Clock, Copy, Loader2, Send, ShieldCheck, X } from "lucide-react";
import Image from "next/image";
import { useActionState, useRef, useState } from "react";
import { PriceCard, type PriceCardData } from "@/components/price-card";
import { RouteNavigationTrap } from "@/components/route-navigation-trap";
import { Alert, Button, Card, Field, inputCls } from "@/components/ui";
import { checkUsername, joinWaitlist, type PaymentInfo, type UsernameCheck } from "./actions";

export function WaitlistForm({ slug, card, examDateKnown }: { slug: string; card: PriceCardData; examDateKnown: boolean }) {
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
      <fieldset className="space-y-2">
        <legend className="text-sm font-semibold">Seu acesso</legend>
        <PriceCard data={card} radio={{ name: "offer", value: "UNTIL_EXAM", defaultChecked: true }} />
        {!examDateKnown && <p className="text-xs text-muted">A data oficial da prova deste concurso ainda será confirmada; o acesso vale até ela.</p>}
      </fieldset>
      <Field label="Cupom de parceiro (opcional)" error={state?.errors?.coupon} hint="Tem um cupom? O desconto é aplicado sobre o preço original e confirmado no valor do Pix.">
        <input name="coupon" type="text" autoComplete="off" maxLength={20} className={`${inputCls} uppercase`} />
      </Field>
      <RefundNotice />
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
        {pending ? "Gerando Pix…" : "Gerar Pix para Pagamento"}
      </Button>
    </form>
  );
}

function RefundNotice() {
  return (
    <aside className="flex gap-3 rounded-2xl border border-ok/30 bg-ok/5 p-4" aria-label="Garantia de 7 dias">
      <ShieldCheck className="mt-0.5 h-5 w-5 shrink-0 text-ok" aria-hidden />
      <div className="space-y-1">
        <h2 className="font-display text-lg font-bold">E se você não gostar da plataforma?</h2>
        <p className="text-sm leading-relaxed text-muted">Você tem até 7 dias para testar a plataforma, e se desistir do acesso, devolvemos seu dinheiro!</p>
      </div>
    </aside>
  );
}

function Payment({ p }: { p: PaymentInfo }) {
  const [copied, setCopied] = useState(false);
  const [showModal, setShowModal] = useState(false);

  async function copy() {
    try {
      await navigator.clipboard.writeText(p.payload);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      /* sem permissão de área de transferência */
    }
  }

  return (
    <Card className="space-y-6">
      <RouteNavigationTrap targetUrl="/concursos" />
      <div className="space-y-2">
        {p.alreadyJoined && <p className="eyebrow">Inscrição já realizada</p>}
        <h2 className="font-display text-5xl font-bold uppercase leading-none">Falta pouco!</h2>
        <p className="text-sm leading-relaxed text-muted">
          Efetue o pagamento via PIX pelo QR Code ou pelo código copia e cola abaixo.
        </p>
      </div>

      <RefundNotice />

      <div className="rounded-xl border border-amber-500/30 bg-amber-500/10 p-4 space-y-1.5 text-xs leading-relaxed text-amber-950 dark:text-amber-100">
        <p className="font-bold text-sm text-amber-700 dark:text-amber-400 flex items-center gap-1.5">
          <AlertTriangle className="h-4 w-4" /> Atenção!
        </p>
        <p>
          A plataforma possui conteúdo próprio, mas baseia o planejamento de estudos no material do <strong>Estratégia Concursos</strong>. Para extrair o máximo da nossa plataforma, recomendamos que você faça seu cadastro assim que tiver acesso ao material.
        </p>
      </div>

      <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-1 rounded-xl bg-surface-2 px-4 py-3">
        <div>
          <p className="text-sm font-semibold">{p.plan}</p>
          <p className="text-xs text-muted">
            <span className="line-through">De {p.original}</span> · {p.discounts}
          </p>
        </div>
        <p className="tabular font-display text-3xl font-bold leading-none">R$ {p.amount}</p>
      </div>

      <div className="flex flex-col items-center gap-5 sm:flex-row sm:items-start">
        <Image src={p.qr} alt="QR Code do Pix" width={208} height={208} unoptimized className="h-52 w-52 shrink-0 rounded-xl border border-border bg-white p-1.5" />
        <div className="min-w-0 flex-1 space-y-3">
          <p className="text-xs font-semibold uppercase tracking-wider text-muted">Pix copia e cola</p>
          <textarea readOnly value={p.payload} rows={5} className={`${inputCls} resize-none break-all font-mono text-[11px] leading-snug`} onFocus={(e) => e.currentTarget.select()} aria-label="Código Pix copia e cola" />
          <div className="flex flex-wrap gap-2.5">
            <Button type="button" variant={copied ? "secondary" : "primary"} onClick={copy} className="w-full sm:w-auto">
              {copied ? <Check className="h-4 w-4 text-ok" aria-hidden /> : <Copy className="h-4 w-4" aria-hidden />}
              {copied ? "Código copiado" : "Copiar código Pix"}
            </Button>
            <Button type="button" variant="secondary" onClick={() => setShowModal(true)} className="w-full sm:w-auto">
              <CheckCircle2 className="h-4 w-4 text-ok" aria-hidden />
              Confirmar pagamento
            </Button>
          </div>
        </div>
      </div>
      <p className="border-t border-dashed border-border-strong pt-4 text-sm text-muted">
        Assim que seu pagamento for confirmado pela administração, você receberá no seu e-mail as credenciais de acesso com a sua senha temporária.
      </p>

      {showModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm"
          role="dialog"
          aria-modal="true"
          aria-labelledby="pix-modal-title"
        >
          <div className="relative w-full max-w-md rounded-2xl border border-border bg-surface p-6 shadow-lift space-y-4">
            <button
              type="button"
              onClick={() => setShowModal(false)}
              className="absolute right-4 top-4 rounded-lg p-1.5 text-muted transition hover:bg-surface-2 hover:text-text cursor-pointer"
              aria-label="Fechar"
            >
              <X className="h-5 w-5" />
            </button>

            <div className="flex items-center gap-3">
              <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-ok/15 text-ok">
                <Clock className="h-6 w-6" />
              </span>
              <div>
                <p className="eyebrow text-ok">Solicitação Confirmada</p>
                <h3 id="pix-modal-title" className="font-display text-xl font-bold uppercase">
                  Pagamento em Análise
                </h3>
              </div>
            </div>

            <div className="space-y-3 text-sm leading-relaxed text-muted">
              <p>
                A sua solicitação foi confirmada e o comprovante está sendo verificado pela nossa equipe.
              </p>
              <div className="rounded-xl border border-ok/30 bg-ok/10 p-3.5 text-xs text-text space-y-1">
                <p className="font-semibold text-ok flex items-center gap-1.5">
                  <Check className="h-4 w-4" /> Liberação em até 1 hora
                </p>
                <p className="text-muted leading-relaxed">
                  Em até <strong>1 hora</strong> você receberá um e-mail de confirmação contendo o seu login e as instruções de acesso ao MentorIA.
                </p>
              </div>
            </div>

            <Button type="button" variant="primary" onClick={() => setShowModal(false)} className="w-full">
              Entendi, vou aguardar o e-mail
            </Button>
          </div>
        </div>
      )}
    </Card>
  );
}
