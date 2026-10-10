"use server";

import { revalidatePath } from "next/cache";
import * as z from "zod";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";

async function ownedActivity(userId: string, id: string) {
  const a = await db.activity.findFirst({ where: { id, week: { plan: { userId } } }, select: { id: true, status: true } });
  if (!a) throw new Error("Atividade não encontrada.");
  return a;
}

export async function setActivityStatus(activityId: string, status: "PENDING" | "IN_PROGRESS" | "DONE" | "SKIPPED") {
  const user = await requireUser();
  await ownedActivity(user.id, activityId);
  await db.activity.update({ where: { id: activityId }, data: { status, completedAt: status === "DONE" ? new Date() : null } });
  revalidatePath("/", "layout");
}

/** Conclui a atividade exigindo o registro de tempo de forma transacional. */
export async function completeActivityWithTime(activityId: string, hours: number, minutes: number): Promise<{ error?: string }> {
  const user = await requireUser();
  const h = Hours.safeParse(hours);
  const m = Mins.safeParse(minutes);
  if (!h.success || !m.success) return { error: "Informe horas (0 a 16) e minutos (0 a 59)." };
  const total = h.data * 60 + m.data;
  if (total < 1) return { error: "O tempo de atividade é obrigatório (mínimo de 1 minuto)." };

  await ownedActivity(user.id, activityId);
  const seconds = total * 60;
  const now = new Date();

  await db.$transaction([
    db.timeLog.create({
      data: { userId: user.id, activityId, seconds, startedAt: now, endedAt: now, source: "MANUAL" },
    }),
    db.activity.update({
      where: { id: activityId },
      data: { status: "DONE", completedAt: now },
    }),
  ]);

  revalidatePath("/", "layout");
  return {};
}


const Hours = z.number().int().min(0).max(16);
const Mins = z.number().int().min(0).max(59);

/** Lança o tempo estudado numa atividade: total de horas + total de minutos. */
export async function logManualTime(activityId: string, hours: number, minutes: number): Promise<{ error?: string }> {
  const user = await requireUser();
  const h = Hours.safeParse(hours);
  const m = Mins.safeParse(minutes);
  if (!h.success || !m.success) return { error: "Informe horas (0 a 16) e minutos (0 a 59)." };
  const total = h.data * 60 + m.data;
  if (total < 1) return { error: "Informe pelo menos 1 minuto." };
  const a = await ownedActivity(user.id, activityId);
  const seconds = total * 60;
  // o tempo lançado vale para o momento do lançamento: recuar o início pela duração jogaria o estudo para o dia (ou a
  // semana) anterior quando a pessoa lança logo depois da meia-noite, e ele sumiria do "esta semana"
  const now = new Date();
  await db.timeLog.create({
    data: { userId: user.id, activityId, seconds, startedAt: now, endedAt: now, source: "MANUAL" },
  });
  if (a.status === "PENDING") await db.activity.update({ where: { id: activityId }, data: { status: "IN_PROGRESS" } });
  revalidatePath("/", "layout");
  return {};
}

export async function deleteTimeLog(id: string) {
  const user = await requireUser();
  await db.timeLog.deleteMany({ where: { id, userId: user.id } });
  revalidatePath("/", "layout");
}

export async function saveNote(segmentId: string, text: string) {
  const user = await requireUser();
  const clean = text.slice(0, 20_000);
  await db.note.upsert({
    where: { userId_segmentId: { userId: user.id, segmentId } },
    create: { userId: user.id, segmentId, text: clean },
    update: { text: clean },
  });
}

export async function answerBizuItem(itemId: string, activityId: string, answer: boolean) {
  const user = await requireUser();
  await ownedActivity(user.id, activityId);
  const item = await db.bizuItem.findUnique({ where: { id: itemId }, select: { isTrue: true } });
  if (!item) throw new Error("Item não encontrado.");
  await db.bizuAnswer.create({ data: { userId: user.id, bizuItemId: itemId, activityId, answer, isCorrect: item.isTrue === answer } });
}
