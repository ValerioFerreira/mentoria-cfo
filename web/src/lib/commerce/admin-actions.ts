"use server";

// Ações administrativas de financeiro e parceiros. Cada uma confere ADMIN no servidor (requireAdmin) antes de qualquer
// leitura do formulário; valores, preços e saldos são sempre calculados aqui, nunca aceitos do navegador.
// CSRF: Server Actions do Next só aceitam POST com Origin igual ao host.
import { revalidatePath } from "next/cache";
import * as z from "zod";
import type { Contest } from "@/generated/prisma/client";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { cancelContract, createContract, grantAccessUntilExam } from "./contracts";
import { createSiteCoupon, deleteSiteCoupon, setSiteCouponActive, updateSiteCoupon } from "./coupons";
import { importLegacyPayer } from "./legacy";
import { type ActionResult, toActionError } from "./errors";
import { formatBRL, parseMoneyInput } from "./money";
import { cancelPendingCharges, reconcilePendingCharges } from "./online";
import { registerPayment, reversePayment } from "./payments";
import {
  createPartner,
  deletePartner,
  registerPayout,
  replacePartnerCoupon,
  resetPartnerPassword,
  setCouponActive,
  setPartnerActive,
  updatePartnerProfile,
} from "./partners";

const CONTESTS = ["CBMPE_SOLDADO", "CBMPE_OFICIAL", "PCPE_AGENTE", "PMPE_SOLDADO", "PMPE_OFICIAL", "CBMPE_COMBO", "PMPE_COMBO"] as const;
const Id = z.string().trim().min(1).max(64);
const IsoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Data inválida.");
const Money = z.string().transform((v, ctx) => {
  const cents = parseMoneyInput(v);
  if (cents === null || cents <= 0) {
    ctx.addIssue({ code: "custom", message: "Valor inválido: use números positivos com até 2 casas (ex.: 42,00)." });
    return z.NEVER;
  }
  return cents;
});
const Optional = z.string().trim().max(200).optional().transform((v) => v || null);

/** Data do formulário (dia civil de Recife) -> meio-dia de Recife, para não trocar de dia em UTC. */
const dayAt = (iso: string) => new Date(`${iso}T12:00:00-03:00`);
const form = (fd: FormData) => Object.fromEntries(fd) as Record<string, string>;
const firstIssue = (e: z.ZodError) => ({ ok: false as const, message: e.issues[0]?.message ?? "Dados inválidos." });

function refreshFinance(contractId?: string) {
  revalidatePath("/admin/financeiro");
  if (contractId) revalidatePath(`/admin/financeiro/${contractId}`);
  revalidatePath("/admin/parceiros", "layout");
}

/* ───────────── Pagamentos e contratações ───────────── */

const PaymentSchema = z.object({
  contractId: Id,
  amount: Money,
  paidAt: IsoDate,
  method: z.enum(["PIX", "TRANSFERENCIA", "DINHEIRO", "OUTRO"], { error: "Escolha a forma de pagamento." }),
  receiptRef: Optional,
  note: z.string().trim().max(500).optional(),
  idempotencyKey: z.string().min(8),
});

export async function adminRegisterPayment(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = PaymentSchema.safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const r = await registerPayment(
      { contractId: d.contractId, amountCents: d.amount, paidAt: dayAt(d.paidAt), method: d.method, receiptRef: d.receiptRef, note: d.note, idempotencyKey: d.idempotencyKey },
      admin.id,
    );
    refreshFinance(d.contractId);
    if (r.duplicate) return { ok: true, message: "Este envio já tinha sido registrado (nenhum lançamento duplicado)." };
    const t = r.totals!;
    const extra = t.status === "OVERPAID" ? ` Pagamento excedente de ${formatBRL(-t.balanceCents)} sinalizado para tratamento.` : "";
    return { ok: true, message: `Pagamento registrado. Recebido: ${formatBRL(t.validReceivedCents)} · saldo: ${formatBRL(Math.max(0, t.balanceCents))}.${extra}` };
  } catch (err) {
    return toActionError(err, "registrar pagamento");
  }
}

