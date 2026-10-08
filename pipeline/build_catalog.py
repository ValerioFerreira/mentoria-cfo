"""Etapa 5 — Consolida estrutura + segmentos + overrides em content/catalog.json (entrada do planejador e do seed).

content/catalog.json
  exam, subjects[{...,aulas:[...]}], gaps[...]
Cada aula: id, number, title, shortTitle, kind, edital, theoryPages, segmentCount, commentedPages, listPages,
           commentedRuns, practiceLinks, incidence, estimates{teoriaH, fixacaoH}
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, load_overrides, load_subjects  # noqa: E402
from textutil import FRONTMATTER, norm  # noqa: E402

PAGES_PER_FIXACAO_HOUR = 12


def clean_title(raw: str) -> str:
    t = re.sub(r"\s+", " ", raw.replace("_ ", ": ").replace("_", ":")).strip().rstrip(".")
    return t


def short_title(title: str, topics: list[dict]) -> str:
    if len(title) <= 70 and ";" not in title and not re.match(r"^\d+(\.\d+)*\.?\s", title):
        return title
    heads = []
    for t in topics:
        if t["kind"] != "heading" or t["level"] != 1 or t.get("auto") or FRONTMATTER.match(t["title"]):
            continue
        name = re.sub(r"\s*[-–]\s*teoria\s*$", "", t["title"], flags=re.I).strip()
        if name and name not in heads:
            heads.append(name)
    if heads:
        s = " · ".join(heads[:3])
        return s if len(s) <= 90 else s[:87].rstrip() + "…"
    return title[:70].rstrip() + "…"


def practice_sections(aula: dict, mapping: dict[str, str]) -> list[dict]:
    """Seções 'Questões Comentadas - <tema>' de uma aula de prática, ligadas à aula de teoria correspondente."""
    markers = sorted(
        (t for t in aula["topics"] if t["kind"] == "marker" and not t.get("auto")), key=lambda t: t["pdfPage"]
    )
    out = []
    commented_themes = {norm(re.sub(r"^quest[õo]es comentadas\s*[-–]\s*", "", m["title"], flags=re.I))
                        for m in markers if re.match(r"^quest[õo]es comentadas", m["title"], re.I)}
    for i, m in enumerate(markers):
        if re.match(r"^quest[õo]es comentadas", m["title"], re.I):
            theme = re.sub(r"^quest[õo]es comentadas\s*[-–]\s*", "", m["title"], flags=re.I).strip()
        elif re.match(r"^lista de quest[õo]es", m["title"], re.I):
            # tema que só existe como lista (ex.: Compreensão textual na Aula 14 de Português): a lista vira a Fixação
            theme = re.sub(r"^lista de quest[õo]es\s*[-–]\s*", "", m["title"], flags=re.I).strip()
            if norm(theme) in commented_themes:
                continue
        else:
            continue
        end = (markers[i + 1]["pdfPage"] - 1) if i + 1 < len(markers) else aula["totalPages"]
        target = next((v for k, v in mapping.items() if norm(k) == norm(theme)), None)
        out.append({"theme": theme, "startPage": m["pdfPage"], "endPage": end, "forAula": target})
    return out


def main() -> int:
    overrides = load_overrides()
    gaps_doc = json.loads((CONTENT_DIR / "gaps.json").read_text(encoding="utf-8"))
    gaps = gaps_doc["gaps"]
    completeness = {k: v for k, v in gaps_doc.get("materialCompleteness", {}).items() if not k.startswith("_")}
    exam = json.loads((CONTENT_DIR / "subjects.json").read_text(encoding="utf-8"))["exam"]

    subjects_out = []
    practice_links: dict[str, list[dict]] = {}
    for subj in sorted(load_subjects(), key=lambda s: s.sort_order):
        struct = json.loads((CONTENT_DIR / "structure" / f"{subj.id}.json").read_text(encoding="utf-8"))["aulas"]
        aulas = []
        for a in struct:
            if a.get("source") == "authored":  # complementos: build_complements.py mescla depois (idempotente)
                continue
            ov = overrides.get(a["id"], {})
            title = clean_title(a["title"])
            kind = ov.get("kind") or ("practice" if a["theoryPages"] == 0 else "theory")
            entry = {
                "id": a["id"],
                "number": a["number"],
                "title": title,
                "shortTitle": short_title(title, a["topics"]),
                "kind": kind,
                "edital": ov.get("edital", "yes"),
                "note": ov.get("note"),
                "totalPages": a["totalPages"],
                "theoryPages": a["theoryPages"],
                "segmentCount": a["segments"],
                "commentedPages": a["commentedPages"],
                "listPages": a["listPages"],
                "commentedRuns": a["commentedRuns"],
                "printedOffset": a["printedOffset"],
                "flags": a["flags"],
            }
            entry["selectable"] = ov.get("edital", "yes") != "no"
            if "practiceFor" in ov:
                secs = practice_sections(a, ov["practiceFor"])
                entry["practiceSections"] = secs
                entry["selectable"] = False  # as páginas já entram na Fixação das aulas de teoria
                for s in secs:
                    if s["forAula"]:
                        practice_links.setdefault(s["forAula"], []).append({**s, "sourceAula": a["id"]})
            aulas.append(entry)
        subjects_out.append(
            {
                "id": subj.id,
                "name": subj.name,
                "block": subj.block,
                "examQuestions": subj.exam_questions,
                "sortOrder": subj.sort_order,
                "materialCompleteness": completeness.get(subj.id, 1.0),
                **({"languageGroup": subj.language_group} if subj.language_group else {}),
                "aulas": aulas,
            }
        )

    # Fixação das aulas de teoria também pode vir de aulas de prática (ex.: Português Aula 14)
    for s in subjects_out:
        for a in s["aulas"]:
            a["practiceLinks"] = practice_links.get(a["id"], [])

    # Incidência (proxy v1): metade pela fatia de páginas de teoria, metade pela fatia de questões comentadas
    for s in subjects_out:
        eligible = [a for a in s["aulas"] if a["selectable"]]
        th = sum(a["theoryPages"] for a in eligible) or 1
        cm = sum((a["commentedPages"] or a["listPages"]) + sum(l["endPage"] - l["startPage"] + 1 for l in a["practiceLinks"])
                 for a in eligible) or 1
        for a in s["aulas"]:
            if not a["selectable"]:
                a["incidence"] = 0.0
                continue
            comm = (a["commentedPages"] or a["listPages"]) + sum(l["endPage"] - l["startPage"] + 1 for l in a["practiceLinks"])
            weight = 0.5 if a["edital"] == "partial" else 1.0
            a["incidence"] = round(weight * (0.5 * a["theoryPages"] / th + 0.5 * comm / cm), 5)
            a["fixacaoHoursFull"] = round(comm / PAGES_PER_FIXACAO_HOUR, 1)

    out = {"exam": exam, "subjects": subjects_out, "gaps": gaps}
    (CONTENT_DIR / "catalog.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n_aulas = sum(len(s["aulas"]) for s in subjects_out)
    print(f"catalog.json: {len(subjects_out)} disciplinas, {n_aulas} aulas, {len(gaps)} lacunas")
    for s in subjects_out:
        print(f"  {s['id']:24s} aulas={len(s['aulas']):2d} teoria={sum(a['theoryPages'] for a in s['aulas']):5d} "
              f"segmentos={sum(a['segmentCount'] for a in s['aulas']):3d} comentadas={sum(a['commentedPages'] for a in s['aulas']):4d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
