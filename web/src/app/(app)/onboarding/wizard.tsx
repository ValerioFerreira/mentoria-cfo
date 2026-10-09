"use client";

import { ArrowLeft, ArrowRight, CalendarDays, Check, ChevronDown, Flame, Gauge, Loader2, Rocket, Sparkles, Zap } from "lucide-react";
import { useEffect, useMemo, useRef, useState, useTransition } from "react";
import { Alert, BLOCK_COLOR, Badge, Button, Card, Count, InfoTip, Progress, Ring, cx } from "@/components/ui";
import { knownFromMarks, type Mark } from "@/lib/anamnesis";
import {
  DEFAULT_ANSWER, EXPERIENCE_OPTIONS, HIT_OPTIONS, LEVEL_LABEL, SELF_OPTIONS, levelFromAnswer,
  type DiagnosticAnswer,
} from "@/lib/diagnostic";
import { longDate } from "@/lib/plan-time";
import { createPlanAction, previewPlan } from "./actions";

export interface WizardItem {
  id: string;
  title: string;
  /** aulas da disciplina que tratam do assunto (o planejador trabalha por aula) */
  aulaIds: string[];
}

export interface WizardSubject {
  id: string;
  name: string;
  block: "I" | "II" | "III";
  examQuestions: number;
  languageGroup: string | null;
  /** assuntos do edital, na ordem do edital */
  items: WizardItem[];
  aulaIds: string[];
  /** a disciplina inclui conteúdo exclusivo do MentorIA sobre pontos do edital */
  hasComplement: boolean;
}

const BANDS = [
  { id: "LEVE", label: "Leve", range: "14 a 21 h por semana", perDay: "≈ 2 a 3 h por dia", min: 14, max: 21, start: 18, Icon: Gauge },
  { id: "MODERADO", label: "Moderado", range: "22 a 28 h por semana", perDay: "≈ 3 a 4 h por dia", min: 22, max: 28, start: 25, Icon: Zap },
  { id: "AVANCADO", label: "Avançado", range: "29 a 50 h por semana", perDay: "≈ 4 a 7 h por dia", min: 29, max: 50, start: 38, Icon: Flame },
] as const;

const BLOCK_NAME = { I: "Bloco I", II: "Bloco II", III: "Bloco III" } as const;
const STEPS = ["Disciplinas", "Anamnese", "Tempo", "Revisão"] as const;
const EXAM_DEFAULT = "2027-02-28";
const KNOWN_OPTIONS = [
  { value: 0, label: "Nunca vi" },
  { value: 1, label: "Já estudei" },
  { value: 2, label: "Domino" },
] as const;

function perDay(h: number) {
  const v = h / 7;
  const hh = Math.floor(v);
  const mm = Math.round((v - hh) * 60);
  return mm === 0 ? `${hh}h` : `${hh}h${String(mm).padStart(2, "0")}`;
}

type Preview = Awaited<ReturnType<typeof previewPlan>>;
type Marks = Record<string, 1 | 2>;