const ReversalSchema = z.object({
  paymentId: Id,
  contractId: Id,
  amount: Money,
  kind: z.enum(["ESTORNO", "CORRECAO"]),
  reason: z.string().trim().min(5, "Informe a justificativa (mínimo de 5 caracteres).").max(500),
  effectiveAt: IsoDate,
  idempotencyKey: z.string().min(8),
});

export async function adminReversePayment(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = ReversalSchema.safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const r = await reversePayment(
      { paymentId: d.paymentId, amountCents: d.amount, kind: d.kind, reason: d.reason, effectiveAt: dayAt(d.effectiveAt), idempotencyKey: d.idempotencyKey },
      admin.id,
    );
    refreshFinance(d.contractId);
    return { ok: true, message: r.duplicate ? "Este ajuste já tinha sido registrado." : "Estorno/correção registrado; saldo e comissões recalculados." };
  } catch (err) {
    return toActionError(err, "estornar pagamento");
  }
}

export async function adminCancelContract(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ contractId: Id, reason: z.string().trim().max(500) }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await cancelContract(parsed.data.contractId, parsed.data.reason, admin.id);
    await cancelPendingCharges(parsed.data.contractId); // o Pix aberto deixa de valer
    refreshFinance(parsed.data.contractId);
    return { ok: true, message: "Contratação cancelada (mantida no histórico)." };
  } catch (err) {
    return toActionError(err, "cancelar contratação");
  }
}

/** Inclui no financeiro quem pagou antes do valor atual (inscrição da lista de espera com pagamento conferido). */
export async function adminImportLegacyPayer(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z
    .object({ entryId: Id, amount: Money, paidAt: IsoDate, method: z.enum(["PIX", "TRANSFERENCIA", "DINHEIRO", "OUTRO"], { error: "Escolha a forma de pagamento." }) })
    .safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const r = await importLegacyPayer({ waitlistEntryId: d.entryId, amountCents: d.amount, paidAt: dayAt(d.paidAt), method: d.method }, admin.id);
    refreshFinance(r.contractId);
    return { ok: true, message: `Incluído com ${formatBRL(d.amount)} pagos.` };
  } catch (err) {
    return toActionError(err, "incluir pagante anterior");
  }
}

/** Reconsulta no Mercado Pago os Pix pendentes (recupera avisos de webhook perdidos). */
export async function adminReconcileOnline(): Promise<ActionResult> {
  await requireAdmin();
  try {
    const r = await reconcilePendingCharges({ limit: 50 });
    refreshFinance();
    return { ok: true, message: r.checked === 0 ? "Nenhum Pix pendente para conferir." : `${r.checked} Pix conferido(s); ${r.received} com movimento novo${r.errors ? `; ${r.errors} falharam` : ""}.` };
  } catch (err) {
    return toActionError(err, "conferir pagamentos online");
  }
}

export async function adminGrantAccess(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ contractId: Id, override: z.string().optional(), justification: z.string().max(500).optional() }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    const r = await grantAccessUntilExam(parsed.data.contractId, admin.id, { override: parsed.data.override === "on", justification: parsed.data.justification });
    refreshFinance(parsed.data.contractId);
    revalidatePath("/admin/cadastros");
    const until = r.until.toLocaleDateString("pt-BR", { timeZone: "America/Recife" });
    return { ok: true, message: r.keptIndefinite ? `A conta já tinha acesso sem prazo, que foi mantido. Contratação marcada como liberada até ${until}.` : `Acesso liberado até ${until} (dia da prova).` };
  } catch (err) {
    return toActionError(err, "liberar acesso");
  }
}

/** Nova contratação lançada pelo administrador para um cliente (com conta ou não), com preço do servidor. */
export async function adminCreateContract(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z
    .object({ email: z.email("E-mail inválido.").trim().toLowerCase(), name: Optional, contest: z.enum(CONTESTS), coupon: Optional })
    .safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const user = await db.user.findUnique({ where: { email: d.email }, select: { id: true, name: true } });
    const r = await createContract({ contest: d.contest, customerEmail: d.email, customerName: d.name ?? user?.name, userId: user?.id ?? null, couponCode: d.coupon }, admin.id);
    refreshFinance(r.contractId);
    return { ok: true, message: r.created ? "Contratação registrada." : "Já existia uma contratação aberta para este cliente e concurso (nada foi duplicado)." };
  } catch (err) {
    return toActionError(err, "criar contratação");
  }
}

