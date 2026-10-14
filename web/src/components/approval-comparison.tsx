"use client";

import { useMemo, type CSSProperties } from "react";
import { Badge, Card, InfoTip } from "@/components/ui";
import type { Contest } from "@/generated/prisma/client";
import {
  PROFILES_GENERATED_AT,
  blendProfiles,
  compareSubjects,
  compareTotal,
  profilesForContest,
  viewOf,
  type ApprovalProfile,
  type GapStatus,
  type ProfileView,
} from "@/lib/approval";
import type { BlockProjection } from "@/lib/metrics";
import { EXAM_TOTAL_QUESTIONS } from "@/lib/planner/constants";
import { subjectName } from "@/lib/ui-format";

const EDITAL_MIN_PCT = 0.3;
const num = (v: number) => (Number.isInteger(v) ? String(v) : v.toFixed(1).replace(".", ","));
const signed = (v: number) => `${v >= 0 ? "+" : "−"}${num(Math.abs(Math.round(v * 10) / 10))}`;
const pct = (v: number) => `${Math.round(v * 100)}%`;

const STATUS: Record<GapStatus, { label: string; tone: "ok" | "gold" | "primary" | "neutral"; color: string }> = {
  acima: { label: "no nível", tone: "ok", color: "var(--ok)" },
  perto: { label: "quase lá", tone: "gold", color: "var(--gold)" },
  abaixo: { label: "abaixo", tone: "primary", color: "var(--primary)" },
  "sem-dados": { label: "sem dados", tone: "neutral", color: "var(--surface-3)" },
};

export function ApprovalComparison({ subjects, contest, contestLabel }: { subjects: BlockProjection["subjects"]; contest: Contest; contestLabel: string }) {
  const profiles = useMemo(() => profilesForContest(contest), [contest]);
  if (profiles.length === 0) {
    return (
      <div className="space-y-4">
        <h3 className="font-display text-xl font-bold uppercase tracking-wide">Você × aprovados</h3>
        <Card tone="soft" className="py-3.5 text-sm text-muted">Ainda não há listas oficiais de concursos anteriores para {contestLabel}.</Card>
      </div>
    );
  }
  return <Comparison subjects={subjects} profiles={profiles} contestLabel={contestLabel} />;
}

