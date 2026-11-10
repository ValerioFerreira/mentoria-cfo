import type { Metadata } from "next";
import Link from "next/link";
import { Badge, Card, EmptyState, PageHeader } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { volumeInfo } from "@/lib/material";
import { MaterialReportActions } from "./actions";

export const metadata: Metadata = { title: "Erros reportados" };

const STATUS = { OPEN: "Aberto", RESOLVED: "Corrigido", DISCARDED: "Descartado" } as const;

export default async function MaterialReportsPage({ searchParams }: { searchParams: Promise<{ status?: string }> }) {
  await requireAdmin();
  const { status } = await searchParams;
  const filter = status === "RESOLVED" || status === "DISCARDED" || status === "ALL" ? status : "OPEN";
  const reports = await db.materialErrorReport.findMany({
    where: filter === "ALL" ? {} : { status: filter },
    orderBy: { createdAt: "desc" },
    take: 300,
    include: { user: { select: { name: true, email: true } } },
  });
  const tabs = [["OPEN", "Abertos"], ["RESOLVED", "Corrigidos"], ["DISCARDED", "Descartados"], ["ALL", "Todos"]] as const;
  return (
    <div className="space-y-6">
      <Link href="/admin" className="text-sm font-semibold text-primary">← Administração</Link>
      <PageHeader eyebrow="Material MentorIA" title="Erros reportados" description="Relatos dos alunos sobre erros nos PDFs: volume, página e explicação. Corrija no capítulo indicado, gere o PDF de novo e marque como corrigido." />
      <div className="flex flex-wrap gap-2">
        {tabs.map(([k, l]) => (
          <Link key={k} href={`/admin/erros-material?status=${k}`} className={`rounded-xl px-3.5 py-2 text-sm font-semibold ${filter === k ? "bg-surface text-text shadow-card" : "bg-surface-2 text-muted hover:text-text"}`}>
            {l}
          </Link>
        ))}
      </div>
      {reports.length === 0 ? (
        <EmptyState title="Nenhum relato aqui">Quando um aluno reportar um erro no PDF, ele aparece nesta lista.</EmptyState>
      ) : (
        <div className="space-y-3">
          {reports.map((r) => (
            <Card key={r.id} className="space-y-3 p-4">
              <div className="flex flex-wrap items-center gap-2 text-sm">
                <Badge tone={r.status === "OPEN" ? "warn" : r.status === "RESOLVED" ? "ok" : "neutral"}>{STATUS[r.status as keyof typeof STATUS] ?? r.status}</Badge>
                <span className="font-semibold">{volumeInfo(r.volumeId)?.titulo ?? r.volumeId}</span>
                <span className="text-muted">· volume {r.volumeId} · pág. {r.page}{r.chapter ? ` · trecho ${r.chapter}` : ""}</span>
              </div>
              <p className="whitespace-pre-wrap text-sm">{r.message}</p>
              <p className="text-xs text-muted">
                {r.user.name ?? r.user.email} · {r.user.email} · {r.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" })}
              </p>
              {r.adminNote && <p className="text-xs text-muted">Observação: {r.adminNote}</p>}
              <MaterialReportActions id={r.id} status={r.status} />
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
