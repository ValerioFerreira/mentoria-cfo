"""Âncoras das diretrizes do material-base: o texto REAL, impresso nas páginas, que o aluno vai encontrar.

Os títulos de `content/segments` (startTopic/stopBeforeTopic) servem ao planejador, aos resumos e às listas de atividades; vários
são rótulos descritivos ou títulos do índice que não aparecem na página. A diretriz não pode usá-los. Este módulo calcula, para
cada trecho, o que está de fato escrito no material (cabeçalhos por fonte + títulos da estrutura que aparecem literalmente na página):

  start.kind = "heading"  a página inicial abre com este cabeçalho  -> "Comece na pág. N, no tópico “H”"
               "inside"   a página abre dentro de um tópico iniciado antes -> "Continue na pág. N, dentro do tópico “H”"
               "opens"    não há cabeçalho antes; cita o início da página -> "Comece na pág. N, que abre com “…”"
  stop.kind  = "heading"  o 1º cabeçalho da pág. seguinte (onde o próximo trecho começa)
               "inside"   a pág. seguinte não tem cabeçalho: o trecho termina dentro de H
               None       último trecho da teoria

Saída: content/directive/anchors.json (espelhado em web/content/directive/anchors.json), lida por web/src/lib/directive-anchors.ts.
Também confere tudo: `python pipeline/directive_anchors.py --check` falha se algum texto citado não estiver na página indicada.
Uso: python pipeline/directive_anchors.py [--check]
"""
from __future__ import annotations

import glob
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import directive_check as dc  # noqa: E402
from textutil import aula_key_map  # noqa: E402

ROOT = dc.ROOT
OUT = ROOT / "content" / "directive" / "anchors.json"
BIDI = re.compile(r"[​-‏‪-‮﻿]")
BOILER = re.compile(r"^(aula\s*\d+|\d+|equipe .*|www\..*|[a-zà-ú .]*estrat[eé]gia.*|p[áa]gina\s*\d+.*)$", re.I)
NOISE = re.compile(r"@|equipe|estrat[eé]gia|material complementar|mentoria|\.com|www|^\W*$", re.I)
KEYS = aula_key_map()
HEAD_CACHE: dict[str, dict[int, list[str]]] = {}


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", BIDI.sub("", s or "")).strip()


def body_lines(text: str) -> list[str]:
    out = []
    for ln in (text or "").splitlines():
        ln = clean(ln)
        if ln and not BOILER.match(ln) and not NOISE.search(ln):
            out.append(ln)
    return out


def font_heads(aula_id: str) -> dict[int, list[str]]:
    if aula_id in HEAD_CACHE:
        return HEAD_CACHE[aula_id]
    out: dict[int, list[str]] = {}
    key = KEYS.get(aula_id)
    f = ROOT / "pipeline" / ".cache" / "headings" / f"{key}.json" if key else None
    if f and f.exists():
        for x in json.loads(f.read_text(encoding="utf-8"))["headings"]:
            t = clean(x["text"])
            if len(t) >= 4 and not NOISE.search(t):
                out.setdefault(x["page"], []).append(t)
        count: dict[str, int] = {}
        for lst in out.values():
            for t in set(lst):
                count[t] = count.get(t, 0) + 1
        out = {p: [t for t in lst if count[t] < 4] for p, lst in out.items()}  # repetido em várias páginas = cabeçalho corrente
    HEAD_CACHE[aula_id] = out
    return out


def page_heads(aula_id: str, pages: dict[int, str]) -> dict[int, list[str]]:
    """Cabeçalhos reais por página, na ordem em que aparecem."""
    heads: dict[int, list[str]] = {}
    cand = {p: list(v) for p, v in font_heads(aula_id).items()}
    for t in dc.aula_struct(aula_id).get("topics", []):
        p, title = t.get("pdfPage"), clean(t.get("title", ""))
        if p and title and title not in cand.get(p, []):
            cand.setdefault(p, []).append(title)
    for p, lst in cand.items():
        txt = dc.norm(pages.get(p, ""))
        ok = [(txt.find(dc.norm(h)), h) for h in lst if dc.norm(h) and dc.norm(h) in txt]
        if ok:
            heads[p] = [h for _, h in sorted(ok)]
    return heads


def opens_text(text: str, limit: int = 80) -> str | None:
    """Primeira linha de texto da página (inteira, contígua no PDF)."""
    s = next((ln for ln in body_lines(text) if len(ln) >= 12), None)
    if not s:
        return None
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0]
    return s.rstrip(" ,;:-–")


def at_top(h: str, text: str) -> bool:
    """O cabeçalho está nas primeiras linhas da página (a página 'abre' com ele)?"""
    top = dc.norm(" ".join(body_lines(text)[:4]))
    return dc.norm(h) in top


