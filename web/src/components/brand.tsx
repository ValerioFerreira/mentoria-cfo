import type { CSSProperties } from "react";

/** Contornos da chama (viewBox 24×24): casca externa, miolo e ponta quente. */
const OUTER = "M12 2.2c.4 3-1.4 4.7-2.9 6.6C7.6 10.6 6 12.4 6 15.4 6 19.3 8.6 22 12 22s6-2.7 6-6.6c0-2.2-.9-3.7-2-5-.1 1.5-.8 2.6-1.8 3.1.6-3.5-.2-7.5-2.2-11.3Z";
const MID = "M12 21.4c-2.4 0-4.1-1.8-4.1-4.2 0-1.7.9-2.8 1.9-3.8.7-.7 1.3-1.4 1.5-2.4 1.8 1.5 3.7 3.2 3.7 6.2 0 2.5-1.2 4.2-3 4.2Z";
const CORE = "M12 21.4c-1.3 0-2.1-1-2.1-2.3 0-1.3.7-1.9 1.4-2.6.4-.4.6-.7.7-1.2 1 .9 2.1 1.7 2.1 3.2 0 1.6-.9 2.9-2.1 2.9Z";

const PALETTE = {
  /** sobre o fundo vermelho da marca */
  tile: { outer: "#ffb62e", mid: "#ffd964", core: "#fff6d0" },
  /** sobre fundo escuro neutro */
  fire: { outer: "#ff5a36", mid: "#ff9a2e", core: "#ffe27a" },
} as const;

/** Chama que arde: três camadas oscilando em ritmos diferentes + brasas subindo. Só CSS (respeita prefers-reduced-motion). */
export function Flame({ className = "h-6 w-6", palette = "fire", embers = true }: { className?: string; palette?: keyof typeof PALETTE; embers?: boolean }) {
  const c = PALETTE[palette];
  return (
    <svg viewBox="0 0 24 24" className={`flame ${className}`} aria-hidden="true" overflow="visible">
      <path className="f-outer" d={OUTER} fill={c.outer} />
      <path className="f-mid" d={MID} fill={c.mid} />
      <path className="f-core" d={CORE} fill={c.core} />
      {embers && (
        <>
          <circle className="f-ember" cx="9.5" cy="5" r="0.7" fill={c.mid} style={{ "--d": "0s", "--x": "-2px" } as CSSProperties} />
          <circle className="f-ember" cx="14.5" cy="6" r="0.55" fill={c.outer} style={{ "--d": "0.9s", "--x": "2px" } as CSSProperties} />
          <circle className="f-ember" cx="12" cy="3.5" r="0.5" fill={c.core} style={{ "--d": "1.6s", "--x": "1px" } as CSSProperties} />
        </>
      )}
    </svg>
  );
}

/** Estrela de 5 pontas (insígnia do 2º Tenente). */
export function Star({ className = "h-4 w-4" }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} fill="currentColor" aria-hidden="true">
      <path d="m12 2.5 2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8L12 2.5Z" />
    </svg>
  );
}

export function BrandMark({ className = "h-9 w-9" }: { className?: string }) {
  return (
    <span className={`relative flex shrink-0 items-center justify-center rounded-[0.7rem] bg-primary text-on-primary shadow-[inset_0_1px_0_rgb(255_255_255/.3),0_8px_18px_-8px_var(--primary)] ${className}`}>
      <Flame palette="tile" className="h-[66%] w-[66%]" />
      <Star className="absolute -right-1 -top-1 h-3.5 w-3.5 text-gold drop-shadow" />
    </span>
  );
}

/** "MentorIA": as duas últimas letras (I + A = Inteligência Artificial) ganham um destaque sutil. */
export function Wordmark({ className }: { className?: string }) {
  return (
    <span className={className}>
      Mentor<span className="brand-ia">IA</span>
    </span>
  );
}

/** Marca. Sem `subtitle` mostra só o nome; dentro do app o menu passa o subtítulo da missão. */
export function Brand({ size = "md", inverse, subtitle }: { size?: "md" | "lg"; inverse?: boolean; subtitle?: string }) {
  return (
    <span className={`inline-flex items-center gap-2.5 ${inverse ? "text-on-ink" : "text-text"}`}>
      <BrandMark className={size === "lg" ? "h-11 w-11" : "h-9 w-9"} />
      <span className={`font-display font-bold leading-none tracking-wide ${size === "lg" ? "text-4xl" : "text-[1.65rem]"}`}>
        <Wordmark />
        {subtitle && (
          <span className="block font-semibold uppercase text-muted" style={{ letterSpacing: "0.16em", fontSize: "0.4em", marginTop: "0.3em", color: inverse ? "var(--on-ink-muted)" : undefined }}>
            {subtitle}
          </span>
        )}
      </span>
    </span>
  );
}
