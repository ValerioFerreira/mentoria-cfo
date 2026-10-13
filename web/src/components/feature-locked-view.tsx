import { ArrowLeft, Clock, Lock, Sparkles, Trophy } from "lucide-react";
import Link from "next/link";
import { Badge, Card, LinkButton, PageHeader } from "@/components/ui";

interface Props {
  moduleName: string;
  description: string;
}

export function FeatureLockedView({ moduleName, description }: Props) {
  return (
    <div className="mx-auto max-w-2xl py-8 space-y-6">
      <Link
        href="/"
        className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text"
      >
        <ArrowLeft className="h-4 w-4" aria-hidden />
        Voltar para a página inicial
      </Link>

      <Card tone="ink" className="p-8 sm:p-10 space-y-6 shadow-card text-center sm:text-left relative overflow-hidden">
        <div className="flex flex-col sm:flex-row items-center sm:items-start gap-5">
          <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-gold/20 text-gold shadow-sm">
            <Clock className="h-7 w-7" />
          </div>

          <div className="space-y-2 flex-1">
            <div className="inline-flex items-center gap-1.5">
              <Badge tone="warn" className="text-xs font-bold py-0.5 px-2.5">
                Em Preparação Final
              </Badge>
            </div>
            <h1 className="font-display text-2xl sm:text-3xl font-bold uppercase text-on-ink">
              {moduleName}
            </h1>
            <p className="text-sm text-on-ink-muted leading-relaxed">
              {description}
            </p>
          </div>
        </div>

        <div className="rounded-xl border border-white/10 bg-white/5 p-4 text-xs text-on-ink-muted leading-relaxed">
          <p className="font-semibold text-on-ink mb-1 flex items-center gap-1.5 justify-center sm:justify-start">
            <Sparkles className="h-4 w-4 text-gold" />
            <span>Liberação Controlada da Plataforma</span>
          </p>
          <p>
            Para garantir a máxima precisão técnica e metodológica das questões e cronogramas, este módulo está restrito temporariamente para revisão e será liberado automaticamente aos alunos cadastrados assim que concluído.
          </p>
        </div>

        <div className="pt-2 flex flex-wrap justify-center sm:justify-start gap-3">
          <LinkButton href="/" variant="primary" size="md">
            Ir para Início
          </LinkButton>
          <LinkButton href="/desempenho" variant="secondary" size="md">
            Ver Meu Desempenho
          </LinkButton>
        </div>
      </Card>
    </div>
  );
}
