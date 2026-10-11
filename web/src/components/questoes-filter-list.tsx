"use client";

import { useState, useTransition } from "react";
import {
  BookOpen,
  CheckCircle2,
  ChevronDown,
  ChevronUp,
  Filter,
  Play,
  Search,
  Sparkles,
  Trophy,
  Sliders,
  XCircle,
} from "lucide-react";
import { BLOCK_COLOR, Badge, Button, Card, Progress } from "@/components/ui";
import type { SubjectOverview } from "@/lib/data/questoes";
import { startSubjectPracticeQuiz } from "@/lib/quiz/practice-actions";
import { MontarCadernoModal } from "@/components/montar-caderno-modal";

interface Props {
  subjects: SubjectOverview[];
  availableBancas?: string[];
}

export function QuestoesFilterList({ subjects, availableBancas = [] }: Props) {
  const [search, setSearch] = useState("");
  const [selectedBlock, setSelectedBlock] = useState<string>("ALL");
  const [selectedBanca, setSelectedBanca] = useState<string>("ALL");
  const [expandedSubject, setExpandedSubject] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();
  const [activeSessionTopic, setActiveSessionTopic] = useState<string | null>(null);
  const [isCustomModalOpen, setIsCustomModalOpen] = useState(false);

  const toggleExpand = (id: string) => {
    setExpandedSubject((prev) => (prev === id ? null : id));
  };

  const handleStartPractice = (subjectId: string, topic?: string, limit?: number) => {
    const key = `${subjectId}::${topic || "all"}::${limit || "all"}`;
    setActiveSessionTopic(key);
    startTransition(async () => {
      await startSubjectPracticeQuiz({ subjectId, topic, limit });
    });
  };

  // Filtragem combinada por Bloco, Busca e Banca
  const filteredSubjects = subjects
    .map((s) => {
      if (selectedBanca !== "ALL" && (!s.bancas || !s.bancas.includes(selectedBanca))) {
        return null;
      }
      const visibleTopics = s.topics.filter((t) => {
        if (selectedBanca !== "ALL" && t.bancas && !t.bancas.includes(selectedBanca)) {
          return false;
        }
        return true;
      });
      return { ...s, topics: visibleTopics };
    })
    .filter((s): s is SubjectOverview => {
      if (!s) return false;
      // Filtro por bloco
      if (selectedBlock !== "ALL" && s.block !== selectedBlock) {
        return false;
      }

      // Filtro de busca
      if (!search.trim()) return true;

      const query = search.toLowerCase();
      const matchSubject = s.name.toLowerCase().includes(query);
      const matchTopic = s.topics.some((t) => t.name.toLowerCase().includes(query));

      return matchSubject || matchTopic;
    });

  return (
    <div className="space-y-6">
      {/* Banner / Ação Destacada: Montar Caderno */}
      <Card className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-5 bg-gradient-to-r from-primary/10 via-surface-2/40 to-surface border-border shadow-xs">
        <div className="flex items-center gap-3.5">
          <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-primary text-on-primary shadow-sm">
            <Sliders className="h-5 w-5" />
          </div>
          <div>
            <h3 className="font-display text-base font-bold text-text uppercase tracking-wide">
              Montar Caderno Personalizado
            </h3>
            <p className="text-xs text-muted mt-0.5">
              Selecione múltiplas disciplinas, escolha assuntos específicos e defina o volume de questões desejado.
            </p>
          </div>
        </div>
        <Button
          variant="primary"
          onClick={() => setIsCustomModalOpen(true)}
          className="shrink-0 gap-2 font-semibold shadow-xs"
        >
          <Sliders className="h-4 w-4" />
          <span>Montar Caderno</span>
        </Button>
      </Card>

      {/* Modal de Montagem de Caderno */}
      <MontarCadernoModal
        subjects={subjects}
        isOpen={isCustomModalOpen}
        onClose={() => setIsCustomModalOpen(false)}
      />
      {/* Controles de Busca e Filtro */}
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="relative flex-1">
          <Search className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted" aria-hidden />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Buscar matéria ou assunto do edital..."
            className="w-full rounded-xl border border-border bg-surface pl-10 pr-4 py-2.5 text-sm text-text placeholder:text-muted focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 shadow-xs"
          />
          {search && (
            <button
              onClick={() => setSearch("")}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-xs font-semibold text-muted hover:text-text cursor-pointer"
            >
              Limpar
            </button>
          )}
        </div>

        {/* Filtro por Bloco */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0">
          {[
            { id: "ALL", label: "Todos os Blocos" },
            { id: "I", label: "Bloco I" },
            { id: "II", label: "Bloco II" },
            { id: "III", label: "Bloco III" },
          ].map((b) => (
            <button
              key={b.id}
              onClick={() => setSelectedBlock(b.id)}
              className={`rounded-lg px-3 py-1.5 text-xs font-semibold transition cursor-pointer shrink-0 ${
                selectedBlock === b.id
                  ? "bg-primary text-on-primary shadow-xs"
                  : "bg-surface-2 text-muted hover:bg-surface-3 hover:text-text"
              }`}
            >
              {b.label}
            </button>
          ))}
        </div>
      </div>

      {/* Filtro Dinâmico por Banca */}
      {availableBancas.length > 0 && (
        <div className="flex items-center gap-2 overflow-x-auto pb-1">
          <span className="text-xs font-semibold uppercase tracking-wider text-muted shrink-0">
            Banca:
          </span>
          <button
            type="button"
            onClick={() => setSelectedBanca("ALL")}
            className={`rounded-lg px-2.5 py-1 text-xs font-semibold transition cursor-pointer shrink-0 ${
              selectedBanca === "ALL"
                ? "bg-gold text-on-ink font-bold shadow-xs"
                : "bg-surface-2 text-muted hover:bg-surface-3 hover:text-text border border-border/50"
            }`}
          >
            Todas as Bancas
          </button>
          {availableBancas.map((banca) => (
            <button
              key={banca}
              type="button"
              onClick={() => setSelectedBanca(banca)}
              className={`rounded-lg px-2.5 py-1 text-xs font-semibold transition cursor-pointer shrink-0 ${
                selectedBanca === banca
                  ? "bg-gold text-on-ink font-bold shadow-xs"
                  : "bg-surface-2 text-muted hover:bg-surface-3 hover:text-text border border-border/50"
              }`}
            >
              {banca}
            </button>
          ))}
        </div>
      )}

      {/* Lista de Disciplinas */}
      {filteredSubjects.length === 0 ? (
        <Card className="p-8 text-center text-muted">
          <Filter className="mx-auto h-8 w-8 text-muted/60 mb-2" />
          <p className="font-semibold text-text">Nenhuma matéria ou assunto encontrado</p>
          <p className="text-sm mt-1">Tente ajustar o termo de busca ou o filtro de bloco.</p>
        </Card>
      ) : (
        <div className="space-y-4">
          {filteredSubjects.map((s) => {
            const isExpanded = expandedSubject === s.id || (Boolean(search.trim()) && s.topics.some((t) => t.name.toLowerCase().includes(search.toLowerCase())));
            const blockColor = BLOCK_COLOR[s.block] || "var(--primary)";
            const hasActivity = s.userAnswered > 0;

            // Filtrar tópicos se houver busca
            const visibleTopics = search.trim()
              ? s.topics.filter((t) => t.name.toLowerCase().includes(search.toLowerCase()))
              : s.topics;

            return (
              <Card
                key={s.id}
                className="overflow-hidden border border-border bg-surface transition shadow-card"
              >
                {/* Cabeçalho da Disciplina */}
                <div
                  onClick={() => toggleExpand(s.id)}
                  className="flex flex-col gap-3 p-4 sm:flex-row sm:items-center sm:justify-between cursor-pointer hover:bg-surface-2/40 transition select-none"
                >
                  <div className="flex items-center gap-3.5 min-w-0">
                    <span
                      className="h-10 w-2 shrink-0 rounded-full"
                      style={{ backgroundColor: blockColor }}
                      aria-hidden
                    />
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="font-display text-lg font-bold uppercase tracking-wide text-text truncate">
                          {s.name}
                        </span>
                        <Badge tone="neutral" className="text-[10px]">
                          Bloco {s.block}
                        </Badge>
                        {s.bancas && s.bancas.map((b) => (
                          <Badge key={b} tone="gold" className="text-[10px]">
                            {b}
                          </Badge>
                        ))}
                      </div>
                      <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-muted mt-0.5">
                        <span>
                          {s.totalQuestions} {s.totalQuestions === 1 ? "questão" : "questões"} no acervo
                        </span>
                        <span>•</span>
                        <span>
                          {s.topics.length} {s.topics.length === 1 ? "assunto" : "assuntos"} do edital
                        </span>
                        {hasActivity && (
                          <>
                            <span>•</span>
                            <span className="font-medium text-ok">
                              {s.userAnswered} resolvidas ({s.userAccuracy ?? 0}% acerto)
                            </span>
                          </>
                        )}
                      </div>
                    </div>
                  </div>

                  {/* Ações e Progresso */}
                  <div className="flex items-center gap-3 self-end sm:self-auto">
                    {hasActivity && (
                      <div className="hidden md:flex flex-col items-end text-xs">
                        <span className="font-semibold text-text">
                          {s.userCorrect}/{s.userAnswered} acertos
                        </span>
                        <div className="w-24 mt-1">
                          <Progress
                            value={s.userAccuracy ?? 0}
                            color={(s.userAccuracy ?? 0) >= 70 ? "var(--ok)" : "var(--gold)"}
                          />
                        </div>
                      </div>
                    )}

                    <Button
                      size="sm"
                      variant="primary"
                      onClick={(e) => {
                        e.stopPropagation();
                        handleStartPractice(s.id, undefined, 20);
                      }}
                      disabled={isPending}
                      className="shrink-0 gap-1.5"
                    >
                      <Play className="h-3.5 w-3.5" />
                      <span>{isPending && activeSessionTopic === `${s.id}::all::20` ? "Iniciando..." : "Treinar Matéria"}</span>
                    </Button>

                    <button
                      className="flex h-8 w-8 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition"
                      aria-label={isExpanded ? "Recolher assuntos" : "Expandir assuntos"}
                    >
                      {isExpanded ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
                    </button>
                  </div>
                </div>

                {/* Lista de Assuntos Expansível */}
                {isExpanded && (
                  <div className="border-t border-border/70 bg-surface-2/20 p-4 space-y-2.5">
                    <div className="flex items-center justify-between text-xs font-semibold text-muted uppercase tracking-wider px-1">
                      <span>Assuntos do Edital Unificado</span>
                      <span>{visibleTopics.length} disponíveis</span>
                    </div>

                    <div className="grid gap-2">
                      {visibleTopics.map((topic) => {
                        const hasTopicActivity = topic.userAnswered > 0;
                        const is5Pending = isPending && activeSessionTopic === `${s.id}::${topic.name}::5`;
                        const isAllPending = isPending && activeSessionTopic === `${s.id}::${topic.name}::all`;

                        return (
                          <div
                            key={topic.name}
                            className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 rounded-xl border border-border/60 bg-surface p-3 transition hover:border-border hover:shadow-xs"
                          >
                            <div className="min-w-0 flex-1">
                              <p className="text-sm font-semibold text-text leading-snug">
                                {topic.name}
                              </p>
                              <div className="flex flex-wrap items-center gap-2 text-xs text-muted mt-1">
                                <span className="rounded-md bg-surface-3 px-2 py-0.5 font-medium text-text/80">
                                  {topic.totalQuestions} {topic.totalQuestions === 1 ? "questão" : "questões"}
                                </span>
                                {hasTopicActivity && (
                                  <span
                                    className={`font-semibold ${
                                      (topic.userAccuracy ?? 0) >= 70
                                        ? "text-ok"
                                        : (topic.userAccuracy ?? 0) >= 50
                                        ? "text-gold"
                                        : "text-primary"
                                    }`}
                                  >
                                    {topic.userCorrect}/{topic.userAnswered} acertos ({topic.userAccuracy}%)
                                  </span>
                                )}
                              </div>
                            </div>

                            {/* Botões para praticar este assunto */}
                            <div className="flex items-center gap-2 self-end sm:self-auto shrink-0">
                              <Button
                                size="sm"
                                variant="secondary"
                                onClick={() => handleStartPractice(s.id, topic.name, 5)}
                                disabled={isPending}
                                className="text-xs px-2.5 py-1"
                                title="Treino rápido com 5 questões deste assunto"
                              >
                                {is5Pending ? "Carregando..." : "5 questões"}
                              </Button>

                              <Button
                                size="sm"
                                variant="secondary"
                                onClick={() => handleStartPractice(s.id, topic.name, 10)}
                                disabled={isPending}
                                className="text-xs px-2.5 py-1"
                                title="Treino com 10 questões deste assunto"
                              >
                                10 questões
                              </Button>

                              <Button
                                size="sm"
                                variant="primary"
                                onClick={() => handleStartPractice(s.id, topic.name)}
                                disabled={isPending}
                                className="text-xs px-3 py-1 gap-1"
                                title="Resolver todas as questões disponíveis deste assunto"
                              >
                                <Play className="h-3 w-3" />
                                {isAllPending ? "Iniciando..." : "Todas"}
                              </Button>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}
