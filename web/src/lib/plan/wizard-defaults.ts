// Pré-seleção do assistente ao refazer o planejamento: reconstrói, a partir do plano vigente, tudo o que o aluno
// escolheu antes (disciplinas, assuntos desmarcados, horas, data da prova, início, anamnese, nível e Modo Turbo).
// Funções puras (sem banco) para poderem ser testadas.
import type { Mark } from "@/lib/anamnesis";
import type { DiagnosticAnswer } from "@/lib/diagnostic";

export interface DefaultsSubject {
  id: string;
  languageGroup: string | null;
  items: { id: string; aulaIds: string[] }[];
}

export interface SavedPlan {
  startDate: string;
  examDate: string;
  params: unknown;
  subjects: { subjectId: string; diagnostic: unknown }[];
}

/** Estado inicial do assistente (valores serializáveis, vindos do servidor). */
export interface WizardInitial {
  selected: string[];
  unselectedTopics: string[];
  hours: number;
  examDate: string;
  /** "now" quando o início anterior já passou; senão a data que o aluno havia escolhido */
  startMode: "now" | "date";
  startPick: string;
  answers: Record<string, DiagnosticAnswer>;
  marks: Record<string, 1 | 2>;
  turbo: boolean;
}

const rec = (v: unknown): Record<string, unknown> => (v && typeof v === "object" && !Array.isArray(v) ? (v as Record<string, unknown>) : {});

function readAnswer(diag: Record<string, unknown>): DiagnosticAnswer | null {
  const { experience, self, hitRate } = diag;
  if ([0, 1, 2, 3].includes(experience as number) && [1, 2, 3, 4, 5].includes(self as number) && ["none", "low", "mid", "high"].includes(hitRate as string)) {
    return { experience, self, hitRate } as DiagnosticAnswer;
  }
  return null;
}

/**
 * Devolve o estado inicial do assistente a partir do plano anterior, ou `null` quando não há o que aproveitar
 * (o assistente então usa os padrões). Só entram disciplinas que ainda existem no concurso do aluno.
 */
export function wizardDefaultsFromPlan(plan: SavedPlan | null, subjects: DefaultsSubject[], todayIso: string): WizardInitial | null {
  if (!plan) return null;
  const byId = new Map(subjects.map((s) => [s.id, s]));
  const kept = plan.subjects.filter((s) => byId.has(s.subjectId));
  if (kept.length === 0) return null;

  const params = rec(plan.params);
  const request = rec(params.request);
  const excludedAulas = new Set(Array.isArray(request.excludedAulas) ? (request.excludedAulas as string[]) : []);

  const answers: Record<string, DiagnosticAnswer> = {};
  const marks: Record<string, 1 | 2> = {};
  const unselected = new Set<string>();
  const known: Record<string, 1 | 2> = {};

  for (const s of kept) {
    const diag = rec(s.diagnostic);
    const answer = readAnswer(diag);
    if (answer) answers[s.subjectId] = answer;
    for (const [aulaId, v] of Object.entries(rec(diag.aulas))) if (v === 1 || v === 2) known[aulaId] = v;

    const subject = byId.get(s.subjectId)!;
    const validItems = new Set(subject.items.map((i) => i.id));
    if (Array.isArray(diag.unselectedTopics)) {
      // guardado como veio do assistente (planos novos)
      for (const id of diag.unselectedTopics as string[]) if (validItems.has(id)) unselected.add(id);
      for (const [id, v] of Object.entries(rec(diag.marks))) if (validItems.has(id) && (v === 1 || v === 2)) marks[id] = v;
    } else {
      // plano antigo: só havia as aulas; deduz os assuntos (assunto cujas aulas saíram do plano = desmarcado;
      // assunto cujas aulas foram todas marcadas = marcado com o menor nível)
      for (const item of subject.items) {
        if (item.aulaIds.length === 0) continue;
        if (item.aulaIds.every((a) => excludedAulas.has(a))) {
          unselected.add(item.id);
          continue;
        }
        const levels = item.aulaIds.map((a) => known[a] ?? 0);
        const floor = Math.min(...levels);
        if (floor > 0) marks[item.id] = floor as Mark as 1 | 2;
      }
    }
  }

  const hours = typeof params.hoursPerWeek === "number" ? params.hoursPerWeek : null;
  const firstStudy = typeof params.firstStudyDate === "string" ? params.firstStudyDate : plan.startDate;
  const future = firstStudy >= todayIso && firstStudy < plan.examDate;

  return {
    selected: kept.map((s) => s.subjectId),
    unselectedTopics: [...unselected],
    hours: hours !== null ? Math.min(50, Math.max(14, hours)) : 38,
    examDate: plan.examDate,
    startMode: future ? "date" : "now",
    startPick: future ? firstStudy : todayIso,
    answers,
    marks,
    turbo: request.turbo === true || params.turbo === true,
  };
}
