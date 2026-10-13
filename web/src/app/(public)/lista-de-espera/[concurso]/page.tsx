import { RouteNavigationTrap } from "@/components/route-navigation-trap";
import { ArrowLeft } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { Alert } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { contestOffer } from "@/lib/commerce/contracts";
import { priceCardText } from "@/lib/commerce/pricing";
import { contestBySlug, contestTitle } from "@/lib/contests";
import { WaitlistForm } from "./waitlist-form";

export async function generateMetadata({ params }: PageProps<"/lista-de-espera/[concurso]">): Promise<Metadata> {
  const c = contestBySlug((await params).concurso);
  return { title: c ? `Plano de estudos · ${c.org} ${c.role}` : "Plano de estudos" };
}

export default async function WaitlistPage({ params }: PageProps<"/lista-de-espera/[concurso]">) {
  if (await getCurrentUser()) redirect("/");
  const { concurso } = await params;
  const c = contestBySlug(concurso);
  if (!c) notFound();
  // preço calculado no servidor a partir da categoria persistida do concurso
  const offer = await contestOffer(c.key);
  const card = offer.available ? { badge: priceCardText(offer.quote).badge, originalCents: offer.quote.originalCents, finalCents: offer.quote.finalCents } : null;
  return (
    <div className="mx-auto max-w-2xl space-y-6 pt-2 sm:pt-8">
      <RouteNavigationTrap targetUrl="/concursos" />
      <Link href="/concursos" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
        <ArrowLeft className="h-4 w-4" aria-hidden />
        Trocar de concurso
      </Link>
      <div>
        <p className="eyebrow">{contestTitle(c)}</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-none">Inscrição & Plano</h1>
      </div>
      {card ? (
        <WaitlistForm slug={c.slug} card={card} examDateKnown={Boolean(offer.examDate)} />
      ) : (
        <Alert tone="info">As inscrições para este concurso abrem em breve: os valores ainda estão em revisão pela administração.</Alert>
      )}
    </div>
  );
}
