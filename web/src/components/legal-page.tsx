import Link from "next/link";
import type { ReactNode } from "react";
import { LEGAL } from "@/lib/legal";

/** Moldura dos documentos legais: título, data de atualização e seções numeradas. */
export function LegalDoc({ title, intro, children }: { title: string; intro: ReactNode; children: ReactNode }) {
  return (
    <article className="mx-auto max-w-3xl space-y-8 pt-2 sm:pt-6">
      <header className="space-y-2">
        <p className="text-xs font-bold uppercase tracking-widest text-muted">{LEGAL.brand}</p>
        <h1 className="font-display text-4xl font-bold uppercase tracking-wide sm:text-5xl">{title}</h1>
        <p className="text-sm text-muted">Última atualização: {LEGAL.updatedAt}</p>
        <div className="space-y-3 pt-2 text-[15px] leading-relaxed">{intro}</div>
      </header>
      <div className="space-y-8">{children}</div>
    </article>
  );
}

export function LegalSection({ n, title, children }: { n: number; title: string; children: ReactNode }) {
  return (
    <section className="space-y-3" aria-labelledby={`secao-${n}`}>
      <h2 id={`secao-${n}`} className="font-display text-2xl font-bold tracking-wide">
        {n}. {title}
      </h2>
      <div className="space-y-3 text-[15px] leading-relaxed [&_a]:font-semibold [&_a]:text-primary [&_a]:underline [&_ul]:list-disc [&_ul]:space-y-1.5 [&_ul]:pl-5">{children}</div>
    </section>
  );
}

/** Aviso de aceite, logo acima do botão que cria a conta ou gera o pagamento. */
export function LegalConsent() {
  return (
    <p className="text-center text-xs leading-relaxed text-muted">
      Ao continuar, você declara que leu e concorda com os{" "}
      <Link href="/termos" target="_blank" className="font-semibold text-primary underline">
        Termos de Uso
      </Link>{" "}
      e com a{" "}
      <Link href="/privacidade" target="_blank" className="font-semibold text-primary underline">
        Política de Privacidade
      </Link>
      .
    </p>
  );
}

/** Rodapé das páginas públicas e de entrada: leva aos dois documentos. */
export function LegalFooter() {
  return (
    <footer className="mx-auto w-full max-w-6xl px-5 pb-8 pt-4 text-center text-xs text-muted sm:px-8">
      <nav aria-label="Documentos legais" className="flex flex-wrap items-center justify-center gap-x-5 gap-y-1">
        <Link href="/termos" className="font-semibold underline-offset-2 hover:text-text hover:underline">
          Termos de Uso
        </Link>
        <Link href="/privacidade" className="font-semibold underline-offset-2 hover:text-text hover:underline">
          Política de Privacidade
        </Link>
      </nav>
      <p className="mt-2">
        {LEGAL.brand} · {LEGAL.companyName} · CNPJ {LEGAL.cnpj}
      </p>
    </footer>
  );
}
