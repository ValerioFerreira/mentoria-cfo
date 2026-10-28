/**
 * Usuário de teste LOCAL: reinicia a conta e "reconhece" pagamentos sem cobrança real, para testar todos os planos
 * sem criar vários usuários. Só vale fora de produção e com o banco em localhost (nunca no banco remoto).
 */
export const TEST_USER_EMAIL = "teste@teste.com";
export const TEST_USER_PASSWORD = "teste";

function localDatabase(url = process.env.DATABASE_URL ?? ""): boolean {
  try {
    const host = new URL(url).hostname;
    return host === "localhost" || host === "127.0.0.1" || host === "[::1]" || host === "::1";
  } catch {
    return false;
  }
}

export function testToolsEnabled(): boolean {
  return process.env.NODE_ENV !== "production" && localDatabase();
}

export function isTestUser(email: string | null | undefined): boolean {
  return !!email && email.trim().toLowerCase() === TEST_USER_EMAIL && testToolsEnabled();
}

export { localDatabase };
