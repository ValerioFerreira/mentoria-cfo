"use server";

import { revalidatePath } from "next/cache";
import * as z from "zod";
import { requireUser } from "@/lib/auth/dal";
import type { OverdueActivity, RescheduleApplied, RescheduleError, RescheduleInput, ReschedulePreview } from "@/lib/planner/reschedule-types";
import { applyComputed, buildPreview, compute, isScenario, loadScenario, overdueOf } from "./reschedule-data";

const Input = z.object({
  activityIds: z.array(z.string().min(1).max(64)).min(1).max(1000),
  params: z.object({
    option: z.enum(["SPREAD", "FILL_GAPS", "RECALC_REST", "MOVE_TO_DAY", "DISMISS"]),
    windowDays: z.union([z.literal(3), z.literal(7), z.literal(14)]).optional(),
    extraLoadPct: z.union([z.literal(15), z.literal(25), z.literal(40)]).optional(),
    targetDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
  }),
});

const invalid = (): RescheduleError => ({ ok: false, error: "Escolha inválida. Atualize a página e tente de novo." });

/** Atividades atrasadas do plano ativo do aluno (passo 1 da tela de reprogramação). */
export async function listOverdue(): Promise<{ ok: true; overdue: OverdueActivity[] } | RescheduleError> {
  const user = await requireUser();
  const sc = await loadScenario(user.id);
  if (!isScenario(sc)) return sc;
  return { ok: true, overdue: overdueOf(sc) };
}

/** Só calcula: mostra para onde cada atividade iria (inclusive as dependentes) e o que muda na carga dos dias. Não grava nada. */
export async function previewReschedule(input: RescheduleInput): Promise<ReschedulePreview | RescheduleError> {
  const user = await requireUser();
  const parsed = Input.safeParse(input);
  if (!parsed.success) return invalid();
  const sc = await loadScenario(user.id);
  if (!isScenario(sc)) return sc;
  const c = await compute(sc, parsed.data);
  if ("ok" in c) return c;
  return buildPreview(c, parsed.data);
}

/** Recalcula no servidor (nunca confia na prévia do navegador) e grava numa transação. */
export async function applyReschedule(input: RescheduleInput): Promise<RescheduleApplied | RescheduleError> {
  const user = await requireUser();
  const parsed = Input.safeParse(input);
  if (!parsed.success) return invalid();
  const sc = await loadScenario(user.id);
  if (!isScenario(sc)) return sc;
  const c = await compute(sc, parsed.data);
  if ("ok" in c) return c;
  const done = await applyComputed(c, parsed.data);
  revalidatePath("/", "layout");
  return done;
}
