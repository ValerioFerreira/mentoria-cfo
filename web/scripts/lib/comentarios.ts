// Leitura dos comentários versionados das questões: content/questoes/comentarios/<disciplina>/<lote>.json.
//
// Formato de cada arquivo (escrito pelos agentes; briefing em pipeline/briefs/questoes-comentarios.md):
//   { "lote": "<disciplina>/<nome>", "trecho": "<disc>/aNN/sNN", "autor": "...", "data": "AAAA-MM-DD",
//     "comentarios": [{ "id": "tec_123", "contentHash": "...", "gabarito": "B", "comentario": "...",
//                       "alternativas": { "A": "Errada: ...", ... }, "autor"?: "...", "data"?: "..." }],
//     "descartes": [{ "id": "tec_456", "motivo": "QUALIDADE: ..." }] }
// Certo/Errado: "alternativas" = {}. Validação de conteúdo: pipeline/questoes/validate_comentarios.py.
// Campo opcional "revisao": "pendente" no arquivo (comentários aproveitados da Fixação ainda não conferidos): não é publicado.
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

export const COMMENTS_DIR = resolve(__dirname, "..", "..", "..", "content", "questoes", "comentarios");

export interface CommentEntry {
  id: string;
  contentHash: string;
  gabarito: string;
  comentario: string;
  alternativas: Record<string, string>;
  autor: string;
  data: string;
  /** arquivo de origem (relativo a content/questoes/comentarios) */
  arquivo: string;
  /** arquivo com "revisao": "pendente" (comentários vindos da Fixação ainda não conferidos): o aplicador não publica */
  pendente: boolean;
}

export interface Discard {
  id: string;
  motivo: string;
  arquivo: string;
}

interface CommentFile {
  autor?: string;
  revisao?: string;
  data?: string;
  comentarios?: Partial<CommentEntry>[];
  descartes?: { id: string; motivo: string }[];
}

/** Lê todos os arquivos de comentários. O mesmo id em dois arquivos: vale o do arquivo mais recente na ordem do nome (e é avisado). */
export function loadComments(filter?: (arquivo: string) => boolean): { entries: Map<string, CommentEntry>; discards: Discard[]; problems: string[] } {
  const entries = new Map<string, CommentEntry>();
  const discards: Discard[] = [];
  const problems: string[] = [];
  if (!existsSync(COMMENTS_DIR)) return { entries, discards, problems };
  const dirs = readdirSync(COMMENTS_DIR, { withFileTypes: true }).filter((d) => d.isDirectory() && !d.name.startsWith("_") && d.name !== "amostras");
  for (const d of dirs.sort((a, b) => a.name.localeCompare(b.name))) {
    for (const f of readdirSync(join(COMMENTS_DIR, d.name)).filter((x) => x.endsWith(".json")).sort()) {
      const arquivo = `${d.name}/${f}`;
      if (filter && !filter(arquivo)) continue;
      let j: CommentFile;
      try {
        j = JSON.parse(readFileSync(join(COMMENTS_DIR, d.name, f), "utf8")) as CommentFile;
      } catch (e) {
        problems.push(`${arquivo}: JSON inválido (${(e as Error).message})`);
        continue;
      }
      for (const c of j.comentarios ?? []) {
        if (!c.id || !c.contentHash || !c.gabarito || !c.comentario || typeof c.alternativas !== "object" || c.alternativas === null) {
          problems.push(`${arquivo}: entrada incompleta (${c.id ?? "sem id"})`);
          continue;
        }
        if (entries.has(c.id)) problems.push(`${c.id}: comentado em ${entries.get(c.id)!.arquivo} e em ${arquivo} (vale o segundo)`);
        entries.set(c.id, {
          id: c.id, contentHash: c.contentHash, gabarito: c.gabarito, comentario: c.comentario.trim(),
          alternativas: Object.fromEntries(Object.entries(c.alternativas).map(([k, v]) => [k, String(v).trim()])),
          autor: c.autor ?? j.autor ?? "?", data: c.data ?? j.data ?? "?", arquivo, pendente: j.revisao === "pendente",
        });
      }
      for (const x of j.descartes ?? []) discards.push({ id: x.id, motivo: x.motivo, arquivo });
    }
  }
  return { entries, discards, problems };
}

export interface DbQuestion {
  id: string;
  contentHash: string | null;
  kind: "MULTIPLA_ESCOLHA" | "CERTO_ERRADO";
  explanation: string;
  options: { label: string; isCorrect: boolean; comment: string | null }[];
}

export type Verdict =
  | { status: "gravar"; optionComments: Record<string, string | null> }
  | { status: "igual" }
  | { status: "ausente" | "desatualizado" | "gabarito" | "alternativas"; detalhe: string };

/** Decide se o comentário pode ser gravado na questão do banco (texto, gabarito e letras conferem). Função pura. */
export function checkComment(c: CommentEntry, q: DbQuestion | undefined): Verdict {
  if (!q) return { status: "ausente", detalhe: "questão não existe neste banco" };
  if (q.contentHash !== c.contentHash) return { status: "desatualizado", detalhe: "o texto ou o gabarito da questão mudou depois do comentário" };
  const correct = q.options.find((o) => o.isCorrect)?.label ?? "";
  if (correct !== c.gabarito) return { status: "gabarito", detalhe: `gabarito do banco ${correct || "—"}, do comentário ${c.gabarito}` };
  const letters = Object.keys(c.alternativas).sort();
  let optionComments: Record<string, string | null>;
  if (q.kind === "CERTO_ERRADO") {
    if (letters.length) return { status: "alternativas", detalhe: "questão Certo/Errado não leva nota por alternativa" };
    optionComments = Object.fromEntries(q.options.map((o) => [o.label, null]));
  } else {
    const labels = q.options.map((o) => o.label).sort();
    if (letters.join() !== labels.join()) return { status: "alternativas", detalhe: `letras do comentário ${letters.join("")}, da questão ${labels.join("")}` };
    optionComments = Object.fromEntries(q.options.map((o) => [o.label, c.alternativas[o.label]]));
  }
  const same = q.explanation.trim() === c.comentario && q.options.every((o) => (o.comment ?? null) === optionComments[o.label]);
  return same ? { status: "igual" } : { status: "gravar", optionComments };
}
