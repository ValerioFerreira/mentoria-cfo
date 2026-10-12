import "server-only";
import { redirect } from "next/navigation";
import { getCurrentUser } from "./session";
import { hasBillingAccess } from "@/lib/billing/access";

/** Garante usuário logado em páginas e server actions; redireciona para /login caso contrário. */
export async function requireUser() {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  if (user.accessExpiresAt && user.accessExpiresAt < new Date() && !(await hasBillingAccess(user.id))) {
    redirect("/pagamentos?status=acesso-expirado");
  }
  return user;
}

export async function requireAdmin() {
  const user = await requireUser();
  if (user.role !== "ADMIN") redirect("/");
  return user;
}