export async function adminUpdateContestSetting(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z
    .object({
      contest: z.enum(CONTESTS),
      category: z.enum(["", "OFICIAL", "PCPE", "PRACA", "COMBO"]),
      examDate: z.union([z.literal(""), IsoDate]),
      price: z.string().trim().max(20).default(""),
      siteDiscount: z.string().trim().max(5).default(""),
    })
    .safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const { contest, category, examDate } = parsed.data;
  // preço do concurso (vazio = padrão da categoria) e desconto do site em % (vazio = desconto padrão de lançamento)
  let priceCents: number | null = null;
  if (parsed.data.price) {
    priceCents = parseMoneyInput(parsed.data.price);
    if (priceCents === null || priceCents <= 0) return { ok: false, message: "Preço inválido: use números positivos com até 2 casas (ex.: 120,00)." };
  }
  let siteDiscountPoints: number | null = null;
  if (parsed.data.siteDiscount) {
    siteDiscountPoints = Number(parsed.data.siteDiscount.replace(",", "."));
    if (!Number.isInteger(siteDiscountPoints) || siteDiscountPoints < 0 || siteDiscountPoints > 100) return { ok: false, message: "Desconto do site: número inteiro de 0 a 100 (%)." };
  }
  try {
    await db.$transaction(async (tx) => {
      const before = await tx.contestSetting.findUnique({ where: { contest: contest as Contest } });
      const data = { category: category || null, examDate: examDate ? new Date(`${examDate}T00:00:00Z`) : null, priceCents, siteDiscountPoints, updatedById: admin.id };
      await tx.contestSetting.upsert({ where: { contest: contest as Contest }, create: { contest: contest as Contest, ...data }, update: data });
      await audit(tx, {
        actorId: admin.id,
        action: "CONTEST_SETTING_UPDATED",
        entityType: "ContestSetting",
        entityId: contest,
        data: {
          before: { category: before?.category ?? null, examDate: before?.examDate?.toISOString().slice(0, 10) ?? null, priceCents: before?.priceCents ?? null, siteDiscountPoints: before?.siteDiscountPoints ?? null },
          after: { category: data.category, examDate: examDate || null, priceCents, siteDiscountPoints },
        },
      });
    });
    revalidatePath("/admin/financeiro");
    revalidatePath("/lista-de-espera", "layout");
    return { ok: true, message: "Concurso atualizado. Contratações já registradas não mudam de preço." };
  } catch (err) {
    return toActionError(err, "atualizar concurso");
  }
}

/* ───────────── Parceiros ───────────── */

export async function adminCreatePartner(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z
    .object({
      email: z.string().trim().max(120),
      username: z.string().trim().max(20),
      name: Optional,
      password: z.string().max(200),
      couponCode: Optional,
      linkExisting: z.string().optional(),
    })
    .safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const r = await createPartner({ email: d.email, username: d.username, name: d.name, password: d.password, couponCode: d.couponCode, linkExisting: d.linkExisting === "on" }, admin.id);
    revalidatePath("/admin/parceiros");
    // a senha inicial nunca é devolvida nem exibida de novo
    return { ok: true, message: r.linked ? `Conta existente vinculada como parceira. Cupom: ${r.couponCode}.` : `Parceiro cadastrado. Cupom: ${r.couponCode}.` };
  } catch (err) {
    return toActionError(err, "cadastrar parceiro");
  }
}

export async function adminUpdatePartner(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ partnerId: Id, name: Optional, username: Optional, email: Optional }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await updatePartnerProfile(parsed.data.partnerId, parsed.data, admin.id);
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: "Dados do parceiro atualizados." };
  } catch (err) {
    return toActionError(err, "editar parceiro");
  }
}

export async function adminDeletePartner(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ partnerId: Id }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await deletePartner(parsed.data.partnerId, admin.id);
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: "Cadastro de parceiro excluído. A conta de usuário continua como conta comum." };
  } catch (err) {
    return toActionError(err, "excluir parceiro");
  }
}

export async function adminSetPartnerActive(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ partnerId: Id, active: z.enum(["true", "false"]) }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    const active = parsed.data.active === "true";
    await setPartnerActive(parsed.data.partnerId, active, admin.id);
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: active ? "Parceiro reativado." : "Parceiro desativado: sessões encerradas e novos logins bloqueados." };
  } catch (err) {
    return toActionError(err, "ativar/desativar parceiro");
  }
}

