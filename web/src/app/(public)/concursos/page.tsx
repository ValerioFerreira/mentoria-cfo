import { RouteNavigationTrap } from "@/components/route-navigation-trap";
import { ArrowLeft, ArrowRight } from "lucide-react";
import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { contestBySlug, type ContestInfo } from "@/lib/contests";

// um contêiner por órgão, na ordem pedida; dentro, os concursos disponíveis (o Combo recebe um selo de destaque)
const GROUPS: { org: string; name: string; slugs: string[] }[] = [
  { org: "CBMPE", name: "Bombeiros", slugs: ["cbmpe-soldado", "cbmpe-oficial", "cbmpe-cfoa", "cbmpe-combo"] },
  { org: "PMPE", name: "Polícia Militar", slugs: ["pmpe-soldado", "pmpe-oficial", "pmpe-combo"] },
  { org: "PCPE", name: "Polícia Civil", slugs: ["pcpe-agente"] },
];

export const metadata: Metadata = { title: "Escolha seu concurso" };

export default async function ContestsPage() {
  if (await getCurrentUser()) redirect("/");
  return (
    <div className="mx-auto flex max-w-6xl flex-col items-center space-y-5 pt-1 text-center sm:pt-4">
      <RouteNavigationTrap targetUrl="/" />
      <div className="w-full text-left">
        <Link href="/" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Voltar para o início
        </Link>
      </div>
      <div className="mx-auto max-w-2xl space-y-2">
        <p className="eyebrow">MentorIA · Plano de estudos</p>
        <h1 className="font-display text-4xl font-bold uppercase leading-[0.92] sm:text-6xl">
          Qual é a sua <span className="text-primary">missão?</span>
        </h1>
      </div>
      <div className="grid w-full gap-4 text-left lg:grid-cols-3 lg:items-start">
        {GROUPS.map((g, gi) => (
          <section key={g.org} aria-labelledby={`org-${g.org}`} className="rise rounded-2xl border border-border bg-surface-2/60 p-3 sm:p-4" style={{ ["--i" as string]: gi * 0.6 }}>
            <header className="mb-3 flex items-baseline justify-between gap-2 px-1">
              <h2 id={`org-${g.org}`} className="font-display text-3xl font-bold uppercase leading-none">{g.org}</h2>
              <p className="text-xs font-semibold uppercase tracking-wider text-muted">{g.name}</p>
            </header>
            <ul className="space-y-3">
              {g.slugs.map((slug) => {
                const c = contestBySlug(slug)!;
                return (
                  <li key={c.slug}>
                    <ContestCard c={c} />
                  </li>
                );
              })}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}

// tom discreto por órgão: vermelho (CBMPE), preto (PMPE) e azul (PCPE)
const ORG_TONE: Record<ContestInfo["org"], { fade: string; border: string }> = {
  CBMPE: { fade: "from-red-950 via-red-950/70", border: "border-red-500/30" },
  PMPE: { fade: "from-black via-black/75", border: "border-white/20" },
  PCPE: { fade: "from-blue-950 via-blue-950/70", border: "border-blue-400/30" },
};

function ContestCard({ c }: { c: ContestInfo }) {
  const combo = c.category === "Combo";
  const tone = ORG_TONE[c.org];
  return (
    <Link
      href={`/lista-de-espera/${c.slug}`}
      className={`group relative flex min-h-[5.5rem] items-end overflow-hidden rounded-xl border ${tone.border} bg-ink text-on-ink shadow-card outline-none transition duration-300 hover:-translate-y-0.5 hover:border-primary/60 hover:shadow-lift focus-visible:-translate-y-0.5 focus-visible:ring-2 focus-visible:ring-primary`}
    >
      <div className={`absolute inset-0 bg-gradient-to-r ${tone.fade} to-ink`} aria-hidden />
      {/* brasão inteiro dentro do card, com fade leve nas laterais; mesma posição em todos os cards do órgão */}
      <div className="pointer-events-none absolute inset-y-1.5 right-12 w-24 [mask-image:linear-gradient(to_right,transparent,black_25%,black_80%,transparent)]" aria-hidden>
        <Image
          src={c.image}
          alt=""
          fill
          sizes="96px"
          className="object-contain opacity-80 transition duration-500 group-hover:scale-105 group-hover:opacity-100"
        />
      </div>
      <div className="absolute inset-y-0 left-0 w-1 origin-top scale-y-0 bg-primary transition duration-500 group-hover:scale-y-100" aria-hidden />
      <div className="relative flex w-full items-center justify-between gap-3 py-2.5 pl-3 pr-12">
        <div className="min-w-0 pr-6">
          <p className="flex flex-wrap items-center gap-x-2 gap-y-1 text-[11px] font-semibold uppercase tracking-wider text-on-ink-muted">
            {c.category || "Cargo"}
            {combo && <span className="whitespace-nowrap rounded-full bg-gold px-2 py-0.5 text-[10px] font-bold text-ink">Estude os dois e economize</span>}
            {!c.available && <span className="rounded-full bg-white/15 px-2 py-0.5 text-on-ink">Em breve</span>}
          </p>
          <h3 className="font-display text-lg font-bold uppercase leading-tight sm:text-xl">{c.role}</h3>
        </div>
        <div className="flex shrink-0 items-center">
          <ArrowRight className="h-5 w-5 shrink-0 text-gold transition duration-300 group-hover:translate-x-1.5" aria-hidden />
        </div>
      </div>
    </Link>
  );
}
