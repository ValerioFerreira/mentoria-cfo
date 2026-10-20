import type { Metadata } from "next";
import { CheckCircle2, Crosshair, HelpCircle, ListChecks, Sparkles, Target, Trophy } from "lucide-react";
import { Badge, Card, Count, PageHeader, Ring, Stat } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { getQuestoesOverview } from "@/lib/data/questoes";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { FeatureLockedView } from "@/components/feature-locked-view";
import { QuestoesFilterList } from "@/components/questoes-filter-list";
import { getUserContest } from "@/lib/user-contest";
import { CONTEST_SUBTITLES, contestSubjectIds } from "@/lib/contests";

export const metadata: Metadata = {
  title: "Banco de Questões — Missão CBMPE 2026",
  description: "Resolva questões do edital unificado do CBMPE 2026 separadas por matéria e assunto.",
};

export default async function QuestoesPage() {
  const user = await requireUser();
  const canAccess = await canUserAccessCoreFeatures(user.role, user.id);

  if (!canAccess) {
    return (
      <FeatureLockedView
        moduleName="Banco de Questões"
        description="O acervo de questões das bancas AOCP e Instituto AOCP selecionadas exclusivamente para o Edital Unificado do CBMPE 2026 está em fase final de validação pedagógica e será liberado automaticamente junto com a ativação geral da plataforma."
      />
    );
  }

  const contest = await getUserContest(user.email);
  const overview = await getQuestoesOverview(user.id, contestSubjectIds(contest), contest);
  const { globalStats, subjects, availableBancas, bancaCounts } = overview;

  return (
    <div className="space-y-8">
      {/* Cabeçalho da Página */}
      <PageHeader
        eyebrow="Prática Livre e Treinamento"
        title="Banco de Questões"
        description={`Questões das disciplinas do edital ${CONTEST_SUBTITLES[contest]}. Escolha a banca, matéria e assunto para praticar à vontade e registrar seu progresso.`}
        info="Só aparecem as disciplinas do edital do seu concurso. Todas as questões resolvidas aqui têm seu desempenho gravado automaticamente em seu perfil e contabilizado em suas métricas gerais de evolução."
      />

      {/* Painel de Métricas do Aluno */}
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card tone="ink" className="p-5 flex items-center justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Acervo Total</p>
            <p className="font-display text-3xl font-bold text-on-ink mt-1">
              <Count value={globalStats.totalQuestions} />
            </p>
            <p className="text-xs text-on-ink-muted mt-0.5">Questões cadastradas no acervo</p>
          </div>
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/20 text-primary">
            <ListChecks className="h-6 w-6" />
          </div>
        </Card>

        <Card tone="ink" className="p-5 flex items-center justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Resolvidas por Você</p>
            <p className="font-display text-3xl font-bold text-on-ink mt-1">
              <Count value={globalStats.userAnswered} />
            </p>
            <p className="text-xs text-on-ink-muted mt-0.5">
              {globalStats.totalQuestions > 0
                ? `${Math.round((globalStats.userAnswered / globalStats.totalQuestions) * 100)}% do acervo coberto`
                : "Nenhuma ainda"}
            </p>
          </div>
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gold/20 text-gold">
            <Crosshair className="h-6 w-6" />
          </div>
        </Card>

        <Card tone="ink" className="p-5 flex items-center justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Taxa de Acerto Geral</p>
            <p className="font-display text-3xl font-bold text-on-ink mt-1">
              {globalStats.userAccuracy !== null ? `${globalStats.userAccuracy}%` : "—"}
            </p>
            <p className="text-xs text-on-ink-muted mt-0.5">
              {globalStats.userAnswered > 0
                ? `${globalStats.userCorrect} acertos em ${globalStats.userAnswered} questões`
                : "Faça questões para medir"}
            </p>
          </div>
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-ok/20 text-ok">
            <Trophy className="h-6 w-6" />
          </div>
        </Card>

        <Card tone="ink" className="p-5 flex items-center justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-on-ink-muted">Matérias Disponíveis</p>
            <p className="font-display text-3xl font-bold text-on-ink mt-1">
              <Count value={globalStats.subjectsCount} />
            </p>
            <p className="text-xs text-on-ink-muted mt-0.5">Disciplinas com questões</p>
          </div>
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-teoria/20 text-teoria">
            <Target className="h-6 w-6" />
          </div>
        </Card>
      </div>

      {/* Navegador e Filtros de Questões por Matéria e Assunto */}
      <QuestoesFilterList
        subjects={subjects}
        blockNames={overview.blockNames}
        availableBancas={availableBancas}
        bancaCounts={bancaCounts}
      />
    </div>
  );
}
