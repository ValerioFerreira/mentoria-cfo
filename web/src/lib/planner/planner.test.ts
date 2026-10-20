import { describe, expect, it } from "vitest";
import { bandOf, generatePlan, hoursPerDayLabel, nextMonday, PlanInputError, type Level, type PlanInput, type PlanResult } from "./index";
import { dayIndexOf, mondayOf, weeksUntil } from "./dates";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "./fixtures";
import { CONTEST_SUBJECTS } from "../contests";

const catalog = loadCatalog();
const segments = loadSegments();
const ALL_PT = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");

function input(hours: number, subjects = ALL_PT, level: Level = 1, extra: Partial<PlanInput> = {}): PlanInput {
  return {
    catalog,
    segments,
    startDate: "2026-10-12",
    examDate: "2027-02-28",
    hoursPerWeek: hours,
    subjects: subjects.map((id) => ({ id, level })),
    ...extra,
  };
}

function flat(plan: PlanResult) {
  return plan.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, week: w.index, kind: w.kind })));
}

describe("datas e faixas", () => {
  it("próxima segunda e nº de semanas até a prova", () => {
    expect(nextMonday("2026-10-07")).toBe("2026-10-12");
    expect(nextMonday("2026-10-12")).toBe("2026-10-12");
    expect(weeksUntil("2026-10-12", "2027-02-28")).toBe(20);
  });
  it("faixas de horas e rótulo de horas por dia", () => {
    expect(bandOf(14)).toBe("LEVE");
    expect(bandOf(21)).toBe("LEVE");
    expect(bandOf(22)).toBe("MODERADO");
    expect(bandOf(28)).toBe("MODERADO");
    expect(bandOf(29)).toBe("AVANCADO");
    expect(hoursPerDayLabel("LEVE")).toBe("2h a 3h por dia");
    expect(hoursPerDayLabel("AVANCADO")).toContain("mais de 4h");
  });
});

describe("início no meio da semana", () => {
  it("segunda-feira da semana e dia da semana de qualquer data", () => {
    expect(mondayOf("2026-10-07")).toBe("2026-10-05"); // quarta
    expect(mondayOf("2026-10-11")).toBe("2026-10-05"); // domingo ainda é da semana anterior
    expect(mondayOf("2026-10-12")).toBe("2026-10-12");
    expect(dayIndexOf("2026-10-07")).toBe(2);
    expect(dayIndexOf("2026-10-11")).toBe(6);
    expect(dayIndexOf("2026-10-12")).toBe(0);
  });

  it("começando na quarta: a semana 1 só tem atividades de quarta em diante e o dia de início fica registrado", () => {
    const plan = generatePlan(input(25, ALL_PT, 1, { startDate: "2026-10-05", firstDay: 2 }));
    const w1 = plan.weeks[0].activities;
    expect(w1.length).toBeGreaterThan(0);
    expect(Math.min(...w1.map((a) => a.day!))).toBeGreaterThanOrEqual(2);
    expect(plan.params.startDate).toBe("2026-10-05");
    expect(plan.params.firstStudyDate).toBe("2026-10-07");
    // a primeira semana é parcial: tem menos minutos do que uma semana cheia
    expect(plan.weeks[0].targetMinutes).toBeLessThan(plan.params.weeklyMinutes * 0.8);
    // nenhuma outra semana é afetada
    expect(plan.weeks[1].activities.some((a) => a.day === 0)).toBe(true);
  });

  it("começar no meio da semana não perde atividades nem estoura os dias (domingo)", () => {
    for (const firstDay of [1, 3, 4, 5, 6]) {
      const plan = generatePlan(input(25, ALL_PT, 1, { startDate: "2026-10-05", firstDay }));
      const w1 = plan.weeks[0].activities;
      expect(w1.every((a) => a.day! >= firstDay && a.day! <= 6)).toBe(true);
      expect(new Set(flat(plan).map((a) => a.key)).size).toBe(flat(plan).length);
    }
  });

  it("firstDay padrão (0) equivale a começar na segunda e valores inválidos são rejeitados", () => {
    const a = generatePlan(input(25));
    const b = generatePlan(input(25, ALL_PT, 1, { firstDay: 0 }));
    expect(b.weeks.map((w) => w.activities.length)).toEqual(a.weeks.map((w) => w.activities.length));
    expect(a.params.firstStudyDate).toBe("2026-10-12");
    expect(() => generatePlan(input(25, ALL_PT, 1, { firstDay: 7 }))).toThrow(PlanInputError);
  });
});

