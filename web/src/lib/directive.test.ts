import { describe, expect, it } from "vitest";
import { aulaLabel, fixacaoSteps, pageLabel, pageRangeLocation, teoriaDirective, teoriaStep, turboDirective, type AulaRef, type SegmentRef } from "./directive";

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
    expect(t.steps[2]).toContain("está da pág. 5 à pág. 62 (Aula 02 — Adjetivos e Advérbios)");
  });
});

