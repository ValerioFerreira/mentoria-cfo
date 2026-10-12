// Regras fixas do edital (2º Tenente CBMPE, código 401) e do planejamento.
export const EXAM_DATE_DEFAULT = "2027-02-28";
/** O conteúdo (Teoria, Revisão, Fixação, Questões) corre até D-2; a véspera (D-1) tem uma única Revisão dos assuntos de maior peso. */
export const CONTENT_ENDS_DAYS_BEFORE_EXAM = 2;
export const WEEKLY_SLACK = 0.9; // 10% de folga para atrasos
/** O encaixe das atividades (blocos de 20–75 min) nas semanas nunca é perfeito: a seleção conta com 95% da capacidade. */
export const PACKING_EFFICIENCY = 0.95;
/** Teto da busca de encaixe: as semanas podem passar até 5% da meta, e a folga semanal de 10% já cobre atrasos. */
export const MAX_SELECTION_EFFICIENCY = 1.04;

export const HOURS_BANDS = {
  LEVE: { min: 14, max: 21 },
  MODERADO: { min: 22, max: 28 },
  AVANCADO: { min: 29, max: 50 },
} as const;

// Segmentação da Teoria (regra do usuário: 10–17 págs. por atividade de ~1 h, conforme a densidade).
export const SEGMENT = { targetLoad: 12, maxPages: 17, minPages: 6 } as const;

export const QUIZ = { questions: 25, limitSeconds: 3600 } as const;
export const FIXACAO_PAGES_PER_HOUR = 12;

export const EXAM_TOTAL_QUESTIONS = 70;

// ───────────────────────── Tempo por atividade ─────────────────────────
/** Teoria: 50 a 80 min (alvo de 60 min). Unidade curta (< `shortPages` págs.) pode ir até `shortMin`. */
export const TEORIA_MINUTES = { perLoadUnit: 60 / SEGMENT.targetLoad, min: 50, max: 80, shortMin: 35, shortPages: 8 } as const;
/** Revisão: base 25 min + 10 min por teoria revista, entre 30 e 60 min. */
export const REVISAO_MINUTES = { base: 25, perTeoria: 10, min: 30, max: 60 } as const;
export const FIXACAO_MINUTES = { normal: 60, min: 40, max: 60 } as const;
export const QUESTOES_MINUTES = { normal: 60, min: 50, max: 80 } as const;
/**
 * Modo Turbo: as unidades de Teoria de menor importância no concurso (e que já têm resumo analítico) são trocadas por esse
 * resumo — ~20 min de leitura por unidade, até 3 unidades seguidas da mesma disciplina por atividade (≤ 1 h). O ciclo é
 * flexibilizado: o bloco de resumos acumula assuntos antes de Revisão (metade do tempo) e Questões (caderno curto).
 */
export const SUMMARY = {
  /** minutos de leitura de um resumo analítico (≤ 20) e piso após o ritmo do aluno */
  minutesPerUnit: 20, minMinutes: 15,
  /** unidades de resumo que formam uma atividade (3 × 20 min = 1 h) */
  maxUnitsPerActivity: 3,
  /** uma Revisão (metade do tempo) a cada tantas atividades de resumo; um caderno curto a cada tantas unidades */
  activitiesPerReview: 3, unitsPerQuiz: 6,
  /** um bloco acumula, no máximo, tantas unidades (≈ 3 h de leitura) antes de fechar o ciclo */
  maxUnitsPerBlock: 9,
} as const;
export const TURBO = {
  revisaoFactor: 0.5, revisaoMin: 25, revisaoMax: 35,
  fixacao: 30,
  questoes: 40, quizQuestions: 15, quizLimitSeconds: 2400,
} as const;
/**
 * Peso de uma unidade lida por resumo na COBERTURA do edital. O Modo Turbo existe para completar o edital: o assunto lido pelo
 * resumo analítico conta como abordado (peso 1). A parte do edital vista só por resumo aparece à parte (`coverage.summaryShare`).
 */
export const SUMMARY_COVERAGE_WEIGHT = 1;
/** Faixa geral de qualquer atividade (menor piso: Revisão/Fixação do Turbo; maior teto: Teoria/Questões). */
export const MIN_ACTIVITY_MINUTES = 15;
export const MAX_ACTIVITY_MINUTES = 80;
export const TARGET_ACTIVITY_MINUTES = 60;
/** Revisão da véspera da prova (D-1). */
export const EVE_REVIEW_MINUTES = 60;

/**
 * Ritmo por nível do aluno na disciplina (multiplica o tempo das atividades): quem já domina o assunto lê,
 * revisa e resolve mais rápido. Nível 0 = referência (10–17 págs. por hora).
 */
export const LEVEL_PACE = { 0: 1, 1: 0.9, 2: 0.8, 3: 0.7 } as const;
/** Aula marcada como "já estudei" na anamnese: leitura de consolidação. */
export const KNOWN_PACE = { 1: 0.75 } as const;

// ───────────────────────── Distribuição diária ─────────────────────────
/** Peso de cada dia da semana (seg…dom). O domingo é um dia leve de fechamento (revisão e cadernos). */
export const DAY_WEIGHTS = [1, 1, 1, 1, 1, 1, 0.45] as const;
export const DAY_NAMES = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"] as const;
export const MAX_SUBJECTS_PER_DAY = 3;
export const MAX_SAME_SUBJECT_MINUTES_PER_DAY = 120;
/** Dias de intervalo mínimos entre etapas do ciclo: Teoria→Revisão, Revisão→Fixação, Fixação→Questões. */
export const CYCLE_GAP_DAYS = 1;

/** Famílias de assunto: matérias parecidas competem na memória, então não ficam coladas no mesmo dia. */
export const FAMILY: Record<string, "JURIDICA" | "LINGUAGEM" | "EXATAS" | "NATUREZA" | "HUMANAS"> = {
  "direito-constitucional": "JURIDICA",
  "direito-administrativo": "JURIDICA",
  "direito-penal-militar": "JURIDICA",
  "legislacoes-pe": "JURIDICA",
  "lingua-portuguesa": "LINGUAGEM",
  "lingua-inglesa": "LINGUAGEM",
  "lingua-espanhola": "LINGUAGEM",
  matematica: "EXATAS",
  estatistica: "EXATAS",
  fisica: "EXATAS",
  quimica: "EXATAS",
  "raciocinio-logico": "EXATAS",
  "historia-pe": "HUMANAS",
  atualidades: "HUMANAS",
  biologia: "NATUREZA",
  informatica: "NATUREZA",
};

