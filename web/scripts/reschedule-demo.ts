// Plano de demonstração LOCAL com atividades atrasadas, para testar a reprogramação (só banco local, só o usuário de teste).
//   npx tsx --conditions=react-server scripts/reschedule-demo.ts [--opcao SPREAD|FILL_GAPS|MOVE_TO_DAY|DISMISS|RECALC_REST] [--janela 3|7|14] [--extra 15|25|40] [--horas 21] [--aplicar]
// Cria (e ativa) um plano de 21 h/semana para teste@teste.com que começou 4 semanas atrás: as atividades de mais de 10 dias atrás ficam
// FEITAS, as dos 10 dias anteriores a hoje ficam ATRASADAS. Com --opcao, calcula a prévia (e grava com --aplicar) para todas as atrasadas.
// Depois: npx tsx scripts/verify-plans.ts --plan <id>   (confere o plano gravado com as regras do verificador)
import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { addDaysISO, dayOfWeekIndex, diffDaysISO, todayISO } from "../src/lib/plan-time";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "../src/lib/planner/fixtures";
import type { Level } from "../src/lib/planner/types";
import { localDatabase, TEST_USER_EMAIL } from "../src/lib/test-user";

const args = process.argv.slice(2);
const opt = (n: string) => (args.includes(n) ? args[args.indexOf(n) + 1] : undefined);

async function main() {
  if (!localDatabase()) throw new Error("DATABASE_URL não aponta para localhost: a demonstração só roda no banco local.");
  const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
  await db.$executeRawUnsafe("SET search_path TO public");
  const user = await db.user.findUnique({ where: { email: TEST_USER_EMAIL } });
  if (!user) throw new Error("Usuário de teste não existe: rode scripts/create-test-user.ts");
  const { savePlan } = await import("../src/lib/plan/persist");
  const { applyComputed, buildPreview, compute, isScenario, loadScenario } = await import("../src/lib/plan/reschedule-data");

  const today = todayISO();
  const back = addDaysISO(today, -28);
  const startIso = addDaysISO(back, -dayOfWeekIndex(back)); // segunda-feira de 4 semanas atrás
  const examIso = "2027-02-28";
  const hours = Number(opt("--horas") ?? 21);
  const catalog = loadCatalog();
  const segments = loadSegments();
  const importance = loadImportance("CBMPE_OFICIAL");
  const examQuestions = loadExamQuestions("CBMPE_OFICIAL");
  const subjects = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
  const input = { catalog, segments, startDate: startIso, examDate: examIso, hoursPerWeek: hours, subjects: subjects.map((id) => ({ id, level: 1 as Level })), importance, examQuestions, contest: "CBMPE_OFICIAL" as const };
  const result = generatePlan(input);
  const planId = await savePlan({ userId: user.id, input, result, diagnostics: {}, foreignLanguage: "EN", hoursBand: "MODERADO", status: "ACTIVE", dbClient: db as never });

  // feitas: mais de 10 dias antes de hoje; as dos 10 dias anteriores ficam atrasadas
  const todayOrd = diffDaysISO(startIso, today);
  const acts = await db.activity.findMany({ where: { planId }, select: { id: true, dayIndex: true, week: { select: { index: true } } } });
  const done = acts.filter((a) => (a.week.index - 1) * 7 + (a.dayIndex ?? 0) < todayOrd - 10).map((a) => a.id);
  for (let i = 0; i < done.length; i += 500) await db.activity.updateMany({ where: { id: { in: done.slice(i, i + 500) } }, data: { status: "DONE", completedAt: new Date() } });
  console.log(`plano ${planId}: início ${startIso}, hoje = dia ${todayOrd}, ${acts.length} atividades, ${done.length} feitas`);

  const option = opt("--opcao") as "SPREAD" | "FILL_GAPS" | "MOVE_TO_DAY" | "DISMISS" | "RECALC_REST" | undefined;
  if (option) {
    const sc = await loadScenario(user.id);
    if (!isScenario(sc)) throw new Error(sc.error);
    const params = {
      option,
      ...(opt("--janela") ? { windowDays: Number(opt("--janela")) as 3 | 7 | 14 } : {}),
      ...(opt("--extra") ? { extraLoadPct: Number(opt("--extra")) as 15 | 25 | 40 } : {}),
      ...(option === "MOVE_TO_DAY" ? { targetDate: addDaysISO(today, 3) } : {}),
    };
    const rq = { activityIds: [...sc.overdueIds], params };
    const c = await compute(sc, rq);
    if ("ok" in c) throw new Error(c.error);
    const p = buildPreview(c, rq);
    console.log(`${option}: ${sc.overdueIds.size} atrasadas → ${p.moves.length} movidas (${p.dependentsMoved} dependentes, ${(p.dependentsShare * 100).toFixed(0)}%), não cabem ${p.doesNotFit.length}${p.noFitLeavesPlan ? " (saem do plano)" : ""}, dispensadas ${p.dismissed.length}, cederam ${p.yielded.length}`);
    for (const w of p.warnings) console.log(`  aviso ${w.code}: ${w.message}`);
    if (p.suggestRecalc) console.log("  sugere RECALC_REST");
    if (args.includes("--aplicar")) console.log("aplicado:", await applyComputed(c, rq));
  }
  await db.$disconnect();
  process.exit(0);
}
main().catch((e) => {
  console.error(String(e instanceof Error ? e.stack : e));
  process.exit(1);
});
