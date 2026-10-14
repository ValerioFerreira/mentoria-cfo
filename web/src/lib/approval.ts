import raw from "./approval/profiles.json";
import type { Contest } from "@/generated/prisma/client";
import type { BlockProjection } from "./metrics";
import { EXAM_TOTAL_QUESTIONS } from "./planner/constants";

/**
 * Perfil de aprovação dos últimos concursos PMPE/CBMPE: média e mínimo de acertos dos aprovados dentro das vagas.
 * Os números vêm de `pipeline/approval_profiles.py` (listas oficiais de classificação; só agregados, sem candidatos).
 */

export interface ApprovalStats {
  n: number;
  mean: number;
  min: number;
  max: number;
  meanPct: number;
  minPct: number;
}

export interface ApprovalProfile {
  id: string;
  label: string;
  corp: "PMPE" | "CBMPE";
  cargo: "oficial" | "praca";
  year: number;
  banca: string;
  vagas: number;
  /** quanto o cargo se parece com o 2º Tenente do CBMPE (peso do perfil no agregado) */
  relevance: number;
  firstCallVagas: number;
  classified: number;
  approved: ApprovalStats;
  firstCall: ApprovalStats;
  minClassified: number;
  totalQuestions: number;
  finalScoreMin?: number;
  note?: string;
  /** por disciplina (slug do sistema; `lingua-estrangeira` agrupa inglês e espanhol) — só nas listas que trazem a nota por disciplina */
  subjects?: Record<string, { max: number; mean: number; min: number }>;
}

export const PROFILES = raw.profiles as ApprovalProfile[];
export const PROFILES_GENERATED_AT = raw.generatedAt;

/** Corporação e cargo de cada concurso do sistema; os perfis de referência são os concursos anteriores da mesma corporação e do mesmo cargo. */
const CONTEST_PROFILE_KEY: Partial<Record<Contest, { corp: ApprovalProfile["corp"]; cargo: ApprovalProfile["cargo"] }>> = {
  CBMPE_OFICIAL: { corp: "CBMPE", cargo: "oficial" },
  CBMPE_SOLDADO: { corp: "CBMPE", cargo: "praca" },
  PMPE_OFICIAL: { corp: "PMPE", cargo: "oficial" },
  PMPE_SOLDADO: { corp: "PMPE", cargo: "praca" },
};

/** Concursos anteriores do concurso do aluno (do mais recente ao mais antigo). Vazio se não há lista oficial para ele. */
export function profilesForContest(contest: Contest): ApprovalProfile[] {
  const key = CONTEST_PROFILE_KEY[contest];
  if (!key) return [];
  return PROFILES.filter((p) => p.corp === key.corp && p.cargo === key.cargo).sort((a, b) => b.year - a.year);
}

/** Peso do perfil: recência (meia-vida de 4 anos contada de 2026) × semelhança com o cargo. 2024 ≈ 0,71 · 2018 ≈ 0,25 · 2016 ≈ 0,18. */
export const WEIGHT_REF_YEAR = 2026;
export const WEIGHT_HALF_LIFE_YEARS = 4;
export function profileWeight(p: Pick<ApprovalProfile, "year" | "relevance">): number {
  return p.relevance * 0.5 ** (Math.max(0, WEIGHT_REF_YEAR - p.year) / WEIGHT_HALF_LIFE_YEARS);
}

/** Inglês e Espanhol são a mesma "Língua Estrangeira" nas listas dos concursos. */
export function profileSlug(subjectId: string): string {
  return subjectId === "lingua-inglesa" || subjectId === "lingua-espanhola" ? "lingua-estrangeira" : subjectId;
}

/** Perfil reduzido ao que a tela compara: percentuais de acerto (0–1), independentes do nº de questões de cada prova. */
export interface ProfileView {
  id: string;
  label: string;
  /** média de acertos dos aprovados / questões da prova */
  totalPct: number;
  /** menor nota entre os aprovados (a "nota de corte real") */
  cutoffPct: number;
  /** média de acerto dos aprovados em cada disciplina */
  subjects: Record<string, number>;
  /** de onde vem, com o peso de cada concurso (só no perfil ponderado tem mais de um) */
  sources: { id: string; label: string; weight: number }[];
}

export function viewOf(p: ApprovalProfile): ProfileView {
  const subjects: Record<string, number> = {};
  for (const [slug, s] of Object.entries(p.subjects ?? {})) subjects[slug] = s.mean / s.max;
  return { id: p.id, label: p.label, totalPct: p.approved.meanPct, cutoffPct: p.approved.minPct, subjects, sources: [{ id: p.id, label: p.label, weight: 1 }] };
}

