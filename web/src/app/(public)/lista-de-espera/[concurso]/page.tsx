import { ArrowLeft } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { Alert } from "@/components/ui";
import { getCurrentUser } from "@/lib/auth/session";
import { contestBySlug, contestTitle } from "@/lib/contests";
import { WaitlistForm } from "./waitlist-form";

export async function generateMetadata({ params }: PageProps<"/lista-de-espera/[concurso]">): Promise<Metadata> {
  const c = contestBySlug((await params).concurso);
  return { title: c ? `Lista de espera · ${c.org} ${c.role}` : "Lista de espera" };
}

export default async function WaitlistPage({ params }: PageProps<"/lista-de-espera/[concurso]">) {
  if (await getCurrentUser()) redirect("/");
  const { concurso } = await params;
  const c = contestBySlug(concurso);
  if (!c) notFound();
  return (
    <div className="mx-auto max-w-xl space-y-6 pt-2 sm:pt-8">
      <Link href="/concursos" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
        <ArrowLeft className="h-4 w-4" aria-hidden />
        Trocar de concurso
      </Link>
      <div>
        <p className="eyebrow">{contestTitle(c)}</p>
        <h1 className="font-display text-5xl font-bold uppercase leading-none">Lista de espera</h1>
      </div>
      {!c.available && (
        <Alert tone="info">
          O plano de estudos do cargo de <strong>{c.role}</strong> ({c.org}) está <strong>em desenvolvimento</strong>. Você já pode entrar na lista de espera: basta efetuar o pagamento por Pix e avisaremos quando o acesso for liberado.
        </Alert>
      )}
      <WaitlistForm slug={c.slug} />
    </div>
  );
}
