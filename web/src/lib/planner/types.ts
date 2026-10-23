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
  onlyContests?: string[];
  excludeContests?: string[];
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
  /** Aulas excluídas porque o usuário desmarcou assuntos específicos do edital. */
  excludedAulas?: string[];
  /** Concurso para o qual o plano é montado (informativo; as notas e os pesos chegam em `importance` e `examQuestions`). */
  contest?: string;
  /** Nota de importância (1–100) de cada trecho NO CONCURSO; `null` = o assunto não consta no edital dele (sai do plano). Ausente = sem filtro. */
  importance?: Record<string, number | null>;
  /** Trechos que já têm resumo analítico: só eles podem ser trocados no Modo Turbo. */
  summaries?: string[];
  /** Questões de cada disciplina na prova do concurso (substitui `examQuestions` do catálogo, que é o do CBMPE Oficial). */
  examQuestions?: Record<string, number>;
  /** Modo Turbo: se o tempo não fechar o edital, as unidades de menor importância viram resumos analíticos (até 3 por atividade). */
  turbo?: boolean;
  /**
   * Pacote combo (dois concursos da mesma corporação em um plano). `contest` é a chave do combo, `importance` já é a união dos
   * editais e `examQuestions` o peso combinado por disciplina (W = Σ peso × questões do concurso). Como o "aparece no edital"
   * é decidido por disciplina, a seleção com W equivale a somar o ganho de cada prova ponderado pelo peso.
   */
  combo?: { priority: string; members: ComboMember[] };
  slack?: number;
}

export interface ComboMember {
  contest: string;
  /** 1 para o concurso prioritário, 0,5 para o outro (peso fixo 2:1) */
  weight: number;
  /** total de questões da prova do concurso */
  totalQuestions: number;
  /** questões de cada disciplina na prova do concurso */
  examQuestions: Record<string, number>;
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
  /** Modo Turbo: Teoria substituída pelo resumo (Bizu) do trecho. */
  turbo?: boolean;
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
  aulas: { aulaId: string; tier: Tier; hours: number; turbo?: boolean }[];
  theoryPagesCovered: number;
  /** Páginas de teoria cobertas só por resumo analítico (Modo Turbo). */
  summaryPages: number;
  theoryPagesEligible: number;
  /** 0–1: fatia do edital da disciplina que o plano cobre (aulas estudadas ou já dominadas × completude do material). */
  coverage: number;
  /** 0–1: profundidade da prática (fixação e cadernos) nas aulas cobertas. */
  depth: number;
  materialCompleteness: number;
  notCovered: { aulaId: string; shortTitle: string; incidence: number }[];
}

/** O que o aluno pediu ao montar o plano (guardado em `params.request` para auditoria e re-elaboração). */
export interface PlanRequest {
  hoursPerWeek: number;
  turbo: boolean;
  firstDay: number;
  contest?: string;
  /** combo: concursos-membro e prioridade escolhida */
  combo?: { contests: string[]; priority: string };
  subjects: { id: string; level: Level }[];
  /** anamnese por aula: 1 já estudei · 2 domino */
  known: Record<string, Known>;
  /** aulas fora do plano porque o aluno desmarcou todos os assuntos delas */
  excludedAulas: string[];
}

export interface ContestCoverage {
  contest: string;
  weight: number;
  /** cobertura ponderada pelos pontos da prova deste concurso, relativa às disciplinas escolhidas */
  selected: number;
  /** cobertura relativa ao total de questões da prova deste concurso */
  edital: number;
  subjects: { subjectId: string; examQuestions: number; coverage: number }[];
}

export interface PlanResult {
  params: {
    /** Solicitação original do aluno. */
    request: PlanRequest;
    /** Modo Turbo pedido (cópia de `request.turbo`, lida pela re-elaboração de planos). */
    turbo: boolean;
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
    /** O edital inteiro (Teoria + Questões) cabe no tempo disponível, sem Modo Turbo? */
    editalFits: boolean;
    /** Nº de aulas com ao menos uma unidade trocada por resumo (Modo Turbo). */
    turboAulas: number;
    /** Nº de unidades de Teoria trocadas por resumo analítico (Modo Turbo). */
    summaryUnits: number;
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
    /** Combo: cobertura de cada prova (disciplinas que ela cobra, com as questões dela). */
    contests?: ContestCoverage[];
    /** 0–1: fração do que o plano cobre que é lida por resumo analítico (Modo Turbo), ponderada pelos pontos da prova. */
    summaryShare: number;
    subjects: SubjectCoverage[];
  };
  warnings: string[];
}
