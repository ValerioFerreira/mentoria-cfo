"use client";

import { CheckCircle2, Eye, EyeOff, KeyRound, Loader2, Mail, Shield, User as UserIcon } from "lucide-react";
import { useActionState, useState, useTransition } from "react";
import { Alert, Badge, Button, Card, Field, SectionTitle, inputCls } from "@/components/ui";
import { CONTEST_SUBTITLES } from "@/lib/contests";
import { updateUserPassword, sendSelfPasswordReset, updateUserContest, type ProfilePasswordState } from "@/lib/profile/actions";

export interface UserProfileData {
  id: string;
  name: string | null;
  email: string;
  username: string | null;
  role: string;
  contest: string;
  createdAt: string;
  accessExpiresAt: string | null;
  mustChangePassword: boolean;
}

const CONTEST_OPTIONS = [
  { key: "CBMPE_OFICIAL", label: "OFICIAL - CBMPE" },
  { key: "CBMPE_SOLDADO", label: "PRAÇA - CBMPE" },
  { key: "PCPE_AGENTE", label: "AGENTE - PCPE" },
];

export function PerfilView({ user }: { user: UserProfileData }) {
  const [state, action, pending] = useActionState(updateUserPassword, undefined);
  const [showCurrent, setShowCurrent] = useState(false);
  const [showNew, setShowNew] = useState(false);
  const [resetMsg, setResetMsg] = useState<{ success: boolean; message: string } | null>(null);
  const [isResetPending, startResetTransition] = useTransition();

  const [selectedContest, setSelectedContest] = useState(user.contest || "CBMPE_OFICIAL");
  const [contestMsg, setContestMsg] = useState<{ success: boolean; message: string } | null>(null);
  const [isContestPending, startContestTransition] = useTransition();

  function handleContestChange(newKey: string) {
    if (newKey === selectedContest) return;
    startContestTransition(async () => {
      setSelectedContest(newKey);
      const res = await updateUserContest(newKey);
      setContestMsg(res);
    });
  }

  function handleSendReset() {
    startResetTransition(async () => {
      const res = await sendSelfPasswordReset();
      setResetMsg(res);
    });
  }

  // Cálculo de dias restantes
  let expirationInfo = "Acesso Indeterminado (até o concurso)";
  if (user.accessExpiresAt) {
    const expDate = new Date(user.accessExpiresAt);
    const now = new Date();
    const diffDays = Math.ceil((expDate.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));
    expirationInfo = `${expDate.toLocaleDateString("pt-BR")} (${diffDays > 0 ? `${diffDays} dias restantes` : "Expirado"})`;
  }

  return (
    <div className="space-y-8 max-w-3xl">
      {/* Dados do Perfil */}
      <Card className="p-6 space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-4 border-b border-border pb-5">
          <div className="flex items-center gap-4">
            <span className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-gold font-display text-2xl font-bold uppercase text-on-primary">
              {(user.name ?? user.email).charAt(0)}
            </span>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="font-display text-2xl font-bold uppercase text-text">{user.name ?? "Aluno"}</h2>
                <Badge tone={user.role === "ADMIN" ? "warn" : "ok"}>
                  {user.role === "ADMIN" ? "ADMINISTRADOR" : "ALUNO"}
                </Badge>
              </div>
              <p className="text-xs text-muted">
                Cadastrado em {new Date(user.createdAt).toLocaleDateString("pt-BR")}
              </p>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
          <div className="rounded-xl bg-surface-2 p-3.5 border border-border">
            <p className="text-xs text-muted uppercase font-semibold">E-mail Cadastrado</p>
            <p className="font-medium text-text mt-0.5">{user.email}</p>
          </div>

          <div className="rounded-xl bg-surface-2 p-3.5 border border-border">
            <p className="text-xs text-muted uppercase font-semibold">Nome de Usuário</p>
            <p className="font-medium text-text mt-0.5">@{user.username ?? "não definido"}</p>
          </div>

          <div className="rounded-xl bg-surface-2 p-3.5 border border-border sm:col-span-2">
            <p className="text-xs text-muted uppercase font-semibold">Validade do Acesso à Plataforma</p>
            <p className="font-bold text-text mt-0.5">{expirationInfo}</p>
          </div>

          <div className="rounded-xl bg-surface-2 p-3.5 border border-border sm:col-span-2">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <p className="text-xs text-muted uppercase font-semibold">Concurso Selecionado</p>
                <p className="font-bold text-text mt-0.5 text-base text-primary">
                  {CONTEST_SUBTITLES[selectedContest as keyof typeof CONTEST_SUBTITLES] ?? "OFICIAL - CBMPE"}
                </p>
                <p className="text-xs text-muted mt-0.5">
                  Define o subtítulo no menu lateral e o foco do seu plano de estudos.
                </p>
              </div>
              <div className="flex flex-wrap gap-2">
                {CONTEST_OPTIONS.map((opt) => (
                  <button
                    key={opt.key}
                    type="button"
                    disabled={isContestPending}
                    onClick={() => handleContestChange(opt.key)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition cursor-pointer ${
                      selectedContest === opt.key
                        ? "bg-primary text-on-primary shadow-sm"
                        : "bg-surface-3 text-muted hover:text-text hover:bg-surface-1 border border-border"
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>
            {contestMsg && (
              <p className={`mt-2 text-xs font-medium ${contestMsg.success ? "text-ok" : "text-danger"}`}>
                {contestMsg.message}
              </p>
            )}
          </div>
        </div>
      </Card>

      {/* Módulo de Senha e Segurança */}
      <section className="space-y-4" aria-labelledby="sec-seguranca">
        <SectionTitle id="sec-seguranca">Segurança e Senha</SectionTitle>

        <Card className="p-6 space-y-6">
          {state?.success && (
            <Alert tone="info">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="h-4 w-4 text-ok" />
                <span>{state.message}</span>
              </div>
            </Alert>
          )}

          {state?.message && !state.success && (
            <Alert tone="danger">{state.message}</Alert>
          )}

          <form action={action} className="space-y-4">
            <div className="space-y-1.5">
              <label htmlFor="currentPassword" className="block text-sm font-semibold">
                Senha Atual
              </label>
              <div className="relative">
                <input
                  id="currentPassword"
                  name="currentPassword"
                  type={showCurrent ? "text" : "password"}
                  required
                  placeholder="Digite sua senha atual"
                  className={`${inputCls} pr-11`}
                  aria-invalid={Boolean(state?.errors?.currentPassword)}
                />
                <button
                  type="button"
                  onClick={() => setShowCurrent((v) => !v)}
                  className="absolute right-1.5 top-1/2 flex h-8 w-8 -translate-y-1/2 cursor-pointer items-center justify-center rounded-lg text-muted transition hover:bg-surface-3/70 hover:text-text"
                >
                  {showCurrent ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
              {state?.errors?.currentPassword?.map((e) => (
                <span key={e} className="block text-xs font-medium text-primary">
                  {e}
                </span>
              ))}
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1.5">
                <label htmlFor="newPassword" className="block text-sm font-semibold">
                  Nova Senha
                </label>
                <div className="relative">
                  <input
                    id="newPassword"
                    name="newPassword"
                    type={showNew ? "text" : "password"}
                    required
                    minLength={8}
                    placeholder="Mínimo 8 caracteres"
                    className={`${inputCls} pr-11`}
                    aria-invalid={Boolean(state?.errors?.newPassword)}
                  />
                  <button
                    type="button"
                    onClick={() => setShowNew((v) => !v)}
                    className="absolute right-1.5 top-1/2 flex h-8 w-8 -translate-y-1/2 cursor-pointer items-center justify-center rounded-lg text-muted transition hover:bg-surface-3/70 hover:text-text"
                  >
                    {showNew ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  </button>
                </div>
                {state?.errors?.newPassword?.map((e) => (
                  <span key={e} className="block text-xs font-medium text-primary">
                    {e}
                  </span>
                ))}
              </div>

              <div className="space-y-1.5">
                <label htmlFor="confirmPassword" className="block text-sm font-semibold">
                  Confirmar Nova Senha
                </label>
                <input
                  id="confirmPassword"
                  name="confirmPassword"
                  type={showNew ? "text" : "password"}
                  required
                  minLength={8}
                  placeholder="Repita a nova senha"
                  className={inputCls}
                  aria-invalid={Boolean(state?.errors?.confirmPassword)}
                />
                {state?.errors?.confirmPassword?.map((e) => (
                  <span key={e} className="block text-xs font-medium text-primary">
                    {e}
                  </span>
                ))}
              </div>
            </div>

            <Button type="submit" size="md" disabled={pending}>
              {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <KeyRound className="h-4 w-4" />}
              {pending ? "Alterando senha…" : "Alterar Senha"}
            </Button>
          </form>

          {/* Recuperação de Senha dentro do perfil */}
          <div className="border-t border-dashed border-border-strong pt-5 space-y-3">
            <div>
              <p className="text-sm font-semibold text-text">Esqueceu sua senha atual?</p>
              <p className="text-xs text-muted">
                Caso você não lembre da senha atual, clique abaixo para receber uma nova senha temporária no e-mail <strong className="text-text">{user.email}</strong>.
              </p>
            </div>

            {resetMsg && (
              <Alert tone={resetMsg.success ? "info" : "danger"}>
                <p className="text-xs leading-relaxed">{resetMsg.message}</p>
              </Alert>
            )}

            <Button
              variant="secondary"
              size="sm"
              onClick={handleSendReset}
              disabled={isResetPending}
            >
              {isResetPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Mail className="h-4 w-4" />}
              {isResetPending ? "Enviando e-mail…" : "Enviar Senha Temporária por E-mail"}
            </Button>
          </div>
        </Card>
      </section>
    </div>
  );
}
