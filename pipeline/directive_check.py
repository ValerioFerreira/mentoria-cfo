"""Confere, nos PDFs, as diretrizes sorteadas por web/scripts/directive-audit.ts (material-base e material MentorIA).

Material-base (texto das páginas no cache do pipeline; complementos pelo PDF em web/public):
  Teoria/Turbo: páginas dentro da aula; o tópico inicial do trecho aparece na página inicial (ou antes, se o trecho começa no
  meio do tópico); o tópico em que parar aparece na página final ou na seguinte.
  Fixação: cada intervalo está dentro das questões comentadas (ou das listas de prática) da aula indicada.
  Revisão: os trechos revistos existem e têm páginas válidas.
Material MentorIA (texto das páginas do PDF do volume):
  Teoria/Turbo: a página inicial traz "CAPÍTULO N" e o título; o "Mapa do capítulo" está na página indicada e antes do fim.
  Revisão: a página do mapa traz "MAPA DO CAPÍTULO"; a do Mapa de revisão traz o título do capítulo.
  Fixação: a página das questões traz o grupo "CAPÍTULO N ·".
Relatório: taxa de erro com intervalo de 95% (Clopper-Pearson) e a lista dos erros.

Uso: python pipeline/directive_check.py pipeline/.cache/directive-audit/amostra-local.json
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
from scipy.stats import beta

sys.path.insert(0, str(Path(__file__).parent))
from config import CONTENT_DIR  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = CONTENT_DIR.parent


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def found(needle: str, hay: str) -> bool:
    needle = re.sub(r"\s*[-–]\s*teoria\s*$|\([^)]*\)", " ", needle or "", flags=re.I)
    n, h = norm(needle), norm(hay)
    if not n:
        return True
    words = n.split()
    if " ".join(words[:5]) in h:
        return True
    key = [w for w in words if len(w) >= 4]
    return bool(key) and sum(w in h for w in key) / len(key) >= 0.6


_structure: dict[str, dict] = {}
_base_pages: dict[str, dict[int, str]] = {}
_keys: dict[str, str] | None = None
_pdf_pages: dict[str, list[str]] = {}


_catalog: dict[str, dict] = {}


def catalog_aula(aula_id: str) -> dict:
    if not _catalog:
        cat = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
        _catalog.update({a["id"]: a for s in cat["subjects"] for a in s["aulas"]})
    return _catalog.get(aula_id, {})


def aula_of(seg_id: str) -> dict:
    aid = "/".join(seg_id.split("/")[:2])
    c = catalog_aula(aid)
    return {"id": aid, "authored": bool(c.get("materialPath")), "materialPath": c.get("materialPath")}


def aula_struct(aula_id: str) -> dict:
    subj = aula_id.split("/")[0]
    if subj not in _structure:
        f = CONTENT_DIR / "structure" / f"{subj}.json"
        _structure[subj] = {a["id"]: a for a in json.loads(f.read_text(encoding="utf-8"))["aulas"]} if f.exists() else {}
    return _structure[subj].get(aula_id, {})


def pdf_pages(path: Path) -> list[str]:
    k = str(path)
    if k not in _pdf_pages:
        _pdf_pages[k] = [p.get_text() for p in pymupdf.open(path)] if path.exists() else []
    return _pdf_pages[k]


def base_pages(aula: dict) -> dict[int, str]:
    global _keys
    if aula["id"] in _base_pages:
        return _base_pages[aula["id"]]
    if aula.get("authored") and aula.get("materialPath"):
        pages = {i + 1: t for i, t in enumerate(pdf_pages(ROOT / "web" / "public" / aula["materialPath"]))}
    else:
        _keys = _keys or aula_key_map()
        key = _keys.get(aula["id"])
        pages = {p["n"]: p["text"] for p in load_pages(key)["pages"]} if key else {}
    _base_pages[aula["id"]] = pages
    return pages


def check_base(u: dict) -> list[str]:
    errs = []
    aula = u["aula"]
    if u["type"] == "FIXACAO":
        for r in u.get("fixRanges") or []:
            src = catalog_aula(r.get("sourceAula") or aula["id"]) or aula_struct(r.get("sourceAula") or aula["id"])
            runs = (src.get("commentedRuns") or []) + [[p["startPage"], p["endPage"]] for p in catalog_aula(aula["id"]).get("practiceLinks") or []
                                                     if isinstance(p, dict) and "startPage" in p]
            if not any(a <= r["start"] and r["end"] <= b for a, b in runs):
                errs.append(f"Fixação págs. {r['start']}-{r['end']} fora das questões comentadas ({runs})")
        return errs
    for s in u["segments"]:
        pages = base_pages(aula_of(s["id"]))
        if not pages:
            errs.append(f"sem o texto das páginas de {aula_of(s['id'])['id']}")
            continue
        total = max(pages)
        if not (1 <= s["startPage"] <= s["endPage"] <= total):
            errs.append(f"{s['id']}: págs. {s['startPage']}-{s['endPage']} fora da aula ({total} págs.)")
            continue
        if u["type"] == "REVISAO":
            continue
        sp, ep = s["startPage"], s["endPage"]
        contains = lambda txt, pg: bool(norm(txt)) and norm(txt) in norm(pages.get(pg, ""))  # noqa: E731
        if s.get("startOpening"):
            if not contains(s["startOpening"], sp):
                errs.append(f"{s['id']}: a pág. {sp} não abre com “{s['startOpening'][:60]}”")
        elif s.get("startTopic"):
            window = range(max(1, sp - 80), sp + 1) if s.get("startsMidTopic") else [sp]
            if not any(contains(s["startTopic"], p) for p in window):
                errs.append(f"{s['id']}: tópico “{s['startTopic'][:60]}” não aparece na pág. {sp}" + (" nem antes" if s.get("startsMidTopic") else ""))
        if s.get("stopBeforeTopic") and not contains(s["stopBeforeTopic"], ep + 1):
            errs.append(f"{s['id']}: tópico de parada “{s['stopBeforeTopic'][:60]}” não aparece na pág. {ep + 1}")
        if s.get("endsMidTopic") and s.get("endTopic") and not any(contains(s["endTopic"], p) for p in range(max(1, sp - 80), ep + 1)):
            errs.append(f"{s['id']}: tópico “{s['endTopic'][:60]}” (onde o trecho termina) não aparece até a pág. {ep}")
        # a diretriz exibida cita exatamente esses textos e esses números de página
        shown = " ".join(u.get("directive") or [])
        for fld in ("startOpening", "startTopic", "stopBeforeTopic"):
            if s.get(fld) and u["type"] == "TEORIA" and not u.get("turbo") and f"“{s[fld].strip()}”" not in shown:
                errs.append(f"{s['id']}: a diretriz exibida não cita {fld} “{s[fld][:40]}”")
        if u["type"] == "TEORIA" and not u.get("turbo") and not re.search(rf"pág\. {sp}(?!\d)", shown):
            errs.append(f"{s['id']}: a diretriz exibida não cita a pág. {sp}")
    return errs


def check_mentoria(u: dict) -> list[str]:
    errs = []
    for c in u["chapters"]:
        pdf = ROOT / "material-pdf" / f"{c['volumeId']}.pdf"
        pages = pdf_pages(pdf)
        if not pages:
            return [f"PDF {c['volumeId']} não encontrado"]
        get = lambda p: pages[p - 1] if p and 1 <= p <= len(pages) else ""  # noqa: E731
        if u["type"] == "FIXACAO":
            if not c.get("questions"):
                continue
            if f"capitulo {c['chapter']} " not in norm(get(c["questions"]["pagina"])) + " ":
                errs.append(f"{c['trecho']}: pág. {c['questions']['pagina']} sem as questões do capítulo {c['chapter']}")
            continue
        if u["type"] in ("TEORIA",):
            t = get(c["start"])
            if f"capitulo {c['chapter']}" not in norm(t) or not found(c["title"], t):
                errs.append(f"{c['trecho']}: pág. {c['start']} não abre o capítulo {c['chapter']} “{c['title'][:50]}”")
            if c.get("mapPage") and not (c["start"] <= c["mapPage"] <= c["end"]):
                errs.append(f"{c['trecho']}: Mapa do capítulo (pág. {c['mapPage']}) fora das págs. {c['start']}-{c['end']}")
        if c.get("mapPage") and "mapa do capitulo" not in norm(get(c["mapPage"])):
            errs.append(f"{c['trecho']}: pág. {c['mapPage']} sem o Mapa do capítulo")
        if u["type"] == "REVISAO" and c.get("reviewPage") and not found(c["title"], get(c["reviewPage"])):
            errs.append(f"{c['trecho']}: pág. {c['reviewPage']} do Mapa de revisão sem o capítulo “{c['title'][:50]}”")
    return errs


def main() -> int:
    f = Path(sys.argv[1])
    d = json.loads(f.read_text(encoding="utf-8"))
    res = []
    for u in d["amostra"]:
        errs = check_base(u) if u["material"] == "base" else check_mentoria(u)
        res.append((u, errs))
    k = sum(1 for _, e in res if e)
    n = len(res)
    lo = beta.ppf(0.025, k, n - k + 1) if k else 0.0
    hi = beta.ppf(0.975, k + 1, n - k) if k < n else 1.0
    by = defaultdict(lambda: [0, 0])
    for u, e in res:
        by[u["stratum"]][0] += 1
        by[u["stratum"]][1] += bool(e)
    lines = [f"# Conferência amostral das diretrizes — {f.name}", "",
             f"População N = {d['N']} diretrizes · amostra n = {n} (95% de confiança, ±5%) · com erro: {k} "
             f"({k / n:.1%}; IC 95% Clopper-Pearson: {lo:.1%} a {hi:.1%})", "", "| Estrato | Amostra | Com erro |", "|---|---|---|"]
    lines += [f"| {s} | {v[0]} | {v[1]} |" for s, v in sorted(by.items())]
    lines += ["", "## Erros", ""]
    for u, e in res:
        for x in e:
            lines.append(f"- [{u['stratum']}] atividade {u['activity']} ({u['aula']['id']}): {x}")
    reasons = Counter(re.sub(r"\d+", "#", x.split(": ", 1)[-1])[:60] for _, e in res for x in e)
    lines += ["", "## Tipos de erro", ""] + [f"- {n_}× {r}" for r, n_ in reasons.most_common(10)]
    out = f.with_suffix(".relatorio.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12 + len(by)]))
    print(f"relatório: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
