import type { Metadata } from "next";
import Link from "next/link";
import { RichContent } from "@/components/rich-content";
import { Alert, Badge, Card, PageHeader, SectionTitle, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { subjectName, subjectShort } from "@/lib/ui-format";
import { AutoSelect } from "./auto-select";
import { ReviewActions, type SegmentChoice } from "./review-actions";

export const metadata: Metadata = { title: "Revisão de questões" };

const STATUSES = ["DRAFT", "APPROVED", "FLAGGED", "RETIRED"] as const;
const LABEL = { DRAFT: "Rascunho", APPROVED: "Aprovada", FLAGGED: "Sinalizada", RETIRED: "Aposentada" } as const;
const PAGE = 15;

export default async function ReviewPage({ searchParams }: PageProps<"/admin/revisao">) {
  await requireAdmin();
  const sp = await searchParams;
  const status = (STATUSES as readonly string[]).includes(String(sp.status)) ? (sp.status as (typeof STATUSES)[number]) : "DRAFT";
  const subject = typeof sp.disciplina === "string" ? sp.disciplina : undefined;
  const aula = subject && typeof sp.assunto === "string" && sp.assunto.startsWith(`${subject}/`) ? sp.assunto : undefined;
  const banca = typeof sp.banca === "string" && sp.banca ? sp.banca : undefined;
  const page = Math.max(1, Number(sp.pagina) || 1);
  const where = { status, ...(subject ? { subjectId: subject } : {}), ...(aula ? { aulaId: aula } : {}), ...(banca ? { banca } : {}) };

  const [counts, reports, items, total, batches] = await Promise.all([
    db.question.groupBy({ by: ["status"], _count: true }),
    db.questionReport.findMany({ where: { status: "OPEN" }, orderBy: { createdAt: "asc" }, take: 20, include: { question: { select: { id: true, statement: true, aulaId: true } }, user: { select: { name: true, email: true } } } }),
    db.question.findMany({
      where,
      orderBy: [{ subjectId: "asc" }, { aulaId: "asc" }, { banca: "asc" }, { segmentId: "asc" }, { id: "asc" }],
      skip: (page - 1) * PAGE,
      take: PAGE,
      include: { options: { orderBy: { label: "asc" } } },
    }),
    db.question.count({ where }),
    db.question.groupBy({ by: ["batch"], where: { status: "DRAFT" }, _count: true }),
  ]);
  // opções dos filtros (contagens no status atual): matérias; assuntos (aulas) da matéria; bancas dentro do que já foi filtrado
  const [subjectOpts, aulaOpts, bancaOpts] = await Promise.all([
    db.question.groupBy({ by: ["subjectId"], where: { status }, _count: true, orderBy: { subjectId: "asc" } }),
    subject ? db.question.groupBy({ by: ["aulaId"], where: { status, subjectId: subject }, _count: true, orderBy: { aulaId: "asc" } }) : Promise.resolve([]),
    db.question.groupBy({ by: ["banca"], where: { status, ...(subject ? { subjectId: subject } : {}), ...(aula ? { aulaId: aula } : {}) }, _count: true, orderBy: { banca: "asc" } }),
  ]);
  const aulaRows = await db.aula.findMany({ where: { id: { in: [...new Set([...aulaOpts.map((a) => a.aulaId), ...items.map((q) => q.aulaId)])] } }, select: { id: true, title: true, shortTitle: true } });
  const aulaLabel = new Map(aulaRows.map((a) => [a.id, a.shortTitle || a.title]));
  // rascunhos do importador agrupados pelo assunto de origem (aprovação em bloco)
  const draftAssuntos =
    status === "DRAFT"
      ? await db.question.groupBy({
          by: ["tecMateria", "tecAssunto"],
          where: { status: "DRAFT", tecMateria: { not: null }, ...(subject ? { subjectId: subject } : {}) },
          _count: true,
        })
      : [];
  // trechos das disciplinas da página, para mover questões de atividade
  const subjectIds = [...new Set(items.map((q) => q.subjectId))];
  const segs = await db.segment.findMany({
    where: { aula: { subjectId: { in: subjectIds } } },
    orderBy: [{ aulaId: "asc" }, { sortOrder: "asc" }],
    select: { id: true, aulaId: true, startTopic: true, aula: { select: { subjectId: true, shortTitle: true, title: true } } },
  });
  const segChoices = new Map<string, SegmentChoice[]>();
  for (const sg of segs) {
    const list = segChoices.get(sg.aula.subjectId) ?? [];
    const aula = sg.aula.shortTitle || sg.aula.title;
    list.push({ id: sg.id, group: `${sg.aulaId.split("/")[1]} · ${aula}`, label: `${sg.id.split("/").slice(1).join("/")} · ${sg.startTopic ?? aula}` });
    segChoices.set(sg.aula.subjectId, list);
  }
  const byStatus = new Map(counts.map((c) => [c.status, c._count]));
  const qs = (p: Record<string, string | number | undefined>) => {
    const u = new URLSearchParams();
    for (const [k, v] of Object.entries({ status, disciplina: subject, assunto: aula, banca, ...p })) if (v !== undefined && v !== "") u.set(k, String(v));
    return `/admin/revisao?${u.toString()}`;
  };
  const pages = Math.max(1, Math.ceil(total / PAGE));

  return (
    <div className="space-y-6">
      <Link href="/admin" className="text-sm font-semibold text-muted underline">← Administração</Link>
      <PageHeader eyebrow="Administração" title="Revisão de questões" description="Somente questões aprovadas chegam aos alunos (em produção). Confira o gabarito e a redação antes de aprovar." />

      <nav className="flex flex-wrap gap-2" aria-label="Filtrar por status">
        {STATUSES.map((s) => (
          <Link key={s} href={qs({ status: s, pagina: 1 })} className={`rounded-full border px-4 py-1.5 text-sm font-semibold transition ${s === status ? "border-primary bg-primary-soft text-primary" : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"}`}>
            {LABEL[s]} <span className="tabular text-muted">{byStatus.get(s) ?? 0}</span>
          </Link>
        ))}
      </nav>

      <Card className="p-4">
        <form method="get" action="/admin/revisao" className="grid gap-3 sm:grid-cols-2 lg:grid-cols-[1fr_1.4fr_1fr_auto] lg:items-end">
          <input type="hidden" name="status" value={status} />
          <label className="space-y-1 text-xs font-semibold uppercase tracking-wider text-muted">
            Matéria
            <AutoSelect name="disciplina" defaultValue={subject ?? ""} className={inputCls} resetOnChange={["assunto", "banca"]}>
              <option value="">Todas</option>
              {subjectOpts.map((s) => <option key={s.subjectId} value={s.subjectId}>{subjectName(s.subjectId)} ({s._count})</option>)}
            </AutoSelect>
          </label>
          <label className="space-y-1 text-xs font-semibold uppercase tracking-wider text-muted">
            Assunto
            <AutoSelect name="assunto" defaultValue={aula ?? ""} disabled={!subject} className={inputCls} resetOnChange={["banca"]}>
              <option value="">{subject ? "Todos" : "Escolha a matéria"}</option>
              {aulaOpts.map((a) => <option key={a.aulaId} value={a.aulaId}>{aulaLabel.get(a.aulaId) ?? a.aulaId} ({a._count})</option>)}
            </AutoSelect>
          </label>
          <label className="space-y-1 text-xs font-semibold uppercase tracking-wider text-muted">
            Banca
            <AutoSelect name="banca" defaultValue={banca ?? ""} className={inputCls}>
              <option value="">Todas</option>
              {bancaOpts.map((b) => <option key={b.banca} value={b.banca}>{b.banca} ({b._count})</option>)}
            </AutoSelect>
          </label>
          <div className="flex gap-2">
            {(subject || aula || banca) && <Link href={`/admin/revisao?status=${status}`} className="rounded-lg border border-border px-4 py-2 text-sm font-semibold text-muted hover:text-text">Limpar</Link>}
          </div>
        </form>
        <p className="mt-2 text-xs text-muted">Os filtros se aplicam ao mudar. O assunto aparece depois de escolher a matéria.</p>
      </Card>

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

      {draftAssuntos.length > 0 && (
        <Card className="space-y-2">
          <p className="font-display text-xl font-bold uppercase tracking-wide">Rascunhos por assunto de origem</p>
          <ul className="space-y-2">
            {draftAssuntos.map((a) => (
              <li key={`${a.tecMateria}|${a.tecAssunto}`} className="flex flex-wrap items-center justify-between gap-2 text-sm">
                <span>
                  {a.tecMateria} · <strong>{a.tecAssunto || "(sem assunto)"}</strong> · {a._count}
                </span>
                {a.tecMateria && <ReviewActions kind="assunto" materia={a.tecMateria} assunto={a.tecAssunto ?? ""} count={a._count} />}
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
        {items.length === 0 ? <Alert tone="info">Nada aqui.</Alert> : items.map((q, i) => (
          <div key={q.id} className="space-y-3">
          {(i === 0 || items[i - 1].subjectId !== q.subjectId || items[i - 1].aulaId !== q.aulaId) && (
            <h3 className="border-b border-border pb-1 pt-2 font-display text-lg font-bold uppercase tracking-wide">
              {subjectName(q.subjectId)} <span className="text-muted">› {aulaLabel.get(q.aulaId) ?? q.aulaId}</span>
            </h3>
          )}
          <Card className="space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-muted">
              <span>{subjectShort(q.subjectId)} · {q.id}</span>
              <span className="flex gap-1.5">
                <Badge>{q.banca}</Badge>
                {q.ano && <Badge>{q.ano}</Badge>}
                {q.kind === "CERTO_ERRADO" && <Badge>C/E</Badge>}
                {q.classifiedBy === "MANUAL" && <Badge>revisada</Badge>}
              </span>
            </div>
            {q.tecMateria && (
              <p className="text-xs text-muted">
                Origem: {q.tecMateria} · <strong className="text-text">{q.tecAssunto || "(sem assunto)"}</strong>
                {q.orgao && ` · ${q.orgao}`} · trecho atual <strong className="text-text">{q.segmentId}</strong>
                {q.classifyNote && <span className="block">Importador: {q.classifyNote}</span>}
              </p>
            )}
            {q.support && (
              <div className="rounded-lg bg-surface-2 p-3 text-sm">
                <RichContent content={q.support} />
              </div>
            )}
            <div className="text-sm leading-relaxed">
              <RichContent content={q.statement} />
            </div>
            <ul className="space-y-1 text-sm">
              {q.options.map((o) => (
                <li key={o.label} className={`flex gap-2.5 rounded-lg px-3 py-1.5 ${o.isCorrect ? "bg-ok/12 text-ok" : "text-muted"}`}>
                  <strong className="font-display text-base">{o.label}</strong>
                  <div className="flex-1">
                    <RichContent content={o.text} />
                  </div>
                </li>
              ))}
            </ul>
            {q.explanation && (
              <div className="text-sm text-muted">
                <strong className="text-text">Comentário: </strong>
                <RichContent content={q.explanation} />
              </div>
            )}
            <ReviewActions kind="question" id={q.id} status={q.status} segmentId={q.segmentId} segments={segChoices.get(q.subjectId)} />
          </Card>
          </div>
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
