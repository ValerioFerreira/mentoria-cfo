import type { WaitlistPlan } from "@/generated/prisma/client";

export interface PlanInfo {
  key: WaitlistPlan;
  name: string;
  /** valor no formato do Pix (campo 54 do BR Code) */
  amount: string;
  /** valor para exibir, sem o "R$" */
  price: string;
}

/** Planos oferecidos na lista de espera. O valor do Pix vem daqui. */
export const WAITLIST_PLANS: Record<WaitlistPlan, PlanInfo> = {
  MONTHLY: { key: "MONTHLY", name: "Mensalidade", amount: "35.00", price: "35,00" },
  UNTIL_EXAM: { key: "UNTIL_EXAM", name: "Acesso até a prova", amount: "100.00", price: "100,00" },
};

export const PLAN_KEYS = Object.keys(WAITLIST_PLANS) as WaitlistPlan[];

export function isPlan(v: unknown): v is WaitlistPlan {
  return typeof v === "string" && v in WAITLIST_PLANS;
}
