"use client";

import {
  AlertCircle,
  Calendar,
  Check,
  CheckCircle2,
  Clock,
  Copy,
  KeyRound,
  Loader2,
  Mail,
  Sparkles,
  Trash2,
  UserCheck,
  UserX,
  X,
} from "lucide-react";
import Link from "next/link";
import { useEffect, useState, useTransition } from "react";
import { Alert, Badge, Button, Card, SectionTitle } from "@/components/ui";
import {
  approveRegistration,
  rejectRegistration,
  deleteWaitlistEntry,
  approvePlan,
  updateAccessValidity,
  resendTemporaryPassword,
  type AdminActionResult,
  type ValidityOption,
} from "@/lib/admin/cadastros-actions";

export interface PendingPlanRow {
  id: string;
  userId: string;
  userName: string;
  userEmail: string;
  createdAt: string;
  examDate: string;
  version: number;
  hoursPerWeek: number | null;
  subjectCount: number;
}

export interface WaitlistRow {
  id: string;
  name: string;
  email: string;
  username: string;
  contest: string;
  plan: string | null;
  status: string;
  createdAt: string;
  paidAt: string | null;
  approvedAt: string | null;
  rejectedAt: string | null;
  accessDuration: string | null;
  rejectionReason: string | null;
  /** contratação (obrigação financeira) ligada à inscrição */
  contract: {
    id: string;
    finalCents: number;
    paidCents: number;
    status: string;
    statusLabel: string;
    couponCode: string | null;
    examDateKnown: boolean;
  } | null;
  user?: {
    id: string;
    mustChangePassword: boolean;
    accessExpiresAt: string | null;
  } | null;
}

const CONTEST_LABELS: Record<string, string> = {
  CBMPE_SOLDADO: "CBMPE Soldado",
  CBMPE_OFICIAL: "CBMPE 2º Tenente",
  PMPE_SOLDADO: "PMPE Soldado",
  PMPE_OFICIAL: "PMPE 2º Tenente",
  PCPE_AGENTE: "PCPE Agente",
  CBMPE_COMBO: "CBMPE Combo (2º Tenente + Soldado)",
  PMPE_COMBO: "PMPE Combo (2º Tenente + Soldado)",
};

// planos das inscrições anteriores ao acesso até a prova (histórico)
const PLAN_LABELS: Record<string, string> = {
  MONTHLY: "R$ 30/mês (plano antigo)",
  UNTIL_EXAM: "R$ 50 permanente (plano antigo)",
};

const brl = (cents: number) => `R$ ${(cents / 100).toFixed(2).replace(".", ",")}`;
type Duration = "UNTIL_EXAM" | "30_DAYS" | "INDEFINITE";

