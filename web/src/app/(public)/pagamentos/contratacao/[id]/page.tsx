import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { PixStatic } from "@/components/pix-static";
import { mercadoPagoConfigured } from "@/lib/billing/mercado-pago";
import { Alert, Badge, Button, Card, PageHeader } from "@/components/ui";
import { isTestUser } from "@/lib/test-user";
import { confirmTestPayment } from "@/lib/test-user-actions";
import { getCurrentUser } from "@/lib/auth/session";
import { CONTRACT_STATUS, contestName, dateBR, discountSummary } from "@/lib/commerce/labels";
import { formatBRL, fromCents, toCents } from "@/lib/commerce/money";
import { db } from "@/lib/db";
import { OnlinePay } from "./online-pay";
import { buildPixPayload, pixConfig, pixQrDataUri } from "@/lib/pix";

export const metadata: Metadata = { title: "Pagamento da contratação" };

export default async function ContractPixPage({ params }: { params: Promise<{ id: string }> }) {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const { id } = await params;
  // só o próprio cliente vê a sua contratação (o id da URL não basta)
  const c = await db.contract.findFirst({ where: { id, OR: [{ userId: user.id }, { customerEmail: user.email.toLowerCase() }] }, include: { siteCoupons: { select: { code: true, appliedPoints: true } } } });
  if (!c) notFound();
  const due = toCents(c.finalAmount) - toCents(c.paidAmount);
  const online = mercadoPagoConfigured();
  const cfg = pixConfig();
  const st = CONTRACT_STATUS[c.status];
  let pix: { payload: string; qr: string } | null = null;
  // sem Mercado Pago configurado, vale o Pix estático (a administração confere e lança)
  if (!online && cfg && due > 0 && c.status !== "CANCELLED") {
    const txId = c.customerEmail.replace(/[^a-zA-Z0-9]/g, "").slice(0, 25) || "ALUNO";
    const payload = buildPixPayload({ ...cfg, amount: fromCents(due) }, c.customerEmail, txId);
    pix = { payload, qr: await pixQrDataUri(payload) };
  }

  return (
    <div className="space-y-6">
      <PageHeader eyebrow={contestName(c.contest)} title="Acesso ilimitado até a prova" description="Pagamento único, sem mensalidade, com acesso até a data da prova." />
      <Card className="mx-auto flex max-w-xl flex-wrap items-center justify-between gap-3">
        <div>
          <p className="text-sm font-semibold">
            <span className="text-muted line-through">De {formatBRL(toCents(c.originalAmount))}</span> por {formatBRL(toCents(c.finalAmount))}
          </p>
          <p className="text-xs text-muted">
            {discountSummary(c)}
            {toCents(c.paidAmount) > 0 ? ` · já recebido: ${formatBRL(toCents(c.paidAmount))}` : ""}
          </p>
        </div>
        <Badge tone={st.tone}>{st.label}</Badge>
      </Card>
      {due <= 0 ? (
        <Alert tone="info">
          {c.accessGrantedAt && c.accessUntil
            ? `Pagamento confirmado. Seu acesso está liberado até ${dateBR(c.accessUntil)}.`
            : c.accessGrantedAt
              ? "Pagamento confirmado. Seu acesso está liberado e valerá até o dia da prova, assim que a data oficial for divulgada."
              : "Pagamento confirmado. O acesso até a data da prova é liberado pela administração."}
        </Alert>
      ) : c.status === "CANCELLED" ? (
        <Alert tone="warn">Esta contratação foi cancelada. Faça uma nova contratação em Contratações e pagamentos.</Alert>
      ) : online ? (
        <OnlinePay contractId={c.id} dueCents={due} />
      ) : pix ? (
        <PixStatic amount={formatBRL(due)} payload={pix.payload} qr={pix.qr} />
      ) : (
        <Alert tone="warn">O pagamento ainda não está configurado. Tente novamente em breve.</Alert>
      )}
      {due > 0 && isTestUser(user.email) && (
        <form action={confirmTestPayment.bind(null, c.id)} className="mx-auto max-w-xl">
          <Button type="submit" size="lg" className="w-full">Confirmar pagamento</Button>
          <p className="mt-2 text-center text-xs text-muted">Teste local: reconhece o pagamento e libera o acesso até a prova.</p>
        </form>
      )}
      {due > 0 && (
        <p className="text-center text-xs leading-relaxed text-muted">
          {online
            ? "O pagamento é confirmado automaticamente pelo Mercado Pago e, em seguida, o acesso até a data da prova é liberado."
            : "A administração confere o pagamento e libera o acesso. A mensagem do Pix leva o seu e-mail para identificarmos o pagamento."}
        </p>
      )}
      {c.pricingRule.startsWith("TROCA:") && (
        <Link href="/perfil" className="block text-center text-sm font-semibold text-primary underline">
          {due <= 0 ? "Concluir a troca de concurso no perfil" : "Depois de pagar, volte ao perfil para concluir a troca de concurso"}
        </Link>
      )}
      <Link href="/pagamentos" className="block text-center text-sm font-semibold text-primary underline">Voltar a Contratações e pagamentos</Link>
    </div>
  );
}
