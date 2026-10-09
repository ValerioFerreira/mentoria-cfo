"use client";

import { useId, useRef, useState, type CSSProperties, type ReactNode } from "react";
import { createPortal } from "react-dom";

const WIDTH = 256;
const MARGIN = 8;

/**
 * Balão informativo (?). O texto é desenhado num portal, direto no <body>, com posição fixa e a camada mais alta
 * da página: assim nenhum cartão, animação ou contexto de empilhamento por cima do botão cobre o balão.
 * Abre com o mouse, o foco (teclado) ou o toque, e fecha ao sair, ao rolar ou ao redimensionar.
 */
export function InfoTip({ children, label = "Mais informações", align = "center", className }: { children: ReactNode; label?: string; align?: "start" | "center" | "end"; className?: string }) {
  const btn = useRef<HTMLButtonElement>(null);
  const id = useId();
  const [style, setStyle] = useState<CSSProperties | null>(null);

  function open() {
    const el = btn.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const width = Math.min(WIDTH, vw - MARGIN * 2);
    const anchor = align === "start" ? r.left : align === "end" ? r.right - width : r.left + r.width / 2 - width / 2;
    const left = Math.max(MARGIN, Math.min(anchor, vw - width - MARGIN));
    // na metade de baixo da tela o balão sobe; na de cima, desce
    const below = r.bottom + 160 < vh || r.top < vh / 2;
    setStyle({ left, width, ...(below ? { top: r.bottom + 8 } : { bottom: vh - r.top + 8 }) });
    window.addEventListener("scroll", close, { capture: true, once: true });
    window.addEventListener("resize", close, { once: true });
  }
  function close() {
    setStyle(null);
  }

  return (
    <span className={`relative inline-flex align-middle ${className ?? ""}`}>
      <button
        ref={btn}
        type="button"
        aria-label={label}
        aria-describedby={style ? id : undefined}
        onMouseEnter={open}
        onMouseLeave={close}
        onFocus={open}
        onBlur={close}
        onClick={() => (style ? close() : open())}
        className="flex h-[18px] w-[18px] cursor-help items-center justify-center rounded-full border border-border-strong bg-surface-2 font-sans text-[11px] font-bold leading-none text-muted transition hover:border-primary hover:bg-primary hover:text-on-primary focus-visible:border-primary focus-visible:bg-primary focus-visible:text-on-primary"
      >
        ?
      </button>
      {style &&
        createPortal(
          <span
            id={id}
            role="tooltip"
            style={style}
            className="pointer-events-none fixed z-[2147483000] rounded-xl border border-border bg-surface p-3 text-left font-sans text-[12.5px] font-normal normal-case leading-snug tracking-normal text-text shadow-lift"
          >
            {children}
          </span>,
          document.body,
        )}
    </span>
  );
}
