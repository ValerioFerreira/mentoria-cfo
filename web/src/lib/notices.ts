import "server-only";
import { db } from "@/lib/db";

/** Avisos de novidade (pop-up). O id é gravado em `User.seenNotices` quando o aviso aparece. */
export const PDF_NOTICE = "pdf-proprio-2026-11";
export const RESCHEDULE_NOTICE = "reprogramar-2026-11";
export const KNOWN_NOTICES: readonly string[] = [PDF_NOTICE, RESCHEDULE_NOTICE];

async function noticeSeen(userId: string, id: string): Promise<boolean> {
  const u = await db.user.findUnique({ where: { id: userId }, select: { seenNotices: true } });
  return !u || u.seenNotices.includes(id);
}

/**
 * Aviso dos PDFs próprios do site: aparece uma única vez, no primeiro acesso depois da atualização, para quem tem plano
 * do CFOA ativo ou em análise (o material próprio da onda 1 é do edital do CFOA).
 */
export async function pdfNoticePending(userId: string): Promise<boolean> {
  if (await noticeSeen(userId, PDF_NOTICE)) return false;
  const plan = await db.plan.findFirst({
    where: { userId, contest: "CBMPE_CFOA", status: { in: ["ACTIVE", "PENDING_ANALYSIS"] } },
    select: { id: true },
  });
  return !!plan;
}

/** Aviso da função Reprogramar: uma única vez, na Missão de hoje de quem tem plano ativo (a página já confere o plano). */
export async function rescheduleNoticePending(userId: string): Promise<boolean> {
  return !(await noticeSeen(userId, RESCHEDULE_NOTICE));
}
