import type { Metadata } from "next";
import { Badge, Card, PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { SIMULADOS_ENABLED, checkSimuladoReadiness, getUserSimulados, type SupportedSimuladoContest, type SimuladoReadiness } from "@/lib/data/simulados";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { FeatureLockedView } from "@/components/feature-locked-view";
import { SimuladosView } from "@/components/simulados-view";

export const metadata: Metadata = {
  title: "Simulados Oficiais — Missão Mentoria",
  description:
    "Realize simulados que reproduzem com fidelidade estrita a distribuição de questões, tempo oficial e regras de corte dos editais do CBMPE e PMPE.",
};

export default async function SimuladosPage() {
  const user = await requireUser();

  if (!SIMULADOS_ENABLED) {
    return (
      <div className="space-y-8">
        <PageHeader
          eyebrow="Em breve"
          title="Simulados Oficiais"
          description="Esta funcionalidade está temporariamente indisponível enquanto concluímos os ajustes finais."
        />
        <Card className="mx-auto max-w-2xl space-y-3 p-8 text-center sm:p-10">
          <Badge tone="warn" className="mx-auto">Em breve</Badge>
          <h2 className="font-display text-2xl font-bold uppercase">Estamos preparando os simulados</h2>
          <p className="text-sm leading-relaxed text-muted">
            Por enquanto, não é possível iniciar, continuar ou consultar resultados de simulados. As demais áreas da plataforma continuam disponíveis.
          </p>
        </Card>
      </div>
    );
  }

  const canAccess = await canUserAccessCoreFeatures(user.role, user.id);

  if (!canAccess) {
    return (
      <FeatureLockedView
        moduleName="Simulados Oficiais"
        description="A Central de Simulados dos Editais Oficiais está passando por validação final de cronometragem e calibração dos critérios eliminatórios de corte por bloco. A realização de simulados oficiais será liberada automaticamente junto com a ativação geral da plataforma."
      />
    );
  }

  const [
    cbmpeOficialReadiness,
    cbmpeCfoaReadiness,
    cbmpeSoldadoReadiness,
    pmpeOficialReadiness,
    pmpeSoldadoReadiness,
    pcpeAgenteReadiness,
    history,
  ] = await Promise.all([
    checkSimuladoReadiness("CBMPE_OFICIAL"),
    checkSimuladoReadiness("CBMPE_CFOA"),
    checkSimuladoReadiness("CBMPE_SOLDADO"),
    checkSimuladoReadiness("PMPE_OFICIAL"),
    checkSimuladoReadiness("PMPE_SOLDADO"),
    checkSimuladoReadiness("PCPE_AGENTE"),
    getUserSimulados(user.id),
  ]);

  const readinessMap: Record<SupportedSimuladoContest, SimuladoReadiness> = {
    CBMPE_OFICIAL: cbmpeOficialReadiness,
    CBMPE_CFOA: cbmpeCfoaReadiness,
    CBMPE_SOLDADO: cbmpeSoldadoReadiness,
    PMPE_OFICIAL: pmpeOficialReadiness,
    PMPE_SOLDADO: pmpeSoldadoReadiness,
    PCPE_AGENTE: pcpeAgenteReadiness,
  };

  return (
    <div className="space-y-8">
      {/* Cabeçalho */}
      <PageHeader
        eyebrow="Condições Reais de Prova"
        title="Simulados Oficiais"
        description="Treine sob a pressão do cronômetro oficial com a distribuição exata de matérias e critérios eliminatórios de corte por bloco do CBMPE e PMPE."
        info="O simulado não revela o gabarito durante a realização e salva suas respostas continuamente no servidor. Todas as tentativas alimentam automaticamente suas estatísticas no painel de desempenho."
      />

      {/* Conteúdo Interativo */}
      <SimuladosView
        readinessMap={readinessMap}
        history={history}
      />
    </div>
  );
}
