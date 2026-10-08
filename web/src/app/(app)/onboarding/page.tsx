import type { Metadata } from "next";
import { requireUser } from "@/lib/auth/dal";
import { loadPlannerData } from "@/lib/data/planner-data";
import { todayISO } from "@/lib/plan-time";
import { Wizard, type WizardSubject } from "./wizard";

export const metadata: Metadata = { title: "Montar plano" };

export default async function OnboardingPage() {
  await requireUser();
  const { catalog } = await loadPlannerData();
  const subjects: WizardSubject[] = catalog.subjects.map((s) => {
    const aulas = s.aulas.filter((a) => a.selectable);
    return {
      id: s.id,
      name: s.name,
      block: s.block,
      examQuestions: s.examQuestions,
      languageGroup: s.languageGroup ?? null,
      aulas: aulas.map((a) => ({ id: a.id, number: a.number, title: a.shortTitle, pages: a.theoryPages, authored: a.source === "authored" })),
      theoryPages: aulas.reduce((n, a) => n + a.theoryPages, 0),
      hasComplement: aulas.some((a) => a.source === "authored"),
    };
  });
  return <Wizard subjects={subjects} todayIso={todayISO()} />;
}
