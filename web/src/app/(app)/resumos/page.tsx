import { ChevronRight, NotebookPen } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import type { CSSProperties } from "react";
import { BLOCK_COLOR, EmptyState, PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getSummaryCounts } from "@/lib/data/summaries";
import { getActivePlan } from "@/lib/data/study";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";

export const metadata: Metadata = { title: "Meus resumos" };

export default async function SummariesPage() {
  const user = await requireUser();
  const [plan, counts, subjects] = await Promise.all([
    getActivePlan(user.id),
    getSummaryCounts(user.id),
    db.subject.findMany({ orderBy: { sortOrder: "asc" }, select: { id: true, block: true } }),
  ]);
  const inPlan = new Set(plan?.subjects.map((s) => s.subjectId) ?? []);
  // as disciplinas do plano e as que já têm resumo (caso o plano tenha sido refeito)
  const cards = subjects.filter((s) => inPlan.has(s.id) || counts.has(s.id));
  const total = [...counts.values()].reduce((n, c) => n + c, 0);

  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Seu material de revisão"
        title="Meus resumos"
        info="Os resumos que você escreve no campo “Meu resumo” das atividades de Teoria ficam reunidos aqui, por disciplina, separados por aula e na ordem dos assuntos."
        description={total ? `${total} ${total === 1 ? "resumo escrito" : "resumos escritos"} até agora.` : undefined}
      />
      {cards.length === 0 ? (
        <EmptyState icon={<NotebookPen className="h-6 w-6" aria-hidden />} title="Nenhum resumo ainda">
          Monte o seu plano e escreva o resumo de cada assunto no campo “Meu resumo” das atividades de Teoria: eles aparecem aqui, organizados por disciplina.
        </EmptyState>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {cards.map((s, i) => {
            const n = counts.get(s.id) ?? 0;
            return (
              <li key={s.id} className="rise" style={{ "--i": Math.min(i, 12) } as CSSProperties}>
                <Link
                  href={`/resumos/${s.id}`}
                  className="card-hover group relative flex h-full items-center gap-4 overflow-hidden rounded-2xl border border-border bg-surface p-4 pl-6 shadow-card"
                >
                  <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: BLOCK_COLOR[s.block as "I" | "II" | "III"] }} aria-hidden />
                  <span className="min-w-0 flex-1">
                    <span className="block font-display text-2xl font-bold uppercase leading-none tracking-wide">{subjectName(s.id)}</span>
                    <span className={`mt-1.5 block text-sm ${n ? "font-semibold text-text" : "text-muted"}`}>
                      {n ? `${n} ${n === 1 ? "resumo" : "resumos"}` : "Nenhum resumo ainda"}
                    </span>
                  </span>
                  <ChevronRight className="h-5 w-5 shrink-0 text-muted transition group-hover:translate-x-0.5 group-hover:text-text" aria-hidden />
                </Link>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
