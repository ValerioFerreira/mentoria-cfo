"use client";

import { X } from "lucide-react";
import Image from "next/image";
import { useEffect, useId, useState, useSyncExternalStore } from "react";
import { createPortal } from "react-dom";
import { dismissNotice } from "@/lib/notices-actions";

const noop = () => () => {};
/** true só no navegador: o portal precisa de `document` (no servidor não há). */
function useIsClient() {
  return useSyncExternalStore(noop, () => true, () => false);
}

/**
 * Casca dos pop-ups de novidade (aviso dos PDFs, aviso do Reprogramar). O aviso é gravado como visto assim que aparece
 * (não depende do clique de fechar), então não volta mesmo que o aluno feche a aba ou navegue antes de dispensá-lo.
 * O botão principal deve ter o id `primaryId` para receber o foco.
 */
export function NoticeModal({
  noticeId,
  preview = false,
  primaryId,
  title,
  titleClassName = "text-4xl sm:text-5xl",
  subtitle,
  children,
  actions,
}: {
  noticeId: string;
  preview?: boolean;
  primaryId: string;
  title: React.ReactNode;
  titleClassName?: string;
  subtitle: React.ReactNode;
  children: React.ReactNode;
  actions: (close: (then?: () => void) => void) => React.ReactNode;
}) {
  const [open, setOpen] = useState(true);
  const titleId = useId();
  const isClient = useIsClient();

  useEffect(() => {
    if (!preview) void dismissNotice(noticeId);
  }, [noticeId, preview]);

  useEffect(() => {
    if (!isClient) return;
    document.getElementById(primaryId)?.focus();
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [isClient, primaryId]);

  function close(then?: () => void) {
    setOpen(false);
    then?.();
  }

  // portal no <body>: dentro da página, um ancestral com animação (transform) prenderia o `fixed` ao conteúdo
  if (!open || !isClient) return null;
  return createPortal(
    <div className="fixed inset-0 z-[100] flex items-end justify-center bg-black/60 p-3 backdrop-blur-sm sm:items-center sm:p-6" onClick={() => close()}>
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        onClick={(e) => e.stopPropagation()}
        className="rise relative max-h-full w-full max-w-lg overflow-y-auto overflow-x-hidden rounded-3xl border border-white/10 bg-ink text-on-ink shadow-2xl"
      >
        <div className="tape h-2 w-full" aria-hidden />
        <button
          type="button"
          onClick={() => close()}
          aria-label="Fechar aviso"
          className="absolute right-3 top-5 z-10 cursor-pointer rounded-full p-1.5 text-on-ink-muted transition hover:bg-white/10 hover:text-on-ink"
        >
          <X className="h-5 w-5" aria-hidden />
        </button>

        <div className="relative px-6 pb-2 pt-6 sm:px-8">
          <Image
            src="/mascote/chama-bizu.png"
            alt=""
            width={600}
            height={600}
            priority
            className="pointer-events-none absolute right-2 top-12 h-24 w-24 drop-shadow-[0_10px_24px_rgba(233,169,12,0.35)] sm:-right-1 sm:top-0 sm:h-44 sm:w-44"
          />
          <span className="inline-flex items-center gap-1.5 rounded-full bg-gold px-3 py-1 font-display text-xs font-bold uppercase tracking-[0.14em] text-ink">
            <span className="h-1.5 w-1.5 rounded-full bg-ink" aria-hidden />
            Novidade
          </span>
          <h2 id={titleId} className={`mt-4 max-w-[calc(100%-6.5rem)] font-display font-bold uppercase leading-[0.95] tracking-wide sm:max-w-[19rem] ${titleClassName}`}>
            {title}
          </h2>
          <p className="mt-3 text-sm leading-relaxed text-on-ink-muted sm:max-w-[19rem]">{subtitle}</p>
        </div>

        <ul className="space-y-3 px-6 pb-2 pt-4 sm:px-8">{children}</ul>

        <div className="flex flex-col gap-2 px-6 pb-6 pt-5 sm:flex-row-reverse sm:px-8">{actions(close)}</div>
      </div>
    </div>,
    document.body,
  );
}

export function NoticeItem({ icon, children }: { icon: React.ReactNode; children: React.ReactNode }) {
  return (
    <li className="flex items-start gap-3 text-sm leading-relaxed text-on-ink-muted">
      <span className="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-white/10 text-gold">{icon}</span>
      <span className="pt-1">{children}</span>
    </li>
  );
}
