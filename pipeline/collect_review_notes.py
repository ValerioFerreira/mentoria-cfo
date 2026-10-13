"""Reúne as NOTAS dos resumos importados (pontos que pedem revisão humana) em resumos-colaboradores/REVISAO-HUMANA-NOTAS.md.

Lê content/summaries/<disc>/<aula>.json (campo `notes` de cada trecho, gravado por import_agent_summaries.py) e cruza com o índice
(resumos-colaboradores/indice.json) para mostrar ID, matéria, aula, agente e as notas. Só leitura (exceto o relatório).

Uso:  python pipeline/collect_review_notes.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, ROOT  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

COLAB = ROOT / "resumos-colaboradores"


def main() -> int:
    index = {r["trecho"]: r for r in json.loads((COLAB / "indice.json").read_text(encoding="utf-8"))["rows"]}
    by_agent: dict[str, list[tuple[dict, str]]] = defaultdict(list)
    total = with_notes = 0
    for f in sorted((CONTENT_DIR / "summaries").glob("*/*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
            row = index.get(s["id"])
            agent = s.get("agent")
            if not row or not agent:
                continue
            total += 1
            note = (s.get("notes") or "").strip()
            if note:
                with_notes += 1
                by_agent[agent].append((row, note))
    lines = [
        "# Pontos que pedem revisão humana (NOTAS dos agentes)",
        "",
        f"{with_notes} de {total} resumos importados trazem notas. Gerado por `pipeline/collect_review_notes.py`; ordem: agente, depois ID.",
        "",
    ]
    for agent in sorted(by_agent):
        items = sorted(by_agent[agent], key=lambda x: x[0]["id"])
        lines += [f"## {agent} — {len(items)} resumos com notas", ""]
        for row, note in items:
            lines += [f"### {row['id']} · {row['subjectName']} · {row['aulaLabel']} · `{row['trecho']}`", "", note, ""]
    (COLAB / "REVISAO-HUMANA-NOTAS.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{with_notes}/{total} resumos com notas -> {COLAB / 'REVISAO-HUMANA-NOTAS.md'}")
    for agent in sorted(by_agent):
        print(f"  {agent}: {len(by_agent[agent])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
