// Tipos do motor de planejamento. Tudo aqui é serializável (JSON) e independente de banco/UI.

export type ExamBlock = "I" | "II" | "III";
export type ActivityType = "TEORIA" | "REVISAO" | "FIXACAO" | "QUESTOES";
export type Level = 0 | 1 | 2 | 3; // 0 iniciante · 1 básico · 2 intermediário · 3 domina
export type Tier = 1 | 2 | 3; // 1 essencial · 2 completo · 3 aprofundamento
/** Conhecimento prévio de uma aula (anamnese): 0 nunca estudei · 1 já estudei · 2 domino. */
export type Known = 0 | 1 | 2;

export interface PracticeLink {
  theme: string;
  startPage: number;
  endPage: number;
  sourceAula: string;
}

export interface CatalogAula {
  id: string;
  number: number;
  title: string;
  shortTitle: string;
  kind: "theory" | "practice";
  edital: "yes" | "partial" | "no";
  selectable: boolean;
  theoryPages: number;
  segmentCount: number;
  commentedPages: number;
  listPages: number;
  commentedRuns: [number, number][];
  practiceLinks: PracticeLink[];
  incidence: number;
  printedOffset: number;
  /** "authored": material complementar do MentorIA (preenche lacuna do edital) com PDF próprio. */
  source?: "base" | "authored";
}

export interface CatalogSubject {
  id: string;
  name: string;
  block: ExamBlock;
  examQuestions: number;
  sortOrder: number;
  languageGroup?: string;
  /** Fatia do edital que o material realmente cobre (1 = completo). */
  materialCompleteness?: number;
  aulas: CatalogAula[];
}

export interface Gap {
  id: string;
  subject: string;
  item: string;
  evidence: string;
  severity: "high" | "medium" | "low";
  remedy: string;
  /** true quando um material complementar do MentorIA já preenche a lacuna */
  resolved?: boolean;
  resolution?: string;
}

export interface Catalog {
  subjects: CatalogSubject[];
  gaps: Gap[];
}

export interface SegmentLite {
  id: string;
  aula: string;
  order: number;
  startPage: number;
  endPage: number;
  pages: number;
  load: number;
}
export type SegmentsByAula = Record<string, SegmentLite[]>;

export interface PlanInput {
  catalog: Catalog;
  segments: SegmentsByAula;
  /** Segunda-feira (YYYY-MM-DD) em que o plano começa. */
  startDate: string;
  /** Dia da semana (0 = segunda … 6 = domingo) em que os estudos começam na 1ª semana; antes dele a semana fica vazia. Padrão 0. */
  firstDay?: number;
  /** Data da prova objetiva (YYYY-MM-DD). */
  examDate: string;
  hoursPerWeek: number;
  subjects: { id: string; level: Level }[];
  /** Anamnese por aula (id da aula → conhecimento). Aulas ausentes valem 0. */
  known?: Record<string, Known>;
  finalReviewWeeks?: number;
  slack?: number;
}

export interface FixRange {
  start: number;
  end: number;
  /** Aula de origem das páginas (aulas de prática, ex.: Português Aula 14). */
  sourceAula?: string;
}

export interface PlannedActivity {
  /** Identificador temporário, único dentro do plano; vira id real ao persistir. */
  key: string;
  type: ActivityType;
  subjectId: string;
  aulaId: string;
  minutes: number;
  /** Segmentos de teoria cobertos (Teoria: 1+; Revisão: até 3 Teorias; Questões: os do grupo). */
  segmentIds: string[];
  /** Teorias anteriores às quais a Revisão/Questões está atrelada. */
  refKeys: string[];
  /** Fixação: faixas de páginas da seção de questões comentadas. */
  fixRanges?: FixRange[];
  /** Revisão final / caderno misto das últimas semanas. */
  scope?: "AULA" | "FINAL";
  quiz?: { questions: number; limitSeconds: number; mixed: boolean };
  /** Dia planejado dentro da semana (0 = segunda … 6 = domingo). */
  day?: number;
}

export interface PlannedWeek {
  index: number;
  startDate: string;
  kind: "CONTENT" | "FINAL_REVIEW";
  targetMinutes: number;
  activities: PlannedActivity[];
}

export interface SubjectCoverage {
  subjectId: string;
  level: Level;
  examQuestions: number;
  /** Horas planejadas (conteúdo novo) na disciplina. */
  plannedHours: number;
  /** Minutos planejados por tipo de atividade. */
  minutes: { teoria: number; revisao: number; fixacao: number; questoes: number };
  /** Minutos para ver TODAS as aulas da disciplina no nível Essencial (Teoria + Questões). */
  fullMinutes: number;
  aulas: { aulaId: string; tier: Tier; hours: number }[];
  theoryPagesCovered: number;
  theoryPagesEligible: number;
  /** 0–1: fatia do edital da disciplina que o plano cobre (aulas estudadas ou já dominadas × completude do material). */
  coverage: number;
  /** 0–1: profundidade da prática (fixação e cadernos) nas aulas cobertas. */
  depth: number;
  materialCompleteness: number;
  notCovered: { aulaId: string; shortTitle: string; incidence: number }[];
}

export interface PlanResult {
  params: {
    hoursPerWeek: number;
    /** Horas efetivas por semana (já com a folga). */
    slotsPerWeek: number;
    weeklyMinutes: number;
    totalWeeks: number;
    contentWeeks: number;
    reviewWeeks: number;
    capacityHours: number;
    plannedHours: number;
    /** Horas por semana (nominais) necessárias para ver o edital inteiro (só Teoria + Questões, com a revisão final no piso). */
    fullEditalHoursPerWeek: number;
    /** Segunda-feira da semana 1. */
    startDate: string;
    /** Dia em que o aluno começa a estudar (pode ser depois da segunda da semana 1). */
    firstStudyDate: string;
    examDate: string;
  };
  weeks: PlannedWeek[];
  coverage: {
    /** Cobertura ponderada pelos pontos da prova, relativa às disciplinas escolhidas. */
    selected: number;
    /** Cobertura ponderada relativa ao edital inteiro (70 questões). */
    edital: number;
    /** Profundidade média da prática, ponderada pelos pontos da prova. */
    depth: number;
    subjects: SubjectCoverage[];
  };
  warnings: string[];
}
