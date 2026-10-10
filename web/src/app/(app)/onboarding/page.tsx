import type { Metadata } from "next";
import { requireUser } from "@/lib/auth/dal";
import { loadPlannerData } from "@/lib/data/planner-data";
import { db } from "@/lib/db";
import { todayISO } from "@/lib/plan-time";
import { getUserContest } from "@/lib/user-contest";
import { CONTEST_SUBJECTS } from "@/lib/contests";
import { Wizard, type WizardSubject } from "./wizard";

export const metadata: Metadata = { title: "Montar plano" };

export default async function OnboardingPage() {
  const user = await requireUser();
  const contest = await getUserContest(user.email);
  const allowed = new Set(CONTEST_SUBJECTS[contest] ?? CONTEST_SUBJECTS.CBMPE_OFICIAL);

  const [{ catalog }, items] = await Promise.all([
    loadPlannerData(),
    db.editalItem.findMany({ orderBy: [{ subjectId: "asc" }, { sortOrder: "asc" }], select: { id: true, subjectId: true, title: true, aulaIds: true } }),
  ]);
  const itemsBySubject = Map.groupBy(items, (i) => i.subjectId);
  const subjects: WizardSubject[] = catalog.subjects
    .filter((s) => allowed.has(s.id))
    .map((s) => {
      const aulas = s.aulas.filter((a) => a.selectable);
      return {
        id: s.id,
        name: s.name,
        block: s.block,
        examQuestions: s.examQuestions,
        languageGroup: s.languageGroup ?? null,
        items: (itemsBySubject.get(s.id) ?? []).map((i) => ({ id: i.id, title: i.title, aulaIds: i.aulaIds as string[] })),
        aulaIds: aulas.map((a) => a.id),
        hasComplement: aulas.some((a) => a.source === "authored"),
      };
    });
  return <Wizard subjects={subjects} todayIso={todayISO()} />;
}
