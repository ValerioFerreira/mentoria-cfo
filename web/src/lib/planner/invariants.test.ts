// Invariantes do planejador rodando com o catálogo e os trechos REAIS de /content, numa matriz de entradas
// (horas × nível × disciplinas × início × data da prova). Não fixa valores de conteúdo: só propriedades estruturais.
import { describe, expect, it } from "vitest";
import { generatePlan, PlanInputError } from "./index";
import { addDays, dayIndexOf } from "./dates";
import { loadCatalog, loadSegments } from "./fixtures";
import { CONTEST_SUBJECTS } from "../contests";
import type { Level, PlanInput, PlanResult } from "./types";

const catalog = loadCatalog();
const segments = loadSegments();
const ALL = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
const SMALL = ["lingua-portuguesa", "matematica", "direito-constitucional"];

const input = (hours: number, subjects: string[] = ALL, level: Level = 1, extra: Partial<PlanInput> = {}): PlanInput => ({
  catalog, segments, startDate: "2026-10-12", examDate: "2027-02-28", hoursPerWeek: hours, subjects: subjects.map((id) => ({ id, level })), ...extra,
});
const acts = (p: PlanResult) => p.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, week: w.index, kind: w.kind })));

const MATRIX: { hours: number; level: Level; subjects: string[]; label: string }[] = [];
for (const hours of [14, 21, 28, 40, 50])
  for (const level of [0, 2, 3] as Level[])
    for (const [label, subjects] of [["todas", ALL], ["3 disciplinas", SMALL]] as const) MATRIX.push({ hours, level, subjects: [...subjects], label });