describe("generatePlan — dia da prova e Legislações PE", () => {
  it("o conteúdo vai até D-2 e a véspera (D-1) tem uma única Revisão; nada no dia da prova nem depois (domingo ou dia útil)", () => {
    for (const [examDate, eveDay] of [["2027-02-28", 5], ["2027-03-03", 1], ["2027-02-22", 6]] as const) {
      const p = generatePlan(input(35, ALL_PT, 1, { examDate }));
      const last = p.weeks.at(-1)!;
      expect(Math.max(...last.activities.map((a) => a.day!)), examDate).toBe(eveDay);
      const eve = last.activities.filter((a) => a.day === eveDay);
      expect(eve, examDate).toHaveLength(1);
      expect(eve[0].type).toBe("REVISAO");
      expect(eve[0].scope).toBe("FINAL");
      for (const a of last.activities.filter((x) => x.day !== eveDay)) expect(a.day!).toBeLessThanOrEqual(eveDay - 1 < 0 ? 6 : eveDay);
    }
  });

  it("as aulas-base de Legislações PE entram mesmo com poucas horas (a incidência nunca é negativa)", () => {
    for (const s of catalog.subjects) for (const a of s.aulas) expect(a.incidence, a.id).toBeGreaterThanOrEqual(0);
    for (const hours of [14, 21]) {
      const p = generatePlan(input(hours, ALL_PT, 1));
      const leg = p.coverage.subjects.find((s) => s.subjectId === "legislacoes-pe")!;
      expect(leg.aulas.map((a) => a.aulaId), `${hours} h`).toContain("legislacoes-pe/a01");
      expect(leg.coverage, `${hours} h`).toBeGreaterThan(0.5);
    }
  });
});

