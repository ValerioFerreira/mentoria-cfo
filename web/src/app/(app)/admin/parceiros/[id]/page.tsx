import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ActionForm } from "@/components/action-form";
import { Badge, Card, Field, PageHeader, Stat, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import {
  adminRegisterPayout,
  adminReplaceCoupon,
  adminResetPartnerPassword,
  adminSetCouponActive,
  adminSetPartnerActive,
  adminUpdatePartner,
} from "@/lib/commerce/admin-actions";
import { newIdempotencyKey } from "@/lib/commerce/keys";
import { AUDIT_LABEL, CONTRACT_STATUS, PAYMENT_METHOD_LABEL, contestName, dateBR } from "@/lib/commerce/labels";
import { formatBRL, toCents } from "@/lib/commerce/money";
import { MIN_PARTNER_PASSWORD } from "@/lib/commerce/partners";
import { partnerAdminDetail } from "@/lib/commerce/queries";
import { todayISO } from "@/lib/plan-time";
import { FilterBar } from "../../financeiro/filter-bar";
import { parseFilters, type SearchParams } from "../../financeiro/filters";

export const metadata: Metadata = { title: "Parceiro" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function PartnerAdminPage({ params, searchParams }: { params: Promise<{ id: string }>; searchParams: Promise<SearchParams> }) {
  await requireAdmin();
  const { id } = await params;
  const f = parseFilters(await searchParams);
  const d = await partnerAdminDetail(id, f);
  if (!d) notFound();
  const { partner: p, balance: b } = d;
  const today = todayISO();
  const activeCoupon = p.coupons.find((c) => c.active);
  const payingEmails = new Set(d.contracts.filter((c) => toCents(c.paidAmount) > 0).map((c) => c.customerEmail));

  return (
    <div className="space-y-6">
      <Link href="/admin/parceiros" className="text-sm font-semibold text-muted underline">← Parceiros</Link>
      <PageHeader
        eyebrow={`Parceiro desde ${dateBR(p.createdAt)}`}
        title={p.user.name ?? p.user.username ?? p.user.email}
        description={`@${p.user.username ?? "—"} · ${p.user.email}`}
        actions={
          <>
            <Badge tone={p.active ? "ok" : "neutral"}>{p.active ? "Ativo" : `Desativado em ${dateBR(p.deactivatedAt)}`}</Badge>
            {activeCoupon && <Badge tone="gold">Cupom {activeCoupon.code}</Badge>}
          </>
        }
      />

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
        <Stat label="Comissões geradas" value={formatBRL(b.generatedCents)} />
        <Stat label="Revertidas" value={formatBRL(b.reversedCents)} />
        <Stat label="Repassado" value={formatBRL(b.paidOutCents)} />
        <Stat label="Disponível" value={formatBRL(b.availableCents)} />
        <Stat label="Pendente (garantia)" value={formatBRL(b.pendingCents)} />
        <Stat label="A compensar" value={formatBRL(b.negativeCents)} />
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <Card className="space-y-3">
          <h2 className="font-display text-lg font-bold uppercase">Registrar repasse</h2>
          <p className="text-sm text-muted">Informe um repasse já pago ao parceiro (sem transferência automática). Limite: saldo disponível de {formatBRL(b.availableCents)}.</p>
          <ActionForm action={adminRegisterPayout} submitLabel="Registrar repasse" confirmText="Confirmar o registro deste repasse?" className="grid gap-3 sm:grid-cols-2">
            <input type="hidden" name="partnerId" value={p.id} />
            <input type="hidden" name="idempotencyKey" value={newIdempotencyKey()} />
            <Field label="Valor pago (R$)"><input name="amount" inputMode="decimal" required className={inputCls} /></Field>
            <Field label="Data efetiva"><input name="paidAt" type="date" required max={today} defaultValue={today} className={inputCls} /></Field>
            <Field label="Forma ou referência"><input name="method" required maxLength={120} placeholder="Pix, transferência…" className={inputCls} /></Field>
            <Field label="Comprovante (identificador)"><input name="receiptRef" maxLength={120} className={inputCls} /></Field>
            <div className="sm:col-span-2"><Field label="Observação (opcional)"><input name="note" maxLength={500} className={inputCls} /></Field></div>
          </ActionForm>
        </Card>

        <Card className="space-y-4">
          <h2 className="font-display text-lg font-bold uppercase">Conta e cupom</h2>
          <ActionForm action={adminUpdatePartner} submitLabel="Salvar dados" submitSize="sm" resetOnSuccess={false} className="grid gap-3 sm:grid-cols-2">
            <input type="hidden" name="partnerId" value={p.id} />
            <Field label="Nome"><input name="name" defaultValue={p.user.name ?? ""} maxLength={120} className={inputCls} /></Field>
            <Field label="Nome de usuário"><input name="username" defaultValue={p.user.username ?? ""} maxLength={20} className={inputCls} /></Field>
          </ActionForm>
          <div className="space-y-2 border-t border-border pt-3">
            <p className="text-sm font-semibold">Cupons</p>
            {p.coupons.map((c) => (
              <div key={c.id} className="flex flex-wrap items-center justify-between gap-2 text-sm">
                <span>
                  <span className="font-mono font-semibold">{c.code}</span> · {c.discountPoints} p.p. · criado {dateBR(c.createdAt)}
                  {c.replacedAt ? ` · substituído ${dateBR(c.replacedAt)}` : ""}
                </span>
                <ActionForm action={adminSetCouponActive} submitLabel={c.active ? "Desativar" : "Ativar"} submitSize="sm" submitVariant={c.active ? "secondary" : "primary"} resetOnSuccess={false} className="flex items-center gap-2">
                  <input type="hidden" name="couponId" value={c.id} />
                  <input type="hidden" name="active" value={c.active ? "false" : "true"} />
                </ActionForm>
              </div>
            ))}
            <ActionForm action={adminReplaceCoupon} submitLabel="Substituir cupom" submitSize="sm" submitVariant="secondary" confirmText="Substituir o cupom? O atual será desativado para novas contratações." className="flex flex-wrap items-end gap-2">
              <input type="hidden" name="partnerId" value={p.id} />
              <input name="code" maxLength={20} placeholder="Novo código (opcional)" aria-label="Novo código" className={`${inputCls} max-w-56 uppercase`} />
            </ActionForm>
          </div>
          <div className="space-y-2 border-t border-border pt-3">
            <ActionForm action={adminResetPartnerPassword} submitLabel="Definir nova senha" submitSize="sm" submitVariant="secondary" confirmText="Definir a nova senha e encerrar as sessões abertas do parceiro?" className="flex flex-wrap items-end gap-2">
              <input type="hidden" name="partnerId" value={p.id} />
              <input name="password" type="password" minLength={MIN_PARTNER_PASSWORD} required autoComplete="new-password" placeholder="Nova senha" aria-label="Nova senha" className={`${inputCls} max-w-56`} />
            </ActionForm>
            <ActionForm
              action={adminSetPartnerActive}
              submitLabel={p.active ? "Desativar parceiro" : "Reativar parceiro"}
              submitSize="sm"
              submitVariant={p.active ? "danger" : "primary"}
              confirmText={p.active ? "Desativar? Novos logins ficam bloqueados e as sessões abertas são encerradas. O histórico é mantido." : undefined}
              resetOnSuccess={false}
            >
              <input type="hidden" name="partnerId" value={p.id} />
              <input type="hidden" name="active" value={p.active ? "false" : "true"} />
            </ActionForm>
          </div>
        </Card>
      </div>

      <FilterBar action={`/admin/parceiros/${p.id}`} raw={f.raw} show={["concurso", "situacao", "periodo"]} />

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Usuários indicados ({d.referrals.length} únicos · {payingEmails.size} pagantes)</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[560px] text-sm">
            <thead className="border-b border-border"><tr><th className={th}>Cliente</th><th className={th}>Desde</th><th className={th}>Cupom usado</th><th className={th}>Pagante</th></tr></thead>
            <tbody>
              {d.referrals.length === 0 && <tr><td className={td} colSpan={4}><span className="text-muted">Nenhuma indicação no período.</span></td></tr>}
              {d.referrals.map((r) => (
                <tr key={r.id} className="border-b border-border/60 last:border-0">
                  <td className={td}>{r.customerEmail}{r.userId ? "" : <span className="text-xs text-muted"> · sem conta</span>}</td>
                  <td className={td}>{dateBR(r.createdAt)}</td>
                  <td className={`${td} font-mono`}>{r.couponCode}</td>
                  <td className={td}>{payingEmails.has(r.customerEmail) ? <Badge tone="ok">Sim</Badge> : "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </section>

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Contratações e pagamentos com o cupom</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[760px] text-sm">
            <thead className="border-b border-border"><tr><th className={th}>Cliente</th><th className={th}>Concurso</th><th className={th}>Devido</th><th className={th}>Recebido</th><th className={th}>Situação</th><th className={th}>Pagamentos</th></tr></thead>
            <tbody>
              {d.contracts.length === 0 && <tr><td className={td} colSpan={6}><span className="text-muted">Nenhuma contratação no período.</span></td></tr>}
              {d.contracts.map((c) => (
                <tr key={c.id} className="border-b border-border/60 last:border-0">
                  <td className={td}><Link className="font-semibold text-primary underline" href={`/admin/financeiro/${c.id}`}>{c.customerEmail}</Link><span className="block text-xs text-muted">{dateBR(c.createdAt)} · {c.couponCode}</span></td>
                  <td className={td}>{contestName(c.contest)}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(c.finalAmount))}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(c.paidAmount))}</td>
                  <td className={td}><Badge tone={CONTRACT_STATUS[c.status].tone}>{CONTRACT_STATUS[c.status].label}</Badge></td>
                  <td className={`${td} text-xs`}>
                    {c.payments.length === 0 ? "—" : c.payments.map((x) => (
                      <span key={x.id} className="block">{dateBR(x.paidAt)} · {formatBRL(toCents(x.amount))} ({PAYMENT_METHOD_LABEL[x.method]}){x.reversals.length ? ` · estornado ${formatBRL(x.reversals.reduce((s, r) => s + toCents(r.amount), 0))}` : ""}</span>
                    ))}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </section>

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Comissões (rastreio até a origem)</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[760px] text-sm">
            <thead className="border-b border-border"><tr><th className={th}>Data</th><th className={th}>Tipo</th><th className={th}>Valor</th><th className={th}>Contratação</th><th className={th}>Pagamento de origem</th><th className={th}>Disponível em</th></tr></thead>
            <tbody>
              {d.entries.length === 0 && <tr><td className={td} colSpan={6}><span className="text-muted">Nenhuma comissão no período.</span></td></tr>}
              {d.entries.map((e) => (
                <tr key={e.id} className="border-b border-border/60 last:border-0">
                  <td className={td}>{dateBR(e.createdAt)}</td>
                  <td className={td}>{e.kind === "ACCRUAL" ? <Badge tone="ok">Gerada</Badge> : <Badge tone="primary">Revertida</Badge>}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(e.amount))}</td>
                  <td className={td}><Link className="text-primary underline" href={`/admin/financeiro/${e.contract.id}`}>{e.contract.customerEmail}</Link><span className="block text-xs text-muted">{contestName(e.contract.contest)}</span></td>
                  <td className={`${td} text-xs`}>
                    {dateBR(e.payment.paidAt)} · {formatBRL(toCents(e.payment.amount))}
                    {e.reversal && <span className="block text-muted">estorno: {e.reversal.reason}</span>}
                  </td>
                  <td className={td}>{dateBR(e.availableAt)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </section>

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Repasses</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[640px] text-sm">
            <thead className="border-b border-border"><tr><th className={th}>Data</th><th className={th}>Valor</th><th className={th}>Forma</th><th className={th}>Comprovante</th><th className={th}>Registrado por</th></tr></thead>
            <tbody>
              {d.payouts.length === 0 && <tr><td className={td} colSpan={5}><span className="text-muted">Nenhum repasse no período.</span></td></tr>}
              {d.payouts.map((x) => (
                <tr key={x.id} className="border-b border-border/60 last:border-0">
                  <td className={td}>{dateBR(x.paidAt)}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(x.amount))}</td>
                  <td className={td}>{x.method}</td>
                  <td className={`${td} text-xs`}>{x.receiptRef ?? "—"}{x.note && <span className="block text-muted">{x.note}</span>}</td>
                  <td className={`${td} text-xs`}>{x.createdBy.name ?? x.createdBy.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </section>

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Histórico</h2>
        <Card className="space-y-1.5">
          {d.history.length === 0 && <p className="text-sm text-muted">Sem registros.</p>}
          {d.history.map((h) => (
            <p key={h.id} className="text-sm">
              <span className="text-xs text-muted">{h.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" })}</span> · {AUDIT_LABEL[h.action] ?? h.action}
            </p>
          ))}
        </Card>
      </section>
    </div>
  );
}
