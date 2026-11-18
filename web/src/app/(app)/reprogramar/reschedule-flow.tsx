"use client";

import { ArrowRight, Check, Loader2 } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useMemo, useState, useTransition } from "react";
import { Alert, Badge, Button, Card, InfoTip, SectionTitle, TYPE_META, cx } from "@/components/ui";
import { applyReschedule, previewReschedule } from "@/lib/plan/reschedule-actions";
import { dayOfWeekIndex, shortDate, weekdayName } from "@/lib/plan-time";
import type {
  OverdueActivity, RescheduleExtraLoadPct, RescheduleInput, RescheduleOption, ReschedulePreview, RescheduleWindowDays,
} from "@/lib/planner/reschedule-types";

/** a prévia lista no máximo isto de início; o recálculo do plano inteiro move centenas de atividades */
const MOVES_SHOWN = 60;
const dayLabel = (iso: string) => `${weekdayName(dayOfWeekIndex(iso))}, ${shortDate(iso)}`;
const hm = (min: number) => (min >= 60 ? `${Math.floor(min / 60)} h${min % 60 ? ` ${min % 60} min` : ""}` : `${min} min`);

const OPTIONS: { id: RescheduleOption; title: string; short: string; info: string }[] = [
  {
    id: "SPREAD", title: "Espalhar pelos próximos dias", short: "Distribui conforme a folga de cada dia",
    info: "Cada atividade vai para o dia com mais folga dentro da janela escolhida, sem passar de 2 horas da mesma disciplina no dia. Você define até quanto cada dia pode passar da meta. O que não couber na janela é procurado nos dias seguintes, até dois dias antes da prova.",
  },
  {
    id: "FILL_GAPS", title: "Encaixar só nas folgas", short: "Nenhum dia passa da meta",
    info: "Usa só os dias (e domingos leves) que ainda têm espaço. Se faltar lugar, uma revisão geral de sobra pode ceder o dia para a atividade atrasada. Quando o plano está cheio, muita coisa não cabe: a prévia mostra o que ficaria de fora.",
  },
  {
    id: "RECALC_REST", title: "Recalcular o restante do plano", short: "Refaz a distribuição de hoje até a prova",
    info: "Distribui de novo todas as atividades que faltam, de hoje até dois dias antes da prova, mantendo o tempo de cada uma. Quase tudo muda de dia. O que não couber sai do plano, começando pelo conteúdo de menor importância para o concurso, e a lista aparece antes de você confirmar.",
  },
  {
    id: "MOVE_TO_DAY", title: "Levar para um dia", short: "Você escolhe o dia",
    info: "Todas as atividades escolhidas vão para o dia que você indicar (ou o mais cedo possível depois dele, já que a revisão não pode cair no mesmo dia da teoria). Se o dia ficar pesado demais, a prévia avisa.",
  },
  {
    id: "DISMISS", title: "Dispensar", short: "Tira do plano",
    info: "As atividades saem do plano e deixam de contar como atrasadas. Isso reduz a cobertura do edital, então use só para o que você realmente não vai estudar.",
  },
];

