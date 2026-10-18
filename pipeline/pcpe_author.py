"""Grava rascunhos de resumo + bizu (um arquivo de texto por aula) em content/summaries e content/items.

Formato do rascunho (UTF-8). Cada trecho começa com `@@@ <id>` e tem 5 blocos:
    @@@ direito-penal/a04/s03
    @@ ANALITICO      markdown do resumo analítico (termina com "### Para fixar")
    @@ SINTETICO      uma linha por ponto: **Ponto**: explicação        (vira bizu.summary)
    @@ TEORIA         C | afirmação || explicação      (C = certo, E = errado)
    @@ REVISAO        idem
    @@ PONTOS         <página> | tópico                (>= 4, páginas dentro do trecho)

Uso:  python pipeline/pcpe_author.py <rascunho.txt> [--batch nome] [--dry-run]
Substitui os trechos listados nos dois arquivos da aula (cria os arquivos se faltarem). Não toca nos demais trechos.
Depois: validate_summaries.py / validate_content.py e, no fim do lote, apply_synthetic.py.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from summary_source import segment  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def parse(text: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for block in re.split(r"^@@@\s+", text, flags=re.M)[1:]:
        head, _, rest = block.partition("\n")
        sid = head.strip()
        parts = re.split(r"^@@\s+(ANALITICO|SINTETICO|TEORIA|REVISAO|PONTOS)\s*$", rest, flags=re.M)
        sec = {parts[i]: parts[i + 1].strip("\n") for i in range(1, len(parts) - 1, 2)}
        missing = {"ANALITICO", "SINTETICO", "TEORIA", "REVISAO", "PONTOS"} - set(sec)
        if missing:
            raise SystemExit(f"{sid}: faltam blocos {sorted(missing)}")
        out[sid] = sec
    return out


def items(block: str, sid: str, kind: str) -> list[dict]:
    res = []
    for ln in block.splitlines():
        if not ln.strip():
            continue
        m = re.match(r"^\s*([CE])\s*\|\s*(.+?)\s*\|\|\s*(.+)$", ln)
        if not m:
            raise SystemExit(f"{sid} {kind}: linha inválida: {ln[:80]}")
        res.append({"statement": m.group(2).strip(), "isTrue": m.group(1) == "C", "explanation": m.group(3).strip()})
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--batch", default="pcpe-revisao")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    drafts = parse(Path(args.draft).read_text(encoding="utf-8"))
    by_aula: dict[str, list[str]] = {}
    for sid in drafts:
        by_aula.setdefault("/".join(sid.split("/")[:2]), []).append(sid)
    for aula, sids in by_aula.items():
        disc, aula_n = aula.split("/")
        sf = CONTENT_DIR / "summaries" / disc / f"{aula_n}.json"
        itf = CONTENT_DIR / "items" / disc / f"{aula_n}.json"
        sdoc = json.loads(sf.read_text(encoding="utf-8")) if sf.exists() else {"aula": aula, "batch": args.batch, "status": "DRAFT", "segments": []}
        idoc = json.loads(itf.read_text(encoding="utf-8")) if itf.exists() else {"aula": aula, "batch": args.batch, "status": "DRAFT", "stage": "bizu", "segments": []}
        for sid in sids:
            sec = drafts[sid]
            seg = segment(sid)
            fp = {"startPage": seg["startPage"], "endPage": seg["endPage"], "startTopic": seg.get("startTopic")}
            synth = [ln.strip() for ln in sec["SINTETICO"].splitlines() if ln.strip()]
            entry = {"id": sid, "fingerprint": fp, "analytic": sec["ANALITICO"].strip(), "synthetic": synth}
            pts = []
            for ln in sec["PONTOS"].splitlines():
                if ln.strip():
                    p, _, t = ln.partition("|")
                    pts.append({"topic": t.strip(), "pageRef": int(p.strip())})
            bizu = {"summary": synth, "teoria": items(sec["TEORIA"], sid, "teoria"), "revisao": items(sec["REVISAO"], sid, "revisao"), "pointers": pts}
            for doc, key, new in ((sdoc, "id", entry), (idoc, "id", {"id": sid, "bizu": bizu})):
                segs = doc["segments"]
                idx = next((i for i, s in enumerate(segs) if s["id"] == sid), None)
                if idx is None:
                    segs.append(new)
                else:
                    segs[idx] = {**segs[idx], **new}
                segs.sort(key=lambda s: s["id"])
        if not args.dry_run:
            for f, doc in ((sf, sdoc), (itf, idoc)):
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{aula}: {len(sids)} trecho(s) {'(simulação)' if args.dry_run else 'gravados'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
