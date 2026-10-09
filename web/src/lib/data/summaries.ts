import "server-only";
import { db } from "@/lib/db";
import { groupSummaries, type SummaryRow } from "@/lib/summaries";

/** Quantos resumos preenchidos o aluno tem em cada disciplina. */
export async function getSummaryCounts(userId: string): Promise<Map<string, number>> {
  const notes = await db.note.findMany({ where: { userId }, select: { text: true, segment: { select: { aula: { select: { subjectId: true } } } } } });
  const counts = new Map<string, number>();
  for (const n of notes) {
    if (!n.text.trim()) continue;
    const id = n.segment.aula.subjectId;
    counts.set(id, (counts.get(id) ?? 0) + 1);
  }
  return counts;
}

/** Resumos de uma disciplina, por aula, e a atividade de Teoria em que cada um foi escrito (para editar). */
export async function getSubjectSummaries(userId: string, subjectId: string) {
  const notes = await db.note.findMany({
    where: { userId, segment: { aula: { subjectId } } },
    select: {
      text: true,
      updatedAt: true,
      segment: { select: { id: true, sortOrder: true, startTopic: true, aula: { select: { id: true, number: true, shortTitle: true } } } },
    },
  });
  const rows: SummaryRow[] = notes.map((n) => ({
    text: n.text, updatedAt: n.updatedAt, segmentOrder: n.segment.sortOrder, topic: n.segment.startTopic, aula: n.segment.aula, segmentId: n.segment.id,
  }));
  const groups = groupSummaries(rows);

  const segmentIds = groups.flatMap((g) => g.items.map((i) => i.segmentId));
  const links = segmentIds.length
    ? await db.activitySegment.findMany({
        where: { segmentId: { in: segmentIds }, activity: { type: "TEORIA", week: { plan: { userId } } } },
        select: { segmentId: true, activityId: true, activity: { select: { week: { select: { plan: { select: { version: true } } } } } } },
      })
    : [];
  // se o aluno refez o plano, vale a atividade do plano mais recente
  const activityOf = new Map<string, { id: string; version: number }>();
  for (const l of links) {
    const version = l.activity.week.plan.version;
    const cur = activityOf.get(l.segmentId);
    if (!cur || version > cur.version) activityOf.set(l.segmentId, { id: l.activityId, version });
  }
  return groups.map((g) => ({ ...g, items: g.items.map((i) => ({ ...i, activityId: activityOf.get(i.segmentId)?.id ?? null })) }));
}
