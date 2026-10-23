import type { Contest, ContractStatus, PaymentMethod } from "@/generated/prisma/client";
import type { FinanceFilters } from "@/lib/commerce/queries";

export type SearchParams = Record<string, string | string[] | undefined>;

const CONTESTS: Contest[] = ["CBMPE_OFICIAL", "CBMPE_SOLDADO", "PMPE_OFICIAL", "PMPE_SOLDADO", "PCPE_AGENTE", "CBMPE_COMBO", "PMPE_COMBO"];
const STATUSES: ContractStatus[] = ["OPEN", "PARTIAL", "PAID", "OVERPAID", "CANCELLED"];
const METHODS: PaymentMethod[] = ["PIX", "CARTAO", "TRANSFERENCIA", "DINHEIRO", "OUTRO"];
const one = (v: string | string[] | undefined) => (Array.isArray(v) ? v[0] : v)?.trim() || undefined;
const day = (v: string | undefined, end: boolean) =>
  v && /^\d{4}-\d{2}-\d{2}$/.test(v) ? new Date(`${v}T${end ? "23:59:59.999" : "00:00:00.000"}-03:00`) : undefined;

/** Filtros da URL validados contra listas fechadas (nada vai cru para a consulta). */
export function parseFilters(sp: SearchParams): FinanceFilters & { raw: Record<string, string> } {
  const raw: Record<string, string> = {};
  for (const k of ["q", "concurso", "situacao", "forma", "de", "ate"]) {
    const v = one(sp[k]);
    if (v) raw[k] = v.slice(0, 80);
  }
  return {
    raw,
    q: raw.q,
    contest: CONTESTS.find((c) => c === raw.concurso),
    status: STATUSES.find((s) => s === raw.situacao),
    method: METHODS.find((m) => m === raw.forma),
    from: day(raw.de, false),
    to: day(raw.ate, true),
  };
}

export { CONTESTS as FILTER_CONTESTS, METHODS as FILTER_METHODS, STATUSES as FILTER_STATUSES };
