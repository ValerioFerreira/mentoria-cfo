"""Seleciona as questões da Fixação de cada volume pela meta da média do material-base (decisão do dono, 02/11/2026).

Por capítulo: meta = content/material/metrics/_fixacao.json (material_fixacao_meta.py), limitada às candidatas exportadas do banco
(pipeline/.cache/material/questoes/<disc>__mNN.json, de web/scripts/material-questoes.ts, já em ordem de preferência: AOCP real,
outras reais, inéditas do banco; sem figura antes; mais recentes antes).
- Mantém as questões já comentadas que continuam entre as candidatas do capítulo.
- Completa até a meta com as candidatas seguintes (entram sem comentário: os comentários são escritos depois).
- Se passar da meta, sai primeiro a de pior posição na ordem de preferência (inéditas antes das reais).
- Inéditas escritas pelo autor (`ineditas[]`, fora do banco) só ficam em capítulo sem nenhuma questão no banco.

Uso: python pipeline/material_fixacao_select.py --onda 1 [--aplicar]   (sem --aplicar só mostra o que faria)
     Grava em pipeline/.cache/material/a-comentar.json a lista das questões novas, por volume.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_material import MATERIAL_DIR, QUESTIONS_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TODO = QUESTIONS_DIR.parent / "a-comentar.json"


def select(vid: str, meta: dict, apply: bool) -> dict:
    vdir = MATERIAL_DIR / vid
    fx_path = vdir / "fixacao.json"
    fx = json.loads(fx_path.read_text(encoding="utf-8"))
    cache = json.loads((QUESTIONS_DIR / (vid.replace("/", "__") + ".json")).read_text(encoding="utf-8"))
    cand: dict[str, list[dict]] = {}
    for q in cache["questoes"]:
        cand.setdefault(q["capitulo"], []).append(q)
    # descartes por qualidade (gabarito duvidoso, lei mudou, depende de figura) nunca voltam a ser escolhidos
    bad = {d["id"] for d in fx.get("descartes", []) if isinstance(d, dict)
           and re.search(r"QUALIDADE|gabarito|desatualiz|errad|anulad|figura|revogad|sem texto|norma interna", str(d.get("motivo", "")), re.I)}
    cand = {t: [q for q in qs if q["id"] not in bad] for t, qs in cand.items()}
    pos = {q["id"]: i for i, q in enumerate(cache["questoes"])}
    existing = {q["id"]: q for q in fx.get("questoes", [])}
    out, added, dropped = [], [], []
    for t, goal in meta["porCapitulo"].items():
        pool = cand.get(t, [])
        ids = {q["id"] for q in pool}
        kept = sorted([q for q in existing.values() if q.get("capitulo") == t and q["id"] in ids], key=lambda q: pos[q["id"]])
        dropped += [q["id"] for q in existing.values() if q.get("capitulo") == t and q["id"] not in ids]
        goal = min(goal, len(pool))
        if len(kept) > goal:
            dropped += [q["id"] for q in kept[goal:]]
            kept = kept[:goal]
        chosen = {q["id"] for q in kept}
        for q in pool:
            if len(kept) >= goal:
                break
            if q["id"] not in chosen:
                new = {"id": q["id"], "capitulo": t, "gabarito": q["gabarito"], "comentario": "", "alternativas": {}}
                kept.append(new)
                chosen.add(q["id"])
                added.append(q["id"])
        out += sorted(kept, key=lambda q: pos[q["id"]])
    dropped += [q["id"] for q in existing.values() if q.get("capitulo") not in meta["porCapitulo"]]
    no_bank = {t for t in meta["porCapitulo"] if not cand.get(t)}
    ineditas = [q for q in fx.get("ineditas", []) if q.get("capitulo") in no_bank]
    dropped += [q["id"] for q in fx.get("ineditas", []) if q.get("capitulo") not in no_bank]
    if apply:
        fx["questoes"] = out
        fx["ineditas"] = ineditas
        fx_path.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"volume": vid, "meta": meta["meta"], "total": len(out) + len(ineditas), "mantidas": len(out) - len(added),
            "novas": added, "removidas": dropped, "ineditasAutor": len(ineditas)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--onda", type=int, required=True)
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--disciplinas", nargs="*", help="só estas disciplinas (padrão: todas da onda)")
    args = ap.parse_args()
    metas = json.loads((MATERIAL_DIR / "metrics" / "_fixacao.json").read_text(encoding="utf-8"))["volumes"]
    rows = [select(vid, m, args.aplicar) for vid, m in sorted(metas.items()) if m["onda"] == args.onda and (MATERIAL_DIR / vid).is_dir()
            and (not args.disciplinas or vid.split("/")[0] in args.disciplinas)]
    print(f"{'volume':<40} {'meta':>5} {'total':>6} {'mant.':>6} {'novas':>6} {'remov.':>7}")
    for r in rows:
        print(f"{r['volume']:<40} {r['meta']:>5} {r['total']:>6} {r['mantidas']:>6} {len(r['novas']):>6} {len(r['removidas']):>7}")
    print(f"{'TOTAL':<40} {sum(r['meta'] for r in rows):>5} {sum(r['total'] for r in rows):>6} {sum(r['mantidas'] for r in rows):>6} "
          f"{sum(len(r['novas']) for r in rows):>6} {sum(len(r['removidas']) for r in rows):>7}")
    if args.aplicar:
        todo = json.loads(TODO.read_text(encoding="utf-8")) if TODO.exists() else {}
        todo.update({r["volume"]: r["novas"] for r in rows if r["novas"]})
        TODO.write_text(json.dumps(todo, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"a comentar: {TODO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
