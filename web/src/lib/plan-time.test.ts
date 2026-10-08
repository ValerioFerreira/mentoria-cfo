import { describe, expect, it } from "vitest";
import { dateOfPlanDay, dayOfWeekIndex, effectiveDays, firstStudyISO, longDate, planPosition, todayISO } from "./plan-time";

describe("calendário do plano", () => {
  it("posição: antes, durante e depois do plano", () => {
    expect(planPosition("2026-10-12", 20, "2026-10-10")).toMatchObject({ state: "before", offset: -2 });
    expect(planPosition("2026-10-12", 20, "2026-10-12")).toMatchObject({ state: "during", week: 1, day: 0 });
    expect(planPosition("2026-10-12", 20, "2026-10-18")).toMatchObject({ state: "during", week: 1, day: 6 });
    expect(planPosition("2026-10-12", 20, "2026-10-19")).toMatchObject({ state: "during", week: 2, day: 0 });
    expect(planPosition("2026-10-12", 20, "2027-02-28")).toMatchObject({ state: "during", week: 20, day: 6 });
    expect(planPosition("2026-10-12", 20, "2027-03-01").state).toBe("after");
  });

  it("início no meio da semana: antes do primeiro dia de estudo o plano ainda não começou", () => {
    // semana 1 começa na segunda 12/10, mas o aluno só começa na quarta 14/10
    expect(planPosition("2026-10-12", 20, "2026-10-13", "2026-10-14")).toMatchObject({ state: "before" });
    expect(planPosition("2026-10-12", 20, "2026-10-14", "2026-10-14")).toMatchObject({ state: "during", week: 1, day: 2 });
    expect(firstStudyISO({ startDate: new Date("2026-10-12"), params: { firstStudyDate: "2026-10-14" } })).toBe("2026-10-14");
    expect(firstStudyISO({ startDate: new Date("2026-10-12"), params: {} })).toBe("2026-10-12");
    expect(dayOfWeekIndex("2026-10-14")).toBe(2);
    expect(dayOfWeekIndex("2026-10-18")).toBe(6);
  });

  it("data civil no fuso de Recife (UTC−3), não em UTC", () => {
    expect(todayISO(new Date("2026-10-14T01:30:00Z"))).toBe("2026-10-13");
    expect(todayISO(new Date("2026-10-14T03:30:00Z"))).toBe("2026-10-14");
  });

  it("data de um dia do plano e rótulo longo", () => {
    expect(dateOfPlanDay("2026-10-12", 2, 2)).toBe("2026-10-21");
    expect(longDate("2026-10-14")).toBe("Quarta-feira, 14 de outubro");
  });

  it("planos antigos sem dia: espalha pela semana na ordem; com dia, respeita", () => {
    const legacy = effectiveDays([0, 1, 2, 3, 4, 5].map((i) => ({ sortOrder: i, dayIndex: null })));
    expect(legacy.map((a) => a.day)).toEqual([0, 1, 2, 3, 4, 5]);
    expect(effectiveDays([{ sortOrder: 0, dayIndex: 4 }, { sortOrder: 1, dayIndex: null }])[0].day).toBe(4);
  });
});
