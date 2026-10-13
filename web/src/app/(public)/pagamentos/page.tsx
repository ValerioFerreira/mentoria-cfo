import type { Metadata } from "next";
import Link from "next/link";
import { redirect } from "next/navigation";
import { ActionForm } from "@/components/action-form";
import { PriceCard } from "@/components/price-card";
import { Alert, Badge, Button, Card, Field, PageHeader, inputCls } from "@/components/ui";
import { cancelMonthlySubscription } from "@/lib/billing/actions";
import { getCurrentUser } from "@/lib/auth/session";
import { startContract } from "@/lib/commerce/customer-actions";
import { CONTRACT_STATUS, contestName, dateBR, dayBR } from "@/lib/commerce/labels";
import { formatBRL, toCents } from "@/lib/commerce/money";
import { CATEGORY_LABEL, priceCardText, quote } from "@/lib/commerce/pricing";
import { CONTESTS } from "@/lib/contests";
import { db } from "@/lib/db";

export const metadata: Metadata = { title: "Contratações e pagamentos" };

const LEGACY_STATUS: Record<string, { label: string; tone: "ok" | "warn" | "neutral" }> = {
  PENDING: { label: "Aguardando pagamento", tone: "warn" },
  ACTIVE: { label: "Ativo", tone: "ok" },
  PAST_DUE: { label: "Pagamento pendente", tone: "warn" },
  CANCELLED: { label: "Cancelado", tone: "neutral" },
  EXPIRED: { label: "Encerrado", tone: "neutral" },
  REFUNDED: { label: "Estornado", tone: "neutral" },
  CHARGEBACK: { label: "Em contestação", tone: "warn" },
};

