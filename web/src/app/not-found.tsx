import Link from "next/link";
import { BrandMark } from "@/components/brand";

export default function NotFound() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-md flex-col items-center justify-center gap-5 px-6 text-center">
      <BrandMark className="h-14 w-14" />
      <p className="eyebrow">Erro 404</p>
      <h1 className="font-display text-6xl font-bold uppercase leading-[0.9]">Página não encontrada</h1>
      <p className="text-sm text-muted">O endereço não existe ou a atividade pertence a outra conta. Volte ao início para continuar de onde parou.</p>
      <Link href="/" className="inline-flex items-center justify-center rounded-xl border border-transparent bg-primary px-5 py-3 text-sm font-semibold text-on-primary shadow-[inset_0_1px_0_rgb(255_255_255/.22),0_8px_18px_-8px_var(--primary)] transition hover:bg-primary-hover">
        Voltar ao início
      </Link>
    </main>
  );
}