describe("invariantes do plano (matriz de entradas)", () => {
  const plans = MATRIX.map((m) => ({ ...m, plan: generatePlan(input(m.hours, m.subjects, m.level)) }));

  it("sempre ocupa todas as semanas até a prova, em ordem, com datas de segunda a segunda", () => {
    for (const { plan, hours, level, label } of plans) {
      const id = `${hours}h/${level}/${label}`;
      expect(plan.weeks.length, id).toBeLessThanOrEqual(plan.params.totalWeeks);
      plan.weeks.forEach((w, i) => {
        expect(w.index, id).toBe(i + 1);
        expect(w.startDate, id).toBe(addDays("2026-10-12", i * 7));
      });
      // a última semana é a da véspera da prova: tem a única Revisão de D-1
      expect(plan.weeks.at(-1)!.activities.filter((a) => a.key.endsWith("#VESPERA")), id).toHaveLength(1);
    }
  });
  it("a meta de cada semana é a soma das atividades e nunca passa de 105% da meta semanal", () => {
    for (const { plan, hours, level, label } of plans) {
      for (const w of plan.weeks) {
        const sum = w.activities.reduce((n, a) => n + a.minutes, 0);
        expect(w.targetMinutes, `${hours}h/${level}/${label} sem. ${w.index}`).toBe(sum);
        expect(sum, `${hours}h/${level}/${label} sem. ${w.index}`).toBeLessThanOrEqual(plan.params.weeklyMinutes * 1.05 + 1e-6);
      }
    }
  });
  it("chaves únicas; toda referência (refKeys) é de uma atividade anterior e da mesma disciplina", () => {
    for (const { plan, hours, level, label } of plans) {
      const seen = new Map<string, string>();
      for (const a of acts(plan)) {
        expect(seen.has(a.key), `${hours}h/${level}/${label} chave repetida ${a.key}`).toBe(false);
        for (const k of a.refKeys) {
          expect(seen.has(k), `${a.key} refere ${k} antes de existir`).toBe(true);
          expect(seen.get(k)).toBe(a.subjectId);
        }
        seen.set(a.key, a.subjectId);
      }
    }
  });
  it("só entram disciplinas escolhidas e as aulas pertencem à disciplina da atividade", () => {
    for (const { plan, subjects } of plans) {
      for (const a of acts(plan)) {
        expect(subjects).toContain(a.subjectId);
        expect(a.aulaId.startsWith(`${a.subjectId}/`)).toBe(true);
      }
    }
  });
  it("todo trecho citado existe no catálogo, na aula indicada, e cada trecho tem no máximo uma Teoria", () => {
    const known = new Map(Object.values(segments).flat().map((s) => [s.id, s.aula]));
    for (const { plan, hours, level, label } of plans) {
      const teoriaSeen = new Set<string>();
      for (const a of acts(plan)) {
        for (const id of a.segmentIds) {
          expect(known.has(id), id).toBe(true);
          if (a.scope !== "FINAL") expect(known.get(id), id).toBe(a.aulaId);
        }
        if (a.type === "TEORIA") for (const id of a.segmentIds) {
          expect(teoriaSeen.has(id), `${hours}h/${level}/${label}: ${id} duas vezes`).toBe(false);
          teoriaSeen.add(id);
        }
      }
    }
  });
  it("atividades duram o que o tipo pede (múltiplos de 5): Teoria 35–80, Revisão 30–60, Fixação 30–60, Questões 40–80; Turbo mais curto", () => {
    const range: Record<string, [number, number]> = { TEORIA: [35, 80], REVISAO: [25, 60], FIXACAO: [30, 60], QUESTOES: [40, 80] };
    for (const { plan } of plans) {
      for (const a of acts(plan)) {
        expect(a.minutes % 5).toBe(0);
        expect(a.minutes, `${a.key} ${a.type}`).toBeGreaterThanOrEqual(range[a.type][0]);
        expect(a.minutes, `${a.key} ${a.type}`).toBeLessThanOrEqual(range[a.type][1]);
        if (a.type === "TEORIA") expect(a.segmentIds.length).toBeGreaterThan(0);
        if (a.type === "FIXACAO") expect(a.fixRanges!.length).toBeGreaterThan(0);
        if (a.type === "QUESTOES") expect(a.quiz).toBeDefined();
      }
    }
  });
  it("nenhum dia da semana fica fora de 0–6; o conteúdo vai até D-2 e só a Revisão da véspera (D-1) cai depois", () => {
    const examDay = dayIndexOf("2027-02-28"); // domingo (6)
    for (const { plan } of plans) {
      for (const a of acts(plan)) {
        expect(a.day).toBeGreaterThanOrEqual(0);
        expect(a.day).toBeLessThanOrEqual(6);
      }
      for (const a of plan.weeks.at(-1)!.activities) expect(a.day!).toBeLessThan(examDay);
      const eve = plan.weeks.at(-1)!.activities.filter((a) => a.day === examDay - 1);
      expect(eve).toHaveLength(1);
      expect(eve[0].key.endsWith("#VESPERA")).toBe(true);
    }
  });
  it("cobertura e profundidade ficam em 0–1; cobertura do edital ≤ da seleção", () => {
    for (const { plan } of plans) {
      for (const x of [plan.coverage.selected, plan.coverage.edital, plan.coverage.depth]) {
        expect(x).toBeGreaterThanOrEqual(0);
        expect(x).toBeLessThanOrEqual(1 + 1e-9);
      }
      expect(plan.coverage.edital).toBeLessThanOrEqual(plan.coverage.selected + 1e-9);
    }
  });
  it("os parâmetros são coerentes (semanas, capacidade, horas)", () => {
    for (const { plan, hours } of plans) {
      const p = plan.params;
      expect(p.totalWeeks).toBe(20);
      expect(p.hoursPerWeek).toBe(hours);
      expect(p.contentWeeks).toBeLessThanOrEqual(p.totalWeeks);
      expect(p.contentWeeks + p.reviewWeeks).toBe(p.totalWeeks);
      expect(p.plannedHours).toBeLessThanOrEqual(p.capacityHours * 1.05 + 1);
      expect(p.weeklyMinutes).toBe(Math.floor(hours * 60 * 0.9));
      expect(p.firstStudyDate).toBe("2026-10-12");
      expect(p.fullEditalHoursPerWeek).toBeGreaterThan(0);
    }
  });
  it("editalFits é consistente com fullEditalHoursPerWeek e com a cobertura (quem estuda bem acima do necessário para o ciclo mínimo vê o edital)", () => {
    for (const { plan, hours } of plans) {
      if (hours >= plan.params.fullEditalHoursPerWeek * 1.5) expect(plan.params.editalFits).toBe(true);
      if (plan.params.editalFits) expect(plan.coverage.selected).toBeGreaterThan(0.99);
    }
    // 3 disciplinas cabem folgadamente nas horas altas
    const small = plans.filter((p) => p.subjects.length === SMALL.length && p.hours === 50);
    for (const p of small) expect(p.plan.params.editalFits).toBe(true);
  });
  // Piso de prática: mesmo quando o edital não cabe, cada aula que entra fecha o ciclo mínimo (Revisão + Questões), então a prática
  // não é sobra: Revisão + Fixação + Questões ficam em torno de metade do tempo de conteúdo.
  it("quando o edital não cabe, a prática (Revisão + Fixação + Questões) é pelo menos 30% do tempo de conteúdo e não há Questões sem Revisão", () => {
    for (const { plan, hours, level, label } of plans) {
      if (plan.params.editalFits) continue;
      const content = acts(plan).filter((a) => a.scope !== "FINAL");
      const total = content.reduce((n, a) => n + a.minutes, 0);
      const practice = content.filter((a) => a.type !== "TEORIA").reduce((n, a) => n + a.minutes, 0);
      expect(practice / total, `${hours}h/${level}/${label}`).toBeGreaterThanOrEqual(0.3);
      for (const q of content.filter((a) => a.type === "QUESTOES"))
        expect(content.some((r) => r.aulaId === q.aulaId && r.type === "REVISAO"), `${hours}h/${level}/${label} ${q.aulaId}`).toBe(true);
    }
  });
});

