import "server-only";
import { db } from "@/lib/db";
import { hashPassword, verifyPassword } from "./password";

export const DEFAULT_ADMIN_EMAIL = "valerioeducfin@gmail.com";
export const DEFAULT_ADMIN_PASSWORD = "P3rn@mbuco";

/**
 * Garante que o administrador padrão (valerioeducfin@gmail.com) exista no banco
 * com role ADMIN e a senha correta configurada. Idempotente.
 */
export async function ensureDefaultAdmin() {
  const email = DEFAULT_ADMIN_EMAIL.toLowerCase();
  const existing = await db.user.findUnique({ where: { email } });

  if (!existing) {
    const passwordHash = await hashPassword(DEFAULT_ADMIN_PASSWORD);
    await db.user.create({
      data: {
        email,
        name: "Valério Ferreira (Admin)",
        username: "valerio",
        role: "ADMIN",
        passwordHash,
        mustChangePassword: false,
      },
    });
    console.log(`[Bootstrap] Administrador ${email} criado com sucesso.`);
    return;
  }

  // Verifica se precisa de atualização de role ou senha
  const passwordMatch = await verifyPassword(DEFAULT_ADMIN_PASSWORD, existing.passwordHash);
  if (existing.role !== "ADMIN" || !passwordMatch) {
    const passwordHash = passwordMatch ? existing.passwordHash : await hashPassword(DEFAULT_ADMIN_PASSWORD);
    await db.user.update({
      where: { id: existing.id },
      data: {
        role: "ADMIN",
        passwordHash,
      },
    });
    console.log(`[Bootstrap] Administrador ${email} atualizado para role ADMIN / senha.`);
  }
}
