import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { Badge, Button, Card, PageHeader } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";
import { cancelMonthlySubscription, startBillingCheckout, startPixCheckout } from "@/lib/billing/actions";

export const metadata: Metadata = { title: "Planos e pagamentos" };

const STATUS: Record<string, { label: string; tone: "ok" | "warn" | "neutral" }> = {
  PENDING: { label: "Aguardando pagamento", tone: "warn" },
  ACTIVE: { label: "Ativo", tone: "ok" },
  PAST_DUE: { label: "Pagamento pendente", tone: "warn" },
  CANCELLED: { label: "Cancelado", tone: "neutral" },
  EXPIRED: { label: "Encerrado", tone: "neutral" },
  REFUNDED: { label: "Estornado", tone: "neutral" },
  CHARGEBACK: { label: "Em contestação", tone: "warn" },
};

export default async function BillingPage({ searchParams }: { searchParams: Promise<{ erro?: string; status?: string }> }) {
  const query = await searchParams;
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const purchases = await db.billingPurchase.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
    include: { payments: { orderBy: { createdAt: "desc" }, take: 1 } },
  });
  const hasPermanent = purchases.some((p) => p.product === "PERMANENT" && p.status === "ACTIVE");
  const monthly = purchases.find((p) => p.product === "MONTHLY" && ["ACTIVE", "PENDING", "PAST_DUE"].includes(p.status));

  return (
    <div className="space-y-7">
      <PageHeader eyebrow="Conta" title="Planos e pagamentos" description="Confira seu acesso e escolha como apoiar a Missão Mentoria." />
      <div className="grid gap-4 md:grid-cols-2">
        <Card className="space-y-4">
          <div className="flex items-center justify-between gap-3"><h2 className="font-display text-xl font-bold">Mensal</h2><Badge>R$ 30/mês</Badge></div>
          <p className="text-sm leading-relaxed text-muted">Cobrança recorrente mensal pelo Mercado Pago. O acesso é liberado após a confirmação do pagamento.</p>
          {monthly?.status === "ACTIVE" ? <div className="space-y-3">
            <Badge tone="ok">Assinatura ativa</Badge>
            {monthly.currentPeriodEnd && <p className="text-sm text-muted">Próxima data de renovação: {monthly.currentPeriodEnd.toLocaleDateString("pt-BR")}.</p>}
            <form action={cancelMonthlySubscription}><input type="hidden" name="purchaseId" value={monthly.id} /><Button type="submit" variant="secondary" size="sm">Cancelar assinatura</Button></form>
          </div> : monthly ? <div className="space-y-2">
            <Badge tone={STATUS[monthly.status]?.tone ?? "neutral"}>{STATUS[monthly.status]?.label ?? monthly.status}</Badge>
            {monthly.checkoutUrl && monthly.status === "PENDING" && <a className="block text-sm font-semibold text-primary underline" href={monthly.checkoutUrl}>Continuar pagamento</a>}
          </div> : <form action={startBillingCheckout}><input type="hidden" name="product" value="MONTHLY" /><Button type="submit">Assinar por R$ 30/mês</Button></form>}
        </Card>

        <Card className="space-y-4">
          <div className="flex items-center justify-between gap-3"><h2 className="font-display text-xl font-bold">Acesso permanente</h2><Badge>R$ 50, pagamento único</Badge></div>
          <p className="text-sm leading-relaxed text-muted">Uma única cobrança. O acesso permanente é independente da assinatura mensal.</p>
          {hasPermanent ? <Badge tone="ok">Acesso permanente ativo</Badge> : <div className="flex flex-wrap gap-2">
            <form action={startBillingCheckout}><input type="hidden" name="product" value="PERMANENT" /><Button type="submit">Pagar com outras opções</Button></form>
            <form action={startPixCheckout}><Button type="submit" variant="secondary">Pagar com PIX · R$ 50</Button></form>
          </div>}
        </Card>
      </div>
      {purchases.length > 0 && <section className="space-y-3">
        <h2 className="font-display text-lg font-bold">Histórico</h2>
        <div className="space-y-2">{purchases.map((purchase) => <Card key={purchase.id} className="flex flex-wrap items-center justify-between gap-3 p-4">
          <div><p className="font-semibold">{purchase.product === "MONTHLY" ? "Mensal" : "Acesso permanente"} · R$ {Number(purchase.amount).toFixed(2).replace(".", ",")}</p>
            <p className="text-xs text-muted">{purchase.createdAt.toLocaleDateString("pt-BR")}{purchase.payments[0]?.statusDetail ? ` · ${purchase.payments[0].statusDetail}` : ""}</p></div>
          <Badge tone={STATUS[purchase.status]?.tone ?? "neutral"}>{STATUS[purchase.status]?.label ?? purchase.status}</Badge>
        </Card>)}</div>
      </section>}
      {query.erro === "pix" && <Card tone="soft"><p className="text-sm text-danger">Não foi possível gerar o PIX. Tente novamente mais tarde ou escolha outra forma de pagamento.</p></Card>}
      {query.erro === "checkout" && <Card tone="soft"><p className="text-sm text-danger">Não foi possível iniciar o checkout. Confira as credenciais do Mercado Pago.</p></Card>}
      <p className="text-xs leading-relaxed text-muted">A confirmação pode levar alguns instantes e é recebida diretamente do Mercado Pago. O retorno do checkout, por si só, não libera o acesso.</p>
    </div>
  );
}
