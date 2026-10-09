import "server-only";
import { redirect } from "next/navigation";
import { getCurrentUser } from "./session";

/** Garante usuário logado em páginas e server actions; redireciona para /login caso contrário. */
export async function requireUser() {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  if (user.accessExpiresAt && user.accessExpiresAt < new Date()) {
    redirect("/login?erro=acesso-expirado");
  }
  return user;
}

export async function requireAdmin() {
  const user = await requireUser();
  if (user.role !== "ADMIN") redirect("/");
  return user;
}
