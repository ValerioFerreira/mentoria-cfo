import { RouteNavigationTrap } from "@/components/route-navigation-trap";
import { ArrowLeft, ArrowRight } from "lucide-react";
import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Badge } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { contestBySlug, type ContestInfo } from "@/lib/contests";

// uma linha por corporação (Soldado, 2º Tenente e Combo); o Combo recebe um selo de destaque
const ROWS: string[][] = [
  ["cbmpe-soldado", "cbmpe-oficial", "cbmpe-combo"],
  ["pmpe-soldado", "pmpe-oficial", "pmpe-combo"],
  ["pcpe-agente"],
];

export const metadata: Metadata = { title: "Escolha seu concurso" };

export default async function ContestsPage() {
  if (await getCurrentUser()) redirect("/");
  return (
    <div className="mx-auto flex max-w-5xl flex-col items-center space-y-8 pt-2 sm:pt-8 text-center">
      <RouteNavigationTrap targetUrl="/" />
      <div className="w-full text-left">
        <Link href="/" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Voltar para o início
        </Link>
      </div>
      <div className="mx-auto max-w-2xl space-y-4">
        <p className="eyebrow">MentorIA · Plano de estudos</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-[0.92] sm:text-7xl">
          Qual é a sua <span className="text-primary">missão?</span>
        </h1>
      </div>
      <div className="w-full max-w-5xl mx-auto space-y-6">
        {ROWS.map((row, r) => (
          <ul key={r} className="flex flex-wrap justify-center gap-6">
            {row.map((slug, i) => {
              const c = contestBySlug(slug)!;
              const combo = c.category === "Combo";
              return (
                <li
                  key={c.slug}
                  className="rise text-left w-full sm:w-[calc(50%-0.75rem)] lg:w-[calc(33.333%-1rem)] max-w-sm shrink-0"
                  style={{ ["--i" as string]: (r * 3 + i) * 0.6 }}
                >
                  {row.length > 1 && (
                    <p aria-hidden={!combo} className={`mb-2 inline-flex items-center rounded-full bg-gold px-3 py-1 text-xs font-bold uppercase tracking-wider text-ink ${combo ? "" : "invisible"}`}>
                      Estude os dois e economize
                    </p>
                  )}
                  <ContestCard c={c} />
                </li>
              );
            })}
          </ul>
        ))}
      </div>
    </div>
  );
}

function ContestCard({ c }: { c: ContestInfo }) {
  return (
    <Link
      href={`/lista-de-espera/${c.slug}`}
      className="group relative flex h-80 flex-col justify-end overflow-hidden rounded-2xl border border-white/10 bg-ink text-on-ink shadow-card outline-none transition duration-300 hover:-translate-y-1.5 hover:border-primary/60 hover:shadow-lift focus-visible:-translate-y-1.5 focus-visible:ring-2 focus-visible:ring-primary"
    >
      <Image
        src={c.image}
        alt=""
        fill
        priority
        sizes="(min-width: 768px) 33vw, 100vw"
        className="object-cover opacity-85 transition duration-500 ease-out group-hover:scale-110 group-hover:opacity-100"
        style={{ objectPosition: c.imagePosition }}
      />
      {/* fade: a imagem some em direção à base, onde fica o texto */}
      <div className="absolute inset-0 bg-gradient-to-t from-ink via-ink/60 to-transparent transition duration-500 group-hover:via-ink/45" aria-hidden />
      <div className="absolute inset-x-0 top-0 h-1 origin-left scale-x-0 bg-primary transition duration-500 group-hover:scale-x-100" aria-hidden />
      <div className="relative space-y-3 p-6">
        <div className="flex items-center gap-2">
          <Badge tone="gold">{c.org}</Badge>
          {c.category && <span className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">{c.category}</span>}
          {!c.available && <span className="rounded-full bg-white/15 px-2.5 py-0.5 text-xs font-semibold leading-5 text-on-ink">Em breve</span>}
        </div>
        <div>
          <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Cargo</p>
          <h2 className="font-display text-4xl font-bold uppercase leading-none">{c.role}</h2>
        </div>
        <p className="flex items-center gap-2 text-sm font-semibold text-gold">
          {c.available ? "Iniciar preparação" : "Ver detalhes"}
          <ArrowRight className="h-4 w-4 transition duration-300 group-hover:translate-x-1.5" aria-hidden />
        </p>
      </div>
    </Link>
  );
}
