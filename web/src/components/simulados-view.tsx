"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import {
  AlertCircle,
  Award,
  BookOpen,
  Calendar,
  CheckCircle2,
  Clock,
  ExternalLink,
  Flame,
  HelpCircle,
  Layers,
  ListChecks,
  Play,
  RotateCcw,
  ShieldAlert,
  ShieldCheck,
  Trophy,
  XCircle,
} from "lucide-react";
import { Badge, Button, Card, Progress } from "@/components/ui";
import type { SimuladoReadiness, SupportedSimuladoContest } from "@/lib/data/simulados";
import { startSimuladoSession } from "@/lib/quiz/simulado-actions";
import { fmtDuration } from "@/lib/ui-format";

interface SimuladoHistoryItem {
  id: string;
  title: string;
  contest: SupportedSimuladoContest;
  roleName: string;
  startedAt: Date;
  finishedAt: Date | null;
  isFinished: boolean;
  score: number;
  total: number;
  percent: number;
  passedCutoff: boolean;
}

interface Props {
  readinessMap?: Record<SupportedSimuladoContest, SimuladoReadiness>;
  oficialReadiness?: SimuladoReadiness;
  soldadoReadiness?: SimuladoReadiness;
  history: SimuladoHistoryItem[];
}

const CONTEST_TABS: {
  key: SupportedSimuladoContest;
  badge: string;
  role: string;
  desc: string;
  org: "CBMPE" | "PMPE";
}[] = [
  { key: "CBMPE_OFICIAL", badge: "CBMPE", role: "Oficial BM (2º Tenente)", desc: "4h30min · 70 questões · CFO", org: "CBMPE" },
  { key: "CBMPE_SOLDADO", badge: "CBMPE", role: "Soldado BM (Praça)", desc: "4h00min · 60 questões · CFSd", org: "CBMPE" },
  { key: "PMPE_OFICIAL", badge: "PMPE", role: "Oficial PM (2º Tenente)", desc: "4h30min · 70 questões · CFO", org: "PMPE" },
  { key: "PMPE_SOLDADO", badge: "PMPE", role: "Soldado PM (Praça)", desc: "4h00min · 60 questões · CFSd", org: "PMPE" },
];