export function RescheduleFlow({ overdue, today, lastDate }: { overdue: OverdueActivity[]; today: string; lastDate: string }) {
  const router = useRouter();
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [selected, setSelected] = useState<Set<string>>(() => new Set(overdue.map((a) => a.id)));
  const [option, setOption] = useState<RescheduleOption>("SPREAD");
  const [windowDays, setWindowDays] = useState<RescheduleWindowDays>(7);
  const [extraLoadPct, setExtraLoadPct] = useState<RescheduleExtraLoadPct>(25);
  const [targetDate, setTargetDate] = useState(today);
  const [preview, setPreview] = useState<ReschedulePreview | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();

  const groups = useMemo(() => {
    const m = new Map<string, OverdueActivity[]>();
    for (const a of overdue) m.set(a.date, [...(m.get(a.date) ?? []), a]);
    return [...m];
  }, [overdue]);
  const chosen = overdue.filter((a) => selected.has(a.id));
  const chosenMin = chosen.reduce((n, a) => n + a.plannedMinutes, 0);

  const input = (opt: RescheduleOption = option): RescheduleInput => ({
    activityIds: chosen.map((a) => a.id),
    params: {
      option: opt,
      ...(opt === "SPREAD" ? { windowDays, extraLoadPct } : {}),
      ...(opt === "MOVE_TO_DAY" ? { targetDate } : {}),
    },
  });

  function toggle(id: string) {
    setSelected((s) => {
      const n = new Set(s);
      if (n.has(id)) n.delete(id);
      else n.add(id);
      return n;
    });
  }
  function toggleDay(items: OverdueActivity[]) {
    setSelected((s) => {
      const n = new Set(s);
      const all = items.every((a) => n.has(a.id));
      for (const a of items) {
        if (all) n.delete(a.id);
        else n.add(a.id);
      }
      return n;
    });
  }

  function runPreview(opt: RescheduleOption = option) {
    setError(null);
    start(async () => {
      const r = await previewReschedule(input(opt));
      if (!r.ok) {
        setError(r.error);
        return;
      }
      setOption(opt);
      setPreview(r);
      setStep(3);
    });
  }

  function confirm() {
    setError(null);
    start(async () => {
      const r = await applyReschedule(input(preview?.option ?? option));
      if (!r.ok) {
        setError(r.error);
        return;
      }
      router.push("/");
      router.refresh();
    });
  }

  return (
    <div className="space-y-6">
      <ol className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider" aria-label="Passos">
        {["Atividades", "Como encaixar", "Conferir"].map((label, i) => (
          <li key={label} className={cx("flex items-center gap-2", step === i + 1 ? "text-text" : "text-muted")}>
            <span className={cx("flex h-6 w-6 items-center justify-center rounded-full border text-[11px]", step === i + 1 ? "border-primary bg-primary text-on-primary" : step > i + 1 ? "border-ok bg-ok text-white" : "border-border")}>
              {step > i + 1 ? <Check className="h-3.5 w-3.5" aria-hidden /> : i + 1}
            </span>
            {label}
            {i < 2 && <span className="mx-1 h-px w-5 bg-border" aria-hidden />}
          </li>
        ))}
      </ol>

      {error && <Alert tone="danger">{error}</Alert>}

      {step === 1 && (
        <section aria-labelledby="s1" className="space-y-4">
          <SectionTitle
            id="s1"
            aside={`${chosen.length} de ${overdue.length} · ${hm(chosenMin)}`}
            info="Todas as atividades atrasadas começam marcadas. Desmarque as que você quer deixar como estão. Marque ou desmarque um dia inteiro pelo botão ao lado da data."
          >
            Quais atividades?
          </SectionTitle>
          {groups.map(([date, items]) => (
            <div key={date} className="space-y-2">
              <div className="flex items-center justify-between gap-2 px-1">
                <p className="text-[11px] font-semibold uppercase tracking-wider text-muted">{dayLabel(date)}</p>
                <button type="button" onClick={() => toggleDay(items)} className="cursor-pointer text-xs font-semibold text-primary hover:underline">
                  {items.every((a) => selected.has(a.id)) ? "Desmarcar o dia" : "Marcar o dia"}
                </button>
              </div>
              {items.map((a) => (
                <label key={a.id} className={cx("flex cursor-pointer items-center gap-3 rounded-xl border px-3.5 py-3 transition", selected.has(a.id) ? "border-primary/60 bg-primary-soft/40" : "border-border bg-surface hover:border-border-strong")}>
                  <input type="checkbox" className="h-4 w-4 shrink-0 accent-[var(--primary)]" checked={selected.has(a.id)} onChange={() => toggle(a.id)} />
                  <ActivityLine title={a.title} subject={a.subjectName} type={a.type} minutes={a.plannedMinutes} />
                </label>
              ))}
            </div>
          ))}
          <div className="flex justify-end gap-2 pt-2">
            <Button onClick={() => setStep(2)} disabled={chosen.length === 0}>
              Continuar <ArrowRight className="h-4 w-4" aria-hidden />
            </Button>
          </div>
        </section>
      )}

      {step === 2 && (
        <section aria-labelledby="s2" className="space-y-4">
          <SectionTitle id="s2" aside={`${chosen.length} ${chosen.length === 1 ? "atividade" : "atividades"} · ${hm(chosenMin)}`} info="Em todas as opções, as atividades seguintes que dependem das que você move (revisão, fixação, caderno de questões) são reorganizadas junto, para manter a ordem certa. Você confere tudo no próximo passo antes de confirmar.">
            Como encaixar?
          </SectionTitle>
          <div className="space-y-2.5" role="radiogroup" aria-label="Como encaixar as atividades">
            {OPTIONS.map((o) => (
              <div key={o.id} className={cx("rounded-xl border p-3.5 transition", option === o.id ? "border-primary bg-primary-soft/40 ring-2 ring-primary/30" : "border-border bg-surface hover:border-border-strong")}>
                <div className="flex items-start gap-3">
                  <button
                    type="button" role="radio" aria-checked={option === o.id} onClick={() => setOption(o.id)}
                    className="flex min-w-0 flex-1 cursor-pointer items-start gap-3 text-left"
                  >
                    <span className={cx("mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2", option === o.id ? "border-primary bg-primary text-on-primary" : "border-border-strong")}>
                      {option === o.id && <span className="h-1.5 w-1.5 rounded-full bg-current" />}
                    </span>
                    <span className="min-w-0">
                      <span className="block font-semibold">{o.title}</span>
                      <span className="block text-xs text-muted">{o.short}</span>
                    </span>
                  </button>
                  <InfoTip align="end" label={`Sobre: ${o.title}`}>{o.info}</InfoTip>
                </div>
                {option === o.id && o.id === "SPREAD" && (
                  <div className="mt-3 grid gap-3 pl-8 sm:grid-cols-2">
                    <Choice label="Janela" value={windowDays} onChange={setWindowDays} options={[[3, "3 dias"], [7, "7 dias"], [14, "14 dias"]]} info="Quantos dias, a partir de hoje (ou de amanhã, se hoje já está cheio), a distribuição usa antes de procurar vaga nos dias seguintes." />
                    <Choice label="Carga extra por dia" value={extraLoadPct} onChange={setExtraLoadPct} options={[[15, "15%"], [25, "25%"], [40, "40%"]]} info="Até quanto cada dia pode passar da meta de estudo. Quanto maior, mais rápido você recupera o atraso, e mais pesado fica cada dia." />
                  </div>
                )}
                {option === o.id && o.id === "MOVE_TO_DAY" && (
                  <div className="mt-3 pl-8">
                    <label className="block text-xs font-semibold text-muted" htmlFor="target-date">Dia de destino</label>
                    <input id="target-date" type="date" min={today} max={lastDate} value={targetDate} onChange={(e) => setTargetDate(e.target.value || today)} className="mt-1 rounded-xl border border-border bg-surface px-3 py-2 text-sm" />
                  </div>
                )}
              </div>
            ))}
          </div>
          <div className="flex justify-between gap-2 pt-2">
            <Button variant="ghost" onClick={() => setStep(1)}>Voltar</Button>
            <Button onClick={() => runPreview()} disabled={pending || (option === "MOVE_TO_DAY" && !targetDate)}>
              {pending ? <><Loader2 className="h-4 w-4 animate-spin" aria-hidden /> Calculando…</> : <>Ver como fica <ArrowRight className="h-4 w-4" aria-hidden /></>}
            </Button>
          </div>
        </section>
      )}

      {step === 3 && preview && (
        <PreviewStep
          preview={preview} pending={pending}
          onBack={() => setStep(2)} onConfirm={confirm}
          onSwitchToRecalc={() => runPreview("RECALC_REST")}
        />
      )}
    </div>
  );
}