export default async function BillingPage({ searchParams }: { searchParams: Promise<{ status?: string }> }) {
  const query = await searchParams;
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  // a página é de quem contrata acesso; parceiro não contrata nem paga
  if (user.isPartner) redirect("/parceria");
  const [contracts, legacy, settings] = await Promise.all([
    db.contract.findMany({
      where: { OR: [{ userId: user.id }, { customerEmail: user.email.toLowerCase() }], status: { not: "CANCELLED" } },
      orderBy: { createdAt: "desc" },
    }),
    db.billingPurchase.findMany({ where: { userId: user.id }, orderBy: { createdAt: "desc" } }),
    db.contestSetting.findMany(),
  ]);
  const settingOf = new Map(settings.map((s) => [s.contest, s]));
  const taken = new Set(contracts.map((c) => c.contest));
  const offers = CONTESTS.filter((c) => c.available && !taken.has(c.key))
    .map((c) => ({ c, category: settingOf.get(c.key)?.category ?? null }))
    .filter((o): o is { c: (typeof CONTESTS)[number]; category: NonNullable<typeof o.category> } => o.category !== null);
  // assinatura mensal antiga ainda ativa: só o cancelamento continua disponível (não há novas adesões mensais)
  const monthly = legacy.find((p) => p.product === "MONTHLY" && p.mpPreapprovalId && ["ACTIVE", "PENDING", "PAST_DUE"].includes(p.status));
  const sample = offers[0] ? quote(offers[0].category) : null;

  return (
    <div className="space-y-7">
      <PageHeader eyebrow="Conta" title="Contratações e pagamentos" description="Acesso ilimitado até a data da prova, com pagamento único e sem mensalidade." />
      {query.status === "acesso-expirado" && <Alert tone="warn">Seu acesso expirou. Confira abaixo a situação das suas contratações.</Alert>}

      <section className="space-y-3" aria-labelledby="minhas">
        <h2 id="minhas" className="font-display text-lg font-bold uppercase">Minhas contratações</h2>
        {contracts.length === 0 ? (
          <Card tone="soft"><p className="text-sm text-muted">Nenhuma contratação registrada nesta conta.</p></Card>
        ) : (
          <div className="grid gap-3 md:grid-cols-2">
            {contracts.map((c) => {
              const due = toCents(c.finalAmount);
              const paid = toCents(c.paidAmount);
              const st = CONTRACT_STATUS[c.status];
              return (
                <Card key={c.id} className="space-y-3">
                  <div className="flex flex-wrap items-start justify-between gap-2">
                    <div>
                      <p className="font-display text-xl font-bold uppercase leading-tight">{contestName(c.contest)}</p>
                      <p className="text-xs text-muted">Contratado em {dateBR(c.createdAt)} · {CATEGORY_LABEL[c.category]}</p>
                    </div>
                    <Badge tone={st.tone}>{st.label}</Badge>
                  </div>
                  <dl className="grid grid-cols-3 gap-2 text-sm">
                    <div><dt className="text-xs text-muted">Valor</dt><dd className="font-semibold tabular">{formatBRL(due)}</dd></div>
                    <div><dt className="text-xs text-muted">Recebido</dt><dd className="font-semibold tabular">{formatBRL(paid)}</dd></div>
                    <div><dt className="text-xs text-muted">Saldo</dt><dd className="font-semibold tabular">{formatBRL(Math.max(0, due - paid))}</dd></div>
                  </dl>
                  <p className="text-xs text-muted">
                    {c.accessGrantedAt ? `Acesso liberado até ${dateBR(c.accessUntil)} (dia da prova).` : "O acesso é liberado pela administração após a confirmação do pagamento."}
                    {c.couponCode ? ` Cupom ${c.couponCode}.` : ""}
                  </p>
                  {due - paid > 0 && (
                    <Link href={`/pagamentos/contratacao/${c.id}`} className="inline-block text-sm font-semibold text-primary underline">
                      Pagar
                    </Link>
                  )}
                </Card>
              );
            })}
          </div>
        )}
      </section>

      {offers.length > 0 && sample && (
        <section className="space-y-3" aria-labelledby="contratar">
          <h2 id="contratar" className="font-display text-lg font-bold uppercase">Contratar acesso a outro concurso</h2>
          <ActionForm action={startContract} submitLabel="Contratar e pagar" pendingLabel="Registrando…" resetOnSuccess={false} className="space-y-4">
            <fieldset className="grid gap-3 sm:grid-cols-2">
              <legend className="mb-2 text-sm font-semibold">Concurso</legend>
              {offers.map(({ c, category }, i) => {
                const q = quote(category);
                return (
                  <PriceCard
                    key={c.key}
                    data={{ badge: priceCardText(q).badge, originalCents: q.originalCents, finalCents: q.finalCents }}
                    radio={{ name: "contest", value: c.key, defaultChecked: i === 0 }}
                    footer={
                      <span className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">
                        {contestName(c.key)}
                        {settingOf.get(c.key)?.examDate ? ` · prova em ${dayBR(settingOf.get(c.key)!.examDate)}` : " · data da prova a confirmar"}
                      </span>
                    }
                  />
                );
              })}
            </fieldset>
            <Field label="Cupom de parceiro (opcional)" hint="O desconto é calculado no servidor e aparece no valor a pagar.">
              <input name="coupon" type="text" autoComplete="off" maxLength={20} className={`${inputCls} max-w-xs uppercase`} />
            </Field>
          </ActionForm>
        </section>
      )}

      {monthly && (
        <Card className="space-y-3">
          <div className="flex items-center justify-between gap-3">
            <h2 className="font-display text-lg font-bold uppercase">Assinatura mensal (plano antigo)</h2>
            <Badge tone={LEGACY_STATUS[monthly.status]?.tone ?? "neutral"}>{LEGACY_STATUS[monthly.status]?.label ?? monthly.status}</Badge>
          </div>
          <p className="text-sm text-muted">A mensalidade não é mais oferecida. Você pode cancelar a recorrência a qualquer momento.</p>
          <form action={cancelMonthlySubscription}>
            <input type="hidden" name="purchaseId" value={monthly.id} />
            <Button type="submit" variant="secondary" size="sm">Cancelar assinatura</Button>
          </form>
        </Card>
      )}

      {legacy.length > 0 && (
        <section className="space-y-2" aria-labelledby="historico">
          <h2 id="historico" className="font-display text-lg font-bold uppercase">Histórico (Mercado Pago)</h2>
          {legacy.map((p) => (
            <Card key={p.id} className="flex flex-wrap items-center justify-between gap-3 p-4">
              <div>
                <p className="font-semibold">{p.product === "MONTHLY" ? "Mensal" : "Acesso permanente"} · {formatBRL(toCents(p.amount))}</p>
                <p className="text-xs text-muted">{dateBR(p.createdAt)}</p>
              </div>
              <Badge tone={LEGACY_STATUS[p.status]?.tone ?? "neutral"}>{LEGACY_STATUS[p.status]?.label ?? p.status}</Badge>
            </Card>
          ))}
        </section>
      )}
    </div>
  );
}
