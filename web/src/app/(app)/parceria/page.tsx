import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { Badge, Card, PageHeader, Stat } from "@/components/ui";
import { requirePartner } from "@/lib/auth/dal";
import { contestName, dateBR } from "@/lib/commerce/labels";
import { formatBRL } from "@/lib/commerce/money";
import { COMMISSION_HOLD_DAYS, COMMISSION_RATE_BP } from "@/lib/commerce/pricing";
import { MIN_CONVERSION_SAMPLE, partnerDashboard } from "@/lib/commerce/queries";

export const metadata: Metadata = { title: "Minha parceria" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";
const TYPE = { COMISSAO: "Comissão gerada", REVERSAO: "Comissão revertida", REPASSE: "Repasse recebido" } as const;

export default async function PartnershipPage() {
  // o painel é sempre do parceiro da sessão: nenhum identificador vem do navegador
  const user = await requirePartner();
  const d = await partnerDashboard(user.id);
  if (!d) redirect("/");
  const b = d.balance;

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Gestão"
        title="Minha parceria"
        description={`Seu cupom dá ${d.discountPoints} pontos percentuais a mais de desconto. Você recebe ${COMMISSION_RATE_BP / 100}% do valor efetivamente pago pelos clientes indicados.`}
      />

      <Card tone="ink" className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Seu cupom exclusivo</p>
          <p className="font-display text-4xl font-bold tracking-wide text-gold">{d.coupon?.code ?? "—"}</p>
        </div>
        {d.coupon ? <Badge tone="gold">+{d.coupon.discountPoints}% de desconto ao cliente</Badge> : <Badge tone="neutral">Sem cupom ativo: fale com a administração</Badge>}
      </Card>

      <section className="space-y-3" aria-labelledby="indicacoes">
        <h2 id="indicacoes" className="font-display text-lg font-bold uppercase">Indicações</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          <Stat label="Usuários indicados" value={d.referredUsers} hint="Únicos, pelo cupom" />
          <Stat label="Clientes pagantes" value={d.payingUsers} />
          <Stat
            label="Conversão"
            value={d.conversion === null ? "—" : `${Math.round(d.conversion * 100)}%`}
            hint={d.conversion === null ? `Aparece a partir de ${MIN_CONVERSION_SAMPLE} indicados` : undefined}
          />
          <Stat label="Contratações" value={d.contracts} hint={`Recebido dos clientes: ${formatBRL(d.receivedCents)}`} />
        </div>
      </section>

      <section className="space-y-3" aria-labelledby="comissoes">
        <h2 id="comissoes" className="font-display text-lg font-bold uppercase">Comissões e repasses</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          <Stat label="Comissões geradas" value={formatBRL(b.generatedCents)} />
          <Stat label="Comissões revertidas" value={formatBRL(b.reversedCents)} hint="Por estornos de clientes" />
          <Stat label="Total recebido em repasses" value={formatBRL(b.paidOutCents)} />
          <Stat label="Saldo disponível" value={formatBRL(b.availableCents)} />
          <Stat label="Pendente de confirmação" value={formatBRL(b.pendingCents)} hint={`Fica disponível ${COMMISSION_HOLD_DAYS} dias após o pagamento (garantia)`} />
          <Stat label="Saldo negativo a compensar" value={formatBRL(b.negativeCents)} hint="Descontado das próximas comissões" />
        </div>
      </section>

      <section className="space-y-2" aria-labelledby="historico">
        <h2 id="historico" className="font-display text-lg font-bold uppercase">Histórico</h2>
        <Card className="overflow-x-auto p-0">
          <table className="w-full min-w-[560px] text-sm">
            <thead className="border-b border-border"><tr><th className={th}>Data</th><th className={th}>Movimento</th><th className={th}>Concurso</th><th className={th}>Valor</th><th className={th}>Situação</th></tr></thead>
            <tbody>
              {d.history.length === 0 && <tr><td className={td} colSpan={5}><span className="text-muted">Nenhum movimento ainda. Divulgue o seu cupom!</span></td></tr>}
              {d.history.map((h) => (
                <tr key={`${h.type}-${h.id}`} className="border-b border-border/60 last:border-0">
                  <td className={td}>{dateBR(h.date)}</td>
                  <td className={td}>{TYPE[h.type]}</td>
                  <td className={td}>{h.contest ? contestName(h.contest) : "—"}</td>
                  <td className={`${td} tabular whitespace-nowrap ${h.amountCents < 0 ? "text-primary" : ""}`}>{formatBRL(h.amountCents)}</td>
                  <td className={`${td} text-xs`}>{h.type === "REPASSE" ? "Pago" : h.pending ? `Disponível em ${dateBR(h.availableAt)}` : "Confirmada"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </section>
    </div>
  );
}
