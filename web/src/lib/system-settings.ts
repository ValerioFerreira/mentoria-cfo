import "server-only";
import { db } from "@/lib/db";

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
 * - Usuários ADMIN têm acesso SEMPRE (mesmo durante o período de revisão).
 * - Usuários comuns só têm acesso se a plataforma estiver com liberação geral ativa.
 */
export async function canUserAccessCoreFeatures(userRole: string): Promise<boolean> {
  if (userRole === "ADMIN") {
    return true;
  }
  return await isPlatformReleased();
}
