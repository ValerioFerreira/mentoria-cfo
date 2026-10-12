"use server";

import { revalidatePath } from "next/cache";
import * as z from "zod";
import { requireAdmin, requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";

const Status = z.enum(["DRAFT", "APPROVED", "FLAGGED", "RETIRED"]);

// Decisão humana: classifiedBy = MANUAL faz o importador (pipeline/questoes) preservar trecho e status.
export async function setQuestionStatus(id: string, status: z.infer<typeof Status>) {
  await requireAdmin();
  await db.question.update({ where: { id }, data: { status: Status.parse(status), classifiedBy: "MANUAL" } });
  revalidatePath("/admin/revisao");
}

/** Aprova em lote todos os rascunhos de um lote de geração (opcionalmente restrito a uma aula). */
export async function approveBatch(batch: string, aulaId?: string) {
  await requireAdmin();
  const r = await db.question.updateMany({
    where: { batch, status: "DRAFT", ...(aulaId ? { aulaId } : {}) },
    data: { status: "APPROVED", classifiedBy: "MANUAL" },
  });
  revalidatePath("/admin/revisao");
  return { approved: r.count };
}

/** Aprova os rascunhos de um assunto do TecConcursos (a sugestão de trecho do importador foi conferida). */
export async function approveTecAssunto(tecMateria: string, tecAssunto: string) {
  await requireAdmin();
  const r = await db.question.updateMany({
    where: { status: "DRAFT", tecMateria, tecAssunto },
    data: { status: "APPROVED", classifiedBy: "MANUAL" },
  });
  revalidatePath("/admin/revisao");
  return { approved: r.count };
}

/** Move a questão para outro trecho (atividade) e a aprova. O item do edital acompanha a aula do trecho. */
export async function moveQuestion(id: string, segmentId: string) {
  await requireAdmin();
  const seg = await db.segment.findUnique({ where: { id: segmentId }, select: { id: true, aulaId: true, aula: { select: { subjectId: true } } } });
  if (!seg) return { error: "Trecho inexistente." };
  const q = await db.question.findUnique({ where: { id }, select: { editalItemId: true } });
  const items = await db.editalItem.findMany({ where: { subjectId: seg.aula.subjectId }, select: { id: true, aulaIds: true } });
  const ofAula = items.filter((e) => Array.isArray(e.aulaIds) && (e.aulaIds as string[]).includes(seg.aulaId));
  const editalItemId = ofAula.find((e) => e.id === q?.editalItemId)?.id ?? ofAula[0]?.id ?? null;
  await db.question.update({
    where: { id },
    data: {
      subjectId: seg.aula.subjectId,
      aulaId: seg.aulaId,
      segmentId: seg.id,
      editalItemId,
      status: "APPROVED",
      classifiedBy: "MANUAL",
    },
  });
  revalidatePath("/admin/revisao");
  return { ok: true };
}

export async function resolveReport(id: string, status: "RESOLVED" | "DISMISSED", retire: boolean) {
  await requireAdmin();
  const rep = await db.questionReport.update({ where: { id }, data: { status } });
  if (retire) await db.question.update({ where: { id: rep.questionId }, data: { status: "FLAGGED" } });
  revalidatePath("/admin/revisao");
}

const Report = z.object({ questionId: z.string().min(1), reason: z.string().trim().min(5, "Descreva o problema em pelo menos 5 caracteres.").max(1000) });

/** Aluno reporta erro/ambiguidade em uma questão (só pode reportar questões que respondeu). */
export async function reportQuestion(questionId: string, reason: string): Promise<{ error?: string; ok?: true }> {
  const user = await requireUser();
  const parsed = Report.safeParse({ questionId, reason });
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Dados inválidos." };
  const answered = await db.quizAnswer.findFirst({ where: { questionId, session: { userId: user.id } }, select: { id: true } });
  if (!answered) return { error: "Você só pode reportar questões que apareceram nos seus cadernos." };
  const dup = await db.questionReport.findFirst({ where: { questionId, userId: user.id, status: "OPEN" } });
  if (!dup) await db.questionReport.create({ data: { userId: user.id, questionId, reason: parsed.data.reason } });
  return { ok: true };
}
