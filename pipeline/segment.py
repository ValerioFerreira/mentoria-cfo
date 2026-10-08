"""Etapa 4 — Estrutura das aulas e segmentação da teoria em trechos de ~1 h.

1) Classifica cada página da aula: THEORY | COMMENTED | LIST | SUMMARY | KEY (gabarito) | FRONT (sumário/abertura).
2) Corta cada trecho contínuo de teoria em segmentos de 10–17 págs. (teto 17), preferindo cortar
   no início de tópico do índice e equilibrando a CARGA (páginas ponderadas pela densidade de texto).

Entrada : pipeline/.cache/index_validated.json + pipeline/.cache/pages/*.json
Saída   : content/structure/<disciplina>.json  e  content/segments/<disciplina>.json
          pipeline/.cache/reports/segments.md
"""
from __future__ import annotations

import collections
import json
import os
import re
import sys
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, CONTENT_DIR, load_subjects  # noqa: E402
from index_validate import stems  # noqa: E402
from textutil import COMMENTED_MARKER, FRONTMATTER, aula_key_map, load_pages, norm  # noqa: E402

VALIDATED_JSON = CACHE_DIR / "index_validated.json"
REPORT_MD = CACHE_DIR / "reports" / "segments.md"
HEADINGS_DIR = CACHE_DIR / "headings"

TARGET_LOAD = 12.0
MAX_PAGES = 17
MIN_PAGES = 6
CHARS_PER_PAGE_REF = 2200.0
DENSITY_FACTOR = {
    "informatica": 1.25, "matematica": 1.25, "fisica": 1.25,
    "estatistica": 1.2, "quimica": 1.15, "biologia": 1.1,
}

# Falsos cabeçalhos: tags de banca "(CESPE / ÓRGÃO / 2010)", "Texto 2", legendas.
BAD_HEAD = re.compile(r"^\s*\d*\s*[.)]?\s*\(|(19|20)\d\d|^texto\s*\d|^quest[ãõ]|^figura|^tabela|^quadro|^gabarito", re.IGNORECASE)

# Seções de fechamento da aula (tudo depois delas, até o próximo marcador explícito, não é teoria).
BACK = re.compile(r"^(palavras finais|considera[çc][õo]es finais|ap[êe]ndice|bibliografia|refer[êe]ncias)", re.IGNORECASE)
ALT_LINE = re.compile(r"^\s*\(?[a-eA-E]\)\s", re.MULTILINE)

# Marcadores detectados pelo texto quando o índice não os traz.
TEXT_MARKER = re.compile(r"^(quest[õo]es|lista de quest|gabarito|resumo|prova comentada)", re.IGNORECASE)


# ───────────────────────── classificação de páginas ─────────────────────────

def marker_type(title: str) -> str:
    t = norm(title)
    if COMMENTED_MARKER.search(title) or ("comentad" in t and "quest" in t) or "questoesparafixacao" in t:
        return "COMMENTED"
    if "gabarito" in t:
        return "KEY"
    if "lista" in t or "semcomentario" in t or "propost" in t:
        return "LIST"
    return "SUMMARY"  # resumo, mapa mental, fórmulas, vocabulário…


