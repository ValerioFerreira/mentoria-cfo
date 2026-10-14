import type { Metadata } from "next";
import Link from "next/link";
import { ActionForm } from "@/components/action-form";
import { Badge, Card, Field, PageHeader, SectionTitle, Stat, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { adminCreatePartner, adminSetPartnerActive } from "@/lib/commerce/admin-actions";
import { formatBRL } from "@/lib/commerce/money";
import { MIN_PARTNER_PASSWORD } from "@/lib/commerce/partners";
import { COMMISSION_RATE_BP, PARTNER_COUPON_DISCOUNT_POINTS } from "@/lib/commerce/pricing";
import { listPartners, partnersDashboard, type PartnersDashboard } from "@/lib/commerce/queries";

export const metadata: Metadata = { title: "Parceiros" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function PartnersPage() {
  await requireAdmin();
  const [partners, dash] = await Promise.all([listPartners(), partnersDashboard()]);
  return (
    <div className="space-y-6">
      <Link href="/admin" className="text-sm font-semibold text-muted underline">← Administração</Link>
      <PageHeader
        eyebrow="Administração"
        title="Parceiros"
        description={`Divulgadores com cupom exclusivo (+${PARTNER_COUPON_DISCOUNT_POINTS} p.p. de desconto ao cliente) e comissão de ${COMMISSION_RATE_BP / 100}% sobre o valor recebido.`}
      />
      <Dashboard d={dash} />

      <SectionTitle id="lista">Parceiros cadastrados</SectionTitle>
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[920px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Parceiro</th><th className={th}>Cupom</th><th className={th}>Indicados</th><th className={th}>Contratações</th><th className={th}>Gerado</th><th className={th}>Repassado</th><th className={th}>Disponível</th><th className={th}>Pendente / a compensar</th><th className={th}>Ações</th></tr>
          </thead>
          <tbody>
            {partners.length === 0 && <tr><td className={td} colSpan={9}><span className="text-muted">Nenhum parceiro cadastrado.</span></td></tr>}
            {partners.map((p) => (
              <tr key={p.id} className="border-b border-border/60 last:border-0 hover:bg-surface-2/60">
                <td className={td}>
                  <Link href={`/admin/parceiros/${p.id}`} className="font-semibold text-primary underline">{p.name ?? p.username ?? p.email}</Link>
                  <span className="block text-xs text-muted">@{p.username} · {p.email}</span>
                  {!p.active && <Badge tone="neutral" className="mt-1">Desativado</Badge>}
                </td>
                <td className={`${td} font-mono`}>{p.coupon ?? <span className="text-muted">sem cupom ativo</span>}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{p.referrals}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{p.contracts}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(p.balance.generatedCents - p.balance.reversedCents)}</td>
                <td className={`${td} tabular whitespace-nowrap`}>{formatBRL(p.balance.paidOutCents)}</td>
                <td className={`${td} tabular whitespace-nowrap font-semibold`}>{formatBRL(p.balance.availableCents)}</td>
                <td className={`${td} tabular whitespace-nowrap text-xs`}>
                  {formatBRL(p.balance.pendingCents)}
                  {p.balance.negativeCents > 0 && <span className="block text-primary">−{formatBRL(p.balance.negativeCents)} a compensar</span>}
                </td>
                <td className={td}>
                  <div className="flex flex-wrap items-center gap-2">
                    <Link href={`/admin/parceiros/${p.id}`} className="text-xs font-semibold text-primary underline">Editar</Link>
                    <ActionForm
                      action={adminSetPartnerActive}
                      submitLabel={p.active ? "Inativar" : "Reativar"}
                      submitSize="sm"
                      submitVariant={p.active ? "secondary" : "primary"}
                      confirmText={p.active ? "Inativar este parceiro? Novos logins ficam bloqueados, as sessões abertas são encerradas e o histórico é mantido." : undefined}
                      resetOnSuccess={false}
                    >
                      <input type="hidden" name="partnerId" value={p.id} />
                      <input type="hidden" name="active" value={p.active ? "false" : "true"} />
                    </ActionForm>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>

      <Card className="space-y-3">
        <h2 className="font-display text-lg font-bold uppercase">Cadastrar parceiro</h2>
        <p className="text-sm text-muted">
          O parceiro entra como usuário comum (acesso acadêmico normal) com o painel Minha parceria. A senha inicial é guardada só como hash, não é exibida de novo e o parceiro não pode trocá-la pela interface.
        </p>
        <ActionForm action={adminCreatePartner} submitLabel="Cadastrar parceiro" className="grid gap-3 sm:grid-cols-2">
          <Field label="E-mail"><input name="email" type="email" required maxLength={120} autoComplete="off" className={inputCls} /></Field>
          <Field label="Nome de usuário" hint="3 a 20: minúsculas, números, ponto, hífen ou sublinhado.">
            <input name="username" required maxLength={20} pattern="[a-z0-9][a-z0-9._\-]{2,19}" autoComplete="off" className={inputCls} />
          </Field>
          <Field label="Nome (opcional)"><input name="name" maxLength={120} className={inputCls} /></Field>
          <Field label="Senha inicial" hint={`Mínimo de ${MIN_PARTNER_PASSWORD} caracteres.`}>
            <input name="password" type="password" minLength={MIN_PARTNER_PASSWORD} autoComplete="new-password" className={inputCls} />
          </Field>
          <Field label="Cupom (opcional)" hint="Em branco: gerado a partir do nome de usuário.">
            <input name="couponCode" maxLength={20} className={`${inputCls} uppercase`} />
          </Field>
          <label className="flex items-start gap-2 self-end text-sm">
            <input type="checkbox" name="linkExisting" className="mt-1" />
            <span>Vincular à conta existente, se o e-mail já tiver cadastro (não cria outra conta; a senha atual é mantida).</span>
          </label>
        </ActionForm>
      </Card>
    </div>
  );
}

const pct = (v: number | null) => (v === null ? "—" : `${Math.round(v * 100)}%`);

function Dashboard({ d }: { d: PartnersDashboard }) {
  const maxMonth = Math.max(1, ...d.months.map((m) => m.receivedCents));
  const maxRank = Math.max(1, ...d.ranking.map((r) => r.receivedCents));
  return (
    <section className="space-y-4" aria-labelledby="ind">
      <SectionTitle id="ind" info="Contratações canceladas não entram. Conversão = contratações com algum valor recebido ÷ usuários indicados pelo cupom. Receita = valor recebido nas contratações feitas com cupom de parceiro.">
        Indicadores da parceria
      </SectionTitle>
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        <Stat label="Parceiros" value={d.partners.total} hint={`${d.partners.active} ativos · ${d.partners.inactive} inativos`} />
        <Stat label="Indicados" value={d.referrals} hint={`${d.withoutActivity} parceiro(s) sem indicações`} />
        <Stat label="Contratações com cupom" value={d.contracts} hint={`${d.payingContracts} com pagamento`} />
        <Stat label="Conversão" value={pct(d.conversion)} hint="indicado que pagou" />
        <Stat label="Receita via parceiros" value={formatBRL(d.receivedCents)} hint={`Devido: ${formatBRL(d.dueCents)}`} />
        <Stat label="Ticket médio" value={d.ticketCents === null ? "—" : formatBRL(d.ticketCents)} hint="por contratação paga" />
        <Stat label="Comissões geradas" value={formatBRL(d.commissionGeneratedCents)} hint={`Repassado: ${formatBRL(d.paidOutCents)}`} />
        <Stat label="A repassar" value={formatBRL(d.availableCents)} hint={`Em garantia: ${formatBRL(d.pendingCents)}`} />
      </div>
      <div className="grid gap-4 lg:grid-cols-2">
        <Card className="space-y-3 p-4">
          <h3 className="font-display text-lg font-bold uppercase">Receita por mês (últimos 6)</h3>
          <ul className="space-y-2">
            {d.months.map((m) => (
              <li key={m.label} className="grid grid-cols-[3.5rem_1fr_auto] items-center gap-3 text-sm">
                <span className="text-xs uppercase text-muted">{m.label}</span>
                <span className="h-2.5 overflow-hidden rounded-full bg-surface-3"><span className="block h-full rounded-full bg-primary" style={{ width: `${(m.receivedCents / maxMonth) * 100}%` }} /></span>
                <span className="tabular text-xs text-muted"><strong className="text-text">{formatBRL(m.receivedCents)}</strong> · {m.contracts} contr.</span>
              </li>
            ))}
          </ul>
        </Card>
        <Card className="space-y-3 p-4">
          <h3 className="font-display text-lg font-bold uppercase">Ranking por receita</h3>
          {d.ranking.length === 0 ? <p className="text-sm text-muted">Sem parceiros.</p> : (
            <ul className="space-y-2">
              {d.ranking.slice(0, 6).map((r, i) => (
                <li key={r.id} className="space-y-1 text-sm">
                  <div className="flex items-baseline justify-between gap-2">
                    <Link href={`/admin/parceiros/${r.id}`} className="min-w-0 truncate font-semibold text-primary underline">{i + 1}. {r.name}</Link>
                    <span className="tabular text-xs text-muted"><strong className="text-text">{formatBRL(r.receivedCents)}</strong> · {r.referrals} indic. · {r.paying} pag. · comissão {formatBRL(r.commissionCents)}</span>
                  </div>
                  <span className="block h-1.5 overflow-hidden rounded-full bg-surface-3"><span className="block h-full rounded-full bg-gold" style={{ width: `${(r.receivedCents / maxRank) * 100}%` }} /></span>
                </li>
              ))}
            </ul>
          )}
        </Card>
      </div>
    </section>
  );
}
