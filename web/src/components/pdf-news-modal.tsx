"use client";

import { BookOpen, FileText } from "lucide-react";
import { useRouter } from "next/navigation";
import { NoticeItem, NoticeModal } from "@/components/notice-modal";
import { Button } from "@/components/ui";

/**
 * Pop-up de novidade: os PDFs próprios do MentorIA. Aparece uma vez (no primeiro acesso depois da atualização) para quem
 * tem plano do CFOA. Gravado como visto ao aparecer (ver `NoticeModal`).
 */
export function PdfNewsModal({ noticeId, preview = false }: { noticeId: string; preview?: boolean }) {
  const router = useRouter();
  return (
    <NoticeModal
      noticeId={noticeId}
      preview={preview}
      primaryId="pdf-news-cta"
      title={
        <>
          Chegaram os <span className="text-gold">PDFs</span> do Mentor<span className="brand-ia">IA</span>
        </>
      }
      subtitle="Material próprio, feito para o seu edital, direto nas suas atividades."
      actions={(close) => (
        <>
          <Button id="pdf-news-cta" size="lg" className="flex-1" onClick={() => close(() => router.push("/"))}>
            Ver minha missão de hoje
          </Button>
          <Button variant="onInk" size="lg" onClick={() => close()}>
            Depois
          </Button>
        </>
      )}
    >
      <NoticeItem icon={<BookOpen className="h-5 w-5" aria-hidden />}>
        Abra em <strong className="text-on-ink">Teoria, Revisão e Fixação</strong>, na aba <strong className="text-on-ink">Material MentorIA</strong>.
      </NoticeItem>
      <NoticeItem icon={<FileText className="h-5 w-5" aria-hidden />}>
        Resumos, esquemas e <strong className="text-on-ink">questões comentadas</strong> em um só PDF.
      </NoticeItem>
    </NoticeModal>
  );
}
