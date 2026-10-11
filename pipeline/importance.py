"""Nota de importância de cada trecho de teoria (= atividade de Teoria) por concurso.

Saída: content/importance/segments.json
  {"version": 1, "basis": {<concurso>: "disciplina" | "edital" | "edital+questoes"},
   "segments": {"<disc>/aNN/sNN": {"shared": n, "sharedShare": x, "contests": {"<CONCURSO>": {"appears": bool, "expected": q, "score": 1..100 | null}}}}}

Método (v1, determinístico, sem a frequência das questões — ver `importance_questions.py` para o refinamento):
  participação do trecho na disciplina = incidência normalizada da aula × (págs. do trecho / págs. de teoria da aula)
  questões esperadas no concurso     = nº de questões da disciplina na prova do concurso × participação do trecho
  nota (1–100)                        = percentil das questões esperadas entre os trechos que aparecem naquele concurso
  `appears` = a disciplina está no concurso (v1). Quando existir o mapa edital→trecho do concurso (content/edital/<concurso>/…),
  o campo vem do edital (ver `basis`).

Uso: python pipeline/importance.py          (gera/atualiza o arquivo)
Pré-requisito: content/contests.json  (npx tsx web/scripts/export-contests.ts, em web/)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

OUT = CONTENT_DIR / "importance" / "segments.json"
EDITAL_DIR = CONTENT_DIR / "edital"


def load_contests() -> dict[str, dict]:
    raw = json.loads((CONTENT_DIR / "contests.json").read_text(encoding="utf-8"))
    return {k: v for k, v in raw.items() if v.get("available")}


def percentile_scores(values: dict[str, float]) -> dict[str, int]:
    """Percentil 1–100 (maior = mais importante); empates dividem o mesmo posto médio."""
    items = sorted(values.items(), key=lambda kv: kv[1])
    n = len(items)
    out: dict[str, int] = {}
    i = 0
    while i < n:
        j = i
        while j + 1 < n and items[j + 1][1] == items[i][1]:
            j += 1
        pct = ((i + j) / 2 + 1) / n * 100
        for k in range(i, j + 1):
            out[items[k][0]] = max(1, min(100, round(pct)))
        i = j + 1
    return out


def build() -> dict:
    contests = load_contests()
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    segments: dict[str, dict] = {}
    shares: dict[str, float] = {}
    subject_of: dict[str, str] = {}
    for subj in catalog["subjects"]:
        aulas = [a for a in subj["aulas"] if a.get("selectable")]
        total_inc = sum(a["incidence"] for a in aulas) or 1.0
        seg_file = CONTENT_DIR / "segments" / f"{subj['id']}.json"
        if not seg_file.exists():
            continue
        by_aula: dict[str, list[dict]] = {}
        for s in json.loads(seg_file.read_text(encoding="utf-8"))["segments"]:
            by_aula.setdefault(s["aula"], []).append(s)
        for a in aulas:
            segs = by_aula.get(a["id"], [])
            pages = sum(s["pages"] for s in segs) or 1
            for s in segs:
                shares[s["id"]] = (a["incidence"] / total_inc) * (s["pages"] / pages)
                subject_of[s["id"]] = subj["id"]

    expected: dict[str, dict[str, float]] = {c: {} for c in contests}
    for sid, share in shares.items():
        subj = subject_of[sid]
        for c, info in contests.items():
            if subj in info["subjects"] and info["exam"].get(subj):
                expected[c][sid] = info["exam"][subj] * share
    scores = {c: percentile_scores(v) for c, v in expected.items()}

    basis = {c: "disciplina" for c in contests}
    for sid in shares:
        rec = {"shared": 0, "sharedShare": 0.0, "contests": {}}
        for c, info in contests.items():
            appears = sid in expected[c]
            rec["contests"][c] = {
                "appears": appears,
                "expected": round(expected[c].get(sid, 0.0), 5),
                "score": scores[c].get(sid) if appears else None,
            }
            if appears:
                rec["shared"] += 1
                rec["sharedShare"] += expected[c][sid] / (info["totalQuestions"] or 1)
        rec["sharedShare"] = round(rec["sharedShare"], 6)
        segments[sid] = rec
    return {"version": 1, "basis": basis, "contests": sorted(contests), "segments": segments}


def main() -> None:
    doc = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    segs = doc["segments"]
    by_shared: dict[int, int] = {}
    for r in segs.values():
        by_shared[r["shared"]] = by_shared.get(r["shared"], 0) + 1
    print(f"{len(segs)} trechos -> {OUT}")
    print("trechos por nº de concursos em que aparecem:", dict(sorted(by_shared.items(), reverse=True)))


if __name__ == "__main__":
    main()
