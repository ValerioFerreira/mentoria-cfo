import { ArrowRight } from "lucide-react";
import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Badge } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { CONTESTS, type ContestInfo } from "@/lib/contests";

export const metadata: Metadata = { title: "Escolha seu concurso" };

export default async function ContestsPage() {
  if (await getCurrentUser()) redirect("/");
  return (
    <div className="space-y-10 pt-4 sm:pt-10">
      <div className="max-w-2xl space-y-4">
        <p className="eyebrow">MentorIA · Plano de estudos</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-[0.92] sm:text-7xl">
          Qual é a sua <span className="text-primary">missão?</span>
        </h1>
        <p className="text-muted">Escolha o concurso. O MentorIA monta o plano de trás para frente a partir da data da prova, com a missão de cada dia, o que estudar e onde.</p>
      </div>
      <ul className="grid gap-5 md:grid-cols-3">
        {CONTESTS.map((c, i) => (
          <li key={c.slug} className="rise" style={{ ["--i" as string]: i * 0.6 }}>
            <ContestCard c={c} />
          </li>
        ))}
      </ul>
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
          {!c.available && <span className="rounded-full bg-white/15 px-2.5 py-0.5 text-xs font-semibold leading-5 text-on-ink">Em desenvolvimento</span>}
        </div>
        <div>
          <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Cargo</p>
          <h2 className="font-display text-4xl font-bold uppercase leading-none">{c.role}</h2>
        </div>
        <p className="flex items-center gap-2 text-sm font-semibold text-gold">
          Entrar na lista de espera
          <ArrowRight className="h-4 w-4 transition duration-300 group-hover:translate-x-1.5" aria-hidden />
        </p>
      </div>
    </Link>
  );
}
