import { ArrowLeft, NotebookPen, Pencil } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { CSSProperties } from "react";
import { Card, EmptyState, PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getSubjectSummaries } from "@/lib/data/summaries";
import { SUBJECT_NAME, subjectName } from "@/lib/ui-format";

export async function generateMetadata({ params }: PageProps<"/resumos/[disciplina]">): Promise<Metadata> {
  const { disciplina } = await params;
  return { title: SUBJECT_NAME[disciplina] ? `Resumos · ${SUBJECT_NAME[disciplina]}` : "Meus resumos" };
}

export default async function SubjectSummariesPage({ params }: PageProps<"/resumos/[disciplina]">) {
  const user = await requireUser();
  const { disciplina } = await params;
  if (!SUBJECT_NAME[disciplina]) notFound();
  const groups = await getSubjectSummaries(user.id, disciplina);
  const total = groups.reduce((n, g) => n + g.items.length, 0);

  return (
    <div className="mx-auto max-w-3xl space-y-7">
      <Link href="/resumos" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
        <ArrowLeft className="h-4 w-4" aria-hidden />
        Meus resumos
      </Link>
      <PageHeader
        eyebrow="Resumos"
        title={subjectName(disciplina)}
        description={total ? `${total} ${total === 1 ? "resumo" : "resumos"} em ${groups.length} ${groups.length === 1 ? "aula" : "aulas"}, na ordem dos assuntos.` : undefined}
      />
      {groups.length === 0 ? (
        <EmptyState icon={<NotebookPen className="h-6 w-6" aria-hidden />} title="Nenhum resumo nesta disciplina">
          Quando você escrever o “Meu resumo” de uma atividade de Teoria desta disciplina, ele aparece aqui.
        </EmptyState>
      ) : (
        groups.map((g, i) => (
          <section key={g.aula.id} aria-labelledby={`aula-${i}`} className="rise space-y-3" style={{ "--i": Math.min(i, 8) } as CSSProperties}>
            <h2 id={`aula-${i}`} className="font-display text-2xl font-bold uppercase leading-tight tracking-wide">
              {g.aula.shortTitle}
            </h2>
            <Card className="divide-y divide-border p-0">
              {g.items.map((it) => (
                <article key={it.segmentId} className="space-y-1.5 px-5 py-4">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    {it.topic ? <p className="eyebrow">{it.topic}</p> : <span />}
                    {it.activityId && (
                      <Link href={`/atividade/${it.activityId}#resumo`} className="inline-flex items-center gap-1 text-xs font-semibold text-muted transition hover:text-primary">
                        <Pencil className="h-3 w-3" aria-hidden />
                        Editar
                      </Link>
                    )}
                  </div>
                  <p className="whitespace-pre-wrap text-[15px] leading-relaxed">{it.text}</p>
                </article>
              ))}
            </Card>
          </section>
        ))
      )}
    </div>
  );
}
