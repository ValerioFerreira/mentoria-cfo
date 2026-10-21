"""Grava analytic/synthetic de trechos a partir de um arquivo de correção (Etapa B do PCPE).

Uso: python pipeline/pcpe_tools/patch_summary.py <correcao.md> [--dry]

Formato do arquivo de correção (markdown simples, um ou mais trechos):

    @@@ <disc>/aNN/sNN
    === analytic
    <texto do analítico>
    === synthetic
    **Ponto**: explicação
    **Outro ponto**: explicação
    === notes
    (opcional) texto acrescentado ao campo "notes" da aula

Só altera os campos `analytic`/`synthetic` do trecho (e acrescenta a nota, se houver);
preserva o resto do arquivo, a impressão digital e o status.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]


def parse(text):
    out = []
    for block in re.split(r"^@@@ ", text, flags=re.M)[1:]:
        tid, rest = block.split("\n", 1)
        parts = re.split(r"^=== (analytic|synthetic|notes)\s*$", rest, flags=re.M)
        rec = {"id": tid.strip()}
        for k, v in zip(parts[1::2], parts[2::2]):
            rec[k] = v.strip()
        out.append(rec)
    return out


def main():
    src = Path(sys.argv[1])
    dry = "--dry" in sys.argv
    recs = parse(src.read_text(encoding="utf-8"))
    by_file = {}
    for r in recs:
        disc, aula, _ = r["id"].split("/")
        by_file.setdefault(ROOT / "content" / "summaries" / disc / f"{aula}.json", []).append(r)
    for path, items in by_file.items():
        doc = json.loads(path.read_text(encoding="utf-8"))
        segs = {s["id"]: s for s in doc["segments"]}
        for r in items:
            seg = segs[r["id"]]
            if "analytic" in r:
                seg["analytic"] = r["analytic"]
            if "synthetic" in r:
                seg["synthetic"] = [l.strip() for l in r["synthetic"].split("\n") if l.strip()]
            if r.get("notes"):
                prev = doc.get("notes", "").strip()
                tag = f"[{r['id']}] "
                if tag + r["notes"] not in prev:  # idempotente: não repete a mesma nota
                    doc["notes"] = (prev + "\n" if prev else "") + tag + r["notes"]
            n = len(seg["analytic"].split())
            print(f"{r['id']}: analítico {n} palavras · sintético {len(seg['synthetic'])} pontos")
        if not dry:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