def classify_pages(topics: list[dict], pages: list[dict], toc_max: int) -> tuple[list[str], list[str]]:
    """Retorna (tipo por página [índice 0 = pág. 1], flags)."""
    n = len(pages)
    flags: list[str] = []
    ev = []  # (página, ordem, tipo)
    for order, t in enumerate(topics):
        if BACK.match(t["title"]):
            typ = "BACK"
        else:
            typ = marker_type(t["title"]) if t["kind"] == "marker" else "THEORY"
        ev.append((t["pdfPage"], order, typ))

    if not any(t["kind"] == "marker" for t in topics):
        # sem marcadores no índice: tenta achar cabeçalhos de seção no texto
        for p in range(toc_max + 2, n + 1):
            head = " ".join(pages[p - 1]["text"].splitlines()[:3])
            if TEXT_MARKER.match(head.strip()):
                ev.append((p, 10_000 + p, marker_type(head)))
                flags.append(f"marcador detectado no texto (pág. {p})")
                break
        else:
            flags.append("sem marcadores de fim de teoria")

    ev.sort()
    types = ["FRONT"] * n
    cur = "THEORY"
    j = 0
    for p in range(1, n + 1):
        while j < len(ev) and ev[j][0] <= p:
            # após "Apêndice/Bibliografia…" só um marcador explícito reabre outra seção
            if not (cur == "BACK" and ev[j][2] == "THEORY"):
                cur = ev[j][2]
            j += 1
        types[p - 1] = "FRONT" if p <= toc_max else cur

    trim_trailing_questions(types, pages, flags)

    # abertura/frontmatter antes do 1º tópico de conteúdo
    heads = [t for t in topics if t["kind"] == "heading" and t["pdfPage"] > toc_max]
    first_content = next((t for t in heads if not FRONTMATTER.match(t["title"])), None)
    if first_content is not None:
        for p in range(toc_max + 1, first_content["pdfPage"]):
            if types[p - 1] == "THEORY":
                types[p - 1] = "FRONT"
    return types, flags


def trim_trailing_questions(types: list[str], pages: list[dict], flags: list[str]) -> None:
    """Sem seção de questões no índice: reclassifica como COMMENTED o bloco final de páginas cheias de alternativas."""
    th = runs_of(types, "THEORY")
    if not th:
        return
    last_s, last_e = th[-1]
    if any(t in ("COMMENTED", "LIST") for t in types[last_e:]):
        return  # já existe seção de questões explícita depois da teoria
    q = [len(ALT_LINE.findall(pages[p - 1]["text"])) >= 3 for p in range(1, len(pages) + 1)]
    start, gap, p = None, 0, last_e
    while p >= last_s:
        if q[p - 1]:
            start, gap = p, 0
        elif gap < 1 and len(pages[p - 1]["text"]) < 400:
            gap += 1
        else:
            break
        p -= 1
    if start is not None and sum(q[start - 1 : last_e]) >= 3:
        for i in range(start, last_e + 1):
            types[i - 1] = "COMMENTED"
        flags.append(f"exercícios finais detectados pelo texto (págs. {start}–{last_e})")


def runs_of(types: list[str], kind: str) -> list[tuple[int, int]]:
    out, start = [], None
    for i, t in enumerate(types, 1):
        if t == kind and start is None:
            start = i
        if t != kind and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(types)))
    return out


# ───────────────────────── partição (programação dinâmica) ─────────────────────────

def partition_run(weights: list[float], cut_penalty: list[float]) -> list[tuple[int, int]]:
    """Divide uma sequência de páginas em segmentos [i, j) minimizando o desvio da carga-alvo.

    weights[k]      : carga da página k (k = 0..m-1)
    cut_penalty[k]  : custo de iniciar um novo segmento na página k (k = 1..m-1); 0 = início de tópico.
    Restrições: 1..MAX_PAGES págs. por segmento. Retorna lista de (início, fim_exclusivo) em índices.
    """
    m = len(weights)
    prefix = [0.0]
    for w in weights:
        prefix.append(prefix[-1] + w)
    INF = float("inf")
    dp = [INF] * (m + 1)
    prev = [-1] * (m + 1)
    dp[0] = 0.0
    for j in range(1, m + 1):
        for i in range(max(0, j - MAX_PAGES), j):
            if dp[i] == INF:
                continue
            load = prefix[j] - prefix[i]
            pages = j - i
            cost = (load - TARGET_LOAD) ** 2
            if pages < MIN_PAGES:
                cost += 30 + 4 * (MIN_PAGES - pages)
            if j < m:
                cost += cut_penalty[j] * 3.0
            c = dp[i] + cost
            if c < dp[j]:
                dp[j], prev[j] = c, i
    segs, j = [], m
    while j > 0:
        i = prev[j]
        segs.append((i, j))
        j = i
    return segs[::-1]


