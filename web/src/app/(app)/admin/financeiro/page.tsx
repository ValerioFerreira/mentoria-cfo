import type { Metadata } from "next";
import Link from "next/link";
import { ActionForm } from "@/components/action-form";
import { Badge, Card, Field, PageHeader, Stat, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { adminCreateContract, adminUpdateContestSetting } from "@/lib/commerce/admin-actions";
import { AUDIT_LABEL, CONTRACT_STATUS, PAYMENT_METHOD_LABEL, REVERSAL_KIND_LABEL, contestName, dateBR, dayBR } from "@/lib/commerce/labels";
import { formatBRL, toCents } from "@/lib/commerce/money";
import { CATEGORY_LABEL, CATEGORY_PRICE_CENTS, LAUNCH_DISCOUNT_POINTS, PARTNER_COUPON_DISCOUNT_POINTS, quote } from "@/lib/commerce/pricing";
import { auditHistory, listContracts, listCustomers, listPayments } from "@/lib/commerce/queries";
import { db } from "@/lib/db";
import { FilterBar } from "./filter-bar";
import { FILTER_CONTESTS, parseFilters, type SearchParams } from "./filters";

export const metadata: Metadata = { title: "Financeiro" };

const TABS = [
  { key: "contratacoes", label: "Contratações" },
  { key: "pagamentos", label: "Pagamentos" },
  { key: "clientes", label: "Clientes e saldos" },
  { key: "concursos", label: "Concursos e preços" },
  { key: "historico", label: "Histórico" },
] as const;
type Tab = (typeof TABS)[number]["key"];

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function FinanceiroPage({ searchParams }: { searchParams: Promise<SearchParams> }) {
  await requireAdmin();
  const sp = await searchParams;
  const tab: Tab = TABS.find((t) => t.key === sp.aba)?.key ?? "contratacoes";
  const f = parseFilters(sp);

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Administração"
        title="Financeiro"
        description="Obrigações, pagamentos recebidos, saldos e histórico. O acesso acadêmico é liberado à parte, na contratação."
      />
      <nav className="flex flex-wrap gap-2" aria-label="Seções do financeiro">
        {TABS.map((t) => (
          <Link
            key={t.key}
            href={`/admin/financeiro?aba=${t.key}`}
            aria-current={tab === t.key ? "page" : undefined}
            className={`rounded-full px-3.5 py-1.5 text-sm font-semibold transition ${tab === t.key ? "bg-ink text-on-ink" : "bg-surface-2 text-muted hover:text-text"}`}
          >
            {t.label}
          </Link>
        ))}
      </nav>
      {tab === "contratacoes" && <Contracts f={f} />}
      {tab === "pagamentos" && <Payments f={f} />}
      {tab === "clientes" && <Customers f={f} />}
      {tab === "concursos" && <ContestsTab />}
      {tab === "historico" && <History f={f} />}
    </div>
  );
}

