"""Etapa 3 — Valida e corrige as páginas do índice .xlsx contra o texto real dos PDFs.

Para cada tópico procura, numa janela de ±3 páginas em torno da página do índice, uma linha que
seja o cabeçalho do tópico. Achando em outra página, corrige a página; não achando, mantém e marca
`verified=False` (vai para a fila de revisão manual).

Entrada : pipeline/.cache/index.json  (xlsx_index.py) + pipeline/.cache/pages/*.json (extract.py)
Saída   : pipeline/.cache/index_validated.json  e  pipeline/.cache/reports/index_validation.md
"""
from __future__ import annotations

import collections
import json
import os
import re
import sys
import unicodedata
from statistics import mode

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, INDEX_JSON  # noqa: E402
from textutil import END_MARKER, aula_key_map, load_pages, norm  # noqa: E402

VALIDATED_JSON = CACHE_DIR / "index_validated.json"
REPORT_MD = CACHE_DIR / "reports" / "index_validation.md"
WINDOW = 3

# classe do marcador -> prefixo normalizado esperado numa linha de cabeçalho
MARKER_CLASSES = [
    ("questoescomentadas", ("questoescomentadas", "questoesparafixacao", "provacomentada", "resolucaode", "questoes")),
    ("listadequestoes", ("listadequestoes", "questoessemcomentarios", "listadeexercicios", "listadeques", "questoes")),
    ("gabarito", ("gabarito",)),
    ("resumo", ("resumo",)),
    ("mapamental", ("mapamental", "mapasmentais")),
    ("formulas", ("formulas",)),
    ("vocabulario", ("quadrosdevocabulario", "quadrodevocabulario", "vocabulario")),
]


def marker_class(title: str) -> tuple[str, ...] | None:
    t = norm(title)
    for cls, prefixes in MARKER_CLASSES:
        if cls in t:
            return prefixes
    return None


def page_candidates(text: str) -> list[str]:
    """Strings normalizadas de 1–3 linhas consecutivas (cabeçalhos podem quebrar em várias linhas)."""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    out: list[str] = []
    for i in range(len(lines)):
        acc = ""
        for j in range(i, min(i + 3, len(lines))):
            acc += lines[j]
            c = norm(acc)
            if c:
                out.append(c)
    return out


def heading_on_page(cands: list[str], title_norm: str) -> bool:
    t = title_norm
    for c in cands:
        extra = len(c) - len(t)
        if c == t:
            return True
        if 0 < extra <= 8 and c.endswith(t):  # prefixo de numeração: "3.1. Título"
            return True
        if 0 < extra <= 10 and c.startswith(t):
            return True
        if len(t) > 30 and extra <= 12 and t[:30] in c and len(c) <= len(t) + 12:
            return True
    return False


_STOP = {"de", "do", "da", "dos", "das", "e", "o", "a", "os", "as", "em", "no", "na", "nos", "nas", "um", "uma",
         "para", "por", "com", "ao", "aos", "sobre", "ou", "que", "se", "ii", "i"}


def stems(s: str) -> set[str]:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    out = set()
    for w in re.findall(r"[a-z0-9]+", s):
        if w in _STOP:
            continue
        out.add(w[:5] if len(w) > 5 else (w[:-1] if w.endswith("s") and len(w) > 3 else w))
    return out


def fuzzy_heading_on_page(text: str, title: str) -> bool:
    """Cabeçalho do corpo com redação diferente da do sumário (ex.: 'Mérito do ato administrativo')."""
    ts = stems(title)
    if len(ts) < 2:
        return False
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for i in range(len(lines)):
        for span in (1, 2):
            chunk = " ".join(lines[i : i + span])
            if len(chunk) > len(title) + 30:
                continue
            ls = stems(chunk)
            if ls and len(ts & ls) / len(ts) >= 0.75 and len(ls) <= len(ts) + 3:
                return True
    return False


def marker_on_page(text: str, prefixes: tuple[str, ...]) -> bool:
    for ln in text.splitlines():
        s = ln.strip()
        if 0 < len(s) <= 90:
            n = norm(s)
            if any(n.startswith(p) for p in prefixes):
                return True
    return False


def parse_toc_pages(s: str) -> int:
    nums = [int(x) for x in re.findall(r"\d+", s or "")]
    return max(nums) if nums else 1