function ActivityLine({ title, subject, type, minutes }: { title: string; subject: string; type: OverdueActivity["type"]; minutes: number }) {
  const m = TYPE_META[type];
  return (
    <span className="flex min-w-0 flex-1 items-center gap-3">
      <m.Icon className="h-4 w-4 shrink-0" style={{ color: m.color }} aria-hidden />
      <span className="min-w-0 flex-1">
        <span className="block truncate text-sm font-semibold">{title}</span>
        <span className="block truncate text-xs text-muted">{subject} · {m.label}</span>
      </span>
      <span className="shrink-0 text-xs font-semibold text-muted tabular">{hm(minutes)}</span>
    </span>
  );
}

function Choice<T extends number>({ label, value, onChange, options, info }: { label: string; value: T; onChange: (v: T) => void; options: [T, string][]; info: string }) {
  return (
    <div>
      <p className="mb-1 flex items-center gap-1.5 text-xs font-semibold text-muted">{label} <InfoTip align="start">{info}</InfoTip></p>
      <div className="inline-flex rounded-xl border border-border p-0.5" role="radiogroup" aria-label={label}>
        {options.map(([v, text]) => (
          <button key={v} type="button" role="radio" aria-checked={value === v} onClick={() => onChange(v)} className={cx("cursor-pointer rounded-lg px-3 py-1.5 text-sm font-semibold transition", value === v ? "bg-primary text-on-primary" : "text-muted hover:text-text")}>
            {text}
          </button>
        ))}
      </div>
    </div>
  );
}

