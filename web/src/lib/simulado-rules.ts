import type { Contest } from "@/generated/prisma/client";

export interface ExamSubjectRule {
  subjectId: string;
  name: string;
  block: "I" | "II" | "III";
  count: number;
}

export interface ContestExamConfig {
  contest: Contest;
  title: string;
  role: string;
  durationMinutes: number;
  durationSeconds: number;
  totalQuestions: number;
  minPercentPerBlock: number;
  minPercentTotal: number;
  noZeroInAnyArea: boolean;
  blocks: {
    I: { name: string; totalQuestions: number; minQuestions: number };
    II: { name: string; totalQuestions: number; minQuestions: number };
    III: { name: string; totalQuestions: number; minQuestions: number };
  };
  subjects: ExamSubjectRule[];
}

export type SupportedSimuladoContest =
  | "CBMPE_OFICIAL"
  | "CBMPE_SOLDADO"
  | "PMPE_OFICIAL"
  | "PMPE_SOLDADO";

export const EXAM_CONFIGS: Record<SupportedSimuladoContest, ContestExamConfig> = {
  CBMPE_OFICIAL: {
    contest: "CBMPE_OFICIAL",
    title: "CBMPE — 2º Tenente (Oficial BM)",
    role: "Oficial CFO",
    durationMinutes: 270, // 4h30min
    durationSeconds: 270 * 60,
    totalQuestions: 70,
    minPercentPerBlock: 30,
    minPercentTotal: 30,
    noZeroInAnyArea: true,
    blocks: {
      I: { name: "Bloco I", totalQuestions: 20, minQuestions: 6 },
      II: { name: "Bloco II", totalQuestions: 20, minQuestions: 6 },
      III: { name: "Bloco III", totalQuestions: 30, minQuestions: 9 },
    },
    subjects: [
      // Bloco I (20 questões)
      { subjectId: "lingua-portuguesa", name: "Língua Portuguesa", block: "I", count: 5 },
      { subjectId: "FOREIGN_LANG", name: "Língua Estrangeira (Inglês ou Espanhol)", block: "I", count: 5 },
      { subjectId: "informatica", name: "Informática", block: "I", count: 5 },
      { subjectId: "estatistica", name: "Estatística", block: "I", count: 5 },
      // Bloco II (20 questões)
      { subjectId: "matematica", name: "Matemática", block: "II", count: 5 },
      { subjectId: "fisica", name: "Física", block: "II", count: 5 },
      { subjectId: "quimica", name: "Química", block: "II", count: 5 },
      { subjectId: "biologia", name: "Biologia", block: "II", count: 5 },
      // Bloco III (30 questões)
      { subjectId: "direito-constitucional", name: "Direito Constitucional", block: "III", count: 8 },
      { subjectId: "direito-administrativo", name: "Direito Administrativo", block: "III", count: 7 },
      { subjectId: "direito-penal-militar", name: "Direito Penal Militar", block: "III", count: 5 },
      { subjectId: "legislacoes-pe", name: "Legislações Pertinentes aos Militares de PE", block: "III", count: 10 },
    ],
  },
  CBMPE_SOLDADO: {
    contest: "CBMPE_SOLDADO",
    title: "CBMPE — Soldado do Corpo de Bombeiros Militar",
    role: "Soldado CFSd",
    durationMinutes: 240, // 4h00min
    durationSeconds: 240 * 60,
    totalQuestions: 60,
    minPercentPerBlock: 30,
    minPercentTotal: 30,
    noZeroInAnyArea: true,
    blocks: {
      I: { name: "Bloco I", totalQuestions: 30, minQuestions: 9 },
      II: { name: "Bloco II", totalQuestions: 20, minQuestions: 6 },
      III: { name: "Bloco III", totalQuestions: 10, minQuestions: 3 },
    },
    subjects: [
      // Bloco I (30 questões)
      { subjectId: "lingua-portuguesa", name: "Língua Portuguesa", block: "I", count: 10 },
      { subjectId: "raciocinio-logico", name: "Raciocínio Lógico", block: "I", count: 10 },
      { subjectId: "informatica", name: "Informática", block: "I", count: 10 },
      // Bloco II (20 questões)
      { subjectId: "historia-pe", name: "História de Pernambuco", block: "II", count: 10 },
      { subjectId: "atualidades", name: "Atualidades", block: "II", count: 5 },
      { subjectId: "biologia", name: "Biologia", block: "II", count: 5 },
      // Bloco III (10 questões)
      { subjectId: "direito-constitucional", name: "Direito Constitucional", block: "III", count: 5 },
      { subjectId: "legislacoes-pe", name: "Legislações Pertinentes aos Militares de PE", block: "III", count: 5 },
    ],
  },
  PMPE_SOLDADO: {
    contest: "PMPE_SOLDADO",
    title: "PMPE — Soldado da Polícia Militar (QPMG)",
    role: "Soldado CFSd",
    durationMinutes: 240, // 4h00min
    durationSeconds: 240 * 60,
    totalQuestions: 60,
    minPercentPerBlock: 30,
    minPercentTotal: 30,
    noZeroInAnyArea: true,
    blocks: {
      I: { name: "Bloco I", totalQuestions: 20, minQuestions: 6 },
      II: { name: "Bloco II", totalQuestions: 20, minQuestions: 6 },
      III: { name: "Bloco III", totalQuestions: 20, minQuestions: 6 },
    },
    subjects: [
      // Bloco I (20 questões)
      { subjectId: "lingua-portuguesa", name: "Língua Portuguesa", block: "I", count: 10 },
      { subjectId: "historia-pe", name: "História de Pernambuco", block: "I", count: 10 },
      // Bloco II (20 questões)
      { subjectId: "raciocinio-logico", name: "Raciocínio Lógico", block: "II", count: 10 },
      { subjectId: "informatica", name: "Informática", block: "II", count: 10 },
      // Bloco III (20 questões)
      { subjectId: "direito-constitucional", name: "Direito Constitucional", block: "III", count: 10 },
      { subjectId: "legislacoes-pe", name: "Direitos Humanos e Legislação Extravagante", block: "III", count: 10 },
    ],
  },
  PMPE_OFICIAL: {
    contest: "PMPE_OFICIAL",
    title: "PMPE — 2º Tenente da Polícia Militar (QOPM)",
    role: "Oficial CFO",
    durationMinutes: 270, // 4h30min
    durationSeconds: 270 * 60,
    totalQuestions: 70,
    minPercentPerBlock: 30,
    minPercentTotal: 30,
    noZeroInAnyArea: true,
    blocks: {
      I: { name: "Bloco I", totalQuestions: 30, minQuestions: 9 },
      II: { name: "Bloco II", totalQuestions: 20, minQuestions: 6 },
      III: { name: "Bloco III", totalQuestions: 20, minQuestions: 6 },
    },
    subjects: [
      // Bloco I (30 questões)
      { subjectId: "lingua-portuguesa", name: "Língua Portuguesa", block: "I", count: 10 },
      { subjectId: "FOREIGN_LANG", name: "Língua Estrangeira (Inglês ou Espanhol)", block: "I", count: 5 },
      { subjectId: "raciocinio-logico", name: "Raciocínio Lógico", block: "I", count: 5 },
      { subjectId: "estatistica", name: "Estatística", block: "I", count: 5 },
      { subjectId: "informatica", name: "Informática", block: "I", count: 5 },
      // Bloco II (20 questões)
      { subjectId: "direito-constitucional", name: "Direito Constitucional", block: "II", count: 5 },
      { subjectId: "direito-administrativo", name: "Direito Administrativo", block: "II", count: 5 },
      { subjectId: "direito-penal", name: "Direito Penal", block: "II", count: 5 },
      { subjectId: "direito-processual-penal", name: "Direito Processual Penal", block: "II", count: 5 },
      // Bloco III (20 questões)
      { subjectId: "legislacoes-pe", name: "Direitos e Garantias Fundamentais", block: "III", count: 10 },
      { subjectId: "direito-penal-militar", name: "Direito Penal Militar", block: "III", count: 5 },
      { subjectId: "direito-processual-penal-militar", name: "Direito Processual Penal Militar", block: "III", count: 5 },
    ],
  },
};
