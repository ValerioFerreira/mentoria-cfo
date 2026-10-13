import { describe, expect, it } from "vitest";
import {
  bundleSegments, buildBlueprint, clampMinutes, fixacaoMinutes, pickFixChunks, questoesMinutes, quizConfig, reviewGroupFor, revisaoMinutes, summaryMinutes, summaryShape, withSummaryUnit,
  splitEven, teoriaMinutes, tierMinutes, tierShape, type AulaBlueprint,
} from "./blueprint";
import { mkAula, mkSeg } from "./testkit";
import type { Level } from "./types";

const segs = (n: number, pages = 12, load = 12) => Array.from({ length: n }, (_, i) => mkSeg("d/a01", i + 1, pages, load, 1 + i * pages));
const bp = (n: number, opts: { level?: Level; known?: 0 | 1 | 2; pages?: number; load?: number; runs?: [number, number][]; links?: { startPage: number; endPage: number; sourceAula: string }[] } = {}): AulaBlueprint =>
  buildBlueprint(
    mkAula("d/a01", 1, { commentedRuns: opts.runs ?? [], practiceLinks: (opts.links ?? []).map((l) => ({ theme: "t", ...l })) }),
    segs(n, opts.pages, opts.load),
    opts.level ?? 0,
    opts.known ?? 0,
  );

describe("clampMinutes", () => {
  it("arredonda para múltiplos de 5 e limita à faixa informada", () => {
    expect(clampMinutes(0, 50, 80)).toBe(50);
    expect(clampMinutes(49, 50, 80)).toBe(50);
    expect(clampMinutes(53, 50, 80)).toBe(55);
    expect(clampMinutes(57.4, 50, 80)).toBe(55);
    expect(clampMinutes(57.5, 50, 80)).toBe(60);
    expect(clampMinutes(95, 50, 80)).toBe(80);
    expect(clampMinutes(10, 25, 35)).toBe(25);
  });
  it("é monotônico e sempre múltiplo de 5", () => {
    let prev = 30;
    for (let m = 0; m <= 200; m += 0.5) {
      const r = clampMinutes(m, 30, 60);
      expect(r % 5).toBe(0);
      expect(r).toBeGreaterThanOrEqual(prev);
      prev = r;
    }
  });
});

describe("bundleSegments", () => {
  it("trechos de tamanho normal ficam separados e na ordem", () => {
    const u = bundleSegments([mkSeg("a", 2, 12, 12, 13), mkSeg("a", 1, 12, 12, 1)]);
    expect(u.map((x) => x.segmentIds)).toEqual([["a/s01"], ["a/s02"]]);
  });
  it("junta trechos muito curtos até chegar a 8 páginas, sem passar de 17", () => {
    const u = bundleSegments([mkSeg("a", 1, 3, 3), mkSeg("a", 2, 3, 3), mkSeg("a", 3, 3, 3), mkSeg("a", 4, 3, 3)]);
    // 3+3+3 = 9 (>= 8) fecha a unidade; o quarto (cauda curta) é absorvido por ela
    expect(u).toHaveLength(1);
    expect(u[0].pages).toBe(12);
    expect(u[0].segmentIds).toHaveLength(4);
    for (const x of u) expect(x.pages).toBeLessThanOrEqual(17);
  });
  it("a cauda curta é absorvida só se couber no teto de páginas", () => {
    const u = bundleSegments([mkSeg("a", 1, 16, 12), mkSeg("a", 2, 3, 3)]);
    expect(u.map((x) => x.pages)).toEqual([16, 3]); // 16 + 3 > 17
  });
  it("não junta se a carga passar do limite", () => {
    const u = bundleSegments([mkSeg("a", 1, 5, 14), mkSeg("a", 2, 5, 14)]);
    expect(u).toHaveLength(2);
  });
  it("lista vazia e um único trecho", () => {
    expect(bundleSegments([])).toEqual([]);
    expect(bundleSegments([mkSeg("a", 1, 4, 4)])).toHaveLength(1);
  });
  it("conserva todas as páginas e todos os trechos", () => {
    const input = Array.from({ length: 11 }, (_, i) => mkSeg("a", i + 1, 2 + (i % 7) * 2, 3 + (i % 5) * 3));
    const u = bundleSegments(input);
    expect(u.flatMap((x) => x.segmentIds).sort()).toEqual(input.map((s) => s.id).sort());
    expect(u.reduce((n, x) => n + x.pages, 0)).toBe(input.reduce((n, s) => n + s.pages, 0));
    for (const x of u) expect(x.pages).toBeLessThanOrEqual(17);
  });
});