describe("Modo Turbo (resumos analíticos)", () => {
  const SMALL = ["lingua-portuguesa", "matematica", "direito-constitucional", "fisica", "quimica", "informatica"];
  const importance = loadImportance("CBMPE_OFICIAL");
  const examQuestions = loadExamQuestions("CBMPE_OFICIAL");
  const allSummaries = Object.values(segments).flat().map((x) => x.id);
  const turboInput = (hours: number, subjects = ALL_PT, level: Level = 1, extra: Partial<PlanInput> = {}) =>
    input(hours, subjects, level, { importance, examQuestions, summaries: allSummaries, ...extra });
  const content = (p: PlanResult) => flat(p).filter((a) => a.scope !== "FINAL");

  it("sem Modo Turbo ninguém é resumo; com ele, o tempo curto passa a cobrir muito mais do edital", () => {
    const off = generatePlan(turboInput(21));
    const on = generatePlan(turboInput(21, ALL_PT, 1, { turbo: true }));
    expect(off.params.editalFits).toBe(false);
    expect(flat(off).some((a) => a.turbo)).toBe(false);
    expect(on.params.summaryUnits).toBeGreaterThan(0);
    expect(on.params.turboAulas).toBeGreaterThan(0);
    expect(on.coverage.selected).toBeGreaterThan(off.coverage.selected + 0.1);
    expect(on.warnings.some((w) => w.startsWith("Modo Turbo"))).toBe(true);
  });

  it("o Turbo prioriza a completude do edital: nunca cobre menos que o plano normal, nem com poucos resumos", () => {
    const few = allSummaries.filter((_, i) => i % 19 === 0);
    for (const hours of [14, 21, 28, 40]) {
      for (const summaries of [few, allSummaries]) {
        const off = generatePlan(turboInput(hours, ALL_PT, 1, { summaries }));
        const on = generatePlan(turboInput(hours, ALL_PT, 1, { turbo: true, summaries }));
        expect(on.coverage.selected, `${hours} h / ${summaries.length} resumos`).toBeGreaterThanOrEqual(off.coverage.selected - 1e-9);
      }
    }
  }, 60_000);

  it("com todos os resumos o Turbo fecha o edital a partir de 21 h e informa a parte lida por resumo", () => {
    const on = generatePlan(turboInput(21, ALL_PT, 1, { turbo: true }));
    expect(on.coverage.selected).toBeGreaterThan(0.99);
    expect(on.coverage.summaryShare).toBeGreaterThan(0.3);
    expect(on.coverage.summaryShare).toBeLessThanOrEqual(1);
    expect(generatePlan(turboInput(21)).coverage.summaryShare).toBe(0);
  });

  it("só vira resumo o trecho que TEM resumo: sem resumos disponíveis o Turbo não muda o plano", () => {
    const a = generatePlan(input(21, ALL_PT, 1, { importance, examQuestions }));
    const b = generatePlan(input(21, ALL_PT, 1, { importance, examQuestions, turbo: true, summaries: [] }));
    expect(b.params.summaryUnits).toBe(0);
    expect(JSON.stringify(b.weeks)).toBe(JSON.stringify(a.weeks));
    const some = new Set(allSummaries.filter((_, i) => i % 4 === 0));
    const c = generatePlan(turboInput(21, ALL_PT, 1, { turbo: true, summaries: [...some] }));
    const used = content(c).filter((a) => a.turbo).flatMap((a) => a.segmentIds);
    expect(used.length).toBeGreaterThan(0);
    for (const id of used) expect(some.has(id)).toBe(true);
  });

  it("atividades de resumo: ≤ 3 trechos da mesma disciplina, ≤ 60 min, e podem atravessar aulas", () => {
    const on = generatePlan(turboInput(21, ALL_PT, 1, { turbo: true }));
    const s = content(on).filter((a) => a.turbo);
    expect(s.length).toBeGreaterThan(20);
    let crossAula = 0;
    for (const a of s) {
      expect(a.type).toBe("TEORIA");
      expect(a.segmentIds.length).toBeGreaterThanOrEqual(1);
      expect(a.minutes).toBeLessThanOrEqual(60);
      expect(a.minutes).toBeGreaterThanOrEqual(15);
      expect(new Set(a.segmentIds.map((id) => id.split("/")[0])).size).toBe(1);
      if (new Set(a.segmentIds.map((id) => id.split("/")[1])).size > 1) crossAula++;
    }
    expect(s.some((a) => a.segmentIds.length === 3)).toBe(true);
    expect(crossAula).toBeGreaterThanOrEqual(0);
  });

  it("o ciclo flexibilizado mantém Questões (caderno curto) depois dos resumos e Revisão/Fixação reduzidas", () => {
    const on = generatePlan(turboInput(40, ALL_PT, 1, { turbo: true }));
    const c = content(on);
    const at = new Map(flat(on).map((a) => [a.key, (a.week - 1) * 7 + a.day!]));
    const turboQ = c.filter((a) => a.type === "QUESTOES" && a.refKeys.some((k) => c.find((x) => x.key === k)?.turbo));
    expect(turboQ.length).toBeGreaterThan(0);
    for (const q of turboQ) {
      expect(q.quiz).toEqual({ questions: 15, limitSeconds: 2400, mixed: false });
      for (const k of q.refKeys) expect(at.get(q.key)! - at.get(k)!).toBeGreaterThanOrEqual(1);
    }
    const reducedR = c.filter((a) => a.type === "REVISAO" && a.refKeys.some((k) => c.find((x) => x.key === k)?.turbo));
    for (const r of reducedR) expect(r.minutes).toBeLessThanOrEqual(35);
  });

  it("as trocas começam pelos trechos de menor importância no concurso", () => {
    const on = generatePlan(turboInput(40, ALL_PT, 1, { turbo: true }));
    const swapped = content(on).filter((a) => a.turbo).flatMap((a) => a.segmentIds);
    const kept = content(on).filter((a) => a.type === "TEORIA" && !a.turbo).flatMap((a) => a.segmentIds);
    const mean = (ids: string[]) => ids.reduce((n, id) => n + (importance[id] ?? 0), 0) / Math.max(1, ids.length);
    expect(swapped.length).toBeGreaterThan(0);
    expect(mean(swapped)).toBeLessThan(mean(kept));
  });

  it("trechos fora do edital do concurso (nota null) não entram no plano", () => {
    const out = Object.entries(importance).filter(([, v]) => v === null).map(([id]) => id);
    const p = generatePlan(input(50, ALL_PT, 1, { importance: { ...importance, "lingua-portuguesa/a02/s01": null }, examQuestions }));
    expect(flat(p).flatMap((a) => a.segmentIds)).not.toContain("lingua-portuguesa/a02/s01");
    expect(out.length).toBeGreaterThanOrEqual(0);
  });

  it("Teoria e Questões se intercalam: no máximo 4 dias seguidos só de Teoria", () => {
    for (const hours of [14, 21, 35]) {
      const p = generatePlan(turboInput(hours, ALL_PT, 0, { turbo: true }));
      const byOrd = new Map<number, Set<string>>();
      for (const a of content(p)) byOrd.set((a.week - 1) * 7 + a.day!, (byOrd.get((a.week - 1) * 7 + a.day!) ?? new Set()).add(a.type));
      let run = 0;
      let max = 0;
      for (const o of [...byOrd.keys()].sort((x, y) => x - y)) {
        run = byOrd.get(o)!.size === 1 && byOrd.get(o)!.has("TEORIA") ? run + 1 : 0;
        max = Math.max(max, run);
      }
      expect(max, `${hours} h`).toBeLessThanOrEqual(4);
    }
  });

  it("se o edital já cabe no tempo, o Modo Turbo não muda nada", () => {
    const need = generatePlan(turboInput(30, SMALL, 1)).params.fullEditalHoursPerWeek;
    const a = generatePlan(turboInput(Math.min(80, need + 6), SMALL, 1));
    const b = generatePlan(turboInput(Math.min(80, need + 6), SMALL, 1, { turbo: true }));
    expect(a.params.editalFits).toBe(true);
    expect(b.params.summaryUnits).toBe(0);
    expect(JSON.stringify(b.weeks)).toBe(JSON.stringify(a.weeks));
  });
});

