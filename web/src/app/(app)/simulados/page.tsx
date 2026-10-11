import type { Metadata } from "next";
import { PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { checkSimuladoReadiness, getUserSimulados } from "@/lib/data/simulados";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { FeatureLockedView } from "@/components/feature-locked-view";
import { SimuladosView } from "@/components/simulados-view";

export const metadata: Metadata = {
  title: "Simulados Oficiais — Missão CBMPE 2026",
  description:
    "Realize simulados que reproduzem com fidelidade estrita a distribuição de questões, tempo oficial e regras de corte do edital.",
};

export default async function SimuladosPage() {
  const user = await requireUser();
  const canAccess = await canUserAccessCoreFeatures(user.role);

  if (!canAccess) {
    return (
      <FeatureLockedView
        moduleName="Simulados Oficiais CBMPE"
        description="A Central de Simulados do Edital Unificado está passando por validação final de cronometragem e calibração dos critérios eliminatórios de corte por bloco. A realização de simulados oficiais será liberada automaticamente junto com a ativação geral da plataforma."
      />
    );
  }

  const [oficialReadiness, soldadoReadiness, history] = await Promise.all([
    checkSimuladoReadiness("CBMPE_OFICIAL"),
    checkSimuladoReadiness("CBMPE_SOLDADO"),
    getUserSimulados(user.id),
  ]);

  return (
    <div className="space-y-8">
      {/* Cabeçalho */}
      <PageHeader
        eyebrow="Condições Reais de Prova"
        title="Simulados Oficiais"
        description="Treine sob a pressão do cronômetro oficial com a distribuição exata de matérias e critérios eliminatórios de corte por bloco do CBMPE 2026."
        info="O simulado não revela o gabarito durante a realização e salva suas respostas continuamente no servidor. Todas as tentativas alimentam automaticamente suas estatísticas no painel de desempenho."
      />

      {/* Conteúdo Interativo */}
      <SimuladosView
        oficialReadiness={oficialReadiness}
        soldadoReadiness={soldadoReadiness}
        history={history}
      />
    </div>
  );
}
