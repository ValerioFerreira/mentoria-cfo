"use server";

import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { chaptersOfVolume, volumeInfo } from "@/lib/material";

export type MaterialReportState = { ok?: boolean; message?: string };

const MAX_PER_DAY = 10;

/** O aluno aponta um erro num PDF do material próprio: volume, página e explicação. O volume e a página são conferidos no servidor. */
export async function reportMaterialError(volumeId: string, _: MaterialReportState, formData: FormData): Promise<MaterialReportState> {
  const user = await requireUser();
  const info = typeof volumeId === "string" ? volumeInfo(volumeId) : null;
  if (!info) return { message: "Material não encontrado." };
  const page = Number(String(formData.get("page") ?? "").trim());
  if (!Number.isInteger(page) || page < 1 || page > info.paginas) return { message: `Informe uma página entre 1 e ${info.paginas}.` };
  const message = String(formData.get("message") ?? "").replace(/\s+/g, " ").trim();
  if (message.length < 10) return { message: "Explique o erro com um pouco mais de detalhe (pelo menos 10 caracteres)." };
  if (message.length > 1000) return { message: "A explicação passou de 1.000 caracteres. Resuma o problema." };

  const since = new Date(Date.now() - 24 * 60 * 60 * 1000);
  if ((await db.materialErrorReport.count({ where: { userId: user.id, createdAt: { gte: since } } })) >= MAX_PER_DAY) {
    return { message: "Você já enviou vários relatos hoje. Tente de novo amanhã." };
  }
  // capítulo cuja faixa de páginas contém a página relatada (ajuda a achar o texto a corrigir)
  const chapter = chaptersOfVolume(volumeId).find((c) => page >= c.start && page <= (c.questions?.ate ?? c.end));
  await db.materialErrorReport.create({ data: { userId: user.id, volumeId, page, message, chapter: chapter?.trecho ?? null } });
  return { ok: true, message: "Obrigado! O erro foi enviado para a equipe revisar." };
}
