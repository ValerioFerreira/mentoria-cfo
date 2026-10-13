import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ActionForm } from "@/components/action-form";
import { Alert, Badge, Card, Field, PageHeader, Stat, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { adminCancelContract, adminGrantAccess, adminRegisterPayment, adminReversePayment } from "@/lib/commerce/admin-actions";
import { newIdempotencyKey } from "@/lib/commerce/keys";
import { AUDIT_LABEL, CONTRACT_STATUS, PAYMENT_METHOD_LABEL, REVERSAL_KIND_LABEL, actorLabel, contestName, dateBR, dayBR } from "@/lib/commerce/labels";
import { formatBRL, toCents } from "@/lib/commerce/money";
import { CATEGORY_LABEL } from "@/lib/commerce/pricing";
import { contractDetail } from "@/lib/commerce/queries";
import { todayISO } from "@/lib/plan-time";

export const metadata: Metadata = { title: "Contratação" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function ContractPage({ params }: { params: Promise<{ id: string }> }) {
  await requireAdmin();
  const { id } = await params;
  const d = await contractDetail(id);
  if (!d) notFound();
  const { contract: c, setting, history, customer } = d;
  const due = toCents(c.finalAmount);
  const paid = toCents(c.paidAmount);
  const today = todayISO();
  const st = CONTRACT_STATUS[c.status];
  const cancelled = c.status === "CANCELLED";

  return (
    <div className="space-y-6">
      <Link href="/admin/financeiro" className="text-sm font-semibold text-muted underline">← Financeiro</Link>
      <PageHeader
        eyebrow={`${contestName(c.contest)} · ${CATEGORY_LABEL[c.category]}`}
        title={c.customerName ?? c.customerEmail}
        description={`${c.customerEmail} · contratação de ${dateBR(c.createdAt)} · regra ${c.pricingRule}`}
        actions={<Badge tone={st.tone}>{st.label}</Badge>}
      />

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Stat label="Preço original" value={formatBRL(toCents(c.originalAmount))} hint={`Descontos: ${c.launchDiscountPoints}% lançamento${c.partnerDiscountPoints ? ` + ${c.partnerDiscountPoints}% cupom ${c.couponCode}` : ""} (${formatBRL(toCents(c.discountAmount))})`} />
        <Stat label="Valor devido" value={formatBRL(due)} />
        <Stat label="Recebido (válido)" value={formatBRL(paid)} />
        <Stat label={paid > due ? "Excedente" : "Saldo pendente"} value={formatBRL(Math.abs(due - paid))} hint={`Saldo consolidado do cliente (${customer.contracts} contratação/ões): ${formatBRL(customer.balanceCents)}`} />
      </div>
      {c.status === "OVERPAID" && <Alert tone="danger">Pagamento excedente de {formatBRL(paid - due)}: o valor recebido foi preservado. Trate com o cliente e, se devolver, registre um estorno.</Alert>}
      {c.partner && (
        <p className="text-sm text-muted">
          Indicação: <Link className="font-semibold text-primary underline" href={`/admin/parceiros/${c.partner.id}`}>@{c.partner.user.username ?? c.partner.user.name}</Link> (cupom {c.couponCode})
        </p>
      )}

      <div className="grid gap-4 lg:grid-cols-2">
        <Card className="space-y-3">
          <h2 className="font-display text-lg font-bold uppercase">Registrar pagamento recebido</h2>
          {cancelled ? <p className="text-sm text-muted">Contratação cancelada.</p> : (
            <ActionForm action={adminRegisterPayment} submitLabel="Registrar pagamento" className="grid gap-3 sm:grid-cols-2">
              <input type="hidden" name="contractId" value={c.id} />
              <input type="hidden" name="idempotencyKey" value={newIdempotencyKey()} />
              <Field label="Valor recebido (R$)"><input name="amount" inputMode="decimal" required placeholder={formatBRL(Math.max(0, due - paid)).replace("R$ ", "")} className={inputCls} /></Field>
              <Field label="Data efetiva"><input name="paidAt" type="date" required max={today} defaultValue={today} className={inputCls} /></Field>
              <Field label="Forma de pagamento">
                <select name="method" defaultValue="PIX" className={inputCls}>
                  {Object.entries(PAYMENT_METHOD_LABEL).filter(([k]) => k !== "CARTAO").map(([k, v]) => <option key={k} value={k}>{v}</option>)}
                </select>
              </Field>
              <Field label="Comprovante (identificador)"><input name="receiptRef" maxLength={120} className={inputCls} /></Field>
              <div className="sm:col-span-2"><Field label="Observação (opcional)"><input name="note" maxLength={500} className={inputCls} /></Field></div>
            </ActionForm>
          )}
        </Card>

        <Card className="space-y-3">
          <h2 className="font-display text-lg font-bold uppercase">Acesso acadêmico</h2>
          <p className="text-sm text-muted">
            {c.accessGrantedAt ? `Liberado em ${dateBR(c.accessGrantedAt)} até ${dateBR(c.accessUntil)}.` : "Ainda não liberado por esta contratação."}{" "}
            {c.user ? `Conta: validade atual ${c.user.accessExpiresAt ? dateBR(c.user.accessExpiresAt) : "sem prazo"}.` : "Sem conta: aprove o cadastro em Cadastros."}
          </p>
          <p className="text-sm text-muted">Data oficial da prova: {setting?.examDate ? dayBR(setting.examDate) : <strong className="text-warn">pendente</strong>}.</p>
          {!cancelled && c.user && setting?.examDate && (
            <ActionForm action={adminGrantAccess} submitLabel="Liberar acesso até a prova" resetOnSuccess={false}>
              <input type="hidden" name="contractId" value={c.id} />
              {c.status !== "PAID" && c.status !== "OVERPAID" && (
                <>
                  <label className="flex items-center gap-2 text-sm"><input type="checkbox" name="override" /> Liberar mesmo com saldo pendente</label>
                  <Field label="Justificativa (obrigatória nesse caso)"><input name="justification" maxLength={500} className={inputCls} /></Field>
                </>
              )}
            </ActionForm>
          )}
        </Card>
      </div>

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Pagamentos ({c.payments.length})</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[760px] text-sm">
            <thead className="border-b border-border">
              <tr><th className={th}>Data</th><th className={th}>Valor</th><th className={th}>Forma</th><th className={th}>Comprovante</th><th className={th}>Lançado por</th><th className={th}>Estornos/correções</th></tr>
            </thead>
            <tbody>
              {c.payments.length === 0 && <tr><td className={td} colSpan={6}><span className="text-muted">Nenhum pagamento registrado.</span></td></tr>}
              {c.payments.map((p) => {
                const left = toCents(p.amount) - p.reversals.reduce((s, r) => s + toCents(r.amount), 0);
                return (
                  <tr key={p.id} className="border-b border-border/60 last:border-0">
                    <td className={td}>{dateBR(p.paidAt)}<span className="block text-xs text-muted">lançado {p.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" })}</span></td>
                    <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(p.amount))}</td>
                    <td className={td}>{PAYMENT_METHOD_LABEL[p.method]}</td>
                    <td className={`${td} text-xs`}>{p.receiptRef ?? "—"}{p.note && <span className="block text-muted">{p.note}</span>}</td>
                    <td className={`${td} text-xs`}>{actorLabel(p.createdBy)}</td>
                    <td className={`${td} text-xs`}>
                      {p.reversals.map((r) => (
                        <span key={r.id} className="block">
                          {REVERSAL_KIND_LABEL[r.kind]} de {formatBRL(toCents(r.amount))} em {dateBR(r.effectiveAt)} — {r.reason} ({actorLabel(r.createdBy)})
                        </span>
                      ))}
                      {left > 0 && (
                        <details className="mt-1">
                          <summary className="cursor-pointer font-semibold text-primary">Estornar ou corrigir</summary>
                          <ActionForm action={adminReversePayment} submitLabel="Registrar ajuste" submitSize="sm" confirmText="Confirmar o estorno/correção? O lançamento original é mantido no histórico." className="mt-2 grid gap-2">
                            <input type="hidden" name="paymentId" value={p.id} />
                            <input type="hidden" name="contractId" value={c.id} />
                            <input type="hidden" name="idempotencyKey" value={newIdempotencyKey()} />
                            <input name="amount" inputMode="decimal" required placeholder={`até ${formatBRL(left)}`} aria-label="Valor do ajuste" className={inputCls} />
                            <select name="kind" defaultValue="ESTORNO" aria-label="Tipo" className={inputCls}>
                              <option value="ESTORNO">Estorno (devolução ao cliente)</option>
                              <option value="CORRECAO">Correção de lançamento</option>
                            </select>
                            <input name="effectiveAt" type="date" required max={today} defaultValue={today} aria-label="Data efetiva" className={inputCls} />
                            <input name="reason" required minLength={5} maxLength={500} placeholder="Justificativa" aria-label="Justificativa" className={inputCls} />
                          </ActionForm>
                        </details>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </Card>
      </section>

      {c.commissions.length > 0 && (
        <section className="space-y-2">
          <h2 className="font-display text-lg font-bold uppercase">Comissões desta contratação</h2>
          <Card className="overflow-x-auto p-0">
            <table className="w-full min-w-[600px] text-sm">
              <thead className="border-b border-border"><tr><th className={th}>Data</th><th className={th}>Tipo</th><th className={th}>Valor</th><th className={th}>Base</th><th className={th}>Origem</th><th className={th}>Disponível em</th></tr></thead>
              <tbody>
                {c.commissions.map((e) => (
                  <tr key={e.id} className="border-b border-border/60 last:border-0">
                    <td className={td}>{dateBR(e.createdAt)}</td>
                    <td className={td}>{e.kind === "ACCRUAL" ? "Gerada" : "Revertida"}</td>
                    <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(e.amount))}</td>
                    <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(e.basisAmount))} × {e.rateBp / 100}%</td>
                    <td className={`${td} text-xs`}>{e.reversalId ? "estorno do pagamento" : "pagamento"} {e.paymentId.slice(-6)}</td>
                    <td className={td}>{dateBR(e.availableAt)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Card>
        </section>
      )}

      <section className="space-y-2">
        <h2 className="font-display text-lg font-bold uppercase">Histórico</h2>
        <Card className="space-y-1.5">
          {history.length === 0 && <p className="text-sm text-muted">Sem registros.</p>}
          {history.map((h) => (
            <p key={h.id} className="text-sm">
              <span className="text-xs text-muted">{h.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" })}</span> · {AUDIT_LABEL[h.action] ?? h.action}
            </p>
          ))}
        </Card>
      </section>

      {!cancelled && paid === 0 && (
        <Card tone="soft" className="space-y-3">
          <h2 className="font-display text-lg font-bold uppercase">Cancelar contratação</h2>
          <ActionForm action={adminCancelContract} submitLabel="Cancelar contratação" submitVariant="danger" confirmText="Cancelar esta contratação? Ela fica no histórico." className="flex flex-wrap items-end gap-3">
            <input type="hidden" name="contractId" value={c.id} />
            <div className="min-w-64 flex-1"><Field label="Motivo"><input name="reason" required minLength={5} maxLength={500} className={inputCls} /></Field></div>
          </ActionForm>
        </Card>
      )}
    </div>
  );
}