export function CadastrosView({
  entries,
  pendingPlans = [],
}: {
  entries: WaitlistRow[];
  pendingPlans?: PendingPlanRow[];
}) {
  const [activeTab, setActiveTab] = useState<"PENDING" | "APPROVED" | "REJECTED" | "PLANS">(
    pendingPlans.length > 0 ? "PLANS" : "PENDING"
  );

  // Modal de Aprovação (novos cadastros)
  const [selectedEntry, setSelectedEntry] = useState<WaitlistRow | null>(null);
  const [duration, setDuration] = useState<Duration>("UNTIL_EXAM");
  const [override, setOverride] = useState(false);
  const [justification, setJustification] = useState("");

  // Modal de Rejeição
  const [rejectEntry, setRejectEntry] = useState<WaitlistRow | null>(null);
  const [rejectReason, setRejectReason] = useState("");

  // Modal de Alteração de Validade / Renovação
  const [validityEntry, setValidityEntry] = useState<WaitlistRow | null>(null);
  const [validityOption, setValidityOption] = useState<ValidityOption>("EXTEND_30_DAYS");
  const [customDate, setCustomDate] = useState("");

  // Modal de Reenvio de E-mail com Nova Senha
  const [resendEntry, setResendEntry] = useState<WaitlistRow | null>(null);

  // Feedback geral, erro interno de modais e clipboard
  const [statusMessage, setStatusMessage] = useState<AdminActionResult | null>(null);
  const [modalError, setModalError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const [isPending, startTransition] = useTransition();

  const pendingList = entries.filter((e) => e.status === "PENDING");
  const approvedList = entries.filter((e) => e.status === "APPROVED");
  const rejectedList = entries.filter((e) => e.status === "REJECTED");

  // Trava a rolagem do fundo quando qualquer modal estiver aberto
  useEffect(() => {
    const hasModal = Boolean(selectedEntry || rejectEntry || validityEntry || resendEntry);
    if (hasModal) {
      const orig = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      return () => {
        document.body.style.overflow = orig;
      };
    }
  }, [selectedEntry, rejectEntry, validityEntry, resendEntry]);

  // Fecha modais com a tecla Escape
  useEffect(() => {
    const hasModal = Boolean(selectedEntry || rejectEntry || validityEntry || resendEntry);
    if (!hasModal) return;

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && !isPending) {
        setSelectedEntry(null);
        setRejectEntry(null);
        setValidityEntry(null);
        setResendEntry(null);
        setModalError(null);
      }
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [selectedEntry, rejectEntry, validityEntry, resendEntry, isPending]);

  function handleApprove(e: WaitlistRow) {
    setStatusMessage(null);
    setModalError(null);
    setSelectedEntry(e);
    setOverride(false);
    setJustification("");
    if (e.contract) {
      setDuration("UNTIL_EXAM");
    } else if (e.plan === "MONTHLY") {
      setDuration("30_DAYS");
    } else {
      setDuration("INDEFINITE");
    }
  }

  function confirmApproval() {
    if (!selectedEntry) return;
    setModalError(null);

    // Validação preventiva no cliente para liberação com saldo pendente
    if (
      duration === "UNTIL_EXAM" &&
      selectedEntry.contract &&
      selectedEntry.contract.paidCents < selectedEntry.contract.finalCents
    ) {
      if (!override) {
        setModalError(
          "Há saldo pendente nesta contratação. Para liberar mesmo assim, marque a opção 'Liberar mesmo com saldo pendente' e forneça a justificativa."
        );
        return;
      }
      if (justification.trim().length < 10) {
        setModalError("A justificativa para liberação com saldo pendente deve ter no mínimo 10 caracteres.");
        return;
      }
    }

    startTransition(async () => {
      const res = await approveRegistration(selectedEntry.id, duration, { override, justification });
      if (res.success) {
        setStatusMessage(res);
        setSelectedEntry(null);
        setModalError(null);
      } else {
        setModalError(res.message);
      }
    });
  }

  function confirmRejection() {
    if (!rejectEntry) return;
    setModalError(null);
    startTransition(async () => {
      const res = await rejectRegistration(rejectEntry.id, rejectReason);
      if (res.success) {
        setStatusMessage(res);
        setRejectEntry(null);
        setRejectReason("");
        setModalError(null);
      } else {
        setModalError(res.message);
      }
    });
  }

  function handleOpenValidity(e: WaitlistRow) {
    setStatusMessage(null);
    setModalError(null);
    setValidityEntry(e);
    setValidityOption("EXTEND_30_DAYS");
    const initialDate = e.user?.accessExpiresAt
      ? new Date(e.user.accessExpiresAt).toISOString().slice(0, 10)
      : new Date(Date.now() + 30 * 86400000).toISOString().slice(0, 10);
    setCustomDate(initialDate);
  }

  function confirmValidityUpdate() {
    if (!validityEntry) return;
    setModalError(null);
    startTransition(async () => {
      const res = await updateAccessValidity(validityEntry.id, validityOption, customDate);
      if (res.success) {
        setStatusMessage(res);
        setValidityEntry(null);
        setModalError(null);
      } else {
        setModalError(res.message);
      }
    });
  }

  function handleOpenResend(e: WaitlistRow) {
    setStatusMessage(null);
    setModalError(null);
    setResendEntry(e);
  }

  function confirmResendCredentials() {
    if (!resendEntry) return;
    setModalError(null);
    startTransition(async () => {
      const res = await resendTemporaryPassword(resendEntry.id);
      if (res.success) {
        setStatusMessage(res);
        setResendEntry(null);
        setModalError(null);
      } else {
        setModalError(res.message);
      }
    });
  }

  function handleDelete(id: string) {
    if (!confirm("Tem certeza que deseja excluir este registro da lista?")) return;
    startTransition(async () => {
      const res = await deleteWaitlistEntry(id);
      setStatusMessage(res);
    });
  }

  const currentList =
    activeTab === "PENDING"
      ? pendingList
      : activeTab === "APPROVED"
        ? approvedList
        : rejectedList;

  return (
    <div className="space-y-6">
      {statusMessage && (
        <Alert tone={statusMessage.success ? "info" : "danger"}>
          <div className="space-y-2">
            <p className="font-semibold">{statusMessage.message}</p>
            {statusMessage.tempPassword && (
              <div className="flex flex-wrap items-center gap-2 pt-1 text-xs">
                <span className="text-muted">Senha temporária:</span>
                <code className="font-mono text-primary text-sm bg-surface-2 px-2.5 py-1 rounded-md border border-border font-bold">
                  {statusMessage.tempPassword}
                </code>
                <button
                  type="button"
                  onClick={() => {
                    navigator.clipboard.writeText(statusMessage.tempPassword!);
                    setCopied(true);
                    setTimeout(() => setCopied(false), 2000);
                  }}
                  className="rounded-md border border-border bg-surface px-2.5 py-1 text-xs font-semibold text-text hover:bg-surface-3 transition flex items-center gap-1 cursor-pointer"
                >
                  {copied ? <Check className="h-3 w-3 text-ok" /> : <Copy className="h-3 w-3" />}
                  {copied ? "Copiado!" : "Copiar Senha"}
                </button>
              </div>
            )}
          </div>
        </Alert>
      )}

      {/* Tabs */}
      <nav className="flex flex-wrap gap-2" aria-label="Abas de cadastros">
        <button
          type="button"
          onClick={() => setActiveTab("PENDING")}
          className={`flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition cursor-pointer ${
            activeTab === "PENDING"
              ? "border-primary bg-primary-soft text-primary"
              : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"
          }`}
        >
          <Clock className="h-4 w-4" />
          Aguardando Aprovação
          <span className="rounded-full bg-surface-3 px-2 py-0.5 text-xs tabular font-bold text-text">
            {pendingList.length}
          </span>
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("APPROVED")}
          className={`flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition cursor-pointer ${
            activeTab === "APPROVED"
              ? "border-ok bg-ok-soft text-ok"
              : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"
          }`}
        >
          <CheckCircle2 className="h-4 w-4" />
          Aprovados (Alunos Ativos)
          <span className="rounded-full bg-surface-3 px-2 py-0.5 text-xs tabular font-bold text-text">
            {approvedList.length}
          </span>
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("PLANS")}
          className={`flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition cursor-pointer ${
            activeTab === "PLANS"
              ? "border-gold bg-gold/15 text-gold font-bold ring-1 ring-gold"
              : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"
          }`}
        >
          <Sparkles className="h-4 w-4 text-gold" />
          Planos para Liberação
          <span className="rounded-full bg-gold/20 px-2 py-0.5 text-xs tabular font-bold text-gold">
            {pendingPlans.length}
          </span>
        </button>

        <button
          type="button"
          onClick={() => setActiveTab("REJECTED")}
          className={`flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition cursor-pointer ${
            activeTab === "REJECTED"
              ? "border-danger bg-danger-soft text-danger"
              : "border-border bg-surface text-muted hover:border-border-strong hover:text-text"
          }`}
        >
          <UserX className="h-4 w-4" />
          Rejeitados
          <span className="rounded-full bg-surface-3 px-2 py-0.5 text-xs tabular font-bold text-text">
            {rejectedList.length}
          </span>
        </button>
      </nav>

      {/* Modal de Aprovação Inicial */}
      {selectedEntry && (
        <div
          className="fixed inset-0 z-[70] flex items-center justify-center overflow-y-auto p-3 sm:p-6 bg-ink/80 backdrop-blur-sm animate-in fade-in duration-200"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-aprovar-titulo"
          onClick={(e) => {
            if (e.target === e.currentTarget && !isPending) {
              setSelectedEntry(null);
              setModalError(null);
            }
          }}
        >
          <div className="relative w-full max-w-lg max-h-[calc(100vh-1.5rem)] sm:max-h-[calc(100vh-3rem)] rounded-2xl border border-primary/30 bg-surface text-text shadow-2xl overflow-hidden flex flex-col my-auto">
            {/* Header fixo */}
            <div className="shrink-0 flex items-center justify-between border-b border-border/70 px-6 py-4 bg-surface-2/40">
              <div>
                <p className="eyebrow text-primary text-[11px] uppercase tracking-wider font-bold">
                  Aprovar Cadastro
                </p>
                <h3 id="modal-aprovar-titulo" className="font-display text-lg font-bold uppercase text-text">
                  {selectedEntry.name}
                </h3>
                <p className="text-xs text-muted">
                  E-mail: <strong className="text-text">{selectedEntry.email}</strong> · Usuário: @{selectedEntry.username}
                </p>
              </div>
              <button
                type="button"
                onClick={() => {
                  setSelectedEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
                aria-label="Fechar"
                className="flex h-8 w-8 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            {/* Corpo rolável */}
            <div className="flex-1 overflow-y-auto min-h-0 p-6 space-y-4">
              {modalError && (
                <Alert tone="danger">
                  <p className="text-xs font-semibold">{modalError}</p>
                </Alert>
              )}

              <div className="space-y-2">
                <label className="block text-xs font-bold uppercase tracking-wider text-muted">
                  Duração Inicial do Acesso:
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {(
                    [
                      selectedEntry.contract && {
                        key: "UNTIL_EXAM" as const,
                        title: "Até a data da prova",
                        desc: selectedEntry.contract.examDateKnown ? "Acesso ilimitado até a prova do concurso." : "Data da prova pendente: cadastre-a em Financeiro.",
                        disabled: !selectedEntry.contract.examDateKnown,
                      },
                      selectedEntry.plan === "MONTHLY" && { key: "30_DAYS" as const, title: "30 Dias", desc: "Plano mensal antigo.", disabled: false },
                      { key: "INDEFINITE" as const, title: "Indeterminado", desc: "Sem prazo (cadastros antigos).", disabled: false },
                    ].filter(Boolean) as { key: Duration; title: string; desc: string; disabled: boolean }[]
                  ).map((o) => (
                    <label
                      key={o.key}
                      className={`flex items-center gap-3 rounded-xl border p-3.5 transition ${o.disabled ? "cursor-not-allowed opacity-60" : "cursor-pointer"} ${
                        duration === o.key
                          ? "border-primary bg-primary/10 text-text ring-1 ring-primary"
                          : "border-border bg-surface text-muted hover:border-border-strong"
                      }`}
                    >
                      <input
                        type="radio"
                        name="duration"
                        value={o.key}
                        checked={duration === o.key}
                        disabled={o.disabled}
                        onChange={() => {
                          setDuration(o.key);
                          setModalError(null);
                        }}
                        className="accent-primary cursor-pointer"
                      />
                      <div>
                        <p className="font-bold text-xs text-text">{o.title}</p>
                        <p className="text-[11px] text-muted">{o.desc}</p>
                      </div>
                    </label>
                  ))}
                </div>
              </div>

              {selectedEntry.contract ? (
                <div className="rounded-xl border border-border p-3.5 text-xs space-y-2.5 bg-surface-2/30">
                  <p className="text-muted leading-relaxed">
                    Contratação: <strong className="text-text">{brl(selectedEntry.contract.finalCents)}</strong> · recebido{" "}
                    <strong className="text-text">{brl(selectedEntry.contract.paidCents)}</strong> · {selectedEntry.contract.statusLabel}
                    {selectedEntry.contract.couponCode ? ` · cupom ${selectedEntry.contract.couponCode}` : ""}{" "}
                    <Link href={`/admin/financeiro/${selectedEntry.contract.id}`} className="font-semibold text-primary underline hover:text-primary-hover">
                      registrar pagamento
                    </Link>
                  </p>
                  {duration === "UNTIL_EXAM" && selectedEntry.contract.paidCents < selectedEntry.contract.finalCents && (
                    <div className="space-y-2.5 rounded-xl border border-warn/40 bg-warn-soft/60 p-3 text-xs text-warn">
                      <div className="flex items-start gap-2">
                        <AlertCircle className="h-4 w-4 shrink-0 mt-0.5 text-warn" />
                        <div className="space-y-1">
                          <p className="font-bold">Pagamento pendente de confirmação</p>
                          <p className="text-[11px] leading-relaxed opacity-90 text-text">
                            Para liberar o acesso antes da quitação financeira, é obrigatório marcar a opção abaixo e fornecer uma justificativa formal (mínimo de 10 caracteres).
                          </p>
                        </div>
                      </div>
                      <label className="flex items-center gap-2 font-semibold text-text cursor-pointer pt-1">
                        <input
                          type="checkbox"
                          checked={override}
                          onChange={(ev) => {
                            setOverride(ev.target.checked);
                            setModalError(null);
                          }}
                          className="h-4 w-4 rounded accent-primary cursor-pointer"
                        />
                        Liberar mesmo com saldo pendente
                      </label>
                      {override && (
                        <div className="space-y-1 pt-1">
                          <input
                            value={justification}
                            onChange={(ev) => {
                              setJustification(ev.target.value);
                              setModalError(null);
                            }}
                            placeholder="Justificativa (mínimo de 10 caracteres, ex: comprovante enviado no WhatsApp)"
                            className="w-full rounded-lg border border-border bg-surface px-3 py-2 text-xs text-text placeholder:text-muted focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
                            autoFocus
                          />
                          <p className="text-[10px] text-muted">
                            {justification.trim().length < 10
                              ? `Faltam ${10 - justification.trim().length} caractere(s) para o mínimo exigido.`
                              : "✓ Justificativa válida para liberação."}
                          </p>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ) : (
                <p className="text-xs text-muted">Inscrição anterior ao acesso até a prova (sem contratação registrada).</p>
              )}

              <div className="rounded-xl bg-surface-2 p-3 text-xs text-muted space-y-1 border border-border">
                <p>
                  📧 Um e-mail com a <strong>senha temporária</strong> e link de acesso será enviado para <strong className="text-text">{selectedEntry.email}</strong>.
                </p>
                <p>
                  🔒 No primeiro login, o aluno será solicitado a cadastrar sua senha pessoal definitiva.
                </p>
              </div>
            </div>

            {/* Footer fixo */}
            <div className="shrink-0 flex items-center justify-end gap-2 border-t border-border/70 px-6 py-4 bg-surface-2/40">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => {
                  setSelectedEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button variant="primary" size="sm" onClick={confirmApproval} disabled={isPending}>
                {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <UserCheck className="h-4 w-4" />}
                {isPending ? "Aprovando…" : "Aprovar e Enviar E-mail"}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Modal de Rejeição */}
      {rejectEntry && (
        <div
          className="fixed inset-0 z-[70] flex items-center justify-center overflow-y-auto p-3 sm:p-6 bg-ink/80 backdrop-blur-sm animate-in fade-in duration-200"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-rejeitar-titulo"
          onClick={(e) => {
            if (e.target === e.currentTarget && !isPending) {
              setRejectEntry(null);
              setModalError(null);
            }
          }}
        >
          <div className="relative w-full max-w-lg max-h-[calc(100vh-1.5rem)] sm:max-h-[calc(100vh-3rem)] rounded-2xl border border-danger/30 bg-surface text-text shadow-2xl overflow-hidden flex flex-col my-auto">
            {/* Header fixo */}
            <div className="shrink-0 flex items-center justify-between border-b border-border/70 px-6 py-4 bg-surface-2/40">
              <div>
                <p className="eyebrow text-danger text-[11px] uppercase tracking-wider font-bold">
                  Rejeitar Cadastro
                </p>
                <h3 id="modal-rejeitar-titulo" className="font-display text-lg font-bold uppercase text-text">
                  {rejectEntry.name}
                </h3>
                <p className="text-xs text-muted">E-mail: {rejectEntry.email}</p>
              </div>
              <button
                type="button"
                onClick={() => {
                  setRejectEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
                aria-label="Fechar"
                className="flex h-8 w-8 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            {/* Corpo rolável */}
            <div className="flex-1 overflow-y-auto min-h-0 p-6 space-y-3">
              {modalError && (
                <Alert tone="danger">
                  <p className="text-xs font-semibold">{modalError}</p>
                </Alert>
              )}
              <label className="block text-xs font-bold text-text">Motivo da Rejeição (opcional):</label>
              <input
                type="text"
                value={rejectReason}
                onChange={(e) => {
                  setRejectReason(e.target.value);
                  setModalError(null);
                }}
                placeholder="Ex.: Comprovante de Pix não identificado"
                className="w-full rounded-xl border border-border bg-surface px-3.5 py-2 text-sm text-text outline-none focus:border-primary"
              />
            </div>

            {/* Footer fixo */}
            <div className="shrink-0 flex items-center justify-end gap-2 border-t border-border/70 px-6 py-4 bg-surface-2/40">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => {
                  setRejectEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button variant="danger" size="sm" onClick={confirmRejection} disabled={isPending}>
                {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <UserX className="h-4 w-4" />}
                Confirmar Rejeição
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Modal de Renovar / Alterar Validade */}
      {validityEntry && (
        <div
          className="fixed inset-0 z-[70] flex items-center justify-center overflow-y-auto p-3 sm:p-6 bg-ink/80 backdrop-blur-sm animate-in fade-in duration-200"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-validade-titulo"
          onClick={(e) => {
            if (e.target === e.currentTarget && !isPending) {
              setValidityEntry(null);
              setModalError(null);
            }
          }}
        >
          <div className="relative w-full max-w-lg max-h-[calc(100vh-1.5rem)] sm:max-h-[calc(100vh-3rem)] rounded-2xl border border-border bg-surface text-text shadow-2xl overflow-hidden flex flex-col my-auto">
            {/* Header fixo */}
            <div className="shrink-0 flex items-center justify-between border-b border-border/70 px-6 py-4 bg-surface-2/40">
              <div className="flex items-center gap-2.5">
                <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <Calendar className="h-5 w-5" />
                </div>
                <div>
                  <h3 id="modal-validade-titulo" className="font-display text-lg font-bold uppercase tracking-wide text-text">
                    Renovar / Alterar Validade
                  </h3>
                  <p className="text-xs text-muted">
                    {validityEntry.name} · @{validityEntry.username}
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => {
                  setValidityEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
                aria-label="Fechar"
                className="flex h-8 w-8 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            {/* Corpo rolável */}
            <div className="flex-1 overflow-y-auto min-h-0 p-6 space-y-4">
              {modalError && (
                <Alert tone="danger">
                  <p className="text-xs font-semibold">{modalError}</p>
                </Alert>
              )}

              {/* Situação Atual */}
              <div className="rounded-xl border border-border bg-surface-2 p-3.5 text-xs space-y-1">
                <p className="font-semibold text-text">Situação Atual do Acesso:</p>
                <div className="text-muted flex flex-wrap gap-x-3 gap-y-1">
                  <span>
                    Tipo gravado:{" "}
                    <strong className="text-text">
                      {validityEntry.accessDuration === "INDEFINITE" ? "Indeterminado" : validityEntry.accessDuration === "UNTIL_EXAM" ? "Até a prova" : "30 dias"}
                    </strong>
                  </span>
                  <span>·</span>
                  <span>
                    {validityEntry.user?.accessExpiresAt ? (
                      <>
                        Expira em:{" "}
                        <strong className="text-text">
                          {new Date(validityEntry.user.accessExpiresAt).toLocaleDateString("pt-BR")}
                        </strong>
                      </>
                    ) : (
                      <strong className="text-ok">Sem data limite (permanente até a prova)</strong>
                    )}
                  </span>
                </div>
              </div>

              {/* Opções de Ajuste */}
              <div className="space-y-2">
                <label className="text-xs font-bold uppercase tracking-wider text-muted block">
                  Escolha o Novo Período de Validade:
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {[
                    { val: "EXTEND_30_DAYS", label: "+30 Dias", desc: "Soma 30 dias ao vencimento" },
                    { val: "EXTEND_60_DAYS", label: "+60 Dias", desc: "Soma 60 dias ao vencimento" },
                    { val: "EXTEND_90_DAYS", label: "+90 Dias", desc: "Soma 90 dias ao vencimento" },
                    { val: "INDEFINITE", label: "Indeterminado", desc: "Permanente até a homologação" },
                  ].map((opt) => (
                    <label
                      key={opt.val}
                      className={`flex items-start gap-3 rounded-xl border p-3 cursor-pointer transition ${
                        validityOption === opt.val
                          ? "border-primary bg-primary/10 text-text ring-1 ring-primary"
                          : "border-border bg-surface hover:bg-surface-2 text-muted"
                      }`}
                    >
                      <input
                        type="radio"
                        name="validityOption"
                        value={opt.val}
                        checked={validityOption === opt.val}
                        onChange={() => {
                          setValidityOption(opt.val as ValidityOption);
                          setModalError(null);
                        }}
                        className="mt-0.5 accent-primary"
                      />
                      <div>
                        <p className="font-bold text-xs text-text">{opt.label}</p>
                        <p className="text-[11px] text-muted">{opt.desc}</p>
                      </div>
                    </label>
                  ))}
                </div>

                {/* Opção de Data Personalizada */}
                <label
                  className={`flex items-start gap-3 rounded-xl border p-3 cursor-pointer transition mt-2 ${
                    validityOption === "CUSTOM_DATE"
                      ? "border-primary bg-primary/10 text-text ring-1 ring-primary"
                      : "border-border bg-surface hover:bg-surface-2 text-muted"
                  }`}
                >
                  <input
                    type="radio"
                    name="validityOption"
                    value="CUSTOM_DATE"
                    checked={validityOption === "CUSTOM_DATE"}
                    onChange={() => {
                      setValidityOption("CUSTOM_DATE");
                      setModalError(null);
                    }}
                    className="mt-0.5 accent-primary"
                  />
                  <div className="flex-1 space-y-1.5">
                    <p className="font-bold text-xs text-text">Data Específica de Expiração</p>
                    {validityOption === "CUSTOM_DATE" && (
                      <input
                        type="date"
                        value={customDate}
                        onChange={(e) => {
                          setCustomDate(e.target.value);
                          setModalError(null);
                        }}
                        className="w-full rounded-lg border border-border bg-surface px-3 py-1.5 text-xs text-text outline-none focus:border-primary"
                      />
                    )}
                  </div>
                </label>
              </div>

              <p className="text-[11px] text-muted">
                💡 Esta ação atualiza a data de acesso do aluno sem resetar nem interferir na senha já cadastrada por ele.
              </p>
            </div>

            {/* Footer fixo */}
            <div className="shrink-0 flex items-center justify-end gap-2 border-t border-border/70 px-6 py-4 bg-surface-2/40">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => {
                  setValidityEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button
                variant="primary"
                size="sm"
                onClick={confirmValidityUpdate}
                disabled={isPending || (validityOption === "CUSTOM_DATE" && !customDate)}
              >
                {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Calendar className="h-4 w-4" />}
                {isPending ? "Atualizando…" : "Salvar Nova Validade"}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Modal de Reenviar E-mail com Nova Senha */}
      {resendEntry && (
        <div
          className="fixed inset-0 z-[70] flex items-center justify-center overflow-y-auto p-3 sm:p-6 bg-ink/80 backdrop-blur-sm animate-in fade-in duration-200"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-reenvio-titulo"
          onClick={(e) => {
            if (e.target === e.currentTarget && !isPending) {
              setResendEntry(null);
              setModalError(null);
            }
          }}
        >
          <div className="relative w-full max-w-lg max-h-[calc(100vh-1.5rem)] sm:max-h-[calc(100vh-3rem)] rounded-2xl border border-border bg-surface text-text shadow-2xl overflow-hidden flex flex-col my-auto">
            {/* Header fixo */}
            <div className="shrink-0 flex items-center justify-between border-b border-border/70 px-6 py-4 bg-surface-2/40">
              <div className="flex items-center gap-2.5">
                <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <KeyRound className="h-5 w-5" />
                </div>
                <div>
                  <h3 id="modal-reenvio-titulo" className="font-display text-lg font-bold uppercase tracking-wide text-text">
                    Reenviar Acesso com Nova Senha
                  </h3>
                  <p className="text-xs text-muted">
                    {resendEntry.name} · {resendEntry.email}
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => {
                  setResendEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
                aria-label="Fechar"
                className="flex h-8 w-8 items-center justify-center rounded-lg text-muted hover:bg-surface-3 hover:text-text transition cursor-pointer"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            {/* Corpo rolável */}
            <div className="flex-1 overflow-y-auto min-h-0 p-6 space-y-4">
              {modalError && (
                <Alert tone="danger">
                  <p className="text-xs font-semibold">{modalError}</p>
                </Alert>
              )}

              <div className="rounded-xl border border-amber-500/30 bg-amber-500/10 p-3.5 text-xs text-amber-200 space-y-1.5">
                <p className="font-bold flex items-center gap-1.5">
                  <AlertCircle className="h-4 w-4 shrink-0 text-amber-400" />
                  Atenção ao Redefinir a Senha:
                </p>
                <p className="text-[12px] leading-relaxed">
                  Uma <strong>nova senha temporária</strong> será gerada e a senha atual do aluno será invalidada. Um e-mail com a nova senha e instruções de acesso será enviado para <strong className="text-text">{resendEntry.email}</strong>.
                </p>
                <p className="text-[11px] text-muted">
                  Ao realizar o login com esta credencial temporária, o aluno será orientado a escolher uma nova senha definitiva.
                </p>
              </div>
            </div>

            {/* Footer fixo */}
            <div className="shrink-0 flex items-center justify-end gap-2 border-t border-border/70 px-6 py-4 bg-surface-2/40">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => {
                  setResendEntry(null);
                  setModalError(null);
                }}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button
                variant="primary"
                size="sm"
                onClick={confirmResendCredentials}
                disabled={isPending}
              >
                {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Mail className="h-4 w-4" />}
                {isPending ? "Gerando e Enviando…" : "Confirmar e Enviar E-mail"}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Listagem */}
      {activeTab === "PLANS" ? (
        <section className="space-y-3" aria-labelledby="sec-planos">
          <SectionTitle id="sec-planos">
            Planejamentos em Análise / Aguardando Liberação ({pendingPlans.length})
          </SectionTitle>

          {pendingPlans.length === 0 ? (
            <Card className="p-8 text-center text-sm text-muted">
              Nenhum planejamento aguardando liberação no momento. Todos os alunos com questionário respondido já possuem plano ativo.
            </Card>
          ) : (
            <div className="space-y-3">
              {pendingPlans.map((p) => (
                <Card key={p.id} className="p-5 space-y-4 border border-gold/30">
                  <div className="flex flex-wrap items-start justify-between gap-3">
                    <div className="space-y-1">
                      <div className="flex flex-wrap items-center gap-2">
                        <h4 className="font-display text-xl font-bold uppercase text-text">{p.userName}</h4>
                        <Badge tone="warn">EM ANÁLISE (24H)</Badge>
                        <Badge tone="neutral">{p.subjectCount} disciplinas</Badge>
                        {p.hoursPerWeek && <Badge tone="neutral">{p.hoursPerWeek}h/semana</Badge>}
                        <Badge tone="neutral">Prova: {p.examDate}</Badge>
                      </div>

                      <p className="text-xs text-muted flex flex-wrap items-center gap-x-3 gap-y-1">
                        <span>E-mail: <strong className="text-text">{p.userEmail}</strong></span>
                        <span>·</span>
                        <span>Solicitado em: {new Date(p.createdAt).toLocaleString("pt-BR")}</span>
                        <span>·</span>
                        <span>Versão do plano: #{p.version}</span>
                      </p>
                    </div>

                    <div className="flex items-center gap-2">
                      <Button
                        size="sm"
                        variant="primary"
                        onClick={() => {
                          startTransition(async () => {
                            const res = await approvePlan(p.id);
                            setStatusMessage(res);
                          });
                        }}
                        disabled={isPending}
                        className="bg-gold text-on-gold hover:opacity-90"
                      >
                        {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Sparkles className="h-4 w-4" />}
                        Liberar Planejamento
                      </Button>
                    </div>
                  </div>
                </Card>
              ))}
            </div>
          )}
        </section>
      ) : (
        <section className="space-y-3" aria-labelledby="sec-cadastros">
          <SectionTitle id="sec-cadastros">
            {activeTab === "PENDING"
              ? `Cadastros Pendentes (${pendingList.length})`
              : activeTab === "APPROVED"
                ? `Cadastros Aprovados (${approvedList.length})`
                : `Cadastros Rejeitados (${rejectedList.length})`}
          </SectionTitle>

          {currentList.length === 0 ? (
            <Card className="p-8 text-center text-sm text-muted">
              Nenhum cadastro encontrado nesta seção.
            </Card>
          ) : (
            <div className="space-y-3">
              {currentList.map((e) => (
                <Card key={e.id} className="p-5 space-y-4">
                  <div className="flex flex-wrap items-start justify-between gap-3">
                    <div className="space-y-1">
                      <div className="flex flex-wrap items-center gap-2">
                        <h4 className="font-display text-xl font-bold uppercase text-text">{e.name}</h4>
                        <Badge tone={e.paidAt ? "ok" : "warn"}>
                          {e.paidAt ? "PIX CONFERIDO" : "AGUARDA PIX"}
                        </Badge>
                        <Badge>{CONTEST_LABELS[e.contest] ?? e.contest}</Badge>
                        {e.contract ? (
                          <Link href={`/admin/financeiro/${e.contract.id}`} title="Abrir no Financeiro">
                            <Badge tone={e.contract.paidCents >= e.contract.finalCents ? "ok" : "warn"}>
                              {brl(e.contract.finalCents)} · {e.contract.statusLabel}
                              {e.contract.couponCode ? ` · ${e.contract.couponCode}` : ""}
                            </Badge>
                          </Link>
                        ) : (
                          e.plan && <Badge tone="neutral">{PLAN_LABELS[e.plan] ?? e.plan}</Badge>
                        )}
                      </div>

                      <p className="text-xs text-muted flex flex-wrap items-center gap-x-3 gap-y-1">
                        <span>E-mail: <strong className="text-text">{e.email}</strong></span>
                        <span>·</span>
                        <span>Usuário: <strong className="text-text">@{e.username}</strong></span>
                        <span>·</span>
                        <span>Cadastrado em: {new Date(e.createdAt).toLocaleString("pt-BR")}</span>
                      </p>
                    </div>

                    {/* Ações */}
                    <div className="flex flex-wrap items-center gap-2">
                      {e.status === "PENDING" && (
                        <>
                          <Button
                            size="sm"
                            variant="primary"
                            onClick={() => handleApprove(e)}
                            disabled={isPending}
                          >
                            <UserCheck className="h-4 w-4" />
                            Aprovar
                          </Button>
                          <Button
                            size="sm"
                            variant="secondary"
                            onClick={() => {
                              setRejectEntry(e);
                              setRejectReason("");
                            }}
                            disabled={isPending}
                          >
                            <UserX className="h-4 w-4 text-danger" />
                            Rejeitar
                          </Button>
                        </>
                      )}

                      {e.status === "APPROVED" && (
                        <div className="flex flex-wrap items-center gap-2">
                          <Button
                            size="sm"
                            variant="secondary"
                            onClick={() => handleOpenValidity(e)}
                            disabled={isPending}
                          >
                            <Calendar className="h-3.5 w-3.5 text-primary" />
                            Renovar / Alterar Validade
                          </Button>

                          <Button
                            size="sm"
                            variant="secondary"
                            onClick={() => handleOpenResend(e)}
                            disabled={isPending}
                          >
                            <Mail className="h-3.5 w-3.5 text-primary" />
                            Reenviar E-mail / Nova Senha
                          </Button>
                        </div>
                      )}

                      {e.status === "REJECTED" && (
                        <Button
                          size="sm"
                          variant="secondary"
                          onClick={() => handleApprove(e)}
                          disabled={isPending}
                        >
                          <UserCheck className="h-3.5 w-3.5 text-ok" />
                          Reavaliar e Aprovar
                        </Button>
                      )}

                      <button
                        type="button"
                        onClick={() => handleDelete(e.id)}
                        disabled={isPending}
                        aria-label="Excluir cadastro"
                        className="p-2 text-muted hover:text-danger rounded-lg transition cursor-pointer"
                      >
                        <Trash2 className="h-4 w-4" />
                      </button>
                    </div>
                  </div>

                  {/* Detalhes para Aprovados */}
                  {e.status === "APPROVED" && (
                    <div className="rounded-xl bg-surface-2 p-3 text-xs text-muted flex flex-wrap items-center justify-between gap-2 border border-border">
                      <div className="flex flex-wrap items-center gap-x-4 gap-y-1">
                        <span>
                          Validade:{" "}
                          <strong className="text-text">
                            {e.accessDuration === "INDEFINITE" ? "Indeterminado" : e.accessDuration === "UNTIL_EXAM" ? "Até a prova" : "30 dias"}
                          </strong>
                        </span>
                        {e.user?.accessExpiresAt && (
                          <span>
                            Expira em:{" "}
                            <strong className="text-text">
                              {new Date(e.user.accessExpiresAt).toLocaleDateString("pt-BR")}
                            </strong>
                          </span>
                        )}
                        <span>
                          Status da Senha:{" "}
                          <strong className={e.user?.mustChangePassword ? "text-warn" : "text-ok"}>
                            {e.user?.mustChangePassword
                              ? "Aguardando 1º login (troca obrigatória)"
                              : "Ativo com senha pessoal"}
                          </strong>
                        </span>
                      </div>
                    </div>
                  )}

                  {/* Detalhes para Rejeitados */}
                  {e.status === "REJECTED" && e.rejectionReason && (
                    <div className="rounded-xl bg-danger-soft p-3 text-xs text-danger flex items-center gap-2">
                      <AlertCircle className="h-4 w-4 shrink-0" />
                      <span>Motivo da recusa: {e.rejectionReason}</span>
                    </div>
                  )}
                </Card>
              ))}
            </div>
          )}
        </section>
      )}
    </div>
  );
}
