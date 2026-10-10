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

  const pendingPlansRaw = await db.plan.findMany({
    where: { status: "PENDING_ANALYSIS" },
    orderBy: { createdAt: "desc" },
    include: {
      user: { select: { id: true, name: true, email: true } },
      subjects: { select: { subjectId: true } },
    },
  });

  const formattedPlans = pendingPlansRaw.map((p) => {
    const params = p.params as { hoursPerWeek?: number; totalWeeks?: number } | null;
    return {
      id: p.id,
      userId: p.user.id,
      userName: p.user.name || p.user.email,
      userEmail: p.user.email,
      createdAt: p.createdAt.toISOString(),
      examDate: p.examDate.toISOString().slice(0, 10),
      version: p.version,
      hoursPerWeek: params?.hoursPerWeek ?? null,
      subjectCount: p.subjects.length,
    };
  });

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Administração"
        title="Gestão de Cadastros"
        description="Aprove ou recuse os cadastros da lista de espera e libere os planejamentos personalizados solicitados pelos alunos."
      />

      <CadastrosView entries={formatted} pendingPlans={formattedPlans} />
    </div>
  );
}
