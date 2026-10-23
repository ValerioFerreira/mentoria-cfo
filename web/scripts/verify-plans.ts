// Verificação diária dos planejamentos: lê as solicitações de plano (por padrão, as em análise = PENDING_ANALYSIS), confere cada uma,
// uma a uma, contra o que o aluno pediu e contra as regras do ciclo Teoria → Revisão → Fixação → Questões, e gera um relatório com o
// veredito LIBERAR / BLOQUEAR e os motivos. SOMENTE LEITURA, a menos que --apply seja informado.
//
//   npx tsx scripts/verify-plans.ts                       # banco local (web/.env), planos em análise
//   npx tsx scripts/verify-plans.ts --remoto              # produção (web/.env.remote: REMOTE_DATABASE_URL), somente leitura
//   npx tsx scripts/verify-plans.ts --remoto --apply      # ativa só os aprovados e grava o relatório de cada plano em params.check
//   opções: --status PENDING_ANALYSIS|ACTIVE|ALL   --plan <id>   --out <pasta> (padrão: web/reports)
//
// Plano com erro NÃO é ativado (continua em análise, bloqueado) e o motivo vai no relatório (e em params.check com --apply).
import "dotenv/config";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, type Contest } from "../src/generated/prisma/client";
import { comboWeights, isCombo, mergeComboImportance } from "../src/lib/combos";
import { dayIndexOf, diffDays } from "../src/lib/planner/dates";
import { loadCatalog, loadSegments } from "../src/lib/planner/fixtures";
import type { Known, Level, PlanRequest } from "../src/lib/planner/types";
import { verifyPlan, type VerifyActivity, type VerifyPlan } from "../src/lib/planner/verify";

const args = process.argv.slice(2);
const flag = (n: string) => args.includes(n);
const opt = (n: string, d?: string) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);

function dbUrl(): string {
  if (!flag("--remoto")) return process.env.DATABASE_URL || "";
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: dbUrl().replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : "")) }) });

const ymd = (d: Date) => d.toISOString().slice(0, 10);

