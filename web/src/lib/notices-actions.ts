"use server";

import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { KNOWN_NOTICES } from "@/lib/notices";

/** Marca um aviso de novidade como visto: ele não volta a aparecer para este aluno. */
export async function dismissNotice(id: string): Promise<void> {
  const user = await requireUser();
  if (!KNOWN_NOTICES.includes(id)) return;
  await db.user.updateMany({ where: { id: user.id, NOT: { seenNotices: { has: id } } }, data: { seenNotices: { push: id } } });
}
