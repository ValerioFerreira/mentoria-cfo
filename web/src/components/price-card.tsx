import { Check } from "lucide-react";
import type { ReactNode } from "react";
import { Star } from "@/components/brand";

/** Valores já calculados no servidor (lib/commerce/pricing); o componente só exibe. */
export interface PriceCardData {
  badge: string;
  originalCents: number;
  finalCents: number;
}

export const ACCESS_TITLE = "Acesso ilimitado";
export const ACCESS_DESCRIPTION = "Pagamento único, sem mensalidade, com acesso até a data da prova.";
export const ACCESS_HIGHLIGHT = "Acesso ilimitado até a prova do concurso.";

const reais = (cents: number) => Math.floor(cents / 100).toLocaleString("pt-BR");
const centavos = (cents: number) => String(cents % 100).padStart(2, "0");

/**
 * Card de preço (fundo azul-escuro, borda amarela, faixa superior, selo de lançamento, preço riscado e promocional).
 * Com `radio`, o card inteiro vira a opção selecionável (radio nativo escondido; teclado e leitor de tela funcionam).
 */
export function PriceCard({ data, radio, footer, className = "" }: { data: PriceCardData; radio?: { name: string; value: string; defaultChecked?: boolean }; footer?: ReactNode; className?: string }) {
  const Tag = radio ? "label" : "div";
  return (
    <Tag
      className={`group relative flex flex-col gap-4 overflow-hidden rounded-2xl border border-gold/60 bg-ink p-5 pt-6 text-on-ink shadow-lift transition ${
        radio ? "cursor-pointer hover:-translate-y-0.5 has-[:checked]:ring-2 has-[:checked]:ring-gold has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-offset-2 has-[:focus-visible]:outline-primary" : ""
      } ${className}`}
    >
      {radio && <input type="radio" name={radio.name} value={radio.value} defaultChecked={radio.defaultChecked} className="sr-only" />}
      <div className="tape tape-rule absolute inset-x-0 top-0 !rounded-none" aria-hidden />
      {radio && (
        <span className="absolute right-4 top-4 grid h-6 w-6 place-items-center rounded-full border-2 border-on-ink-muted transition group-has-[:checked]:border-gold group-has-[:checked]:bg-gold" aria-hidden>
          <Check className="h-3.5 w-3.5 text-ink opacity-0 transition group-has-[:checked]:opacity-100" />
        </span>
      )}
      <span className="inline-flex w-fit items-center gap-1.5 rounded-full bg-gold px-2.5 py-1 text-xs font-bold text-ink">
        <Star className="h-3 w-3" />
        {data.badge}
      </span>
      <span className="space-y-1">
        <span className="block font-display text-2xl font-bold uppercase leading-none">{ACCESS_TITLE}</span>
        <span className="block text-sm font-semibold text-on-ink-muted line-through">
          De R$ {reais(data.originalCents)},{centavos(data.originalCents)}
        </span>
        <span className="flex flex-wrap items-baseline gap-x-1.5">
          <span className="font-display text-xl font-semibold text-gold">R$</span>
          <span className="tabular font-display text-6xl font-bold leading-none">{reais(data.finalCents)}</span>
          <span className="font-display text-2xl font-bold leading-none">,{centavos(data.finalCents)}</span>
          <span className="sr-only">Preço promocional: R$ {reais(data.finalCents)},{centavos(data.finalCents)}</span>
        </span>
      </span>
      <span className="space-y-1 text-sm text-on-ink-muted">
        <span className="block">{ACCESS_DESCRIPTION}</span>
        <span className="block font-semibold text-gold">{ACCESS_HIGHLIGHT}</span>
      </span>
      {footer}
    </Tag>
  );
}
