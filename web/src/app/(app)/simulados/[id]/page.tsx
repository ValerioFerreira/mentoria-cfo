import type { Metadata } from "next";
import { notFound, redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { SimuladoRunner, type SimuladoQuestionItem } from "@/components/simulado-runner";

export const metadata: Metadata = {
  title: "Simulado Oficial em Andamento — Missão CBMPE 2026",
};

export default async function SimuladoSessionPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role))) {
    redirect("/simulados");
  }

  const { id } = await params;

  const session = await db.quizSession.findFirst({
    where: {
      id,
      userId: user.id,
      kind: "SIMULADO",
    },
    include: {
      answers: {
        orderBy: { position: "asc" },
        include: {
          question: {
            include: {
              options: {
                orderBy: { label: "asc" },
                select: {
                  label: true,
                  text: true,
                  // IMPORTANTE: NÃO expor isCorrect para o cliente durante a prova!
                },
              },
              subject: {
                select: {
                  name: true,
                  block: true,
                },
              },
            },
          },
        },
      },
    },
  });

  if (!session) notFound();

  // Se já foi finalizado, vai para a página de resultado
  if (session.finishedAt) {
    redirect(`/simulados/resultado/${session.id}`);
  }

  const questions: SimuladoQuestionItem[] = session.answers.map((a) => ({
    position: a.position,
    subjectName: a.question.subject?.name ?? "Disciplina",
    block: (a.question.subject?.block as "I" | "II" | "III") ?? "I",
    topic: a.question.topic,
    statement: a.question.statement,
    support: a.question.support,
    options: a.question.options.map((o) => ({
      label: o.label,
      text: o.text,
    })),
    chosenLabel: a.chosenLabel,
    flagged: a.flagged,
  }));

  return (
    <SimuladoRunner
      sessionId={session.id}
      title={session.title ?? "Simulado Oficial CBMPE 2026"}
      startedAtMs={session.startedAt.getTime()}
      limitSeconds={session.limitSeconds}
      serverNowMs={Date.now()}
      questions={questions}
    />
  );
}
