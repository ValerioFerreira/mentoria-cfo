// Formatação de datas/tempos e rótulos curtos para a interface.

export const SUBJECT_SHORT: Record<string, string> = {
  "lingua-portuguesa": "Português",
  "lingua-inglesa": "Inglês",
  "lingua-espanhola": "Espanhol",
  informatica: "Informática",
  estatistica: "Estatística",
  matematica: "Matemática",
  fisica: "Física",
  quimica: "Química",
  biologia: "Biologia",
  "direito-constitucional": "D. Constitucional",
  "direito-administrativo": "D. Administrativo",
  "legislacoes-pe": "Legislações PE",
  "direito-penal-militar": "D. Penal Militar",
  "raciocinio-logico": "R. Lógico",
  "historia-pe": "História PE",
  atualidades: "Atualidades",
};

export const subjectShort = (id: string) => SUBJECT_SHORT[id] ?? id;

/** Nome por extenso, mas sem o título oficial gigante (para listas com espaço). */
export const SUBJECT_NAME: Record<string, string> = {
  "lingua-portuguesa": "Língua Portuguesa",
  "lingua-inglesa": "Língua Inglesa",
  "lingua-espanhola": "Língua Espanhola",
  informatica: "Informática",
  estatistica: "Estatística",
  matematica: "Matemática",
  fisica: "Física",
  quimica: "Química",
  biologia: "Biologia",
  "direito-constitucional": "Direito Constitucional",
  "direito-administrativo": "Direito Administrativo",
  "legislacoes-pe": "Legislações Militares de PE",
  "direito-penal-militar": "Direito Penal Militar",
  "raciocinio-logico": "Raciocínio Lógico",
  "historia-pe": "História de Pernambuco",
  atualidades: "Atualidades",
};
export const subjectName = (id: string) => SUBJECT_NAME[id] ?? id;

const fmtDM = new Intl.DateTimeFormat("pt-BR", { day: "2-digit", month: "2-digit", timeZone: "UTC" });

/** "12/10 – 18/10" para a semana que começa em `start` (segunda, em UTC). */
export function weekRange(start: Date): string {
  const end = new Date(start.getTime() + 6 * 86_400_000);
  return `${fmtDM.format(start)} – ${fmtDM.format(end)}`;
}

export function fmtDate(d: Date): string {
  return new Intl.DateTimeFormat("pt-BR", { day: "2-digit", month: "long", year: "numeric", timeZone: "UTC" }).format(d);
}

/** 3725 → "1h02" ; 540 → "9 min" ; 40 → "40 s" ; 0 → "0 min" */
export function fmtDuration(seconds: number): string {
  const s = Math.max(0, Math.round(seconds));
  if (s === 0) return "0 min";
  if (s < 60) return `${s} s`;
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  if (h === 0) return `${m} min`;
  return `${h}h${String(m).padStart(2, "0")}`;
}

export function fmtClock(ms: number): string {
  const total = Math.max(0, Math.floor(ms / 1000));
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  const mm = String(m).padStart(2, "0");
  const ss = String(s).padStart(2, "0");
  return h > 0 ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}

export const STATUS_LABEL = { PENDING: "A fazer", IN_PROGRESS: "Em andamento", DONE: "Concluída", SKIPPED: "Pulada" } as const;
