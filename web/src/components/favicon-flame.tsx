"use client";

import { useEffect } from "react";
import { FLAME_FRAMES, flameFrameHref } from "@/lib/flame-frames";

/**
 * Anima o ícone da aba: troca o href do <link rel="icon"> (o do Next, em app/icon.svg) por uma sequência de quadros da
 * chama. Reaproveita o mesmo elemento para não ficar com dois ícones. Respeita "reduzir movimento".
 */
export function FaviconFlame() {
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    let link = document.querySelector<HTMLLinkElement>('link[rel~="icon"]');
    const created = !link;
    if (!link) {
      link = document.createElement("link");
      link.rel = "icon";
      document.head.appendChild(link);
    }
    const original = link.href;
    link.type = "image/svg+xml";
    let i = 0;
    const tick = () => {
      i = (i + 1) % FLAME_FRAMES;
      link.href = flameFrameHref(i);
    };
    tick();
    const id = window.setInterval(tick, 160);
    return () => {
      window.clearInterval(id);
      if (created) link.remove();
      else if (original) link.href = original;
    };
  }, []);
  return null;
}