def validate_aula(topics: list[dict], pages: list[dict], toc_max: int) -> None:
    cand_cache: dict[int, list[str]] = {}

    def cands(n: int) -> list[str]:
        if n not in cand_cache:
            cand_cache[n] = page_candidates(pages[n - 1]["text"])
        return cand_cache[n]

    for t in topics:
        p0 = t["pdfPage"]
        t["indexPage"] = p0
        t["verified"] = False
        t["delta"] = None
        t["kind"] = "marker" if END_MARKER.search(t["title"]) else "heading"
        window = [p for p in sorted(range(p0 - WINDOW, p0 + WINDOW + 1), key=lambda p: (abs(p - p0), p))
                  if toc_max < p <= len(pages)]
        found = None
        pref = marker_class(t["title"]) if t["kind"] == "marker" else None
        if pref is not None:
            for p in window:
                if abs(p - p0) <= 2 and marker_on_page(pages[p - 1]["text"], pref):
                    found = p
                    break
        else:
            tn = norm(re.sub(r"\s*[-–]\s*(AOCP|FCC|CEBRASPE|CESPE|FGV|VUNESP|multibancas?)\s*$", "", t["title"], flags=re.I))
            if len(tn) >= 5:
                for p in window:
                    if heading_on_page(cands(p), tn):
                        found = p
                        break
                if found is None:
                    for p in window:
                        if fuzzy_heading_on_page(pages[p - 1]["text"], t["title"]):
                            found = p
                            break
        if found is not None:
            t["verified"] = True
            t["delta"] = found - p0
            t["pdfPage"] = found


def main() -> int:
    idx = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    keys = aula_key_map()
    cov = {c["aula"]: c for c in idx["coverage"]}
    by_aula: dict[str, list[dict]] = collections.defaultdict(list)
    for t in idx["topics"]:
        by_aula[t["aula"]].append(t)

    stats: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    unverified: list[dict] = []
    offsets: dict[str, int] = {}
    for aula, topics in by_aula.items():
        if aula not in keys:
            print(f"[aviso] sem cache de páginas para {aula}")
            continue
        data = load_pages(keys[aula])
        validate_aula(topics, data["pages"], parse_toc_pages(cov.get(aula, {}).get("tocPages", "")))
        subj = topics[0]["subject"]
        for t in topics:
            stats[subj]["n"] += 1
            if t["verified"]:
                stats[subj]["ok_exact" if t["delta"] == 0 else "corrected"] += 1
            else:
                stats[subj]["unverified"] += 1
                unverified.append({"aula": aula, "title": t["title"], "page": t["indexPage"], "kind": t["kind"]})
        diffs = [t["printedPage"] - t["pdfPage"] for t in topics if t["verified"] and t.get("printedPage") is not None]
        offsets[aula] = mode(diffs) if diffs else 0

    out = {"topics": [t for ts in by_aula.values() for t in ts], "coverage": idx["coverage"], "printedOffset": offsets}
    VALIDATED_JSON.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Validação do índice", "", "| Disciplina | Tópicos | Página exata | Corrigidos (±3) | Não localizados |", "|---|---|---|---|---|"]
    tot = collections.Counter()
    for s, c in sorted(stats.items()):
        lines.append(f"| {s} | {c['n']} | {c['ok_exact']} | {c['corrected']} | {c['unverified']} |")
        tot.update(c)
    lines.append(f"| **TOTAL** | {tot['n']} | {tot['ok_exact']} | {tot['corrected']} | {tot['unverified']} |")
    lines += ["", "## Não localizados (amostra por aula)", ""]
    per_aula = collections.defaultdict(list)
    for u in unverified:
        per_aula[u["aula"]].append(u)
    for a, us in sorted(per_aula.items()):
        lines.append(f"- **{a}** — {len(us)}: " + "; ".join(f"{u['title'][:40]} (p.{u['page']})" for u in us[:4]))
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    pct = lambda k: 100 * tot[k] / max(tot["n"], 1)  # noqa: E731
    print(f"{tot['n']} tópicos: exatos {pct('ok_exact'):.1f}% | corrigidos {pct('corrected'):.1f}% | não localizados {pct('unverified'):.1f}%")
    print(f"relatório: {REPORT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
