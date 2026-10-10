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
} from "lucide-react";
import { Badge, Button, Card, SectionTitle } from "@/components/ui";
import { releasePlansAndNotifyAll, type ReleaseResult } from "@/lib/admin/liberacao-actions";

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
  users: UserRow[];
}

export function LiberacaoView({
  totalUsers,
  pendingPlansCount,
  activePlansCount,
  users,
}: LiberacaoViewProps) {
  const [isPending, startTransition] = useTransition();
  const [showConfirmModal, setShowConfirmModal] = useState(false);
  const [result, setResult] = useState<ReleaseResult | null>(null);

  const handleExecuteRelease = () => {
    setShowConfirmModal(false);
    startTransition(async () => {
      try {
        const res = await releasePlansAndNotifyAll();
        setResult(res);
      } catch (err) {
        console.error("Erro ao liberar planos:", err);
        setResult({
          success: false,
          message: err instanceof Error ? err.message : "Erro desconhecido ao executar liberação.",
          plansActivated: 0,
          totalUsers,
          emailsSent: 0,
          errors: 1,
        });
      }
    });
  };

  return (
    <div className="space-y-8">
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
              {result.success ? "Disparo Concluído com Sucesso" : "Falha na Execução"}
            </h3>
          </div>
          <p className="text-sm text-text leading-relaxed font-medium">{result.message}</p>
        </Card>
      )}

      {/* Painel Principal de Ação */}
      <Card className="p-6 sm:p-8 space-y-6 border border-gold/30 bg-surface">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="space-y-1.5 max-w-xl">
            <div className="flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-gold" />
              <h2 className="font-display text-xl font-bold uppercase text-text">
                Disparo Oficial de Conclusão dos Planejamentos
              </h2>
            </div>
            <p className="text-sm text-muted leading-relaxed">
              Ao acionar este botão, todos os planejamentos atualmente em análise serão ativados no sistema e um e-mail de aviso será enviado a todos os cadastrados, informando que a plataforma e os cronogramas estão prontos.
            </p>
          </div>

          <Button
            size="lg"
            variant="primary"
            onClick={() => setShowConfirmModal(true)}
            disabled={isPending}
            className="w-full sm:w-auto bg-gold text-on-gold hover:opacity-95 shadow-md flex items-center gap-2.5 shrink-0"
          >
            {isPending ? (
              <Loader2 className="h-5 w-5 animate-spin" />
            ) : (
              <Send className="h-5 w-5" />
            )}
            {isPending ? "Processando e Enviando..." : "Liberar Planos e Notificar Todos por E-mail"}
          </Button>
        </div>
      </Card>

      {/* Modal de Confirmação */}
      {showConfirmModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm animate-in fade-in">
          <Card className="w-full max-w-md p-6 space-y-5 shadow-2xl border-gold/40">
            <div className="flex items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-xl bg-gold/20 text-gold">
                <AlertTriangle className="h-5 w-5" />
              </div>
              <h3 className="font-display text-lg font-bold uppercase text-text">
                Confirmar Disparo Geral
              </h3>
            </div>

            <p className="text-sm text-muted leading-relaxed">
              Você está prestes a liberar <strong>{pendingPlansCount} planejamento(s)</strong> pendente(s) e enviar e-mails de notificação para todos os <strong>{totalUsers} usuário(s)</strong> cadastrados na plataforma.
            </p>

            <div className="rounded-xl bg-surface-muted p-3 text-xs text-muted flex items-center gap-2">
              <Mail className="h-4 w-4 shrink-0 text-gold" />
              <span>O e-mail contém o link de acesso direto ao planejamento do aluno.</span>
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
                className="bg-gold text-on-gold hover:opacity-95"
              >
                Confirmar e Enviar
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
