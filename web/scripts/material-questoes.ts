// Exporta (somente leitura) as questões do banco que servem à Fixação de cada volume do material próprio MentorIA.
// Para cada volume de content/material/volumes/<disciplina>.json, grava pipeline/.cache/material/questoes/<disciplina>__mNN.json
// com as questões APROVADAS classificadas nos trechos do volume (enunciado, texto-base, alternativas, gabarito, banca, ano).
// O comentário que já existe no banco NÃO é exportado para o agente: vai para <arquivo>.ref.json, usado só pelo validador
// (pipeline/validate_material.py) para garantir que o comentário novo é autoral.
//   npx tsx scripts/material-questoes.ts --volume direito-penal-militar/m01
//   npx tsx scripts/material-questoes.ts --wave 1        # todos os volumes da onda 1
//   npx tsx scripts/material-questoes.ts --subject direito-penal-militar
import "dotenv/config";
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

type Volume = { id: string; title: string; wave: number; trechos: string[] };

const ROOT = resolve(__dirname, "..", "..");
const VOLUMES_DIR = resolve(ROOT, "content", "material", "volumes");
const OUT_DIR = resolve(ROOT, "pipeline", ".cache", "material", "questoes");

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(name);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

function loadVolumes(): Volume[] {
  if (!existsSync(VOLUMES_DIR)) throw new Error("rode antes: python pipeline/material_volumes.py");
  return readdirSync(VOLUMES_DIR)
    .filter((f) => f.endsWith(".json"))
    .flatMap((f) => (JSON.parse(readFileSync(resolve(VOLUMES_DIR, f), "utf8")) as { volumes: Volume[] }).volumes);
}

const maxPerChapter = Number(arg("--max-por-capitulo") ?? 8);
const PCPE_SUBJECTS = ["contabilidade-geral", "direito-penal/", "direito-processual-penal/", "legislacao-pcpe", "legislacao-penal-especial"];
const isPcpeVolume = (id: string) => PCPE_SUBJECTS.some((s) => id.startsWith(s.endsWith("/") ? s : s + "/"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "" }) });

async function main() {
  const volume = arg("--volume");
  const wave = arg("--wave");
  const subject = arg("--subject");
  if (!volume && !wave && !subject) throw new Error("informe --volume <id>, --wave <n> ou --subject <disciplina>");
  const vols = loadVolumes().filter(
    (v) => (volume && v.id === volume) || (wave && v.wave === Number(wave)) || (subject && v.id.startsWith(subject + "/")),
  );
  if (!vols.length) throw new Error("nenhum volume encontrado");
  mkdirSync(OUT_DIR, { recursive: true });
  for (const v of vols) {
    const qs = await db.question.findMany({
      where: { segmentId: { in: v.trechos }, status: "APPROVED" },
      include: { options: { orderBy: { label: "asc" } } },
      orderBy: [{ ano: "desc" }, { id: "asc" }],
    });
    const all = qs.map((q) => ({
      id: q.id,
      capitulo: q.segmentId,
      tipo: q.kind,
      banca: q.banca,
      ano: q.ano,
      orgao: q.orgao,
      cargo: q.cargo,
      assunto: q.tecAssunto ?? q.topic,
      temFigura: /\/q-img\//.test(q.statement + (q.support ?? "") + q.options.map((o) => o.text).join(" ")),
      textoBase: q.support,
      enunciado: q.statement,
      alternativas: q.options.map((o) => ({ letra: o.label, texto: o.text })),
      gabarito: q.kind === "CERTO_ERRADO" ? (q.options.find((o) => o.isCorrect)?.text.trim().toUpperCase().startsWith("C") ? "C" : "E") : q.options.find((o) => o.isCorrect)?.label,
    }));
    // Candidatas por capítulo (economia: o agente lê só estas): AOCP antes (Cebraspe junto no PCPE), sem figura antes,
    // as mais recentes primeiro; inéditas MentorIA só depois das reais.
    const pcpe = isPcpeVolume(v.id);
    const rank = (r: (typeof all)[number]) =>
      (r.banca.includes("AOCP") || (pcpe && r.banca.toUpperCase().includes("CEBRASPE")) ? 0 : r.banca === "Inédita MentorIA" ? 2 : 1) * 10 +
      (r.temFigura ? 1 : 0);
    const porCapitulo: Record<string, number> = {};
    const noBanco: Record<string, number> = {};
    const rows: typeof all = [];
    for (const t of v.trechos) {
      const cand = all.filter((r) => r.capitulo === t).sort((a, b) => rank(a) - rank(b) || (b.ano ?? 0) - (a.ano ?? 0));
      noBanco[t] = cand.length;
      rows.push(...cand.slice(0, maxPerChapter));
      porCapitulo[t] = Math.min(cand.length, maxPerChapter);
    }
    const base = resolve(OUT_DIR, v.id.replace("/", "__"));
    writeFileSync(
      base + ".json",
      JSON.stringify(
        { volume: v.id, titulo: v.title, exportadoEm: new Date().toISOString(), total: rows.length, porCapitulo, noBanco, questoes: rows },
        null,
        1,
      ),
    );
    const picked = new Set(rows.map((r) => r.id));
    writeFileSync(base + ".ref.json", JSON.stringify(Object.fromEntries(qs.filter((q) => picked.has(q.id)).map((q) => [q.id, q.explanation ?? ""]))));
    console.log(`${v.id.padEnd(40)} ${String(rows.length).padStart(4)} candidatas de ${all.length}  (${Object.values(porCapitulo).filter((n) => n === 0).length} capítulos sem questão)`);
  }
}

main().finally(() => db.$disconnect());