export function Wizard({ subjects, todayIso }: { subjects: WizardSubject[]; todayIso: string }) {
  const [step, setStep] = useState(0);
  const [selected, setSelected] = useState<Set<string>>(() => new Set(subjects.filter((s) => s.id !== "lingua-inglesa").map((s) => s.id)));
  const [hours, setHours] = useState(38);
  const [examDate, setExamDate] = useState(EXAM_DEFAULT);
  // início dos estudos: "now" = hoje (calculado no servidor, fuso de Recife) ou uma data da agenda
  const [startMode, setStartMode] = useState<"now" | "date">("now");
  const [startPick, setStartPick] = useState(todayIso);
  const start = startMode === "now" ? "now" : startPick;
  const startValid = startMode === "now" || (startPick >= todayIso && startPick < examDate);
  const [answers, setAnswers] = useState<Record<string, DiagnosticAnswer>>({});
  const [marks, setMarks] = useState<Marks>({});
  const [preview, setPreview] = useState<Preview | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [pending, startTransition] = useTransition();
  const seq = useRef(0);

  const chosen = useMemo(() => subjects.filter((s) => selected.has(s.id)), [subjects, selected]);
  const band = BANDS.find((b) => hours >= b.min && hours <= b.max) ?? BANDS[0];
  const levels = useMemo(
    () => chosen.map((s) => ({ id: s.id, level: levelFromAnswer(answers[s.id] ?? DEFAULT_ANSWER) })),
    [chosen, answers],
  );
  // marcas por assunto viram marcas por aula (o que o planejador entende); só as disciplinas escolhidas entram no cálculo
  const knownChosen = useMemo(() => Object.assign({}, ...chosen.map((s) => knownFromMarks(s, marks))) as Record<string, 1 | 2>, [chosen, marks]);
  const points = chosen.reduce((n, s) => n + s.examQuestions, 0);

  // prévia de cobertura (debounce) sempre que a seleção, as horas, a data, os níveis ou a anamnese mudam
  useEffect(() => {
    if (chosen.length === 0 || step < 2) return;
    const id = ++seq.current;
    const t = setTimeout(async () => {
      const r = await previewPlan({ subjects: levels, hoursPerWeek: hours, examDate, start, known: knownChosen });
      if (id === seq.current) setPreview(r);
    }, 350);
    return () => clearTimeout(t);
  }, [chosen.length, levels, hours, examDate, start, knownChosen, step]);

  function toggle(s: WizardSubject) {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(s.id)) next.delete(s.id);
      else {
        next.add(s.id);
        if (s.languageGroup) for (const o of subjects) if (o.languageGroup === s.languageGroup && o.id !== s.id) next.delete(o.id);
      }
      return next;
    });
  }
  const setAnswer = (id: string, patch: Partial<DiagnosticAnswer>) =>
    setAnswers((a) => ({ ...a, [id]: { ...(a[id] ?? DEFAULT_ANSWER), ...patch } }));
  const setMark = (itemId: string, v: Mark) =>
    setMarks((m) => {
      const next = { ...m };
      if (v === 0) delete next[itemId];
      else next[itemId] = v;
      return next;
    });
  const setMarkAll = (s: WizardSubject, v: Mark) =>
    setMarks((m) => {
      const next = { ...m };
      for (const i of s.items) {
        if (v === 0) delete next[i.id];
        else next[i.id] = v;
      }
      return next;
    });

  function submit() {
    setError(null);
    startTransition(async () => {
      const res = await createPlanAction({ subjects: levels, hoursPerWeek: hours, examDate, start, known: knownChosen, diagnostics: answers });
      if (res?.error) setError(res.error);
    });
  }

  const goStep = (n: number) => {
    setStep(Math.max(0, Math.min(STEPS.length - 1, n)));
    window.scrollTo({ top: 0 });
  };
  const canNext = step === 0 ? chosen.length > 0 : true;
  const langs = subjects.filter((s) => s.languageGroup);
  const others = subjects.filter((s) => !s.languageGroup);

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* etapas */}
      <div>
        <ol className="flex items-center" aria-label="Etapas">
          {STEPS.map((label, i) => {
            const past = i < step;
            const on = i === step;
            return (
              <li key={label} className={cx("flex items-center", i < STEPS.length - 1 && "flex-1")} aria-current={on ? "step" : undefined}>
                <span className="flex items-center gap-2.5">
                  <span
                    className={cx(
                      "flex h-9 w-9 items-center justify-center rounded-full border-2 font-display text-lg font-bold transition-all duration-300",
                      past && "border-ok bg-ok text-white",
                      on && "border-primary bg-primary text-on-primary shadow-[0_8px_18px_-8px_var(--primary)]",
                      !past && !on && "border-border-strong bg-surface text-muted",
                    )}
                  >
                    {past ? <Check className="pop h-4 w-4" strokeWidth={3} aria-hidden /> : i + 1}
                  </span>
                  <span className={cx("hidden text-sm font-semibold sm:inline", on ? "text-text" : "text-muted")}>{label}</span>
                </span>
                {i < STEPS.length - 1 && (
                  <span className="mx-3 h-0.5 flex-1 overflow-hidden rounded-full bg-surface-3">
                    <span className="block h-full bg-ok transition-[width] duration-500" style={{ width: past ? "100%" : "0%" }} />
                  </span>
                )}
              </li>
            );
          })}
        </ol>
      </div>

      <div key={step} className="page-in">
        {step === 0 && (
          <section className="space-y-6" aria-labelledby="t0">
            <div>
              <h1 id="t0" className="flex items-center gap-3 font-display text-4xl font-bold uppercase leading-none sm:text-5xl">
                Quais disciplinas entram na missão?
                <InfoTip align="start">A prova tem 70 questões. Em Língua Estrangeira você faz Inglês ou Espanhol.</InfoTip>
              </h1>
            </div>
            <div className="flex flex-wrap items-center gap-2 text-sm">
              <Button variant="secondary" size="sm" onClick={() => setSelected(new Set(subjects.filter((s) => s.id !== "lingua-inglesa").map((s) => s.id)))}>Selecionar todas</Button>
              <Button variant="ghost" size="sm" onClick={() => setSelected(new Set())}>Limpar</Button>
              <span className="ml-auto font-semibold text-muted tabular"><strong className="font-display text-xl text-text">{chosen.length}</strong> escolhidas · <strong className="font-display text-xl text-text">{points}</strong> questões da prova</span>
            </div>
            {(["I", "II", "III"] as const).map((b) => (
              <fieldset key={b} className="space-y-2.5">
                <legend className="mb-1 flex items-center gap-2 font-display text-xl font-bold uppercase tracking-wide">
                  <span className="h-3 w-3 rounded-[4px]" style={{ background: BLOCK_COLOR[b] }} aria-hidden />
                  {BLOCK_NAME[b]}
                </legend>
                <div className="grid gap-2.5 sm:grid-cols-2">
                  {others.filter((s) => s.block === b).map((s) => (
                    <SubjectCard key={s.id} s={s} on={selected.has(s.id)} onToggle={() => toggle(s)} />
                  ))}
                  {b === "I" && (
                    <Card className={cx("p-4 transition sm:col-span-2", langs.some((l) => selected.has(l.id)) && "border-primary")}>
                      <div className="flex flex-wrap items-center justify-between gap-3">
                        <div>
                          <p className="font-semibold">Língua Estrangeira</p>
                          <p className="text-xs text-muted">5 questões · escolha uma</p>
                        </div>
                        <div className="flex gap-1 rounded-xl bg-surface-3 p-1" role="group" aria-label="Língua estrangeira">
                          {langs.map((l) => (
                            <button
                              key={l.id}
                              type="button"
                              aria-pressed={selected.has(l.id)}
                              onClick={() => toggle(l)}
                              className={cx("cursor-pointer rounded-lg px-4 py-2 text-sm font-semibold transition", selected.has(l.id) ? "bg-surface text-primary shadow-card" : "text-muted hover:text-text")}
                            >
                              {l.id === "lingua-inglesa" ? "Inglês" : "Espanhol"}
                              <span className="ml-2 text-xs font-normal text-muted">{l.items.length} assuntos</span>
                            </button>
                          ))}
                        </div>
                      </div>
                    </Card>
                  )}
                </div>
              </fieldset>
            ))}
          </section>
        )}

        {step === 1 && (
          <section className="space-y-6" aria-labelledby="t1">
            <h1 id="t1" className="flex items-center gap-3 font-display text-4xl font-bold uppercase leading-none sm:text-5xl">
              O que você já estudou?
              <InfoTip align="start">
                A anamnese vem antes do tempo porque define quanto do edital já está encaminhado. Quem estuda uma disciplina com mais bagagem lê e revisa mais rápido, e assuntos marcados como dominados saem do plano (voltam só nas revisões finais). Se preferir, pule: assumimos que tudo é novo.
              </InfoTip>
            </h1>
            <div className="space-y-3">
              {chosen.map((s) => {
                const a = answers[s.id] ?? DEFAULT_ANSWER;
                const lvl = levelFromAnswer(a);
                const studied = s.items.filter((x) => marks[x.id] === 1).length;
                const mastered = s.items.filter((x) => marks[x.id] === 2).length;
                return (
                  <Card key={s.id} className="relative space-y-3.5 overflow-hidden p-4 pl-6">
                    <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: BLOCK_COLOR[s.block] }} aria-hidden />
                    <div className="flex items-center justify-between gap-2">
                      <h2 className="font-display text-2xl font-bold uppercase tracking-wide">{s.name}</h2>
                      <Badge tone={lvl >= 2 ? "ok" : "neutral"}>{LEVEL_LABEL[lvl]}</Badge>
                    </div>
                    <ChipRow label="Experiência" value={a.experience} options={EXPERIENCE_OPTIONS.map((o) => ({ value: o.value, label: o.label }))} onChange={(v) => setAnswer(s.id, { experience: v })} />
                    <ChipRow label="Como você se avalia?" value={a.self} options={SELF_OPTIONS} onChange={(v) => setAnswer(s.id, { self: v })} />
                    <ChipRow label="Acerto recente em questões" value={a.hitRate} options={HIT_OPTIONS} onChange={(v) => setAnswer(s.id, { hitRate: v })} />
                    <AssuntoChecklist s={s} marks={marks} onSet={setMark} onAll={(v) => setMarkAll(s, v)} summary={studied + mastered > 0 ? `${studied} já estudei · ${mastered} domino` : `${s.items.length} assuntos`} />
                  </Card>
                );
              })}
            </div>
          </section>
        )}

        {step === 2 && (
          <section className="space-y-6" aria-labelledby="t2">
            <h1 id="t2" className="flex items-center gap-3 font-display text-4xl font-bold uppercase leading-none sm:text-5xl">
              Quanto tempo por semana?
              <InfoTip align="start">Média semanal considerando os 7 dias. Reservamos 10% de folga para imprevistos e o domingo fica mais leve.</InfoTip>
            </h1>
            <div className="grid gap-3 sm:grid-cols-3">
              {BANDS.map((b) => {
                const on = band.id === b.id;
                return (
                  <button
                    key={b.id}
                    type="button"
                    aria-pressed={on}
                    onClick={() => setHours(b.start)}
                    className={cx("cursor-pointer rounded-2xl border-2 p-4 text-left transition duration-200 hover:-translate-y-0.5", on ? "border-primary bg-primary-soft shadow-lift" : "border-border bg-surface shadow-card hover:border-border-strong")}
                  >
                    <b.Icon className={cx("h-6 w-6", on ? "text-primary" : "text-muted")} aria-hidden />
                    <p className="mt-2 font-display text-3xl font-bold uppercase leading-none">{b.label}</p>
                    <p className="mt-1 text-sm">{b.range}</p>
                    <p className="text-xs text-muted">{b.perDay}</p>
                  </button>
                );
              })}
            </div>
            <Card className="space-y-4">
              <div className="flex items-end justify-between">
                <label htmlFor="hours" className="text-sm font-semibold">Horas por semana</label>
                <span className="text-right"><span className="font-display text-6xl font-bold leading-none tabular">{hours}</span><span className="font-display text-2xl font-bold text-muted"> h</span><br /><span className="text-xs text-muted">≈ {perDay(hours)} por dia</span></span>
              </div>
              <input id="hours" type="range" min={band.min} max={band.max} value={hours} onChange={(e) => setHours(Number(e.target.value))} className="h-2 w-full cursor-pointer accent-[var(--primary)]" />
              <div className="flex justify-between text-xs font-semibold text-muted tabular"><span>{band.min} h</span><span>{band.max} h</span></div>
            </Card>
            <PreviewBox preview={preview} subjects={chosen} hours={hours} onUseHours={setHours} />
          </section>
        )}

        {step === 3 && (
          <section className="space-y-6" aria-labelledby="t3">
            <h1 id="t3" className="flex items-center gap-3 font-display text-4xl font-bold uppercase leading-none sm:text-5xl">
              Confira e gere o plano
              <InfoTip align="start">Escolha quando começar: o plano conta o primeiro dia como o dia de início e distribui as horas só pelos dias que restam na primeira semana. Você pode refazê-lo quando quiser.</InfoTip>
            </h1>
            <Card className="space-y-4">
              <div className="flex flex-wrap items-center gap-x-8 gap-y-3 text-sm">
                <span><strong className="font-display text-3xl tabular">{hours} h</strong> <span className="text-muted">por semana ({band.label})</span></span>
                <label className="flex items-center gap-2 font-semibold">
                  Data da prova
                  <input type="date" value={examDate} onChange={(e) => setExamDate(e.target.value)} className="rounded-lg border border-border bg-surface px-2.5 py-1.5 text-sm font-normal" />
                </label>
              </div>
              <ul className="flex flex-wrap gap-2">
                {chosen.map((s) => (
                  <li key={s.id}><Badge className="!py-1">{s.name} · {LEVEL_LABEL[levels.find((l) => l.id === s.id)!.level]}</Badge></li>
                ))}
              </ul>
            </Card>
            <Card className="space-y-3">
              <div className="flex items-center gap-2 text-sm font-semibold">
                <CalendarDays className="h-4 w-4 text-primary" aria-hidden />
                Início dos estudos
                <InfoTip align="start">&quot;Imediatamente&quot; usa a data de hoje no horário de Recife e conta hoje como o primeiro dia. Se escolher uma data, a primeira semana terá só os dias a partir dela.</InfoTip>
              </div>
              <div role="radiogroup" aria-label="Início dos estudos" className="grid gap-2 sm:grid-cols-2">
                {([["now", "Começar imediatamente", longDate(todayIso)], ["date", "Escolher uma data", "Abra a agenda e selecione o dia"]] as const).map(([id, title, sub]) => {
                  const on = startMode === id;
                  return (
                    <button key={id} type="button" role="radio" aria-checked={on} onClick={() => setStartMode(id)}
                      className={cx("cursor-pointer rounded-xl border-2 p-3 text-left transition duration-200", on ? "border-primary bg-primary-soft" : "border-border bg-surface hover:border-border-strong")}>
                      <span className="block text-sm font-semibold">{title}</span>
                      <span className="block text-xs text-muted">{sub}</span>
                    </button>
                  );
                })}
              </div>
              {startMode === "date" && (
                <label className="flex flex-wrap items-center gap-2 text-sm font-semibold">
                  Data de início
                  <input type="date" value={startPick} min={todayIso} max={examDate} onChange={(e) => setStartPick(e.target.value)} className="rounded-lg border border-border bg-surface px-2.5 py-1.5 text-sm font-normal" />
                  {!startValid && <span className="text-xs font-normal text-danger">Escolha uma data entre hoje e a prova.</span>}
                </label>
              )}
            </Card>
            <PreviewBox preview={preview} subjects={chosen} hours={hours} detailed />
            {error && <Alert tone="danger">{error}</Alert>}
          </section>
        )}
      </div>

      <div className="flex items-center justify-between border-t border-border pt-5">
        <Button variant="ghost" onClick={() => goStep(step - 1)} disabled={step === 0 || pending}>
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Voltar
        </Button>
        {step < STEPS.length - 1 ? (
          <Button size="lg" onClick={() => goStep(step + 1)} disabled={!canNext}>
            Continuar
            <ArrowRight className="h-5 w-5" aria-hidden />
          </Button>
        ) : (
          <Button size="lg" onClick={submit} disabled={pending || chosen.length === 0 || !startValid}>
            {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <Rocket className="h-5 w-5" aria-hidden />}
            {pending ? "Gerando plano…" : "Gerar meu plano"}
          </Button>
        )}
      </div>
    </div>
  );
}

