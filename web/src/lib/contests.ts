import type { Contest } from "@/generated/prisma/client";

export interface ContestInfo {
  /** parte da URL: /lista-de-espera/<slug> */
  slug: string;
  key: Contest;
  org: "CBMPE" | "PCPE";
  /** nome do cargo, sem a corporação */
  role: string;
  /** "Praça", "Oficial"… */
  category: string;
  /** imagem de fundo do card (em /public) */
  image: string;
  /** posição do recorte da imagem no card */
  imagePosition: string;
  /** false: o planejador ainda está em desenvolvimento; a pessoa entra na lista de espera pagando */
  available: boolean;
}

export const CONTESTS: ContestInfo[] = [
  { slug: "cbmpe-soldado", key: "CBMPE_SOLDADO", org: "CBMPE", role: "Soldado", category: "Praça", image: "/images/CBMPE.webp", imagePosition: "center 30%", available: true },
  { slug: "cbmpe-oficial", key: "CBMPE_OFICIAL", org: "CBMPE", role: "2º Tenente", category: "Oficial", image: "/images/CBMPE.webp", imagePosition: "center 70%", available: true },
  { slug: "pcpe-agente", key: "PCPE_AGENTE", org: "PCPE", role: "Agente de Polícia", category: "", image: "/images/PCPE.webp", imagePosition: "center", available: false },
];

export const CONTEST_SUBTITLES: Record<Contest, string> = {
  CBMPE_OFICIAL: "OFICIAL - CBMPE",
  CBMPE_SOLDADO: "PRAÇA - CBMPE",
  PCPE_AGENTE: "AGENTE - PCPE",
};

export function contestBySlug(slug: string): ContestInfo | undefined {
  return CONTESTS.find((c) => c.slug === slug);
}

export function contestTitle(c: ContestInfo): string {
  return `${c.org} · Cargo: ${c.role}${c.category ? ` (${c.category})` : ""}`;
}
