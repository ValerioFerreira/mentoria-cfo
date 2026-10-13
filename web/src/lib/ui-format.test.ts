import { describe, expect, it } from "vitest";
import { fmtClock, fmtDate, fmtDuration, STATUS_LABEL, SUBJECT_NAME, SUBJECT_SHORT, subjectName, subjectShort, weekRange } from "./ui-format";
import { FAMILY } from "./planner/constants";

describe("fmtDuration", () => {
  it("zero e negativos viram '0 min'", () => {
    expect(fmtDuration(0)).toBe("0 min");
    expect(fmtDuration(-30)).toBe("0 min");
  });
  it("menos de 1 minuto aparece em segundos", () => {
    expect(fmtDuration(40)).toBe("40 s");
    expect(fmtDuration(59)).toBe("59 s");
  });
  it("minutos inteiros sem hora", () => {
    expect(fmtDuration(60)).toBe("1 min");
    expect(fmtDuration(540)).toBe("9 min");
    expect(fmtDuration(3599)).toBe("59 min");
  });
  it("a partir de 1 h usa 'XhMM' com minutos em dois dígitos", () => {
    expect(fmtDuration(3600)).toBe("1h00");
    expect(fmtDuration(3725)).toBe("1h02");
    expect(fmtDuration(7 * 3600 + 5 * 60)).toBe("7h05");
  });
  it("arredonda segundos fracionados", () => {
    expect(fmtDuration(59.6)).toBe("1 min");
    expect(fmtDuration(0.4)).toBe("0 min");
  });
});

describe("fmtClock", () => {
  it("formata MM:SS abaixo de 1 hora e H:MM:SS a partir dela", () => {
    expect(fmtClock(0)).toBe("00:00");
    expect(fmtClock(65_000)).toBe("01:05");
    expect(fmtClock(3_599_000)).toBe("59:59");
    expect(fmtClock(3_600_000)).toBe("1:00:00");
    expect(fmtClock(3_725_000)).toBe("1:02:05");
  });
  it("milissegundos negativos não geram relógio negativo e frações são truncadas", () => {
    expect(fmtClock(-5000)).toBe("00:00");
    expect(fmtClock(1999)).toBe("00:01");
  });
});

describe("datas da interface (UTC)", () => {
  it("weekRange mostra segunda a domingo em dd/mm", () => {
    expect(weekRange(new Date("2026-10-12T00:00:00Z"))).toBe("12/10 – 18/10");
  });
  it("weekRange atravessa a virada do mês e do ano", () => {
    expect(weekRange(new Date("2026-12-28T00:00:00Z"))).toBe("28/12 – 03/01");
    expect(weekRange(new Date("2026-10-26T00:00:00Z"))).toBe("26/10 – 01/11");
  });
  it("fmtDate usa o dia UTC (não recua no fuso de Recife)", () => {
    expect(fmtDate(new Date("2027-02-28T00:00:00Z"))).toBe("28 de fevereiro de 2027");
  });
});

describe("rótulos de disciplina", () => {
  it("conhece todas as 16 disciplinas e devolve o próprio id quando desconhecida", () => {
    expect(Object.keys(SUBJECT_SHORT)).toHaveLength(16);
    expect(Object.keys(SUBJECT_NAME)).toHaveLength(16);
    expect(subjectShort("matematica")).toBe("Matemática");
    expect(subjectName("legislacoes-pe")).toBe("Legislações Militares de PE");
    expect(subjectShort("nao-existe")).toBe("nao-existe");
    expect(subjectName("nao-existe")).toBe("nao-existe");
  });
  it("as mesmas disciplinas do planejador (famílias) têm rótulos curtos e longos", () => {
    for (const id of Object.keys(FAMILY)) {
      expect(SUBJECT_SHORT[id], id).toBeTruthy();
      expect(SUBJECT_NAME[id], id).toBeTruthy();
    }
  });
  it("status de atividade têm rótulo em português para os 4 estados", () => {
    expect(Object.keys(STATUS_LABEL).sort()).toEqual(["DONE", "IN_PROGRESS", "PENDING", "SKIPPED"]);
  });
});