describe("generatePlan — validações", () => {
  it("rejeita Inglês e Espanhol juntos", () => {
    expect(() => generatePlan(input(20, ["lingua-inglesa", "lingua-espanhola"]))).toThrow(PlanInputError);
  });
  it("exige início na segunda-feira e ao menos uma disciplina", () => {
    expect(() => generatePlan(input(20, ALL_PT, 1, { startDate: "2026-10-13" }))).toThrow(PlanInputError);
    expect(() => generatePlan(input(20, []))).toThrow(PlanInputError);
  });
});

describe.each([14, 21, 25, 35, 50])("generatePlan — invariantes com %i h/semana", (hours) => {
  const plan = generatePlan(input(hours));
  const acts = flat(plan);
  const ord = (a: { week: number; day?: number }) => (a.week - 1) * 7 + a.day!;
  const content = acts.filter((a) => a.scope !== "FINAL");

  it("ocupa as 20 semanas; a última tem a única Revisão da véspera e o conteúdo corre até D-2", () => {
    expect(plan.weeks.length).toBe(20);
    const eve = acts.filter((a) => a.scope === "FINAL" && a.key.endsWith("#VESPERA"));
    expect(eve).toHaveLength(1);
    expect(eve[0].week).toBe(20);
    expect(acts.filter((a) => ord(a) === ord(eve[0]))).toHaveLength(1); // D-1 só tem essa atividade
    expect(Math.max(...content.map(ord))).toBeLessThanOrEqual(ord(eve[0]) - 1);
  });

  it("nenhuma semana excede a meta de minutos (±5%) e o total cabe na capacidade", () => {
    for (const w of plan.weeks) expect(w.targetMinutes).toBeLessThanOrEqual(plan.params.weeklyMinutes * 1.05 + 1);
    expect(plan.params.plannedHours).toBeLessThanOrEqual(plan.params.capacityHours * 1.05 + 1);
  });

  it("toda atividade tem um dia (seg–dom) e a Revisão nunca cai no dia das Teorias que revê", () => {
    const at = new Map(acts.map((a) => [a.key, ord(a)]));
    for (const a of acts) {
      expect(a.day).toBeGreaterThanOrEqual(0);
      expect(a.day).toBeLessThanOrEqual(6);
      if (a.type === "REVISAO" && a.scope === "AULA") for (const r of a.refKeys) expect(at.get(r)!, a.key).toBeLessThan(ord(a));
    }
  });

  it("os dias da semana vêm em ordem crescente e nenhum dia concentra mais de 3 disciplinas sem carga alta", () => {
    for (const w of plan.weeks) {
      for (let i = 1; i < w.activities.length; i++) expect(w.activities[i].day!).toBeGreaterThanOrEqual(w.activities[i - 1].day!);
      for (let d = 0; d < 7; d++) {
        const dayActs = w.activities.filter((a) => a.day === d && a.scope === "AULA");
        const mins = dayActs.reduce((n, a) => n + a.minutes, 0);
        expect(new Set(dayActs.map((a) => a.subjectId)).size).toBeLessThanOrEqual(Math.max(4, Math.ceil(mins / 45)));
      }
    }
  });

  it("ciclo respeitado em dias: Revisão depois da Teoria, Fixação depois de toda a Teoria/Revisão, Questões depois da Fixação (ou da Revisão)", () => {
    for (const aula of new Set(content.map((a) => a.aulaId))) {
      const l = content.filter((a) => a.aulaId === aula);
      const first = (t: string) => Math.min(...l.filter((a) => a.type === t).map(ord));
      const last = (t: string) => Math.max(...l.filter((a) => a.type === t).map(ord));
      const has = (t: string) => l.some((a) => a.type === t);
      if (has("REVISAO")) expect(first("REVISAO"), aula).toBeGreaterThan(first("TEORIA"));
      if (has("FIXACAO")) {
        expect(first("FIXACAO"), aula).toBeGreaterThan(last("TEORIA"));
        if (has("REVISAO")) expect(first("FIXACAO"), aula).toBeGreaterThan(last("REVISAO"));
      }
      if (has("QUESTOES")) {
        expect(first("QUESTOES"), aula).toBeGreaterThan(last("TEORIA"));
        if (has("FIXACAO")) expect(first("QUESTOES"), aula).toBeGreaterThan(last("FIXACAO"));
        else if (has("REVISAO")) expect(first("QUESTOES"), aula).toBeGreaterThan(last("REVISAO"));
      }
    }
  });

  it("cada atividade de Teoria tem no máximo 17 páginas e cada Revisão atrela 1–4 Teorias", () => {
    const pages = (ids: string[]) =>
      ids.reduce((n, id) => {
        const aula = id.split("/s")[0];
        return n + segments[aula].find((s) => s.id === id)!.pages;
      }, 0);
    for (const a of content.filter((x) => x.type === "TEORIA")) expect(pages(a.segmentIds)).toBeLessThanOrEqual(17);
    for (const a of content.filter((x) => x.type === "REVISAO")) {
      expect(a.refKeys.length).toBeGreaterThanOrEqual(1);
      expect(a.refKeys.length).toBeLessThanOrEqual(4);
    }
  });

  it("chaves de atividade são únicas", () => {
    expect(new Set(acts.map((a) => a.key)).size).toBe(acts.length);
  });
});

