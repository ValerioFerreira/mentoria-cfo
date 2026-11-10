"use server";

import { revalidatePath } from "next/cache";
import { requireUser } from "@/lib/auth/dal";
import { cpfDigits, isValidCpf } from "@/lib/cpf";
import { db } from "@/lib/db";

export type CpfState = { ok?: boolean; message?: string };

/**
 * Grava o CPF do aluno (carimbado no rodapé dos PDFs do material). Depois de gravado, só o administrador altera: o CPF
 * identifica o titular da licença e não pode ser trocado por quem baixa o material.
 */
export async function saveCpf(_: CpfState, formData: FormData): Promise<CpfState> {
  const user = await requireUser();
  const raw = String(formData.get("cpf") ?? "");
  if (!isValidCpf(raw)) return { message: "CPF inválido. Confira os 11 números." };
  const digits = cpfDigits(raw);
  const current = await db.user.findUnique({ where: { id: user.id }, select: { cpf: true } });
  if (current?.cpf) return { message: "O CPF já foi informado. Para corrigi-lo, fale com o suporte." };
  await db.user.update({ where: { id: user.id }, data: { cpf: digits } });
  revalidatePath("/perfil");
  return { ok: true, message: "CPF registrado. Seus PDFs já podem ser abertos." };
}
