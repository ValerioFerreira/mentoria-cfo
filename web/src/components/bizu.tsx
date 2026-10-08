"use client";

import { Check, PartyPopper, X } from "lucide-react";
import { useState, useTransition } from "react";
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

export function BizuSummary({ markdown }: { markdown: string }) {
  // Bizus são escritos em Markdown simples (listas com "- " e **negrito**); render mínimo e seguro.
  const lines = markdown.split("\n").filter((l) => l.trim());
  return (
    <Card tone="soft" className="relative overflow-hidden pl-7">
      <span className="absolute inset-y-0 left-0 w-1.5 bg-gold" aria-hidden />
      <ul className="space-y-2.5 text-[15px] leading-relaxed">
        {lines.map((l, i) => (
          <li key={i} className="flex gap-3">
            <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-gold" aria-hidden />
            <span>
              {l.replace(/^[-*]\s*/, "").split(/(\*\*[^*]+\*\*)/g).map((part, j) =>
                part.startsWith("**") && part.endsWith("**") ? <strong key={j}>{part.slice(2, -2)}</strong> : <span key={j}>{part}</span>,
              )}
            </span>
          </li>
        ))}
      </ul>
    </Card>
  );
}