function Comparison({ subjects, profiles, contestLabel }: { subjects: BlockProjection["subjects"]; profiles: ApprovalProfile[]; contestLabel: string }) {
  // um único concurso anterior: usa-o direto; vários: média ponderada (recentes pesam mais)
  const view: ProfileView = useMemo(() => (profiles.length === 1 ? viewOf(profiles[0]) : blendProfiles(profiles)), [profiles]);
  const profile = profiles.length === 1 ? profiles[0] : undefined;

  const rows = useMemo(() => compareSubjects(subjects, view), [subjects, view]);
  const total = useMemo(() => compareTotal(rows, view), [rows, view]);
  const comparable = rows.filter((r) => r.approved !== null);
  const missing = rows.filter((r) => r.approved === null);
  // maiores lacunas primeiro; sem dado do aluno por último
  const sorted = [...comparable].sort((a, b) => (a.gapQuestions === null ? 1 : 0) - (b.gapQuestions === null ? 1 : 0) || (a.gapQuestions ?? 0) - (b.gapQuestions ?? 0));
  const gaps = sorted.filter((r) => r.gapQuestions !== null && r.gapQuestions < 0).slice(0, 3);

  const max = EXAM_TOTAL_QUESTIONS;
  const userOnScale = total.userQuestions !== null && total.scope === "total" ? total.userQuestions : null;
  const diff = total.userQuestions !== null && total.approvedSameScope !== null ? total.userQuestions - total.approvedSameScope : null;
  const marks = [
    { key: "edital", label: "Mínimo do edital", at: EDITAL_MIN_PCT * max, color: "var(--muted)" },
    { key: "corte", label: "Nota de corte real", at: total.cutoffQuestions, color: "var(--gold)" },
    { key: "media", label: "Média dos aprovados", at: total.approvedQuestions, color: "var(--ok)" },
  ];

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-x-2 gap-y-2">
        <h3 className="flex items-center gap-2 font-display text-xl font-bold uppercase tracking-wide">
          Você × aprovados · {contestLabel}
          <InfoTip align="start">
            <strong>Aprovado</strong> = classificado dentro das vagas do edital (listas oficiais de classificação). A média e o mínimo são em acertos, trazidos para a prova de {max} questões.
            Os números são dos concursos anteriores de {contestLabel}
            {view.sources.length > 1 ? (
              <>, em média ponderada com peso maior para os mais recentes (cai pela metade a cada 4 anos). Pesos: {view.sources.map((s) => `${s.label} ${pct(s.weight)}`).join(" · ")}.</>
            ) : (
              <>: {view.sources[0].label}.</>
            )}{" "}
            Só os concursos de 2024 (Instituto AOCP) trazem a nota por disciplina; os de 2016 a 2018 mostram só o total. Seu acerto por disciplina só entra com 10 questões ou mais. Dados oficiais atualizados em {PROFILES_GENERATED_AT.split("-").reverse().join("/")}.
          </InfoTip>
        </h3>
      </div>

      <div className="grid gap-3 md:grid-cols-3">
        <Card className="space-y-1 p-4">
          <p className="eyebrow">Nota de corte real</p>
          <p className="font-display text-4xl font-bold leading-none tabular">
            {num(total.cutoffQuestions)}
            <span className="text-base font-medium text-muted"> de {max} questões</span>
          </p>
          <p className="text-xs text-muted">o aprovado mais fraco · o edital só elimina abaixo de {num(max * EDITAL_MIN_PCT)}</p>
        </Card>
        <Card className="space-y-1 p-4">
          <p className="eyebrow">Média dos aprovados</p>
          <p className="font-display text-4xl font-bold leading-none tabular">
            {num(total.approvedQuestions)}
            <span className="text-base font-medium text-muted"> de {max} · {pct(view.totalPct)}</span>
          </p>
          <p className="text-xs text-muted">
            {profile ? `${profile.approved.n} aprovados (${profile.vagas} vagas) · ${profile.banca}` : `${view.sources.length} concursos anteriores (${profiles.map((p) => p.year).join(", ")})`}
          </p>
        </Card>
        <Card tone="soft" className="space-y-1 p-4">
          <p className="eyebrow">Você hoje</p>
          <p className="font-display text-4xl font-bold leading-none tabular">
            {total.userQuestions === null ? "—" : num(total.userQuestions)}
            <span className="text-base font-medium text-muted">{total.scope === "parcial" ? " questões" : ` de ${max} questões`}</span>
          </p>
          <p className="text-xs text-muted">
            {total.scope === "sem-dados"
              ? Object.keys(view.subjects).length === 0 && total.measured > 0
                ? `este concurso só divulgou o total: faltam disciplinas medidas (${total.measured} de ${total.of})`
                : "faça cadernos (10+ questões por disciplina) para comparar"
              : total.scope === "parcial"
                ? `só ${total.measured} de ${total.of} disciplinas medidas: os aprovados fazem ${num(total.approvedSameScope ?? 0)} nelas (${signed(diff ?? 0)})`
                : `${signed(diff ?? 0)} questões vs. a média dos aprovados`}
          </p>
        </Card>
      </div>

      <div className="space-y-2">
        <div className="relative h-3 rounded-full bg-surface-3" role="img" aria-label={`Escala de 0 a ${max} questões com o mínimo do edital, a nota de corte real, a média dos aprovados e a sua estimativa`}>
          {userOnScale !== null && (
            <div className="absolute inset-y-0 left-0 rounded-full" style={{ width: `${Math.min(100, (userOnScale / max) * 100)}%`, background: userOnScale >= total.approvedQuestions ? "var(--ok)" : userOnScale >= total.cutoffQuestions ? "var(--gold)" : "var(--primary)" }} />
          )}
          {marks.map((m) => (
            <span key={m.key} className="absolute -top-1 h-5 w-[3px] rounded-full ring-2 ring-[var(--surface)]" style={{ left: `${(m.at / max) * 100}%`, background: m.color }} aria-hidden />
          ))}
        </div>
        <ul className="flex flex-wrap gap-x-5 gap-y-1 text-xs text-muted">
          {marks.map((m) => (
            <li key={m.key} className="flex items-center gap-1.5">
              <span className="h-2.5 w-[3px] rounded-full" style={{ background: m.color }} aria-hidden />
              {m.label}: <strong className="tabular text-text">{num(m.at)}</strong>
            </li>
          ))}
          {userOnScale !== null && (
            <li className="flex items-center gap-1.5">
              <span className="h-2.5 w-4 rounded-full bg-primary" aria-hidden />
              Você: <strong className="tabular text-text">{num(userOnScale)}</strong>
            </li>
          )}
        </ul>
      </div>

      {comparable.length === 0 ? (
        <Card tone="soft" className="py-3.5 text-sm text-muted">
          {profile ? "Os concursos anteriores só divulgaram a nota total, sem a nota por disciplina." : "Sem dados por disciplina."}
        </Card>
      ) : (
        <Card className="space-y-3 p-4">
          {gaps.length > 0 && (
            <p className="text-sm">
              <span className="font-semibold">Maiores lacunas:</span>{" "}
              {gaps.map((g, i) => (
                <span key={g.id}>
                  {i > 0 && " · "}
                  {subjectName(g.id)} <span className="tabular text-primary">({signed(g.gapQuestions!)} q)</span>
                </span>
              ))}
            </p>
          )}
          <ul className="divide-y divide-border">
            {sorted.map((r, i) => {
              const st = STATUS[r.status];
              return (
                <li key={r.id} className="rise grid gap-x-4 gap-y-1.5 py-2.5 sm:grid-cols-[minmax(0,12rem)_1fr_17rem] sm:items-center" style={{ "--i": Math.min(i, 8) } as CSSProperties}>
                  <span className="min-w-0 text-sm font-medium">{subjectName(r.id)}</span>
                  <div className="relative h-2 rounded-full bg-surface-3" role="img" aria-label={`${subjectName(r.id)}: você ${r.user === null ? "sem dados" : pct(r.user)}, aprovados ${pct(r.approved!)}`}>
                    {r.user !== null && <div className="absolute inset-y-0 left-0 rounded-full" style={{ width: `${r.user * 100}%`, background: st.color }} />}
                    <span className="absolute -top-1 h-4 w-[3px] rounded-full bg-text ring-2 ring-[var(--surface)]" style={{ left: `${r.approved! * 100}%` }} aria-hidden />
                  </div>
                  <div className="flex items-center justify-between gap-2 text-xs text-muted tabular sm:justify-end">
                    <span>
                      {r.user === null ? "—" : <strong className="text-text">{pct(r.user)}</strong>} · aprovados {pct(r.approved!)}
                      {r.gapQuestions !== null && <span className="ml-1">({signed(r.gapQuestions)} q)</span>}
                    </span>
                    <Badge tone={st.tone}>{st.label}</Badge>
                  </div>
                </li>
              );
            })}
          </ul>
          <p className="flex items-center gap-1.5 text-xs text-muted">
            <span className="h-3 w-[3px] rounded-full bg-text" aria-hidden /> traço = média dos aprovados · barra = seu acerto
            {missing.length > 0 && <span> · sem dado neste concurso: {missing.map((m) => subjectName(m.id)).join(", ")}</span>}
          </p>
        </Card>
      )}
    </div>
  );
}
