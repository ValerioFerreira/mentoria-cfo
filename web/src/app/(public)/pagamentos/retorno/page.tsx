import { redirect } from "next/navigation";
import { Badge, Card, PageHeader } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { toCents } from "@/lib/commerce/money";
import { syncProviderPayment } from "@/lib/commerce/online";
import { db } from "@/lib/db";

type SearchParams = Record<string, string | string[] | undefined>;
const one = (v: string | string[] | undefined) => (typeof v === "string" ? v : undefined);

/**
 * Retorno do Checkout Pro. O endereço é só informativo: o acesso nunca nasce daqui. Quando o Mercado Pago informa o
 * número do pagamento, ele é CONSULTADO na API autenticada (a mesma conciliação do webhook, idempotente) para a
 * confirmação aparecer sem esperar o aviso.
 */
export default async function BillingReturnPage({ searchParams }: { searchParams: Promise<SearchParams> }) {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const sp = await searchParams;
  const contractId = one(sp.contrato);
  const paymentId = one(sp.payment_id) ?? one(sp.collection_id);

  let confirmed = false;
  if (contractId) {
    const own = await db.contract.findFirst({ where: { id: contractId, OR: [{ userId: user.id }, { customerEmail: user.email.toLowerCase() }] }, select: { id: true } });
    if (own) {
      if (paymentId && /^\d{4,20}$/.test(paymentId)) {
        try {
          await syncProviderPayment(paymentId);
        } catch (err) {
          console.error("[online-payment] retorno do checkout", err instanceof Error ? err.message : "erro");
        }
      }
      const c = await db.contract.findUniqueOrThrow({ where: { id: own.id }, select: { finalAmount: true, paidAmount: true, status: true } });
      confirmed = c.status !== "CANCELLED" && toCents(c.finalAmount) - toCents(c.paidAmount) <= 0;
    }
  }

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Mercado Pago"
        title={confirmed ? "Pagamento confirmado" : "Pagamento em confirmação"}
        description={confirmed ? "Recebemos o seu pagamento." : "Recebemos seu retorno do checkout. O status será atualizado após a confirmação do Mercado Pago."}
      />
      <Card className="mx-auto max-w-xl space-y-3 text-center">
        <Badge tone={confirmed ? "ok" : "warn"} className="mx-auto">{confirmed ? "Pago" : "Aguardando confirmação"}</Badge>
        <p className="text-sm text-muted">
          {confirmed ? "O acesso até a data da prova é liberado assim que a confirmação é processada." : "Esta página não altera seu acesso. Consulte a situação atual em Contratações e pagamentos."}
        </p>
        <a href="/pagamentos" className="inline-block font-semibold text-primary underline">Ver meus pagamentos</a>
      </Card>
    </div>
  );
}
