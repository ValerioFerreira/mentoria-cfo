import { describe, expect, it } from "vitest";
import {
  aulaLabel, fixacaoMentoria, fixacaoSteps, materialHref, pageLabel, pageRangeLocation, revisaoMentoria, teoriaDirective, teoriaMentoria, teoriaStep,
  turboDirective, turboMentoriaStep, withAnchor, type AulaRef, type SegmentAnchor, type MaterialChapter, type SegmentRef,
} from "./directive";

const seg = (over: Partial<SegmentRef> = {}): SegmentRef => ({
  id: "x/a02/s01", startPage: 12, endPage: 24, startPrinted: 12, endPrinted: 24,
  startTopic: "Comparativos", startsMidTopic: false, stopBeforeTopic: "Superlativos",
  endsMidTopic: false, endTopic: "Comparativos", endsTheory: false, ...over,
});
const aula: AulaRef = { id: "x/a02", number: 2, shortTitle: "Adjetivos e Advérbios", subjectName: "Língua Inglesa", printedOffset: 0 };

describe("diretriz de Teoria", () => {
  it("diz início, fim e o tópico em que parar", () => {
    expect(teoriaStep(seg())).toBe("Comece na pág. 12, no tópico “Comparativos”, e estude até a pág. 24, parando antes do tópico “Superlativos” (se ele começar no meio da pág. 25, leia também a parte da pág. 25 que vem antes do título).");
  });
  it("mostra a página impressa quando difere da do PDF", () => {
    expect(pageLabel(12, 11)).toBe("pág. 12 (impressa 11)");
    expect(pageLabel(12, 12)).toBe("pág. 12");
    expect(pageLabel(12, null)).toBe("pág. 12");
  });
  it("corte no meio de tópico avisa que continua na próxima atividade", () => {
    const s = teoriaStep(seg({ stopBeforeTopic: null, endsMidTopic: true, endTopic: "Superlativos" }));
    expect(s).toContain("ainda estará dentro de “Superlativos”");
  });
  it("último trecho encerra a teoria; trecho que começa no meio de tópico diz que continua", () => {
    expect(teoriaStep(seg({ stopBeforeTopic: null, endsTheory: true }))).toContain("encerra a teoria desta aula");
    expect(teoriaStep(seg({ startsMidTopic: true }))).toMatch(/^Continue na pág\. 12, dentro do tópico/);
  });
  it("junta vários segmentos em ordem de página e soma as páginas", () => {
    const d = teoriaDirective(aula, [seg({ startPage: 30, endPage: 35 }), seg()]);
    expect(d.steps).toHaveLength(2);
    expect(d.steps[0]).toContain("pág. 12");
    expect(d.pages).toBe(13 + 6);
    expect(d.heading).toBe("Língua Inglesa · Aula 02 — Adjetivos e Advérbios");
  });
  it("rótulo da aula tem número com dois dígitos", () => {
    expect(aulaLabel(aula)).toBe("Aula 02 — Adjetivos e Advérbios");
  });
});

describe("diretriz de Fixação", () => {
  it("aponta as páginas da própria aula e de aulas de prática vinculadas", () => {
    const steps = fixacaoSteps(aula, [{ start: 40, end: 51 }, { start: 4, end: 8, sourceAula: "p/a14" }], () => "Aula 14 (extra)");
    expect(steps[0]).toContain("págs. 40 a 51 desta aula");
    expect(steps[0]).toContain("págs. 4 a 8 da Aula 14 (extra)");
  });
});

describe("diretriz de Modo Turbo e localização de páginas", () => {
  it("formata intervalo como 'da pág. X à pág. Y' e página única como 'na pág. X'", () => {
    expect(pageRangeLocation(5, null, 62, null)).toBe("da pág. 5 à pág. 62");
    expect(pageRangeLocation(5, 4, 62, 61)).toBe("da pág. 5 (impressa 4) à pág. 62 (impressa 61)");
    expect(pageRangeLocation(10, null, 10, null)).toBe("na pág. 10");

    const t = turboDirective(aula, [
      seg({ startPage: 5, endPage: 20, startPrinted: null, endPrinted: null }),
      seg({ startPage: 21, endPage: 62, startPrinted: null, endPrinted: null }),
    ]);
    expect(t.steps[0]).toContain("Modo Turbo");
    expect(t.steps[0]).toContain("resumo analítico");
    expect(t.steps[1]).toContain("Bizu");
    expect(t.steps[2]).toContain("Meu resumo");
    expect(t.steps[3]).toContain("está da pág. 5 à pág. 62 (Aula 02 — Adjetivos e Advérbios)");
    expect(t.pages).toBe(0);
    expect(turboDirective(aula, [seg()], 20).steps[0]).toContain("≈ 20 min");
  });
});



