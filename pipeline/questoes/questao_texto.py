"""Imprime o texto completo das questões de um arquivo de comentários, com o comentário atual (para revisão).

    PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/questao_texto.py <arquivo.json> [--id tec_123]

Lê o acervo extraído dos cadernos (o mesmo que o importador grava no banco). As figuras citadas são copiadas para
pipeline/.cache/questoes-comentar/img/<sha>.png e o caminho é impresso, para abrir com a ferramenta Read.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from questoes.importar import Store, load_all  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

IMG_OUT = ROOT / "pipeline" / ".cache" / "questoes-comentar" / "img"
IMG_RE = re.compile(r"/q-img/([0-9a-f]{64})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo")
    ap.add_argument("--id")
    a = ap.parse_args()
    store = Store(ROOT / "docs" / "questoes")
    acv: dict[str, dict] = {}
    for d in load_all(store):
        for q in d["questoes"]:
            acv[q["tecId"]] = q
    doc = json.loads(Path(a.arquivo).read_text(encoding="utf-8"))
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    for c in doc.get("comentarios", []):
        if a.id and c["id"] != a.id:
            continue
        q = acv.get(c["id"].removeprefix("tec_"))
        print("=" * 100)
        if not q:
            print(f"{c['id']}: não está no acervo")
            continue
        figs = []
        for t in [q.get("support") or "", q["statement"], *[o["text"] for o in q["options"]]]:
            for m in IMG_RE.finditer(t):
                dst = IMG_OUT / f"{m.group(1)}.png"
                src = store.img_dir / f"{m.group(1)}.png"
                if not dst.exists() and src.exists():
                    shutil.copyfile(src, dst)
                figs.append(dst.relative_to(ROOT).as_posix())
        print(f"{c['id']} · {q['kind']} · {q.get('banca')} {q.get('ano')} · assunto: {q.get('assunto')} · gabarito {q['answer']}")
        if figs:
            print("FIGURAS:", ", ".join(dict.fromkeys(figs)))
        if q.get("support"):
            print("TEXTO-BASE:", q["support"])
        print("ENUNCIADO:", q["statement"])
        for o in q["options"]:
            print(f"  {o['label']}) {o['text']}")
        print("--- comentário atual ---")
        print(c.get("comentario", ""))
        for k, v in sorted((c.get("alternativas") or {}).items()):
            print(f"  [{k}] {v}")


if __name__ == "__main__":
    main()
