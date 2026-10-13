import { describe, expect, it } from "vitest";
import { addDays, dayIndexOf, diffDays, mondayOf, nextMonday, parseISO, toISO, weekday, weeksUntil } from "./dates";
import { bandOf, hoursPerDayLabel } from "./bands";
import { HOURS_BANDS } from "./constants";

describe("datas do planejador (UTC)", () => {
  it("parseISO/toISO fazem a ida e volta", () => {
    for (const iso of ["2026-10-12", "2027-02-28", "2028-02-29", "2026-12-31", "2027-01-01"]) expect(toISO(parseISO(iso))).toBe(iso);
  });
  it("addDays cruza mês, ano e ano bissexto, para frente e para trás", () => {
    expect(addDays("2026-10-31", 1)).toBe("2026-11-01");
    expect(addDays("2026-12-31", 1)).toBe("2027-01-01");
    expect(addDays("2028-02-28", 1)).toBe("2028-02-29");
    expect(addDays("2027-02-28", 1)).toBe("2027-03-01");
    expect(addDays("2026-10-12", -12)).toBe("2026-09-30");
    expect(addDays("2026-10-12", 0)).toBe("2026-10-12");
  });
  it("diffDays é a inversa de addDays e tem sinal", () => {
    expect(diffDays("2026-10-12", "2027-02-28")).toBe(139);
    expect(diffDays("2027-02-28", "2026-10-12")).toBe(-139);
    expect(diffDays("2026-10-12", "2026-10-12")).toBe(0);
    for (const n of [-400, -7, 0, 1, 7, 365]) expect(diffDays("2026-10-12", addDays("2026-10-12", n))).toBe(n);
  });
  it("não sofre com horário de verão (diferença de dias exata ao longo de um ano inteiro)", () => {
    let d = "2026-01-01";
    for (let i = 0; i < 400; i++) {
      const n = addDays(d, 1);
      expect(diffDays(d, n)).toBe(1);
      d = n;
    }
  });
  it("weekday: 0 = domingo … 6 = sábado", () => {
    expect(weekday("2026-10-11")).toBe(0); // domingo
    expect(weekday("2026-10-12")).toBe(1);
    expect(weekday("2026-10-17")).toBe(6);
  });
  it("nextMonday: a própria segunda ou a próxima, a partir de qualquer dia", () => {
    const expected: Record<string, string> = {
      "2026-10-12": "2026-10-12", // seg
      "2026-10-13": "2026-10-19", // ter
      "2026-10-14": "2026-10-19",
      "2026-10-15": "2026-10-19",
      "2026-10-16": "2026-10-19",
      "2026-10-17": "2026-10-19", // sáb
      "2026-10-18": "2026-10-19", // dom
    };
    for (const [from, to] of Object.entries(expected)) expect(nextMonday(from), from).toBe(to);
    expect(nextMonday("2026-12-30")).toBe("2027-01-04");
  });
  it("mondayOf: segunda da semana (seg–dom) que contém a data", () => {
    for (let i = 0; i < 7; i++) expect(mondayOf(addDays("2026-10-12", i))).toBe("2026-10-12");
    expect(mondayOf("2026-10-18")).toBe("2026-10-12");
    expect(mondayOf("2026-10-19")).toBe("2026-10-19");
    expect(mondayOf("2027-01-01")).toBe("2026-12-28");
  });
  it("dayIndexOf: 0 = segunda … 6 = domingo", () => {
    expect([0, 1, 2, 3, 4, 5, 6].map((i) => dayIndexOf(addDays("2026-10-12", i)))).toEqual([0, 1, 2, 3, 4, 5, 6]);
  });
  it("weeksUntil conta a semana da prova inteira (arredonda para cima)", () => {
    expect(weeksUntil("2026-10-12", "2026-10-12")).toBe(1);
    expect(weeksUntil("2026-10-12", "2026-10-18")).toBe(1);
    expect(weeksUntil("2026-10-12", "2026-10-19")).toBe(2);
    expect(weeksUntil("2026-10-12", "2027-02-28")).toBe(20);
    expect(weeksUntil("2026-10-12", "2027-03-01")).toBe(21);
  });
  it("weeksUntil nunca é negativo quando a prova é antes do início", () => {
    expect(weeksUntil("2026-10-12", "2026-10-01")).toBe(0);
    expect(weeksUntil("2026-10-12", "2025-01-01")).toBe(0);
  });
});

describe("faixas de horas", () => {
  it("bandOf respeita os limites exatos das faixas", () => {
    expect(bandOf(HOURS_BANDS.LEVE.min)).toBe("LEVE");
    expect(bandOf(HOURS_BANDS.LEVE.max)).toBe("LEVE");
    expect(bandOf(HOURS_BANDS.MODERADO.min)).toBe("MODERADO");
    expect(bandOf(HOURS_BANDS.MODERADO.max)).toBe("MODERADO");
    expect(bandOf(HOURS_BANDS.AVANCADO.min)).toBe("AVANCADO");
    expect(bandOf(HOURS_BANDS.AVANCADO.max)).toBe("AVANCADO");
  });
  it("horas fora das faixas caem na mais próxima", () => {
    expect(bandOf(0)).toBe("LEVE");
    expect(bandOf(5)).toBe("LEVE");
    expect(bandOf(80)).toBe("AVANCADO");
  });
  it("horas fracionadas entre faixas não ficam sem faixa (21,5 h é Moderado)", () => {
    expect(bandOf(21.5)).toBe("MODERADO");
    expect(bandOf(28.5)).toBe("AVANCADO");
  });
  it("rótulo de horas por dia: 14–21 h/sem = 2h a 3h; 22–28 h/sem = 3h08 a 4h", () => {
    expect(hoursPerDayLabel("LEVE")).toBe("2h a 3h por dia");
    expect(hoursPerDayLabel("MODERADO")).toBe("3h09 a 4h por dia");
    expect(hoursPerDayLabel("AVANCADO")).toBe("mais de 4h por dia");
  });
});