export async function adminResetPartnerPassword(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ partnerId: Id, password: z.string().max(200) }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await resetPartnerPassword(parsed.data.partnerId, parsed.data.password, admin.id);
    return { ok: true, message: "Senha redefinida e sessões abertas encerradas." };
  } catch (err) {
    return toActionError(err, "redefinir senha do parceiro");
  }
}

export async function adminReplaceCoupon(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ partnerId: Id, code: Optional }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    const code = await replacePartnerCoupon(parsed.data.partnerId, parsed.data.code, admin.id);
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: `Cupom substituído. Novo código: ${code}.` };
  } catch (err) {
    return toActionError(err, "substituir cupom");
  }
}

export async function adminSetCouponActive(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ couponId: Id, active: z.enum(["true", "false"]) }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await setCouponActive(parsed.data.couponId, parsed.data.active === "true", admin.id);
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: parsed.data.active === "true" ? "Cupom ativado." : "Cupom desativado: não vale para novas contratações." };
  } catch (err) {
    return toActionError(err, "ativar/desativar cupom");
  }
}

const PayoutSchema = z.object({
  partnerId: Id,
  amount: Money,
  paidAt: IsoDate,
  method: z.string().trim().min(2, "Informe a forma de pagamento ou a referência.").max(120),
  receiptRef: Optional,
  note: z.string().trim().max(500).optional(),
  idempotencyKey: z.string().min(8),
});

export async function adminRegisterPayout(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = PayoutSchema.safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  const d = parsed.data;
  try {
    const r = await registerPayout(
      { partnerId: d.partnerId, amountCents: d.amount, paidAt: dayAt(d.paidAt), method: d.method, receiptRef: d.receiptRef, note: d.note, idempotencyKey: d.idempotencyKey },
      admin.id,
    );
    revalidatePath("/admin/parceiros", "layout");
    return { ok: true, message: r.duplicate ? "Este repasse já tinha sido registrado." : `Repasse de ${formatBRL(d.amount)} registrado.` };
  } catch (err) {
    return toActionError(err, "registrar repasse");
  }
}

/* ───────────── Cupons do site (/admin/cupons) ───────────── */

const CouponCode = z.string().trim().max(20, "O cupom deve ter de 4 a 20 letras maiúsculas ou números.");
const CouponPoints = z.string().trim().max(6);

export async function adminCreateSiteCoupon(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ code: CouponCode, discountPoints: CouponPoints }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    const c = await createSiteCoupon(parsed.data, admin.id);
    revalidatePath("/admin/cupons");
    return { ok: true, message: `Cupom ${c.code} criado.` };
  } catch (err) {
    return toActionError(err, "criar cupom");
  }
}

export async function adminUpdateSiteCoupon(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ couponId: Id, code: CouponCode.optional(), discountPoints: CouponPoints }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await updateSiteCoupon(parsed.data.couponId, parsed.data, admin.id);
    revalidatePath("/admin/cupons");
    return { ok: true, message: "Cupom atualizado. Contratações já registradas não mudam de preço." };
  } catch (err) {
    return toActionError(err, "editar cupom");
  }
}

export async function adminSetSiteCouponActive(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ couponId: Id, active: z.enum(["true", "false"]) }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    const active = parsed.data.active === "true";
    await setSiteCouponActive(parsed.data.couponId, active, admin.id);
    revalidatePath("/admin/cupons");
    return { ok: true, message: active ? "Cupom ativado." : "Cupom inativado: não vale para novas contratações." };
  } catch (err) {
    return toActionError(err, "ativar/inativar cupom");
  }
}

export async function adminDeleteSiteCoupon(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const admin = await requireAdmin();
  const parsed = z.object({ couponId: Id }).safeParse(form(fd));
  if (!parsed.success) return firstIssue(parsed.error);
  try {
    await deleteSiteCoupon(parsed.data.couponId, admin.id);
    revalidatePath("/admin/cupons");
    return { ok: true, message: "Cupom excluído." };
  } catch (err) {
    return toActionError(err, "excluir cupom");
  }
}
