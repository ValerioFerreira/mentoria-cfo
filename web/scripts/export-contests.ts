// Exporta disciplinas e pesos de prova por concurso (fonte: contests.ts e simulado-rules.ts) para content/contests.json,
// que o pipeline Python lê (importância dos assuntos, fila de resumos). Rode de novo se esses arquivos mudarem.
// Uso: npx tsx scripts/export-contests.ts
import fs from "node:fs";
import path from "node:path";
import { CONTESTS, CONTEST_SUBJECTS } from "../src/lib/contests";
import { EXAM_CONFIGS } from "../src/lib/simulado-rules";

const out: Record<string, unknown> = {};
for (const c of CONTESTS) {
  const cfg = (EXAM_CONFIGS as Record<string, (typeof EXAM_CONFIGS)[keyof typeof EXAM_CONFIGS]>)[c.key];
  const exam: Record<string, number> = {};
  for (const s of cfg?.subjects ?? []) {
    // "FOREIGN_LANG": o candidato escolhe Inglês ou Espanhol; o peso vale para qualquer uma das duas
    if (s.subjectId === "FOREIGN_LANG") {
      exam["lingua-inglesa"] = s.count;
      exam["lingua-espanhola"] = s.count;
    } else exam[s.subjectId] = s.count;
  }
  out[c.key] = {
    available: c.available,
    category: c.category || null,
    org: c.org,
    totalQuestions: cfg?.totalQuestions ?? null,
    /** disciplinas do catálogo que o concurso usa (as demais de `exam` não têm material no catálogo) */
    subjects: CONTEST_SUBJECTS[c.key],
    /** nº de questões por disciplina na prova */
    exam,
  };
}
const file = path.resolve(__dirname, "../../content/contests.json");
fs.writeFileSync(file, JSON.stringify(out, null, 2) + "\n", "utf-8");
console.log(`escrito ${file}`);