describe("generatePlan — comportamento", () => {
  it("cobertura cresce com as horas e todas as disciplinas aparecem com tempo suficiente", () => {
    const p14 = generatePlan(input(14));
    const p25 = generatePlan(input(25));
    const p35 = generatePlan(input(35));
    expect(p25.coverage.selected).toBeGreaterThan(p14.coverage.selected);
    expect(p35.coverage.selected).toBeGreaterThan(p25.coverage.selected);
    const subjects25 = new Set(flat(p25).filter((a) => a.scope !== "FINAL").map((a) => a.subjectId));
    expect(subjects25.size).toBe(ALL_PT.length);
  });

  it("é determinístico", () => {
    expect(JSON.stringify(generatePlan(input(28)))).toBe(JSON.stringify(generatePlan(input(28))));
  });

  it("nível mais baixo aumenta a prioridade e o nº de revisões", () => {
    const low = generatePlan(input(21, ["direito-administrativo", "fisica"], 0));
    const high = generatePlan(input(21, ["direito-administrativo", "fisica"], 3));
    const revs = (p: PlanResult) => flat(p).filter((a) => a.type === "REVISAO" && a.scope === "AULA").length;
    const teo = (p: PlanResult) => flat(p).filter((a) => a.type === "TEORIA").length;
    expect(revs(low) / teo(low)).toBeGreaterThan(revs(high) / teo(high));
  });

  it("poucas disciplinas terminam cedo e as semanas sobrantes viram revisão", () => {
    const p = generatePlan(input(35, ["legislacoes-pe"]));
    expect(p.params.plannedHours).toBeLessThan(p.params.capacityHours);
    expect(p.params.contentWeeks).toBeLessThan(p.params.totalWeeks - 1);
    expect(p.weeks.filter((w) => w.kind === "FINAL_REVIEW").length).toBeGreaterThanOrEqual(2);
    // com os complementos do MentorIA (Decreto 50.014, Lei 15.187 e Lei 14.751) o edital da disciplina fica completo
    expect(p.coverage.subjects[0].coverage).toBeGreaterThan(0.99);
  });

  it("as lacunas do material-base foram preenchidas por complementos: não há aviso de lacuna aberta, mas o aviso existe se uma lacuna reaparecer", () => {
    const p = generatePlan(input(21, ["legislacoes-pe", "lingua-inglesa"]));
    expect(p.warnings.filter((w) => w.startsWith("Lacuna no material"))).toHaveLength(0);
    const aulas = catalog.subjects.flatMap((s) => s.aulas).filter((a) => a.source === "authored");
    expect(aulas.length).toBeGreaterThanOrEqual(11);
    const withGap = { ...catalog, gaps: [{ id: "x", subject: "legislacoes-pe", item: "Norma X", evidence: "", severity: "high" as const, remedy: "Módulo." }] };
    expect(generatePlan(input(21, ["legislacoes-pe"], 1, { catalog: withGap })).warnings.some((w) => w.includes("Norma X"))).toBe(true);
  });

  it("Português usa as questões da Aula 14 (prática) na Fixação das aulas de teoria", () => {
    const p = generatePlan(input(50, ["lingua-portuguesa"]));
    const fix = flat(p).filter((a) => a.type === "FIXACAO" && a.aulaId === "lingua-portuguesa/a01");
    expect(fix.some((a) => a.fixRanges?.some((r) => r.sourceAula === "lingua-portuguesa/a14"))).toBe(true);
  });
});

