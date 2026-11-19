"use server";

import { revalidatePath } from "next/cache";
import { requireUser } from "@/lib/auth/dal";
import { cpfDigits, isValidCpf } from "@/lib/cpf";
import { db } from "@/lib/db";
import { normalizeFullName } from "@/lib/person-name";

export type CpfState = { ok?: boolean; message?: string };

/**
 * Grava o CPF e confirma o nome completo do titular (os dois vão no rodapé dos PDFs do material). O nome passa a ficar em
 * caixa alta na conta. Depois de gravados, só o administrador altera: o CPF identifica o titular da licença e não pode ser
 * trocado por quem baixa o material.
 *
 * A validação confere os 11 dígitos e os dígitos verificadores (rejeita sequências como 111.111.111-11): isso afasta número
 * inventado ou digitado errado, mas não consulta a Receita Federal para saber a quem o CPF pertence.
 */
export async function saveCpf(_: CpfState, formData: FormData): Promise<CpfState> {
  const user = await requireUser();
  const raw = String(formData.get("cpf") ?? "");
  if (!isValidCpf(raw)) return { message: "CPF inválido. Confira os 11 números." };
  const fullName = normalizeFullName(String(formData.get("name") ?? ""));
  if (!fullName) return { message: "Informe o seu nome completo, com nome e sobrenome, só com letras." };
  if (formData.get("confirm") !== "on") return { message: "Marque a confirmação: o nome e o CPF são seus e vão no rodapé dos PDFs." };
  const digits = cpfDigits(raw);
  const current = await db.user.findUnique({ where: { id: user.id }, select: { cpf: true } });
  if (current?.cpf) return { message: "O CPF já foi informado. Para corrigi-lo, fale com o suporte." };
  await db.user.update({ where: { id: user.id }, data: { cpf: digits, name: fullName } });
  revalidatePath("/perfil");
  return { ok: true, message: "CPF e nome registrados. Seus PDFs já podem ser abertos." };
}
