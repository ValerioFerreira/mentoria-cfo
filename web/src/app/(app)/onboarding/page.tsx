import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { loadPlannerData } from "@/lib/data/planner-data";
import { db } from "@/lib/db";
import { getPendingPlan } from "@/lib/data/study";
import { todayISO } from "@/lib/plan-time";
import { getUserContest } from "@/lib/user-contest";
import { wizardDefaultsFromPlan } from "@/lib/plan/wizard-defaults";
import { CONTEST_SUBJECTS } from "@/lib/contests";
import { contestExamQuestions } from "@/lib/data/contest-data";
import { Wizard, type WizardSubject } from "./wizard";

export const metadata: Metadata = { title: "Montar plano" };

export default async function OnboardingPage() {
  const user = await requireUser();
  const pending = await getPendingPlan(user.id);
  if (pending) {
    redirect("/plano");
  }
  const contest = await getUserContest(user.email);
  const allowed = new Set(CONTEST_SUBJECTS[contest] ?? CONTEST_SUBJECTS.CBMPE_OFICIAL);

  const [{ catalog }, items] = await Promise.all([
    loadPlannerData(),
    db.editalItem.findMany({ orderBy: [{ subjectId: "asc" }, { sortOrder: "asc" }], select: { id: true, subjectId: true, title: true, aulaIds: true } }),
  ]);
  const itemsBySubject = Map.groupBy(items, (i) => i.subjectId);
  const weights = contestExamQuestions(contest);
  const subjects: WizardSubject[] = catalog.subjects
    .filter((s) => allowed.has(s.id))
    .map((s) => {
      const aulas = s.aulas.filter((a) => a.selectable);
      return {
        id: s.id,
        name: s.name,
        block: s.block,
        examQuestions: weights[s.id] ?? s.examQuestions,
        languageGroup: s.languageGroup ?? null,
        items: (itemsBySubject.get(s.id) ?? []).map((i) => ({ id: i.id, title: i.title, aulaIds: i.aulaIds as string[] })),
        aulaIds: aulas.map((a) => a.id),
        hasComplement: aulas.some((a) => a.source === "authored"),
      };
    });
  // refazer o plano: o assistente já abre com as escolhas do plano vigente (o aluno só altera o que quiser mudar)
  const current = await db.plan.findFirst({
    where: { userId: user.id, status: { in: ["ACTIVE", "ARCHIVED"] } },
    orderBy: { version: "desc" },
    select: { startDate: true, examDate: true, params: true, subjects: { select: { subjectId: true, diagnostic: true } } },
  });
  const today = todayISO();
  const initial = wizardDefaultsFromPlan(
    current && {
      startDate: current.startDate.toISOString().slice(0, 10),
      examDate: current.examDate.toISOString().slice(0, 10),
      params: current.params,
      subjects: current.subjects,
    },
    subjects.map((s) => ({ id: s.id, languageGroup: s.languageGroup, items: s.items })),
    today,
  );
  return <Wizard subjects={subjects} todayIso={today} initial={initial} />;
}
