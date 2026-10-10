/* eslint-disable @typescript-eslint/no-explicit-any */
// Sorteia trechos para auditoria por amostragem (diretriz + bizu). Uso: npx tsx scripts/_sample-audit.ts <saida.json> [n] [seed] [disciplina1,disciplina2,...]
import fs from "node:fs";
import path from "node:path";
import { teoriaStep, pageLabel, type SegmentRef } from "../src/lib/directive";

const root = path.resolve(__dirname, "../..");
const out = process.argv[2];
const N = Number(process.argv[3] ?? 50);
let seed = Number(process.argv[4] ?? 20261010);
const only = process.argv[5] ? new Set(process.argv[5].split(",")) : null;
const rnd = () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296);

const cat = JSON.parse(fs.readFileSync(path.join(root, "content/catalog.json"), "utf8"));
const pool: any[] = [];
for (const subjCat of cat.subjects) {
  const subj = subjCat.id;
  if (only && !only.has(subj)) continue;
  const seg = JSON.parse(fs.readFileSync(path.join(root, "content/segments", `${subj}.json`), "utf8"));
  const segs: any[] = Array.isArray(seg.segments) ? seg.segments : Object.values(seg.segments).flat();
  const itemsDir = path.join(root, "content/items", subj);
  const bizuById = new Map<string, any>();
  if (fs.existsSync(itemsDir)) {
    for (const f of fs.readdirSync(itemsDir)) {
      if (!f.endsWith(".json")) continue;
      const d = JSON.parse(fs.readFileSync(path.join(itemsDir, f), "utf8"));
      for (const s of d.segments ?? []) if (s.bizu) bizuById.set(s.id, s.bizu);
    }
  }
  for (const s of segs) {
    const bizu = bizuById.get(s.id);
    if (!bizu) continue;
    const aula = subjCat.aulas.find((a: any) => a.id === s.aula);
    if (!aula || aula.number > 100) continue; // complementos autorais não têm PDF do material-base
    const ref: SegmentRef = {
      id: s.id, startPage: s.startPage, endPage: s.endPage, startPrinted: s.startPrinted, endPrinted: s.endPrinted,
      startTopic: s.startTopic, startsMidTopic: s.startsMidTopic, stopBeforeTopic: s.stopBeforeTopic,
      endsMidTopic: s.endsMidTopic, endTopic: s.endTopic, endsTheory: s.endsTheory,
    };
    pool.push({
      segmentId: s.id,
      subject: subj,
      aulaNumber: aula.number,
      aulaTitle: aula.shortTitle ?? aula.title,
      diretriz: teoriaStep(ref),
      paginas: `${pageLabel(s.startPage, s.startPrinted)} a ${pageLabel(s.endPage, s.endPrinted)}`,
      bizu: { summary: bizu.summary, pointers: bizu.pointers, certoErrado: [...(bizu.teoria ?? []), ...(bizu.revisao ?? [])] },
    });
  }
}
for (let i = pool.length - 1; i > 0; i--) {
  const j = Math.floor(rnd() * (i + 1));
  [pool[i], pool[j]] = [pool[j], pool[i]];
}
const sample = pool.slice(0, N).map((x, i) => ({ n: i + 1, ...x }));
fs.writeFileSync(out, JSON.stringify(sample, null, 1), "utf8");
const bySubj: Record<string, number> = {};
for (const s of sample) bySubj[s.subject] = (bySubj[s.subject] ?? 0) + 1;
console.log(`pool=${pool.length} amostra=${sample.length}`, bySubj);
