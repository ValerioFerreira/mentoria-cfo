"""Lista as menções a concurso, banca e instituição no texto que vai para o PDF (só leitura).

O material próprio é genérico para qualquer concurso (decisão do dono, 02/11/2026). Fontes do texto impresso:
corpo dos capítulos e do volume.md (sem o front matter), comentários do fixacao.json e os complementos (content/complements).
Os quadros [!lei] ficam de fora: são a letra da lei.

Uso:
  python pipeline/contest_mentions.py                     # resumo por disciplina
  python pipeline/contest_mentions.py --lista legislacoes-pe direito-penal-militar   # linhas a revisar dessas pastas
  python pipeline/contest_mentions.py --json saida.json
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_material import BANCA, DIRECIONA, INSTITUICAO, MATERIAL_DIR, parse_front_matter, strip_lei  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

COMPLEMENTS = MATERIAL_DIR.parent / "complements"
KINDS = (("direcionamento", DIRECIONA), ("banca", BANCA), ("instituicao", INSTITUICAO))


def _scan(text: str, path: Path, offset: int, group: str) -> list[dict]:
    out = []
    clean = strip_lei(text).splitlines()
    raw = text.splitlines()
    for i, ln in enumerate(raw):
        if i < len(clean) and ln.startswith(">") and ln not in clean:
            continue
        for kind, rx in KINDS:
            for m in rx.finditer(ln):
                out.append({"grupo": group, "arquivo": str(path.relative_to(MATERIAL_DIR.parent.parent)).replace("\\", "/"),
                            "linha": i + 1 + offset, "tipo": kind, "termo": m.group(0), "texto": ln.strip()[:300]})
    return out


def scan_all() -> list[dict]:
    rows: list[dict] = []
    for f in sorted(MATERIAL_DIR.glob("*/m*/*.md")):
        if f.name == "REVISAO.md":
            continue
        text = f.read_text(encoding="utf-8")
        _, body, _ = parse_front_matter(text)
        offset = text[: len(text) - len(body)].count("\n")
        rows += _scan(body, f, offset, f.parent.parent.name)
    for f in sorted(MATERIAL_DIR.glob("*/m*/fixacao.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for q in (d.get("questoes") or []) + (d.get("ineditas") or []):
            txt = " ".join([q.get("comentario", ""), *[str(v) for v in (q.get("alternativas") or {}).values()],
                            q.get("enunciado", ""), *[str(v) for v in (q.get("alternativas_texto") or {}).values()]])
            for r in _scan(txt, f, 0, f.parent.parent.name):
                r["linha"] = q.get("id")
                rows.append(r)
    for f in sorted(COMPLEMENTS.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        body = text
        if text.startswith("---"):  # front matter (id, resolves…) não vai para o PDF
            end = text.find("\n---", 3)
            body = text[end + 4:] if end > 0 else text
        rows += _scan(body, f, text[: len(text) - len(body)].count("\n"), "complementos")
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lista", nargs="*", metavar="PASTA", help="mostra as linhas destas disciplinas (ou 'complementos')")
    ap.add_argument("--json", metavar="ARQ")
    ap.add_argument("--sem-instituicao", action="store_true", help="omite as menções só de instituição (avisos)")
    args = ap.parse_args()
    rows = scan_all()
    if args.json:
        Path(args.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.lista is not None:
        for r in rows:
            if (not args.lista or r["grupo"] in args.lista) and not (args.sem_instituicao and r["tipo"] == "instituicao"):
                print(f"{r['arquivo']}:{r['linha']} [{r['tipo']}] {r['termo']} | {r['texto']}")
        return 0
    by = Counter((r["grupo"], r["tipo"]) for r in rows)
    groups = sorted({g for g, _ in by})
    print(f"{'pasta':<34} {'direc.':>7} {'banca':>6} {'instit.':>8}")
    for g in groups:
        print(f"{g:<34} {by[(g, 'direcionamento')]:>7} {by[(g, 'banca')]:>6} {by[(g, 'instituicao')]:>8}")
    print(f"{'TOTAL':<34} {sum(v for (g, t), v in by.items() if t == 'direcionamento'):>7} "
          f"{sum(v for (g, t), v in by.items() if t == 'banca'):>6} {sum(v for (g, t), v in by.items() if t == 'instituicao'):>8}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
