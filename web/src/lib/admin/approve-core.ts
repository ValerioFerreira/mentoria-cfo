import "server-only";
import { hashPassword } from "@/lib/auth/password";
import { audit } from "@/lib/commerce/audit";
import { grantAccessUntilExam, linkContractsToUser } from "@/lib/commerce/contracts";
import { CommerceError } from "@/lib/commerce/errors";
import { db } from "@/lib/db";
import { generateTemporaryPassword, sendApprovalEmail } from "@/lib/email";

export type AccessDuration = "UNTIL_EXAM" | "30_DAYS" | "INDEFINITE";

export interface ApproveInput {
  entryId: string;
  duration: AccessDuration;
  /** administrador que aprova; nulo quando a aprovação é automática (pagamento confirmado) */
  actorId: string | null;
  override?: boolean;
  justification?: string;
  /** automático: só aprova inscrição ainda pendente (avisos repetidos não geram segunda senha nem segundo e-mail) */
  onlyIfPending?: boolean;
}

export interface ApproveOutcome {
  success: boolean;
  message: string;
  /** só no fluxo manual (o administrador copia quando o e-mail não sai) */
  tempPassword?: string;
  emailSent?: boolean;
  /** recusa esperada (já tratada, sem prova cadastrada, etc.) com o código do motivo */
  code?: string;
  entryName?: string;
}

/**
 * Aprova uma inscrição da lista de espera: cria (ou atualiza) a conta com senha temporária, liga as contratações,
 * libera o acesso conforme a validade e avisa por e-mail. É o mesmo caminho do administrador e da aprovação automática
 * depois da confirmação do pagamento; tudo na mesma transação (se a data da prova não existe, nada é criado).
 */
export async function approveWaitlistEntry(input: ApproveInput): Promise<ApproveOutcome> {
  const { duration, actorId } = input;
  if (duration !== "UNTIL_EXAM" && duration !== "30_DAYS" && duration !== "INDEFINITE") {
    return { success: false, message: "Validade inválida.", code: "INVALID" };
  }
  const entry = await db.waitlistEntry.findUnique({ where: { id: input.entryId } });
  if (!entry) return { success: false, message: "Registro da lista de espera não encontrado.", code: "NOT_FOUND" };

  // acesso até a prova: precisa da contratação (obrigação financeira) desta inscrição
  const contract = await db.contract.findFirst({
    where: { customerEmail: entry.email, contest: entry.contest, status: { not: "CANCELLED" } },
    orderBy: { createdAt: "desc" },
    select: { id: true },
  });
  if (duration === "UNTIL_EXAM" && !contract) {
    return { success: false, message: "Esta inscrição não tem contratação registrada. Registre-a em Financeiro ou escolha outra validade.", code: "NO_CONTRACT" };
  }

  const tempPassword = generateTemporaryPassword("MTR");
  const passwordHash = await hashPassword(tempPassword);
  const accessExpiresAt = duration === "30_DAYS" ? new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) : null;

  let accessUntil: Date | null = null;
  try {
    await db.$transaction(async (tx) => {
      if (input.onlyIfPending) {
        await tx.$queryRaw`SELECT "id" FROM "WaitlistEntry" WHERE "id" = ${entry.id} FOR UPDATE`;
        const current = await tx.waitlistEntry.findUniqueOrThrow({ where: { id: entry.id }, select: { status: true } });
        if (current.status !== "PENDING") throw new CommerceError("Inscrição já tratada.", "ALREADY_HANDLED");
      }
      const existingUser = await tx.user.findUnique({ where: { email: entry.email }, include: { partner: { select: { id: true } } } });
      let userId: string;
      if (!existingUser) {
        let username = entry.username;
        const userWithUsername = await tx.user.findUnique({ where: { username } });
        if (userWithUsername) username = `${username}_${Math.floor(100 + Math.random() * 900)}`;
        userId = (
          await tx.user.create({
            data: { name: entry.name, email: entry.email, username, passwordHash, mustChangePassword: true, accessExpiresAt, role: "USER" },
          })
        ).id;
      } else {
        if (existingUser.role !== "USER") throw new CommerceError("Este e-mail pertence a um administrador.", "EMAIL_ADMIN");
        if (existingUser.partner) throw new CommerceError("Este e-mail é de um parceiro: libere o acesso pela contratação, em Financeiro (a senha do parceiro não é trocada).", "EMAIL_PARTNER");
        userId = existingUser.id;
        await tx.user.update({ where: { id: userId }, data: { passwordHash, mustChangePassword: true, accessExpiresAt } });
      }
      await linkContractsToUser(tx, userId, entry.email);
      if (duration === "UNTIL_EXAM" && contract) {
        // mesma regra do Financeiro: exige data da prova e quitação (ou liberação justificada)
        const g = await grantAccessUntilExam(contract.id, actorId, { override: input.override, justification: input.justification, newAccount: true }, tx);
        accessUntil = g.until;
      }
      await tx.waitlistEntry.update({
        where: { id: entry.id },
        data: { status: "APPROVED", paidAt: entry.paidAt ?? new Date(), approvedAt: new Date(), accessDuration: duration },
      });
      if (actorId === null && contract) {
        await audit(tx, { actorId: null, action: "AUTO_APPROVED", entityType: "Contract", entityId: contract.id, data: { entryId: entry.id, until: (accessUntil as Date | null)?.toISOString() ?? null } });
      }
    });
  } catch (err) {
    if (err instanceof CommerceError) return { success: false, message: err.message, code: err.code, entryName: entry.name };
    throw err;
  }

  const loginUrl = `${(process.env.SITE_URL || process.env.APP_URL || "https://www.missaomentoria.com.br").replace(/\/$/, "")}/login`;
  let emailSent = false;
  try {
    const res = await sendApprovalEmail({ to: entry.email, name: entry.name, tempPassword, accessDuration: duration, accessUntil, loginUrl });
    emailSent = res?.success ?? false;
  } catch (err) {
    console.error("Erro ao enviar e-mail de aprovação:", err instanceof Error ? err.message : "erro desconhecido");
  }
  if (actorId === null && !emailSent && contract) {
    // a conta já existe com senha temporária que ninguém recebeu: o administrador reenvia as credenciais em Cadastros
    await db.$transaction((tx) => audit(tx, { actorId: null, action: "AUTO_APPROVAL_EMAIL_FAILED", entityType: "Contract", entityId: contract.id, data: { entryId: entry.id } }));
  }
  return {
    success: true,
    message: emailSent
      ? `Cadastro de ${entry.name} aprovado com sucesso! E-mail com senha temporária enviado.`
      : `Cadastro de ${entry.name} aprovado! Atenção: configure RESEND_API_KEY ou SMTP na Vercel para envio automático. Copie a senha temporária abaixo para enviar ao aluno.`,
    tempPassword: actorId === null ? undefined : tempPassword,
    emailSent,
    entryName: entry.name,
  };
}
