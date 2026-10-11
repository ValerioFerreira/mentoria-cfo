"use client";

import { useState, useTransition } from "react";
import {
  Send,
  Users,
  Clock,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  Loader2,
  Mail,
  ShieldCheck,
  ShieldAlert,
  Lock,
  Unlock,
  Power,
} from "lucide-react";
import { Badge, Button, Card, SectionTitle } from "@/components/ui";
import {
  releasePlansAndNotifyAll,
  togglePlatformRelease,
  type ReleaseResult,
} from "@/lib/admin/liberacao-actions";

interface UserRow {
  id: string;
  name: string | null;
  email: string;
  role: string;
  createdAt: string;
  planStatus: string;
}

interface LiberacaoViewProps {
  totalUsers: number;
  pendingPlansCount: number;
  activePlansCount: number;
  initialIsReleased: boolean;
  users: UserRow[];
}

export function LiberacaoView({
  totalUsers,
  pendingPlansCount,
  activePlansCount,
  initialIsReleased,
  users,
}: LiberacaoViewProps) {
  const [isPending, startTransition] = useTransition();
  const [isReleased, setIsReleased] = useState(initialIsReleased);
  const [showConfirmModal, setShowConfirmModal] = useState(false);
  const [showToggleModal, setShowToggleModal] = useState(false);
  const [result, setResult] = useState<ReleaseResult | null>(null);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);

  // Executa liberação geral completa (ativa planos, libera plataforma e dispara e-mails)
  const handleExecuteRelease = () => {
    setShowConfirmModal(false);
    startTransition(async () => {
      try {
        const res = await releasePlansAndNotifyAll();
        setResult(res);
        setIsReleased(true);
      } catch (err) {
        console.error("Erro ao liberar planos:", err);
        setResult({
          success: false,
          message: err instanceof Error ? err.message : "Erro desconhecido ao executar liberação.",
          plansActivated: 0,
          totalUsers,
          emailsSent: 0,
          errors: 1,
          isPlatformReleased: isReleased,
        });
      }
    });
  };

  // Alterna o status da liberação geral (com ou sem disparo de e-mails)
  const handleToggleRelease = (targetStatus: boolean) => {
    setShowToggleModal(false);
    startTransition(async () => {
      try {
        const res = await togglePlatformRelease(targetStatus);
        setIsReleased(res.isReleased);
        setStatusMessage(res.message);
      } catch (err) {
        setStatusMessage(err instanceof Error ? err.message : "Erro ao alterar status da plataforma.");
      }
    });
  };

  return (
    <div className="space-y-8">
      {/* Painel de Status Geral da Plataforma */}
      <Card
        className={`p-6 sm:p-8 space-y-6 border shadow-md transition ${
          isReleased
            ? "border-emerald-500/40 bg-gradient-to-r from-emerald-500/10 via-surface to-surface"
            : "border-amber-500/40 bg-gradient-to-r from-amber-500/10 via-surface to-surface"
        }`}
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div className="flex items-center gap-4">
            <div
              className={`grid h-14 w-14 place-items-center rounded-2xl shadow-sm ${
                isReleased
                  ? "bg-emerald-500 text-white"
                  : "bg-amber-500/20 text-amber-500"
              }`}
            >
              {isReleased ? <Unlock className="h-7 w-7" /> : <Lock className="h-7 w-7" />}
            </div>

            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold uppercase tracking-wider text-muted">
                  Controle de Acesso da Plataforma
                </span>
                <Badge tone={isReleased ? "ok" : "warn"} className="text-xs font-bold py-0.5 px-2.5">
                  {isReleased ? "SISTEMA LIBERADO" : "SISTEMA BLOQUEADO (MODO REVISÃO)"}
                </Badge>
              </div>
              <h2 className="font-display text-2xl font-bold uppercase text-text">
                {isReleased
                  ? "Plataforma 100% Liberada para Todos os Alunos"
                  : "Funcionalidades Restritas Apenas para Administrador"}
              </h2>
              <p className="text-xs text-muted max-w-xl leading-relaxed">
                {isReleased
                  ? "Planejamento, Banco de Questões e Simulados estão abertos e acessíveis para todos os usuários cadastrados."
                  : "Usuários comuns visualizam o aviso de elaboração. Planejamento, Questões e Simulados estão disponíveis exclusivamente para usuários com papel ADMIN."}
              </p>
            </div>
          </div>

          {/* Botões de Ação de Liberação Geral */}
          <div className="flex flex-wrap sm:flex-col gap-2.5 w-full sm:w-auto shrink-0">
            {!isReleased ? (
              <Button
                size="lg"
                variant="primary"
                onClick={() => setShowConfirmModal(true)}
                disabled={isPending}
                className="w-full sm:w-auto bg-gold text-on-gold hover:opacity-95 shadow-md flex items-center justify-center gap-2 font-bold px-6"
              >
                {isPending ? (
                  <Loader2 className="h-5 w-5 animate-spin" />
                ) : (
                  <Power className="h-5 w-5" />
                )}
                <span>{isPending ? "Processando..." : "Liberação Geral do Sistema"}</span>
              </Button>
            ) : (
              <Button
                size="sm"
                variant="secondary"
                onClick={() => setShowToggleModal(true)}
                disabled={isPending}
                className="w-full sm:w-auto text-amber-600 hover:text-amber-700 hover:bg-amber-500/10 border-amber-500/30 flex items-center justify-center gap-2"
              >
                <Lock className="h-4 w-4" />
                <span>Bloquear Novamente (Modo Revisão)</span>
              </Button>
            )}

            <Button
              size="sm"
              variant={isReleased ? "primary" : "secondary"}
              onClick={() => setShowConfirmModal(true)}
              disabled={isPending}
              className="w-full sm:w-auto flex items-center justify-center gap-2"
            >
              <Mail className="h-4 w-4" />
              <span>Notificar Todos por E-mail</span>
            </Button>
          </div>
        </div>
      </Card>

      {/* Mensagem de Status Rápido */}
      {statusMessage && (
        <Card className="p-4 border border-border bg-surface-2/60 text-xs text-text font-medium flex items-center justify-between">
          <span>{statusMessage}</span>
          <button
            onClick={() => setStatusMessage(null)}
            className="text-muted hover:text-text cursor-pointer ml-2"
          >
            Fechar
          </button>
        </Card>
      )}

      {/* Cards de Métricas */}
      <div className="grid gap-4 sm:grid-cols-3">
        <Card className="p-5 flex items-center gap-4">
          <div className="grid h-12 w-12 place-items-center rounded-2xl bg-primary/10 text-primary">
            <Users className="h-6 w-6" />
          </div>
          <div>
            <p className="text-xs uppercase font-bold tracking-wider text-muted">Usuários Cadastrados</p>
            <p className="font-display text-2xl font-bold text-text">{totalUsers}</p>
          </div>
        </Card>

        <Card className="p-5 flex items-center gap-4 border-amber-500/30">
          <div className="grid h-12 w-12 place-items-center rounded-2xl bg-amber-500/10 text-amber-500">
            <Clock className="h-6 w-6" />
          </div>
          <div>
            <p className="text-xs uppercase font-bold tracking-wider text-muted">Planos em Análise</p>
            <p className="font-display text-2xl font-bold text-amber-500">{pendingPlansCount}</p>
          </div>
        </Card>

        <Card className="p-5 flex items-center gap-4 border-emerald-500/30">
          <div className="grid h-12 w-12 place-items-center rounded-2xl bg-emerald-500/10 text-emerald-500">
            <ShieldCheck className="h-6 w-6" />
          </div>
          <div>
            <p className="text-xs uppercase font-bold tracking-wider text-muted">Planos Já Ativos</p>
            <p className="font-display text-2xl font-bold text-emerald-500">{activePlansCount}</p>
          </div>
        </Card>
      </div>

      {/* Resultado da Execução */}
      {result && (
        <Card
          className={`p-6 border ${
            result.success ? "border-emerald-500/40 bg-emerald-500/10" : "border-danger/40 bg-danger/10"
          } space-y-2 animate-in fade-in`}
        >
          <div className="flex items-center gap-2">
            {result.success ? (
              <CheckCircle2 className="h-5 w-5 text-emerald-600" />
            ) : (
              <AlertTriangle className="h-5 w-5 text-danger" />
            )}
            <h3 className="font-display text-lg font-bold uppercase text-text">
              {result.success ? "Operação Concluída com Sucesso" : "Falha na Execução"}
            </h3>
          </div>
          <p className="text-sm text-text leading-relaxed font-medium">{result.message}</p>
        </Card>
      )}

      {/* Modal de Confirmação de Liberação Geral + E-mail */}
      {showConfirmModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm animate-in fade-in">
          <Card className="w-full max-w-md p-6 space-y-5 shadow-2xl border-gold/40">
            <div className="flex items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-xl bg-gold/20 text-gold">
                <Power className="h-5 w-5" />
              </div>
              <h3 className="font-display text-lg font-bold uppercase text-text">
                Confirmar Liberação Geral
              </h3>
            </div>

            <p className="text-sm text-muted leading-relaxed">
              Esta ação irá ativar permanentemente o acesso a <strong>Planejamento, Banco de Questões e Simulados</strong> para todos os <strong>{totalUsers} usuário(s)</strong> cadastrados, ativando <strong>{pendingPlansCount} planejamento(s)</strong> e disparando a notificação por e-mail.
            </p>

            <div className="rounded-xl bg-surface-muted p-3 text-xs text-muted flex items-center gap-2">
              <Mail className="h-4 w-4 shrink-0 text-gold" />
              <span>O e-mail oficial contém o link de acesso direto à plataforma.</span>
            </div>

            <div className="flex justify-end gap-3 pt-2">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setShowConfirmModal(false)}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button
                variant="primary"
                size="sm"
                onClick={handleExecuteRelease}
                disabled={isPending}
                className="bg-gold text-on-gold hover:opacity-95 font-bold"
              >
                Confirmar Liberação Geral
              </Button>
            </div>
          </Card>
        </div>
      )}

      {/* Modal de Bloqueio (Modo Revisão) */}
      {showToggleModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm animate-in fade-in">
          <Card className="w-full max-w-md p-6 space-y-5 shadow-2xl border-amber-500/40">
            <div className="flex items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-xl bg-amber-500/20 text-amber-500">
                <Lock className="h-5 w-5" />
              </div>
              <h3 className="font-display text-lg font-bold uppercase text-text">
                Bloquear Acesso Geral
              </h3>
            </div>

            <p className="text-sm text-muted leading-relaxed">
              Você deseja retornar a plataforma ao <strong>Modo de Revisão</strong>? O acesso a Planejamento, Questões e Simulados ficará indisponível para alunos comuns, permanecendo liberado apenas para administradores.
            </p>

            <div className="flex justify-end gap-3 pt-2">
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setShowToggleModal(false)}
                disabled={isPending}
              >
                Cancelar
              </Button>
              <Button
                variant="primary"
                size="sm"
                onClick={() => handleToggleRelease(false)}
                disabled={isPending}
                className="bg-amber-600 text-white hover:bg-amber-700"
              >
                Bloquear Plataforma
              </Button>
            </div>
          </Card>
        </div>
      )}

      {/* Listagem de Usuários */}
      <section className="space-y-4" aria-labelledby="sec-alunos">
        <SectionTitle id="sec-alunos">
          Lista de Usuários Cadastrados ({users.length})
        </SectionTitle>

        <Card className="overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-surface-muted border-b border-border text-xs font-bold uppercase text-muted">
                <tr>
                  <th className="px-4 py-3">Nome / Usuário</th>
                  <th className="px-4 py-3">E-mail</th>
                  <th className="px-4 py-3">Papel</th>
                  <th className="px-4 py-3">Status do Plano</th>
                  <th className="px-4 py-3">Data do Cadastro</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {users.map((u) => (
                  <tr key={u.id} className="hover:bg-surface-muted/50 transition-colors">
                    <td className="px-4 py-3 font-semibold text-text">
                      {u.name ?? "Sem nome informado"}
                    </td>
                    <td className="px-4 py-3 text-muted">{u.email}</td>
                    <td className="px-4 py-3">
                      <Badge tone={u.role === "ADMIN" ? "ok" : "neutral"}>
                        {u.role}
                      </Badge>
                    </td>
                    <td className="px-4 py-3">
                      {u.planStatus === "ACTIVE" ? (
                        <Badge tone="ok">ATIVO</Badge>
                      ) : u.planStatus === "PENDING_ANALYSIS" ? (
                        <Badge tone="warn">EM ANÁLISE</Badge>
                      ) : (
                        <Badge tone="neutral">SEM PLANO</Badge>
                      )}
                    </td>
                    <td className="px-4 py-3 text-xs text-muted">
                      {new Date(u.createdAt).toLocaleString("pt-BR")}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
      </section>
    </div>
  );
}
