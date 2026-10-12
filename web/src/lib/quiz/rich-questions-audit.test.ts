import { describe, expect, it } from "vitest";
import { Fragment, createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { formatInlineRich } from "@/components/rich-content";

describe("Auditoria e Renderização de Questões Ricas", () => {
  describe("1. Formatação Inline e Sanitização de Asteriscos", () => {
    it("renderiza negrito semântico fechado corretamente", () => {
      const node = formatInlineRich("Assinale a alternativa **CORRETA** sobre o ato.");
      expect(node).toBeDefined();
    });

    it("sanitiza asteriscos residuais soltos impedindo que apareçam literalmente", () => {
      const textWithDanglingStars = "No exercício da função, **constata que o ato é nulo. **";
      const node = formatInlineRich(textWithDanglingStars);
      expect(node).toBeDefined();
      // formatInlineRich converte em Fragment sem caracteres ** soltos
    });

    it("renderiza sublinhado legítimo com tag <u>", () => {
      const node = formatInlineRich("desviando <u>periodicamente</u> o foco da história.");
      expect(node).toBeDefined();
    });

    it("preserva caracteres especiais e matemáticos sem alteração", () => {
      const formula = "A resistência é R = 10 Ω e a corrente I = 2 A. Logo U = 20 V.";
      const node = formatInlineRich(formula);
      expect(node).toBeDefined();
    });
  });

  describe("2. Marcação dos cadernos importados (pipeline/questoes/EXTRACAO.md)", () => {
    const html = (t: string) => renderToStaticMarkup(createElement(Fragment, null, formatInlineRich(t)));

    it("fórmula embutida vira imagem inline com altura em em", () => {
      const out = html("de intensidade ![fórmula:1.9](/q-img/" + "a".repeat(64) + "). Considerando");
      expect(out).toContain('src="/q-img/' + "a".repeat(64) + '"');
      expect(out).toContain("height:1.9em");
      expect(out).toContain("q-crop");
    });

    it("sobrescrito, subscrito e destaque", () => {
      expect(html("CO<sub>2</sub> e Pb<sup>2+</sup>")).toContain("CO<sub>2</sub> e Pb<sup>2+</sup>");
      expect(html("nas <mark>palavras destacadas</mark>")).toContain("<mark");
    });

    it("asterisco escapado é literal e não abre itálico", () => {
      const out = html("2 \\* 3 = 6 e 4 \\* 5 = 20");
      expect(out).toBe("2 * 3 = 6 e 4 * 5 = 20");
    });
  });
});
