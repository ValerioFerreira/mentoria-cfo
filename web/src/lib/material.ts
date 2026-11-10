import "server-only";
import { readFileSync } from "node:fs";
import path from "node:path";
import { cookies } from "next/headers";
import type { MaterialChapter, MaterialChoice } from "@/lib/directive";

/**
 * Material próprio MentorIA: páginas de cada capítulo nos PDFs, lidas do índice gerado por pipeline/build_material.py
 * (content/material/index.json, espelhado em web/content/material/index.json). Cada trecho do edital é um capítulo.
 */
interface IndexChapter {
  numero: number;
  titulo: string;
  pagina: number | null;
  ate: number | null;
  mapa: number | null;
  revisao: number | null;
  questoes: { pagina: number; ate: number } | null;
}
interface IndexVolume {
  titulo: string;
  numero: number;
  disciplina: string;
  paginas: number;
  atualizadoEm?: string | null;
  capitulos: Record<string, IndexChapter>;
}

let cache: Map<string, MaterialChapter> | null = null;
const volumeMeta = new Map<string, { paginas: number; titulo: string }>();

function load(): Map<string, MaterialChapter> {
  if (cache) return cache;
  const map = new Map<string, MaterialChapter>();
  try {
    const raw = JSON.parse(readFileSync(path.join(process.cwd(), "content", "material", "index.json"), "utf8")) as {
      volumes: Record<string, IndexVolume>;
    };
    for (const [volumeId, v] of Object.entries(raw.volumes)) {
      volumeMeta.set(volumeId, { paginas: v.paginas, titulo: v.titulo });
      for (const [trecho, c] of Object.entries(v.capitulos)) {
        if (!c.pagina || !c.ate) continue;
        map.set(trecho, {
          trecho, volumeId, volumeNumber: v.numero, volumeTitle: v.titulo, subjectName: v.disciplina, chapter: c.numero, title: c.titulo,
          start: c.pagina, end: c.ate, mapPage: c.mapa, reviewPage: c.revisao, questions: c.questoes,
        });
      }
    }
  } catch {
    // sem índice (material ainda não gerado): as diretrizes ficam só no material-base
  }
  cache = map;
  return map;
}

/** Capítulo do material próprio que corresponde ao trecho (ou undefined, se o trecho ainda não tem capítulo publicado). */
export function chapterFor(segmentId: string): MaterialChapter | undefined {
  return load().get(segmentId);
}

/** Capítulos de todos os trechos de uma aula (a Fixação é por aula). */
export function chaptersForAula(aulaId: string): MaterialChapter[] {
  return [...load().values()].filter((c) => c.trecho.startsWith(aulaId + "/"));
}

/** Volumes conhecidos (para validar o caminho da rota do PDF). */
export function hasVolume(volumeId: string): boolean {
  for (const c of load().values()) if (c.volumeId === volumeId) return true;
  return false;
}

/** Capítulos de um volume, para achar o trecho de uma página. */
export function chaptersOfVolume(volumeId: string): MaterialChapter[] {
  return [...load().values()].filter((c) => c.volumeId === volumeId);
}

/** Total de páginas e título de um volume do material próprio (ou null se o volume não existir). */
export function volumeInfo(volumeId: string): { paginas: number; titulo: string } | null {
  load();
  return volumeMeta.get(volumeId) ?? null;
}

export const MATERIAL_COOKIE = "material";

/** Material preferido do aluno (cookie; padrão: o material próprio MentorIA). */
export async function getMaterialChoice(): Promise<MaterialChoice> {
  const v = (await cookies()).get(MATERIAL_COOKIE)?.value;
  return v === "base" ? "base" : "mentoria";
}
