"""Etapa M2a — Corpus de questões reais do material (Fonte A do guia de estilo AOCP).

Lê as seções de questões comentadas de cada aula e extrai cada item:
  banca, órgão, ano, tipo (mc5|mc4|ce), enunciado, alternativas, gabarito.

SAÍDA LOCAL (pipeline/.cache/corpus/questions.jsonl) — nunca versionada: contém texto de terceiros.
O que vai para o repositório são só as ESTATÍSTICAS e o guia de estilo (content/style/*.json|md).

Uso:  python pipeline/corpus.py
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, CONTENT_DIR  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

CORPUS_DIR = CACHE_DIR / "corpus"

TAG_RE = re.compile(r"^[ \t]*(?:(\d{1,3})[ \t]*[.)\-][ \t]*\n?[ \t]*)?\(\s*([^()\n]{3,120}?)\s*\)[ \t]*", re.MULTILINE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
BANCA_WORDS = re.compile(
    r"^(instituto\s+)?(aocp|cespe|cebraspe|fcc|fgv|vunesp|quadrix|ibfc|idecan|cesgranrio|fundatec|iades|ufrj|ufpe|puc|"
    r"enem|uerj|unifesp|ufmg|uel|ufrgs|fuvest|unicamp|consulplan|ibade|selecon|fumarc|nucepe|nc-ufpr|ufpr|ime|ita|epcar|"
    r"esa|eear|afa|efomm|escola naval|instituto americano|ceperj|inpi|upenet|funcab|legalle|gsa|objetiva|cetro|makiyama|"
    r"prof\.|professor|estrat[ée]gia|quest[ãa]o in[ée]dita)",
    re.IGNORECASE,
)
ALT_LINE = re.compile(r"^[ \t]*\(?([a-eA-E])\)[ \t]*(\S.*)?$")
GAB_RE = re.compile(
    r"(?:gabarito|resposta|resp\.?)\s*[:\-–]?\s*(?:letra|alternativa|item)?\s*[:\-–]?\s*([A-E]|certo|errado|anulad[ao])\b",
    re.IGNORECASE,
)
COMMENT_RE = re.compile(r"^\s*(coment[áa]rios?|resolu[çc][ãa]o|gabarito|resposta|resp\.)\b", re.IGNORECASE | re.MULTILINE)


def is_real_tag(tag: str) -> bool:
    t = tag.strip()
    if len(t) < 3 or len(t) > 120:
        return False
    if YEAR_RE.search(t) and re.search(r"[A-Za-zÀ-ÿ]{3,}", t):
        return True
    return bool(BANCA_WORDS.match(t))


def parse_tag(tag: str) -> dict:
    parts = [p.strip() for p in re.split(r"\s*[/–—-]\s*|\s+-\s+", tag) if p.strip()]
    year_m = YEAR_RE.search(tag)
    year = int(year_m.group(0)) if year_m else None
    banca = parts[0] if parts else tag
    banca_norm = re.sub(r"^instituto\s+", "", banca, flags=re.I).strip().upper()
    orgao = " / ".join(p for p in parts[1:] if not YEAR_RE.fullmatch(p))[:80]
    return {"banca": banca_norm, "orgao": orgao, "ano": year, "tag": tag}


def split_item(body: str) -> dict | None:
    """Separa enunciado, alternativas, gabarito e comentário do texto de um item."""
    lines = [ln.rstrip() for ln in body.splitlines()]
    first_alt = None
    expected = "a"
    alts: list[tuple[str, list[str]]] = []
    stmt: list[str] = []
    after: list[str] = []
    state = "stmt"
    for ln in lines:
        m = ALT_LINE.match(ln)
        if state in ("stmt", "alts") and m and m.group(1).lower() == expected:
            state = "alts"
            alts.append((m.group(1).lower(), [m.group(2) or ""]))
            expected = chr(ord(expected) + 1)
            continue
        if state == "alts":
            if COMMENT_RE.match(ln) or (not ln.strip() and False):
                state = "after"
                after.append(ln)
            elif ln.strip():
                alts[-1][1].append(ln.strip())
            continue
        if state == "after":
            after.append(ln)
        else:
            stmt.append(ln)
    tail = "\n".join(after) if after else ""
    if state == "stmt":  # sem alternativas: pode ser Certo/Errado
        full = "\n".join(lines)
        m = GAB_RE.search(full)
        if m and m.group(1).lower() in ("certo", "errado"):
            cut = full[: m.start()]
            cm = COMMENT_RE.search(cut)
            statement = (cut[: cm.start()] if cm else cut).strip()
            return {"kind": "ce", "statement": statement, "options": {}, "answer": m.group(1).upper(), "comment": cut[cm.start():].strip() if cm else ""}
        return None
    n = len(alts)
    if n < 4:
        return None
    options = {k: re.sub(r"\s+", " ", " ".join(v)).strip() for k, v in alts}
    gm = GAB_RE.search(tail or body)
    answer = gm.group(1).upper() if gm else None
    return {
        "kind": "mc5" if n >= 5 else "mc4",
        "statement": re.sub(r"[ \t]+", " ", "\n".join(stmt)).strip(),
        "options": options,
        "answer": answer,
        "comment": tail.strip(),
    }


_HDR = re.compile(r"^.{3,70}\sAula\s+\d+\s*$", re.MULTILINE)


def parse_run(text: str, meta: dict) -> list[dict]:
    text = _HDR.sub("", text)  # cabeçalhos "<Professor> Aula NN" que sobraram no meio do texto
    items = []
    matches = [m for m in TAG_RE.finditer(text) if is_real_tag(m.group(2))]
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end() : end]
        parsed = split_item(body)
        if not parsed:
            continue
        rec = {**meta, **parse_tag(m.group(2)), **parsed}
        items.append(rec)
    return items


def main() -> int:
    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    keys = aula_key_map()
    out_path = CORPUS_DIR / "questions.jsonl"
    total = 0
    by_banca: dict[str, int] = {}
    with out_path.open("w", encoding="utf-8") as fh:
        for subj_file in sorted((CONTENT_DIR / "structure").glob("*.json")):
            struct = json.loads(subj_file.read_text(encoding="utf-8"))
            for aula in struct["aulas"]:
                runs = aula["commentedRuns"]
                if not runs:
                    continue
                data = load_pages(keys[aula["id"]])
                for (s, e) in runs:
                    text = "\n".join(p["text"] for p in data["pages"][s - 1 : e])
                    for rec in parse_run(text, {"subject": struct["subject"], "aula": aula["id"], "pages": [s, e]}):
                        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                        total += 1
                        by_banca[rec["banca"]] = by_banca.get(rec["banca"], 0) + 1
    print(f"{total} questões -> {out_path}")
    print("top bancas:", sorted(by_banca.items(), key=lambda x: -x[1])[:12])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
