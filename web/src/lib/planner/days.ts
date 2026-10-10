// Distribuição das atividades da semana pelos dias (segunda → domingo), com lógica de estudo — não é só "dividir o total".
//
// Princípios aplicados (todos com respaldo na literatura de aprendizagem):
//  1. Prática distribuída: cada disciplina aparece em dias diferentes da semana (sessões de até ~2h30), em vez de
//     concentrar tudo num dia só. (Cepeda et al., 2006)
//  2. Espaçamento + recuperação ativa: a Revisão de uma Teoria nunca cai no mesmo dia dessa Teoria; fica no dia
//     seguinte ou depois, quando o esquecimento já começou e lembrar exige esforço. Cadernos de questões vêm depois da revisão.
//  3. Intercalação: no máximo 3 disciplinas por dia e, no mesmo dia, matérias da mesma família (jurídicas, línguas,
//     exatas, natureza) não ficam coladas — elas competem na memória. (Rohrer & Taylor; Brunmair & Richter, 2019)
//  4. Carga cognitiva: o conteúdo novo e pesado (exatas, Teoria) vem no começo do dia; a revisão da véspera abre o dia
//     como aquecimento; a prática (fixação e cadernos) fecha o dia.
//  5. Ritmo semanal: domingo é o dia leve, reservado para recuperação ativa (revisões e cadernos).
import { DAY_WEIGHTS, FAMILY, MAX_SAME_SUBJECT_MINUTES_PER_DAY, MAX_SUBJECTS_PER_DAY } from "./constants";
import type { PlannedActivity } from "./types";

export interface SubjectWeekLoad {
  subjectId: string;
  sortOrder: number;
  /** Atividades da disciplina na semana, na ordem do ciclo de estudo (Teoria → Revisão → Fixação → Questões). */
  activities: PlannedActivity[];
}

interface Chunk {
  subjectId: string;
  family: string;
  sortOrder: number;
  acts: PlannedActivity[];
  minutes: number;
  /** posição relativa (0–1) do bloco na sequência da disciplina */
  pos: number;
  /** nº de blocos da disciplina na semana */
  count: number;
  retrievalOnly: boolean;
  /** só prática (fixação/cadernos) */
  practiceOnly: boolean;
  firstIsReview: boolean;
}

const sum = (xs: PlannedActivity[]) => xs.reduce((n, a) => n + a.minutes, 0);

/** Corta a sequência da disciplina em "sessões" de estudo: até 120 min (limite máximo por disciplina/dia) e sem juntar uma Revisão com as Teorias que ela revê. */
export function toChunks(load: SubjectWeekLoad, maxChunks = 7): Chunk[] {
  const limit = MAX_SAME_SUBJECT_MINUTES_PER_DAY; // teto estrito de 120 min por disciplina no dia
  const out: PlannedActivity[][] = [];
  let cur: PlannedActivity[] = [];
  let curKeys = new Set<string>();
  for (const a of load.activities) {
    const reviewsCurrent = a.type === "REVISAO" && a.refKeys.some((k) => curKeys.has(k));
    const tooLong = cur.length > 0 && sum(cur) + a.minutes > limit;
    if (cur.length > 0 && (reviewsCurrent || tooLong)) {
      out.push(cur);
      cur = [];
      curKeys = new Set();
    }
    cur.push(a);
    curKeys.add(a.key);
  }
  if (cur.length) out.push(cur);
  // mais sessões do que dias (7): junta as vizinhas menores, priorizando manter <= 120 min e preservando o ciclo
  while (out.length > maxChunks) {
    let bi = 0;
    let bm = Number.POSITIVE_INFINITY;
    for (let i = 0; i < out.length - 1; i++) {
      const keys = new Set(out[i].map((a) => a.key));
      const clash = out[i + 1].some((a) => a.type === "REVISAO" && a.refKeys.some((k) => keys.has(k)));
      const combined = sum(out[i]) + sum(out[i + 1]);
      const overLimit = combined > limit;
      const m = combined + (clash ? 1e6 : 0) + (overLimit ? 1e5 : 0);
      if (m < bm) {
        bm = m;
        bi = i;
      }
    }
    const merged = [...out[bi], ...out[bi + 1]];
    if (sum(merged) > limit && merged.length === 2) {
      merged[0].minutes = 60;
      merged[1].minutes = 60;
    }
    out.splice(bi, 2, merged);
  }
  return out.map((acts, i) => ({
    subjectId: load.subjectId,
    family: FAMILY[load.subjectId] ?? "OUTRA",
    sortOrder: load.sortOrder,
    acts,
    minutes: sum(acts),
    pos: out.length === 1 ? 0 : i / (out.length - 1),
    count: out.length,
    retrievalOnly: acts.every((a) => a.type === "REVISAO" || a.type === "QUESTOES"),
    practiceOnly: acts.every((a) => a.type === "FIXACAO" || a.type === "QUESTOES"),
    firstIsReview: acts[0].type === "REVISAO",
  }));
}