async function Contracts({ f }: { f: ReturnType<typeof parseFilters> }) {
  const { rows, totals } = await listContracts(f);
  return (
    <div className="space-y-4">
      <FilterBar action="/admin/financeiro" raw={f.raw} hidden={{ aba: "contratacoes" }} />
      <div className="grid gap-3 sm:grid-cols-3">
        <Stat label="Contratações (não canceladas)" value={totals.count} />
        <Stat label="Valor devido" value={formatBRL(totals.dueCents)} />
        <Stat label="Recebido" value={formatBRL(totals.receivedCents)} hint={`Saldo: ${formatBRL(totals.dueCents - totals.receivedCents)}`} />
      </div>
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[860px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Cliente</th><th className={th}>Concurso</th><th className={th}>Original</th><th className={th}>Devido</th><th className={th}>Recebido</th><th className={th}>Saldo</th><th className={th}>Situação</th><th className={th}>Acesso</th></tr>
          </thead>
          <tbody>
            {rows.length === 0 && <tr><td className={td} colSpan={8}><span className="text-muted">Nenhuma contratação encontrada.</span></td></tr>}
            {rows.map((c) => {
              const due = toCents(c.finalAmount);
              const paid = toCents(c.paidAmount);
              return (
                <tr key={c.id} className="border-b border-border/60 last:border-0 hover:bg-surface-2/60">
                  <td className={td}>
                    <Link href={`/admin/financeiro/${c.id}`} className="font-semibold text-primary underline">{c.customerName ?? c.customerEmail}</Link>
                    <span className="block text-xs text-muted">{c.customerEmail}{c.userId ? "" : " · sem conta"}</span>
                    <span className="block text-xs text-muted">{dateBR(c.createdAt)}{c.couponCode ? ` · cupom ${c.couponCode}${c.partner?.user.username ? ` (@${c.partner.user.username})` : ""}` : ""}</span>
                  </td>
                  <td className={td}>{contestName(c.contest)}<span className="block text-xs text-muted">{CATEGORY_LABEL[c.category]}</span></td>
                  <td className={`${td} tabular whitespace-nowrap text-muted line-through`}>{formatBRL(toCents(c.originalAmount))}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(due)}</td>
                  <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(paid)}<span className="block text-xs text-muted">{c._count.payments} pag. · {c._count.reversals} ajuste(s)</span></td>
                  <td className={`${td} tabular whitespace-nowrap`}>{due - paid < 0 ? <span className="text-primary">excedente {formatBRL(paid - due)}</span> : formatBRL(due - paid)}</td>
                  <td className={td}><Badge tone={CONTRACT_STATUS[c.status].tone}>{CONTRACT_STATUS[c.status].label}</Badge></td>
                  <td className={`${td} text-xs`}>
                    {c.accessGrantedAt ? `Liberado até ${dateBR(c.accessUntil)}` : c.examDateAtContract ? "Não liberado" : <span className="text-warn">Data da prova pendente</span>}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </Card>
      <Card className="space-y-3">
        <h2 className="font-display text-lg font-bold uppercase">Nova contratação manual</h2>
        <p className="text-sm text-muted">Para cliente que contratou fora do site. O preço segue a categoria do concurso e o cupom (se houver), sempre calculado pelo sistema.</p>
        <ActionForm action={adminCreateContract} submitLabel="Registrar contratação" className="grid gap-3 sm:grid-cols-2">
          <Field label="E-mail do cliente"><input name="email" type="email" required className={inputCls} /></Field>
          <Field label="Nome (opcional)"><input name="name" className={inputCls} /></Field>
          <Field label="Concurso">
            <select name="contest" required className={inputCls}>{FILTER_CONTESTS.map((c) => <option key={c} value={c}>{contestName(c)}</option>)}</select>
          </Field>
          <Field label="Cupom (opcional)"><input name="coupon" maxLength={20} className={`${inputCls} uppercase`} /></Field>
        </ActionForm>
      </Card>
    </div>
  );
}

async function Payments({ f }: { f: ReturnType<typeof parseFilters> }) {
  const rows = await listPayments(f);
  const total = rows.reduce((s, p) => s + toCents(p.amount), 0);
  const reversed = rows.reduce((s, p) => s + p.reversals.reduce((a, r) => a + toCents(r.amount), 0), 0);
  return (
    <div className="space-y-4">
      <FilterBar action="/admin/financeiro" raw={f.raw} hidden={{ aba: "pagamentos" }} />
      <div className="grid gap-3 sm:grid-cols-3">
        <Stat label="Pagamentos" value={rows.length} />
        <Stat label="Total lançado" value={formatBRL(total)} />
        <Stat label="Estornos e correções" value={formatBRL(reversed)} hint={`Válido: ${formatBRL(total - reversed)}`} />
      </div>
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[860px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Data</th><th className={th}>Cliente</th><th className={th}>Concurso</th><th className={th}>Valor</th><th className={th}>Forma</th><th className={th}>Comprovante</th><th className={th}>Lançado por</th><th className={th}>Ajustes</th></tr>
          </thead>
          <tbody>
            {rows.length === 0 && <tr><td className={td} colSpan={8}><span className="text-muted">Nenhum pagamento encontrado.</span></td></tr>}
            {rows.map((p) => (
              <tr key={p.id} className="border-b border-border/60 last:border-0">
                <td className={td}>{dateBR(p.paidAt)}<span className="block text-xs text-muted">lançado {dateBR(p.createdAt)}</span></td>
                <td className={td}><Link href={`/admin/financeiro/${p.contract.id}`} className="font-semibold text-primary underline">{p.contract.customerName ?? p.contract.customerEmail}</Link></td>
                <td className={td}>{contestName(p.contract.contest)}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(toCents(p.amount))}</td>
                <td className={td}>{PAYMENT_METHOD_LABEL[p.method]}</td>
                <td className={`${td} text-xs`}>{p.receiptRef ?? "—"}{p.note && <span className="block text-muted">{p.note}</span>}</td>
                <td className={`${td} text-xs`}>{p.createdBy.name ?? p.createdBy.email}</td>
                <td className={`${td} text-xs`}>
                  {p.reversals.length === 0 ? "—" : p.reversals.map((r) => (
                    <span key={r.id} className="block">{REVERSAL_KIND_LABEL[r.kind]} {formatBRL(toCents(r.amount))} em {dateBR(r.effectiveAt)}: {r.reason}</span>
                  ))}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}

async function Customers({ f }: { f: ReturnType<typeof parseFilters> }) {
  const rows = await listCustomers(f);
  return (
    <div className="space-y-4">
      <FilterBar action="/admin/financeiro" raw={f.raw} hidden={{ aba: "clientes" }} show={["q", "concurso", "situacao", "periodo"]} />
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[720px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Cliente</th><th className={th}>Concursos</th><th className={th}>Devido</th><th className={th}>Recebido</th><th className={th}>Saldo consolidado</th></tr>
          </thead>
          <tbody>
            {rows.length === 0 && <tr><td className={td} colSpan={5}><span className="text-muted">Nenhum cliente encontrado.</span></td></tr>}
            {rows.map((c) => (
              <tr key={c.email} className="border-b border-border/60 last:border-0">
                <td className={td}>
                  <Link href={`/admin/financeiro?aba=contratacoes&q=${encodeURIComponent(c.email)}`} className="font-semibold text-primary underline">{c.name ?? c.email}</Link>
                  <span className="block text-xs text-muted">{c.email}{c.hasAccount ? "" : " · sem conta"}</span>
                </td>
                <td className={`${td} text-xs`}>{c.contests.map(contestName).join(", ")}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(c.dueCents)}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(c.receivedCents)}</td>
                <td className={`${td} tabular whitespace-nowrap`}>
                  {c.dueCents - c.receivedCents >= 0 ? formatBRL(c.dueCents - c.receivedCents) : <span className="text-primary">excedente {formatBRL(c.receivedCents - c.dueCents)}</span>}
                  {c.overpaid && <Badge tone="primary" className="ml-2">tratar excedente</Badge>}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}

async function ContestsTab() {
  const settings = await db.contestSetting.findMany();
  const byKey = new Map(settings.map((s) => [s.contest, s]));
  return (
    <div className="space-y-4">
      <Card tone="soft" className="space-y-1 text-sm">
        <p className="font-semibold">Regras comerciais vigentes</p>
        <p className="text-muted">
          Preço original: Oficial e PCPE {formatBRL(CATEGORY_PRICE_CENTS.OFICIAL)}; Praça {formatBRL(CATEGORY_PRICE_CENTS.PRACA)}. Lançamento: {LAUNCH_DISCOUNT_POINTS}% ({formatBRL(quote("OFICIAL").finalCents)} e {formatBRL(quote("PRACA").finalCents)}).
          Cupom de parceiro: +{PARTNER_COUPON_DISCOUNT_POINTS} p.p. ({formatBRL(quote("OFICIAL", PARTNER_COUPON_DISCOUNT_POINTS).finalCents)} e {formatBRL(quote("PRACA", PARTNER_COUPON_DISCOUNT_POINTS).finalCents)}).
        </p>
        <p className="text-muted">Sem categoria, o concurso não pode ser contratado. Sem data da prova, a contratação é registrada, mas o acesso até a prova não é liberado.</p>
      </Card>
      <div className="grid gap-3 md:grid-cols-2">
        {FILTER_CONTESTS.map((c) => {
          const s = byKey.get(c);
          return (
            <Card key={c} className="space-y-3">
              <div className="flex items-center justify-between gap-2">
                <h3 className="font-display text-lg font-bold uppercase">{contestName(c)}</h3>
                {!s?.category ? <Badge tone="warn">Sem categoria</Badge> : !s.examDate ? <Badge tone="warn">Data da prova pendente</Badge> : <Badge tone="ok">Completo</Badge>}
              </div>
              <ActionForm action={adminUpdateContestSetting} submitLabel="Salvar" submitSize="sm" resetOnSuccess={false} className="grid gap-3 sm:grid-cols-2">
                <input type="hidden" name="contest" value={c} />
                <Field label="Categoria comercial">
                  <select name="category" defaultValue={s?.category ?? ""} className={inputCls}>
                    <option value="">— em revisão —</option>
                    <option value="OFICIAL">Oficial</option>
                    <option value="PCPE">PCPE</option>
                    <option value="PRACA">Praça</option>
                  </select>
                </Field>
                <Field label="Data oficial da prova">
                  <input type="date" name="examDate" defaultValue={s?.examDate?.toISOString().slice(0, 10) ?? ""} className={inputCls} />
                </Field>
              </ActionForm>
              {s?.examDate && <p className="text-xs text-muted">Acesso das contratações vale até 23:59 de {dayBR(s.examDate)} (Recife).</p>}
            </Card>
          );
        })}
      </div>
    </div>
  );
}

async function History({ f }: { f: ReturnType<typeof parseFilters> }) {
  const rows = await auditHistory({ from: f.from, to: f.to });
  return (
    <div className="space-y-4">
      <FilterBar action="/admin/financeiro" raw={f.raw} hidden={{ aba: "historico" }} show={["periodo"]} />
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[720px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Quando</th><th className={th}>Ação</th><th className={th}>Registro</th><th className={th}>Detalhes</th></tr>
          </thead>
          <tbody>
            {rows.length === 0 && <tr><td className={td} colSpan={4}><span className="text-muted">Sem registros no período.</span></td></tr>}
            {rows.map((h) => (
              <tr key={h.id} className="border-b border-border/60 last:border-0">
                <td className={`${td} whitespace-nowrap text-xs`}>{h.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" })}</td>
                <td className={td}>{AUDIT_LABEL[h.action] ?? h.action}</td>
                <td className={`${td} text-xs`}>
                  {h.entityType === "Contract" ? <Link className="text-primary underline" href={`/admin/financeiro/${h.entityId}`}>Contratação</Link>
                    : h.entityType === "Partner" ? <Link className="text-primary underline" href={`/admin/parceiros/${h.entityId}`}>Parceiro</Link>
                      : `${h.entityType} ${h.entityId}`}
                </td>
                <td className={`${td} max-w-md break-words font-mono text-[11px] text-muted`}>{h.data ? JSON.stringify(h.data) : "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
