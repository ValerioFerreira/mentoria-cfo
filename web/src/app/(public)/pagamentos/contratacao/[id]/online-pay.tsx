"use client";

import { CreditCard, Loader2, QrCode } from "lucide-react";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { PixStatic } from "@/components/pix-static";
import { Button, Card } from "@/components/ui";
import { checkPayment, createCardCheckout, createPix, type PixPayload } from "@/lib/commerce/online-actions";
import { formatBRL } from "@/lib/commerce/money";

const POLL_MS = 6000;

/** Escolha entre Pix (QR Code na tela, confirmação automática) e cartão (página do Mercado Pago). */
export function OnlinePay({ contractId, dueCents }: { contractId: string; dueCents: number }) {
  const router = useRouter();
  const [pix, setPix] = useState<PixPayload | null>(null);
  const [busy, setBusy] = useState<"pix" | "card" | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function startPix() {
    setBusy("pix");
    setError(null);
    const r = await createPix(contractId);
    setBusy(null);
    if (r.ok && r.data) setPix(r.data);
    else setError(r.message);
  }

  async function startCard() {
    setBusy("card");
    setError(null);
    const r = await createCardCheckout(contractId);
    if (r.ok && r.data) {
      window.location.assign(r.data.url);
      return;
    }
    setBusy(null);
    setError(r.message);
  }

  // com o Pix na tela, confere o pagamento a cada poucos segundos e atualiza a página quando confirmar
  useEffect(() => {
    if (!pix) return;
    let stopped = false;
    const timer = setInterval(async () => {
      const r = await checkPayment(contractId);
      if (!stopped && r.ok && r.data?.paid) {
        stopped = true;
        clearInterval(timer);
        router.refresh();
      }
    }, POLL_MS);
    return () => {
      stopped = true;
      clearInterval(timer);
    };
  }, [pix, contractId, router]);

  return (
    <div className="mx-auto max-w-xl space-y-5">
      {!pix && (
        <Card className="space-y-4">
          <p className="text-sm text-muted">Valor a pagar agora</p>
          <p className="font-display text-3xl font-bold tabular">{formatBRL(dueCents)}</p>
          <div className="grid gap-3 sm:grid-cols-2">
            <Button type="button" onClick={startPix} disabled={busy !== null} className="w-full">
              {busy === "pix" ? <Loader2 className="h-4 w-4 animate-spin" aria-hidden /> : <QrCode className="h-4 w-4" aria-hidden />}
              Pagar com Pix
            </Button>
            <Button type="button" variant="secondary" onClick={startCard} disabled={busy !== null} className="w-full">
              {busy === "card" ? <Loader2 className="h-4 w-4 animate-spin" aria-hidden /> : <CreditCard className="h-4 w-4" aria-hidden />}
              Pagar com cartão
            </Button>
          </div>
          {error && <p role="alert" className="text-sm text-primary">{error}</p>}
        </Card>
      )}
      {pix && (
        <>
          <PixStatic
            amount={formatBRL(pix.amountCents)}
            payload={pix.qrCode}
            qr={pix.qrCodeBase64.startsWith("data:") ? pix.qrCodeBase64 : `data:image/png;base64,${pix.qrCodeBase64}`}
          />
          <p role="status" className="text-center text-sm text-muted">
            Aguardando o pagamento… esta página atualiza sozinha quando o Pix for confirmado.
            {pix.expiresAt ? ` O código vale até ${new Date(pix.expiresAt).toLocaleString("pt-BR", { timeZone: "America/Recife" })}.` : ""}
          </p>
        </>
      )}
    </div>
  );
}
