import "server-only";
import { db } from "@/lib/db";
import { hasBillingAccess } from "@/lib/billing/access";

const PLATFORM_RELEASED_KEY = "PLATFORM_RELEASED";

/**
 * Verifica se a liberação geral da plataforma foi acionada.
 */
export async function isPlatformReleased(): Promise<boolean> {
  try {
    const setting = await db.systemSetting.findUnique({
      where: { key: PLATFORM_RELEASED_KEY },
    });
    if (setting) {
      return setting.value === "true";
    }
  } catch (err) {
    console.error("[isPlatformReleased] Erro ao consultar setting:", err);
  }
  return false;
}

/**
 * Define o status da liberação geral da plataforma.
 */
export async function setPlatformReleased(released: boolean): Promise<void> {
  await db.systemSetting.upsert({
    where: { key: PLATFORM_RELEASED_KEY },
    create: {
      key: PLATFORM_RELEASED_KEY,
      value: released ? "true" : "false",
    },
    update: {
      value: released ? "true" : "false",
    },
  });
}

/**
 * Determina se o usuário atual tem acesso às funcionalidades essenciais
 * (Planejamento, Questões e Simulados).
 * - ADMIN: sempre
 * - Parceiro ativo: sempre (acesso acadêmico completo + painel de parceria)
 * - Liberação geral da plataforma: todos os alunos
 * - Plano ACTIVE (liberação individual pelo admin): esse aluno
 * - Direito de pagamento válido (billing legado): esse aluno
 */
export async function canUserAccessCoreFeatures(userRole: string, userId?: string): Promise<boolean> {
  if (userRole === "ADMIN") {
    return true;
  }
  if (await isPlatformReleased()) return true;
  if (!userId) return false;

  const partner = await db.partner.findUnique({
    where: { userId },
    select: { active: true },
  });
  if (partner?.active) return true;

  const activePlan = await db.plan.findFirst({
    where: { userId, status: "ACTIVE" },
    select: { id: true },
  });
  if (activePlan) return true;

  return hasBillingAccess(userId);
}
