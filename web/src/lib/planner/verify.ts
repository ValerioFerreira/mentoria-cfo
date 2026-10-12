// Verificação independente de um planejamento: confere o plano PRONTO (como foi gravado) contra o que o aluno pediu, o catálogo e as
// regras do ciclo de estudo. Não reaproveita o motor: recalcula tudo a partir das atividades, para pegar defeitos do próprio motor.
// Uso: web/scripts/verify-plans.ts (lê os planos do banco) e planner/verify.test.ts.
import { diffDays, dayIndexOf } from "./dates";
import type { Catalog, PlanRequest, PlanResult, SegmentsByAula } from "./types";

export interface VerifyActivity {
  key: string;
  type: "TEORIA" | "REVISAO" | "FIXACAO" | "QUESTOES";
  subjectId: string;
  aulaId: string;
  minutes: number;
  /** semana (1…) e dia (0 = segunda … 6 = domingo) */
  week: number;
  day: number | null;
  scope: "AULA" | "FINAL";
  turbo: boolean;
  segmentIds: string[];
  refKeys: string[];
  quizQuestions?: number | null;
  hasFixRanges?: boolean;
}

export interface VerifyPlan {
  id: string;
  /** segunda-feira da semana 1 */
  startDate: string;
  examDate: string;
  params: Partial<PlanResult["params"]> & { weeklyMinutes?: number; capacityHours?: number };
  coverage?: { selected?: number } | null;
  request: PlanRequest;
  weeks: { index: number; startDate: string; targetMinutes: number }[];
  activities: VerifyActivity[];
}

export interface VerifyContext {
  catalog: Catalog;
  segments: SegmentsByAula;
  /** nota de cada trecho no concurso (null = fora do edital); ausente = sem filtro */
  importance?: Record<string, number | null>;
  /** trechos com resumo analítico disponível; ausente = não confere */
  summaries?: Set<string>;
}

export interface Issue {
  code: string;
  message: string;
  where?: string;
}

export interface VerifyReport {
  verdict: "LIBERAR" | "BLOQUEAR";
  errors: Issue[];
  warnings: Issue[];
  stats: Record<string, number | string>;
}

const BLOCK_KEY = /#S(R|F|Q\d*)?$/; // atividades dos blocos de resumo do Modo Turbo
const MAX_SUBJECT_DAY_MIN = 120;
const WEEK_OVERSHOOT = 1.05;
const MIN_USE_WHEN_MISSING = 0.85; // se faltou aula, o plano deveria ter usado ao menos isto da capacidade
const RANGE: Record<VerifyActivity["type"], [number, number]> = { TEORIA: [15, 80], REVISAO: [25, 60], FIXACAO: [30, 60], QUESTOES: [40, 80] };

const aulaOfSegment = (id: string) => id.split("/").slice(0, 2).join("/");
const subjectOfSegment = (id: string) => id.split("/")[0];

/** Converte um PlanResult do motor no formato verificável (testes e comparação com o motor atual). */
export function planFromResult(result: PlanResult, startDate: string, examDate: string, id = "gerado"): VerifyPlan {
  return {
    id,
    startDate,
    examDate,
    params: result.params,
    coverage: result.coverage,
    request: result.params.request,
    weeks: result.weeks.map((w) => ({ index: w.index, startDate: w.startDate, targetMinutes: w.targetMinutes })),
    activities: result.weeks.flatMap((w) =>
      w.activities.map((a) => ({
        key: a.key, type: a.type, subjectId: a.subjectId, aulaId: a.aulaId, minutes: a.minutes, week: w.index, day: a.day ?? null,
        scope: a.scope ?? "AULA", turbo: !!a.turbo, segmentIds: a.segmentIds, refKeys: a.refKeys, quizQuestions: a.quiz?.questions ?? null,
        hasFixRanges: !!a.fixRanges?.length,
      })),
    ),
  };
}