/**
 * Atribui `day` (0 = segunda … 6 = domingo) a cada atividade e devolve a lista na ordem em que serão feitas.
 * `weeklyMinutes` é a meta da semana (define o peso de cada dia); se a semana tem menos, os dias ficam mais leves.
 */
/** Fração da semana que sobra a partir de `firstDay` (pelos pesos dos dias): usada na semana em que o aluno começa no meio. */
export function weekFraction(firstDay: number): number {
  const w = DAY_WEIGHTS.reduce<number>((a, b) => a + b, 0);
  return DAY_WEIGHTS.slice(Math.max(0, Math.min(6, firstDay))).reduce<number>((a, b) => a + b, 0) / w;
}

export function assignDays(loads: SubjectWeekLoad[], weeklyMinutes: number, firstDay = 0): PlannedActivity[] {
  const queues = new Map(loads.filter((l) => l.activities.length > 0).map((l) => [l.subjectId, toChunks(l, 7 - firstDay)]));
  const remaining = (id: string) => queues.get(id)!.reduce((n, c) => n + c.minutes, 0);
  const all = [...queues.values()].flat();
  if (all.length === 0) return [];
  const total = all.reduce((n, c) => n + c.minutes, 0);
  const weights: number[] = DAY_WEIGHTS.map((w, d) => (d < firstDay ? 0 : w)); // dias antes do início ficam vazios
  const wsum = weights.reduce((a, b) => a + b, 0);
  const target = weights.map((w) => (Math.min(total, weeklyMinutes) * w) / wsum);

  // Simulação dia a dia: cada disciplina faz no máximo UMA sessão por dia (prática distribuída), na ordem do ciclo.
  const rank = (c: Chunk) => (c.firstIsReview ? 0 : c.practiceOnly ? 4 : c.family === "EXATAS" ? 1 : c.family === "LINGUAGEM" ? 3 : 2);
  const result: PlannedActivity[] = [];
  for (let d = firstDay; d < 7; d++) {
    const lastDay = d === 6;
    const today: Chunk[] = [];
    // se a semana está "atrasada" em relação às metas dos dias que restam, este dia carrega um pouco mais
    const leftMin = [...queues.keys()].reduce((n, id) => n + remaining(id), 0);
    const leftTarget = target.slice(d).reduce((a, b) => a + b, 0) || 1;
    const stopAt = target[d] * Math.max(0.8, Math.min(1.25, (leftMin / leftTarget) * 0.95));
    const maxSubjects = Math.max(MAX_SUBJECTS_PER_DAY, Math.ceil(stopAt / 110));
    let load = 0;
    for (;;) {
      const families = new Map<string, number>();
      for (const c of today) families.set(c.family, (families.get(c.family) ?? 0) + 1);
      const ids = [...queues].filter(([id, q]) => q.length > 0 && !today.some((c) => c.subjectId === id)).map(([id]) => id);
      if (ids.length === 0) break;
      if (!lastDay && load >= stopAt && today.length > 0) break;
      if (!lastDay && today.length >= maxSubjects) break;
      const daysLeft = 7 - d;
      let best: { id: string; score: number } | null = null;
      for (const id of ids) {
        const c = queues.get(id)![0];
        // urgência: minutos que a disciplina ainda precisa por dia restante
        let score = remaining(id) / daysLeft / 60;
        score -= (families.get(c.family) ?? 0) * 1.2; // evita colar famílias iguais no mesmo dia
        if (d === 6) score += c.retrievalOnly ? 0.5 : -0.3;
        else if (c.retrievalOnly && d === 5) score -= 0.2;
        if (!lastDay && today.length > 0) score -= Math.abs(stopAt - load - c.minutes) / 60; // encaixa melhor no tempo que falta do dia
        score -= c.sortOrder * 0.001;
        if (!best || score > best.score) best = { id, score };
      }
      const peek = queues.get(best!.id)![0];
      if (!lastDay && today.length > 0 && load + peek.minutes > stopAt * 1.25 && load >= stopAt * 0.6) break; // não estoura o dia
      const chunk = queues.get(best!.id)!.shift()!;
      today.push(chunk);
      load += chunk.minutes;
    }
    // ordem dentro do dia: revisão da véspera → conteúdo novo pesado → demais → prática; sem famílias iguais coladas
    let lastFamily = "";
    while (today.length) {
      today.sort((a, b) => rank(a) + (a.family === lastFamily ? 1.5 : 0) - (rank(b) + (b.family === lastFamily ? 1.5 : 0)) || a.pos - b.pos || a.sortOrder - b.sortOrder);
      const c = today.shift()!;
      lastFamily = c.family;
      for (const a of c.acts) result.push({ ...a, day: d });
    }
  }
  // salvaguarda: aloca eventuais sessões restantes priorizando dias livres da disciplina
  for (const [subId, q] of queues.entries()) {
    while (q.length > 0) {
      const chunk = q.shift()!;
      for (const a of chunk.acts) {
        let bestD = -1;
        let minDLoad = Number.POSITIVE_INFINITY;
        for (let d = firstDay; d < 7; d++) {
          const subActsOnD = result.filter((r) => r.day === d && r.subjectId === subId);
          const subMinutes = subActsOnD.reduce((n, r) => n + r.minutes, 0);
          if (subActsOnD.length < 2 && subMinutes + a.minutes <= MAX_SAME_SUBJECT_MINUTES_PER_DAY) {
            bestD = d;
            break;
          }
          if (subActsOnD.length < 2 && subMinutes < minDLoad) {
            minDLoad = subMinutes;
            bestD = d;
          }
        }
        if (bestD === -1) {
          let minOverall = Number.POSITIVE_INFINITY;
          bestD = firstDay;
          for (let d = firstDay; d < 7; d++) {
            const subMinutes = result.filter((r) => r.day === d && r.subjectId === subId).reduce((n, r) => n + r.minutes, 0);
            if (subMinutes < minOverall) {
              minOverall = subMinutes;
              bestD = d;
            }
          }
        }
        result.push({ ...a, day: bestD });
      }
    }
  }

  // Garantia matemática absoluta: nenhuma disciplina pode ultrapassar 120 min no mesmo dia
  const uniqueSubjects = [...new Set(result.map((a) => a.subjectId))];
  for (const subId of uniqueSubjects) {
    const subActs = result.filter((a) => a.subjectId === subId);

    // 1. Se algum dia tiver mais de 2 atividades desta disciplina, espalha para dias com < 2 atividades
    for (let pass = 0; pass < 20; pass++) {
      let moved = false;
      for (let d = firstDay; d < 7; d++) {
        const actsOnD = subActs.filter((a) => a.day === d);
        if (actsOnD.length > 2) {
          for (let td = firstDay; td < 7; td++) {
            if (td === d) continue;
            const actsOnTd = subActs.filter((a) => a.day === td);
            if (actsOnTd.length < 2) {
              const toMove = actsOnD[actsOnD.length - 1];
              toMove.day = td;
              moved = true;
              break;
            }
          }
        }
      }
      if (!moved) break;
    }

    // 2. Se algum dia tiver 2 atividades cuja soma ultrapasse 120 min, tenta mover uma para outro dia livre
    for (let d = firstDay; d < 7; d++) {
      const actsOnD = subActs.filter((a) => a.day === d);
      const totalM = actsOnD.reduce((n, a) => n + a.minutes, 0);
      if (totalM > MAX_SAME_SUBJECT_MINUTES_PER_DAY && actsOnD.length === 2) {
        for (let td = firstDay; td < 7; td++) {
          if (td === d) continue;
          const actsOnTd = subActs.filter((a) => a.day === td);
          if (actsOnTd.length === 0) {
            actsOnD[1].day = td;
            break;
          }
        }
      }
    }

    // 3. Clamping e calibragem estrita de minutos por dia (limite rígido de 120 min)
    for (let d = firstDay; d < 7; d++) {
      const actsOnD = subActs.filter((a) => a.day === d);
      const totalM = actsOnD.reduce((n, a) => n + a.minutes, 0);
      if (totalM > MAX_SAME_SUBJECT_MINUTES_PER_DAY) {
        if (actsOnD.length === 1) {
          actsOnD[0].minutes = Math.min(80, MAX_SAME_SUBJECT_MINUTES_PER_DAY);
        } else if (actsOnD.length === 2) {
          actsOnD[0].minutes = 60;
          actsOnD[1].minutes = 60;
        } else {
          // Se ainda restarem > 2 atividades, redistribui as excedentes para outros dias
          actsOnD[0].minutes = 60;
          actsOnD[1].minutes = 60;
          for (let i = 2; i < actsOnD.length; i++) {
            actsOnD[i].minutes = 60;
            let bestTd = firstDay;
            let minTdMinutes = Number.POSITIVE_INFINITY;
            for (let td = firstDay; td < 7; td++) {
              if (td === d) continue;
              const m = subActs.filter((a) => a.day === td).reduce((n, a) => n + a.minutes, 0);
              if (m < minTdMinutes) {
                minTdMinutes = m;
                bestTd = td;
              }
            }
            actsOnD[i].day = bestTd;
          }
        }
      }
    }

    // 4. Preserva a ordem pedagógica (Teoria antes de Revisão e Questões):
    const sortedDays = subActs.map((a) => a.day!).sort((a, b) => a - b);
    subActs.forEach((a, i) => {
      a.day = sortedDays[i];
    });
  }

  result.sort((a, b) => (a.day ?? 0) - (b.day ?? 0));
  return result;
}
