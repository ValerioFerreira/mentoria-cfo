"use client";

import {
  AlertCircle,
  Calendar,
  CheckCircle2,
  Clock,
  Eye,
  Loader2,
  Mail,
  ShieldCheck,
  Trash2,
  UserCheck,
  UserX,
} from "lucide-react";
import { useState, useTransition } from "react";
import { Alert, Badge, Button, Card, SectionTitle } from "@/components/ui";
import { approveRegistration, rejectRegistration, deleteWaitlistEntry, type AdminActionResult } from "@/lib/admin/cadastros-actions";

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
  user?: {
    id: string;
    mustChangePassword: boolean;
    accessExpiresAt: string | null;
  } | null;
}

const CONTEST_LABELS: Record<string, string> = {
  CBMPE_SOLDADO: "CBMPE Soldado",
  CBMPE_OFICIAL: "CBMPE 2º Tenente",
  PCPE_AGENTE: "PCPE Agente",
};

const PLAN_LABELS: Record<string, string> = {
  MONTHLY: "R$ 20/mês",
  UNTIL_EXAM: "R$ 75 até a prova",
};

export function CadastrosView({ entries }: { entries: WaitlistRow[] }) {
  const [activeTab, setActiveTab] = useState<"PENDING" | "APPROVED" | "REJECTED">("PENDING");
  const [selectedEntry, setSelectedEntry] = useState<WaitlistRow | null>(null);
  const [duration, setDuration] = useState<"30_DAYS" | "INDEFINITE">("30_DAYS");
  const [rejectEntry, setRejectEntry] = useState<WaitlistRow | null>(null);
  const [rejectReason, setRejectReason] = useState("");
  const [statusMessage, setStatusMessage] = useState<AdminActionResult | null>(null);
  const [isPending, startTransition] = useTransition();

  const pendingList = entries.filter((e) => e.status === "PENDING");
  const approvedList = entries.filter((e) => e.status === "APPROVED");
  const rejectedList = entries.filter((e) => e.status === "REJECTED");

  function handleApprove(e: WaitlistRow) {
    setStatusMessage(null);
    setSelectedEntry(e);
    // Sugere plano baseado no selecionado pelo usuário
    if (e.plan === "UNTIL_EXAM") {
      setDuration("INDEFINITE");
    } else {
      setDuration("30_DAYS");
    }
  }

  function confirmApproval() {
    if (!selectedEntry) return;
    startTransition(async () => {
      const res = await approveRegistration(selectedEntry.id, duration);
      setStatusMessage(res);
      if (res.success) {
        setSelectedEntry(null);
      }
    });
  }

  function confirmRejection() {
    if (!rejectEntry) return;
    startTransition(async () => {
      const res = await rejectRegistration(rejectEntry.id, rejectReason);
      setStatusMessage(res);
      if (res.success) {
        setRejectEntry(null);
        setRejectReason("");
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
          <div className="space-y-1">
            <p className="font-semibold">{statusMessage.message}</p>
            {statusMessage.tempPassword && (
              <p className="text-xs text-muted">
                Senha temporária gerada:{" "}
                <strong className="font-mono text-primary text-sm bg-surface-2 px-2 py-0.5 rounded">
                  {statusMessage.tempPassword}
                </strong>{" "}
                (copie caso deseje encaminhar via WhatsApp)
              </p>
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

      {/* Modal de Aprovação */}
      {selectedEntry && (
        <Card className="border-2 border-primary/40 bg-surface-2 p-6 shadow-xl space-y-5">
          <div className="flex items-start justify-between">
            <div>
              <p className="eyebrow text-primary">Aprovar Cadastro</p>
              <h3 className="font-display text-2xl font-bold uppercase">{selectedEntry.name}</h3>
              <p className="text-sm text-muted">
                E-mail: <strong className="text-text">{selectedEntry.email}</strong> · Usuário: @{selectedEntry.username}
              </p>
            </div>
            <button
              onClick={() => setSelectedEntry(null)}
              className="text-xs font-semibold text-muted hover:text-text cursor-pointer"
            >
              Cancelar
            </button>
          </div>

          <div className="space-y-3">
            <label className="block text-sm font-bold text-text">
              Duração da Validade do Acesso:
            </label>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <label
                className={`flex items-center gap-3 rounded-xl border p-4 cursor-pointer transition ${
                  duration === "30_DAYS"
                    ? "border-primary bg-primary-soft text-text ring-1 ring-primary"
                    : "border-border bg-surface text-muted hover:border-border-strong"
                }`}
              >
                <input
                  type="radio"
                  name="duration"
                  value="30_DAYS"
                  checked={duration === "30_DAYS"}
                  onChange={() => setDuration("30_DAYS")}
                  className="accent-primary"
                />
                <div>
                  <p className="font-bold text-sm text-text">30 Dias</p>
                  <p className="text-xs text-muted">Acesso válido por 1 mês a partir de hoje.</p>
                </div>
              </label>

              <label
                className={`flex items-center gap-3 rounded-xl border p-4 cursor-pointer transition ${
                  duration === "INDEFINITE"
                    ? "border-primary bg-primary-soft text-text ring-1 ring-primary"
                    : "border-border bg-surface text-muted hover:border-border-strong"
                }`}
              >
                <input
                  type="radio"
                  name="duration"
                  value="INDEFINITE"
                  checked={duration === "INDEFINITE"}
                  onChange={() => setDuration("INDEFINITE")}
                  className="accent-primary"
                />
                <div>
                  <p className="font-bold text-sm text-text">Indeterminado</p>
                  <p className="text-xs text-muted">Válido até a homologação da prova do concurso.</p>
                </div>
              </label>
            </div>
          </div>

          <div className="rounded-xl bg-surface p-3 text-xs text-muted space-y-1 border border-border">
            <p>
              📧 Ao confirmar, um e-mail com a <strong>senha temporária</strong> e as instruções de primeiro acesso será enviado imediatamente para <strong className="text-text">{selectedEntry.email}</strong>.
            </p>
            <p>
              🔒 Ao efetuar o login, o aluno será orientado a escolher sua nova senha definitiva.
            </p>
          </div>

          <div className="flex justify-end gap-3 pt-2">
            <Button variant="secondary" onClick={() => setSelectedEntry(null)} disabled={isPending}>
              Cancelar
            </Button>
            <Button variant="primary" onClick={confirmApproval} disabled={isPending}>
              {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <UserCheck className="h-4 w-4" />}
              {isPending ? "Aprovando e enviando e-mail…" : "Aprovar e Enviar E-mail"}
            </Button>
          </div>
        </Card>
      )}

      {/* Modal de Rejeição */}
      {rejectEntry && (
        <Card className="border-2 border-danger/40 bg-surface-2 p-6 shadow-xl space-y-4">
          <div className="flex items-start justify-between">
            <div>
              <p className="eyebrow text-danger">Rejeitar Cadastro</p>
              <h3 className="font-display text-xl font-bold uppercase">{rejectEntry.name}</h3>
              <p className="text-xs text-muted">E-mail: {rejectEntry.email}</p>
            </div>
            <button
              onClick={() => setRejectEntry(null)}
              className="text-xs font-semibold text-muted hover:text-text cursor-pointer"
            >
              Cancelar
            </button>
          </div>

          <div className="space-y-1.5">
            <label className="block text-xs font-bold text-text">Motivo da Rejeição (opcional):</label>
            <input
              type="text"
              value={rejectReason}
              onChange={(e) => setRejectReason(e.target.value)}
              placeholder="Ex.: Comprovante de Pix não localizado"
              className="w-full rounded-xl border border-border bg-surface px-3 py-2 text-sm text-text outline-none focus:border-primary"
            />
          </div>

          <div className="flex justify-end gap-3 pt-2">
            <Button variant="secondary" onClick={() => setRejectEntry(null)} disabled={isPending}>
              Voltar
            </Button>
            <Button variant="danger" onClick={confirmRejection} disabled={isPending}>
              {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <UserX className="h-4 w-4" />}
              Confirmar Rejeição
            </Button>
          </div>
        </Card>
      )}

      {/* Listagem */}
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
                      {e.plan && <Badge tone="neutral">{PLAN_LABELS[e.plan] ?? e.plan}</Badge>}
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
                          onClick={() => handleApprove(e)}
                          disabled={isPending}
                        >
                          <Calendar className="h-3.5 w-3.5" />
                          Renovar / Alterar Validade
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
                          {e.accessDuration === "30_DAYS" ? "30 dias" : "Indeterminado"}
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
                          {e.user?.mustChangePassword ? "Aguardando 1º login (troca obrigatória)" : "Ativo com senha pessoal"}
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
    </div>
  );
}
