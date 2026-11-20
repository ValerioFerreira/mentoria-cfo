"use client";

import { CalendarClock, Eye, TriangleAlert } from "lucide-react";
import { useRouter } from "next/navigation";
import { NoticeItem, NoticeModal } from "@/components/notice-modal";
import { Button } from "@/components/ui";

/**
 * Pop-up de novidade: a função Reprogramar. Aparece uma única vez, na Missão de hoje, para quem tem plano ativo.
 * O título foi definido pelo dono do produto: não reescrever sem aprovação.
 */
export function RescheduleNewsModal({ noticeId, overdueCount, preview = false }: { noticeId: string; overdueCount: number; preview?: boolean }) {
  const router = useRouter();
  const strong = "text-on-ink";
  return (
    <NoticeModal
      noticeId={noticeId}
      preview={preview}
      primaryId="reschedule-news-cta"
      titleClassName="text-3xl sm:text-4xl"
      title={
        <>
          Os estudos atrasaram? Calma, chegou a função de <span className="text-gold">Reprogramar!</span>
        </>
      }
      subtitle="Reorganize as atividades atrasadas sem bagunçar o seu plano."
      actions={(close) =>
        overdueCount > 0 ? (
          <>
            <Button id="reschedule-news-cta" size="lg" className="flex-1" onClick={() => close(() => router.push("/reprogramar"))}>
              Reprogramar agora
            </Button>
            <Button variant="onInk" size="lg" onClick={() => close()}>
              Entendi
            </Button>
          </>
        ) : (
          <Button id="reschedule-news-cta" size="lg" className="flex-1" onClick={() => close()}>
            Entendi
          </Button>
        )
      }
    >
      <NoticeItem icon={<TriangleAlert className="h-5 w-5" aria-hidden />}>
        Quando houver atividades atrasadas, o botão <strong className={strong}>Reprogramar</strong> aparece no aviso amarelo da Missão de hoje.
      </NoticeItem>
      <NoticeItem icon={<CalendarClock className="h-5 w-5" aria-hidden />}>
        Escolha as atividades e como encaixá-las: <strong className={strong}>espalhar pelos próximos dias</strong>, <strong className={strong}>só nas folgas</strong>,{" "}
        <strong className={strong}>levar para um dia</strong>, <strong className={strong}>recalcular o restante do plano</strong> ou <strong className={strong}>dispensar</strong>.
      </NoticeItem>
      <NoticeItem icon={<Eye className="h-5 w-5" aria-hidden />}>
        Antes de confirmar, você vê <strong className={strong}>para onde cada uma vai</strong> e a carga de cada dia. As atividades seguintes andam junto: a ordem
        Teoria → Revisão → Fixação → Questões é mantida e nada passa da véspera da prova.
      </NoticeItem>
    </NoticeModal>
  );
}
