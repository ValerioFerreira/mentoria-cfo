"""Espelha para web/content (lido pelo build/seed) o conteúdo das 12 disciplinas do PCPE Agente que mudou em content/.

Só copia arquivo ausente ou diferente (comparando o JSON, não os bytes: ignora CRLF/indentação) e só das disciplinas do
PCPE, para não mexer em arquivos de outras frentes. Depois rode `python pipeline/apply_synthetic.py` (bizu.summary +
importance + contests + summaries) e confira com `python pipeline/pcpe_tools/audit_pcpe.py .`.

Uso: python pipeline/pcpe_tools/mirror_web.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C, W = ROOT / "content", ROOT / "web" / "content"
PCPE_SUBJECTS = [
    "lingua-portuguesa", "informatica", "raciocinio-logico", "matematica", "estatistica", "contabilidade-geral",
    "legislacao-pcpe", "direito-constitucional", "direito-administrativo", "direito-penal",
    "legislacao-penal-especial", "direito-processual-penal",
]


def same(a: Path, b: Path) -> bool:
    if not b.exists():
        return False
    if a.suffix != ".json":
        return a.read_bytes().replace(b"\r\n", b"\n") == b.read_bytes().replace(b"\r\n", b"\n")
    return json.loads(a.read_text(encoding="utf-8")) == json.loads(b.read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    copied = 0
    for sub in PCPE_SUBJECTS:
        files: list[Path] = []
        for kind in ("items", "summaries"):
            files += sorted((C / kind / sub).glob("*.json"))
        for kind in ("structure", "segments", "overrides", "edital"):
            f = C / kind / f"{sub}.json"
            if f.exists():
                files.append(f)
        f = C / "edital" / "pcpe" / f"{sub}.json"
        if f.exists():
            files.append(f)
        for src in files:
            dst = W / src.relative_to(C)
            if same(src, dst):
                continue
            copied += 1
            print(("[simulação] " if args.dry_run else "") + str(src.relative_to(C)))
            if not args.dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
    for kind in ("catalog.json", "gaps.json", "subjects.json", "contests.json", "overrides.json"):
        src, dst = C / kind, W / kind
        if src.exists() and not same(src, dst):
            copied += 1
            print(("[simulação] " if args.dry_run else "") + kind)
            if not args.dry_run:
                shutil.copy2(src, dst)
    print(f"{copied} arquivo(s) {'a copiar' if args.dry_run else 'copiado(s)'} para web/content")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