# ───────────────────────── montagem por aula ─────────────────────────

def page_weight(chars: int, factor: float) -> float:
    return min(max(chars / CHARS_PER_PAGE_REF, 0.5), 1.3) * factor


def auto_headings(key: str, index_topics: list[dict], types: list[str]) -> list[dict]:
    """Subtítulos detectados por fonte que ainda não estão no índice (mesma página ±1 e radicais parecidos)."""
    path = HEADINGS_DIR / f"{key}.json"
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))["headings"]
    sizes = sorted({h["size"] for h in raw}, reverse=True)
    index_stems = [(t["pdfPage"], stems(t["title"])) for t in index_topics if t["kind"] == "heading"]
    out = []
    for h in raw:
        if h["page"] > len(types) or types[h["page"] - 1] != "THEORY":
            continue
        hs = stems(h["text"])
        if not hs or BAD_HEAD.search(h["text"]):
            continue
        dup = any(abs(pg - h["page"]) <= 1 and len(hs & st) / max(len(hs), 1) >= 0.75 for pg, st in index_stems)
        if dup:
            continue
        level = 2 if sizes and h["size"] == sizes[0] else 3
        out.append({"level": level, "title": h["text"], "pdfPage": h["page"], "printedPage": None,
                    "kind": "heading", "verified": True, "auto": True})
    return out


def build_aula(aula_id: str, topics: list[dict], data: dict, coverage: dict, printed_offset: int) -> tuple[dict, list[dict]]:
    pages = data["pages"]
    subject = data["subject"]
    toc_max = max([int(x) for x in re.findall(r"\d+", coverage.get("tocPages", "") or "")] or [1])
    topics = sorted(topics, key=lambda t: (t["pdfPage"], t["title"]))
    types, flags = classify_pages(topics, pages, toc_max)
    factor = DENSITY_FACTOR.get(subject, 1.0)

    topics = topics + auto_headings(data["key"], topics, types)
    heading_by_page: dict[int, dict] = {}
    for t in topics:
        if t["kind"] == "heading" and t["pdfPage"] > toc_max and types[t["pdfPage"] - 1] == "THEORY":
            cur = heading_by_page.get(t["pdfPage"])
            if cur is None or t["level"] < cur["level"]:
                heading_by_page[t["pdfPage"]] = t

    def active_topic(p: int) -> dict | None:
        best = None
        for hp, t in heading_by_page.items():
            if hp <= p and (best is None or hp > best["pdfPage"]):
                best = t
        return best

    segments: list[dict] = []
    order = 0
    theory_runs = runs_of(types, "THEORY")
    for (rs, re_) in theory_runs:
        idx = list(range(rs, re_ + 1))
        w = [page_weight(pages[p - 1]["chars"], factor) for p in idx]
        pen = []
        for k, p in enumerate(idx):
            t = heading_by_page.get(p)
            pen.append(8.0 if t is None else (0.0 if t["level"] == 1 else 1.0 if t["level"] == 2 else 2.0))
        for (i, j) in partition_run(w, pen):
            order += 1
            s_pg, e_pg = idx[i], idx[j - 1]
            st = heading_by_page.get(s_pg)
            start_mid = st is None
            start_t = st or active_topic(s_pg)
            nxt = heading_by_page.get(idx[j]) if j < len(idx) else None
            ends_run = j >= len(idx)
            end_mid = (not ends_run) and nxt is None
            end_t = active_topic(e_pg)
            covered = [t["title"] for hp, t in sorted(heading_by_page.items()) if s_pg <= hp <= e_pg][:10]
            segments.append({
                "id": f"{aula_id}/s{order:02d}",
                "aula": aula_id,
                "order": order,
                "startPage": s_pg,
                "endPage": e_pg,
                "startPrinted": s_pg + printed_offset,
                "endPrinted": e_pg + printed_offset,
                "pages": e_pg - s_pg + 1,
                "load": round(sum(w[i:j]), 2),
                "startTopic": start_t["title"] if start_t else None,
                "startsMidTopic": start_mid,
                "stopBeforeTopic": nxt["title"] if nxt else None,
                "endsMidTopic": end_mid,
                "endTopic": end_t["title"] if end_t else None,
                "endsTheory": ends_run and rs == theory_runs[-1][0],
                "topicsCovered": covered,
                "minutes": 60,
            })

    commented = runs_of(types, "COMMENTED")
    theory_pages = sum(e - s + 1 for s, e in theory_runs)
    if theory_pages == 0:
        flags.append("sem páginas de teoria")
    aula = {
        "id": aula_id,
        "number": data["aulaNumber"],
        "file": data["file"],
        "totalPages": len(pages),
        "tocMax": toc_max,
        "printedOffset": printed_offset,
        "theoryRuns": [list(r) for r in theory_runs],
        "theoryPages": theory_pages,
        "commentedRuns": [list(r) for r in commented],
        "commentedPages": sum(e - s + 1 for s, e in commented),
        "listPages": sum(e - s + 1 for s, e in runs_of(types, "LIST")),
        "segments": len(segments),
        "flags": flags,
        "topics": [
            {"level": t["level"], "title": t["title"], "pdfPage": t["pdfPage"], "printedPage": t.get("printedPage"),
             "kind": t["kind"], "verified": t["verified"], **({"auto": True} if t.get("auto") else {})}
            for t in topics
        ],
    }
    return aula, segments


