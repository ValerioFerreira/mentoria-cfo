"use client";

import { useEffect, useId, useState, useTransition } from "react";
import { createPortal } from "react-dom";
import {
  AlertCircle,
  BookOpen,
  Check,
  CheckSquare,
  ChevronDown,
  ChevronRight,
  Filter,
  Layers,
  ListPlus,
  Play,
  RotateCcw,
  Sliders,
  Sparkles,
  Square,
  X,
} from "lucide-react";
import { Badge, Button, Card, Progress } from "@/components/ui";
import type { SubjectOverview } from "@/lib/data/questoes";
import { createCustomNotebook } from "@/lib/quiz/practice-actions";

interface Props {
  subjects: SubjectOverview[];
  isOpen: boolean;
  onClose: () => void;
}

export function MontarCadernoModal({ subjects, isOpen, onClose }: Props) {
  const [isPending, startTransition] = useTransition();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Modo de distribuição de quantidade: 'TOTAL' ou 'PER_SUBJECT'
  const [mode, setMode] = useState<"TOTAL" | "PER_SUBJECT">("TOTAL");
  const [totalCount, setTotalCount] = useState<number>(20);
  const [notebookTitle, setNotebookTitle] = useState<string>("");

  // Estado de seleção: quais matérias estão marcadas
  const [selectedSubjects, setSelectedSubjects] = useState<Set<string>>(
    new Set(subjects.map((s) => s.id)) // Por padrão, seleciona todas
  );

  // Seleção de tópicos por matéria: se não estiver no mapa ou for vazio, significa "TODOS OS ASSUNTOS"
  const [selectedTopicsBySubject, setSelectedTopicsBySubject] = useState<
    Map<string, Set<string>>
  >(new Map());

  // Quantidade de questões por matéria (para o modo PER_SUBJECT)
  const [countBySubject, setCountBySubject] = useState<Map<string, number>>(
    new Map(subjects.map((s) => [s.id, 5]))
  );

  // Qual disciplina está expandida para visualização de tópicos
  const [expandedSubjectId, setExpandedSubjectId] = useState<string | null>(null);

  useEffect(() => {
    if (!isOpen) return;
    const esc = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", esc);
    return () => document.removeEventListener("keydown", esc);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  // Alternar seleção de matéria
  const toggleSubject = (subjectId: string) => {
    setSelectedSubjects((prev) => {
      const next = new Set(prev);
      if (next.has(subjectId)) {
        next.delete(subjectId);
      } else {
        next.add(subjectId);
      }
      return next;
    });
  };

  // Selecionar todas as matérias
  const selectAllSubjects = () => {
    setSelectedSubjects(new Set(subjects.map((s) => s.id)));
  };

  // Desmarcar todas as matérias
  const deselectAllSubjects = () => {
    setSelectedSubjects(new Set());
  };

  // Alternar seleção de tópico específico dentro de uma disciplina
  const toggleTopic = (subjectId: string, topicId: string) => {
    const s = subjects.find((x) => x.id === subjectId);
    if (!s) return;

    setSelectedTopicsBySubject((prev) => {
      const next = new Map(prev);
      let currentSet = next.get(subjectId);

      // Se ainda não existia set específico, cria com todos os tópicos exceto o clicado
      if (!currentSet) {
        currentSet = new Set(s.topics.map((t) => t.id));
        currentSet.delete(topicId);
      } else {
        currentSet = new Set(currentSet);
        if (currentSet.has(topicId)) {
          currentSet.delete(topicId);
        } else {
          currentSet.add(topicId);
        }
      }

      next.set(subjectId, currentSet);
      return next;
    });
  };

  // Marcar todos os tópicos de uma disciplina
  const selectAllTopicsForSubject = (subjectId: string) => {
    setSelectedTopicsBySubject((prev) => {
      const next = new Map(prev);
      next.delete(subjectId); // Sem set = todos os tópicos
      return next;
    });
  };

  // Cálculo da quantidade disponível no acervo com base na seleção atual
  const calculateAvailableQuestions = () => {
    let count = 0;
    for (const sId of selectedSubjects) {
      const s = subjects.find((x) => x.id === sId);
      if (!s) continue;

      const topicsSet = selectedTopicsBySubject.get(sId);
      if (!topicsSet) {
        // Todos os tópicos da matéria
        count += s.totalQuestions;
      } else {
        // Tópicos específicos selecionados
        for (const t of s.topics) {
          if (topicsSet.has(t.id)) {
            count += t.totalQuestions;
          }
        }
      }
    }
    return count;
  };

  const totalAvailable = calculateAvailableQuestions();

  // Quantidade pretendida pelo usuário
  const totalWanted =
    mode === "TOTAL"
      ? totalCount
      : Array.from(selectedSubjects).reduce(
          (sum, sId) => sum + (countBySubject.get(sId) ?? 5),
          0
        );

  const isExceeded = totalWanted > totalAvailable;

  const handleGenerate = () => {
    setErrorMessage(null);

    if (selectedSubjects.size === 0) {
      setErrorMessage("Selecione pelo menos uma disciplina.");
      return;
    }

    if (totalWanted <= 0) {
      setErrorMessage("Defina uma quantidade maior que zero.");
      return;
    }

    if (isExceeded) {
      setErrorMessage(
        `A quantidade solicitada (${totalWanted}) excede o total disponível no acervo para os filtros selecionados (${totalAvailable} questões).`
      );
      return;
    }

    startTransition(async () => {
      const items = Array.from(selectedSubjects).map((sId) => {
        const topicsSet = selectedTopicsBySubject.get(sId);
        return {
          subjectId: sId,
          topics: topicsSet ? Array.from(topicsSet) : undefined,
          count: mode === "PER_SUBJECT" ? countBySubject.get(sId) ?? 5 : undefined,
        };
      });

      const res = await createCustomNotebook({
        title: notebookTitle.trim() || undefined,
        mode,
        totalCount: mode === "TOTAL" ? totalCount : undefined,
        items,
      });

      if (res && "error" in res) {
        setErrorMessage(res.error);
      }
    });
  };

  // portal: o botão que abre este diálogo fica dentro de um cartão animado (transform), que prenderia o `fixed` ao cartão
  return createPortal(
    <div className="modal-scroll fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-3 backdrop-blur-xs sm:p-4">
      <div role="dialog" aria-modal="true" aria-label="Montar caderno personalizado" className="relative flex max-h-[calc(100dvh-1.5rem)] w-full max-w-3xl flex-col overflow-hidden rounded-2xl border border-border bg-surface text-text shadow-2xl sm:max-h-[90dvh]">
        {/* Cabeçalho */}
        <div className="flex items-center justify-between border-b border-border/70 px-6 py-4 bg-surface-2/40">
          <div className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary/10 text-primary">
              <Sliders className="h-5 w-5" />
            </div>
            <div>
              <h2 className="font-display text-lg font-bold uppercase tracking-wide text-text">
                Montar Caderno Personalizado
              </h2>
              <p className="text-xs text-muted">
                Configure matérias, assuntos e quantidade de questões conforme sua estratégia.
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            aria-label="Fechar"
            className="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer sm:h-8 sm:w-8"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        {/* Corpo do Modal (Scrollável) */}
        <div className="p-6 space-y-6 overflow-y-auto flex-1">
          {/* Mensagem de Erro */}
          {errorMessage && (
            <div className="flex items-start gap-2.5 rounded-xl border border-primary/40 bg-primary/10 p-3.5 text-xs text-primary">
              <AlertCircle className="h-4 w-4 shrink-0 mt-0.5" />
              <div className="flex-1 font-medium">{errorMessage}</div>
            </div>
          )}

          {/* Nome do Caderno (Opcional) */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-text uppercase tracking-wider">
              Título do Caderno (Opcional)
            </label>
            <input
              type="text"
              value={notebookTitle}
              onChange={(e) => setNotebookTitle(e.target.value)}
              placeholder="Ex: Treino Geral AOCP — Semana 2"
              className="w-full rounded-xl border border-border bg-surface-2 px-3.5 py-2 text-sm text-text placeholder:text-muted focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
            />
          </div>

          {/* Modo de Quantidade */}
          <div className="rounded-xl border border-border/80 bg-surface-2/30 p-4 space-y-3">
            <label className="text-xs font-semibold uppercase tracking-wider text-muted block">
              Distribuição da Quantidade de Questões
            </label>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => setMode("TOTAL")}
                className={`flex items-start gap-3 p-3 rounded-xl border text-left transition cursor-pointer ${
                  mode === "TOTAL"
                    ? "border-primary bg-primary/10 text-text"
                    : "border-border/70 bg-surface hover:bg-surface-2 text-muted"
                }`}
              >
                <div
                  className={`mt-0.5 flex h-4 w-4 shrink-0 rounded-full border items-center justify-center ${
                    mode === "TOTAL" ? "border-primary" : "border-muted"
                  }`}
                >
                  {mode === "TOTAL" && <div className="h-2 w-2 rounded-full bg-primary" />}
                </div>
                <div>
                  <p className="text-xs font-bold text-text">Quantidade Total Definida</p>
                  <p className="text-[11px] text-muted leading-tight mt-0.5">
                    Sorteia aleatoriamente entre as matérias e assuntos selecionados.
                  </p>
                </div>
              </button>

              <button
                type="button"
                onClick={() => setMode("PER_SUBJECT")}
                className={`flex items-start gap-3 p-3 rounded-xl border text-left transition cursor-pointer ${
                  mode === "PER_SUBJECT"
                    ? "border-primary bg-primary/10 text-text"
                    : "border-border/70 bg-surface hover:bg-surface-2 text-muted"
                }`}
              >
                <div
                  className={`mt-0.5 flex h-4 w-4 shrink-0 rounded-full border items-center justify-center ${
                    mode === "PER_SUBJECT" ? "border-primary" : "border-muted"
                  }`}
                >
                  {mode === "PER_SUBJECT" && <div className="h-2 w-2 rounded-full bg-primary" />}
                </div>
                <div>
                  <p className="text-xs font-bold text-text">Quantidade por Matéria</p>
                  <p className="text-[11px] text-muted leading-tight mt-0.5">
                    Você escolhe quantas questões quer para cada matéria selecionada.
                  </p>
                </div>
              </button>
            </div>

            {/* Slider / Campo no Modo Total */}
            {mode === "TOTAL" && (
              <div className="pt-2 space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-semibold text-text">Quantidade Total de Questões:</span>
                  <span className="font-display text-base font-bold text-primary">
                    {totalCount} questões
                  </span>
                </div>
                <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
                  <input
                    type="range"
                    min={5}
                    max={Math.min(100, Math.max(5, totalAvailable))}
                    step={5}
                    value={totalCount}
                    onChange={(e) => setTotalCount(Number(e.target.value))}
                    className="min-w-32 flex-1 accent-primary"
                  />
                  <div className="flex gap-1">
                    {[10, 20, 30, 50].map((preset) => (
                      <button
                        key={preset}
                        type="button"
                        onClick={() => setTotalCount(preset)}
                        className={`rounded-lg px-2 py-1 text-[11px] font-semibold transition cursor-pointer ${
                          totalCount === preset
                            ? "bg-primary text-on-primary"
                            : "bg-surface-3 text-muted hover:text-text"
                        }`}
                      >
                        {preset}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Seleção de Disciplinas e Assuntos */}
          <div className="space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <label className="text-xs font-semibold uppercase tracking-wider text-muted">
                Disciplinas e Assuntos do Edital ({selectedSubjects.size} de {subjects.length} selecionadas)
              </label>

              <div className="flex items-center gap-2 text-xs">
                <button
                  type="button"
                  onClick={selectAllSubjects}
                  className="font-semibold text-primary hover:underline cursor-pointer"
                >
                  Marcar todas
                </button>
                <span className="text-muted">•</span>
                <button
                  type="button"
                  onClick={deselectAllSubjects}
                  className="font-semibold text-muted hover:text-text cursor-pointer"
                >
                  Desmarcar todas
                </button>
              </div>
            </div>

            {/* Lista das matérias */}
            <div className="space-y-2 max-h-72 overflow-y-auto pr-1">
              {subjects.map((s) => {
                const isChecked = selectedSubjects.has(s.id);
                const isExpanded = expandedSubjectId === s.id;
                const topicsMap = selectedTopicsBySubject.get(s.id);
                const isAllTopics = !topicsMap || topicsMap.size === s.topics.length;
                const selectedTopicsCount = topicsMap ? topicsMap.size : s.topics.length;
                const countVal = countBySubject.get(s.id) ?? 5;

                return (
                  <div
                    key={s.id}
                    className={`rounded-xl border transition ${
                      isChecked
                        ? "border-border bg-surface shadow-xs"
                        : "border-border/40 bg-surface-2/30 opacity-70"
                    }`}
                  >
                    <div className="flex items-center justify-between p-3 gap-3">
                      <div className="flex items-center gap-3 min-w-0 flex-1">
                        <button
                          type="button"
                          onClick={() => toggleSubject(s.id)}
                          className="flex items-center gap-2 cursor-pointer text-left flex-1 min-w-0"
                        >
                          <div
                            className={`flex h-4 w-4 shrink-0 items-center justify-center rounded border ${
                              isChecked
                                ? "border-primary bg-primary text-on-primary"
                                : "border-muted/60 bg-surface"
                            }`}
                          >
                            {isChecked && <Check className="h-3 w-3 stroke-[3]" />}
                          </div>
                          <div className="min-w-0">
                            <span className="text-xs font-bold text-text block truncate">
                              {s.name}
                            </span>
                            <span className="text-[11px] text-muted">
                              {s.totalQuestions} questões no acervo ·{" "}
                              {isAllTopics
                                ? "Todos os assuntos"
                                : `${selectedTopicsCount} de ${s.topics.length} assuntos`}
                            </span>
                          </div>
                        </button>
                      </div>

                      {/* Controles da Matéria */}
                      <div className="flex items-center gap-2 shrink-0">
                        {mode === "PER_SUBJECT" && isChecked && (
                          <div className="flex items-center gap-1.5 bg-surface-2 px-2 py-1 rounded-lg border border-border/60">
                            <span className="text-[11px] text-muted font-medium">Qtd:</span>
                            <input
                              type="number"
                              min={1}
                              max={s.totalQuestions}
                              value={countVal}
                              onChange={(e) => {
                                const val = Math.max(1, Math.min(s.totalQuestions, Number(e.target.value)));
                                setCountBySubject((prev) => new Map(prev).set(s.id, val));
                              }}
                              className="w-12 text-center text-xs font-bold text-text bg-transparent focus:outline-none"
                            />
                          </div>
                        )}

                        <button
                          type="button"
                          onClick={() => setExpandedSubjectId(isExpanded ? null : s.id)}
                          className="rounded-lg p-1 text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer"
                          title="Filtrar assuntos específicos"
                        >
                          {isExpanded ? (
                            <ChevronDown className="h-4 w-4" />
                          ) : (
                            <ChevronRight className="h-4 w-4" />
                          )}
                        </button>
                      </div>
                    </div>

                    {/* Tópicos Expansíveis */}
                    {isExpanded && (
                      <div className="border-t border-border/60 bg-surface-2/40 p-3 space-y-2">
                        <div className="flex items-center justify-between text-[11px]">
                          <span className="font-semibold text-muted uppercase tracking-wider">
                            Assuntos do Edital
                          </span>
                          <button
                            type="button"
                            onClick={() => selectAllTopicsForSubject(s.id)}
                            className="font-medium text-primary hover:underline cursor-pointer"
                          >
                            Selecionar todos os assuntos
                          </button>
                        </div>

                        <div className="grid gap-1.5 max-h-48 overflow-y-auto">
                          {s.topics.map((t) => {
                            const isTopicChecked =
                              !topicsMap || topicsMap.has(t.id);

                            return (
                              <button
                                key={t.id}
                                type="button"
                                onClick={() => toggleTopic(s.id, t.id)}
                                className={`flex items-center justify-between p-2 rounded-lg text-left text-xs transition cursor-pointer ${
                                  isTopicChecked
                                    ? "bg-surface border border-border/80 text-text"
                                    : "bg-transparent border border-transparent text-muted hover:bg-surface-3"
                                }`}
                              >
                                <div className="flex items-center gap-2 min-w-0 flex-1">
                                  <div
                                    className={`flex h-3.5 w-3.5 shrink-0 items-center justify-center rounded border ${
                                      isTopicChecked
                                        ? "border-primary bg-primary text-on-primary"
                                        : "border-muted/50 bg-surface"
                                    }`}
                                  >
                                    {isTopicChecked && <Check className="h-2.5 w-2.5 stroke-[3]" />}
                                  </div>
                                  <span className="truncate">{t.name}</span>
                                </div>
                                <span className="text-[10px] text-muted shrink-0 pl-2">
                                  {t.totalQuestions} {t.totalQuestions === 1 ? "q." : "qs."}
                                </span>
                              </button>
                            );
                          })}
                        </div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Rodapé do Modal com Resumo e Ação */}
        <div className="border-t border-border/70 p-4 bg-surface-2/60 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
          <div className="text-xs">
            <div className="flex items-center gap-2 font-semibold">
              <span className="text-text">Total a Gerar:</span>
              <span className="text-primary font-bold text-sm">
                {totalWanted} questões
              </span>
              <span className="text-muted">de {totalAvailable} disponíveis no acervo</span>
            </div>
            {isExceeded && (
              <p className="text-[11px] font-semibold text-primary mt-0.5">
                Atenção: reduza a quantidade para no máximo {totalAvailable} questões.
              </p>
            )}
          </div>

          <div className="flex items-center gap-2 self-end sm:self-auto">
            <Button
              variant="secondary"
              size="sm"
              onClick={onClose}
              disabled={isPending}
            >
              Cancelar
            </Button>
            <Button
              variant="primary"
              size="sm"
              onClick={handleGenerate}
              disabled={isPending || isExceeded || selectedSubjects.size === 0}
              className="gap-1.5"
            >
              <Play className="h-3.5 w-3.5" />
              <span>{isPending ? "Montando Caderno..." : "Gerar e Resolver Caderno"}</span>
            </Button>
          </div>
        </div>
      </div>
    </div>,
    document.body,
  );
}