def anchor_for(seg: dict, nxt: dict | None, heads: dict[int, list[str]], pages: dict[int, str]) -> dict:
    sp, ep = seg["startPage"], seg["endPage"]
    # início
    on = heads.get(sp, [])
    top = next((h for h in on if at_top(h, pages.get(sp, ""))), None)
    if top:
        start = {"kind": "heading", "text": top}
    else:
        prev = [(p, h) for p in sorted(heads) if p < sp for h in heads[p]]
        if prev:
            start = {"kind": "inside", "text": prev[-1][1], "page": prev[-1][0]}
        else:
            o = opens_text(pages.get(sp, ""))
            start = {"kind": "opens", "text": o}
    # fim
    stop = None
    if not seg.get("endsTheory") and ep + 1 in pages:
        nh = heads.get(ep + 1, [])
        if nh:
            stop = {"kind": "heading", "text": nh[0]}
        else:
            last = [(p, h) for p in sorted(heads) if p <= ep for h in heads[p]]
            stop = {"kind": "inside", "text": last[-1][1] if last else None}
    return {"start": start, "stop": stop}


def printed_offset(aula_id: str, pages: dict[int, str]) -> int:
    """Número impresso = pág. do PDF + offset. Vale o que está impresso nas páginas (maioria); sem isso, o da estrutura."""
    votes: dict[int, int] = {}
    for pg, t in pages.items():
        lines = [x.strip() for x in (t or "").splitlines() if x.strip()]
        for n in {int(x) for x in lines[:2] + lines[-3:] if re.fullmatch(r"\d{1,4}", x)}:
            votes[n - pg] = votes.get(n - pg, 0) + 1
    if votes:
        off, c = max(votes.items(), key=lambda kv: kv[1])
        if c >= 0.4 * len(pages):
            return off
    return dc.aula_struct(aula_id).get("printedOffset") or 0


def build() -> dict:
    anchors: dict[str, dict] = {}
    for f in sorted(glob.glob(str(ROOT / "content" / "segments" / "*.json"))):
        segs = json.loads(Path(f).read_text(encoding="utf-8"))["segments"]
        by_aula: dict[str, list[dict]] = {}
        for s in segs:
            by_aula.setdefault(dc.aula_of(s["id"])["id"], []).append(s)
        for aid, lst in by_aula.items():
            pages = dc.base_pages(dc.aula_of(lst[0]["id"]))
            if not pages:
                continue
            heads = page_heads(aid, pages)
            off = 0 if dc.aula_of(lst[0]["id"])["authored"] else printed_offset(aid, pages)
            lst.sort(key=lambda s: s["startPage"])
            for i, s in enumerate(lst):
                a = anchor_for(s, lst[i + 1] if i + 1 < len(lst) else None, heads, pages)
                a.update(startPage=s["startPage"], endPage=s["endPage"], startPrinted=s["startPage"] + off, endPrinted=s["endPage"] + off)
                anchors[s["id"]] = a
    return anchors


def check(anchors: dict) -> list[str]:
    errs = []
    for sid, a in anchors.items():
        aula = dc.aula_of(sid)
        pages = dc.base_pages(aula)
        sp, ep = a["startPage"], a["endPage"]
        if not (1 <= sp <= ep <= max(pages)):
            errs.append(f"{sid}: páginas {sp}-{ep} fora da aula")
            continue
        st = a["start"]
        txt = dc.norm(st.get("text") or "")
        if not txt:
            errs.append(f"{sid}: início sem texto")
        elif st["kind"] in ("heading", "opens") and txt not in dc.norm(pages[sp]):
            errs.append(f"{sid}: “{st['text']}” não está na pág. {sp}")
        elif st["kind"] == "inside" and txt not in dc.norm(pages.get(st.get("page"), "")):
            errs.append(f"{sid}: “{st['text']}” não está na pág. {st.get('page')}")
        sp_ = a.get("stop")
        if sp_ and sp_["kind"] == "heading" and dc.norm(sp_["text"]) not in dc.norm(pages.get(ep + 1, "")):
            errs.append(f"{sid}: parada “{sp_['text']}” não está na pág. {ep + 1}")
    return errs


def main() -> int:
    anchors = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(anchors, ensure_ascii=False, indent=1), encoding="utf-8")
    mirror = ROOT / "web" / "content" / "directive"
    mirror.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(OUT, mirror / "anchors.json")
    kinds: dict[str, int] = {}
    for a in anchors.values():
        k = "start:" + a["start"]["kind"]
        kinds[k] = kinds.get(k, 0) + 1
        if a["stop"]:
            k = "stop:" + a["stop"]["kind"]
            kinds[k] = kinds.get(k, 0) + 1
    print(f"{len(anchors)} trechos · {kinds}")
    errs = check(anchors)
    print(f"conferência: {len(errs)} erro(s)")
    for e in errs[:40]:
        print(" ", e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
