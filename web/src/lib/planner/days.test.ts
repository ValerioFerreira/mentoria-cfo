import { describe, expect, it } from "vitest";
import { assignDays, toChunks, weekFraction, type SubjectWeekLoad } from "./days";
import { DAY_WEIGHTS, FAMILY, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import { mkAct } from "./testkit";
import type { PlannedActivity } from "./types";

/** Ciclo Teoria×n → Revisão (atrelada às n Teorias) de uma disciplina. */
function cycle(subjectId: string, groups: number, perGroup = 3, teoriaMin = 60): PlannedActivity[] {
  const out: PlannedActivity[] = [];
  for (let g = 0; g < groups; g++) {
    const keys: string[] = [];
    for (let i = 0; i < perGroup; i++) {
      const key = `${subjectId}#T${g * perGroup + i + 1}`;
      keys.push(key);
      out.push(mkAct(key, "TEORIA", subjectId, teoriaMin));
    }
    out.push(mkAct(`${subjectId}#R${g + 1}`, "REVISAO", subjectId, 45, { refKeys: keys }));
  }
  return out;
}
const load = (subjectId: string, activities: PlannedActivity[], sortOrder = 1): SubjectWeekLoad => ({ subjectId, sortOrder, activities });

describe("weekFraction", () => {
  it("1 para a semana inteira e decresce até o domingo leve", () => {
    expect(weekFraction(0)).toBe(1);
    const total = DAY_WEIGHTS.reduce((a, b) => a + b, 0);
    expect(weekFraction(6)).toBeCloseTo(0.45 / total);
    expect(weekFraction(3)).toBeCloseTo((1 + 1 + 1 + 0.45) / total);
    for (let d = 1; d <= 6; d++) expect(weekFraction(d)).toBeLessThan(weekFraction(d - 1));
  });
  it("valores fora do intervalo são limitados a 0–6", () => {
    expect(weekFraction(-3)).toBe(1);
    expect(weekFraction(10)).toBe(weekFraction(6));
  });
});

describe("toChunks (sessões de estudo da disciplina)", () => {
  it("corta em sessões de até ~2h30 mantendo a ordem e sem perder atividades", () => {
    const acts = Array.from({ length: 8 }, (_, i) => mkAct(`a#T${i}`, "TEORIA", "a", 60));
    const chunks = toChunks(load("a", acts));
    expect(chunks.flatMap((c) => c.acts.map((a) => a.key))).toEqual(acts.map((a) => a.key));
    for (const c of chunks) expect(c.minutes).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
    expect(chunks.length).toBeGreaterThanOrEqual(4);
  });
  it("uma Revisão nunca cai na mesma sessão da Teoria que ela revê", () => {
    const chunks = toChunks(load("a", cycle("a", 2, 2, 30)));
    for (const c of chunks) {
      const keys = new Set(c.acts.map((a) => a.key));
      for (const a of c.acts) if (a.type === "REVISAO") for (const k of a.refKeys) expect(keys.has(k), `${a.key} com ${k}`).toBe(false);
    }
  });
  it("no máximo 7 sessões (uma por dia da semana), mesmo com carga enorme", () => {
    const acts = Array.from({ length: 40 }, (_, i) => mkAct(`a#T${i}`, "TEORIA", "a", 60));
    const chunks = toChunks(load("a", acts));
    expect(chunks.length).toBeLessThanOrEqual(7);
    expect(chunks.flatMap((c) => c.acts)).toHaveLength(40);
    expect(toChunks(load("a", acts), 4).length).toBeLessThanOrEqual(4);
  });
  it("metadados: família, posição relativa e perfil de prática", () => {
    const acts = [mkAct("direito-penal-militar#F1", "FIXACAO", "direito-penal-militar", 60), mkAct("direito-penal-militar#Q1", "QUESTOES", "direito-penal-militar", 60)];
    const [c] = toChunks(load("direito-penal-militar", acts));
    expect(c.family).toBe(FAMILY["direito-penal-militar"]);
    expect(c.practiceOnly).toBe(true);
    expect(c.retrievalOnly).toBe(false); // Fixação é prática, mas não é recuperação (Revisão/Questões)
    expect(toChunks(load("a", [mkAct("a#R", "REVISAO", "a", 30), mkAct("a#Q", "QUESTOES", "a", 30)]))[0].retrievalOnly).toBe(true);
    expect(c.pos).toBe(0);
    expect(c.count).toBe(1);
    expect(toChunks(load("zzz-desconhecida", [mkAct("x", "TEORIA", "zzz", 30)]))[0].family).toBe("OUTRA");
  });
  it("uma disciplina só com Teoria não é prática nem recuperação", () => {
    const [c] = toChunks(load("a", [mkAct("a#T1", "TEORIA", "a", 60)]));
    expect(c.practiceOnly).toBe(false);
    expect(c.retrievalOnly).toBe(false);
    expect(c.firstIsReview).toBe(false);
  });
});

describe("assignDays", () => {
  const SUBJECTS = ["lingua-portuguesa", "matematica", "direito-constitucional", "biologia"];
  const week = () => SUBJECTS.map((id, i) => load(id, cycle(id, 2, 2, 45), i + 1));

  it("sem carga não há atividades", () => {
    expect(assignDays([], 600)).toEqual([]);
    expect(assignDays([load("a", [])], 600)).toEqual([]);
  });
  it("não perde nem duplica nenhuma atividade e todas recebem dia 0–6", () => {
    const loads = week();
    const input = loads.flatMap((l) => l.activities.map((a) => a.key)).sort();
    const out = assignDays(loads, 1500);
    expect(out.map((a) => a.key).sort()).toEqual(input);
    for (const a of out) {
      expect(a.day).toBeGreaterThanOrEqual(0);
      expect(a.day).toBeLessThanOrEqual(6);
    }
  });
  it("a lista devolvida está em ordem crescente de dia", () => {
    const days = assignDays(week(), 1500).map((a) => a.day!);
    expect(days).toEqual([...days].sort((a, b) => a - b));
  });
  it("dentro de cada disciplina, a ordem do ciclo é preservada", () => {
    const loads = week();
    const out = assignDays(loads, 1500);
    for (const l of loads) expect(out.filter((a) => a.subjectId === l.subjectId).map((a) => a.key)).toEqual(l.activities.map((a) => a.key));
  });
  it("a Revisão cai em dia posterior ao de todas as Teorias que ela revê", () => {
    const out = assignDays(week(), 1500);
    const dayOf = new Map(out.map((a) => [a.key, a.day!]));
    for (const a of out) if (a.type === "REVISAO") for (const k of a.refKeys) expect(dayOf.get(a.key)!, `${a.key} x ${k}`).toBeGreaterThan(dayOf.get(k)!);
  });
  it("com firstDay, nada cai antes do dia de início", () => {
    for (const firstDay of [1, 2, 4, 5]) {
      const out = assignDays(week().map((l) => ({ ...l, activities: l.activities.slice(0, 4) })), 600, firstDay);
      expect(out.length).toBeGreaterThan(0);
      expect(Math.min(...out.map((a) => a.day!))).toBeGreaterThanOrEqual(firstDay);
    }
  });
  it("começando no domingo, tudo cai no domingo", () => {
    const out = assignDays([load("a", [mkAct("a#1", "TEORIA", "a", 60), mkAct("a#2", "TEORIA", "a", 60)])], 120, 6);
    expect(out.map((a) => a.day)).toEqual([6, 6]);
  });
  it("uma disciplina com poucas atividades se espalha por dias diferentes (prática distribuída)", () => {
    const acts = Array.from({ length: 6 }, (_, i) => mkAct(`a#T${i}`, "TEORIA", "a", 60));
    const out = assignDays([load("a", acts)], 360);
    expect(new Set(out.map((a) => a.day)).size).toBeGreaterThanOrEqual(3);
  });
  it("não coloca duas sessões da mesma disciplina no mesmo dia quando há dias de sobra", () => {
    const acts = Array.from({ length: 6 }, (_, i) => mkAct(`a#T${i}`, "TEORIA", "a", 90));
    const out = assignDays([load("a", acts)], 540);
    const sessions = new Map<number, number>();
    // sessões = grupos contíguos no mesmo dia; com 6 × 90 min (limite ~150 por sessão) cada dia comporta uma só sessão
    for (const a of out) sessions.set(a.day!, (sessions.get(a.day!) ?? 0) + a.minutes);
    for (const m of sessions.values()) expect(m).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY + 60);
  });
  it("carga leve fica concentrada nos primeiros dias e o domingo é o mais leve em semana cheia", () => {
    const loads = ["lingua-portuguesa", "matematica", "direito-constitucional", "biologia", "quimica", "informatica"].map((id, i) => load(id, cycle(id, 3, 2, 45), i + 1));
    const out = assignDays(loads, 2000);
    const minutes = Array.from({ length: 7 }, (_, d) => out.filter((a) => a.day === d).reduce((n, a) => n + a.minutes, 0));
    expect(minutes[6]).toBeLessThan(Math.max(...minutes.slice(0, 6)));
  });
  it("é determinístico", () => {
    expect(assignDays(week(), 1500)).toEqual(assignDays(week(), 1500));
  });
});
