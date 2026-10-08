"use client";

import { Check, Moon, Palette, Sun, Coffee } from "lucide-react";
import { useEffect, useRef, useState, useSyncExternalStore } from "react";
import { cx } from "@/components/ui";

export type Theme = "light" | "sepia" | "dark";
const OPTIONS: { id: Theme; label: string; hint: string; Icon: typeof Sun; swatch: string }[] = [
  { id: "light", label: "Claro", hint: "Fundo branco-azulado", Icon: Sun, swatch: "linear-gradient(135deg,#ffffff 50%,#edf0f4 50%)" },
  { id: "sepia", label: "Sépia", hint: "Papel quente, leitura longa", Icon: Coffee, swatch: "linear-gradient(135deg,#faf3e3 50%,#e9dcc0 50%)" },
  { id: "dark", label: "Dark", hint: "Fundo escuro", Icon: Moon, swatch: "linear-gradient(135deg,#14233a 50%,#080f1a 50%)" },
];

const subscribe = (cb: () => void) => {
  window.addEventListener("theme:changed", cb);
  return () => window.removeEventListener("theme:changed", cb);
};
function read(): Theme {
  const t = document.documentElement.dataset.theme;
  if (t === "light" || t === "sepia" || t === "dark") return t;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(t: Theme) {
  try {
    document.documentElement.dataset.theme = t;
    document.cookie = `theme=${t}; path=/; max-age=31536000; samesite=lax`;
  } catch {}
  window.dispatchEvent(new Event("theme:changed"));
}

/** Botão "Aparência" (canto superior direito): Claro, Sépia ou Dark. A escolha fica em cookie e é aplicada já no servidor. */
export function AppearanceMenu({ initial, inverse }: { initial?: Theme | null; inverse?: boolean }) {
  const theme = useSyncExternalStore(subscribe, read, () => initial ?? "light");
  const [open, setOpen] = useState(false);
  const box = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const away = (e: MouseEvent) => !box.current?.contains(e.target as Node) && setOpen(false);
    const esc = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("mousedown", away);
    document.addEventListener("keydown", esc);
    return () => {
      document.removeEventListener("mousedown", away);
      document.removeEventListener("keydown", esc);
    };
  }, [open]);

  function choose(t: Theme) {
    applyTheme(t);
    setOpen(false);
  }

  return (
    <div ref={box} className="relative">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        aria-haspopup="menu"
        aria-expanded={open}
        aria-label="Aparência"
        className={cx(
          "inline-flex cursor-pointer items-center gap-2 rounded-xl border px-3 py-2 text-[13px] font-semibold transition active:scale-95",
          inverse ? "border-white/15 bg-white/10 text-on-ink hover:bg-white/20" : "border-border bg-surface text-text shadow-card hover:border-border-strong",
        )}
      >
        <Palette className="h-4 w-4" aria-hidden />
        <span className="hidden sm:inline">Aparência</span>
      </button>
      {open && (
        <div role="menu" aria-label="Aparência" className="pop absolute right-0 top-full z-50 mt-2 w-60 origin-top-right rounded-2xl border border-border bg-surface p-1.5 text-text shadow-lift">
          {OPTIONS.map((o) => (
            <button
              key={o.id}
              type="button"
              role="menuitemradio"
              aria-checked={theme === o.id}
              onClick={() => choose(o.id)}
              className={cx("flex w-full cursor-pointer items-center gap-3 rounded-xl px-3 py-2.5 text-left transition", theme === o.id ? "bg-primary-soft" : "hover:bg-surface-2")}
            >
              <span className="h-8 w-8 shrink-0 rounded-lg border border-border-strong" style={{ background: o.swatch }} aria-hidden />
              <span className="min-w-0 flex-1">
                <span className="block text-sm font-semibold leading-tight">{o.label}</span>
                <span className="block text-xs text-muted">{o.hint}</span>
              </span>
              {theme === o.id && <Check className="h-4 w-4 text-primary" aria-hidden />}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