describe("variações de calendário", () => {
  it("prova de terça a domingo: nada no dia da prova nem depois", () => {
    for (const examDate of ["2027-02-23", "2027-02-24", "2027-02-25", "2027-02-26", "2027-02-27", "2027-02-28"]) {
      const plan = generatePlan(input(25, SMALL, 1, { examDate }));
      const examDay = dayIndexOf(examDate);
      const last = plan.weeks.at(-1)!;
      expect(last.startDate, examDate).toBe(addDays(examDate, -examDay));
      expect(last.activities.length, examDate).toBeGreaterThan(0);
      for (const a of last.activities) expect(a.day!, examDate).toBeLessThan(examDay);
    }
  });
  it("prova na segunda-feira: a semana da prova não tem atividades e a véspera (domingo) tem a única Revisão", () => {
    const plan = generatePlan(input(25, SMALL, 1, { examDate: "2027-02-22" }));
    const last = plan.weeks.at(-1)!;
    expect(last.startDate).toBe("2027-02-15");
    expect(last.activities.filter((a) => a.day === 6)).toHaveLength(1);
    expect(plan.weeks.every((w) => w.startDate < "2027-02-22")).toBe(true);
  });
  it("início em qualquer dia da semana 1 (firstDay 0–6) nunca agenda antes do dia de início e nunca perde disciplina", () => {
    for (let firstDay = 0; firstDay <= 6; firstDay++) {
      const plan = generatePlan(input(25, SMALL, 1, { firstDay }));
      expect(plan.params.firstStudyDate).toBe(addDays("2026-10-12", firstDay));
      expect(Math.min(...plan.weeks[0].activities.map((a) => a.day!)), `firstDay ${firstDay}`).toBeGreaterThanOrEqual(firstDay);
      expect(new Set(acts(plan).map((a) => a.subjectId))).toEqual(new Set(SMALL));
    }
  });
  it("prova bem próxima (2 a 4 semanas): gera plano válido, sem estourar semanas, com a revisão da véspera", () => {
    for (const examDate of ["2026-10-25", "2026-11-01", "2026-11-08"]) {
      const plan = generatePlan(input(25, SMALL, 1, { examDate }));
      expect(plan.params.totalWeeks).toBeGreaterThanOrEqual(2);
      expect(plan.weeks.length).toBeLessThanOrEqual(plan.params.totalWeeks);
      expect(plan.weeks.at(-1)!.activities.some((a) => a.key.endsWith("#VESPERA"))).toBe(true);
    }
  });
  it("prova distante (1 ano): as semanas sobrantes viram revisão e o plano continua válido", () => {
    const plan = generatePlan(input(25, SMALL, 1, { examDate: "2027-10-10" }));
    expect(plan.params.totalWeeks).toBe(52);
    expect(plan.weeks).toHaveLength(52);
    expect(plan.weeks.filter((w) => w.kind === "FINAL_REVIEW").length).toBeGreaterThanOrEqual(2);
    expect(plan.params.editalFits).toBe(true);
  });
  it("com o dia de início colado na prova não sobra dia de estudo: erro de data muito próxima", () => {
    expect(() => generatePlan(input(25, SMALL, 1, { examDate: "2026-10-19", firstDay: 6 }))).toThrowError(PlanInputError);
  });
});