describe("buildBlueprint", () => {
  it("ritmo por nível e agrupamento de revisão", () => {
    expect([0, 1, 2, 3].map((l) => bp(2, { level: l as Level }).pace)).toEqual([1, 0.9, 0.8, 0.7]);
    expect([0, 1, 2, 3].map((l) => reviewGroupFor(l as Level))).toEqual([2, 3, 3, 4]);
  });
  it("'já estudei' multiplica o ritmo de leitura por 0,75; 'nunca estudei' não muda", () => {
    expect(bp(2, { level: 0, known: 1 }).readPace).toBeCloseTo(0.75);
    expect(bp(2, { level: 2, known: 1 }).readPace).toBeCloseTo(0.8 * 0.75);
    expect(bp(2, { level: 2, known: 0 }).readPace).toBe(0.8);
    // a prática (Fixação/Questões) usa só o ritmo do nível
    expect(bp(2, { level: 2, known: 1 }).pace).toBe(0.8);
  });
  it("faixas de Fixação juntam as questões comentadas da aula e as de aulas de prática vinculadas", () => {
    const b = bp(2, { runs: [[30, 41]], links: [{ startPage: 5, endPage: 9, sourceAula: "p/a14" }] });
    expect(b.fixRanges).toEqual([{ start: 30, end: 41 }, { start: 5, end: 9, sourceAula: "p/a14" }]);
    expect(b.fixPages).toBe(12 + 5);
    expect(b.fixChunksFull).toBe(2); // ceil(17 / 12)
  });
  it("sem questões comentadas não há Fixação", () => {
    const b = bp(2);
    expect(b.fixPages).toBe(0);
    expect(b.fixChunksFull).toBe(0);
  });
});

describe("minutos de cada atividade", () => {
  const u = (load: number, ids = 1, pages = 12) => ({ segmentIds: Array.from({ length: ids }, (_, i) => `s${i}`), pages, load });
  it("Teoria: 60 min para carga 12, com piso de 50 e teto de 80 antes do ritmo", () => {
    const b = bp(1);
    expect(teoriaMinutes(u(12), b)).toBe(60);
    expect(teoriaMinutes(u(6), b)).toBe(50);
    expect(teoriaMinutes(u(1), b)).toBe(50);
    expect(teoriaMinutes(u(15), b)).toBe(75);
    expect(teoriaMinutes(u(40), b)).toBe(80);
  });
  it("Teoria curta (menos de 8 págs.) pode durar a partir de 35 min", () => {
    expect(teoriaMinutes(u(3, 1, 5), bp(1))).toBe(35);
    expect(teoriaMinutes(u(8, 1, 7), bp(1))).toBe(40);
    expect(teoriaMinutes(u(3, 1, 8), bp(1))).toBe(50); // 8 págs. já não é curta
  });
  it("Teoria: cada nível encurta o tempo com piso de 50 min e teto de 80 min", () => {
    expect(teoriaMinutes(u(12), bp(1, { level: 1 }))).toBe(55); // 54 → 55
    expect(teoriaMinutes(u(12), bp(1, { level: 2 }))).toBe(50); // piso 50
    expect(teoriaMinutes(u(12), bp(1, { level: 3 }))).toBe(50); // piso 50
    expect(teoriaMinutes(u(12), bp(1, { level: 0, known: 1 }))).toBe(50); // piso 50
  });
  it("Teoria nunca sai de 35–80 min nem da grade de 5 min, para qualquer carga, páginas e nível", () => {
    for (const level of [0, 1, 2, 3] as Level[])
      for (const known of [0, 1] as const)
        for (let load = 0; load <= 40; load++)
          for (const pages of [3, 7, 8, 17]) {
            const m = teoriaMinutes(u(load, 1, pages), bp(1, { level, known }));
            expect(m).toBeGreaterThanOrEqual(pages < 8 ? 35 : 50);
            expect(m).toBeLessThanOrEqual(80);
            expect(m % 5).toBe(0);
          }
  });
  it("Resumo analítico (Turbo): ~20 min por unidade, até 15 min para quem lê mais rápido", () => {
    expect(summaryMinutes(bp(1))).toBe(20);
    expect(summaryMinutes(bp(1, { level: 1 }))).toBe(20); // 18 → 20
    expect(summaryMinutes({ readPace: 0.6 })).toBe(15); // piso
    expect(summaryMinutes(bp(1, { level: 0, known: 1 }))).toBe(15);
  });
  it("Revisão: 30 a 60 min", () => {
    const b = bp(1);
    expect([1, 2, 3, 4, 5].map((n) => revisaoMinutes(n, b))).toEqual([35, 45, 55, 60, 60]);
  });
  it("Revisão reduzida (Turbo): metade do tempo, entre 25 e 35 min", () => {
    const b = bp(1);
    expect([1, 2, 3, 4, 5].map((n) => revisaoMinutes(n, b, true))).toEqual([25, 25, 30, 30, 30]);
  });
  it("Fixação: 60 min vezes o ritmo, entre 40 e 60 min (reduzida: 30 min)", () => {
    expect([0, 1, 2, 3].map((l) => fixacaoMinutes(bp(1, { level: l as Level })))).toEqual([60, 55, 50, 40]);
    expect(fixacaoMinutes(bp(1), true)).toBe(30);
  });
  it("Questões: 60 min com piso de 50 min (reduzidas: caderno de 15 questões em 40 min)", () => {
    expect([0, 1, 2, 3].map((l) => questoesMinutes(bp(1, { level: l as Level })))).toEqual([60, 55, 50, 50]);
    expect(questoesMinutes(bp(1), true)).toBe(40);
    expect(quizConfig()).toEqual({ questions: 25, limitSeconds: 3600, mixed: false });
    expect(quizConfig(true)).toEqual({ questions: 15, limitSeconds: 2400, mixed: false });
  });
});