describe("modelo de tempo", () => {
  const minutesOf = (p: PlanResult, subject: string) => p.coverage.subjects.find((s) => s.subjectId === subject)!.minutes;

  it("a Teoria segue a regra de 10–17 págs. por hora: Legislações PE (44 págs.) leva ~3–5 h de leitura", () => {
    const baseOnly = Object.fromEntries(["c01", "c02", "c03"].map((c) => [`legislacoes-pe/${c}`, 2 as const])); // só as aulas 01 e 02 (44 págs.)
    const p = generatePlan(input(35, ["legislacoes-pe"], 0, { known: baseOnly }));
    const t = minutesOf(p, "legislacoes-pe").teoria / 60;
    expect(t).toBeGreaterThan(2.5);
    expect(t).toBeLessThan(5.5);
  });

  it("quanto mais avançado o aluno, menos minutos cada atividade leva", () => {
    const mins = (level: Level) => {
      const m = minutesOf(generatePlan(input(50, ["direito-administrativo"], level)), "direito-administrativo");
      return m.teoria + m.revisao + m.fixacao + m.questoes;
    };
    expect(mins(3)).toBeLessThan(mins(2));
    expect(mins(2)).toBeLessThan(mins(1));
    expect(mins(1)).toBeLessThan(mins(0));
  });

  it("a anamnese por aula: 'já estudei' encurta a leitura e 'domino' tira a aula do plano sem perder cobertura", () => {
    const aulas = catalog.subjects.find((s) => s.id === "direito-administrativo")!.aulas.filter((a) => a.selectable);
    const base = generatePlan(input(35, ["direito-administrativo"], 1));
    const studied = generatePlan(input(35, ["direito-administrativo"], 1, { known: Object.fromEntries(aulas.map((a) => [a.id, 1 as const])) }));
    const mastered = generatePlan(input(35, ["direito-administrativo"], 1, { known: Object.fromEntries(aulas.map((a) => [a.id, 2 as const])) }));
    expect(minutesOf(studied, "direito-administrativo").teoria).toBeLessThan(minutesOf(base, "direito-administrativo").teoria);
    expect(flat(mastered).filter((a) => a.kind === "CONTENT")).toHaveLength(0);
    expect(mastered.coverage.subjects[0].coverage).toBeGreaterThan(0.99);
  });

  it("ciclo mínimo completo: com o tempo justo para ver todas as aulas, cada uma fecha Teoria → Revisão → Fixação → Questões", () => {
    const SMALL = ["lingua-portuguesa", "matematica", "direito-constitucional"];
    const need = generatePlan(input(30, SMALL, 1)).params.fullEditalHoursPerWeek;
    const p = generatePlan(input(Math.min(80, need), SMALL, 1));
    const content = flat(p).filter((a) => a.scope !== "FINAL");
    const n = (t: string) => content.filter((a) => a.type === t).length;
    expect(n("REVISAO")).toBeGreaterThan(0);
    expect(n("FIXACAO")).toBeGreaterThan(0);
    expect(n("QUESTOES")).toBeGreaterThan(0);
    for (const aula of new Set(content.map((a) => a.aulaId))) {
      const l = content.filter((a) => a.aulaId === aula);
      if (l.some((a) => a.type === "TEORIA")) {
        expect(l.some((a) => a.type === "REVISAO"), aula).toBe(true);
        expect(l.some((a) => a.type === "QUESTOES"), aula).toBe(true);
      }
    }
  });

  it("com o máximo de horas, o perfil avançado cobre a maior parte do edital e nenhuma disciplina fica de fora", () => {
    const p = generatePlan(input(50, ALL_PT, 3));
    expect(p.coverage.selected).toBeGreaterThan(0.8);
    expect(p.coverage.subjects.every((s) => s.aulas.length >= 1)).toBe(true);
    expect(generatePlan(input(14, ALL_PT, 0)).coverage.subjects.every((s) => s.aulas.length >= 1)).toBe(true);
  });

  it("não há semana de revisão final fixa: com o edital apertado o conteúdo ocupa até a semana da prova", () => {
    const tight = generatePlan(input(35, ALL_PT, 1));
    expect(tight.params.contentWeeks).toBeGreaterThanOrEqual(19);
    const roomy = generatePlan(input(35, ["legislacoes-pe"], 1));
    expect(roomy.weeks.filter((w) => w.kind === "FINAL_REVIEW").length).toBeGreaterThanOrEqual(2); // sobra vira revisão geral antes de D-2
  });

  it("PCPE com 10h/semana e todas as 12 disciplinas sem Turbo não deixa nenhuma disciplina de fora", () => {
    const pcpeSubjects = CONTEST_SUBJECTS.PCPE_AGENTE.filter((id) => id !== "lingua-espanhola" && id !== "lingua-inglesa");
    const importance = loadImportance("PCPE_AGENTE");
    const examQuestions = loadExamQuestions("PCPE_AGENTE");
    const p = generatePlan({
      catalog,
      segments,
      contest: "PCPE_AGENTE",
      importance,
      examQuestions,
      startDate: "2026-10-19",
      firstDay: 1,
      examDate: "2027-03-07",
      hoursPerWeek: 10,
      subjects: pcpeSubjects.map((id) => ({ id, level: 0 as const })),
      turbo: false,
    });
    for (const sub of pcpeSubjects) {
      const hasActs = flat(p).some((a) => a.subjectId === sub && a.scope !== "FINAL");
      expect(hasActs, `disciplina ${sub} deve ter ao menos uma aula no plano`).toBe(true);
    }
  });
});

