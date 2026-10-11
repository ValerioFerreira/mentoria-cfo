"use client";

import { useState, useTransition, useMemo, useRef, useEffect } from "react";
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
  Building2,
  Check,
  X,
} from "lucide-react";
import { BLOCK_COLOR, Badge, Button, Card, Progress } from "@/components/ui";
import type { SubjectOverview } from "@/lib/data/questoes";
import { startSubjectPracticeQuiz } from "@/lib/quiz/practice-actions";
import { MontarCadernoModal } from "@/components/montar-caderno-modal";

interface Props {
  subjects: SubjectOverview[];
  availableBancas?: string[];
  bancaCounts?: Record<string, number>;
}

export function QuestoesFilterList({ subjects, availableBancas = [], bancaCounts = {} }: Props) {
  const [search, setSearch] = useState("");
  const [selectedBlock, setSelectedBlock] = useState<string>("ALL");
  const [selectedBancas, setSelectedBancas] = useState<string[]>([]);
  const [isBancaOpen, setIsBancaOpen] = useState(false);
  const [bancaSearch, setBancaSearch] = useState("");
  const [expandedSubject, setExpandedSubject] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();
  const [activeSessionTopic, setActiveSessionTopic] = useState<string | null>(null);
  const [isCustomModalOpen, setIsCustomModalOpen] = useState(false);

  const bancaDropdownRef = useRef<HTMLDivElement>(null);

  // Fechar dropdown ao clicar fora
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (bancaDropdownRef.current && !bancaDropdownRef.current.contains(event.target as Node)) {
        setIsBancaOpen(false);
      }
    }
    if (isBancaOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    }
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isBancaOpen]);

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

  // Se nenhuma banca estiver selecionada ou se todas estiverem selecionadas, considera "Todas as bancas"
  const isAllBancasSelected =
    selectedBancas.length === 0 || selectedBancas.length === availableBancas.length;

  const totalAcervo = useMemo(() => {
    return Object.values(bancaCounts).reduce((acc, c) => acc + c, 0);
  }, [bancaCounts]);

  const totalSelectedQuestions = useMemo(() => {
    if (isAllBancasSelected) return totalAcervo;
    return selectedBancas.reduce((acc, b) => acc + (bancaCounts[b] || 0), 0);
  }, [isAllBancasSelected, selectedBancas, bancaCounts, totalAcervo]);

  const toggleBanca = (banca: string) => {
    setSelectedBancas((prev) => {
      if (isAllBancasSelected) {
        // Se estava em "Todas", selecionar apenas essa banca
        return [banca];
      }
      if (prev.includes(banca)) {
        const next = prev.filter((b) => b !== banca);
        return next;
      } else {
        return [...prev, banca];
      }
    });
  };

  const handleSelectAllBancas = () => {
    setSelectedBancas([]);
    setBancaSearch("");
  };

  const handleClearBancas = () => {
    setSelectedBancas([]);
    setBancaSearch("");
  };

  // Bancas filtradas pelo autocomplete da pesquisa
  const filteredBancasForDropdown = useMemo(() => {
    if (!bancaSearch.trim()) return availableBancas;
    const q = bancaSearch.toLowerCase().trim();
    return availableBancas.filter((b) => b.toLowerCase().includes(q));
  }, [availableBancas, bancaSearch]);

  // Filtragem e mapeamento das disciplinas respeitando as regras estritas:
  // - Se uma disciplina tiver 0 questões da banca filtrada, ELA NÃO DEVE SUMIR DA TELA.
  const processedSubjects = useMemo(() => {
    return subjects.map((s) => {
      // Cálculo das questões disponíveis para as bancas filtradas
      let countInSubject = s.totalQuestions;
      let relevantBancasForBadge: string[] = [];

      if (!isAllBancasSelected) {
        countInSubject = selectedBancas.reduce((acc, b) => acc + (s.bancaCounts?.[b] || 0), 0);
        // Exibir apenas as bancas selecionadas que possuem questões nesta matéria
        relevantBancasForBadge = selectedBancas.filter((b) => (s.bancaCounts?.[b] || 0) > 0);
      }

      // Processar tópicos
      const processedTopics = s.topics.map((t) => {
        let countInTopic = t.totalQuestions;
        if (!isAllBancasSelected) {
          countInTopic = selectedBancas.reduce((acc, b) => acc + (t.bancaCounts?.[b] || 0), 0);
        }
        return {
          ...t,
          filteredQuestionsCount: countInTopic,
        };
      });

      return {
        ...s,
        filteredQuestionsCount: countInSubject,
        relevantBancasForBadge,
        topics: processedTopics,
      };
    });
  }, [subjects, isAllBancasSelected, selectedBancas]);

  // Aplicação dos filtros de Bloco e de Busca por texto
  const filteredSubjects = useMemo(() => {
    return processedSubjects.filter((s) => {
      // Filtro por bloco
      if (selectedBlock !== "ALL" && s.block !== selectedBlock) {
        return false;
      }

      // Filtro de busca textual
      if (!search.trim()) return true;
      const query = search.toLowerCase();
      const matchSubject = s.name.toLowerCase().includes(query);
      const matchTopic = s.topics.some((t) => t.name.toLowerCase().includes(query));
      return matchSubject || matchTopic;
    });
  }, [processedSubjects, selectedBlock, search]);

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

      {/* Barra de Controles: Busca, Blocos e Seletor de Bancas à Direita */}
      <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
        {/* Campo de Busca */}
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

        {/* Filtros da Direita: Blocos e Dropdown de Bancas */}
        <div className="flex flex-wrap items-center justify-between sm:justify-end gap-2.5">
          {/* Filtro por Bloco */}
          <div className="flex items-center gap-1.5 overflow-x-auto pb-0.5 sm:pb-0">
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

          {/* Seletor Dropdown de Bancas Alinhado à Direita */}
          <div className="relative" ref={bancaDropdownRef}>
            <button
              type="button"
              onClick={() => setIsBancaOpen(!isBancaOpen)}
              className={`flex items-center gap-2 rounded-xl px-3.5 py-2 text-xs font-semibold border transition cursor-pointer shadow-xs ${
                !isAllBancasSelected
                  ? "bg-gold text-on-ink border-gold/80 font-bold"
                  : "bg-surface border-border text-text hover:bg-surface-2"
              }`}
            >
              <Building2 className="h-4 w-4" />
              <span>
                {isAllBancasSelected
                  ? `Todas as Bancas (${totalAcervo.toLocaleString("pt-BR")})`
                  : selectedBancas.length === 1
                  ? `${selectedBancas[0]} (${(bancaCounts[selectedBancas[0]] ?? 0).toLocaleString("pt-BR")})`
                  : `${selectedBancas.length} bancas selecionadas (${totalSelectedQuestions.toLocaleString("pt-BR")})`}
              </span>
              <ChevronDown className={`h-3.5 w-3.5 transition-transform duration-200 ${isBancaOpen ? "rotate-180" : ""}`} />
            </button>

            {/* Menu Dropdown com Autocomplete e Multi-seleção */}
            {isBancaOpen && (
              <div className="absolute right-0 top-full mt-2 z-50 w-72 sm:w-80 rounded-2xl border border-border bg-surface p-3 shadow-lift backdrop-blur-md animate-in fade-in zoom-in-95 duration-150">
                {/* Cabeçalho do Dropdown com Busca/Autocomplete */}
                <div className="space-y-2 mb-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold uppercase tracking-wider text-muted">
                      Filtrar por Banca
                    </span>
                    <button
                      onClick={() => setIsBancaOpen(false)}
                      className="text-muted hover:text-text p-1 rounded-md"
                    >
                      <X className="h-3.5 w-3.5" />
                    </button>
                  </div>

                  <div className="relative">
                    <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted" />
                    <input
                      type="text"
                      value={bancaSearch}
                      onChange={(e) => setBancaSearch(e.target.value)}
                      placeholder="Pesquisar banca..."
                      autoFocus
                      className="w-full rounded-lg border border-border bg-surface-2 pl-8 pr-3 py-1.5 text-xs text-text placeholder:text-muted focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary/20"
                    />
                    {bancaSearch && (
                      <button
                        onClick={() => setBancaSearch("")}
                        className="absolute right-2.5 top-1/2 -translate-y-1/2 text-[10px] text-muted hover:text-text"
                      >
                        Limpar
                      </button>
                    )}
                  </div>

                  {/* Botões Rápidos: Selecionar Todas / Limpar Filtros */}
                  <div className="flex items-center justify-between pt-1 border-t border-border/50 text-[11px]">
                    <button
                      type="button"
                      onClick={handleSelectAllBancas}
                      className="font-semibold text-primary hover:underline cursor-pointer"
                    >
                      Selecionar todas (Padrão)
                    </button>
                    <button
                      type="button"
                      onClick={handleClearBancas}
                      className="font-semibold text-muted hover:text-text cursor-pointer"
                    >
                      Limpar filtros
                    </button>
                  </div>
                </div>

                {/* Lista com Checkbox para Seleção Múltipla */}
                <div className="max-h-64 overflow-y-auto space-y-1 pr-1 custom-scrollbar">
                  {/* Opção Todas as Bancas */}
                  <label
                    onClick={handleSelectAllBancas}
                    className={`flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-semibold cursor-pointer transition ${
                      isAllBancasSelected
                        ? "bg-gold/20 text-text font-bold"
                        : "hover:bg-surface-2 text-muted"
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <div className={`h-4 w-4 rounded flex items-center justify-center border transition ${
                        isAllBancasSelected
                          ? "bg-gold border-gold text-on-ink"
                          : "border-border bg-surface"
                      }`}>
                        {isAllBancasSelected && <Check className="h-3 w-3" />}
                      </div>
                      <span>Todas as Bancas</span>
                    </div>
                    <span className="text-[10px] font-normal px-1.5 py-0.5 rounded-full bg-surface-3 text-muted">
                      {totalAcervo.toLocaleString("pt-BR")}
                    </span>
                  </label>

                  {filteredBancasForDropdown.map((banca) => {
                    const isChecked = !isAllBancasSelected && selectedBancas.includes(banca);
                    const count = bancaCounts[banca] ?? 0;

                    return (
                      <label
                        key={banca}
                        onClick={() => toggleBanca(banca)}
                        className={`flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-semibold cursor-pointer transition ${
                          isChecked
                            ? "bg-gold/15 text-text font-bold"
                            : "hover:bg-surface-2 text-muted"
                        }`}
                      >
                        <div className="flex items-center gap-2">
                          <div className={`h-4 w-4 rounded flex items-center justify-center border transition ${
                            isChecked
                              ? "bg-gold border-gold text-on-ink"
                              : "border-border bg-surface"
                          }`}>
                            {isChecked && <Check className="h-3 w-3" />}
                          </div>
                          <span>{banca}</span>
                        </div>
                        <span className="text-[10px] font-normal px-1.5 py-0.5 rounded-full bg-surface-3 text-muted">
                          {count.toLocaleString("pt-BR")}
                        </span>
                      </label>
                    );
                  })}

                  {filteredBancasForDropdown.length === 0 && (
                    <p className="text-center py-4 text-xs text-muted">
                      Nenhuma banca encontrada com &ldquo;{bancaSearch}&rdquo;
                    </p>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>

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
            const isExpanded =
              expandedSubject === s.id ||
              (Boolean(search.trim()) &&
                s.topics.some((t) => t.name.toLowerCase().includes(search.toLowerCase())));
            const blockColor = BLOCK_COLOR[s.block] || "var(--primary)";
            const hasActivity = s.userAnswered > 0;
            const hasAvailableQuestions = s.filteredQuestionsCount > 0;

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
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="font-display text-lg font-bold uppercase tracking-wide text-text truncate">
                          {s.name}
                        </span>
                        <Badge tone="neutral" className="text-[10px]">
                          Bloco {s.block}
                        </Badge>
                        {/* Regra de exibição dos badges de banca:
                            - Em "Todas as bancas": NÃO APARECEM nomes das bancas
                            - Se banca(s) selecionada(s): aparecem os badges amarelos das bancas selecionadas */}
                        {!isAllBancasSelected &&
                          s.relevantBancasForBadge.map((b) => (
                            <Badge key={b} tone="gold" className="text-[10px]">
                              {b}
                            </Badge>
                          ))}
                      </div>
                      <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-muted mt-0.5">
                        <span className={hasAvailableQuestions ? "font-semibold text-text" : "text-muted"}>
                          {s.filteredQuestionsCount}{" "}
                          {s.filteredQuestionsCount === 1 ? "questão" : "questões"} no acervo
                          {!isAllBancasSelected && " (filtradas)"}
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
                        if (hasAvailableQuestions) {
                          handleStartPractice(s.id, undefined, 20);
                        }
                      }}
                      disabled={isPending || !hasAvailableQuestions}
                      className="shrink-0 gap-1.5"
                    >
                      <Play className="h-3.5 w-3.5" />
                      <span>
                        {isPending && activeSessionTopic === `${s.id}::all::20`
                          ? "Iniciando..."
                          : !hasAvailableQuestions
                          ? "0 questões"
                          : "Treinar Matéria"}
                      </span>
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
                      <span>Assuntos do Edital</span>
                      <span>{visibleTopics.length} disponíveis</span>
                    </div>

                    <div className="grid gap-2">
                      {visibleTopics.map((topic) => {
                        const hasTopicActivity = topic.userAnswered > 0;
                        const hasTopicQuestions = topic.filteredQuestionsCount > 0;
                        const is5Pending = isPending && activeSessionTopic === `${s.id}::${topic.name}::5`;
                        const isAllPending = isPending && activeSessionTopic === `${s.id}::${topic.name}::all`;

                        return (
                          <div
                            key={topic.name}
                            className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 rounded-xl border border-border/60 bg-surface p-3 transition hover:border-border hover:shadow-xs"
                          >
                            <div className="min-w-0">
                              <div className="flex items-center gap-2">
                                <span className="font-semibold text-sm text-text">
                                  {topic.name}
                                </span>
                              </div>
                              <div className="flex items-center gap-2 text-xs text-muted mt-0.5">
                                <span className={hasTopicQuestions ? "font-medium text-text" : "text-muted"}>
                                  {topic.filteredQuestionsCount}{" "}
                                  {topic.filteredQuestionsCount === 1 ? "questão" : "questões"}
                                  {!isAllBancasSelected && " filtradas"}
                                </span>
                                {hasTopicActivity && (
                                  <>
                                    <span>•</span>
                                    <span className="text-ok font-medium">
                                      {topic.userCorrect}/{topic.userAnswered} acertos ({topic.userAccuracy}%)
                                    </span>
                                  </>
                                )}
                              </div>
                            </div>

                            <div className="flex items-center gap-2 shrink-0 self-end sm:self-auto">
                              <Button
                                size="sm"
                                variant="secondary"
                                onClick={() => handleStartPractice(s.id, topic.name, 5)}
                                disabled={isPending || !hasTopicQuestions}
                                className="text-xs h-7 px-2.5"
                              >
                                {is5Pending ? "Iniciando..." : "Treinar 5"}
                              </Button>
                              <Button
                                size="sm"
                                variant="primary"
                                onClick={() => handleStartPractice(s.id, topic.name)}
                                disabled={isPending || !hasTopicQuestions}
                                className="text-xs h-7 px-2.5"
                              >
                                {isAllPending ? "Iniciando..." : "Treinar Todas"}
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