/** Média ponderada dos perfis (peso = recência × semelhança); por disciplina só entram os concursos que têm a disciplina. */
export function blendProfiles(profiles: ApprovalProfile[]): ProfileView {
  const weights = profiles.map(profileWeight);
  const sum = weights.reduce((a, b) => a + b, 0);
  const wavg = (f: (p: ApprovalProfile) => number) => profiles.reduce((acc, p, i) => acc + f(p) * weights[i], 0) / sum;
  const slugs = new Set(profiles.flatMap((p) => Object.keys(p.subjects ?? {})));
  const subjects: Record<string, number> = {};
  for (const slug of slugs) {
    const withSlug = profiles.map((p, i) => ({ s: p.subjects?.[slug], w: weights[i] })).filter((x) => x.s);
    const wsum = withSlug.reduce((a, x) => a + x.w, 0);
    subjects[slug] = withSlug.reduce((a, x) => a + (x.s!.mean / x.s!.max) * x.w, 0) / wsum;
  }
  return {
    id: "ponderado",
    label: "Perfil ponderado",
    totalPct: wavg((p) => p.approved.meanPct),
    cutoffPct: wavg((p) => p.approved.minPct),
    subjects,
    sources: profiles.map((p, i) => ({ id: p.id, label: p.label, weight: weights[i] / sum })),
  };
}

export type GapStatus = "acima" | "perto" | "abaixo" | "sem-dados";

/** Diferença (em pontos percentuais, 0–1) entre o seu acerto e o dos aprovados: ≥ 0 acima; até −10 p.p. perto; abaixo disso, abaixo. */
export function gapStatus(gap: number | null): GapStatus {
  if (gap === null) return "sem-dados";
  return gap >= 0 ? "acima" : gap > -0.1 ? "perto" : "abaixo";
}

export interface SubjectComparison {
  id: string;
  examQuestions: number;
  /** seu acerto (0–1); null com menos de 10 questões */
  user: number | null;
  /** acerto médio dos aprovados; null se o concurso não traz a disciplina */
  approved: number | null;
  gap: number | null;
  /** diferença em questões da prova (gap × questões da disciplina) */
  gapQuestions: number | null;
  status: GapStatus;
}

export function compareSubjects(subjects: BlockProjection["subjects"], view: ProfileView): SubjectComparison[] {
  return subjects.map((s) => {
    const approved = view.subjects[profileSlug(s.id)] ?? null;
    const gap = s.accuracy !== null && approved !== null ? s.accuracy - approved : null;
    return {
      id: s.id,
      examQuestions: s.examQuestions,
      user: s.accuracy,
      approved,
      gap,
      gapQuestions: gap === null ? null : gap * s.examQuestions,
      status: gapStatus(gap),
    };
  });
}

export interface TotalComparison {
  /** acertos esperados dos aprovados na prova de 70 questões */
  approvedQuestions: number;
  /** nota de corte real em questões */
  cutoffQuestions: number;
  /** suas questões estimadas e o que os aprovados fazem nas mesmas disciplinas (parcial = só o que você já mediu) */
  userQuestions: number | null;
  approvedSameScope: number | null;
  scope: "total" | "parcial" | "sem-dados";
  measured: number;
  of: number;
}

/** Total: seus acertos estimados × os dos aprovados. Se faltam disciplinas medidas, compara só as que têm dado nos dois lados. */
export function compareTotal(comparisons: SubjectComparison[], view: ProfileView, examQuestions = EXAM_TOTAL_QUESTIONS): TotalComparison {
  const approvedQuestions = view.totalPct * examQuestions;
  const cutoffQuestions = view.cutoffPct * examQuestions;
  // concurso que só divulgou o total: compara o total estimado do aluno (só vale com todas as disciplinas medidas)
  if (Object.keys(view.subjects).length === 0) {
    const complete = comparisons.length > 0 && comparisons.every((c) => c.user !== null);
    const measured = comparisons.filter((c) => c.user !== null).length;
    return {
      approvedQuestions,
      cutoffQuestions,
      userQuestions: complete ? comparisons.reduce((a, c) => a + c.user! * c.examQuestions, 0) : null,
      approvedSameScope: complete ? approvedQuestions : null,
      scope: complete ? "total" : "sem-dados",
      measured,
      of: comparisons.length,
    };
  }
  const withUser = comparisons.filter((c) => c.user !== null && c.approved !== null);
  const userQuestions = withUser.length ? withUser.reduce((a, c) => a + c.user! * c.examQuestions, 0) : null;
  const approvedSameScope = withUser.length ? withUser.reduce((a, c) => a + c.approved! * c.examQuestions, 0) : null;
  const complete = withUser.length === comparisons.length && comparisons.length > 0;
  return {
    approvedQuestions,
    cutoffQuestions,
    userQuestions,
    approvedSameScope,
    scope: !withUser.length ? "sem-dados" : complete ? "total" : "parcial",
    measured: withUser.length,
    of: comparisons.length,
  };
}
