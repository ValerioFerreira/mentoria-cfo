"use client";

import {
  AlertTriangle,
  BookOpen,
  Check,
  Download,
  FileText,
  Gavel,
  Lightbulb,
  PartyPopper,
  Printer,
  Scale,
  Sparkles,
  X,
} from "lucide-react";
import { useState, useTransition, type ReactNode } from "react";
import { Button, Card, cx } from "@/components/ui";
import { answerBizuItem } from "@/lib/study/actions";

export interface BizuItemView {
  id: string;
  statement: string;
  isTrue: boolean;
  explanation: string;
}

/** Itens Certo/Errado de fixação rápida. Mostra o gabarito e a explicação depois de responder. */
export function BizuItems({ activityId, items }: { activityId: string; items: BizuItemView[] }) {
  const [answers, setAnswers] = useState<Record<string, boolean>>({});
  const [, start] = useTransition();
  if (items.length === 0) return null;
  const answered = Object.keys(answers).length;
  const hits = items.filter((i) => answers[i.id] === i.isTrue).length;
  return (
    <div className="space-y-3 pt-2">
      <div className="flex items-center justify-between gap-3">
        <p className="eyebrow">Certo ou Errado · Fixação Imediata</p>
        <div className="flex items-center gap-1.5" aria-label={`${answered} de ${items.length} respondidos`}>
          {items.map((it) => {
            const g = answers[it.id];
            return <span key={it.id} className={cx("h-2 w-6 rounded-full transition-colors duration-300", g === undefined ? "bg-surface-3" : g === it.isTrue ? "bg-ok" : "bg-primary")} />;
          })}
        </div>
      </div>
      {items.map((it, idx) => {
        const given = answers[it.id];
        const has = given !== undefined;
        const ok = has && given === it.isTrue;
        return (
          <div
            key={it.id}
            className={cx(
              "rounded-2xl border bg-surface p-4 shadow-card transition-colors duration-300",
              !has && "border-border",
              has && ok && "border-ok/50 bg-ok/5",
              has && !ok && "border-primary/50 bg-primary-soft/60",
            )}
          >
            <p className="flex gap-3 text-[15px] leading-relaxed">
              <span className="font-display text-xl font-bold leading-6 tabular text-muted">{idx + 1}</span>
              <span>{it.statement}</span>
            </p>
            <div className="mt-3 flex flex-wrap items-center gap-2 pl-7" role="group" aria-label={`Item ${idx + 1}: certo ou errado`}>
              {([true, false] as const).map((v) => {
                const chosen = has && given === v;
                return (
                  <button
                    key={String(v)}
                    type="button"
                    disabled={has}
                    onClick={() => {
                      setAnswers((a) => ({ ...a, [it.id]: v }));
                      start(async () => { await answerBizuItem(it.id, activityId, v); });
                    }}
                    className={cx(
                      "inline-flex cursor-pointer items-center gap-1.5 rounded-xl border px-4 py-1.5 text-sm font-bold transition duration-200 active:scale-95 disabled:cursor-default",
                      chosen ? (ok ? "pop border-ok bg-ok text-white" : "pop border-primary bg-primary text-on-primary") : has ? "border-border bg-surface opacity-50" : "border-border bg-surface hover:-translate-y-px hover:border-border-strong hover:shadow-card",
                    )}
                  >
                    {v ? <Check className="h-4 w-4" strokeWidth={3} aria-hidden /> : <X className="h-4 w-4" strokeWidth={3} aria-hidden />}
                    {v ? "Certo" : "Errado"}
                  </button>
                );
              })}
              {has && <span className={cx("pop text-sm font-bold", ok ? "text-ok" : "text-primary")}>{ok ? "Acertou" : `Gabarito: ${it.isTrue ? "Certo" : "Errado"}`}</span>}
            </div>
            {has && <p className="page-in mt-3 border-t border-border pt-3 pl-7 text-sm leading-relaxed text-muted">{it.explanation}</p>}
          </div>
        );
      })}
      {answered === items.length && (
        <div className="pop flex items-center gap-3 rounded-2xl bg-gold-soft px-4 py-3 text-gold-text">
          <PartyPopper className="h-5 w-5 shrink-0" aria-hidden />
          <p className="text-sm font-bold">Você acertou {hits} de {items.length}.</p>
        </div>
      )}
    </div>
  );
}

function formatInline(text: string): ReactNode[] {
  // Trata **negrito**, *itálico*, `código` e destaques
  const parts = text.split(/(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g);
  return parts.map((part, idx) => {
    if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
      return (
        <strong key={idx} className="font-bold text-text">
          {part.slice(2, -2)}
        </strong>
      );
    }
    if (part.startsWith("*") && part.endsWith("*") && part.length > 2) {
      return (
        <em key={idx} className="italic text-text">
          {part.slice(1, -1)}
        </em>
      );
    }
    if (part.startsWith("`") && part.endsWith("`") && part.length > 2) {
      return (
        <code key={idx} className="rounded bg-surface-3 px-1.5 py-0.5 font-mono text-xs font-semibold text-text">
          {part.slice(1, -1)}
        </code>
      );
    }
    return <span key={idx}>{part}</span>;
  });
}

