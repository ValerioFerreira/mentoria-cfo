"use client";

import Image from "next/image";
import { useState } from "react";
import { Button, Card } from "@/components/ui";

/** QR Code e "copia e cola" de um Pix estático com valor fixo calculado no servidor. */
export function PixStatic({ amount, payload, qr }: { amount: string; payload: string; qr: string }) {
  const [copied, setCopied] = useState(false);
  const [copyError, setCopyError] = useState(false);

  async function copyCode() {
    try {
      await navigator.clipboard.writeText(payload);
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
        <p className="font-display text-3xl font-bold tabular">{amount}</p>
        <Image unoptimized src={qr} alt="QR Code Pix para pagamento" width={256} height={256} className="mx-auto h-64 w-64 rounded-xl border border-border bg-white p-2" />
        <p className="text-sm text-muted">Abra o app do seu banco e escaneie o QR Code, ou copie o código abaixo.</p>
      </Card>
      <Card className="space-y-3">
        <label htmlFor="pix-code" className="text-sm font-semibold">Pix copia e cola</label>
        <textarea id="pix-code" readOnly value={payload} rows={4} className="w-full resize-y rounded-lg border border-border bg-surface-2 p-3 font-mono text-xs text-text" />
        <Button type="button" onClick={copyCode} className="w-full">{copied ? "Código copiado" : "Copiar código Pix"}</Button>
        {copyError && <p role="alert" className="text-sm text-primary">Não foi possível copiar automaticamente. Selecione e copie o código acima.</p>}
      </Card>
    </div>
  );
}
