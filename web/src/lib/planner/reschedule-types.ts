// Contrato da reprogramação de atividades: tipos compartilhados entre o motor (reschedule.ts), as server actions
// (lib/plan/reschedule-actions.ts) e a interface (app/(app)/reprogramar).
//
// Datas sempre "AAAA-MM-DD" (dia civil de Recife). Minutos das atividades nunca mudam.

/** Como colocar as atividades selecionadas. Todas as opções reorganizam também as dependentes (T → R → F → Q). */
export type RescheduleOption =
  | "SPREAD" // redistribuir nos próximos dias, ponderado pela folga de cada dia
  | "FILL_GAPS" // encaixar só nas folgas (nenhum dia passa da meta)
  | "RECALC_REST" // recalcular todo o restante do plano (hoje até D-2)
  | "MOVE_TO_DAY" // mover para um dia escolhido
  | "DISMISS"; // dispensar (status SKIPPED)

export type RescheduleWindowDays = 3 | 7 | 14;
export type RescheduleExtraLoadPct = 15 | 25 | 40;

export interface RescheduleParams {
  option: RescheduleOption;
  /** SPREAD: janela em dias a partir de hoje (ou de amanhã, se hoje já está cheio). Padrão 7. */
  windowDays?: RescheduleWindowDays;
  /** SPREAD: carga extra máxima por dia, em % da meta do dia. Padrão 25. */
  extraLoadPct?: RescheduleExtraLoadPct;
  /** MOVE_TO_DAY: dia de destino, entre hoje e D-2. */
  targetDate?: string;
}

export interface RescheduleInput {
  /** ids das atividades atrasadas escolhidas pelo aluno */
  activityIds: string[];
  params: RescheduleParams;
}

/** Uma atividade atrasada, como a interface a lista (carregada por lib/plan/overdue.ts). */
export interface OverdueActivity {
  id: string;
  /** texto para o aluno: assunto da atividade (nunca "Aula NN") */
  title: string;
  subjectName: string;
  type: "TEORIA" | "REVISAO" | "FIXACAO" | "QUESTOES";
  plannedMinutes: number;
  /** data em que estava planejada */
  date: string;
  status: "PENDING" | "IN_PROGRESS";
}

export type RescheduleMoveReason =
  | "SELECTED" // atividade escolhida pelo aluno
  | "DEPENDENT"; // reorganizada por depender de uma atividade movida

export interface RescheduleMove {
  id: string;
  title: string;
  subjectName: string;
  type: OverdueActivity["type"];
  plannedMinutes: number;
  fromDate: string;
  toDate: string;
  reason: RescheduleMoveReason;
  /** DEPENDENT: título da atividade de que depende e que foi movida ("reorganizada por depender de…") */
  dependsOnTitle?: string;
}

export interface RescheduleDayLoad {
  date: string;
  /** minutos planejados no dia antes e depois da reprogramação */
  before: number;
  after: number;
  /** meta de minutos do dia (dayTarget) */
  target: number;
}

export type RescheduleWarningCode =
  | "OVER_DAY_TARGET" // algum dia passou da meta
  | "OVER_SUBJECT_DAY" // > 120 min de uma disciplina no dia (escolha do aluno em MOVE_TO_DAY)
  | "SPARE_REVIEW_YIELDED" // cedeu lugar a revisão geral de sobra
  | "COVERAGE_IMPACT" // DISMISS: impacto na cobertura
  | "MANY_DEPENDENTS" // a cascata desloca > 30% das pendentes
  | "DOES_NOT_FIT" // há atividades que não cabem até D-2
  | "RECURRENT_DELAY"; // 2+ reprogramações em 14 dias ou atraso > 50% da meta semanal

export interface RescheduleWarning {
  code: RescheduleWarningCode;
  message: string;
}

export interface RescheduleNoFit {
  id: string;
  title: string;
  subjectName: string;
  plannedMinutes: number;
  /** nota de importância no concurso (SegmentImportance), quando houver; as de menor nota saem primeiro em RECALC_REST */
  importance?: number | null;
}

export interface ReschedulePreview {
  ok: true;
  option: RescheduleOption;
  moves: RescheduleMove[];
  /** ids dispensados (DISMISS) */
  dismissed: string[];
  /** atividades que não cabem até D-2 (nas opções comuns ficam onde estão; em RECALC_REST saem do plano: ver `noFitLeavesPlan`) */
  doesNotFit: RescheduleNoFit[];
  /** true em RECALC_REST: a lista "não cabe" sai do plano ao confirmar (a interface a mostra antes) */
  noFitLeavesPlan: boolean;
  /** revisões gerais de sobra que cedem o lugar (FILL_GAPS e RECALC_REST): saem do plano ao confirmar */
  yielded: RescheduleNoFit[];
  dayLoads: RescheduleDayLoad[];
  warnings: RescheduleWarning[];
  /** quantas pendentes (fora as selecionadas) a cascata deslocou, e a fração do total de pendentes */
  dependentsMoved: number;
  dependentsShare: number;
  /** a prévia recomenda trocar por RECALC_REST (cascata grande ou algo não cabe) */
  suggestRecalc: boolean;
  /** a prévia recomenda refazer o plano com menos horas (/onboarding) */
  suggestRedoPlan: boolean;
}

export interface RescheduleError {
  ok: false;
  error: string;
}

export interface RescheduleApplied {
  ok: true;
  moved: number;
  dismissed: number;
}

/** Assinaturas das server actions (lib/plan/reschedule-actions.ts). */
export interface RescheduleActions {
  previewReschedule(input: RescheduleInput): Promise<ReschedulePreview | RescheduleError>;
  applyReschedule(input: RescheduleInput): Promise<RescheduleApplied | RescheduleError>;
}
