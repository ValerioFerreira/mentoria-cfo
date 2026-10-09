import "server-only";
import { randomUUID } from "node:crypto";
import { db } from "@/lib/db";
import type { PlanInput, PlanResult } from "@/lib/planner/types";

interface SaveArgs {
  userId: string;
  input: PlanInput;
  result: PlanResult;
  diagnostics: Record<string, unknown>;
  foreignLanguage: "EN" | "ES" | null;
  hoursBand: "LEVE" | "MODERADO" | "AVANCADO";
}

/** Persiste o plano gerado e arquiva o anterior (o histórico de tempo e cadernos é preservado). */
export async function savePlan({ userId, input, result, diagnostics, foreignLanguage, hoursBand }: SaveArgs): Promise<string> {
  return db.$transaction(
    async (tx) => {
      const prev = await tx.plan.findFirst({ where: { userId, status: "ACTIVE" }, orderBy: { version: "desc" } });
      if (prev) await tx.plan.update({ where: { id: prev.id }, data: { status: "ARCHIVED" } });

      await tx.profile.upsert({
        where: { userId },
        create: { userId, examDate: new Date(input.examDate), hoursBand, hoursPerWeek: input.hoursPerWeek, foreignLanguage },
        update: { examDate: new Date(input.examDate), hoursBand, hoursPerWeek: input.hoursPerWeek, foreignLanguage },
      });

      const plan = await tx.plan.create({
        data: {
          userId,
          version: (prev?.version ?? 0) + 1,
          startDate: new Date(input.startDate),
          examDate: new Date(input.examDate),
          params: result.params as object,
          coverage: result.coverage as object,
          warnings: result.warnings,
        },
      });

      await tx.planSubject.createMany({
        data: input.subjects.map((s) => ({ planId: plan.id, subjectId: s.id, level: s.level, diagnostic: (diagnostics[s.id] ?? {}) as object })),
      });

      const weekIds = new Map<number, string>();
      const weekRows = result.weeks.map((w) => {
        const id = randomUUID();
        weekIds.set(w.index, id);
        return { id, planId: plan.id, index: w.index, startDate: new Date(w.startDate), targetMinutes: w.targetMinutes, kind: w.kind };
      });
      await tx.week.createMany({ data: weekRows });

      const keyToId = new Map<string, string>();
      const activityRows = result.weeks.flatMap((w) =>
        w.activities.map((a, order) => {
          const id = randomUUID();
          keyToId.set(a.key, id);
          return {
            id, planId: plan.id, weekId: weekIds.get(w.index)!, sortOrder: order, type: a.type, subjectId: a.subjectId, aulaId: a.aulaId,
            plannedMinutes: a.minutes, key: a.key, scope: a.scope ?? ("AULA" as const),
            fixRanges: a.fixRanges ? (a.fixRanges as object[]) : undefined,
            dayIndex: a.day ?? null, turbo: a.turbo ?? false, quizQuestions: a.quiz?.questions ?? null, quizLimitSec: a.quiz?.limitSeconds ?? null, quizMixed: a.quiz?.mixed ?? false,
          };
        }),
      );
      for (let i = 0; i < activityRows.length; i += 500) await tx.activity.createMany({ data: activityRows.slice(i, i + 500) });

      const segRows = result.weeks.flatMap((w) =>
        w.activities.flatMap((a) => [...new Set(a.segmentIds)].map((segmentId) => ({ activityId: keyToId.get(a.key)!, segmentId }))),
      );
      for (let i = 0; i < segRows.length; i += 1000) await tx.activitySegment.createMany({ data: segRows.slice(i, i + 1000) });

      const refRows = result.weeks.flatMap((w) =>
        w.activities.flatMap((a) => a.refKeys.map((k) => ({ activityId: keyToId.get(a.key)!, refActivityId: keyToId.get(k)! }))),
      );
      for (let i = 0; i < refRows.length; i += 1000) await tx.activityRef.createMany({ data: refRows.slice(i, i + 1000) });

      return plan.id;
    },
    { timeout: 60_000, maxWait: 10_000 },
  );
}
