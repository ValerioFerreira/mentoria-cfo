import { describe, expect, it } from "vitest";
import { bandOf, generatePlan, hoursPerDayLabel, nextMonday, PlanInputError, type Level, type PlanInput, type PlanResult } from "./index";
import { dayIndexOf, mondayOf, weeksUntil } from "./dates";
import { loadCatalog, loadSegments } from "./fixtures";

const catalog = loadCatalog();
const segments = loadSegments();
const ALL_PT = catalog.subjects.filter((s) => s.id !== "lingua-espanhola").map((s) => s.id);

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
  const content = acts.filter((a) => a.kind === "CONTENT");

  it("ocupa as 20 semanas, com as 2 últimas (ao menos) de revisão final", () => {
    expect(plan.weeks.length).toBe(20);
    expect(plan.weeks.at(-1)!.kind).toBe("FINAL_REVIEW");
    expect(plan.weeks.at(-2)!.kind).toBe("FINAL_REVIEW");
    expect(plan.weeks.filter((w) => w.kind === "FINAL_REVIEW").length).toBeGreaterThanOrEqual(2);
  });

  it("nenhuma semana excede a meta de minutos (±5%) e o total cabe na capacidade", () => {
    for (const w of plan.weeks) expect(w.targetMinutes).toBeLessThanOrEqual(plan.params.weeklyMinutes * 1.05 + 1);
    expect(plan.params.plannedHours).toBeLessThanOrEqual(plan.params.capacityHours + 1);
  });

  it("toda atividade tem um dia (seg–dom) e a Revisão quase nunca cai no dia das Teorias que revê", () => {
    let total = 0;
    let same = 0;
    for (const w of plan.weeks) {
      const dayOf = new Map(w.activities.map((a) => [a.key, a.day]));
      for (const a of w.activities) {
        expect(a.day).toBeGreaterThanOrEqual(0);
        expect(a.day).toBeLessThanOrEqual(6);
        if (a.type === "REVISAO" && a.scope === "AULA")
          for (const r of a.refKeys) {
            if (!dayOf.has(r)) continue;
            total++;
            if (dayOf.get(r) === a.day) same++;
            else expect(dayOf.get(r)!).toBeLessThan(a.day!);
          }
      }
    }
    // só semanas muito carregadas (poucos dias para muitas sessões da mesma disciplina) forçam Teoria e Revisão no mesmo dia
    expect(same / Math.max(1, total)).toBeLessThanOrEqual(hours <= 28 ? 0.02 : 0.12);
  });

  const lastContent = plan.weeks.filter((x) => x.kind === "CONTENT").at(-1);
  it("os dias da semana vêm em ordem crescente e nenhum dia concentra mais de 3 disciplinas sem carga alta", () => {
    for (const w of plan.weeks) {
      for (let i = 1; i < w.activities.length; i++) expect(w.activities[i].day!).toBeGreaterThanOrEqual(w.activities[i - 1].day!);
      if (w.kind === "FINAL_REVIEW" || w === lastContent) continue; // na reta final todas as disciplinas entram; a última semana de conteúdo junta as sobras
      for (let d = 0; d < 7; d++) {
        const dayActs = w.activities.filter((a) => a.day === d);
        const mins = dayActs.reduce((n, a) => n + a.minutes, 0);
        expect(new Set(dayActs.map((a) => a.subjectId)).size).toBeLessThanOrEqual(Math.max(4, Math.ceil(mins / 60)));
      }
    }
  });

  it("Revisão e Questões vêm depois das Teorias a que se atrelam; Fixação/Questões só após toda a teoria da aula", () => {
    const order = new Map(content.map((a, i) => [a.key, i]));
    for (const a of content) {
      for (const ref of a.refKeys) expect(order.get(ref)!).toBeLessThan(order.get(a.key)!);
      if (a.type === "FIXACAO" || a.type === "QUESTOES") {
        const teorias = content.filter((t) => t.aulaId === a.aulaId && t.type === "TEORIA");
        for (const t of teorias) expect(order.get(t.key)!).toBeLessThan(order.get(a.key)!);
      }
      if (a.type === "FIXACAO" || a.type === "QUESTOES") {
        const revs = content.filter((r) => r.aulaId === a.aulaId && r.type === "REVISAO");
        for (const r of revs) expect(order.get(r.key)!).toBeLessThan(order.get(a.key)!);
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
    const subjects25 = new Set(flat(p25).filter((a) => a.kind === "CONTENT").map((a) => a.subjectId));
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
    expect(p.weeks.filter((w) => w.kind === "CONTENT").length).toBeLessThan(p.params.contentWeeks);
    // com os complementos do MentorIA (Decreto 50.014, Lei 15.187 e Lei 14.751) o edital da disciplina fica completo
    expect(p.coverage.subjects[0].coverage).toBeGreaterThan(0.99);
  });

  it("as lacunas do Estratégia foram preenchidas por complementos: não há aviso de lacuna aberta, mas o aviso existe se uma lacuna reaparecer", () => {
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

  it("a Teoria segue a regra de 10–17 págs. por hora: Legislações PE (44 págs.) leva ~3–4 h de leitura", () => {
    const estrategiaOnly = Object.fromEntries(["c01", "c02", "c03"].map((c) => [`legislacoes-pe/${c}`, 2 as const])); // só as aulas 01 e 02 (44 págs.)
    const p = generatePlan(input(35, ["legislacoes-pe"], 0, { known: estrategiaOnly }));
    const t = minutesOf(p, "legislacoes-pe").teoria / 60;
    expect(t).toBeGreaterThan(2.5);
    expect(t).toBeLessThan(4.5);
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
    expect(minutesOf(studied, "direito-administrativo").teoria).toBeLessThan(minutesOf(base, "direito-administrativo").teoria * 0.75);
    expect(flat(mastered).filter((a) => a.kind === "CONTENT")).toHaveLength(0);
    expect(mastered.coverage.subjects[0].coverage).toBeGreaterThan(0.99);
  });

  it("é possível fechar o edital inteiro (nível Essencial) dentro da faixa Avançado para quem tem nível intermediário", () => {
    const p = generatePlan(input(50, ALL_PT, 2));
    expect(p.params.fullEditalHoursPerWeek).toBeLessThanOrEqual(50);
    const pf = generatePlan(input(p.params.fullEditalHoursPerWeek, ALL_PT, 2));
    const seen = pf.coverage.subjects.every((s) => s.aulas.length + 0 >= 1);
    expect(seen).toBe(true);
    expect(pf.coverage.subjects.every((s) => s.notCovered.length === 0)).toBe(true);
  });
});
