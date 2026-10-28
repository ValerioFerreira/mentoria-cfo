"use client";

import { ArrowRight, BadgeCheck, Loader2, Ticket } from "lucide-react";
import { useRouter } from "next/navigation";
import { useEffect, useState, useTransition } from "react";
import { Alert, Button, inputCls } from "@/components/ui";
import { formatBRL } from "@/lib/commerce/money";
import { CONTESTS, CONTEST_SUBTITLES } from "@/lib/contests";
import { finishContestUpgrade, previewContestSwitch, startContestUpgrade, updateUserContest, type ContestSwitchView } from "@/lib/profile/actions";

const GROUPS = ["CBMPE", "PMPE", "PCPE"] as const;

type Pay = Extract<ContestSwitchView, { ok: true }>;

export function ContestSwitcher({ current, prices, resumePaid }: { current: string; prices: Record<string, number | null>; resumePaid: boolean }) {
  const router = useRouter();
  const [selected, setSelected] = useState(current);
  const [target, setTarget] = useState<string | null>(null);
  const [offer, setOffer] = useState<Pay | null>(null);
  const [coupons, setCoupons] = useState("");
  const [msg, setMsg] = useState<{ ok: boolean; text: string } | null>(null);
  const [pending, start] = useTransition();

  // pagamento da diferença confirmado em outra tela: conclui a troca uma única vez
  useEffect(() => {
    if (!resumePaid) return;
    let alive = true;
    finishContestUpgrade().then((r) => {
      if (!alive || !r) return;
      setMsg({ ok: r.success, text: r.message });
      router.refresh();
    });
    return () => {
      alive = false;
    };
  }, [resumePaid, router]);

  const currentPrice = prices[current] ?? null;

  function pick(key: string) {
    if (key === selected || pending) return;
    setMsg(null);
    setOffer(null);
    setTarget(null);
    start(async () => {
      const view = await previewContestSwitch(key);
      if (!view.ok) return setMsg({ ok: false, text: view.message });
      if (view.mode === "PAY") {
        setTarget(key);
        setCoupons("");
        return setOffer(view);
      }
      const res = await updateUserContest(key);
      setMsg({ ok: res.success, text: res.message });
      if (res.success) {
        setSelected(key);
        router.refresh();
      }
    });
  }

  function applyCoupons() {
    if (!target) return;
    start(async () => {
      const view = await previewContestSwitch(target, coupons);
      if (!view.ok) return setMsg({ ok: false, text: view.message });
      setMsg(null);
      setOffer(view);
    });
  }

  function pay() {
    if (!target) return;
    start(async () => {
      const res = await startContestUpgrade(target, coupons);
      if (!res.success) return setMsg({ ok: false, text: res.message });
      if (res.payUrl) return router.push(res.payUrl);
      setMsg({ ok: true, text: res.message });
      setSelected(target);
      setTarget(null);
      setOffer(null);
      router.refresh();
    });
  }

  return (
    <div className="space-y-4">
      <div className="space-y-5">
        {GROUPS.map((org) => {
          const items = CONTESTS.filter((c) => c.org === org && c.available);
          if (!items.length) return null;
          return (
            <div key={org}>
              <p className="mb-2 text-[11px] font-bold uppercase tracking-[0.14em] text-muted">{org}</p>
              <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                {items.map((c) => {
                  const active = selected === c.key;
                  const price = prices[c.key];
                  const dearer = !active && price != null && currentPrice != null && price > currentPrice;
                  return (
                    <button
                      key={c.key}
                      type="button"
                      disabled={pending}
                      aria-pressed={active}
                      onClick={() => pick(c.key)}
                      className={`group flex cursor-pointer items-center justify-between gap-3 rounded-xl border px-3.5 py-3 text-left transition disabled:cursor-wait ${
                        active ? "border-primary bg-primary/10 shadow-sm" : target === c.key ? "border-gold bg-surface-1" : "border-border bg-surface-1 hover:border-border-strong hover:bg-surface-3/60"
                      }`}
                    >
                      <span className="min-w-0">
                        <span className="block truncate text-sm font-bold text-text">{c.role}</span>
                        <span className="block truncate text-xs text-muted">
                          {c.category || "Carreira policial"}
                          {price != null ? ` · ${formatBRL(price)}` : ""}
                        </span>
                      </span>
                      {active ? (
                        <BadgeCheck className="h-5 w-5 shrink-0 text-primary" aria-label="Concurso atual" />
                      ) : dearer ? (
                        <span className="shrink-0 rounded-full bg-gold/15 px-2 py-0.5 text-[10px] font-bold uppercase text-gold">Pagar diferença</span>
                      ) : (
                        <ArrowRight className="h-4 w-4 shrink-0 text-muted opacity-0 transition group-hover:opacity-100" />
                      )}
                    </button>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>

      {pending && !offer && (
        <p className="flex items-center gap-2 text-xs text-muted">
          <Loader2 className="h-3.5 w-3.5 animate-spin" /> Verificando…
        </p>
      )}

      {offer && target && (
        <div className="space-y-3 rounded-xl border border-gold/40 bg-surface-1 p-4">
          <p className="text-sm font-bold text-text">Trocar para {CONTEST_SUBTITLES[target as keyof typeof CONTEST_SUBTITLES]}</p>
          <dl className="space-y-1 text-sm">
            <Line label="Preço do concurso no site" value={formatBRL(offer.targetSiteCents)} />
            <Line label="Você já pagou" value={`− ${formatBRL(offer.creditCents)}`} />
            <Line label="Diferença" value={formatBRL(offer.residualCents)} />
            {offer.couponPoints > 0 && <Line label={`Cupons (${offer.couponPoints}% sobre a diferença)`} value={`− ${formatBRL(offer.residualCents - offer.finalCents)}`} tone="ok" />}
            <div className="flex items-baseline justify-between border-t border-dashed border-border-strong pt-2">
              <dt className="font-bold text-text">A pagar</dt>
              <dd className="font-display text-2xl font-bold text-primary">{formatBRL(offer.finalCents)}</dd>
            </div>
          </dl>

          <div>
            <label htmlFor="switch-coupons" className="mb-1 flex items-center gap-1.5 text-xs font-semibold text-muted">
              <Ticket className="h-3.5 w-3.5" /> Cupom de desconto
            </label>
            <div className="flex gap-2">
              <input id="switch-coupons" value={coupons} onChange={(e) => setCoupons(e.target.value.toUpperCase())} placeholder="Código do cupom" maxLength={150} className={inputCls} />
              <Button type="button" variant="secondary" size="md" disabled={pending || !coupons.trim()} onClick={applyCoupons}>
                Aplicar
              </Button>
            </div>
            {offer.coupons.length > 0 && (
              <p className="mt-1 text-xs text-ok">
                {offer.coupons.map((c) => `${c.code} (${c.discountPoints}%)`).join(" · ")}
                {offer.capped ? " — desconto limitado a 100%." : ""}
              </p>
            )}
          </div>

          <div className="flex flex-wrap gap-2">
            <Button type="button" size="md" disabled={pending} onClick={pay}>
              {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : null}
              {offer.finalCents > 0 ? `Pagar ${formatBRL(offer.finalCents)} e trocar` : "Trocar de concurso"}
            </Button>
            <Button
              type="button"
              variant="secondary"
              size="md"
              disabled={pending}
              onClick={() => {
                setOffer(null);
                setTarget(null);
              }}
            >
              Cancelar
            </Button>
          </div>
        </div>
      )}

      {msg && <Alert tone={msg.ok ? "info" : "danger"}>{msg.text}</Alert>}
    </div>
  );
}

function Line({ label, value, tone }: { label: string; value: string; tone?: "ok" }) {
  return (
    <div className="flex items-baseline justify-between gap-3">
      <dt className="text-muted">{label}</dt>
      <dd className={`font-semibold ${tone === "ok" ? "text-ok" : "text-text"}`}>{value}</dd>
    </div>
  );
}