export function verifyPlan(plan: VerifyPlan, ctx: VerifyContext): VerifyReport {
  const errors: Issue[] = [];
  const warnings: Issue[] = [];
  const err = (code: string, message: string, where?: string) => errors.push({ code, message, where });
  const warn = (code: string, message: string, where?: string) => warnings.push({ code, message, where });
  const req = plan.request;
  const acts = plan.activities;
  const content = acts.filter((a) => a.scope !== "FINAL");
  const ord = (a: VerifyActivity) => (a.week - 1) * 7 + (a.day ?? 0);
  const byKey = new Map(acts.map((a) => [a.key, a]));

  // ───── 1. estrutura e datas ─────
  const weeks = [...plan.weeks].sort((a, b) => a.index - b.index);
  weeks.forEach((w, i) => {
    if (w.index !== i + 1) err("SEMANA_SEQUENCIA", `semana ${w.index} fora de sequência (esperada ${i + 1})`);
    const sum = acts.filter((a) => a.week === w.index).reduce((n, a) => n + a.minutes, 0);
    if (sum !== w.targetMinutes) err("SEMANA_SOMA", `semana ${w.index}: meta ${w.targetMinutes} min ≠ soma das atividades ${sum} min`);
    const weekly = plan.params.weeklyMinutes;
    if (weekly && sum > weekly * WEEK_OVERSHOOT + 1) err("SEMANA_EXCESSO", `semana ${w.index}: ${sum} min passa de 105% da meta semanal (${weekly} min)`);
  });
  for (const a of acts) {
    if (a.day === null || a.day < 0 || a.day > 6) err("DIA_INVALIDO", `atividade sem dia válido (seg–dom)`, a.key);
    if (!weeks.some((w) => w.index === a.week)) err("SEMANA_INEXISTENTE", `atividade em semana inexistente (${a.week})`, a.key);
  }
  const examOrd = diffDays(plan.startDate, plan.examDate);
  const eveOrd = examOrd - 1;
  const lastContentOrd = examOrd - 2;
  const firstOrd = req.firstDay ?? 0;
  for (const a of content) {
    if (ord(a) > lastContentOrd) err("DEPOIS_DE_D2", `conteúdo agendado depois de D-2 (dia ${ord(a) - examOrd} da prova)`, a.key);
    if (ord(a) < firstOrd) err("ANTES_DO_INICIO", `atividade antes do dia de início dos estudos`, a.key);
  }
  for (const a of acts) if (ord(a) > eveOrd) err("DEPOIS_DA_VESPERA", `atividade no dia da prova ou depois`, a.key);
  const eve = acts.filter((a) => ord(a) === eveOrd);
  if (eve.length !== 1 || eve[0].type !== "REVISAO" || eve[0].scope !== "FINAL") err("VESPERA", `a véspera da prova (D-1) deve ter uma única Revisão final (tem ${eve.length} atividade(s))`);
  if (dayIndexOf(plan.examDate) < 0) err("DATA_PROVA", "data da prova inválida");

  // ───── 2. o que o aluno pediu ─────
  const requested = new Set(req.subjects.map((s) => s.id));
  const known = req.known ?? {};
  const excluded = new Set(req.excludedAulas ?? []);
  for (const a of acts) if (!requested.has(a.subjectId)) err("DISCIPLINA_NAO_PEDIDA", `disciplina ${a.subjectId} não foi pedida pelo aluno`, a.key);
  const planned = new Set<string>();
  for (const a of content) {
    planned.add(a.aulaId);
    for (const s of a.segmentIds) planned.add(aulaOfSegment(s));
  }
  let expectedAulas = 0;
  let missingAulas = 0;
  const missingBySubject: string[] = [];
  for (const sel of req.subjects) {
    const subject = ctx.catalog.subjects.find((s) => s.id === sel.id);
    if (!subject) {
      err("DISCIPLINA_DESCONHECIDA", `disciplina ${sel.id} não existe no catálogo`);
      continue;
    }
    const expected = subject.aulas.filter((a) => a.selectable && !excluded.has(a.id) && known[a.id] !== 2 && (ctx.segments[a.id]?.length ?? 0) > 0);
    // com o filtro do edital do concurso, aulas cujos trechos todos estão fora do edital não são esperadas
    const inEdital = expected.filter((a) => !ctx.importance || (ctx.segments[a.id] ?? []).some((s) => ctx.importance![s.id] !== null));
    expectedAulas += inEdital.length;
    const got = inEdital.filter((a) => planned.has(a.id));
    const miss = inEdital.filter((a) => !planned.has(a.id));
    missingAulas += miss.length;
    if (inEdital.length > 0 && got.length === 0) err("DISCIPLINA_SEM_CONTEUDO", `${sel.id}: nenhuma aula entrou no plano (a disciplina não pode ficar de fora)`);
    if (miss.length) missingBySubject.push(`${sel.id} (${miss.length})`);
  }
  for (const a of content) {
    for (const sid of a.segmentIds) {
      const aula = aulaOfSegment(sid);
      if (excluded.has(aula)) err("AULA_EXCLUIDA", `trecho de aula que o aluno desmarcou do edital (${aula})`, a.key);
      if (known[aula] === 2) err("AULA_DOMINADA", `trecho de aula que o aluno disse dominar (${aula})`, a.key);
      if (ctx.importance && ctx.importance[sid] === null) err("FORA_DO_EDITAL", `trecho fora do edital do concurso (${sid})`, a.key);
    }
  }
  const capacityMin = (plan.params.capacityHours ?? 0) * 60;
  const usedMin = content.reduce((n, a) => n + a.minutes, 0);
  const use = capacityMin > 0 ? usedMin / capacityMin : 1;
  if (missingAulas > 0) {
    const msg = `${missingAulas} de ${expectedAulas} aulas pedidas ficaram fora do plano [${missingBySubject.join(", ")}]; plano usa ${(use * 100).toFixed(0)}% da capacidade`;
    if (use < MIN_USE_WHEN_MISSING) err("FALTOU_AULA_SOBROU_TEMPO", `${msg}: sobrou tempo que poderia cobrir mais aulas`);
    else warn("AULAS_FORA_POR_TEMPO", `${msg} (o tempo disponível não comporta mais)`);
  }

  // ───── 3. trechos ─────
  const seenTeoria = new Set<string>();
  for (const a of content) {
    for (const sid of a.segmentIds) {
      const seg = (ctx.segments[aulaOfSegment(sid)] ?? []).find((s) => s.id === sid);
      if (!seg) {
        err("TRECHO_INEXISTENTE", `trecho ${sid} não existe no catálogo`, a.key);
        continue;
      }
      if (subjectOfSegment(sid) !== a.subjectId) err("TRECHO_OUTRA_DISCIPLINA", `trecho ${sid} é de outra disciplina`, a.key);
      const block = a.turbo || BLOCK_KEY.test(a.key);
      if (!block && aulaOfSegment(sid) !== a.aulaId) err("TRECHO_OUTRA_AULA", `trecho ${sid} não é da aula ${a.aulaId}`, a.key);
      if (a.type === "TEORIA") {
        if (seenTeoria.has(sid)) err("TEORIA_DUPLICADA", `trecho ${sid} aparece em mais de uma Teoria`, a.key);
        seenTeoria.add(sid);
      }
    }
    if (a.type === "TEORIA" && !a.turbo) {
      const pages = a.segmentIds.reduce((n, sid) => n + ((ctx.segments[aulaOfSegment(sid)] ?? []).find((s) => s.id === sid)?.pages ?? 0), 0);
      if (pages > 17) err("TEORIA_GRANDE", `Teoria com ${pages} págs. (teto 17)`, a.key);
    }
  }

  // ───── 4. tempos ─────
  for (const a of acts) {
    const [lo, hi] = RANGE[a.type];
    if (a.minutes % 5 !== 0 || a.minutes < lo || a.minutes > hi) err("MINUTOS_FORA_DA_FAIXA", `${a.type} com ${a.minutes} min (faixa ${lo}–${hi}, múltiplos de 5)`, a.key);
    if (a.type === "QUESTOES" && !(a.quizQuestions && a.quizQuestions > 0)) err("CADERNO_SEM_QUESTOES", "atividade de Questões sem caderno configurado", a.key);
    if (a.type === "FIXACAO" && a.hasFixRanges === false) err("FIXACAO_SEM_FAIXA", "Fixação sem faixa de páginas", a.key);
  }
  const perSubjectDay = new Map<string, VerifyActivity[]>();
  for (const a of acts) perSubjectDay.set(`${ord(a)}|${a.subjectId}`, [...(perSubjectDay.get(`${ord(a)}|${a.subjectId}`) ?? []), a]);
  let multi = 0;
  for (const [k, l] of perSubjectDay) {
    const m = l.reduce((n, a) => n + a.minutes, 0);
    if (m > MAX_SUBJECT_DAY_MIN) err("DISCIPLINA_DIA_EXCESSO", `${l[0].subjectId} soma ${m} min no mesmo dia (máx. ${MAX_SUBJECT_DAY_MIN})`, `dia ${k.split("|")[0]}`);
    if (l.length > 1) multi++;
  }
  if (perSubjectDay.size > 0 && multi / perSubjectDay.size > 0.25) warn("MUITAS_ATIVIDADES_NO_DIA", `${Math.round((multi / perSubjectDay.size) * 100)}% dos dias-disciplina têm mais de uma atividade (o ideal é uma)`);

  // ───── 5. referências e ciclo T → R → F → Q ─────
  for (const a of acts) {
    for (const k of a.refKeys) {
      const r = byKey.get(k);
      if (!r) err("REF_INEXISTENTE", `referência a atividade inexistente (${k})`, a.key);
      else {
        if (r.subjectId !== a.subjectId) err("REF_OUTRA_DISCIPLINA", `referência a atividade de outra disciplina (${k})`, a.key);
        if (ord(r) > ord(a)) err("REF_DEPOIS", `atividade vem antes daquilo a que se atrela (${k})`, a.key);
        else if (a.type === "REVISAO" && a.scope === "AULA" && ord(a) - ord(r) < 1) err("REVISAO_NO_DIA_DA_TEORIA", `Revisão no mesmo dia (ou antes) da Teoria que revê (${k})`, a.key);
      }
    }
  }
  const isBlock = (a: VerifyActivity) => a.turbo || BLOCK_KEY.test(a.key);
  const quizzes = content.filter((a) => a.type === "QUESTOES");
  for (const t of content.filter((a) => a.type === "TEORIA")) {
    const q = quizzes.find((x) => x.refKeys.includes(t.key));
    if (!q) err("TEORIA_SEM_CADERNO", "Teoria sem caderno de Questões que feche o ciclo", t.key);
    else if (ord(q) - ord(t) < 1) err("CADERNO_NO_DIA_DA_TEORIA", "caderno no mesmo dia da Teoria", q.key);
  }
  const byAula = new Map<string, VerifyActivity[]>();
  for (const a of content.filter((x) => !isBlock(x))) byAula.set(a.aulaId, [...(byAula.get(a.aulaId) ?? []), a]);
  for (const [aula, l] of byAula) {
    const T = l.filter((a) => a.type === "TEORIA");
    const R = l.filter((a) => a.type === "REVISAO");
    const F = l.filter((a) => a.type === "FIXACAO");
    const Q = l.filter((a) => a.type === "QUESTOES");
    const lastT = T.length ? Math.max(...T.map(ord)) : -1;
    for (const x of [...R, ...F, ...Q]) if (T.length && ord(x) <= Math.min(...T.map(ord))) err("CICLO_ANTES_DA_TEORIA", `${x.type} antes/no dia da Teoria na aula ${aula}`, x.key);
    if (Q.length && T.length && !R.length) err("QUESTOES_SEM_REVISAO", `aula ${aula}: Questões sem Revisão antes`);
    if (F.length) {
      if (T.length && Math.min(...F.map(ord)) <= lastT) err("FIXACAO_ANTES_DA_TEORIA", `aula ${aula}: Fixação antes de terminar a Teoria`);
      for (const r of R) if (Math.min(...F.map(ord)) - ord(r) < 1) err("FIXACAO_SEM_FOLGA", `aula ${aula}: Fixação sem 1 dia de folga depois da Revisão`, r.key);
    }
    for (const q of Q) {
      if (F.length && ord(q) - Math.max(...F.map(ord)) < 1) err("QUESTOES_SEM_FOLGA_FIXACAO", `aula ${aula}: Questões sem 1 dia de folga depois da Fixação`, q.key);
      if (!F.length && R.length && ord(q) - Math.max(...R.map(ord)) < 1) err("QUESTOES_SEM_FOLGA_REVISAO", `aula ${aula}: Questões sem 1 dia de folga depois da Revisão`, q.key);
    }
  }
  // blocos de resumo (Modo Turbo): resumos → Revisão (metade) → Fixação reduzida → Questões
  const blocks = new Map<string, VerifyActivity[]>();
  for (const a of content.filter(isBlock)) blocks.set(a.key.split("#S")[0] || a.key, [...(blocks.get(a.key.split("#S")[0] || a.key) ?? []), a]);
  for (const [tag, l] of blocks) {
    for (const s of l.filter((a) => a.type === "TEORIA")) if (s.segmentIds.length > 6) err("RESUMO_GRANDE", `atividade de resumo com ${s.segmentIds.length} trechos (máx. 3 unidades)`, s.key);
    const S = l.filter((a) => a.type === "TEORIA");
    const R = l.filter((a) => a.type === "REVISAO");
    const F = l.filter((a) => a.type === "FIXACAO");
    const Q = l.filter((a) => a.type === "QUESTOES");
    const lastS = S.length ? Math.max(...S.map(ord)) : -1;
    for (const r of R) if (ord(r) - lastS < 0) err("BLOCO_REVISAO_ANTES", `bloco ${tag}: Revisão antes dos resumos`, r.key);
    for (const q of Q) {
      const before = [...R, ...F];
      if (before.length && ord(q) - Math.max(...before.map(ord)) < 1) err("BLOCO_QUESTOES_SEM_FOLGA", `bloco ${tag}: Questões sem 1 dia de folga depois da Revisão/Fixação`, q.key);
      if (ord(q) - lastS < 1 && S.length) err("BLOCO_QUESTOES_NO_DIA", `bloco ${tag}: Questões no dia do último resumo`, q.key);
    }
  }

  // ───── 6. Modo Turbo ─────
  const turboActs = acts.filter((a) => a.turbo);
  if (!req.turbo && turboActs.length) err("TURBO_NAO_PEDIDO", `${turboActs.length} atividades de resumo, mas o aluno não pediu o Modo Turbo`);
  if (ctx.summaries) for (const a of turboActs) for (const sid of a.segmentIds) if (!ctx.summaries.has(sid)) err("RESUMO_INEXISTENTE", `atividade de resumo usa trecho sem resumo analítico (${sid})`, a.key);
  if (req.turbo && !turboActs.length) warn("TURBO_SEM_TROCAS", "Modo Turbo pedido, mas nenhum assunto foi trocado por resumo (o edital cabia ou faltam resumos)");

  const cov = plan.coverage?.selected;
  if (typeof cov === "number" && (cov < 0 || cov > 1 + 1e-9)) err("COBERTURA_INVALIDA", `cobertura gravada fora de 0–100% (${cov})`);

  const stats: Record<string, number | string> = {
    atividades: acts.length,
    teoria: acts.filter((a) => a.type === "TEORIA").length,
    resumos: turboActs.length,
    revisao: acts.filter((a) => a.type === "REVISAO").length,
    fixacao: acts.filter((a) => a.type === "FIXACAO").length,
    questoes: acts.filter((a) => a.type === "QUESTOES").length,
    horasConteudo: Math.round(usedMin / 60),
    usoDaCapacidade: `${(use * 100).toFixed(0)}%`,
    aulasPedidas: expectedAulas,
    aulasForaDoPlano: missingAulas,
    cobertura: typeof cov === "number" ? `${(cov * 100).toFixed(1)}%` : "?",
  };
  return { verdict: errors.length ? "BLOQUEAR" : "LIBERAR", errors, warnings, stats };
}
