import { notFound, redirect } from "next/navigation";
import { Badge, Card, PageHeader } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";
import { PixPaymentDetails } from "./pix-payment-details";

export default async function PixPaymentPage({ params }: { params: Promise<{ purchaseId: string }> }) {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const { purchaseId } = await params;
  const purchase = await db.billingPurchase.findFirst({
    where: { id: purchaseId, userId: user.id, product: "PERMANENT" },
    select: {
      amount: true,
      status: true,
      pixQrCode: true,
      pixQrCodeBase64: true,
      pixTicketUrl: true,
      pixExpiresAt: true,
      payments: { orderBy: { createdAt: "desc" }, take: 1, select: { status: true } },
    },
  });
  if (!purchase) notFound();

  if (purchase.status === "ACTIVE") {
    return <div className="space-y-5">
      <PageHeader eyebrow="PIX" title="Pagamento confirmado" description="Seu acesso permanente está ativo." />
      <Badge tone="ok">Acesso permanente ativo</Badge>
      <a href="/pagamentos" className="block font-semibold text-primary underline">Voltar a Contratações e pagamentos</a>
    </div>;
  }
  if (!purchase.pixQrCode || !purchase.pixQrCodeBase64) notFound();
  const pixExpired = (purchase.pixExpiresAt && purchase.pixExpiresAt <= new Date())
    || purchase.payments[0]?.status === "CANCELLED"
    || purchase.payments[0]?.status === "REJECTED";

  return <div className="space-y-6">
    <PageHeader eyebrow="PIX" title="Conclua seu pagamento" description="Pague pelo app do seu banco usando o QR Code ou o código copia e cola." />
    {pixExpired ? <Card className="mx-auto max-w-xl space-y-4 text-center">
      <Badge tone="warn" className="mx-auto">PIX expirado ou cancelado</Badge>
      <p className="text-sm text-muted">Este código não vale mais. Para contratar o acesso até a prova, volte a Contratações e pagamentos.</p>
    </Card> : <>
      <div className="text-center"><Badge tone="warn">Aguardando pagamento</Badge></div>
      <PixPaymentDetails
        amount={Number(purchase.amount).toFixed(2).replace(".", ",")}
        qrCode={purchase.pixQrCode}
        qrCodeBase64={purchase.pixQrCodeBase64}
        ticketUrl={purchase.pixTicketUrl}
        expiresAt={purchase.pixExpiresAt?.toISOString() ?? null}
      />
    </>}
    <a href="/pagamentos" className="block text-center text-sm font-semibold text-primary underline">Voltar a Contratações e pagamentos</a>
  </div>;
}