const ch = (over: Partial<MaterialChapter> = {}): MaterialChapter => ({
  trecho: "dpm/a00/s01", volumeId: "direito-penal-militar/m01", volumeNumber: 1, volumeTitle: "Aplicação da lei penal militar",
  subjectName: "Direito Penal Militar", chapter: 1, title: "Crime militar", start: 4, end: 15, mapPage: 14, reviewPage: 50,
  questions: { pagina: 40, ate: 42 }, ...over,
});

describe("diretriz pelo material próprio MentorIA", () => {
  it("Teoria: volume, capítulo, páginas e o Mapa do capítulo", () => {
    const [b] = teoriaMentoria([ch(), ch({ trecho: "dpm/a00/s02", chapter: 2, title: "Tempo do crime", start: 16, end: 26, mapPage: 26 })]);
    expect(b.heading).toBe("Direito Penal Militar · Material MentorIA · Volume 01");
    expect(b.pages).toBe(12 + 11);
    expect(b.steps[0]).toContain("capítulo 1, “Crime militar”, da pág. 4 à pág. 15");
    expect(b.steps[0]).toContain("“Mapa do capítulo” (pág. 14)");
    expect(materialHref(b, b.firstPage)).toBe("/material/direito-penal-militar/m01#page=4");
  });
  it("separa capítulos de volumes diferentes", () => {
    expect(teoriaMentoria([ch(), ch({ volumeId: "direito-penal-militar/m02", volumeNumber: 2, chapter: 1 })])).toHaveLength(2);
  });
  it("Turbo, Revisão e Fixação apontam as páginas certas", () => {
    expect(turboMentoriaStep([ch()])).toContain("Volume 01, págs. 4 a 15");
    expect(revisaoMentoria([ch()])[0]).toBe("Volume 01 · capítulo 1, “Crime militar”: Mapa do capítulo na pág. 14; resumo no Mapa de revisão do volume, pág. 50.");
    expect(fixacaoMentoria([ch()])[0]).toContain("capítulo 1 (págs. 40 a 42)");
    expect(fixacaoMentoria([ch({ questions: null })])).toEqual([]);
  });
});

describe("withAnchor: o texto e as páginas vêm do que está impresso", () => {
  const anchor = (over: Partial<SegmentAnchor> = {}): SegmentAnchor => ({
    start: { kind: "heading", text: "Adjetivo" }, stop: { kind: "heading", text: "Advérbio" },
    startPage: 18, endPage: 34, startPrinted: 17, endPrinted: 33, ...over,
  });

  it("troca páginas e rótulos pelos cabeçalhos reais", () => {
    const t = teoriaStep(withAnchor(seg(), anchor()));
    expect(t).toContain("Comece na pág. 18 (impressa 17), no tópico “Adjetivo”");
    expect(t).toContain("estude até a pág. 34 (impressa 33)");
    expect(t).toContain("parando antes do tópico “Advérbio”");
    expect(t).not.toContain("Comparativos");
  });

  it("início dentro de um tópico, término dentro de outro e página que abre sem cabeçalho", () => {
    const a = anchor({ start: { kind: "inside", text: "Adjetivo" }, stop: { kind: "inside", text: "Grau" } });
    const t = teoriaStep(withAnchor(seg(), a));
    expect(t).toContain("Continue na pág. 18 (impressa 17), dentro do tópico “Adjetivo”");
    expect(t).toContain("você ainda estará dentro de “Grau”");
    const o = teoriaStep(withAnchor(seg(), anchor({ start: { kind: "opens", text: "Como o valor tabelado" }, stop: null })));
    expect(o).toContain("que abre com “Como o valor tabelado”");
  });

  it("sem âncora, não cita tópico que não possa ser conferido", () => {
    const t = teoriaStep(withAnchor(seg(), undefined));
    expect(t).not.toContain("tópico");
    expect(t).toContain("pág. 12");
  });
});