function renderTable(tableBlock: string, blockIdx: number): ReactNode {
  const lines = tableBlock.trim().split("\n").map((l) => l.trim()).filter(Boolean);
  if (lines.length < 2) return null;

  const headerLine = lines[0];
  const bodyLines = lines.slice(1).filter((l) => !l.replace(/[\s|:-]/g, "").length === false);

  const parseCells = (row: string) =>
    row
      .replace(/^\|/, "")
      .replace(/\|$/, "")
      .split("|")
      .map((c) => c.trim());

  const headers = parseCells(headerLine);

  return (
    <div key={`tbl-${blockIdx}`} className="my-4 overflow-x-auto rounded-xl border border-border/80 bg-surface shadow-xs">
      <table className="w-full text-left text-sm">
        <thead className="border-b border-border/80 bg-surface-2/80 text-xs font-bold uppercase tracking-wider text-muted">
          <tr>
            {headers.map((h, i) => (
              <th key={i} className="px-4 py-3">
                {formatInline(h)}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-border/40">
          {bodyLines.map((rowStr, rowIdx) => {
            const cells = parseCells(rowStr);
            return (
              <tr key={rowIdx} className="hover:bg-surface-2/40 transition-colors">
                {cells.map((cell, cellIdx) => (
                  <td key={cellIdx} className="px-4 py-2.5 text-text/90 align-top leading-relaxed">
                    {formatInline(cell)}
                  </td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export function BizuSummary({
  markdown,
  title,
}: {
  markdown: string;
  title?: string;
}) {
  const rawBlocks = markdown
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean);

  const handleDownloadPdf = () => {
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  return (
    <article className="bizu-sheet relative rounded-2xl border border-border/80 bg-surface p-6 shadow-sm sm:p-9 space-y-6 print:p-0 print:border-none print:shadow-none print:bg-transparent">
      {/* Cabeçalho da Folha de PDF */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-border/60 pb-4">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="grid h-6 w-6 place-items-center rounded-lg bg-primary/10 text-primary">
              <FileText className="h-3.5 w-3.5" aria-hidden />
            </span>
            <span className="font-display text-xs font-bold uppercase tracking-wider text-muted">
              MentorIA · Caderno Teórico & Síntese Analítica
            </span>
          </div>
          {title && (
            <h2 className="font-display text-xl font-bold uppercase text-text sm:text-2xl">
              {title}
            </h2>
          )}
        </div>

        <Button
          type="button"
          onClick={handleDownloadPdf}
          size="sm"
          variant="secondary"
          className="no-print gap-1.5 text-xs font-semibold"
          title="Baixar PDF / Imprimir resumo"
        >
          <Download className="h-3.5 w-3.5 text-primary" aria-hidden />
          <span>Baixar PDF</span>
        </Button>
      </div>

      {/* Corpo de Leitura Contínua e Analítica (Estilo Apostila / Livro) */}
      <div className="space-y-4 text-[15.5px] leading-[1.75] text-text/90">
        {rawBlocks.map((block, i) => {
          // 1. Tabela Markdown
          if (block.includes("|") && block.includes("\n") && block.split("\n")[0].trim().startsWith("|")) {
            return renderTable(block, i);
          }

          // 2. Cabeçalhos Multiníveis
          if (block.startsWith("## ")) {
            const titleText = block.replace(/^##\s*/, "");
            return (
              <div key={i} className="pt-6 pb-1">
                <h2 className="flex items-center gap-2.5 font-display text-lg font-bold uppercase tracking-tight text-primary border-b border-primary/20 pb-1">
                  <span className="h-4 w-1.5 rounded-full bg-primary" />
                  {titleText}
                </h2>
              </div>
            );
          }

          if (block.startsWith("### ")) {
            const titleText = block.replace(/^###\s*/, "");
            return (
              <div key={i} className="pt-4 pb-0.5">
                <h3 className="flex items-center gap-2 font-display text-base font-bold uppercase tracking-wide text-text">
                  <span className="h-3.5 w-1 rounded-full bg-gold" />
                  {titleText}
                </h3>
              </div>
            );
          }

          if (block.startsWith("#### ")) {
            const titleText = block.replace(/^####\s*/, "");
            return (
              <div key={i} className="pt-2 pb-0.5">
                <h4 className="font-semibold text-sm text-text/95 uppercase tracking-wide">
                  {titleText}
                </h4>
              </div>
            );
          }

          // 3. Quadro de Atenção / Pegadinha da Banca (> ⚠️ ou ⚠️)
          if (
            block.startsWith("> ⚠️") ||
            block.startsWith("⚠️") ||
            block.startsWith("> **Atenção") ||
            block.startsWith("**Atenção") ||
            block.startsWith("> **Cuidado") ||
            block.startsWith("**Cuidado")
          ) {
            const clean = block.replace(/^>\s*/, "").replace(/^⚠️\s*/, "");
            return (
              <div
                key={i}
                className="my-3 flex items-start gap-3 rounded-xl border-l-4 border-amber-500 bg-amber-500/10 p-4 text-[14.5px] leading-relaxed text-amber-950 dark:text-amber-100"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded bg-amber-500/20 text-amber-600 dark:text-amber-400">
                  <AlertTriangle className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean)}</div>
              </div>
            );
          }

          // 4. Quadro de Bizu Estratégico / Mnemônico (> 📌 ou 📌)
          if (
            block.startsWith("> 📌") ||
            block.startsWith("📌") ||
            block.startsWith("> **Bizu") ||
            block.startsWith("**Bizu") ||
            block.startsWith("> **Mnemônico") ||
            block.startsWith("**Mnemônico")
          ) {
            const clean = block.replace(/^>\s*/, "").replace(/^📌\s*/, "");
            return (
              <div
                key={i}
                className="my-3 flex items-start gap-3 rounded-xl border-l-4 border-gold bg-gold/10 p-4 text-[14.5px] leading-relaxed text-text shadow-xs"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded bg-gold/20 text-gold">
                  <Sparkles className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean)}</div>
              </div>
            );
          }

          // 5. Quadro de Jurisprudência / Base Legal (> ⚖️ ou ⚖️)
          if (
            block.startsWith("> ⚖️") ||
            block.startsWith("⚖️") ||
            block.startsWith("> **Jurisprudência") ||
            block.startsWith("> **Base Legal")
          ) {
            const clean = block.replace(/^>\s*/, "").replace(/^⚖️\s*/, "");
            return (
              <div
                key={i}
                className="my-3 flex items-start gap-3 rounded-xl border-l-4 border-indigo-500 bg-indigo-500/10 p-4 text-[14.5px] leading-relaxed text-indigo-950 dark:text-indigo-100"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded bg-indigo-500/20 text-indigo-600 dark:text-indigo-400">
                  <Scale className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean)}</div>
              </div>
            );
          }

          // 6. Quadro de Exemplo Prático (> 💡 ou 💡)
          if (
            block.startsWith("> 💡") ||
            block.startsWith("💡") ||
            block.startsWith("> **Exemplo") ||
            block.startsWith("**Exemplo")
          ) {
            const clean = block.replace(/^>\s*/, "").replace(/^💡\s*/, "");
            return (
              <div
                key={i}
                className="my-3 flex items-start gap-3 rounded-xl border-l-4 border-sky-500 bg-sky-500/10 p-4 text-[14.5px] leading-relaxed text-sky-950 dark:text-sky-100"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded bg-sky-500/20 text-sky-600 dark:text-sky-400">
                  <Lightbulb className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean)}</div>
              </div>
            );
          }

          // 7. Lista não ordenada com múltiplos itens
          if (block.includes("\n") && block.split("\n").every((l) => l.trim().startsWith("- ") || l.trim().startsWith("• ") || l.trim().startsWith("* "))) {
            const items = block.split("\n").map((l) => l.trim().replace(/^[-•*]\s*/, ""));
            return (
              <ul key={i} className="my-2 space-y-1.5 pl-6 list-disc text-text/90">
                {items.map((it, itIdx) => (
                  <li key={itIdx} className="leading-relaxed">
                    {formatInline(it)}
                  </li>
                ))}
              </ul>
            );
          }

          // 8. Lista ordenada com múltiplos itens
          if (block.includes("\n") && block.split("\n").every((l) => /^\d+\.\s+/.test(l.trim()))) {
            const items = block.split("\n").map((l) => l.trim().replace(/^\d+\.\s*/, ""));
            return (
              <ol key={i} className="my-2 space-y-1.5 pl-6 list-decimal text-text/90">
                {items.map((it, itIdx) => (
                  <li key={itIdx} className="leading-relaxed">
                    {formatInline(it)}
                  </li>
                ))}
              </ol>
            );
          }

          // 9. Item único de lista
          if (block.startsWith("• ") || block.startsWith("- ") || block.startsWith("* ")) {
            const clean = block.replace(/^[-•*]\s*/, "");
            return (
              <div key={i} className="flex items-start gap-2.5 pl-2">
                <span className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-primary/70" />
                <p className="min-w-0 flex-1 leading-relaxed">{formatInline(clean)}</p>
              </div>
            );
          }

          // 10. Parágrafo analítico de texto corrido
          return (
            <p key={i} className="text-justify font-normal leading-relaxed">
              {formatInline(block)}
            </p>
          );
        })}
      </div>

      {/* Rodapé Editorial da Folha */}
      <div className="border-t border-dashed border-border/60 pt-4 flex flex-wrap items-center justify-between text-xs text-muted">
        <span>MentorIA · Preparação Individualizada para Concursos</span>
        <span className="font-mono font-semibold">Caderno Teórico de Alta Retenção</span>
      </div>
    </article>
  );
}
