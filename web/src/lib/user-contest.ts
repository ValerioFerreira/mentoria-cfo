import "server-only";
import { cookies } from "next/headers";
import { db } from "@/lib/db";
import type { Contest } from "@/generated/prisma/client";
import { CONTEST_SUBTITLES } from "./contests";

export const CONTEST_COOKIE = "mentoria_contest";

export async function getUserContest(userEmail?: string): Promise<Contest> {
  // 1. Cookie preferencial (permite troca instantânea no perfil ou na sessão)
  try {
    const jar = await cookies();
    const cookieVal = jar.get(CONTEST_COOKIE)?.value as Contest | undefined;
    if (cookieVal && cookieVal in CONTEST_SUBTITLES) {
      return cookieVal;
    }
  } catch {
    // cookies() pode não estar disponível fora de contexto de requisição
  }

  // 2. Concurso selecionado no cadastro/lista de espera
  if (userEmail) {
    try {
      const entry = await db.waitlistEntry.findFirst({
        where: { email: userEmail.toLowerCase() },
        select: { contest: true },
        orderBy: { createdAt: "desc" },
      });
      if (entry?.contest && entry.contest in CONTEST_SUBTITLES) {
        return entry.contest;
      }
    } catch (err) {
      console.error("[getUserContest] Erro ao consultar concurso do usuário:", err);
    }
  }

  // 3. Padrão
  return "CBMPE_OFICIAL";
}

export async function getUserContestSubtitle(userEmail?: string): Promise<string> {
  const contest = await getUserContest(userEmail);
  return CONTEST_SUBTITLES[contest] ?? "OFICIAL - CBMPE";
}
