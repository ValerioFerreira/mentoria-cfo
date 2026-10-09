import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { PerfilView, type UserProfileData } from "./perfil-view";

export const metadata: Metadata = { title: "Meu Perfil" };

export default async function PerfilPage() {
  const sessionUser = await requireUser();

  const user = await db.user.findUnique({
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
  });

  if (!user) {
    return null;
  }

  const profileData: UserProfileData = {
    ...user,
    createdAt: user.createdAt.toISOString(),
    accessExpiresAt: user.accessExpiresAt ? user.accessExpiresAt.toISOString() : null,
  };

  return (
    <div className="space-y-6">
      <PageHeader
        eyebrow="Conta"
        title="Meu Perfil"
        description="Gerencie os dados da sua conta de acesso, validade do seu plano e suas credenciais de segurança."
      />

      <PerfilView user={profileData} />
    </div>
  );
}
