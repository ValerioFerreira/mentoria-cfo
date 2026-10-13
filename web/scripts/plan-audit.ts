// Auditoria do planejador contra as regras do ciclo de estudo, rodando o motor real (catálogo e trechos de /content).
// Uso: npx tsx scripts/plan-audit.ts [--turbo]   (sem flag: cenários normais e Turbo)
import { generatePlan } from "../src/lib/planner";
import { dayIndexOf, diffDays } from "../src/lib/planner/dates";
import { loadCatalog, loadSegments } from "../src/lib/planner/fixtures";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import type { Level, PlanResult } from "../src/lib/planner/types";

const catalog = loadCatalog();
const segments = loadSegments();
const ALL = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
const START = "2026-10-12";
const EXAM = "2027-02-28";
type A = PlanResult["weeks"][number]["activities"][number] & { ord: number };

function audit(hours: number, level: Level, turbo: boolean) {
  const plan = generatePlan({ catalog, segments, startDate: START, examDate: EXAM, hoursPerWeek: hours, subjects: ALL.map((id) => ({ id, level })), turbo });
  const acts: A[] = plan.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, ord: (w.index - 1) * 7 + a.day! })));
  const content = acts.filter((a) => a.scope !== "FINAL");
  const count = (t: string) => content.filter((a) => a.type === t).length;

  // ordem e folgas do ciclo, por aula
  const byAula = new Map<string, A[]>();
  for (const a of content) byAula.set(a.aulaId, [...(byAula.get(a.aulaId) ?? []), a]);
  let qSemRevisao = 0, revNoDiaDaTeoria = 0, qNoDiaDaFixacao = 0, ordemRuim = 0;
  const gapFQ: number[] = [];
  for (const l of byAula.values()) {
    const of = (t: string) => l.filter((a) => a.type === t);
    const T = of("TEORIA"), R = of("REVISAO"), F = of("FIXACAO"), Q = of("QUESTOES");
    const turboAula = T.some((t) => t.turbo);
    if (Q.length && !R.length && !turboAula) qSemRevisao++;
    for (const r of R) for (const k of r.refKeys) if (T.find((t) => t.key === k)?.ord === r.ord) revNoDiaDaTeoria++;
    if (T.length && R.length && Math.min(...R.map((a) => a.ord)) <= Math.min(...T.map((a) => a.ord))) ordemRuim++;
    if (F.length && Q.length) {
      const gap = Math.min(...Q.map((a) => a.ord)) - Math.max(...F.map((a) => a.ord));
      gapFQ.push(gap);
      if (gap <= 0) qNoDiaDaFixacao++;
    }
  }

  // dias
  const perDay = new Map<string, A[]>();
  for (const a of acts) perDay.set(`${a.ord}|${a.subjectId}`, [...(perDay.get(`${a.ord}|${a.subjectId}`) ?? []), a]);
  const over120 = [...perDay.values()].filter((l) => l.reduce((n, a) => n + a.minutes, 0) > 120).length;
  const unica = [...perDay.values()].filter((l) => l.length === 1).length / perDay.size;

  // sequência de dias só de Teoria
  const types = new Map<number, Set<string>>();
  for (const a of content) types.set(a.ord, (types.get(a.ord) ?? new Set()).add(a.type));
  let run = 0, maxRun = 0;
  for (const o of [...types.keys()].sort((x, y) => x - y)) {
    run = types.get(o)!.size === 1 && types.get(o)!.has("TEORIA") ? run + 1 : 0;
    maxRun = Math.max(maxRun, run);
  }

  // reta final
  const examOrd = diffDays(START, EXAM);
  const lastT = [...content].reverse().find((a) => a.type === "TEORIA");
  const eve = acts.filter((a) => a.ord === examOrd - 1);
  const minutes = content.reduce((n, a) => n + a.minutes, 0);
  const practice = content.filter((a) => a.type !== "TEORIA").reduce((n, a) => n + a.minutes, 0);
  const semDisciplina = ALL.filter((id) => !content.some((a) => a.subjectId === id));
  void dayIndexOf;

  return {
    cenario: `${hours}h n${level}${turbo ? " TURBO" : ""}`,
    cob: `${Math.round(plan.coverage.edital * 100)}%`,
    "T/R/F/Q": `${count("TEORIA")}/${count("REVISAO")}/${count("FIXACAO")}/${count("QUESTOES")}`,
    prat: `${Math.round((practice / minutes) * 100)}%`,
    "Q sem R": qSemRevisao,
    "R no dia da T": revNoDiaDaTeoria,
    "Q no dia da F": qNoDiaDaFixacao,
    "ordem ruim": ordemRuim,
    "gap F→Q mediano": gapFQ.length ? [...gapFQ].sort((a, b) => a - b)[Math.floor(gapFQ.length / 2)] : "-",
    ">120min": over120,
    "1 ativ/disc/dia": `${Math.round(unica * 100)}%`,
    "máx dias só T": maxRun,
    "últ. T (dias antes)": lastT ? examOrd - lastT.ord : "-",
    "ativ. em D-1": eve.length,
    "disc. sem nada": semDisciplina.length,
    turboAulas: plan.params.turboAulas,
  };
}

const onlyTurbo = process.argv.includes("--turbo");
const scenarios: [number, Level, boolean][] = [];
for (const [h, l] of [[14, 0], [21, 1], [28, 2], [40, 2], [50, 3]] as [number, Level][]) {
  if (!onlyTurbo) scenarios.push([h, l, false]);
  scenarios.push([h, l, true]);
}
console.table(scenarios.map(([h, l, t]) => audit(h, l, t)));