describe("tierShape", () => {
  it("Mínimo: toda aula com Teoria tem Revisão curta, 1 h de Fixação (se há questões comentadas) e cadernos (1 por até 4 Teorias)", () => {
    for (const n of [1, 3, 4, 5, 6, 9, 16]) {
      const s = tierShape(bp(n, { runs: [[1, 40]] }), 1);
      expect(s.reviews).toBe(Math.ceil(n / 4));
      expect(s.fixChunks).toBe(1);
      expect(s.quizzes).toBe(Math.ceil(n / 4));
    }
    expect(tierShape(bp(3), 1).fixChunks).toBe(0); // sem questões comentadas não há Fixação
  });
  it("Completo acrescenta Revisões no agrupamento do nível (2 a 4 Teorias), mais Fixação (1 a 4 h) e cadernos", () => {
    const b = bp(6, { level: 0, runs: [[1, 48]] }); // 48 págs. de questões = 4 h de Fixação
    expect(b.fixChunksFull).toBe(4);
    expect(tierShape(b, 2)).toEqual({ reviews: 3, fixChunks: 1, quizzes: 2 }); // ceil(6/2); round(4*.35)=1; ceil(6/3)
    expect(tierShape(bp(6, { level: 3, runs: [[1, 48]] }), 2).reviews).toBe(2); // ceil(6/4)
  });
  it("Aprofundamento: Fixação até 10 h e dois terços das Teorias em cadernos", () => {
    const b = bp(6, { runs: [[1, 240]] }); // 20 h possíveis
    expect(tierShape(b, 3)).toEqual({ reviews: 3, fixChunks: 10, quizzes: 4 });
    expect(tierShape(bp(6, { runs: [[1, 24]] }), 3).fixChunks).toBe(2); // não passa do que existe
  });
  it("aula sem Teoria não tem Revisão nem caderno, só Fixação se houver questões comentadas", () => {
    const s = tierShape(bp(0, { runs: [[1, 24]] }), 3);
    expect(s).toEqual({ reviews: 0, fixChunks: 2, quizzes: 0 });
  });
  it("unidades em resumo saem do ciclo da aula: o ciclo normal só vê as unidades lidas no material", () => {
    const b = bp(6, { runs: [[1, 48]] });
    const mixed = withSummaryUnit(withSummaryUnit(b, b.teoria[0]), b.teoria[1]); // 4 normais + 2 em resumo
    expect(mixed.teoria).toHaveLength(4);
    expect(mixed.summary).toHaveLength(2);
    expect(tierShape(mixed, 1)).toEqual(tierShape(bp(4, { runs: [[1, 48]] }), 1));
    // aula inteira em resumo: o ciclo (Revisão, Fixação, Questões) passa para o bloco do Turbo
    let all = b;
    for (const u of b.teoria) all = withSummaryUnit(all, u);
    expect(all.teoria).toHaveLength(0);
    expect(tierShape(all, 3)).toEqual({ reviews: 0, fixChunks: 0, quizzes: 0 });
  });
  it("resumos: caderno curto já no mínimo (1 por 6 unidades); Revisão (metade do tempo) na camada 2; Fixação reduzida na 3", () => {
    let b = bp(6, { runs: [[1, 48]] });
    for (const u of [...b.teoria]) b = withSummaryUnit(b, u);
    expect(summaryShape(b, 1)).toEqual({ reviews: 0, fixChunks: 0, quizzes: 1 });
    expect(summaryShape(b, 2).reviews).toBeCloseTo(6 / 9);
    expect(summaryShape(b, 2).fixChunks).toBe(0);
    expect(summaryShape(b, 3).fixChunks).toBe(1);
    expect(summaryShape(bp(3), 3)).toEqual({ reviews: 0, fixChunks: 0, quizzes: 0 }); // sem resumos
  });
  it("trocar unidades por resumo custa bem menos que o ciclo mínimo normal e mantém os cadernos", () => {
    const normal = bp(6, { runs: [[1, 48]] });
    let turbo = normal;
    for (const u of [...normal.teoria]) turbo = withSummaryUnit(turbo, u);
    expect(tierMinutes(turbo, 1).total).toBeLessThan(tierMinutes(normal, 1).total * 0.5);
    expect(tierMinutes(turbo, 1).questoes).toBeGreaterThan(0);
    expect(tierMinutes(turbo, 1).teoria).toBe(6 * 20);
  });
  it("as camadas são cumulativas: Mínimo ≤ Completo ≤ Aprofundamento em minutos (também com unidades em resumo)", () => {
    for (const n of [1, 2, 4, 7, 12]) {
      for (const level of [0, 1, 2, 3] as Level[]) {
        for (const converted of [0, 1, 3]) {
          let b = bp(n, { level, runs: [[1, 36]] });
          for (const u of b.teoria.slice(0, converted)) b = withSummaryUnit(b, u);
          const t = [1, 2, 3].map((tier) => tierMinutes(b, tier as 1 | 2 | 3).total);
          expect(t[0]).toBeLessThanOrEqual(t[1]);
          expect(t[1]).toBeLessThanOrEqual(t[2]);
        }
      }
    }
  });
  it("tierMinutes soma as partes", () => {
    const m = tierMinutes(bp(6, { runs: [[1, 48]] }), 2);
    expect(m.total).toBe(m.teoria + m.revisao + m.fixacao + m.questoes);
    expect(m.teoria).toBe(6 * 60);
  });
});

