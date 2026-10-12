import type { Metadata } from "next";
import Link from "next/link";
import { ActionForm } from "@/components/action-form";
import { Badge, Card, Field, PageHeader, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { adminCreatePartner } from "@/lib/commerce/admin-actions";
import { formatBRL } from "@/lib/commerce/money";
import { MIN_PARTNER_PASSWORD } from "@/lib/commerce/partners";
import { COMMISSION_RATE_BP, PARTNER_COUPON_DISCOUNT_POINTS } from "@/lib/commerce/pricing";
import { listPartners } from "@/lib/commerce/queries";

export const metadata: Metadata = { title: "Parceiros" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function PartnersPage() {
  await requireAdmin();
  const partners = await listPartners();
  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Administração"
        title="Parceiros"
        description={`Divulgadores com cupom exclusivo (+${PARTNER_COUPON_DISCOUNT_POINTS} p.p. de desconto ao cliente) e comissão de ${COMMISSION_RATE_BP / 100}% sobre o valor recebido.`}
      />
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[820px] text-sm">
          <thead className="border-b border-border">
            <tr><th className={th}>Parceiro</th><th className={th}>Cupom</th><th className={th}>Indicados</th><th className={th}>Contratações</th><th className={th}>Gerado</th><th className={th}>Repassado</th><th className={th}>Disponível</th><th className={th}>Pendente / a compensar</th></tr>
          </thead>
          <tbody>
            {partners.length === 0 && <tr><td className={td} colSpan={8}><span className="text-muted">Nenhum parceiro cadastrado.</span></td></tr>}
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