function SubjectCard({ s, on, onToggle }: { s: WizardSubject; on: boolean; onToggle: () => void }) {
  return (
    <button
      type="button"
      role="checkbox"
      aria-checked={on}
      onClick={onToggle}
      className={cx(
        "relative cursor-pointer overflow-hidden rounded-2xl border-2 p-4 pl-5 text-left transition duration-200 hover:-translate-y-0.5",
        on ? "border-primary bg-primary-soft shadow-lift" : "border-border bg-surface shadow-card hover:border-border-strong",
      )}
    >
      <span className="absolute inset-y-0 left-0 w-1.5" style={{ background: BLOCK_COLOR[s.block] }} aria-hidden />
      <div className="flex items-start justify-between gap-2">
        <p className="font-semibold leading-snug">{s.name}</p>
        <span className={cx("mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md border-2 transition", on ? "border-primary bg-primary text-on-primary" : "border-border-strong")}>
          {on && <Check className="pop h-3 w-3" strokeWidth={4} aria-hidden />}
        </span>
      </div>
      <p className="mt-1 text-xs text-muted tabular">{s.examQuestions} {s.examQuestions === 1 ? "questão" : "questões"} na prova · {s.items.length} assuntos</p>
      {s.hasComplement && (
        <p className="mt-1 flex items-center gap-1 text-xs font-medium text-gold-text">
          <Sparkles className="h-3 w-3" aria-hidden />
          Inclui conteúdo exclusivo do MentorIA
        </p>
      )}
    </button>
  );
}

