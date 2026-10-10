"use client";

import {
  AlertTriangle,
  BookOpen,
  Check,
  Download,
  FileText,
  Lightbulb,
  PartyPopper,
  Printer,
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
  // Trata **negrito**, `código` e destaques
  const parts = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return parts.map((part, idx) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return (
        <strong key={idx} className="font-bold text-text">
          {part.slice(2, -2)}
        </strong>
      );
    }
    if (part.startsWith("`") && part.endsWith("`")) {
      return (
        <code key={idx} className="rounded bg-surface-3 px-1.5 py-0.5 font-mono text-xs font-semibold text-text">
          {part.slice(1, -1)}
        </code>
      );
    }
    return <span key={idx}>{part}</span>;
  });
}

export function BizuSummary({
  markdown,
  title,
}: {
  markdown: string;
  title?: string;
}) {
  const rawParagraphs = markdown
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
        {rawParagraphs.map((para, i) => {
          // 1. Cabeçalho / Título de Seção (###)
          if (para.startsWith("#")) {
            const titleText = para.replace(/^#+\s*/, "");
            return (
              <div key={i} className="pt-4 pb-1">
                <h3 className="flex items-center gap-2.5 font-display text-base font-bold uppercase tracking-wide text-text">
                  <span className="h-4 w-1.5 rounded-full bg-primary" />
                  {titleText}
                </h3>
              </div>
            );
          }

          // 2. Quadro de Atenção / Pegadinha da Banca (> ⚠️ ou ⚠️)
          if (
            para.startsWith("> ⚠️") ||
            para.includes("⚠️") ||
            para.startsWith("**Atenção") ||
            para.startsWith("**Cuidado")
          ) {
            const clean = para.replace(/^>\s*/, "").replace(/^⚠️\s*/, "");
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

          // 3. Quadro de Bizu Estratégico / Mnemônico (> 📌 ou 📌)
          if (
            para.startsWith("> 📌") ||
            para.includes("📌") ||
            para.startsWith("**Bizu") ||
            para.startsWith("**Mnemônico")
          ) {
            const clean = para.replace(/^>\s*/, "").replace(/^📌\s*/, "");
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

          // 4. Aplicação Prática / Exemplos (• **Aplicação:**)
          if (para.startsWith("•") || para.startsWith("-")) {
            const clean = para.replace(/^[-•*]\s*/, "");
            return (
              <div key={i} className="flex items-start gap-2.5 pl-2">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-primary/70" />
                <p className="min-w-0 flex-1">{formatInline(clean)}</p>
              </div>
            );
          }

          // 5. Parágrafo analítico de texto corrido
          return (
            <p key={i} className="text-justify font-normal">
              {formatInline(para)}
            </p>
          );
        })}
      </div>

      {/* Rodapé Editorial da Folha */}
      <div className="border-t border-dashed border-border/60 pt-4 flex flex-wrap items-center justify-between text-xs text-muted">
        <span>MentorIA · Preparação Individualizada</span>
        <span className="font-mono">Caderno Teórico de Alta Retenção</span>
      </div>
    </article>
  );
}
