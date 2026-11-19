"use client";

import { BookOpen, FileText, X } from "lucide-react";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { useEffect, useState, useTransition } from "react";
import { Button } from "@/components/ui";
import { dismissNotice } from "@/lib/notices-actions";

/**
 * Pop-up de novidade: os PDFs próprios do MentorIA. Aparece uma vez (no primeiro acesso depois da atualização) para quem
 * tem plano do CFOA; ao fechar, o aviso é gravado como visto e não volta.
 */
export function PdfNewsModal({ noticeId, preview = false }: { noticeId: string; preview?: boolean }) {
  const [open, setOpen] = useState(true);
  const [, start] = useTransition();
  const router = useRouter();

  useEffect(() => {
    document.getElementById("pdf-news-cta")?.focus();
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") close();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function close(then?: () => void) {
    setOpen(false);
    if (!preview) start(() => void dismissNotice(noticeId));
    then?.();
  }

  if (!open) return null;
  return (
    <div className="fixed inset-0 z-[100] flex items-end justify-center bg-black/60 p-3 backdrop-blur-sm sm:items-center sm:p-6" onClick={() => close()}>
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby="pdf-news-title"
        onClick={(e) => e.stopPropagation()}
        className="rise relative w-full max-w-lg overflow-hidden rounded-3xl border border-white/10 bg-ink text-on-ink shadow-2xl"
      >
        <div className="tape h-2 w-full" aria-hidden />
        <button
          type="button"
          onClick={() => close()}
          aria-label="Fechar aviso"
          className="absolute right-3 top-5 z-10 cursor-pointer rounded-full p-1.5 text-on-ink-muted transition hover:bg-white/10 hover:text-on-ink"
        >
          <X className="h-5 w-5" aria-hidden />
        </button>

        <div className="relative px-6 pb-2 pt-6 sm:px-8">
          <Image
            src="/mascote/chama-bizu.png"
            alt=""
            width={600}
            height={600}
            priority
            className="pointer-events-none absolute right-2 top-12 h-24 w-24 drop-shadow-[0_10px_24px_rgba(233,169,12,0.35)] sm:-right-1 sm:top-0 sm:h-44 sm:w-44"
          />
          <span className="inline-flex items-center gap-1.5 rounded-full bg-gold px-3 py-1 font-display text-xs font-bold uppercase tracking-[0.14em] text-ink">
            <span className="h-1.5 w-1.5 rounded-full bg-ink" aria-hidden />
            Novidade
          </span>
          <h2 id="pdf-news-title" className="mt-4 max-w-[calc(100%-6.5rem)] font-display text-4xl font-bold uppercase leading-[0.95] tracking-wide sm:max-w-[19rem] sm:text-5xl">
            Chegaram os <span className="text-gold">PDFs</span> do Mentor<span className="brand-ia">IA</span>
          </h2>
          <p className="mt-3 text-sm leading-relaxed text-on-ink-muted sm:max-w-[19rem]">Material próprio, feito para o seu edital, direto nas suas atividades.</p>
        </div>

        <ul className="space-y-3 px-6 pb-2 pt-4 sm:px-8">
          <Item icon={<BookOpen className="h-5 w-5" aria-hidden />}>
            Abra em <strong className="text-on-ink">Teoria, Revisão e Fixação</strong>, na aba <strong className="text-on-ink">Material MentorIA</strong>.
          </Item>
          <Item icon={<FileText className="h-5 w-5" aria-hidden />}>
            Resumos, esquemas e <strong className="text-on-ink">questões comentadas</strong> em um só PDF.
          </Item>
        </ul>

        <div className="flex flex-col gap-2 px-6 pb-6 pt-5 sm:flex-row-reverse sm:px-8">
          <Button id="pdf-news-cta" size="lg" className="flex-1" onClick={() => close(() => router.push("/"))}>
            Ver minha missão de hoje
          </Button>
          <Button variant="onInk" size="lg" onClick={() => close()}>
            Depois
          </Button>
        </div>
      </div>
    </div>
  );
}

function Item({ icon, children }: { icon: React.ReactNode; children: React.ReactNode }) {
  return (
    <li className="flex items-start gap-3 text-sm leading-relaxed text-on-ink-muted">
      <span className="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-white/10 text-gold">{icon}</span>
      <span className="pt-1">{children}</span>
    </li>
  );
}
