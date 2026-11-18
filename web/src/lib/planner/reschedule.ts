// Reprogramação de atividades atrasadas (motor puro, sem banco nem datas: trabalha em "dias do plano", ord = (semana − 1) × 7 + dia).
//
// O aluno escolhe atividades atrasadas e uma opção (ver reschedule-types.ts); o motor devolve onde cada uma cai e, SEMPRE, reorganiza
// as atividades seguintes que dependem das movidas (Teoria → Revisão → Fixação → Questões, com a folga de CYCLE_GAP_DAYS), pelas
// mesmas regras do agendador (days.ts): ≤ 120 min por disciplina/dia, carga do dia limitada pela meta (mais a folga que a opção
// permite) e nada depois de D-2. Os minutos das atividades NUNCA mudam. D-1 (revisão da véspera) fica intacto.
//
// Os pré-requisitos não são gravados no banco: `depsFromKeys` os reconstrói a partir do formato do `key` (schedule.ts: #T, #R, #F, #Q
// e os blocos do Turbo #S, #SR, #SF, #SQ) e das referências (`refKeys`) das Revisões e dos cadernos.
import { CYCLE_GAP_DAYS, FAMILY, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import { dayTarget, orderDay, scheduleCalendar, type CalendarStream } from "./days";
import type { CycleActivity } from "./schedule";
import type { RescheduleParams, RescheduleWarningCode } from "./reschedule-types";

export type EngineType = "TEORIA" | "REVISAO" | "FIXACAO" | "QUESTOES";
export type EngineStatus = "PENDING" | "IN_PROGRESS" | "DONE" | "SKIPPED";

export interface EngineActivity {
  id: string;
  key: string;
  type: EngineType;
  subjectId: string;
  aulaId: string;
  minutes: number;
  /** dia do plano: (semana − 1) × 7 + dia (0 = segunda da semana 1) */
  ord: number;
  /** posição dentro do dia (Activity.sortOrder) */
  sortOrder: number;
  status: EngineStatus;
  scope: "AULA" | "FINAL";
  turbo: boolean;
  /** chaves das Teorias/resumos a que a Revisão ou o caderno se atrela (Activity.refs) */
  refKeys: string[];
}

export interface EngineInput {
  activities: EngineActivity[];
  weeklyMinutes: number;
  todayOrd: number;
  /** primeiro dia de estudo do plano */
  firstOrd: number;
  /** último dia com conteúdo (D-2) */
  lastContentOrd: number;
  /** véspera da prova (D-1): fica intacta */
  eveOrd: number;
  selectedIds: string[];
  params: RescheduleParams;
  /** MOVE_TO_DAY: dia de destino, já em ord */
  targetOrd?: number;
  /** importância média por aula (0–100): em RECALC_REST, o que não cabe sai pelas de menor nota */
  importanceByAula?: Record<string, number>;
}

export interface EnginePlacement {
  id: string;
  fromOrd: number;
  toOrd: number;
  reason: "SELECTED" | "DEPENDENT";
  /** DEPENDENT: atividade movida de que esta depende (a que mais a empurrou) */
  causedById?: string;
}

export interface EngineWarning {
  code: RescheduleWarningCode;
  ord?: number;
  count?: number;
  minutes?: number;
  subjectId?: string;
}

export interface EngineDayLoad {
  ord: number;
  before: number;
  after: number;
  target: number;
}

export interface EngineResult {
  placements: EnginePlacement[];
  /** selecionadas dispensadas (DISMISS): vão para SKIPPED */
  dismissed: string[];
  /** revisões gerais de sobra que cederam o lugar (vão para SKIPPED) */
  yielded: string[];
  /** não cabem até D-2: ficam onde estão (opções comuns) ou saem do plano, vão para SKIPPED (RECALC_REST, ver `leavePlan`) */
  doesNotFit: string[];
  /** true em RECALC_REST: a lista "não cabe" sai do plano ao confirmar (a prévia a mostra antes) */
  noFitLeavesPlan: boolean;
  /** atividades de cada dia que mudou, na ordem em que serão feitas */
  order: Map<number, string[]>;
  dayLoads: EngineDayLoad[];
  warnings: EngineWarning[];
  /** pendentes (fora as selecionadas) que a cascata deslocou */
  dependentsMoved: number;
  /** total de pendentes do plano (base da fração acima) */
  pendingCount: number;
}

const TYPE_RANK: Record<EngineType, number> = { TEORIA: 0, REVISAO: 1, FIXACAO: 2, QUESTOES: 3 };
const KEY = /^(.*)#(T|R|F|Q)(\d+)$/;
const BLOCK_KEY = /#S(R|F|Q\d*)?$/;
const EPS = 1e-6;
/** quantos dias à frente aceita-se esperar por um dia sem outra atividade da mesma disciplina */
const SAME_SUBJECT_PATIENCE = 3;

const isPending = (a: { status: EngineStatus }) => a.status === "PENDING" || a.status === "IN_PROGRESS";
const isBlock = (a: Pick<EngineActivity, "key" | "turbo">) => a.turbo || BLOCK_KEY.test(a.key);
const blockPrefix = (key: string) => key.replace(/#S(R|F|Q\d*)?$/, "");
const byNaturalKey = (a: string, b: string) => a.localeCompare(b, undefined, { numeric: true });

/** Ordem topológica do plano original: por dia, depois T → R → F → Q, depois pela chave. */
const topo = (a: EngineActivity, b: EngineActivity) => a.ord - b.ord || TYPE_RANK[a.type] - TYPE_RANK[b.type] || byNaturalKey(a.key, b.key);

export interface EngineDep {
  id: string;
  /** dias de folga: a atividade só pode cair em ord(dep) + gap ou depois */
  gap: number;
}

/**
 * Pré-requisitos de cada atividade, pelas mesmas regras do agendador (schedule.ts):
 *  - Teoria n depende da Teoria n−1 (folga 0);
 *  - Revisão depende das Teorias que revê (`refKeys`; sem elas, das Teorias da aula até o dia dela), folga de CYCLE_GAP_DAYS;
 *  - Fixação depende de toda a Revisão da aula (ou da Teoria, se não há Revisão), folga CYCLE_GAP_DAYS; Fixação k de Fixação k−1 (folga 0);
 *  - Questões dependem da Fixação (ou da Revisão, ou da Teoria), folga CYCLE_GAP_DAYS; caderno k do caderno k−1 (folga 0);
 *  - blocos do Turbo: resumo (#S) → Revisão (#SR) → Fixação (#SF) → caderno (#SQn), mesma folga;
 *  - revisões gerais e cadernos mistos (scope FINAL) não dependem de nada.
 */
export function depsFromKeys(acts: EngineActivity[]): Map<string, EngineDep[]> {
  const deps = new Map<string, EngineDep[]>();
  const add = (a: EngineActivity, dep: EngineActivity | undefined, gap: number) => {
    if (!dep || dep.id === a.id) return;
    const list = deps.get(a.id) ?? [];
    if (!list.some((d) => d.id === dep.id)) list.push({ id: dep.id, gap });
    deps.set(a.id, list);
  };
  const byKey = new Map(acts.map((a) => [a.key, a]));
  const resolve = (keys: string[]) => keys.map((k) => byKey.get(k)).filter((x): x is EngineActivity => !!x);

  const groups = new Map<string, EngineActivity[]>();
  for (const a of acts) {
    if (a.scope !== "AULA" || isBlock(a)) continue;
    groups.set(a.aulaId, [...(groups.get(a.aulaId) ?? []), a]);
  }
  for (const list of groups.values()) {
    const of = (t: EngineType) => list.filter((a) => a.type === t).sort((x, y) => byNaturalKey(x.key, y.key));
    const T = of("TEORIA");
    const R = of("REVISAO");
    const F = of("FIXACAO");
    for (const a of list) {
      const m = KEY.exec(a.key);
      const n = m ? Number(m[3]) : 1;
      if (a.type === "TEORIA" && m && n > 1) add(a, byKey.get(`${m[1]}#T${n - 1}`), 0);
      else if (a.type === "REVISAO") {
        const refs = resolve(a.refKeys);
        for (const t of refs.length ? refs : T.filter((t) => t.ord <= a.ord)) add(a, t, CYCLE_GAP_DAYS);
      } else if (a.type === "FIXACAO") {
        for (const x of R.length ? R : T) add(a, x, CYCLE_GAP_DAYS);
        if (m && n > 1) add(a, byKey.get(`${m[1]}#F${n - 1}`), 0);
      } else if (a.type === "QUESTOES") {
        for (const x of F.length ? F : R.length ? R : T) add(a, x, CYCLE_GAP_DAYS);
        if (m && n > 1) add(a, byKey.get(`${m[1]}#Q${n - 1}`), 0);
      }
    }
  }
  // blocos de resumo do Turbo
  const blocks = acts.filter((a) => a.scope === "AULA" && isBlock(a));
  for (const a of blocks) {
    if (a.type === "TEORIA") continue;
    const prefix = blockPrefix(a.key);
    const same = (t: EngineType, suffix: RegExp) => blocks.filter((b) => b.type === t && blockPrefix(b.key) === prefix && suffix.test(b.key));
    if (a.type === "REVISAO") for (const s of resolve(a.refKeys)) add(a, s, CYCLE_GAP_DAYS);
    else if (a.type === "FIXACAO") {
      const rs = same("REVISAO", /#SR$/);
      for (const r of rs.length ? rs : resolve(a.refKeys)) add(a, r, CYCLE_GAP_DAYS);
    } else if (a.type === "QUESTOES") {
      for (const s of resolve(a.refKeys)) add(a, s, CYCLE_GAP_DAYS);
      for (const x of [...same("FIXACAO", /#SF$/), ...same("REVISAO", /#SR$/)]) add(a, x, CYCLE_GAP_DAYS);
      const m = /#SQ(\d+)$/.exec(a.key);
      if (m && Number(m[1]) > 1) add(a, byKey.get(`${prefix}#SQ${Number(m[1]) - 1}`), 0);
    }
  }
  return deps;
}

/**
 * Calcula a reprogramação. Não grava nada; devolve os movimentos para a prévia e para a gravação (reschedule-actions.ts).
 * As opções SPREAD, FILL_GAPS e MOVE_TO_DAY colocam as selecionadas e depois reorganizam as dependentes; DISMISS libera as
 * dependentes; RECALC_REST roda o agendador de novo sobre todas as pendentes, de hoje até D-2.
 */
export function planReschedule(input: EngineInput): EngineResult {
  const { weeklyMinutes: W, lastContentOrd: LAST } = input;
  const acts = new Map(input.activities.map((a) => [a.id, a]));
  const deps = depsFromKeys(input.activities);
  const cur = new Map(input.activities.map((a) => [a.id, a.ord]));
  const original = new Map(cur);
  const option = input.params.option;

  const selected = input.selectedIds
    .map((id) => acts.get(id))
    .filter((a): a is EngineActivity => !!a && isPending(a) && a.scope === "AULA")
    .sort(topo);
  const selectedSet = new Set(selected.map((a) => a.id));
  const dismissed = new Set<string>();
  const yielded = new Set<string>();
  const noFit = new Set<string>();
  const placements = new Map<string, EnginePlacement>();

  // ───── carga por dia e por disciplina/dia (tudo o que está no plano e não foi dispensado) ─────
  const load = new Map<number, number>();
  const subj = new Map<string, number>();
  const bump = (a: EngineActivity, ord: number, sign: 1 | -1) => {
    load.set(ord, (load.get(ord) ?? 0) + sign * a.minutes);
    const k = `${ord}|${a.subjectId}`;
    subj.set(k, (subj.get(k) ?? 0) + sign * a.minutes);
  };
  for (const a of input.activities) if (a.status !== "SKIPPED") bump(a, a.ord, 1);
  const loadBefore = new Map(load);

  const dropFromDay = (a: EngineActivity) => bump(a, cur.get(a.id)!, -1);
  const put = (a: EngineActivity, ord: number) => {
    cur.set(a.id, ord);
    bump(a, ord, 1);
  };

  const lbOf = (a: EngineActivity): number => {
    let lb = input.firstOrd;
    for (const d of deps.get(a.id) ?? []) {
      const dep = acts.get(d.id)!;
      if (dismissed.has(d.id) || dep.status === "SKIPPED") continue;
      if (noFit.has(d.id)) return Infinity;
      const o = cur.get(d.id)!;
      lb = Math.max(lb, (dep.status === "DONE" ? Math.min(o, input.todayOrd) : o) + d.gap);
    }
    return lb;
  };

  /** Primeiro dia viável (ou o de maior folga relativa) entre `from` e `to`; null se nenhum. */
  const findDay = (a: EngineActivity, from: number, to: number, factor: number, pref: "earliest" | "slack"): number | null => {
    let firstViable: number | null = null;
    let best: number | null = null;
    let bestSlack = -Infinity;
    for (let d = Math.max(from, input.firstOrd); d <= Math.min(to, LAST); d++) {
      const t = dayTarget(W, d);
      const l = load.get(d) ?? 0;
      if (l + a.minutes > t * factor + EPS) continue;
      const sm = subj.get(`${d}|${a.subjectId}`) ?? 0;
      if (sm + a.minutes > MAX_SAME_SUBJECT_MINUTES_PER_DAY) continue;
      if (pref === "earliest") {
        if (sm === 0) return d;
        firstViable ??= d;
        if (d - firstViable >= SAME_SUBJECT_PATIENCE) return firstViable;
        continue;
      }
      const slack = (t - l) / t - (sm > 0 ? 0.05 : 0); // de preferência uma atividade por disciplina/dia
      if (slack > bestSlack + 1e-9) {
        best = d;
        bestSlack = slack;
      }
    }
    return pref === "earliest" ? firstViable : best;
  };

  const spareFinals = () => input.activities.filter((a) => a.scope === "FINAL" && a.ord !== input.eveOrd && isPending(a) && !yielded.has(a.id));
  /** FILL_GAPS: se nenhum dia tem folga, uma revisão geral de sobra cede o lugar. */
  const findDayYielding = (a: EngineActivity, from: number): { day: number; give: EngineActivity } | null => {
    for (let d = Math.max(from, input.firstOrd); d <= LAST; d++) {
      for (const f of spareFinals().filter((x) => cur.get(x.id) === d)) {
        const l = (load.get(d) ?? 0) - f.minutes;
        const sm = (subj.get(`${d}|${a.subjectId}`) ?? 0) - (f.subjectId === a.subjectId ? f.minutes : 0);
        if (l + a.minutes <= dayTarget(W, d) + EPS && sm + a.minutes <= MAX_SAME_SUBJECT_MINUTES_PER_DAY) return { day: d, give: f };
      }
    }
    return null;
  };

  /**
   * Uma atividade que não coube fica onde estava; então toda atividade da cadeia que vem ANTES dela e que esta reprogramação
   * empurrou para a frente volta ao lugar original (senão a Revisão ficaria no passado e a Teoria no futuro). Vale também
   * para as ancestrais das ancestrais: a cadeia T → R → F → Q é "tudo ou nada" a partir do ponto que não coube.
   */
  const revertAncestors = (a: EngineActivity) => {
    const seen = new Set<string>();
    const walk = (id: string) => {
      for (const d of deps.get(id) ?? []) {
        if (seen.has(d.id)) continue;
        seen.add(d.id);
        const dep = acts.get(d.id)!;
        if (placements.has(d.id)) {
          bump(dep, cur.get(d.id)!, -1);
          bump(dep, original.get(d.id)!, 1);
          cur.set(d.id, original.get(d.id)!);
          placements.delete(d.id);
          noFit.add(d.id);
        }
        walk(d.id);
      }
    };
    walk(a.id);
  };

  const record = (a: EngineActivity, to: number, reason: EnginePlacement["reason"], causedById?: string) => {
    const from = original.get(a.id)!;
    if (to === from) placements.delete(a.id);
    else placements.set(a.id, { id: a.id, fromOrd: from, toOrd: to, reason, ...(causedById ? { causedById } : {}) });
  };

  const startOrd = (() => {
    const t = Math.max(input.todayOrd, input.firstOrd);
    return (load.get(t) ?? 0) - selected.filter((a) => cur.get(a.id) === t).reduce((n, a) => n + a.minutes, 0) < dayTarget(W, t) ? t : t + 1;
  })();

  if (option === "RECALC_REST") return recalc();

  // ───── Passo 1: colocar as selecionadas ─────
  for (const a of selected) dropFromDay(a);
  if (option === "DISMISS") {
    for (const a of selected) dismissed.add(a.id);
  } else {
    const extra = (input.params.extraLoadPct ?? 25) / 100;
    const window = input.params.windowDays ?? 7;
    for (const a of selected) {
      const lb = lbOf(a);
      let day: number | null = null;
      if (lb !== Infinity) {
        if (option === "SPREAD") {
          day = findDay(a, Math.max(lb, startOrd), startOrd + window - 1, 1 + extra, "slack");
          day ??= findDay(a, Math.max(lb, startOrd + window), LAST, 1 + extra, "earliest"); // o que não coube na janela
        } else if (option === "FILL_GAPS") {
          day = findDay(a, Math.max(lb, startOrd), LAST, 1, "earliest");
          if (day === null) {
            const y = findDayYielding(a, Math.max(lb, startOrd));
            if (y) {
              dropFromDay(y.give);
              yielded.add(y.give.id);
              day = y.day;
            }
          }
        } else if (option === "MOVE_TO_DAY") {
          const t = Math.max(input.targetOrd ?? startOrd, lb, input.firstOrd);
          day = t <= LAST ? t : null; // o destino é escolha do aluno: a prévia avisa se estourar a carga
        }
      }
      if (day === null) {
        noFit.add(a.id);
        put(a, original.get(a.id)!); // fica onde estava
        revertAncestors(a);
        continue;
      }
      put(a, day);
      record(a, day, "SELECTED");
    }
  }

  // ───── Passo 2: reorganizar as dependentes (T → R → F → Q), em ordem topológica ─────
  if (option !== "DISMISS") {
    const factor = option === "SPREAD" ? 1 + (input.params.extraLoadPct ?? 25) / 100 : option === "MOVE_TO_DAY" ? 1.25 : 1;
    const movedIds = () => new Set(placements.keys());
    for (const b of input.activities.filter((x) => isPending(x) && x.scope === "AULA" && !selectedSet.has(x.id)).sort(topo)) {
      const lb = lbOf(b);
      const here = cur.get(b.id)!;
      if (lb !== Infinity && here >= lb) continue;
      const cause = (deps.get(b.id) ?? [])
        .filter((d) => movedIds().has(d.id) || noFit.has(d.id))
        .sort((x, y) => (cur.get(y.id)! + y.gap) - (cur.get(x.id)! + x.gap))[0];
      dropFromDay(b);
      const day = lb === Infinity ? null : findDay(b, Math.max(lb, input.todayOrd), LAST, factor, "earliest");
      if (day === null) {
        noFit.add(b.id);
        put(b, here);
        revertAncestors(b);
        continue;
      }
      put(b, day);
      record(b, day, "DEPENDENT", cause?.id);
    }
  }

  return finish([...placements.values()].filter((p) => p.reason === "DEPENDENT").length);

  // ───── RECALC_REST: o agendador de novo sobre todas as pendentes, de hoje até D-2 ─────
  function recalc(): EngineResult {
    const pool = input.activities.filter((a) => isPending(a) && a.scope === "AULA").sort(topo);
    const poolIds = new Set(pool.map((a) => a.id));
    const imp = (aulaId: string) => input.importanceByAula?.[aulaId] ?? 50;
    const cycleOf = (a: EngineActivity) => (isBlock(a) ? blockPrefix(a.key) : a.aulaId);
    const dropped = new Set<string>(); // ciclos (aulas) que saíram por falta de tempo
    let result: { days: Map<number, { key: string }[]>; leftover: number } | null = null;
    let leftoverIds: string[] = [];
    for (let guard = 0; guard < 15; guard++) {
      const live = pool.filter((a) => !dropped.has(cycleOf(a)));
      const liveIds = new Set(live.map((a) => a.id));
      const streams = new Map<string, CalendarStream>();
      live.forEach((a, i) => {
        const s = streams.get(a.subjectId) ?? { subjectId: a.subjectId, examQuestions: 0, sortOrder: streams.size, queue: [] };
        const after = (deps.get(a.id) ?? []).filter((d) => liveIds.has(d.id)).map((d) => ({ key: acts.get(d.id)!.key, gap: d.gap }));
        const ca: CycleActivity = {
          key: a.key, type: a.type, subjectId: a.subjectId, aulaId: a.aulaId, minutes: a.minutes, segmentIds: [], refKeys: [],
          scope: "AULA", turbo: a.turbo, after, cycle: cycleOf(a),
        };
        void i;
        s.queue.push(ca);
        streams.set(a.subjectId, s);
      });
      // o dia de hoje só entra se ainda tem folga; as revisões gerais de sobra (scope FINAL) podem ceder os dias que o conteúdo ocupar
      const from = Math.max(input.firstOrd, startOrd);
      const r = scheduleCalendar([...streams.values()], { weeklyMinutes: W, firstOrd: from, lastOrd: LAST });
      const placed = new Set<string>();
      for (const list of r.days.values()) for (const p of list) placed.add(p.key);
      leftoverIds = live.filter((a) => !placed.has(a.key)).map((a) => a.id);
      result = { days: r.days, leftover: r.leftover };
      if (leftoverIds.length === 0 || !input.importanceByAula) break;
      // o que não cabe sai pelas aulas de menor importância (se houver uma menos importante que a que ficou de fora)
      const worstLeft = Math.max(...leftoverIds.map((id) => imp(acts.get(id)!.aulaId)));
      const candidates = [...new Set(live.filter((a) => placed.has(a.key)).map(cycleOf))]
        .map((c) => ({ c, v: imp(live.find((a) => cycleOf(a) === c)!.aulaId) }))
        .filter((x) => x.v < worstLeft)
        .sort((x, y) => x.v - y.v);
      if (candidates.length === 0) break;
      dropped.add(candidates[0].c);
    }
    // aplica o resultado
    const idByKey = new Map(pool.map((a) => [a.key, a.id]));
    const newOrd = new Map<string, number>();
    for (const [ord, list] of result!.days) for (const p of list) newOrd.set(idByKey.get(p.key)!, ord);
    for (const a of pool) dropFromDay(a);
    for (const a of pool) {
      const to = newOrd.get(a.id);
      if (to === undefined) {
        noFit.add(a.id); // sai do plano (vai para SKIPPED ao confirmar; a prévia lista antes): voltar ao dia antigo colidiria com o resto
      } else {
        put(a, to);
        record(a, to, selectedSet.has(a.id) ? "SELECTED" : "DEPENDENT");
      }
    }
    // revisões gerais de sobra que ficaram nos dias ocupados pelo conteúdo cedem o lugar
    const contentDays = new Set(newOrd.values());
    const lastUsed = Math.max(-1, ...contentDays);
    for (const f of spareFinals()) {
      const o = cur.get(f.id)!;
      if (contentDays.has(o) || (o <= lastUsed && o >= startOrd)) {
        dropFromDay(f);
        yielded.add(f.id);
      }
    }
    void poolIds;
    return finish(pool.filter((a) => !selectedSet.has(a.id) && placements.has(a.id)).length);
  }

  // ───── saída ─────
  function finish(dependentsMoved: number): EngineResult {
    const moved = [...placements.values()];
    const changedDays = new Set<number>();
    for (const p of moved) {
      changedDays.add(p.fromOrd);
      changedDays.add(p.toOrd);
    }
    for (const id of [...dismissed, ...yielded, ...(option === "RECALC_REST" ? noFit : [])]) changedDays.add(original.get(id)!);
    const leaves = option === "RECALC_REST";
    const inDay = (ord: number) =>
      input.activities.filter((a) => a.status !== "SKIPPED" && !dismissed.has(a.id) && !yielded.has(a.id) && !(leaves && noFit.has(a.id)) && cur.get(a.id) === ord);
    const order = new Map<number, string[]>();
    for (const d of changedDays) {
      const list = inDay(d);
      const entries = list.map((a, i) => ({
        a,
        family: FAMILY[a.subjectId] ?? "OUTRA",
        seq: placements.has(a.id) ? 10_000 + i : a.sortOrder, // quem chegou entra depois; a ordem do dia é refeita por orderDay
      }));
      order.set(d, orderDay(entries).map((a) => a.id));
    }
    const dayLoads: EngineDayLoad[] = [...changedDays]
      .sort((a, b) => a - b)
      .map((ord) => ({ ord, before: loadBefore.get(ord) ?? 0, after: load.get(ord) ?? 0, target: Math.round(dayTarget(W, ord)) }))
      .filter((d) => d.before !== d.after);

    const warnings: EngineWarning[] = [];
    for (const d of dayLoads) if (d.after > d.target + 1 && d.after > d.before) warnings.push({ code: "OVER_DAY_TARGET", ord: d.ord, minutes: d.after - d.target });
    for (const d of changedDays) {
      for (const subjectId of new Set(inDay(d).map((a) => a.subjectId))) {
        const m = subj.get(`${d}|${subjectId}`) ?? 0;
        const had = input.activities.filter((a) => a.status !== "SKIPPED" && a.ord === d && a.subjectId === subjectId).reduce((n, a) => n + a.minutes, 0);
        if (m > MAX_SAME_SUBJECT_MINUTES_PER_DAY && m > had) warnings.push({ code: "OVER_SUBJECT_DAY", ord: d, subjectId, minutes: m });
      }
    }
    if (yielded.size) warnings.push({ code: "SPARE_REVIEW_YIELDED", count: yielded.size });
    if (option === "DISMISS" && dismissed.size) {
      warnings.push({ code: "COVERAGE_IMPACT", count: dismissed.size, minutes: [...dismissed].reduce((n, id) => n + acts.get(id)!.minutes, 0) });
    }
    const pendingCount = input.activities.filter((a) => isPending(a) && a.scope === "AULA").length;
    if (option !== "RECALC_REST" && pendingCount > 0 && dependentsMoved / pendingCount > 0.3) warnings.push({ code: "MANY_DEPENDENTS", count: dependentsMoved });
    if (noFit.size) warnings.push({ code: "DOES_NOT_FIT", count: noFit.size });

    return {
      placements: moved,
      dismissed: [...dismissed],
      yielded: [...yielded],
      doesNotFit: [...noFit],
      noFitLeavesPlan: leaves,
      order,
      dayLoads,
      warnings,
      dependentsMoved,
      pendingCount,
    };
  }
}