describe("splitEven", () => {
  it("divide em blocos contíguos e o mais iguais possível", () => {
    expect(splitEven(7, 3)).toEqual([[0, 1, 2], [3, 4], [5, 6]]);
    expect(splitEven(6, 3)).toEqual([[0, 1], [2, 3], [4, 5]]);
    expect(splitEven(1, 1)).toEqual([[0]]);
  });
  it("mais grupos que itens: descarta os vazios", () => {
    expect(splitEven(2, 5)).toEqual([[0], [1]]);
    expect(splitEven(0, 3)).toEqual([]);
  });
  it("zero grupos devolve vazio", () => {
    expect(splitEven(5, 0)).toEqual([]);
  });
  it("cobre todos os índices exatamente uma vez", () => {
    for (let n = 0; n < 15; n++)
      for (let g = 0; g < 8; g++) {
        const flat = splitEven(n, g).flat();
        expect(flat).toEqual(g === 0 ? [] : Array.from({ length: n }, (_, i) => i));
      }
  });
});

describe("pickFixChunks", () => {
  it("corta em blocos de 12 páginas preservando a origem de cada faixa", () => {
    const b = bp(1, { runs: [[10, 21]], links: [{ startPage: 1, endPage: 6, sourceAula: "p/a14" }] });
    const chunks = pickFixChunks(b, 5);
    expect(chunks).toEqual([[{ start: 10, end: 21 }], [{ start: 1, end: 6, sourceAula: "p/a14" }]]);
  });
  it("um bloco que atravessa duas faixas separa as faixas", () => {
    const b = bp(1, { runs: [[1, 8]], links: [{ startPage: 20, endPage: 27, sourceAula: "p/a14" }] });
    const chunks = pickFixChunks(b, 9);
    expect(chunks[0]).toEqual([{ start: 1, end: 8 }, { start: 20, end: 23, sourceAula: "p/a14" }]);
    expect(chunks[1]).toEqual([{ start: 24, end: 27, sourceAula: "p/a14" }]);
  });
  it("quando pedem menos blocos que o total, espalha pelo começo, meio e fim", () => {
    const b = bp(1, { runs: [[1, 60]] }); // 5 blocos
    expect(pickFixChunks(b, 1)).toEqual([[{ start: 1, end: 12 }]]);
    expect(pickFixChunks(b, 2).map((c) => c[0].start)).toEqual([1, 49]);
    expect(pickFixChunks(b, 3).map((c) => c[0].start)).toEqual([1, 25, 49]);
  });
  it("sem faixas não há blocos; pedir zero devolve vazio", () => {
    expect(pickFixChunks(bp(1), 3)).toEqual([]);
    expect(pickFixChunks(bp(1, { runs: [[1, 24]] }), 0)).toEqual([]);
  });
  it("cada página aparece uma vez só quando todos os blocos são pedidos", () => {
    const b = bp(1, { runs: [[3, 17], [30, 52]] });
    const pages = pickFixChunks(b, 99).flatMap((c) => c.flatMap((r) => Array.from({ length: r.end - r.start + 1 }, (_, i) => r.start + i)));
    expect(pages).toHaveLength(b.fixPages);
    expect(new Set(pages).size).toBe(b.fixPages);
  });
});
