import { describe, expect, it } from "vitest";
import { chartReadiness, projectExam, weeksWithStudy, quizBySubject, secondsByDay, secondsThisWeek, secondsByWeek, secondsBySubject, streakDays, totalSeconds, weakTopics, weekIndexOf, type QuizRow, type SubjectMeta, type TimeRow } from "./metrics";

const d = (s: string) => new Date(s + "T12:00:00Z");
const t = (iso: string, seconds: number, subjectId: string | null = "x"): TimeRow => ({ seconds, startedAt: d(iso), subjectId });

describe("tempo estudado", () => {
  it("soma total e por disciplina (tempo sem atividade fica à parte)", () => {
    const rows = [t("2026-10-12", 3600, "a"), t("2026-10-13", 1800, "a"), t("2026-10-13", 600, null)];
    expect(totalSeconds(rows)).toBe(6000);
    const m = secondsBySubject(rows);
    expect(m.get("a")).toBe(5400);
    expect(m.get("_none")).toBe(600);
  });
  it("distribui por semana do plano e ignora fora do intervalo", () => {
    const start = d("2026-10-12");
    expect(weekIndexOf(d("2026-10-12"), start, 20)).toBe(1);
    expect(weekIndexOf(d("2026-10-19"), start, 20)).toBe(2);
    expect(weekIndexOf(d("2026-10-11"), start, 20)).toBeNull();
    const rows = [t("2026-10-13", 100), t("2026-10-20", 200), t("2026-10-21", 300)];
    expect(secondsByWeek(rows, start, 3)).toEqual([100, 500, 0]);
  });
  it("semana civil (segunda a domingo, Recife): estudo às 22h de domingo ainda é da semana que termina", () => {
    // domingo 11/10 22h em Recife = segunda 12/10 01h UTC; hoje: quarta 14/10
    const sundayNight = { seconds: 3600, startedAt: new Date("2026-10-12T01:00:00Z"), subjectId: "x" };
    const mondayNoon = t("2026-10-12", 600);
    expect(secondsThisWeek([sundayNight, mondayNoon], d("2026-10-14"))).toBe(600);
    expect(secondsThisWeek([sundayNight], d("2026-10-11"))).toBe(3600);
    // lançamento sem plano e antes do início do plano também conta na semana corrente
    expect(secondsThisWeek([t("2026-10-13", 120)], d("2026-10-14"))).toBe(120);
  });
  it("sequência de dias consecutivos, tolerando que hoje ainda esteja em aberto", () => {
    const rows = [t("2026-10-10", 60), t("2026-10-11", 60), t("2026-10-12", 60)];
    expect(streakDays(rows, d("2026-10-12"))).toBe(3);
    expect(streakDays(rows, d("2026-10-13"))).toBe(3); // ontem estudou
    expect(streakDays(rows, d("2026-10-15"))).toBe(0);
  });
  it("série diária: janela de N dias terminando hoje, com zeros nos dias sem estudo", () => {
    const rows = [t("2026-10-10", 60), t("2026-10-12", 100), t("2026-10-12", 50), t("2026-09-01", 999)];
    const days = secondsByDay(rows, d("2026-10-12"), 4);
    expect(days.map((x) => x.date)).toEqual(["2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12"]);
    expect(days.map((x) => x.seconds)).toEqual([0, 60, 0, 150]);
  });
});

const q = (subjectId: string, ok: boolean | null, topic: string | null = "T", seconds = 30): QuizRow => ({
  subjectId, topic, chosen: ok === null ? null : ok ? "A" : "B", isCorrect: ok === null ? null : ok, seconds, finishedAt: d("2026-10-20"),
});

describe("questões", () => {
  it("acerto por disciplina conta branco como erro", () => {
    const m = quizBySubject([q("a", true), q("a", false), q("a", null), q("a", true)]);
    expect(m.get("a")).toMatchObject({ total: 4, answered: 3, correct: 2, accuracy: 0.5 });
  });
  it("assuntos fracos exigem mínimo de tentativas e acerto < 70%", () => {
    const rows = [q("a", false, "Ruim"), q("a", false, "Ruim"), q("a", true, "Ruim"), q("a", true, "Bom"), q("a", true, "Bom"), q("a", true, "Bom"), q("a", false, "Poucos")];
    const w = weakTopics(rows);
    expect(w.map((x) => x.topic)).toEqual(["Ruim"]);
  });
});

describe("projeção por bloco", () => {
  const subs: SubjectMeta[] = [
    { id: "p", name: "Port", block: "I", examQuestions: 5 },
    { id: "i", name: "Info", block: "I", examQuestions: 5 },
    { id: "m", name: "Mat", block: "II", examQuestions: 5 },
  ];
  const stat = (id: string, total: number, correct: number) => [id, { subjectId: id, answered: total, total, correct, accuracy: correct / total, avgSeconds: 30 }] as const;
  it("sem dados suficientes não projeta", () => {
    const p = projectExam(subs, new Map([stat("p", 4, 4)]));
    expect(p[0].status).toBe("sem-dados");
    expect(p[0].projected).toBeNull();
  });
  it("projeta pontos e marca risco abaixo de 30% ou com área zerada", () => {
    const ok = projectExam(subs, new Map([stat("p", 20, 14), stat("i", 20, 10), stat("m", 20, 12)]));
    expect(ok[0]).toMatchObject({ status: "ok", projected: 5 * 0.7 + 5 * 0.5 });
    const risk = projectExam(subs, new Map([stat("p", 20, 20), stat("i", 20, 0), stat("m", 20, 12)]));
    expect(risk[0].status).toBe("risco"); // Informática zerada, mesmo com o bloco acima de 30%
    const low = projectExam(subs, new Map([stat("p", 20, 4), stat("i", 20, 4), stat("m", 20, 4)]));
    expect(low[1].status).toBe("risco"); // 20% < 30%
  });
});

describe("prontidão dos gráficos", () => {
  it("só libera o gráfico com o mínimo de dados e informa quanto falta", () => {
    expect(chartReadiness(0, 3)).toEqual({ ready: false, missing: 3 });
    expect(chartReadiness(2, 3)).toEqual({ ready: false, missing: 1 });
    expect(chartReadiness(3, 3)).toEqual({ ready: true, missing: 0 });
    expect(chartReadiness(9, 3)).toEqual({ ready: true, missing: 0 });
  });
  it("conta só as semanas do plano com tempo lançado", () => {
    expect(weeksWithStudy([0, 0, 0])).toBe(0);
    expect(weeksWithStudy([0, 3600, 0, 60])).toBe(2);
  });
});
