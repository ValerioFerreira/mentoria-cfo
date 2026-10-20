import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { loadPlannerData } from "@/lib/data/planner-data";
import { db } from "@/lib/db";
import { getPendingPlan } from "@/lib/data/study";
import { todayISO } from "@/lib/plan-time";
import { getUserContest } from "@/lib/user-contest";
import { wizardDefaultsFromPlan } from "@/lib/plan/wizard-defaults";
import { CONTEST_SUBJECTS, editalItemApplies } from "@/lib/contests";
import { contestExamQuestions } from "@/lib/data/contest-data";
import { EXAM_CONFIGS, type SupportedSimuladoContest } from "@/lib/simulado-rules";
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
    db.editalItem.findMany({ orderBy: [{ subjectId: "asc" }, { sortOrder: "asc" }], select: { id: true, subjectId: true, title: true, aulaIds: true, onlyContests: true, excludeContests: true } }),
  ]);
  const itemsBySubject = Map.groupBy(items, (i) => i.subjectId);
  const weights = contestExamQuestions(contest);
  // blocos da prova do concurso (no PCPE: P1 Noções de Direito e P2 Conhecimentos Específicos) e data da prova cadastrada
  const exam = EXAM_CONFIGS[contest as SupportedSimuladoContest];
  const blockOf = new Map((exam?.subjects ?? []).map((x) => [x.subjectId, x.block]));
  const blockNames = contest === "PCPE_AGENTE" && exam ? { I: exam.blocks.I.name, II: exam.blocks.II.name } : undefined;
  const examDate = (await db.contestSetting.findUnique({ where: { contest }, select: { examDate: true } }))?.examDate?.toISOString().slice(0, 10) ?? null;
  const subjects: WizardSubject[] = catalog.subjects
    .filter((s) => allowed.has(s.id))
    .map((s) => {
      const aulas = s.aulas.filter((a) => a.selectable);
      return {
        id: s.id,
        name: s.name,
        block: (contest === "PCPE_AGENTE" ? blockOf.get(s.id) : undefined) ?? s.block,
        examQuestions: weights[s.id] ?? s.examQuestions,
        languageGroup: s.languageGroup ?? null,
        items: (itemsBySubject.get(s.id) ?? []).filter((i) => editalItemApplies(i, contest)).map((i) => ({ id: i.id, title: i.title, aulaIds: i.aulaIds as string[] })),
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
  return <Wizard subjects={subjects} todayIso={today} initial={initial} defaultExamDate={examDate} blockNames={blockNames} />;
}