async function main() {
  const status = opt("--status", "PENDING_ANALYSIS")!;
  const planId = opt("--plan");
  const where = planId ? { id: planId } : status === "ALL" ? { status: { in: ["PENDING_ANALYSIS", "ACTIVE"] as ("PENDING_ANALYSIS" | "ACTIVE")[] } } : { status: status as "PENDING_ANALYSIS" | "ACTIVE" };
  const plans = await db.plan.findMany({
    where,
    orderBy: { createdAt: "asc" },
    include: {
      user: { select: { email: true, name: true } },
      subjects: true,
      weeks: { select: { id: true, index: true, startDate: true, targetMinutes: true } },
    },
  });
  const allActivities = await db.activity.findMany({
    where: { planId: { in: plans.map((p) => p.id) } },
    include: { segments: { select: { segmentId: true } }, refs: { include: { refActivity: { select: { key: true } } } } },
  });
  const activitiesByPlan = Map.groupBy(allActivities, (a) => a.planId);
  const catalog = loadCatalog();
  const segments = loadSegments();
  const summaries = new Set((await db.analyticSummary.findMany({ select: { segmentId: true } })).map((s) => s.segmentId));
  const importanceBy = new Map<string, Record<string, number | null>>();
  const importanceOf = async (c: Contest, priority?: string) => {
    const key = `${c}|${priority ?? ""}`;
    if (!importanceBy.has(key)) {
      if (isCombo(c)) {
        // combo: união dos editais dos dois concursos-membro, como no assistente
        const weights = comboWeights(c, priority ?? "");
        const rows = await db.segmentImportance.findMany({ where: { contest: { in: weights.map((w) => w.contest) } }, select: { segmentId: true, contest: true, appears: true, score: true, expected: true } });
        const members = weights.map(({ contest, weight }) => {
          const mine = rows.filter((r) => r.contest === contest);
          return { weight, importance: Object.fromEntries(mine.map((r) => [r.segmentId, r.appears ? r.score : null])), expected: Object.fromEntries(mine.map((r) => [r.segmentId, r.expected])) };
        });
        importanceBy.set(key, mergeComboImportance(members));
      } else {
        const rows = await db.segmentImportance.findMany({ where: { contest: c }, select: { segmentId: true, appears: true, score: true } });
        importanceBy.set(key, Object.fromEntries(rows.map((r) => [r.segmentId, r.appears ? r.score : null])));
      }
    }
    const m = importanceBy.get(key)!;
    return Object.keys(m).length ? m : undefined; // banco sem notas: não filtra
  };

  const lines: string[] = [];
  const results: { id: string; email: string; verdict: string; errors: number; warnings: number }[] = [];
  let released = 0;
  for (const p of plans) {
    const contest = (p.contest ?? "CBMPE_OFICIAL") as Contest;
    const params = (p.params as Record<string, unknown>) ?? {};
    const startDate = ymd(p.startDate);
    const saved = params.request as PlanRequest | undefined;
    const firstStudy = typeof params.firstStudyDate === "string" ? diffDays(startDate, params.firstStudyDate) : 0;
    const known: Record<string, Known> = {};
    for (const s of p.subjects) {
      const aulas = ((s.diagnostic as Record<string, unknown>)?.aulas ?? {}) as Record<string, number>;
      for (const [id, v] of Object.entries(aulas)) if (v === 1 || v === 2) known[id] = v as Known;
    }
    const rebuilt = !saved;
    const request: PlanRequest =
      saved ?? {
        hoursPerWeek: Number(params.hoursPerWeek ?? 0),
        turbo: Boolean(params.turbo ?? Number(params.turboAulas ?? 0) > 0),
        firstDay: firstStudy,
        contest,
        subjects: p.subjects.map((s) => ({ id: s.subjectId, level: (s.level ?? 1) as Level })),
        known,
        excludedAulas: [],
      };
    const weekIndex = new Map(p.weeks.map((w) => [w.id, w.index]));
    const activities: VerifyActivity[] = (activitiesByPlan.get(p.id) ?? []).map((a) => ({
      key: a.key,
      type: a.type,
      subjectId: a.subjectId,
      aulaId: a.aulaId,
      minutes: a.plannedMinutes,
      week: weekIndex.get(a.weekId) ?? 0,
      day: a.dayIndex,
      scope: a.scope,
      turbo: a.turbo,
      segmentIds: a.segments.map((s) => s.segmentId),
      refKeys: a.refs.map((r) => r.refActivity.key),
      quizQuestions: a.quizQuestions,
      hasFixRanges: Array.isArray(a.fixRanges) ? a.fixRanges.length > 0 : a.fixRanges != null,
    }));
    const vp: VerifyPlan = {
      id: p.id,
      startDate,
      examDate: ymd(p.examDate),
      params: params as VerifyPlan["params"],
      coverage: p.coverage as VerifyPlan["coverage"],
      request,
      contest: p.contest,
      weeks: p.weeks.map((w) => ({ index: w.index, startDate: ymd(w.startDate), targetMinutes: w.targetMinutes })),
      activities,
    };
    const report = verifyPlan(vp, { catalog, segments, importance: await importanceOf(contest, request.combo?.priority), summaries });
    if (rebuilt) report.warnings.unshift({ code: "SOLICITACAO_RECONSTRUIDA", message: "plano antigo, sem a solicitação original gravada: pedido reconstruído a partir das disciplinas, níveis e anamnese (assuntos desmarcados não são conhecidos)" });

    results.push({ id: p.id, email: p.user.email, verdict: report.verdict, errors: report.errors.length, warnings: report.warnings.length });
    lines.push(`## ${report.verdict === "LIBERAR" ? "✅ LIBERAR" : "⛔ BLOQUEAR"} — ${p.user.name ?? p.user.email} <${p.user.email}>`);
    lines.push(`Plano \`${p.id}\` · v${p.version} · ${p.status} · ${contest} · criado em ${ymd(p.createdAt)} · prova ${ymd(p.examDate)} (${diffDays(startDate, ymd(p.examDate)) } dias após o início; dia da semana ${dayIndexOf(ymd(p.examDate))})`);
    lines.push(`Pedido: ${request.hoursPerWeek} h/semana · ${request.subjects.length} disciplinas · Turbo ${request.turbo ? "sim" : "não"} · aulas marcadas ${Object.keys(request.known ?? {}).length} · aulas excluídas ${(request.excludedAulas ?? []).length}`);
    lines.push(`Números: ${Object.entries(report.stats).map(([k, v]) => `${k}=${v}`).join(" · ")}`);
    if (report.errors.length) {
      lines.push("", "**Erros (bloqueiam o plano):**");
      const grouped = new Map<string, string[]>();
      for (const e of report.errors) grouped.set(e.code, [...(grouped.get(e.code) ?? []), `${e.message}${e.where ? ` [${e.where}]` : ""}`]);
      for (const [code, msgs] of grouped) lines.push(`- \`${code}\` ×${msgs.length}: ${msgs[0]}${msgs.length > 1 ? ` (+${msgs.length - 1} ocorrências)` : ""}`);
    }
    if (report.warnings.length) {
      lines.push("", "Avisos:");
      for (const w of report.warnings) lines.push(`- \`${w.code}\`: ${w.message}`);
    }
    lines.push("");

    if (flag("--apply")) {
      const check = { checkedAt: new Date().toISOString(), verdict: report.verdict, errors: report.errors.slice(0, 30), warnings: report.warnings.slice(0, 30), stats: report.stats };
      const activate = report.verdict === "LIBERAR" && p.status === "PENDING_ANALYSIS";
      await db.plan.update({ where: { id: p.id }, data: { params: { ...params, check } as object, ...(activate ? { status: "ACTIVE" as const } : {}) } });
      if (activate) released++;
    }
  }

  const total = results.length;
  const ok = results.filter((r) => r.verdict === "LIBERAR").length;
  const head = [
    `# Verificação de planejamentos — ${new Date().toLocaleString("pt-BR", { timeZone: "America/Recife" })}`,
    `Banco: ${flag("--remoto") ? "PRODUÇÃO (remoto)" : "local"} · filtro: ${planId ?? status} · modo: ${flag("--apply") ? "APLICAR (ativa os aprovados)" : "somente leitura"}`,
    `**${total} plano(s): ${ok} para liberar, ${total - ok} bloqueado(s).**${flag("--apply") ? ` Ativados agora: ${released}.` : ""}`,
    "",
    "| Plano | Aluno | Veredito | Erros | Avisos |",
    "| --- | --- | --- | --- | --- |",
    ...results.map((r) => `| \`${r.id}\` | ${r.email} | ${r.verdict} | ${r.errors} | ${r.warnings} |`),
    "",
  ];
  const out = [...head, ...lines].join("\n");
  const dir = resolve(opt("--out", resolve(__dirname, "..", "reports"))!);
  mkdirSync(dir, { recursive: true });
  const file = resolve(dir, `verificacao-${new Date().toISOString().slice(0, 10)}${flag("--remoto") ? "-remoto" : ""}.md`);
  writeFileSync(file, out, "utf8");
  console.log(out);
  console.log(`\nRelatório salvo em ${file}`);
  process.exitCode = total - ok > 0 ? 2 : 0; // código 2 = há plano bloqueado (útil para automação)
}

main().finally(() => db.$disconnect());
