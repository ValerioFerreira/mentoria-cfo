import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { CadastrosView, type WaitlistRow } from "./cadastros-view";

export const metadata: Metadata = { title: "Gestão de Cadastros" };

export default async function AdminCadastrosPage() {
  await requireAdmin();

  const entries = await db.waitlistEntry.findMany({
    orderBy: { createdAt: "desc" },
  });

  // Busca os usuários correspondentes por e-mail para checar validade e senha
  const emails = entries.map((e) => e.email);
  const users = await db.user.findMany({
    where: { email: { in: emails } },
    select: { id: true, email: true, mustChangePassword: true, accessExpiresAt: true },
  });

  const userMap = new Map(users.map((u) => [u.email, u]));

  const formatted: WaitlistRow[] = entries.map((e) => {
    const u = userMap.get(e.email);
    return {
      id: e.id,
      name: e.name,
      email: e.email,
      username: e.username,
      contest: e.contest,
      plan: e.plan,
      status: e.status || "PENDING",
      createdAt: e.createdAt.toISOString(),
      paidAt: e.paidAt ? e.paidAt.toISOString() : null,
      approvedAt: e.approvedAt ? e.approvedAt.toISOString() : null,
      rejectedAt: e.rejectedAt ? e.rejectedAt.toISOString() : null,
      accessDuration: e.accessDuration,
      rejectionReason: e.rejectionReason,
      user: u
        ? {
            id: u.id,
            mustChangePassword: u.mustChangePassword,
            accessExpiresAt: u.accessExpiresAt ? u.accessExpiresAt.toISOString() : null,
          }
        : null,
    };
  });

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Administração"
        title="Gestão de Cadastros"
        description="Aprove ou recuse os cadastros da lista de espera. Ao aprovar, defina o período de validade (30 dias ou indeterminado) e envie a senha temporária por e-mail."
      />

      <CadastrosView entries={formatted} />
    </div>
  );
}
