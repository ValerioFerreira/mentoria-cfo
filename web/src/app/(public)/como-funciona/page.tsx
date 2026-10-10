import { ArrowLeft, ArrowRight, BookOpen, Brain, CheckCircle2, ChevronRight, Flame, Sparkles, Target, Zap } from "lucide-react";
import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Badge, Card, LinkButton } from "@/components/ui";
import {
  ProgressSlider,
  SliderBtn,
  SliderBtnGroup,
  SliderContent,
  SliderNavControls,
  SliderWrapper,
} from "@/components/progressive-carousel";

export const metadata: Metadata = {
  title: "Como Funciona a Plataforma | MentorIA",
  description:
    "Entenda como a MentorIA estrutura seu planejamento de estudos inteligente e individualizado rumo à aprovação.",
};

const CAROUSEL_STEPS = [
  {
    sliderName: "passo-1",
    step: 1,
    title: "Montar meu plano",
    desc: "Na página \"Missão de Hoje\", selecione \"Montar meu plano\"",
    img: "/images/carousel/slide-1.png",
  },
  {
    sliderName: "passo-2",
    step: 2,
    title: "Disciplinas",
    desc: "Selecione as disciplinas que você vai querer estudar",
    img: "/images/carousel/slide-2.png",
  },
  {
    sliderName: "passo-3",
    step: 3,
    title: "Anamnese",
    desc: "Responda à anamnese, para que o modelo calibre seu planejamento individual",
    img: "/images/carousel/slide-3.png",
  },
  {
    sliderName: "passo-4",
    step: 4,
    title: "Ritmo Semanal",
    desc: "Defina qual será seu ritmo semanal de estudos",
    img: "/images/carousel/slide-4.png",
  },
  {
    sliderName: "passo-5",
    step: 5,
    title: "Geração do Plano",
    desc: "Confirme suas informações e gere seu planejamento",
    img: "/images/carousel/slide-5.png",
  },
  {
    sliderName: "passo-6",
    step: 6,
    title: "Rumo à Aprovação",
    desc: "Pronto! Seu planejamento já está montado. Vá até a página \"Missão de hoje\" e rumo à aprovação!",
    img: "/images/carousel/slide-6.png",
  },
];

const FEATURES = [
  {
    icon: Brain,
    title: "Calibração por Anamnese",
    badge: "Inteligência Individual",
    desc: "O algoritmo avalia sua experiência prévia em cada matéria e distribui o tempo priorizando seus pontos fracos e matérias de maior peso no edital.",
  },
  {
    icon: Flame,
    title: "Blocos de Estudo de 1h",
    badge: "Foco & Produtividade",
    desc: "Diretrizes cirúrgicas de estudo divididas em blocos de Teoria, Fixação, Revisão Espaçada e Cadernos de 25 Questões.",
  },
  {
    icon: Zap,
    title: "Bizus Direcionados com C/E",
    badge: "Resumo & Validação",
    desc: "Resumos estruturados no estilo apostila com pontos de atenção de prova, exemplos práticos e itens rápidos de Certo/Errado para fixação imediata.",
  },
  {
    icon: Target,
    title: "Questões no Padrão da Banca",
    badge: "Prática Real",
    desc: "Milhares de questões calibradas no perfil da AOCP com resolução completa comentada alternativa por alternativa.",
  },
];

