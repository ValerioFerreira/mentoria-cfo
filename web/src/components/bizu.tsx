"use client";

import { AlertTriangle, BookOpen, Check, Lightbulb, PartyPopper, Sparkles, X } from "lucide-react";
import { useState, useTransition, type ReactNode } from "react";
import { Card, cx } from "@/components/ui";
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
    <div className="space-y-3">
      <div className="flex items-center justify-between gap-3">
        <p className="eyebrow">Certo ou Errado</p>
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

export function BizuSummary({ markdown }: { markdown: string }) {
  const rawLines = markdown.split("\n").map((l) => l.trim()).filter(Boolean);

  return (
    <Card className="relative overflow-hidden border border-border/80 bg-surface/90 p-5 shadow-card sm:p-6 space-y-4">
      {/* Barra superior de identificação no estilo apostila */}
      <div className="flex items-center justify-between border-b border-border/60 pb-3">
        <div className="flex items-center gap-2">
          <div className="flex h-6 w-6 items-center justify-center rounded-lg bg-gold/15 text-gold">
            <BookOpen className="h-3.5 w-3.5" aria-hidden />
          </div>
          <span className="font-display text-xs font-bold uppercase tracking-wider text-muted">
            Caderno Teórico · Bizu Direcionado
          </span>
        </div>
        <span className="rounded-full bg-gold/10 px-2.5 py-0.5 text-[11px] font-bold text-gold-text">
          Síntese Essencial
        </span>
      </div>

      {/* Conteúdo estruturado */}
      <div className="space-y-3.5 pt-1 text-[15px] leading-relaxed">
        {rawLines.map((raw, i) => {
          const clean = raw.replace(/^[-*]\s*/, "");

          // 1. Títulos / Cabeçalhos (ex: ### ou ##)
          if (clean.startsWith("#")) {
            const titleText = clean.replace(/^#+\s*/, "");
            return (
              <div key={i} className="flex items-center gap-2.5 pt-2 pb-1">
                <span className="h-4 w-1 rounded-full bg-gold" />
                <h3 className="font-display text-base font-bold uppercase tracking-wide text-text">
                  {titleText}
                </h3>
              </div>
            );
          }

          // 2. Pontos de Atenção / Pegadinhas / Cuidado
          if (
            clean.includes("⚠️") ||
            clean.startsWith("**Atenção") ||
            clean.startsWith("**Cuidado") ||
            clean.startsWith("**Pegadinha") ||
            clean.startsWith("**Importante")
          ) {
            return (
              <div
                key={i}
                className="my-2 flex items-start gap-3 rounded-2xl border border-amber-500/30 bg-amber-500/10 p-4 text-[14.5px] leading-relaxed text-amber-950 shadow-xs dark:text-amber-100"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md bg-amber-500/20 text-amber-600 dark:text-amber-400">
                  <AlertTriangle className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean.replace(/^⚠️\s*/, ""))}</div>
              </div>
            );
          }

          // 3. Exemplos Práticos / Aplicação
          if (
            clean.includes("💡") ||
            clean.startsWith("**Exemplo") ||
            clean.startsWith("**Aplicação")
          ) {
            return (
              <div
                key={i}
                className="my-2 flex items-start gap-3 rounded-2xl border border-sky-500/30 bg-sky-500/10 p-4 text-[14.5px] leading-relaxed text-sky-950 shadow-xs dark:text-sky-100"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md bg-sky-500/20 text-sky-600 dark:text-sky-400">
                  <Lightbulb className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean.replace(/^💡\s*/, ""))}</div>
              </div>
            );
          }

          // 4. Bizus de Prova / Mnemônicos / Memorize
          if (
            clean.includes("📌") ||
            clean.startsWith("**Bizu") ||
            clean.startsWith("**Mnemônico") ||
            clean.startsWith("**Memorize") ||
            clean.startsWith("**Dica")
          ) {
            return (
              <div
                key={i}
                className="my-2 flex items-start gap-3 rounded-2xl border border-gold/40 bg-gold/10 p-4 text-[14.5px] leading-relaxed text-text shadow-xs"
              >
                <div className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md bg-gold/20 text-gold">
                  <Sparkles className="h-3.5 w-3.5" aria-hidden />
                </div>
                <div className="min-w-0 flex-1">{formatInline(clean.replace(/^📌\s*/, ""))}</div>
              </div>
            );
          }

          // 5. Tópico normal (Apresentação elegante com indicador e destaque visual)
          return (
            <div
              key={i}
              className="flex items-start gap-3 rounded-xl border border-border/40 bg-surface-2/60 p-3.5 transition-colors hover:border-border-strong hover:bg-surface-2"
            >
              <span className="mt-1.5 h-2 w-2 shrink-0 rounded-full bg-gold shadow-xs" aria-hidden />
              <div className="min-w-0 flex-1 text-text/95">
                {formatInline(clean)}
              </div>
            </div>
          );
        })}
      </div>
    </Card>
  );
}

