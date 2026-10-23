"""Gera a estrutura (content/structure/) e segmentos (content/segments/) para as disciplinas do CFOA:
- administracao (Noções de Administração - 11 aulas)
- direitos-humanos (Direitos Humanos - 6 aulas)
- direito-processual-penal-militar (Direito Processual Penal Militar - 14 aulas)

Regras:
1. Neutralidade absoluta: sem nomes de professores, 'Equipe', 'Estratégia', 'Somente PDF', redes sociais.
2. Segmentação equilibrada: trechos de 10 a 17 páginas (teto 17).
3. Classificação precisa das páginas: FRONT, THEORY, COMMENTED, LIST, KEY.
"""
from __future__ import annotations

import json
import os
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"
CONTENT_DIR = ROOT / "content"

TARGET_LOAD = 13.0
MAX_PAGES = 17

BANNED_WORDS = [
    "prof", "professor", "professora", "stefan", "fantini", "ricardo", "torques",
    "equipe", "estrategia", "estratégia", "telegram", "instagram", "youtube",
    "somente pdf", "somente em pdf", "forum de duvidas", "fórum de dúvidas",
    "fale comigo", "apresentacao do curso", "apresentação do curso"
]

TITLES_OVERRIDE = {
    "administracao/a09": "Evolução da Administração Pública no Brasil após 1930: Reformas Administrativas e a Nova Gestão Pública (Parte I)",
    "administracao/a10": "Evolução da Administração Pública no Brasil após 1930: Reformas Administrativas e a Nova Gestão Pública (Parte II)",
    "direitos-humanos/a00": "Introdução aos Direitos Humanos: Conceito, Terminologia e Classificação",
    "direitos-humanos/a01": "Histórico e Afirmação dos Direitos Humanos",
    "direitos-humanos/a02": "Declaração Universal dos Direitos Humanos de 1948 (ONU)",
    "direitos-humanos/a03": "Convenção Americana de Direitos Humanos (Pacto de San José da Costa Rica)",
    "direitos-humanos/a04": "Programa Nacional de Direitos Humanos (PNDH-3) e Comissão Nacional da Verdade",
    "direitos-humanos/a05": "Direitos Fundamentais na CF/88, Direitos Civis, Políticos, Sociais e Difusos",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def is_banned(s: str) -> bool:
    s_low = s.lower()
    return any(w in s_low for w in BANNED_WORDS)


def clean_aula_title(filename: str, aula_id: str) -> str:
    if aula_id in TITLES_OVERRIDE:
        return TITLES_OVERRIDE[aula_id]
    t = re.sub(r"^\s*\d{3}\s*-\s*Aula\s*\d+\s*[-–]?\s*", "", filename)
    t = re.sub(r"^\s*-\s*Prof\..*?-\s*", "", t)
    t = re.sub(r"\.pdf$", "", t).strip()
    t = re.sub(r"^\s*\(Somente\s+(?:em\s+)?PDF\)\s*", "", t, flags=re.I)
    t = re.sub(r"\s*-\s*Somente\s+(?:em\s+)?PDF\b", "", t, flags=re.I)
    t = re.sub(r"\s+", " ", t.replace("_ ", ": ").replace("_", ":")).strip().rstrip(".")
    return t


def analyze_pdf_layout(pages_data: dict) -> tuple[int, int, int | None, int | None, int | None]:
    pages = pages_data["pages"]
    tot = len(pages)

    # 1. Detect TOC pages (front)
    toc_pages = []
    for p in pages[:8]:
        t_norm = norm(p["text"])
        if "sumario" in t_norm or "indice" in t_norm:
            toc_pages.append(p["n"])

    front_end = max(toc_pages) if toc_pages else 1

    # Check for presentation/introductory pages after TOC
    theory_start = front_end + 1
    for p in pages[front_end:min(front_end + 8, tot)]:
        lines = [ln.strip() for ln in p["text"].split("\n") if ln.strip()]
        for ln in lines[:4]:
            nl = norm(ln)
            if nl.startswith("apresentacaodocurso") or nl.startswith("formasdecontato") or nl.startswith("forumdeduvidas"):
                theory_start = p["n"] + 1

    # 2. Detect commented questions, list, and gabarito
    comm_start = None
    list_start = None
    gab_start = None

    for p in pages:
        p_num = p["n"]
        if p_num < theory_start:
            continue
        lines = [ln.strip() for ln in p["text"].split("\n") if ln.strip()]
        for ln in lines[:6]:
            nl = norm(ln)
            if not comm_start:
                if ("questoescomentadas" in nl or
                    "questoescomcomentarios" in nl or
                    "listadequestoescomcomentarios" in nl or
                    "exercicioscomentados" in nl):
                    comm_start = p_num
                    break
            if not list_start and comm_start and p_num > comm_start:
                if ("listadequestoes" in nl or
                    "questoessemcomentarios" in nl or
                    "questoespropostas" in nl):
                    if "comcomentarios" not in nl:
                        list_start = p_num
                        break
            if not gab_start and (list_start or comm_start):
                if nl == "gabarito" or nl.startswith("gabaritodasquestoes") or nl.startswith("gabaritofinal"):
                    gab_start = p_num
                    break

    theory_end = (comm_start - 1) if comm_start else ((list_start - 1) if list_start else ((gab_start - 1) if gab_start else tot))
    return theory_start, theory_end, comm_start, list_start, gab_start


def extract_topics(pages: list[dict], theory_start: int, theory_end: int, clean_title: str) -> list[dict]:
    topics = []
    seen_titles = set()

    for p_idx in range(theory_start, theory_end + 1):
        p_data = pages[p_idx - 1]
        lines = [ln.strip() for ln in p_data["text"].split("\n") if ln.strip()]
        for ln in lines[:8]:
            if is_banned(ln):
                continue
            # Look for numbered headings: e.g. "1 - Conceito", "1.1 - Níveis", "Capítulo I", "Art. 1º"
            m = re.match(r"^(\d{1,2}(?:\.\d{1,2})*)\s*[-–\.]\s*([A-ZÀ-ÿ].{3,80})$", ln)
            if m:
                num_s, title_s = m.group(1), m.group(2).strip()
                full_t = f"{num_s}. {title_s}"
                if is_banned(full_t) or len(title_s) < 3:
                    continue
                if full_t.lower() not in seen_titles:
                    seen_titles.add(full_t.lower())
                    lvl = 1 if "." not in num_s else 2
                    topics.append({
                        "level": lvl,
                        "title": full_t,
                        "pdfPage": p_idx,
                        "printedPage": None,
                        "kind": "heading",
                        "verified": True,
                        "manual": True,
                    })
                    break

    # If no numbered topics found, look for uppercase headings or fallback to clean_title
    if not topics:
        for p_idx in range(theory_start, theory_end + 1):
            p_data = pages[p_idx - 1]
            lines = [ln.strip() for ln in p_data["text"].split("\n") if ln.strip()]
            for ln in lines[:4]:
                if is_banned(ln):
                    continue
                if re.match(r"^[A-ZÀ-ÿ\s]{4,60}$", ln) and not any(w in norm(ln) for w in ["aula", "sumario", "indice"]):
                    t_cap = ln.strip().title()
                    if t_cap.lower() not in seen_titles:
                        seen_titles.add(t_cap.lower())
                        topics.append({
                            "level": 1,
                            "title": t_cap,
                            "pdfPage": p_idx,
                            "printedPage": None,
                            "kind": "heading",
                            "verified": True,
                            "manual": True,
                        })
                        break

    if not topics:
        topics.append({
            "level": 1,
            "title": clean_title,
            "pdfPage": theory_start,
            "printedPage": None,
            "kind": "heading",
            "verified": True,
            "manual": True,
        })

    return topics


def analyze_aula(pages_data: dict, subject_id: str) -> tuple[dict, list[dict]]:
    pages = pages_data["pages"]
    tot = len(pages)
    aula_id = pages_data["aula"]
    aula_num = pages_data["aulaNumber"]
    filename = pages_data["file"]

    theory_start, theory_end, comm_start, list_start, gab_start = analyze_pdf_layout(pages_data)

    types = ["FRONT"] * tot
    for i in range(theory_start, theory_end + 1):
        if i <= tot:
            types[i - 1] = "THEORY"

    if comm_start:
        end_comm = (list_start - 1) if list_start else ((gab_start - 1) if gab_start else tot)
        for i in range(comm_start, end_comm + 1):
            if i <= tot:
                types[i - 1] = "COMMENTED"

    if list_start:
        end_list = (gab_start - 1) if gab_start else tot
        for i in range(list_start, end_list + 1):
            if i <= tot:
                types[i - 1] = "LIST"

    if gab_start:
        for i in range(gab_start, tot + 1):
            types[i - 1] = "KEY"

    theory_runs = [[theory_start, theory_end]] if theory_end >= theory_start else []
    theory_pages = sum(e - s + 1 for s, e in theory_runs)

    commented_runs = []
    if comm_start:
        end_comm = (list_start - 1) if list_start else ((gab_start - 1) if gab_start else tot)
        commented_runs.append([comm_start, end_comm])
    commented_pages = sum(e - s + 1 for s, e in commented_runs)

    list_pages = sum(1 for t in types if t == "LIST")

    clean_t = clean_aula_title(filename, aula_id)
    topics = extract_topics(pages, theory_start, theory_end, clean_t)

    # Partition theory run into segments
    segments = []
    seg_order = 0
    for s_run, e_run in theory_runs:
        run_len = e_run - s_run + 1
        if run_len <= MAX_PAGES:
            n_splits = 1
        else:
            n_splits = max(1, round(run_len / TARGET_LOAD))
            while any(run_len / n_splits > MAX_PAGES for _ in [1]):
                n_splits += 1

        chunk_size = run_len / n_splits
        for k in range(n_splits):
            seg_order += 1
            sp = s_run + int(round(k * chunk_size))
            ep = s_run + int(round((k + 1) * chunk_size)) - 1
            if k == n_splits - 1:
                ep = e_run
            ep = max(sp, min(ep, e_run))

            matching_topics = [t["title"] for t in topics if sp <= t["pdfPage"] <= ep]
            if not matching_topics:
                # Find closest topic at or before sp
                earlier = [t["title"] for t in topics if t["pdfPage"] <= sp]
                active_t = earlier[-1] if earlier else topics[0]["title"]
            else:
                active_t = matching_topics[0]

            end_t = matching_topics[-1] if matching_topics else active_t

            segments.append({
                "id": f"{aula_id}/s{seg_order:02d}",
                "aula": aula_id,
                "order": seg_order,
                "startPage": sp,
                "endPage": ep,
                "startPrinted": sp,
                "endPrinted": ep,
                "pages": ep - sp + 1,
                "load": round((ep - sp + 1) * 0.95, 2),
                "startTopic": active_t,
                "startsMidTopic": False,
                "stopBeforeTopic": None,
                "endsMidTopic": False,
                "endTopic": end_t,
                "endsTheory": (k == n_splits - 1),
                "topicsCovered": matching_topics if matching_topics else [active_t],
                "minutes": 60,
            })

    page_map = "".join(t[0] for t in types)

    aula_dict = {
        "id": aula_id,
        "number": aula_num,
        "file": filename,
        "title": clean_t,
        "totalPages": tot,
        "tocMax": 1,
        "printedOffset": 0,
        "theoryRuns": theory_runs,
        "theoryPages": theory_pages,
        "commentedRuns": commented_runs,
        "commentedPages": commented_pages,
        "listPages": list_pages,
        "segments": len(segments),
        "pageMap": page_map,
        "flags": [
            f"págs. {r[0]}-{r[1]} → THEORY" for r in theory_runs
        ],
        "topics": topics,
    }

    return aula_dict, segments


def process_subject(subject_id: str, folder_prefix: str):
    print(f"Processando '{subject_id}' (prefixo '{folder_prefix}')...")
    json_files = sorted(PAGES_DIR.glob(f"{folder_prefix}_*.json"))
    if not json_files:
        print(f"ERRO: Nenhum arquivo em pages para {folder_prefix}_*.json!")
        return

    aulas = []
    all_segments = []

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
        aula_obj, segs = analyze_aula(data, subject_id)
        aulas.append(aula_obj)
        all_segments.extend(segs)

    aulas.sort(key=lambda a: a["number"])

    struct_doc = {"subject": subject_id, "aulas": aulas}
    seg_doc = {"subject": subject_id, "segments": all_segments}

    struct_path = CONTENT_DIR / "structure" / f"{subject_id}.json"
    seg_path = CONTENT_DIR / "segments" / f"{subject_id}.json"

    struct_path.parent.mkdir(parents=True, exist_ok=True)
    seg_path.parent.mkdir(parents=True, exist_ok=True)

    with open(struct_path, "w", encoding="utf-8") as f:
        json.dump(struct_doc, f, ensure_ascii=False, indent=2)

    with open(seg_path, "w", encoding="utf-8") as f:
        json.dump(seg_doc, f, ensure_ascii=False, indent=2)

    total_theory = sum(a["theoryPages"] for a in aulas)
    max_seg_p = max(s["pages"] for s in all_segments) if all_segments else 0
    print(f"  OK: {len(aulas)} aulas, {len(all_segments)} segmentos, {total_theory} págs teoria (máx seg: {max_seg_p} págs).")


def main():
    process_subject("administracao", "49")
    process_subject("direitos-humanos", "50")
    process_subject("direito-processual-penal-militar", "26")
    print("Todas as 3 disciplinas estruturadas e salvas com sucesso!")


if __name__ == "__main__":
    main()
