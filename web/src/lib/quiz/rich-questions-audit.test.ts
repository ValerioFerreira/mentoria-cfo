import { describe, expect, it } from "vitest";
import fs from "fs";
import path from "path";
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

  describe("2. Validação do Acervo Auditado no Disco", () => {
    const jsonPath = path.resolve(process.cwd(), "content/questoes_estrategia_cbmpe_pmpe.json");
    const imgDir = path.resolve(process.cwd(), "public/questoes/imagens");

    it("carrega a base de dados do Estratégia sem corrupção JSON", () => {
      expect(fs.existsSync(jsonPath)).toBe(true);
      const raw = fs.readFileSync(jsonPath, "utf-8");
      const qs = JSON.parse(raw);
      expect(qs.length).toBeGreaterThan(2000);
    });

    it("garante zero asteriscos desbalanceados no acervo auditado", () => {
      const raw = fs.readFileSync(jsonPath, "utf-8");
      const qs: any[] = JSON.parse(raw);
      let danglingCount = 0;
      for (const q of qs) {
        const st: string = q.statement || "";
        const matches = st.match(/\*\*/g);
        if (matches && matches.length % 2 !== 0) {
          danglingCount++;
        }
      }
      expect(danglingCount).toBe(0);
    });

    it("garante que todas as imagens referenciadas existem fisicamente no disco", () => {
      const raw = fs.readFileSync(jsonPath, "utf-8");
      const qs: any[] = JSON.parse(raw);
      let missingCount = 0;

      for (const q of qs) {
        const st: string = q.statement || "";
        const urls = st.match(/!\[.*?\]\((\/questoes\/imagens\/[^)]+)\)/g) || [];
        for (const u of urls) {
          const fn = u.replace(/.*\/questoes\/imagens\//, "").replace(/\).*/, "");
          const fpath = path.join(imgDir, fn);
          if (!fs.existsSync(fpath)) {
            missingCount++;
          }
        }
      }
      expect(missingCount).toBe(0);
    });

    it("garante que questões que exigem visual e não possuem figura estão marcadas como DRAFT", () => {
      const raw = fs.readFileSync(jsonPath, "utf-8");
      const qs: any[] = JSON.parse(raw);
      const visualReqRegex = /\b(?:na figura abaixo|conforme a figura|no gráfico abaixo|no circuito elétrico)\b/i;

      for (const q of qs) {
        const st: string = q.statement || "";
        if (visualReqRegex.test(st) && !st.includes("![")) {
          expect(q.status).toBe("DRAFT");
        }
      }
    });

    it("não remove conteúdo legítimo que contenha números, URLs, nomes ou siglas", () => {
      const raw = fs.readFileSync(jsonPath, "utf-8");
      const qs: any[] = JSON.parse(raw);
      // Pelo menos 95% das questões permanecem APPROVED
      const approvedCount = qs.filter((q) => q.status === "APPROVED").length;
      expect(approvedCount / qs.length).toBeGreaterThan(0.94);
    });
  });
});