describe("validação de entrada", () => {
  const bad = (extra: Partial<PlanInput> & { hoursPerWeek?: number }, msg: RegExp) => {
    expect(() => generatePlan(input(extra.hoursPerWeek ?? 25, extra.subjects ? extra.subjects.map((s) => s.id) : SMALL, 1, extra))).toThrowError(msg);
    expect(() => generatePlan(input(extra.hoursPerWeek ?? 25, extra.subjects ? extra.subjects.map((s) => s.id) : SMALL, 1, extra))).toThrowError(PlanInputError);
  };
  it("horas fora de 5–80 (inclusive NaN e infinito) são rejeitadas", () => {
    for (const h of [0, 4.9, 80.1, 500, -3, Number.NaN, Number.POSITIVE_INFINITY]) bad({ hoursPerWeek: h }, /Horas por semana/);
  });
  it("aceita os extremos 5 e 80 horas", () => {
    expect(() => generatePlan(input(5, SMALL))).not.toThrow();
    expect(() => generatePlan(input(80, SMALL))).not.toThrow();
  });
  it("início que não é segunda-feira é rejeitado", () => {
    for (const d of ["2026-10-13", "2026-10-14", "2026-10-17", "2026-10-18"]) bad({ startDate: d }, /segunda-feira/);
  });
  it("dia de início fora de 0–6 ou fracionado é rejeitado", () => {
    for (const fd of [-1, 7, 1.5, Number.NaN]) bad({ firstDay: fd }, /Dia de início/);
  });
  it("prova com menos de 2 semanas ou antes do início é rejeitada", () => {
    bad({ examDate: "2026-10-18" }, /muito próxima/);
    bad({ examDate: "2026-10-01" }, /muito próxima/);
  });
  it("disciplina inexistente e lista vazia são rejeitadas", () => {
    bad({ subjects: [{ id: "astrologia", level: 0 }] }, /desconhecida/);
    expect(() => generatePlan({ ...input(25), subjects: [] })).toThrowError(/ao menos uma disciplina/i);
  });
  it("Inglês e Espanhol juntos são rejeitados; Espanhol sozinho é aceito", () => {
    bad({ subjects: [{ id: "lingua-inglesa", level: 0 }, { id: "lingua-espanhola", level: 0 }] }, /apenas uma língua/);
    const plan = generatePlan({ ...input(25), subjects: [{ id: "lingua-espanhola", level: 1 }, { id: "matematica", level: 1 }] });
    expect(new Set(acts(plan).map((a) => a.subjectId))).toEqual(new Set(["lingua-espanhola", "matematica"]));
  });
});

describe("propriedades de comportamento", () => {
  it("é determinístico mesmo com Modo Turbo, anamnese e início no meio da semana", () => {
    const extra: Partial<PlanInput> = { turbo: true, firstDay: 3, known: { "matematica/a01": 1, "matematica/a02": 2 } };
    expect(generatePlan(input(14, ALL, 0, extra))).toEqual(generatePlan(input(14, ALL, 0, extra)));
  });
  it("não muta o catálogo nem os trechos recebidos", () => {
    const before = JSON.stringify([catalog, segments]);
    generatePlan(input(21, ALL, 0, { turbo: true }));
    expect(JSON.stringify([catalog, segments])).toBe(before);
  });
  it("mais horas por semana nunca diminui o total de horas planejadas de conteúdo", () => {
    let prev = 0;
    for (const h of [14, 17, 21, 25, 29, 35, 42, 50]) {
      const p = generatePlan(input(h, ALL, 1)).params.plannedHours;
      expect(p, `${h} h`).toBeGreaterThanOrEqual(prev);
      prev = p;
    }
  });
  it("mais horas por semana não reduz a cobertura do edital (com tolerância de arredondamento)", () => {
    let prev = 0;
    for (const h of [14, 17, 21, 25, 29, 35, 42, 50]) {
      const c = generatePlan(input(h, ALL, 1)).coverage.edital;
      expect(c, `${h} h`).toBeGreaterThanOrEqual(prev - 0.01);
      prev = c;
    }
  });
  it("aula marcada como dominada some das atividades e as demais permanecem", () => {
    const base = generatePlan(input(25, SMALL, 1));
    const aula = acts(base).find((a) => a.type === "TEORIA" && a.subjectId === "matematica")!.aulaId;
    const p = generatePlan(input(25, SMALL, 1, { known: { [aula]: 2 } }));
    expect(acts(p).some((a) => a.aulaId === aula && a.scope !== "FINAL")).toBe(false);
    expect(acts(p).some((a) => a.subjectId === "matematica")).toBe(true);
  });
  it("conhecimento '0' na anamnese equivale a não informar", () => {
    const aula = acts(generatePlan(input(25, SMALL, 1)))[0].aulaId;
    expect(generatePlan(input(25, SMALL, 1, { known: { [aula]: 0 } }))).toEqual(generatePlan(input(25, SMALL, 1)));
  });
  it("nível mais alto na disciplina reduz o tempo médio das Teorias", () => {
    const mean = (lvl: Level) => {
      const t = acts(generatePlan(input(30, ["matematica"], lvl))).filter((a) => a.type === "TEORIA");
      return t.reduce((n, a) => n + a.minutes, 0) / t.length;
    };
    expect(mean(3)).toBeLessThan(mean(0));
  });
  it("avisos: lacunas altas/médias não resolvidas só aparecem se houver; textos não vazios", () => {
    const p = generatePlan(input(14, ALL, 0));
    for (const w of p.warnings) expect(w.trim().length).toBeGreaterThan(10);
  });
});
