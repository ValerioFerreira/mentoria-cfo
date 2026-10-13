"use client";

import { useState } from "react";
import Image from "next/image";
import { Button, Card } from "@/components/ui";

export function PixPaymentDetails({
  amount,
  qrCode,
  qrCodeBase64,
  ticketUrl,
  expiresAt,
}: {
  amount: string;
  qrCode: string;
  qrCodeBase64: string;
  ticketUrl: string | null;
  expiresAt: string | null;
}) {
  const [copied, setCopied] = useState(false);
  const [copyError, setCopyError] = useState(false);
  const imageSource = qrCodeBase64.startsWith("data:") ? qrCodeBase64 : `data:image/png;base64,${qrCodeBase64}`;

  async function copyCode() {
    try {
      await navigator.clipboard.writeText(qrCode);
      setCopied(true);
      setCopyError(false);
    } catch {
      setCopied(false);
      setCopyError(true);
    }
  }

  return (
    <div className="mx-auto max-w-xl space-y-5">
      <Card className="space-y-4 text-center">
        <p className="text-sm text-muted">Valor do pagamento</p>
        <p className="font-display text-2xl font-bold">R$ {amount}</p>
        <Image unoptimized src={imageSource} alt="QR Code Pix para pagamento" width={256} height={256} className="mx-auto h-64 w-64 rounded-xl border border-border p-2" />
        {expiresAt && <p className="text-sm text-muted">Este PIX vence em {new Date(expiresAt).toLocaleString("pt-BR")}.</p>}
        <p className="text-sm text-muted">Abra o app do seu banco e escaneie o QR Code, ou copie o código abaixo.</p>
      </Card>
      <Card className="space-y-3">
        <label htmlFor="pix-code" className="text-sm font-semibold">PIX copia e cola</label>
        <textarea id="pix-code" readOnly value={qrCode} rows={4} className="w-full resize-y rounded-lg border border-border bg-surface-2 p-3 text-xs text-text" />
        <Button type="button" onClick={copyCode} className="w-full">{copied ? "Código copiado" : "Copiar código PIX"}</Button>
        {copyError && <p role="alert" className="text-sm text-danger">Não foi possível copiar automaticamente. Selecione e copie o código acima.</p>}
        {ticketUrl && <a className="block text-center text-sm font-semibold text-primary underline" href={ticketUrl} target="_blank" rel="noreferrer">Abrir instruções do Mercado Pago</a>}
      </Card>
      <p className="text-center text-xs leading-relaxed text-muted">A confirmação pode levar alguns instantes. Depois de pagar, confira o status em Planos e pagamentos.</p>
    </div>
  );
}
