"""Vigia mensal do material próprio: baixa de novo as leis e aponta só o que mudou (artigos citados cujo texto vigente mudou).

Compara a impressão digital (sha256) de cada artigo citado, guardada em content/material/atualizacao/indice.json por
pipeline/material_update_index.py, com o texto vigente recém-baixado do Planalto/ALEPE (pipeline/leis.py). Grava
content/material/atualizacao/relatorio-AAAA-MM.md com:
  1. artigos que MUDARAM (ou foram revogados/sumiram) e os capítulos e volumes afetados;
  2. jurisprudência citada nos volumes de volatilidade ALTA (para conferir nos sites dos tribunais);
  3. pontos sensíveis (pendências, julgamentos em curso, redação nova).
O agente mensal (pipeline/briefs/atualizacao.md) trabalha só sobre esse relatório.

Uso: python pipeline/material_watch.py [--sem-baixar]   (--sem-baixar: compara com o cache atual, sem internet)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import material_update_index as mui  # noqa: E402
from leis import baixar  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def diff(idx: dict) -> list[dict]:
    """Artigos cujo texto vigente mudou desde o índice."""
    mui._ART_CACHE.clear()
    changes = []
    seen = set()
    for vid, v in idx["volumes"].items():
        for t, c in v["capitulos"].items():
            for n in c["normas"]:
                if not n.get("sha"):
                    continue
                key = (n["lei"], n["art"])
                now = mui.sha(mui.article_text(*key))
                if now != n["sha"]:
                    changes.append({"lei": n["lei"], "art": n["art"], "volume": vid, "trecho": t, "arquivo": c["arquivo"],
                                    "situacao": "removido ou revogado" if not now else "texto mudou",
                                    "texto": (mui.article_text(*key) or "")[:600], "novo": key not in seen})
                    seen.add(key)
    return changes


def report(idx: dict, changes: list[dict]) -> str:
    today = dt.date.today()
    lines = [f"# Relatório de atualização do material — {today:%m/%Y}", "",
             f"Gerado em {today:%d/%m/%Y} por `pipeline/material_watch.py` sobre o índice de {idx['geradoEm'][:10]}.", ""]
    lines += ["## 1. Artigos que mudaram desde o índice", ""]
    if not changes:
        lines += ["Nenhum artigo citado mudou no texto vigente.", ""]
    else:
        by_art: dict[tuple, list] = defaultdict(list)
        for c in changes:
            by_art[(c["lei"], c["art"])].append(c)
        for (lei, art), cs in sorted(by_art.items()):
            lines.append(f"### {lei} art. {art} ({cs[0]['situacao']})")
            lines.append(f"Texto vigente: {cs[0]['texto'] or '(não encontrado)'}")
            lines += [f"- {c['volume']} · {c['trecho']} · `{c['arquivo']}`" for c in cs]
            lines.append("")
    lines += ["## 2. Jurisprudência a conferir (volumes de volatilidade ALTA)", ""]
    for vid, v in idx["volumes"].items():
        if v["volatilidade"] != "ALTA":
            continue
        items = sorted({j for c in v["capitulos"].values() for j in c["jurisprudencia"]})
        if items:
            lines.append(f"- **{vid}**: {'; '.join(items)}")
    lines += ["", "## 3. Pontos sensíveis (pendências, julgamentos em curso, redação nova)", ""]
    for vid, v in idx["volumes"].items():
        for t, c in v["capitulos"].items():
            for s in c["sensiveis"]:
                lines.append(f"- {vid} · {t}: {s[:240]}")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sem-baixar", action="store_true")
    args = ap.parse_args()
    f = mui.OUT_DIR / "indice.json"
    if not f.exists():
        print("rode antes: pipeline/.venv/Scripts/python pipeline/material_update_index.py")
        return 1
    idx = json.loads(f.read_text(encoding="utf-8"))
    if not args.sem_baixar:
        baixar(sorted(idx["normas"]))
    changes = diff(idx)
    out = mui.OUT_DIR / f"relatorio-{dt.date.today():%Y-%m}.md"
    out.write_text(report(idx, changes), encoding="utf-8")
    arts = {(c["lei"], c["art"]) for c in changes}
    vols = {c["volume"] for c in changes}
    print(f"{len(arts)} artigo(s) mudaram, em {len(vols)} volume(s) -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
