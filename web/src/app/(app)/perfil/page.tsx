import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { getUserContest } from "@/lib/user-contest";
import { PerfilView, type UserProfileData } from "./perfil-view";

export const metadata: Metadata = { title: "Meu Perfil" };

export default async function PerfilPage() {
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
      },
    }),
    getUserContest(sessionUser.email),
  ]);

  if (!user) {
    return null;
  }

  const profileData: UserProfileData = {
    ...user,
    contest,
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

      <PerfilView user={profileData} />
    </div>
  );
}
