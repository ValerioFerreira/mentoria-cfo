// Regras fixas do edital (2º Tenente CBMPE, código 401) e do planejamento.
export const EXAM_DATE_DEFAULT = "2027-02-28";
export const FINAL_REVIEW_WEEKS = 2;
export const WEEKLY_SLACK = 0.9; // 10% de folga para atrasos

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
/** Teoria: 60 min para uma carga de 12 (≈ 10–17 págs. conforme a densidade); trechos leves levam menos, densos mais. */
export const TEORIA_MINUTES = { perLoadUnit: 60 / SEGMENT.targetLoad, min: 30, max: 75 } as const;
/** Revisão: 10 min por Teoria revista + 15 min de base (recuperação ativa do resumo + Bizu). */
export const REVISAO_MINUTES = { base: 15, perTeoria: 10, min: 30, max: 50 } as const;
export const FIXACAO_MINUTES = 60;
export const QUESTOES_MINUTES = 60;
export const MIN_ACTIVITY_MINUTES = 20;

/**
 * Ritmo por nível do aluno na disciplina (multiplica o tempo das atividades): quem já domina o assunto lê,
 * revisa e resolve mais rápido. Nível 0 = referência (10–17 págs. por hora).
 */
export const LEVEL_PACE = { 0: 1, 1: 0.9, 2: 0.75, 3: 0.6 } as const;
/** Aula marcada como "já estudei" na anamnese: leitura de consolidação, bem mais rápida. */
export const KNOWN_PACE = { 1: 0.65 } as const;

// ───────────────────────── Distribuição diária ─────────────────────────
/** Peso de cada dia da semana (seg…dom). O domingo é um dia leve de fechamento (revisão e cadernos). */
export const DAY_WEIGHTS = [1, 1, 1, 1, 1, 1, 0.45] as const;
export const DAY_NAMES = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"] as const;
export const MAX_SUBJECTS_PER_DAY = 3;
export const MAX_SAME_SUBJECT_MINUTES_PER_DAY = 150;

/** Famílias de assunto: matérias parecidas competem na memória, então não ficam coladas no mesmo dia. */
export const FAMILY: Record<string, "JURIDICA" | "LINGUAGEM" | "EXATAS" | "NATUREZA"> = {
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
  biologia: "NATUREZA",
  informatica: "NATUREZA",
};
