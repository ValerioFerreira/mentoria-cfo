import type { Metadata } from "next";
import Link from "next/link";
import { Alert, Badge, Card, PageHeader, SectionTitle } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { subjectShort } from "@/lib/ui-format";
import { ReviewActions } from "./review-actions";

export const metadata: Metadata = { title: "Revisão de questões" };

const STATUSES = ["DRAFT", "APPROVED", "FLAGGED", "RETIRED"] as const;
const LABEL = { DRAFT: "Rascunho", APPROVED: "Aprovada", FLAGGED: "Sinalizada", RETIRED: "Aposentada" } as const;
const PAGE = 15;

export default async function ReviewPage({ searchParams }: PageProps<"/admin/revisao">) {
  await requireAdmin();
  const sp = await searchParams;
  const status = (STATUSES as readonly string[]).includes(String(sp.status)) ? (sp.status as (typeof STATUSES)[number]) : "DRAFT";
  const subject = typeof sp.disciplina === "string" ? sp.disciplina : undefined;
  const page = Math.max(1, Number(sp.pagina) || 1);

  const [counts, reports, items, total, batches] = await Promise.all([
    db.question.groupBy({ by: ["status"], _count: true }),
    db.questionReport.findMany({ where: { status: "OPEN" }, orderBy: { createdAt: "asc" }, take: 20, include: { question: { select: { id: true, statement: true, aulaId: true } }, user: { select: { name: true, email: true } } } }),
    db.question.findMany({
      where: { status, ...(subject ? { subjectId: subject } : {}) },
      orderBy: [{ aulaId: "asc" }, { segmentId: "asc" }, { id: "asc" }],
      skip: (page - 1) * PAGE,
      take: PAGE,
      include: { options: { orderBy: { label: "asc" } } },
    }),
    db.question.count({ where: { status, ...(subject ? { subjectId: subject } : {}) } }),
    db.question.groupBy({ by: ["batch"], where: { status: "DRAFT" }, _count: true }),
  ]);
  const byStatus = new Map(counts.map((c) => [c.status, c._count]));
  const qs = (p: Record<string, string | number | undefined>) => {
    const u = new URLSearchParams();
    for (const [k, v] of Object.entries({ status, disciplina: subject, ...p })) if (v !== undefined && v !== "") u.set(k, String(v));
    return `/admin/revisao?${u.toString()}`;
  };
  const pages = Math.max(1, Math.ceil(total / PAGE));

  return (
    <div className="space-y-6">
      <PageHeader eyebrow="Administração" title="Revisão de questões" description="Somente questões aprovadas chegam aos alunos (em produção). Confira o gabarito e a redação antes de aprovar." />

      <nav className="flex flex-wrap gap-2" aria-label="Filtrar por status">
        {STATUSES.map((s) => (
          <Link key={s} href={qs({ status: s, pagina: 1 })} className={`rounded-full border px-4 py-1.5 text-sm font-semibold transition ${s === status ? "border-primary bg-primary-soft text-primary" : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"}`}>
            {LABEL[s]} <span className="tabular text-muted">{byStatus.get(s) ?? 0}</span>
          </Link>
        ))}
      </nav>

      {batches.length > 0 && status === "DRAFT" && (
        <Card className="space-y-2">
          <p className="font-display text-xl font-bold uppercase tracking-wide">Aprovação em lote</p>
          <ul className="space-y-2">
            {batches.map((b) => (
              <li key={b.batch ?? "-"} className="flex flex-wrap items-center justify-between gap-2 text-sm">
                <span>Lote <strong>{b.batch ?? "(sem lote)"}</strong> · {b._count} rascunhos</span>
                {b.batch && <ReviewActions kind="batch" batch={b.batch} />}
              </li>
            ))}
          </ul>
        </Card>
      )}

      {reports.length > 0 && (
        <section className="space-y-2" aria-labelledby="rep">
          <SectionTitle id="rep">Denúncias de alunos ({reports.length})</SectionTitle>
          {reports.map((r) => (
            <Card key={r.id} className="space-y-2 p-4 text-sm">
              <p className="text-xs text-muted">{r.user.name ?? r.user.email} · {r.question.aulaId}</p>
              <p className="line-clamp-2">{r.question.statement}</p>
              <p className="rounded-md bg-warn-soft p-2 text-warn">{r.reason}</p>
              <ReviewActions kind="report" reportId={r.id} />
            </Card>
          ))}
        </section>
      )}

      <section className="space-y-3" aria-labelledby="lst">
        <SectionTitle id="lst">{LABEL[status]} ({total})</SectionTitle>
        {items.length === 0 ? <Alert tone="info">Nada aqui.</Alert> : items.map((q) => (
          <Card key={q.id} className="space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-muted">
              <span>{subjectShort(q.subjectId)} · {q.id}</span>
              <span className="flex gap-1.5"><Badge>{q.pattern}</Badge><Badge>dific. {q.difficulty}</Badge>{q.pageRef && <Badge>pág. {q.pageRef}</Badge>}</span>
            </div>
            {q.support && <div className="whitespace-pre-line rounded-lg bg-surface-2 p-3 text-sm">{q.support}</div>}
            <p className="whitespace-pre-line text-sm leading-relaxed">{q.statement}</p>
            <ul className="space-y-1 text-sm">
              {q.options.map((o) => (
                <li key={o.label} className={`flex gap-2.5 rounded-lg px-3 py-1.5 ${o.isCorrect ? "bg-ok/12 text-ok" : "text-muted"}`}><strong className="font-display text-base">{o.label}</strong><span>{o.text}</span></li>
              ))}
            </ul>
            <p className="text-sm text-muted"><strong className="text-text">Comentário: </strong>{q.explanation}</p>
            <ReviewActions kind="question" id={q.id} status={q.status} />
          </Card>
        ))}
        {pages > 1 && (
          <div className="flex items-center justify-between text-sm">
            {page > 1 ? <Link href={qs({ pagina: page - 1 })} className="font-semibold text-primary hover:underline">← Anterior</Link> : <span />}
            <span className="text-muted tabular">Página {page} de {pages}</span>
            {page < pages ? <Link href={qs({ pagina: page + 1 })} className="font-semibold text-primary hover:underline">Próxima →</Link> : <span />}
          </div>
        )}
      </section>
    </div>
  );
}
