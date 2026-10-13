import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { isPlatformReleased } from "@/lib/system-settings";
import { LiberacaoView } from "./liberacao-view";

export const metadata: Metadata = { title: "Liberação Geral do Sistema e Notificação" };

export default async function AdminLiberacaoPage() {
  await requireAdmin();

  const [totalUsers, pendingPlansCount, activePlansCount, platformReleased, usersList] = await Promise.all([
    db.user.count(),
    db.plan.count({ where: { status: "PENDING_ANALYSIS" } }),
    db.plan.count({ where: { status: "ACTIVE" } }),
    isPlatformReleased(),
    db.user.findMany({
      select: {
        id: true,
        name: true,
        email: true,
        createdAt: true,
        role: true,
        plans: {
          select: { id: true, status: true, version: true },
          orderBy: { version: "desc" },
          take: 1,
        },
      },
      orderBy: { createdAt: "desc" },
    }),
  ]);

  const formattedUsers = usersList.map((u) => ({
    id: u.id,
    name: u.name,
    email: u.email,
    role: u.role,
    createdAt: u.createdAt.toISOString(),
    planStatus: u.plans[0]?.status ?? "SEM_PLANO",
  }));

  return (
    <div className="space-y-6">
      <PageHeader
        title="Liberação Geral e Notificação"
        description="Libere os planejamentos individualizados e envie o e-mail oficial comunicando a conclusão a todos os alunos cadastrados."
      />

      <LiberacaoView
        totalUsers={totalUsers}
        pendingPlansCount={pendingPlansCount}
        activePlansCount={activePlansCount}
        initialIsReleased={platformReleased}
        users={formattedUsers}
      />
    </div>
  );
}
