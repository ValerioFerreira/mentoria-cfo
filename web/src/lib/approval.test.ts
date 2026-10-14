import { describe, expect, it } from "vitest";
import { PROFILES, blendProfiles, compareSubjects, compareTotal, gapStatus, profileSlug, profileWeight, profilesForContest, viewOf, type ApprovalProfile } from "./approval";

const base = { corp: "CBMPE", cargo: "oficial", banca: "x", vagas: 10, firstCallVagas: 5, classified: 20, minClassified: 30, totalQuestions: 70 } as const;
const stats = (meanPct: number, minPct: number) => ({ n: 10, mean: meanPct * 70, min: minPct * 70, max: 70, meanPct, minPct });
const prof = (id: string, year: number, relevance: number, meanPct: number, subjects?: ApprovalProfile["subjects"]): ApprovalProfile => ({
  ...base, id, label: id, year, relevance, approved: stats(meanPct, meanPct - 0.1), firstCall: stats(meanPct, meanPct), subjects,
});

describe("perfil de aprovação", () => {
  it("peso cai pela metade a cada 4 anos e pela relevância do cargo", () => {
    expect(profileWeight({ year: 2026, relevance: 1 })).toBe(1);
    expect(profileWeight({ year: 2022, relevance: 1 })).toBeCloseTo(0.5);
    expect(profileWeight({ year: 2022, relevance: 0.5 })).toBeCloseTo(0.25);
    expect(profileWeight({ year: 2030, relevance: 1 })).toBe(1); // sem peso acima de 1 para ano futuro
  });

  it("perfil ponderado dá mais peso ao concurso recente", () => {
    const novo = prof("novo", 2024, 1, 0.7);
    const velho = prof("velho", 2016, 1, 0.9);
    const v = blendProfiles([novo, velho]);
    expect(v.totalPct).toBeGreaterThan(0.7);
    expect(v.totalPct).toBeLessThan(0.8); // mais perto de 0,7 que de 0,9
    expect(v.sources.reduce((a, s) => a + s.weight, 0)).toBeCloseTo(1);
  });

  it("disciplina só entra no agregado dos concursos que a trazem", () => {
    const a = prof("a", 2024, 1, 0.7, { "lingua-portuguesa": { max: 5, mean: 4, min: 2 } });
    const b = prof("b", 2018, 1, 0.8); // só total
    const v = blendProfiles([a, b]);
    expect(v.subjects["lingua-portuguesa"]).toBeCloseTo(0.8); // 4/5, sem diluir com o concurso sem disciplina
    expect(Object.keys(v.subjects)).toEqual(["lingua-portuguesa"]);
  });

  it("inglês e espanhol viram língua estrangeira", () => {
    expect(profileSlug("lingua-inglesa")).toBe("lingua-estrangeira");
    expect(profileSlug("lingua-espanhola")).toBe("lingua-estrangeira");
    expect(profileSlug("informatica")).toBe("informatica");
  });

  it("faixas do comparativo", () => {
    expect(gapStatus(0.02)).toBe("acima");
    expect(gapStatus(0)).toBe("acima");
    expect(gapStatus(-0.05)).toBe("perto");
    expect(gapStatus(-0.2)).toBe("abaixo");
    expect(gapStatus(null)).toBe("sem-dados");
  });

  const subs = (acc: [number | null, number | null]) => [
    { id: "lingua-portuguesa", name: "", examQuestions: 5, accuracy: acc[0], projected: null, total: 20 },
    { id: "lingua-inglesa", name: "", examQuestions: 5, accuracy: acc[1], projected: null, total: 20 },
  ];
  const view = viewOf(prof("p", 2024, 1, 0.7, { "lingua-portuguesa": { max: 5, mean: 4, min: 3 }, "lingua-estrangeira": { max: 5, mean: 3, min: 1 } }));

  it("compara por disciplina em pontos percentuais e questões", () => {
    const [lp, le] = compareSubjects(subs([0.6, 0.7]), view);
    expect(lp).toMatchObject({ approved: 0.8, status: "abaixo" });
    expect(lp.gapQuestions).toBeCloseTo(-1);
    expect(le).toMatchObject({ approved: 0.6, status: "acima" }); // inglês casa com língua estrangeira
  });

  it("disciplina sem dados do aluno ou sem dado no concurso fica sem comparação", () => {
    const [lp, le] = compareSubjects(subs([null, 0.7]), viewOf(prof("q", 2024, 1, 0.7, { "lingua-portuguesa": { max: 5, mean: 4, min: 3 } })));
    expect(lp.status).toBe("sem-dados");
    expect(le).toMatchObject({ approved: null, status: "sem-dados" });
  });

  it("total: completo quando todas as disciplinas foram medidas, parcial caso contrário", () => {
    const full = compareTotal(compareSubjects(subs([0.6, 0.7]), view), view);
    expect(full.scope).toBe("total");
    expect(full.userQuestions).toBeCloseTo(6.5);
    expect(full.approvedSameScope).toBeCloseTo(7);
    expect(full.approvedQuestions).toBeCloseTo(49);
    const part = compareTotal(compareSubjects(subs([0.6, null]), view), view);
    expect(part).toMatchObject({ scope: "parcial", measured: 1, of: 2 });
    expect(compareTotal(compareSubjects(subs([null, null]), view), view).scope).toBe("sem-dados");
  });

  it("concurso só com total: compara o total estimado do aluno quando todas as disciplinas foram medidas", () => {
    const soTotal = viewOf(prof("t", 2018, 1, 0.8)); // 80% de 70 = 56
    const completo = compareTotal(compareSubjects(subs([0.6, 0.7]), soTotal), soTotal);
    expect(completo).toMatchObject({ scope: "total", approvedSameScope: 56 });
    expect(completo.userQuestions).toBeCloseTo(6.5);
    expect(compareTotal(compareSubjects(subs([0.6, null]), soTotal), soTotal)).toMatchObject({ scope: "sem-dados", userQuestions: null, measured: 1 });
  });

  it("os perfis gerados são coerentes", () => {
    expect(PROFILES.length).toBeGreaterThanOrEqual(6);
    for (const p of PROFILES) {
      expect(p.approved.min).toBeLessThanOrEqual(p.approved.mean);
      expect(p.approved.mean).toBeLessThanOrEqual(p.totalQuestions);
      expect(p.approved.n).toBeLessThanOrEqual(p.vagas);
      expect(p.firstCall.min).toBeGreaterThanOrEqual(p.approved.min); // 1ª chamada é o topo da lista
      // nenhum nome ou inscrição vazou para o arquivo
      expect(JSON.stringify(p)).not.toMatch(/\d{6,}/);
    }
    expect(blendProfiles(PROFILES).totalPct).toBeGreaterThan(0.6);
  });

  it("os perfis de referência são os concursos anteriores do mesmo órgão e cargo do aluno", () => {
    expect(profilesForContest("CBMPE_OFICIAL").map((p) => p.id)).toEqual(["cbmpe-oficial-2024", "cfo-cbmpe-2018"]);
    expect(profilesForContest("CBMPE_SOLDADO").every((p) => p.corp === "CBMPE" && p.cargo === "praca")).toBe(true);
    expect(profilesForContest("PMPE_OFICIAL").every((p) => p.corp === "PMPE" && p.cargo === "oficial")).toBe(true);
    expect(profilesForContest("PMPE_SOLDADO").every((p) => p.corp === "PMPE" && p.cargo === "praca")).toBe(true);
    expect(profilesForContest("PCPE_AGENTE")).toEqual([]);
  });
});
