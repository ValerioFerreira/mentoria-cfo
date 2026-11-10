"""Meta de questões da Fixação de cada volume do material próprio, pela média do material-base (decisão do dono, 02/11/2026).

Razão por disciplina = questões comentadas das aulas-base (pipeline/.cache/corpus/questions.jsonl, de pipeline/corpus.py) ÷ páginas
de teoria dessas mesmas aulas (content/catalog.json, só as aulas que têm questões comentadas). Meta de cada capítulo = razão × páginas
de teoria do trecho na fonte (content/material/metrics), arredondada, com mínimo de 2. O validador e o seletor leem
content/material/metrics/_fixacao.json.

Uso: python pipeline/material_fixacao_meta.py   (rode pipeline/corpus.py antes, se o corpus não existir)
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import CACHE_DIR, CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MATERIAL = CONTENT_DIR / "material"
OUT = MATERIAL / "metrics" / "_fixacao.json"
CORPUS = CACHE_DIR / "corpus" / "questions.jsonl"
MIN_PER_CHAPTER = 2


def ratios() -> dict[str, dict]:
    q = Counter(json.loads(ln)["aula"] for ln in CORPUS.read_text(encoding="utf-8").splitlines() if ln.strip())
    cat = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    out = {}
    for s in cat["subjects"]:
        aulas = [a for a in s["aulas"] if a.get("theoryPages") and q.get(a["id"], 0) > 0]
        qs, pages = sum(q[a["id"]] for a in aulas), sum(a["theoryPages"] for a in aulas)
        out[s["id"]] = {"questoes": qs, "paginasTeoria": pages, "aulas": len(aulas), "razao": round(qs / pages, 4) if pages else 0.0}
    return out


def build() -> dict:
    r = ratios()
    metrics = {}
    for f in (MATERIAL / "metrics").glob("*.json"):
        if f.name.startswith("_"):
            continue
        for t in json.loads(f.read_text(encoding="utf-8"))["trechos"]:
            metrics[t["id"]] = t
    volumes = {}
    for f in sorted((MATERIAL / "volumes").glob("*.json")):
        for v in json.loads(f.read_text(encoding="utf-8"))["volumes"]:
            subj = v["id"].split("/")[0]
            k = r.get(subj, {}).get("razao", 0.0)
            caps = {}
            for t in v["trechos"]:
                pages = ((metrics.get(t) or {}).get("source") or {}).get("theoryPages") or 0
                caps[t] = max(MIN_PER_CHAPTER, round(k * pages))
            volumes[v["id"]] = {"onda": v.get("wave"), "meta": sum(caps.values()), "porCapitulo": caps}
    return {"_comentario": "Gerado por pipeline/material_fixacao_meta.py (não edite à mão).", "minimoPorCapitulo": MIN_PER_CHAPTER,
            "razaoPorDisciplina": r, "volumes": volumes}


def main() -> int:
    if not CORPUS.exists():
        print("rode antes: pipeline/.venv/Scripts/python pipeline/corpus.py")
        return 1
    d = build()
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    w1 = [v for v in d["volumes"].values() if v["onda"] == 1]
    print(f"{OUT}: {len(d['volumes'])} volumes; onda 1 = {sum(v['meta'] for v in w1)} questões "
          f"({min(v['meta'] for v in w1)} a {max(v['meta'] for v in w1)} por volume)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