def main() -> int:
    idx = json.loads(VALIDATED_JSON.read_text(encoding="utf-8"))
    keys = aula_key_map()
    cov = {c["aula"]: c for c in idx["coverage"]}
    by_aula: dict[str, list[dict]] = collections.defaultdict(list)
    for t in idx["topics"]:
        by_aula[t["aula"]].append(t)

    out_struct = CONTENT_DIR / "structure"
    out_seg = CONTENT_DIR / "segments"
    out_struct.mkdir(parents=True, exist_ok=True)
    out_seg.mkdir(parents=True, exist_ok=True)

    report = ["# Segmentação", ""]
    report.append("| Disciplina | Aulas | Pág. teoria | Segmentos | Pág./seg (mín–méd–máx) | Cortes no meio de tópico | Aulas com alerta |")
    report.append("|---|---|---|---|---|---|---|")
    problems: list[str] = []
    for subj in sorted(load_subjects(), key=lambda s: s.sort_order):
        aulas, segs = [], []
        for aula_id in sorted(a for a in keys if a.startswith(subj.id + "/")):
            data = load_pages(keys[aula_id])
            a, s = build_aula(aula_id, by_aula.get(aula_id, []), data, cov.get(aula_id, {}), idx["printedOffset"].get(aula_id, 0))
            a["title"] = re.sub(r"^\d{3}\s*-\s*Aula\s+\d+\s*", "", data["file"]).removesuffix(".pdf").strip()
            aulas.append(a)
            segs.extend(s)
        (out_struct / f"{subj.id}.json").write_text(json.dumps({"subject": subj.id, "aulas": aulas}, ensure_ascii=False, indent=1), encoding="utf-8")
        (out_seg / f"{subj.id}.json").write_text(json.dumps({"subject": subj.id, "segments": segs}, ensure_ascii=False, indent=1), encoding="utf-8")
        pg = [s["pages"] for s in segs] or [0]
        mid = sum(1 for s in segs if s["endsMidTopic"])
        flagged = [a["id"].split("/")[1] for a in aulas if a["flags"]]
        report.append(
            f"| {subj.id} | {len(aulas)} | {sum(a['theoryPages'] for a in aulas)} | {len(segs)} | "
            f"{min(pg)}–{sum(pg)/len(pg):.1f}–{max(pg)} | {mid} | {', '.join(flagged) or '—'} |"
        )
        problems += [f"{s['id']}: {s['pages']} págs. (> {MAX_PAGES})" for s in segs if s["pages"] > MAX_PAGES]
    report += ["", f"Violações do teto de {MAX_PAGES} págs.: {len(problems)}"] + [f"- {p}" for p in problems]
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
