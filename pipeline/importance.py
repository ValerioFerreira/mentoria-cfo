"""Nota de importância de cada trecho de teoria (= atividade de Teoria) por concurso.

Saída: content/importance/segments.json
  {"version": 1, "basis": {<concurso>: "disciplina" | "edital" | "edital+questoes"},
   "segments": {"<disc>/aNN/sNN": {"shared": n, "sharedShare": x, "contests": {"<CONCURSO>": {"appears": bool, "expected": q, "score": 1..100 | null}}}}}

Método (v1, determinístico, sem a frequência das questões — ver `importance_questions.py` para o refinamento):
  participação do trecho na disciplina = incidência normalizada da aula × (págs. do trecho / págs. de teoria da aula)
  questões esperadas no concurso     = nº de questões da disciplina na prova do concurso × participação do trecho
  nota (1–100)                        = percentil das questões esperadas entre os trechos que aparecem naquele concurso
  `appears` = a disciplina e aula estão no edital do concurso (via onlyContests e excludeContests versionados).

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
    return raw


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


def is_aula_in_contest(a: dict, contest_key: str) -> bool:
    """Verifica elegibilidade da aula para o concurso via dados versionados no catálogo."""
    if not a.get("selectable"):
        return False
    if a.get("onlyContests") and contest_key not in a["onlyContests"]:
        return False
    if a.get("excludeContests") and contest_key in a["excludeContests"]:
        return False
    return True


def build() -> dict:
    contests = load_contests()
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))

    all_segments: dict[str, dict] = {}
    segs_by_aula: dict[str, list[dict]] = {}
    subject_of: dict[str, str] = {}

    for subj in catalog["subjects"]:
        seg_file = CONTENT_DIR / "segments" / f"{subj['id']}.json"
        if not seg_file.exists():
            continue
        for s in json.loads(seg_file.read_text(encoding="utf-8"))["segments"]:
            all_segments[s["id"]] = s
            segs_by_aula.setdefault(s["aula"], []).append(s)
            subject_of[s["id"]] = subj["id"]

    expected: dict[str, dict[str, float]] = {c: {} for c in contests}

    for c, info in contests.items():
        exam_subjects = set(info.get("subjects", []))
        exam_weights = info.get("exam", {})

        for subj in catalog["subjects"]:
            sid = subj["id"]
            if sid not in exam_subjects or not exam_weights.get(sid):
                continue

            eligible_aulas = [a for a in subj["aulas"] if is_aula_in_contest(a, c)]
            total_inc = sum(a["incidence"] for a in eligible_aulas) or 1.0

            for a in eligible_aulas:
                segs = segs_by_aula.get(a["id"], [])
                pages = sum(s["pages"] for s in segs) or 1
                for s in segs:
                    share = (a["incidence"] / total_inc) * (s["pages"] / pages)
                    expected[c][s["id"]] = exam_weights[sid] * share

    scores = {c: percentile_scores(v) for c, v in expected.items()}

    basis = {c: "disciplina" for c in contests}
    segments: dict[str, dict] = {}

    for sid in all_segments:
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
