import { redirect } from "next/navigation";
import { Badge, Card, PageHeader } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";

export default async function BillingReturnPage() {
  if (!await getCurrentUser()) redirect("/login");
  return <div className="space-y-6">
    <PageHeader eyebrow="Mercado Pago" title="Pagamento em confirmação" description="Recebemos seu retorno do checkout. O status será atualizado após a confirmação do Mercado Pago." />
    <Card className="mx-auto max-w-xl space-y-3 text-center">
      <Badge tone="warn" className="mx-auto">Aguardando confirmação</Badge>
      <p className="text-sm text-muted">Esta página não altera seu acesso. Consulte a situação atual em Planos e pagamentos.</p>
      <a href="/pagamentos" className="inline-block font-semibold text-primary underline">Ver meus pagamentos</a>
    </Card>
  </div>;
}