export default function ComoFuncionaPage() {
  return (
    <div className="space-y-12 pt-2 sm:pt-6">
      {/* Topo / Voltar */}
      <div className="space-y-4">
        <Link
          href="/login"
          className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text"
        >
          <ArrowLeft className="h-4 w-4" aria-hidden />
          Voltar para o login
        </Link>
        <div className="max-w-3xl space-y-3">
          <p className="eyebrow">Guia Rápido · MentorIA</p>
          <h1 className="font-display text-4xl font-bold uppercase leading-[0.95] sm:text-6xl">
            Como funciona a <span className="text-primary">plataforma?</span>
          </h1>
          <p className="text-base leading-relaxed text-muted sm:text-lg">
            A MentorIA transforma o edital do seu concurso em uma esteira de estudos diária, calibrada
            para a sua realidade de tempo e seu nível de conhecimento.
          </p>
        </div>
      </div>

      {/* Carrossel Interativo Passo a Passo */}
      <section className="space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3 border-b border-border-strong/50 pb-3">
          <div className="space-y-1">
            <h2 className="font-display text-2xl font-bold uppercase tracking-tight sm:text-3xl">
              Passo a Passo: Como Começar
            </h2>
            <p className="text-sm text-muted">
              Veja como é simples calibrar e iniciar seu planejamento de estudos na plataforma.
            </p>
          </div>
          <Badge tone="gold">6 Passos Simples</Badge>
        </div>

        <div className="rounded-2xl border border-border bg-surface p-3 sm:p-6 shadow-card">
          <ProgressSlider
            duration={6500}
            activeSlider="passo-1"
            sliderValues={CAROUSEL_STEPS.map((s) => s.sliderName)}
            className="space-y-4"
          >
            <div className="flex items-center justify-between px-1">
              <span className="text-xs font-semibold uppercase tracking-wider text-muted">
                Visualização do Sistema
              </span>
              <SliderNavControls />
            </div>

            <SliderContent>
              {CAROUSEL_STEPS.map((step) => (
                <SliderWrapper key={step.sliderName} value={step.sliderName}>
                  <div className="relative overflow-hidden rounded-xl border border-border/80 bg-surface-2">
                    <div className="relative aspect-[16/9] w-full sm:aspect-[16/8] max-h-[500px]">
                      <Image
                        src={step.img}
                        alt={step.desc}
                        fill
                        priority={step.step === 1}
                        className="object-contain"
                        sizes="(max-width: 768px) 100vw, 1100px"
                      />
                    </div>
                  </div>
                </SliderWrapper>
              ))}
            </SliderContent>

            <SliderBtnGroup className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5 pt-2">
              {CAROUSEL_STEPS.map((step) => (
                <SliderBtn
                  key={step.sliderName}
                  value={step.sliderName}
                  className="rounded-xl border border-border p-3.5 text-left cursor-pointer overflow-hidden transition"
                  progressBarClass="bg-primary/25"
                >
                  <div className="flex items-center gap-2 mb-1.5">
                    <span className="grid h-6 w-6 place-items-center rounded-full bg-primary font-mono text-xs font-bold text-on-primary">
                      {step.step}
                    </span>
                    <span className="font-semibold text-xs uppercase tracking-wider text-muted">
                      {step.title}
                    </span>
                  </div>
                  <p className="text-xs font-medium text-text leading-snug line-clamp-2">
                    {step.desc}
                  </p>
                </SliderBtn>
              ))}
            </SliderBtnGroup>
          </ProgressSlider>
        </div>
      </section>

      {/* Funcionalidades em Destaque */}
      <section className="space-y-6">
        <div className="space-y-1 border-b border-border-strong/50 pb-3">
          <h2 className="font-display text-2xl font-bold uppercase tracking-tight sm:text-3xl">
            Tudo o que você precisa em um só lugar
          </h2>
          <p className="text-sm text-muted">
            Tecnologia e método desenhados para você estudar com clareza absoluta todos os dias.
          </p>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          {FEATURES.map((feat) => {
            const Icon = feat.icon;
            return (
              <Card key={feat.title} className="p-5 space-y-3 transition duration-200 hover:border-primary/40">
                <div className="flex items-center justify-between">
                  <div className="grid h-10 w-10 place-items-center rounded-xl bg-primary-soft text-primary">
                    <Icon className="h-5 w-5" />
                  </div>
                  <span className="rounded-full bg-surface-2 px-2.5 py-0.5 text-[11px] font-semibold text-muted border border-border">
                    {feat.badge}
                  </span>
                </div>
                <div className="space-y-1">
                  <h3 className="font-display text-lg font-bold">{feat.title}</h3>
                  <p className="text-xs leading-relaxed text-muted">{feat.desc}</p>
                </div>
              </Card>
            );
          })}
        </div>
      </section>

      {/* CTA Final */}
      <section className="rounded-2xl border border-primary/30 bg-ink p-8 text-on-ink shadow-lift space-y-6 text-center sm:text-left">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
          <div className="space-y-2 max-w-xl">
            <Badge tone="gold">Inicie sua preparação</Badge>
            <h3 className="font-display text-3xl font-bold uppercase leading-tight sm:text-4xl text-on-ink">
              Pronto para conquistar sua farda?
            </h3>
            <p className="text-sm leading-relaxed text-on-ink-muted">
              Garanta sua vaga na lista de espera ou entre agora mesmo com seu acesso.
            </p>
          </div>
          <div className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
            <LinkButton href="/concursos" variant="primary" size="lg" className="w-full sm:w-auto">
              Criar conta / Escolher concurso
              <ArrowRight className="h-4 w-4" />
            </LinkButton>
            <LinkButton href="/login" variant="onInk" size="lg" className="w-full sm:w-auto">
              Já tenho acesso
            </LinkButton>
          </div>
        </div>
      </section>
    </div>
  );
}
