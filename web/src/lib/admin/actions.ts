"use server";

import { revalidatePath } from "next/cache";
import * as z from "zod";
import { requireAdmin, requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";

const Status = z.enum(["DRAFT", "APPROVED", "FLAGGED", "RETIRED"]);

export async function setQuestionStatus(id: string, status: z.infer<typeof Status>) {
  await requireAdmin();
  await db.question.update({ where: { id }, data: { status: Status.parse(status) } });
  revalidatePath("/admin/revisao");
}

/** Aprova em lote todos os rascunhos de um lote de geração (opcionalmente restrito a uma aula). */
export async function approveBatch(batch: string, aulaId?: string) {
  await requireAdmin();
  const r = await db.question.updateMany({ where: { batch, status: "DRAFT", ...(aulaId ? { aulaId } : {}) }, data: { status: "APPROVED" } });
  revalidatePath("/admin/revisao");
  return { approved: r.count };
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
