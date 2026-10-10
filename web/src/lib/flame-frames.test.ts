import { describe, expect, it } from "vitest";
import { FLAME_FRAMES, flameFrameHref, flameFrameSvg } from "./flame-frames";

describe("quadros da chama do ícone da aba", () => {
  it("cada quadro é um SVG 32×32 bem formado", () => {
    for (let i = 0; i < FLAME_FRAMES; i++) {
      const svg = flameFrameSvg(i);
      expect(svg.startsWith('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">')).toBe(true);
      expect(svg.endsWith("</svg>")).toBe(true);
      expect(svg).not.toMatch(/NaN|undefined|Infinity/);
      expect((svg.match(/<path /g) ?? []).length).toBe(3);
    }
  });
  it("os quadros animam (não são todos iguais) e o ciclo é determinístico", () => {
    const frames = Array.from({ length: FLAME_FRAMES }, (_, i) => flameFrameSvg(i));
    expect(new Set(frames).size).toBe(FLAME_FRAMES);
    expect(flameFrameSvg(3)).toBe(frames[3]);
  });
  it("o href é um data URI SVG que decodifica para o quadro", () => {
    const href = flameFrameHref(2);
    expect(href.startsWith("data:image/svg+xml,")).toBe(true);
    expect(decodeURIComponent(href.slice("data:image/svg+xml,".length))).toBe(flameFrameSvg(2));
  });
});