export function SimuladosView({ readinessMap, oficialReadiness, soldadoReadiness, history }: Props) {
  const [selectedContest, setSelectedContest] = useState<SupportedSimuladoContest>("CBMPE_OFICIAL");
  const [foreignLang, setForeignLang] = useState<"lingua-inglesa" | "lingua-espanhola">(
    "lingua-inglesa"
  );
  const [isPending, startTransition] = useTransition();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const currentReadiness =
    readinessMap?.[selectedContest] ||
    (selectedContest === "CBMPE_SOLDADO" ? soldadoReadiness! : oficialReadiness!);
  const config = currentReadiness.config;
  const hasForeignLang = config.subjects.some((s) => s.subjectId === "FOREIGN_LANG");

  const handleStartSimulado = () => {
    setErrorMessage(null);
    startTransition(async () => {
      const res = await startSimuladoSession({
        contest: selectedContest,
        foreignLang: hasForeignLang ? foreignLang : undefined,
      });

      if (res && "error" in res) {
        setErrorMessage(res.error);
      }
    });
  };

  return (
    <div className="space-y-8">
      {/* Seletor de Concurso / Cargo */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {CONTEST_TABS.map((tab) => {
          const isSelected = selectedContest === tab.key;
          return (
            <button
              key={tab.key}
              type="button"
              onClick={() => setSelectedContest(tab.key)}
              className={`flex items-start gap-3 p-3.5 rounded-2xl border text-left transition cursor-pointer ${
                isSelected
                  ? "border-primary bg-primary/10 shadow-sm"
                  : "border-border bg-surface hover:bg-surface-2/60 text-muted"
              }`}
            >
              <div
                className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-xl font-bold text-xs ${
                  isSelected
                    ? "bg-primary text-on-primary"
                    : "bg-surface-3 text-muted"
                }`}
              >
                {tab.badge}
              </div>
              <div className="min-w-0">
                <div className="flex items-center gap-1.5">
                  <h3 className="font-display text-sm font-bold text-text uppercase truncate">
                    {tab.role}
                  </h3>
                </div>
                <p className="text-[11px] text-muted mt-0.5 truncate">
                  {tab.desc}
                </p>
              </div>
            </button>
          );
        })}
      </div>

      {/* Cartão de Configuração e Diagnóstico da Prova */}
      <Card className="p-6 sm:p-8 space-y-6 border border-border bg-surface shadow-card">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-border/70 pb-5">
          <div>
            <span className="text-xs font-semibold uppercase tracking-wider text-muted">
              Estrutura Regulamentar do Edital
            </span>
            <h2 className="font-display text-2xl font-bold text-text mt-0.5">
              {config.title}
            </h2>
          </div>

          <div className="flex items-center gap-3">
            <div className="flex items-center gap-1.5 bg-surface-2 px-3 py-1.5 rounded-xl border border-border text-xs font-semibold text-text">
              <Clock className="h-4 w-4 text-primary" />
              <span>Duração: {config.durationMinutes} minutos ({fmtDuration(config.durationSeconds)})</span>
            </div>
            <div className="flex items-center gap-1.5 bg-surface-2 px-3 py-1.5 rounded-xl border border-border text-xs font-semibold text-text">
              <ListChecks className="h-4 w-4 text-ok" />
              <span>Total: {config.totalQuestions} questões</span>
            </div>
          </div>
        </div>

        {/* Mensagem de Erro (se houver) */}
        {errorMessage && (
          <div className="flex items-start gap-2.5 rounded-xl border border-primary/40 bg-primary/10 p-4 text-xs text-primary font-medium">
            <AlertCircle className="h-4 w-4 shrink-0 mt-0.5" />
            <span>{errorMessage}</span>
          </div>
        )}

        {/* Escolha de Língua Estrangeira (quando exigida no edital) */}
        {hasForeignLang && (
          <div className="rounded-xl border border-border/70 bg-surface-2/30 p-4 space-y-2">
            <label className="text-xs font-semibold uppercase tracking-wider text-muted block">
              Opção de Língua Estrangeira (Bloco I — 5 questões)
            </label>
            <div className="flex items-center gap-3">
              <button
                type="button"
                onClick={() => setForeignLang("lingua-inglesa")}
                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl border text-xs font-semibold transition cursor-pointer ${
                  foreignLang === "lingua-inglesa"
                    ? "border-primary bg-primary text-on-primary shadow-xs"
                    : "border-border bg-surface text-muted hover:text-text"
                }`}
              >
                <span>Língua Inglesa</span>
              </button>
              <button
                type="button"
                onClick={() => setForeignLang("lingua-espanhola")}
                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl border text-xs font-semibold transition cursor-pointer ${
                  foreignLang === "lingua-espanhola"
                    ? "border-primary bg-primary text-on-primary shadow-xs"
                    : "border-border bg-surface text-muted hover:text-text"
                }`}
              >
                <span>Língua Espanhola</span>
              </button>
            </div>
          </div>
        )}

        {/* Grade de Blocos e Regras Oficiais de Corte */}
        <div className="space-y-3">
          <h4 className="text-xs font-bold uppercase tracking-wider text-muted">
            Distribuição de Questões e Critérios de Aprovação
          </h4>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="rounded-xl border border-border bg-surface-2/40 p-3.5 space-y-1">
              <div className="flex items-center justify-between text-xs font-bold text-text">
                <span>Bloco I</span>
                <span className="text-primary">{config.blocks.I.totalQuestions} questões</span>
              </div>
              <p className="text-[11px] text-muted leading-tight">
                Mínimo de 30% ({config.blocks.I.minQuestions} acertos) para não ser desclassificado.
              </p>
            </div>

            <div className="rounded-xl border border-border bg-surface-2/40 p-3.5 space-y-1">
              <div className="flex items-center justify-between text-xs font-bold text-text">
                <span>Bloco II</span>
                <span className="text-primary">{config.blocks.II.totalQuestions} questões</span>
              </div>
              <p className="text-[11px] text-muted leading-tight">
                Mínimo de 30% ({config.blocks.II.minQuestions} acertos) para não ser desclassificado.
              </p>
            </div>

            <div className="rounded-xl border border-border bg-surface-2/40 p-3.5 space-y-1">
              <div className="flex items-center justify-between text-xs font-bold text-text">
                <span>Bloco III</span>
                <span className="text-primary">{config.blocks.III.totalQuestions} questões</span>
              </div>
              <p className="text-[11px] text-muted leading-tight">
                Mínimo de 30% ({config.blocks.III.minQuestions} acertos) e não zerar nenhuma matéria.
              </p>
            </div>
          </div>
        </div>

        {/* Diagnóstico de Disponibilidade do Acervo em Tempo Real */}
        <div className="rounded-2xl border border-border/80 bg-surface-2/30 p-5 space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div className="flex items-center gap-2">
              <span className="font-display text-sm font-bold uppercase tracking-wide text-text">
                Verificação Prévia de Acervo
              </span>
              {currentReadiness.isReady ? (
                <Badge tone="ok" className="text-[10px] font-bold">
                  Acervo Completo
                </Badge>
              ) : (
                <Badge tone="primary" className="text-[10px] font-bold">
                  Acervo Incompleto ({currentReadiness.totalAvailable}/{currentReadiness.totalRequired})
                </Badge>
              )}
            </div>

            <span className="text-xs text-muted">
              Exclusivamente questões da banca <strong>AOCP / Instituto AOCP</strong>
            </span>
          </div>

          {/* Lista de Matérias e Status de Disponibilidade */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5">
            {currentReadiness.subjects.map((sub) => (
              <div
                key={sub.subjectId}
                className={`flex items-center justify-between p-2.5 rounded-xl border text-xs ${
                  sub.isSufficient
                    ? "border-border/60 bg-surface/80"
                    : "border-primary/40 bg-primary/5 text-primary"
                }`}
              >
                <div className="min-w-0 pr-2">
                  <p className="font-semibold text-text truncate">{sub.name}</p>
                  <p className="text-[11px] text-muted">
                    Bloco {sub.block} · Exige {sub.required}
                  </p>
                </div>

                <div className="text-right shrink-0">
                  <span
                    className={`font-mono font-bold ${
                      sub.isSufficient ? "text-ok" : "text-primary"
                    }`}
                  >
                    {sub.available}/{sub.required}
                  </span>
                  <span
                    className={`block text-[10px] font-semibold uppercase ${
                      sub.isSufficient ? "text-ok" : "text-primary"
                    }`}
                  >
                    {sub.isSufficient ? "Pronto" : "Falta"}
                  </span>
                </div>
              </div>
            ))}
          </div>

          {/* Alerta Metodológico caso haja matérias insuficientes */}
          {!currentReadiness.isReady && (
            <div className="flex items-start gap-3 rounded-xl border border-gold/40 bg-gold/10 p-4 text-xs text-text leading-relaxed">
              <AlertCircle className="h-4 w-4 shrink-0 text-gold mt-0.5" />
              <div>
                <p className="font-bold text-gold-text">
                  Garantia de Fidelidade ao Edital {config.title}
                </p>
                <p className="mt-1 text-muted">
                  Para garantir a máxima precisão metodológica, a plataforma não gera simulados com distribuição adulterada ou disciplinas ausentes. A geração desta prova será liberada automaticamente assim que os cadernos completos das disciplinas marcadas acima forem integrados à pasta oficial de questões.
                </p>
              </div>
            </div>
          )}

          {/* Ação de Iniciar Simulado */}
          <div className="flex items-center justify-between border-t border-border/70 pt-4">
            <div className="text-xs text-muted">
              {currentReadiness.isReady
                ? "Ao iniciar, o cronômetro oficial começará a correr. Respostas são salvas automaticamente a cada clique."
                : "Aguarde a liberação do acervo completo ou pratique via Montar Caderno na página de Questões."}
            </div>

            <Button
              variant="primary"
              size="lg"
              onClick={handleStartSimulado}
              disabled={!currentReadiness.isReady || isPending}
              className="gap-2 font-bold px-6 shadow-md"
            >
              <Play className="h-4 w-4" />
              <span>{isPending ? "Preparando Prova..." : "Iniciar Simulado Oficial"}</span>
            </Button>
          </div>
        </div>
      </Card>

      {/* Histórico de Simulados Realizados */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="font-display text-lg font-bold uppercase tracking-wide text-text">
            Seu Histórico de Simulados
          </h3>
          <span className="text-xs text-muted font-semibold">
            {history.length} {history.length === 1 ? "prova realizada" : "provas realizadas"}
          </span>
        </div>

        {history.length === 0 ? (
          <Card className="p-8 text-center text-muted border border-border bg-surface">
            <Trophy className="mx-auto h-8 w-8 text-muted/50 mb-2" />
            <p className="font-semibold text-text">Nenhum simulado oficial realizado ainda</p>
            <p className="text-xs mt-1">
              Assim que você realizar um simulado completo, o histórico, percentuais e critérios de corte serão registrados aqui.
            </p>
          </Card>
        ) : (
          <div className="grid gap-3">
            {history.map((h) => (
              <Card
                key={h.id}
                className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 border border-border bg-surface hover:bg-surface-2/40 transition"
              >
                <div className="flex items-center gap-3.5 min-w-0">
                  <div
                    className={`flex h-11 w-11 shrink-0 items-center justify-center rounded-xl font-bold text-sm ${
                      h.passedCutoff
                        ? "bg-ok/20 text-ok border border-ok/40"
                        : "bg-primary/20 text-primary border border-primary/40"
                    }`}
                  >
                    {h.percent}%
                  </div>

                  <div className="min-w-0">
                    <div className="flex items-center gap-2">
                      <p className="font-display text-sm font-bold text-text truncate">
                        {h.title}
                      </p>
                      {h.passedCutoff ? (
                        <Badge tone="ok" className="text-[10px]">
                          Aprovado no Corte
                        </Badge>
                      ) : (
                        <Badge tone="primary" className="text-[10px]">
                          Reprovado no Corte
                        </Badge>
                      )}
                    </div>
                    <p className="text-xs text-muted mt-0.5">
                      {h.startedAt.toLocaleDateString("pt-BR")} · {h.score} de {h.total} pontos ·{" "}
                      {h.isFinished ? "Finalizado" : "Em andamento"}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-2 self-end sm:self-auto">
                  {h.isFinished ? (
                    <Link
                      href={`/simulados/resultado/${h.id}`}
                      className="inline-flex items-center gap-1.5 rounded-xl border border-border bg-surface-2 px-3 py-1.5 text-xs font-semibold text-text hover:bg-surface-3 transition"
                    >
                      <span>Ver Resultado e Gabarito</span>
                      <ExternalLink className="h-3.5 w-3.5" />
                    </Link>
                  ) : (
                    <Link
                      href={`/simulados/${h.id}`}
                      className="inline-flex items-center gap-1.5 rounded-xl bg-primary px-3 py-1.5 text-xs font-semibold text-on-primary hover:bg-primary-hover transition"
                    >
                      <Play className="h-3.5 w-3.5" />
                      <span>Continuar Prova</span>
                    </Link>
                  )}
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