function ChipRow<T extends string | number>({ label, value, options, onChange }: { label: string; value: T; options: { value: T; label: string }[]; onChange: (v: T) => void }) {
  return (
    <div>
      <p className="mb-1.5 text-xs font-semibold text-muted">{label}</p>
      <div className="flex flex-wrap gap-1.5" role="group" aria-label={label}>
        {options.map((o) => (
          <button
            key={String(o.value)}
            type="button"
            aria-pressed={o.value === value}
            onClick={() => onChange(o.value)}
            className={cx("cursor-pointer rounded-full border px-3.5 py-1.5 text-xs font-semibold transition active:scale-95", o.value === value ? "border-primary bg-primary text-on-primary shadow-[0_6px_14px_-8px_var(--primary)]" : "border-border bg-surface text-muted hover:border-border-strong hover:text-text")}
          >
            {o.label}
          </button>
        ))}
      </div>
    </div>
  );
}

/** Assuntos do edital da disciplina: o aluno marca o que nunca viu, já estudou ou domina. */
function AssuntoChecklist({ s, marks, onSet, onAll, summary }: { s: WizardSubject; marks: Marks; onSet: (id: string, v: Mark) => void; onAll: (v: Mark) => void; summary: string }) {
  const [open, setOpen] = useState(false);
  if (s.items.length === 0) return null;
  return (
    <div className="rounded-xl border border-border bg-surface-2/60">
      <button type="button" onClick={() => setOpen((v) => !v)} aria-expanded={open} className="flex w-full cursor-pointer items-center justify-between gap-3 px-3.5 py-2.5 text-left text-sm font-semibold">
        <span>Conteúdos que você já estudou <span className="ml-1 text-xs font-normal text-muted">({summary})</span></span>
        <ChevronDown className={cx("h-4 w-4 text-muted transition-transform", open && "rotate-180")} aria-hidden />
      </button>
      {open && (
        <div className="swap-in space-y-2 border-t border-border px-3.5 py-3">
          <div className="flex flex-wrap gap-1.5">
            <Button variant="secondary" size="sm" onClick={() => onAll(1)}>Todos: já estudei</Button>
            <Button variant="secondary" size="sm" onClick={() => onAll(2)}>Todos: domino</Button>
            <Button variant="ghost" size="sm" onClick={() => onAll(0)}>Limpar</Button>
          </div>
          <ul className="max-h-[28rem] divide-y divide-border overflow-y-auto pr-1">
            {s.items.map((it) => {
              const v = (marks[it.id] ?? 0) as Mark;
              return (
                <li key={it.id} className="flex flex-wrap items-center justify-between gap-x-3 gap-y-1.5 py-2">
                  <span className="min-w-0 flex-1 text-sm">{it.title}</span>
                  <span className="flex shrink-0 gap-0.5 rounded-lg bg-surface-3 p-0.5" role="group" aria-label={it.title}>
                    {KNOWN_OPTIONS.map((o) => (
                      <button
                        key={o.value}
                        type="button"
                        aria-pressed={v === o.value}
                        onClick={() => onSet(it.id, o.value)}
                        className={cx("cursor-pointer rounded-md px-2.5 py-1 text-xs font-semibold transition", v === o.value ? (o.value === 2 ? "bg-ok text-white shadow-card" : o.value === 1 ? "bg-surface text-primary shadow-card" : "bg-surface text-text shadow-card") : "text-muted hover:text-text")}
                      >
                        {o.label}
                      </button>
                    ))}
                  </span>
                </li>
              );
            })}
          </ul>
        </div>
      )}
    </div>
  );
}