function PreviewStep({ preview: p, pending, onBack, onConfirm, onSwitchToRecalc }: { preview: ReschedulePreview; pending: boolean; onBack: () => void; onConfirm: () => void; onSwitchToRecalc: () => void }) {
  const dependents = p.moves.filter((m) => m.reason === "DEPENDENT");
  const selectedMoves = p.moves.filter((m) => m.reason === "SELECTED");
  const [showAll, setShowAll] = useState(false);
  const shown = showAll ? p.moves : p.moves.slice(0, MOVES_SHOWN);
  const byDay = useMemo(() => {
    const m = new Map<string, typeof p.moves>();
    for (const x of shown) m.set(x.toDate, [...(m.get(x.toDate) ?? []), x]);
    return [...m].sort((a, b) => a[0].localeCompare(b[0]));
  }, [shown]);
  const maxLoad = Math.max(1, ...p.dayLoads.flatMap((d) => [d.before, d.after, d.target]));
  const nothing = p.moves.length === 0 && p.dismissed.length === 0 && p.yielded.length === 0 && p.doesNotFit.length === 0;

  return (
    <section aria-labelledby="s3" className="space-y-5">
      <SectionTitle id="s3" info="Nada foi gravado ainda. Esta é a prévia: confira os dias, as atividades que vão mudar de lugar (inclusive as seguintes, que andam junto para manter a ordem certa) e o que não coube.">
        Como fica
      </SectionTitle>

      <Card className="flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
        <span><strong className="font-display text-2xl tabular">{selectedMoves.length}</strong> <span className="text-muted">escolhidas</span></span>
        <span className="inline-flex items-center gap-1.5">
          <strong className="font-display text-2xl tabular">{dependents.length}</strong> <span className="text-muted">seguintes reorganizadas</span>
          <InfoTip align="start">Atividades que dependem das que você moveu (por exemplo, a revisão que só pode vir depois da teoria) e por isso também mudaram de dia.</InfoTip>
        </span>
        {p.dismissed.length > 0 && <span><strong className="font-display text-2xl tabular">{p.dismissed.length}</strong> <span className="text-muted">dispensadas</span></span>}
        {p.doesNotFit.length > 0 && <span><strong className="font-display text-2xl tabular text-warn">{p.doesNotFit.length}</strong> <span className="text-muted">{p.noFitLeavesPlan ? "sairão do plano" : "não couberam"}</span></span>}
      </Card>

      {p.warnings.length > 0 && (
        <div className="space-y-2">
          {p.warnings.filter((w) => w.code !== "RECURRENT_DELAY").map((w) => <Alert key={w.code} tone="warn">{w.message}</Alert>)}
        </div>
      )}
      {p.suggestRecalc && (
        <Card tone="soft" className="flex flex-wrap items-center justify-between gap-3">
          <p className="text-sm font-semibold">Quer ver o plano recalculado de hoje até a prova?</p>
          <div className="flex items-center gap-2">
            <InfoTip align="end">Com muita coisa deslocada, ou atividades que não couberam, costuma ser mais limpo refazer a distribuição inteira. Você vê a lista do que não cabe antes de confirmar.</InfoTip>
            <Button variant="secondary" size="sm" onClick={onSwitchToRecalc} disabled={pending}>Trocar por “Recalcular o restante”</Button>
          </div>
        </Card>
      )}
      {p.suggestRedoPlan && (
        <Card tone="soft" className="flex flex-wrap items-center justify-between gap-3">
          <div className="text-sm">
            <p className="font-semibold">O plano está pesado para o seu tempo?</p>
            <p className="text-muted">{p.warnings.find((w) => w.code === "RECURRENT_DELAY")?.message}</p>
          </div>
          <Link href="/onboarding" className="text-sm font-semibold text-primary hover:underline">Refazer o plano com menos horas</Link>
        </Card>
      )}

      {p.dayLoads.length > 0 && (
        <div className="space-y-2">
          <p className="flex items-center gap-1.5 text-[11px] font-semibold uppercase tracking-wider text-muted">
            Carga dos dias afetados
            <InfoTip align="start">A barra cinza é o que o dia tinha; a colorida é como fica. O traço marca a meta de estudo do dia. Dias que passam da meta ficam em destaque.</InfoTip>
          </p>
          <ul className="max-h-72 space-y-1.5 overflow-y-auto rounded-xl border border-border p-3">
            {p.dayLoads.map((d) => (
              <li key={d.date} className="grid grid-cols-[5.5rem_1fr_7.5rem] items-center gap-3 text-xs tabular">
                <span className="font-semibold">{dayLabel(d.date)}</span>
                <span className="relative block h-3 overflow-hidden rounded bg-surface-3" aria-hidden>
                  <span className="absolute inset-y-0 left-0 bg-border-strong/60" style={{ width: `${(d.before / maxLoad) * 100}%` }} />
                  <span className={cx("absolute inset-y-0 left-0 opacity-80", d.after > d.target ? "bg-warn" : "bg-primary")} style={{ width: `${(d.after / maxLoad) * 100}%`, height: "50%", top: "25%" }} />
                  <span className="absolute inset-y-0 w-0.5 bg-text" style={{ left: `${(d.target / maxLoad) * 100}%` }} />
                </span>
                <span className={cx("text-right", d.after > d.target && "font-bold text-warn")}>{hm(d.before)} → {hm(d.after)}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {byDay.length > 0 && (
        <div className="space-y-3">
          <p className="text-[11px] font-semibold uppercase tracking-wider text-muted">Para onde vai cada atividade</p>
          {byDay.map(([date, items]) => (
            <div key={date} className="space-y-1.5">
              <p className="px-1 text-xs font-semibold">{dayLabel(date)}</p>
              {items.map((m) => (
                <div key={m.id} className="rounded-xl border border-border bg-surface px-3.5 py-2.5">
                  <div className="flex items-center gap-3">
                    <ActivityLine title={m.title} subject={m.subjectName} type={m.type} minutes={m.plannedMinutes} />
                  </div>
                  <p className="mt-1 flex flex-wrap items-center gap-x-2 text-[11px] text-muted">
                    <span>de {dayLabel(m.fromDate)}</span>
                    {m.reason === "DEPENDENT" && (
                      <Badge tone="gold">{m.dependsOnTitle ? `reorganizada por depender de “${m.dependsOnTitle}”` : "reorganizada no recálculo do plano"}</Badge>
                    )}
                  </p>
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {p.moves.length > shown.length && (
        <Button variant="secondary" size="sm" onClick={() => setShowAll(true)}>Ver as outras {p.moves.length - shown.length} atividades</Button>
      )}

      {p.dismissed.length > 0 && <p className="text-sm text-muted">{p.dismissed.length} {p.dismissed.length === 1 ? "atividade será dispensada" : "atividades serão dispensadas"}.</p>}
      {p.yielded.length > 0 && (
        <List title="Revisões gerais de sobra que cedem o lugar" rows={p.yielded.map((y) => ({ id: y.id, title: y.title, sub: `${y.subjectName} · ${hm(y.plannedMinutes)}` }))} />
      )}
      {p.doesNotFit.length > 0 && (
        <List
          title={p.noFitLeavesPlan ? "Não cabem até a prova e sairão do plano" : "Não couberam e continuam onde estavam"}
          rows={p.doesNotFit.map((y) => ({ id: y.id, title: y.title, sub: `${y.subjectName} · ${hm(y.plannedMinutes)}${y.importance != null ? ` · importância ${Math.round(y.importance)}` : ""}` }))}
        />
      )}
      {nothing && <Alert tone="info">Nada muda com esta escolha. Volte e tente outra opção.</Alert>}

      <div className="flex flex-wrap justify-between gap-2 border-t border-border pt-4">
        <Button variant="ghost" onClick={onBack} disabled={pending}>Voltar</Button>
        <Button onClick={onConfirm} disabled={pending || nothing}>
          {pending ? <><Loader2 className="h-4 w-4 animate-spin" aria-hidden /> Gravando…</> : "Confirmar reprogramação"}
        </Button>
      </div>
    </section>
  );
}

function List({ title, rows }: { title: string; rows: { id: string; title: string; sub: string }[] }) {
  return (
    <div className="space-y-1.5">
      <p className="text-[11px] font-semibold uppercase tracking-wider text-muted">{title}</p>
      <ul className="divide-y divide-border rounded-xl border border-border">
        {rows.map((r) => (
          <li key={r.id} className="px-3.5 py-2">
            <p className="truncate text-sm font-semibold">{r.title}</p>
            <p className="text-xs text-muted">{r.sub}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
