"use server";

import { redirect } from "next/navigation";
import * as z from "zod";
import { requireUser } from "@/lib/auth/dal";
import { loadPlannerData } from "@/lib/data/planner-data";
import { bandOf, dayIndexOf, generatePlan, mondayOf, PlanInputError } from "@/lib/planner";
import { addDays } from "@/lib/planner/dates";
import { todayISO } from "@/lib/plan-time";
import { savePlan } from "@/lib/plan/persist";
import type { Known, Level } from "@/lib/planner/types";

/** Data real no formato AAAA-MM-DD (rejeita 2027-02-30) e no máximo ~2 anos à frente (evita planos com milhares de semanas). */
const examDateOk = (v: string) => {
  const d = new Date(`${v}T00:00:00Z`);
  if (Number.isNaN(d.getTime()) || d.toISOString().slice(0, 10) !== v) return false;
  return v <= addDays(todayISO(), 730);
};

const Selection = z.object({
  subjects: z
    .array(z.object({ id: z.string(), level: z.union([z.literal(0), z.literal(1), z.literal(2), z.literal(3)]) }))
    .min(1, "Escolha ao menos uma disciplina.")
    .refine((l) => new Set(l.map((s) => s.id)).size === l.length, "Há disciplinas repetidas."),
  hoursPerWeek: z.number().int().min(14).max(50),
  examDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).refine(examDateOk, "Data da prova inválida ou distante demais (máximo de 2 anos)."),
  /** "now" = começar hoje (dia civil de Recife); ou uma data AAAA-MM-DD escolhida na agenda */
  start: z.union([z.literal("now"), z.string().regex(/^\d{4}-\d{2}-\d{2}$/)]).default("now"),
  /** anamnese por aula: id da aula → 1 (já estudei) ou 2 (domino); ausente = nunca estudei */
  known: z.record(z.string(), z.union([z.literal(0), z.literal(1), z.literal(2)])).default({}),
  /** Modo Turbo: se o tempo não fechar o edital, as aulas de menor valor viram resumos */
  turbo: z.boolean().default(false),
});
export type SelectionInput = z.input<typeof Selection>;

/**
 * Resolve a data de início. "Começar imediatamente" usa o dia civil de Recife no servidor (não o UTC, que vira o dia
 * às 21h locais). A semana 1 sempre começa na segunda; `firstDay` marca em que dia dela o aluno entra.
 */
function resolveStart(start: string): { startDate: string; firstDay: number; firstStudyDate: string } | { error: string } {
  const today = todayISO();
  const first = start === "now" ? today : start;
  if (first < today) return { error: "A data de início não pode estar no passado." };
  return { startDate: mondayOf(first), firstDay: dayIndexOf(first), firstStudyDate: first };
}

/** Prévia leve (sem gravar) para mostrar a cobertura estimada enquanto o aluno ajusta as horas. */
export async function previewPlan(input: SelectionInput) {
  await requireUser();
  const parsed = Selection.safeParse(input);
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Dados inválidos." } as const;
  const begin = resolveStart(parsed.data.start);
  if ("error" in begin) return { error: begin.error } as const;
  const data = await loadPlannerData();
  try {
    const r = generatePlan({
      ...data,
      startDate: begin.startDate,
      firstDay: begin.firstDay,
      examDate: parsed.data.examDate,
      hoursPerWeek: parsed.data.hoursPerWeek,
      subjects: parsed.data.subjects as { id: string; level: Level }[],
      known: parsed.data.known as Record<string, Known>,
      turbo: parsed.data.turbo,
    });
    return {
      ok: true as const,
      coverageSelected: r.coverage.selected,
      coverageEdital: r.coverage.edital,
      depth: r.coverage.depth,
      totalWeeks: r.params.totalWeeks,
      capacityHours: r.params.capacityHours,
      plannedHours: r.params.plannedHours,
      fullEditalHoursPerWeek: r.params.fullEditalHoursPerWeek,
      editalFits: r.params.editalFits,
      turboAulas: r.params.turboAulas,
      subjects: r.coverage.subjects.map((s) => ({ id: s.subjectId, hours: s.plannedHours, coverage: s.coverage, depth: s.depth })),
    };
  } catch (e) {
    if (e instanceof PlanInputError) return { error: e.message } as const;
    throw e;
  }
}

export async function createPlanAction(input: SelectionInput & { diagnostics: Record<string, unknown> }): Promise<{ error: string } | never> {
  const user = await requireUser();
  const parsed = Selection.safeParse(input);
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Dados inválidos." };
  const begin = resolveStart(parsed.data.start);
  if ("error" in begin) return { error: begin.error };
  const data = await loadPlannerData();
  const planInput = {
    ...data,
    startDate: begin.startDate,
    firstDay: begin.firstDay,
    examDate: parsed.data.examDate,
    hoursPerWeek: parsed.data.hoursPerWeek,
    subjects: parsed.data.subjects as { id: string; level: Level }[],
    known: parsed.data.known as Record<string, Known>,
    turbo: parsed.data.turbo,
  };
  let result;
  try {
    result = generatePlan(planInput);
  } catch (e) {
    if (e instanceof PlanInputError) return { error: e.message };
    throw e;
  }
  // a anamnese de cada disciplina guarda as 3 respostas + as aulas marcadas
  const diagnostics: Record<string, unknown> = {};
  for (const s of parsed.data.subjects) {
    const aulas = Object.fromEntries(Object.entries(parsed.data.known).filter(([id, v]) => id.startsWith(`${s.id}/`) && v > 0));
    diagnostics[s.id] = { ...((input.diagnostics?.[s.id] as object | undefined) ?? {}), aulas };
  }
  const lang = parsed.data.subjects.find((s) => s.id === "lingua-inglesa") ? "EN" : parsed.data.subjects.find((s) => s.id === "lingua-espanhola") ? "ES" : null;
  await savePlan({
    userId: user.id,
    input: planInput,
    result,
    diagnostics,
    foreignLanguage: lang,
    hoursBand: bandOf(parsed.data.hoursPerWeek) === "LEVE" ? "LEVE" : bandOf(parsed.data.hoursPerWeek) === "MODERADO" ? "MODERADO" : "AVANCADO",
  });
  redirect("/plano");
}
