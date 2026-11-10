import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { quote } from "@/lib/commerce/pricing";
import { pendingPaidSwitch } from "@/lib/commerce/switch";
import { getUserContest } from "@/lib/user-contest";
import { maskCpf } from "@/lib/cpf";
import { CpfCard } from "./cpf-card";
import { PerfilView, type UserProfileData } from "./perfil-view";

export const metadata: Metadata = { title: "Meu Perfil" };

export default async function PerfilPage({ searchParams }: { searchParams: Promise<{ cpf?: string }> }) {
  const { cpf: cpfParam } = await searchParams;
  const sessionUser = await requireUser();

  const [user, contest] = await Promise.all([
    db.user.findUnique({
      where: { id: sessionUser.id },
      select: {
        id: true,
        name: true,
        email: true,
        username: true,
        role: true,
        createdAt: true,
        accessExpiresAt: true,
        mustChangePassword: true,
        cpf: true,
      },
    }),
    getUserContest(sessionUser.email),
  ]);

  if (!user) {
    return null;
  }

  const settings = await db.contestSetting.findMany();
  const contestPrices: Record<string, number | null> = Object.fromEntries(
    settings.map((s) => [s.contest, s.category ? quote(s.category, 0, s).finalCents : null]),
  );
  const resumePaidSwitch = Boolean(await pendingPaidSwitch(user.id, user.email));

  const { cpf, ...userData } = user;
  const profileData: UserProfileData = {
    ...userData,
    isPartner: sessionUser.isPartner,
    contest,
    contestPrices,
    resumePaidSwitch,
    createdAt: user.createdAt.toISOString(),
    accessExpiresAt: user.accessExpiresAt ? user.accessExpiresAt.toISOString() : null,
  };

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Conta"
        title="Meu Perfil"
        description="Gerencie os dados da sua conta de acesso, validade do seu plano, concurso escolhido e suas credenciais de segurança."
      />

      <CpfCard masked={cpf ? maskCpf(cpf) : null} required={cpfParam === "necessario"} />
      <PerfilView user={profileData} />
    </div>
  );
}
