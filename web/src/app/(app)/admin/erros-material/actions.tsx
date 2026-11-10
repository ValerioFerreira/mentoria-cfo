"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { Button, inputCls } from "@/components/ui";
import { resolveMaterialReport } from "@/lib/admin/actions";

export function MaterialReportActions({ id, status }: { id: string; status: string }) {
  const [note, setNote] = useState("");
  const [pending, start] = useTransition();
  const router = useRouter();
  const run = (s: "RESOLVED" | "DISCARDED" | "OPEN") =>
    start(async () => {
      await resolveMaterialReport(id, s, note);
      router.refresh();
    });
  return (
    <div className="flex flex-wrap items-center gap-2">
      {status === "OPEN" ? (
        <>
          <input value={note} onChange={(e) => setNote(e.target.value)} placeholder="Observação (opcional)" maxLength={500} className={`${inputCls} max-w-sm`} />
          <Button size="sm" disabled={pending} onClick={() => run("RESOLVED")}>Marcar como corrigido</Button>
          <Button size="sm" variant="secondary" disabled={pending} onClick={() => run("DISCARDED")}>Descartar</Button>
        </>
      ) : (
        <Button size="sm" variant="secondary" disabled={pending} onClick={() => run("OPEN")}>Reabrir</Button>
      )}
    </div>
  );
}