function PreviewBox({ preview, subjects, hours, detailed, onUseHours }: { preview: Preview | null; subjects: WizardSubject[]; hours: number; detailed?: boolean; onUseHours?: (h: number) => void }) {
  if (!preview) return <Card className="flex items-center gap-3 text-sm text-muted"><Loader2 className="h-4 w-4 animate-spin" aria-hidden />Calculando cobertura estimada…</Card>;
  if ("error" in preview) return <Alert tone="danger">{preview.error}</Alert>;
  const pct = Math.round(preview.coverageSelected * 100);
  const need = preview.fullEditalHoursPerWeek;
  const fits = need <= 50;
  return (
    <Card tone="ink" className="space-y-4">
      <div className="flex flex-wrap items-center gap-6">
        <Ring value={preview.coverageSelected} size={112} stroke={12} color="var(--gold)" track="rgb(255 255 255 / 0.12)" label={`Cobertura estimada do edital: ${pct}%`}>
          <span className="font-display text-4xl font-bold leading-none"><Count value={pct} suffix="%" /></span>
        </Ring>
        <div className="min-w-[14rem] flex-1 space-y-1.5">
          <p className="eyebrow flex items-center gap-1.5 !text-on-ink-muted">
            Cobertura estimada do edital
            <InfoTip align="start">
              Parte do edital das {subjects.length} disciplinas que o plano faz você estudar em {preview.totalWeeks} semanas (≈ {preview.capacityHours} h de conteúdo), levando em conta o que você já estudou. Ver o edital inteiro (só Teoria e Questões; revisões e fixação entram com o tempo que sobrar) exige ≈ {need} h por semana com o seu perfil.
            </InfoTip>
          </p>
          <p className="text-sm text-on-ink-muted">
            {pct >= 99
              ? "Com esse tempo, o plano fecha o edital inteiro."
              : fits
                ? <>Para fechar o edital inteiro: <strong className="text-on-ink">≈ {need} h por semana</strong> ({perDay(need)} por dia).</>
                : <>Fechar tudo exigiria ≈ {need} h por semana; o plano prioriza o que mais vale na prova.</>}
          </p>
          {pct < 99 && fits && onUseHours && hours < need && (
            <Button variant="onInk" size="sm" onClick={() => onUseHours(need)}>Usar {need} h por semana</Button>
          )}
        </div>
      </div>
      {detailed && (
        <ul className="grid gap-x-8 gap-y-2.5 text-sm sm:grid-cols-2">
          {preview.subjects.map((p) => (
            <li key={p.id} className="space-y-1">
              <div className="flex items-center justify-between gap-3">
                <span className="truncate">{subjects.find((s) => s.id === p.id)?.name}</span>
                <span className="tabular text-on-ink-muted">{Math.round(p.hours)} h · {Math.round(p.coverage * 100)}%</span>
              </div>
              <Progress value={p.coverage} size="sm" color="var(--gold)" label={`Cobertura de ${subjects.find((s) => s.id === p.id)?.name}`} className="!bg-white/10" />
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}
