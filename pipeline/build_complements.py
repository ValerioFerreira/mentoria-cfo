"""Materiais complementares do MentorIA: preenchem lacunas do edital que o Estratégia não cobre.

Fonte autoral:  content/complements/<id>.md   (front matter simples + Markdown)
Saídas:
  - web/public/complementos/<id>.pdf           PDF servido ao aluno (abre dentro da atividade)
  - content/catalog.json / structure/<disciplina>.json / segments/<disciplina>.json   (aulas "authored" mescladas)
  - content/gaps.json                          (lacunas resolvidas + completude do material)

Rode DEPOIS de segment.py e build_catalog.py (que regeneram os arquivos acima). É idempotente.
Uso: python pipeline/build_complements.py [--only <id>] [--no-pdf]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf as fitz
import markdown

from config import CONTENT_DIR, ROOT

SRC_DIR = CONTENT_DIR / "complements"
PDF_DIR = ROOT / "web" / "public" / "complementos"
COMPLEMENT_BASE = 100  # aula.number = 100 + ordem (a interface mostra "Complemento NN")
SEGMENT_MAX_PAGES = 17
SEGMENT_TARGET_PAGES = 13
# Páginas do material autoral são densas (tabelas, listas, macetes): ~8–9 págs. por hora, contra 10–17 do Estratégia.
LOAD_PER_PAGE = 1.4

CSS = """
body { font-family: sans-serif; font-size: 10.4pt; line-height: 1.38; color: #1b2433; }
p { margin: 0 0 6pt 0; text-align: left; }
h1 { font-size: 23pt; line-height: 1.05; color: #0e1b2e; margin: 0 0 4pt 0; }
h2 { font-size: 15pt; color: #0e1b2e; margin: 14pt 0 5pt 0; padding-bottom: 2pt; border-bottom: 1.5pt solid #d4301f; page-break-after: avoid; }
h2.first { margin-top: 10pt; }
h3 { font-size: 11.6pt; color: #d4301f; margin: 10pt 0 3pt 0; }
h4 { font-size: 10.6pt; color: #0e1b2e; margin: 8pt 0 2pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 15pt; }
li { margin: 0 0 2.5pt 0; }
strong { color: #0e1b2e; }
em { color: #34425a; }
table { border-collapse: separate; border-spacing: 0; width: 100%; margin: 4pt 0 8pt 0; font-size: 9.4pt; }
th { background-color: #e6ebf3; color: #0e1b2e; padding: 3.5pt 5pt; text-align: left; border-bottom: 1.2pt solid #0e1b2e; }
td { border-bottom: 0.6pt solid #c8d0dc; padding: 3.5pt 5pt; vertical-align: top; }
blockquote { margin: 5pt 0 8pt 0; padding: 5pt 9pt; background-color: #fff4d1; border-left: 3pt solid #e9a90c; }
blockquote p { margin: 0 0 3pt 0; }
code { font-family: monospace; background-color: #eef1f6; }
.kicker { font-size: 8.6pt; letter-spacing: 1.6pt; color: #d4301f; font-weight: bold; margin: 0 0 6pt 0; }
.sub { font-size: 11pt; color: #55627a; margin: 0 0 8pt 0; }
.src { font-size: 8.8pt; color: #55627a; margin-top: 14pt; border-top: 0.6pt solid #c8d0dc; padding-top: 5pt; }
"""


def unquote(v: str) -> str:
    """Tira as aspas que envolvem o valor inteiro (mas não a aspa final de um título como Funções do "que" e do "se")."""
    v = v.strip()
    return v[1:-1] if len(v) > 1 and v[0] == v[-1] == '"' else v


@dataclass
class Doc:
    id: str
    subject: str
    title: str
    short: str
    subtitle: str
    weight: float
    order: int
    body: str
    sources: str = ""
    topics: list[tuple[int, str, int]] = field(default_factory=list)  # (nível, título, página)
    pages: int = 0


def parse(path: Path) -> Doc:
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise SystemExit(f"{path.name}: front matter ausente")
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip()] = unquote(v)
    body = m.group(2).strip()
    sources = ""
    sm = re.search(r"\n##\s+Fontes\s*\n(.*)$", body, re.S)
    if sm:  # a seção "Fontes" vira rodapé do PDF (não é um tópico de estudo)
        sources = sm.group(1).strip()
        body = body[: sm.start()].strip()
    return Doc(
        id=meta["id"], subject=meta["subject"], title=meta["title"], short=meta.get("short", meta["title"]),
        subtitle=meta.get("subtitle", ""), weight=float(meta.get("weight", "0.05")), order=int(meta.get("order", "1")),
        body=body, sources=sources,
    )


def to_html(doc: Doc) -> str:
    inner = markdown.markdown(doc.body, extensions=["tables", "sane_lists"])
    first = [True]

    def mark_first(m: re.Match) -> str:
        if first[0]:
            first[0] = False
            return '<h2 class="first">'
        return "<h2>"

    inner = re.sub(r"<h2>", mark_first, inner)
    src = f'<div class="src"><b>Fontes e método.</b> {markdown.markdown(doc.sources)}</div>' if doc.sources else ""
    head = (
        f'<p class="kicker">MATERIAL COMPLEMENTAR · MENTORIA</p><h1>{html.escape(doc.title)}</h1>'
        f'<p class="sub">{html.escape(doc.subtitle)}</p>'
    )
    return f"<html><body>{head}{inner}{src}</body></html>"


def build_pdf(doc: Doc, out: Path | None) -> None:
    story = fitz.Story(html=to_html(doc), user_css=CSS)
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (50, 54, -50, -62)
    heads: list[tuple[int, str, int]] = []

    def recorder(elpos):
        if elpos.heading and (elpos.open_close & 1):
            heads.append((elpos.heading, (elpos.text or "").strip(), elpos.page))

    tmp = fitz.DocumentWriter(str(out) if out else str(ROOT / "pipeline" / ".cache" / f"_tmp_{doc.id}.pdf"))
    pno, more = 0, 1
    while more:
        dev = tmp.begin_page(mediabox)
        more, _ = story.place(where)
        story.element_positions(recorder, {"page": pno + 1})
        story.draw(dev)
        tmp.end_page()
        pno += 1
    tmp.close()
    doc.pages = pno
    doc.topics = [(h, t, p) for h, t, p in heads if h in (2, 3) and t]
    # rodapé com numeração
    pdf = fitz.open(str(out) if out else str(ROOT / "pipeline" / ".cache" / f"_tmp_{doc.id}.pdf"))
    total = len(pdf)
    for i, page in enumerate(pdf, start=1):
        r = page.rect
        page.draw_line((50, r.height - 44), (r.width - 50, r.height - 44), color=(0.78, 0.82, 0.88), width=0.6)
        page.insert_text((50, r.height - 30), f"MentorIA · Material complementar · {doc.short}", fontsize=8, fontname="helv", color=(0.33, 0.38, 0.48))
        label = f"Página {i} de {total}"
        w = fitz.get_text_length(label, fontname="helv", fontsize=8)
        page.insert_text((r.width - 50 - w, r.height - 30), label, fontsize=8, fontname="helv", color=(0.33, 0.38, 0.48))
    pdf.set_metadata({"title": f"{doc.title} — MentorIA", "author": "MentorIA", "subject": doc.subtitle})
    if out:
        data = pdf.tobytes(garbage=3, deflate=True)
        pdf.close()
        out.write_bytes(data)
    else:
        pdf.close()


def segments_for(doc: Doc) -> list[dict]:
    """Segmentos de ~1 h: grupos de seções (##) que começam sempre em início de seção, com no máx. 17 páginas."""
    sections = [(t, p) for h, t, p in doc.topics if h == 2]
    if not sections:
        sections = [(doc.title, 1)]
    # cada seção ocupa da sua página até a anterior à próxima seção
    bounds = []
    for i, (t, p) in enumerate(sections):
        end = (sections[i + 1][1] - 1) if i + 1 < len(sections) else doc.pages
        bounds.append((t, p, max(p, end)))
    total = doc.pages
    if total <= SEGMENT_MAX_PAGES:
        groups = [bounds]
    else:
        groups, cur = [], []
        for b in bounds:
            span = (b[2] - cur[0][1] + 1) if cur else 0
            if cur and span > SEGMENT_MAX_PAGES - 0 or (cur and (cur[-1][2] - cur[0][1] + 1) >= SEGMENT_TARGET_PAGES):
                groups.append(cur)
                cur = []
            cur.append(b)
        if cur:
            groups.append(cur)
    out = []
    prev_end = 0
    for i, g in enumerate(groups, start=1):
        start, end = g[0][1], g[-1][2]
        # duas seções que começam na mesma página, em lados opostos do corte, não podem repetir essa página
        start = max(start, prev_end + 1)
        end = max(end, start)
        prev_end = end
        pages = end - start + 1
        nxt = groups[i][0][0] if i < len(groups) else None
        out.append({
            "id": f"{doc.subject}/c{doc.order:02d}/s{i:02d}",
            "aula": f"{doc.subject}/c{doc.order:02d}",
            "order": i, "startPage": start, "endPage": end, "startPrinted": start, "endPrinted": end,
            "pages": pages, "load": round(pages * LOAD_PER_PAGE, 2),
            "startTopic": g[0][0], "startsMidTopic": False, "stopBeforeTopic": nxt, "endsMidTopic": False,
            "endTopic": g[-1][0], "endsTheory": i == len(groups), "topicsCovered": [t for t, _, _ in g], "minutes": 60,
        })
    return out


def merge(docs: list[Doc]) -> None:
    catalog_path = CONTENT_DIR / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    gaps_path = CONTENT_DIR / "gaps.json"
    gaps_doc = json.loads(gaps_path.read_text(encoding="utf-8"))
    by_subject: dict[str, list[Doc]] = {}
    for d in docs:
        by_subject.setdefault(d.subject, []).append(d)

    for subj in catalog["subjects"]:
        mine = sorted(by_subject.get(subj["id"], []), key=lambda d: d.order)
        subj["aulas"] = [a for a in subj["aulas"] if a.get("source") != "authored"]  # idempotente
        w_total = sum(d.weight for d in mine)
        # a soma de incidências da disciplina é preservada: as aulas do Estratégia cedem a fatia dos complementos.
        # `incidenceBase` guarda o valor original para a mescla ser idempotente.
        for a in subj["aulas"]:
            if a.get("selectable"):
                a["incidenceBase"] = a.get("incidenceBase", a["incidence"])
                a["incidence"] = round(a["incidenceBase"] * (1 - w_total), 5)
        base_inc = sum(a["incidenceBase"] for a in subj["aulas"] if a.get("selectable"))
        # estrutura e segmentos do Estratégia, sem os complementos anteriores
        struct_path = CONTENT_DIR / "structure" / f"{subj['id']}.json"
        seg_path = CONTENT_DIR / "segments" / f"{subj['id']}.json"
        struct = json.loads(struct_path.read_text(encoding="utf-8"))
        segs = json.loads(seg_path.read_text(encoding="utf-8"))
        struct["aulas"] = [a for a in struct["aulas"] if a.get("source") != "authored"]
        segs["segments"] = [s for s in segs["segments"] if "/c" not in s["aula"].split("/")[-1][:2] and not re.match(r".*/c\d+$", s["aula"])]
        for d in mine:
            seg_list = segments_for(d)
            aula_id = f"{d.subject}/c{d.order:02d}"
            incidence = round(base_inc * d.weight, 5) if base_inc else round(d.weight, 5)
            subj["aulas"].append({
                "id": aula_id, "number": COMPLEMENT_BASE + d.order, "title": d.title, "shortTitle": d.short,
                "kind": "theory", "edital": "yes", "selectable": True, "note": f"Material complementar MentorIA: {d.subtitle}",
                "totalPages": d.pages, "theoryPages": d.pages, "segmentCount": len(seg_list), "commentedPages": 0, "listPages": 0,
                "commentedRuns": [], "practiceLinks": [], "printedOffset": 0, "incidence": incidence,
                "source": "authored", "materialPath": f"complementos/{d.id}.pdf",
            })
            struct["aulas"].append({
                "id": aula_id, "number": COMPLEMENT_BASE + d.order, "file": f"{d.id}.pdf", "totalPages": d.pages, "printedOffset": 0,
                "theoryRuns": [[1, d.pages]], "theoryPages": d.pages, "commentedRuns": [], "commentedPages": 0, "listPages": 0,
                "segments": len(seg_list), "flags": ["authored"], "source": "authored",
                "topics": [{"level": h - 1, "title": t, "pdfPage": p, "printedPage": p, "kind": "heading", "verified": True} for h, t, p in d.topics],
            })
            segs["segments"].extend(seg_list)
        struct_path.write_text(json.dumps(struct, ensure_ascii=False, indent=2), encoding="utf-8")
        seg_path.write_text(json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8")
        subj["aulas"].sort(key=lambda a: a["number"])
        if mine:
            subj["materialCompleteness"] = 1.0

    # lacunas: o que os complementos resolvem fica registrado (a interface esconde as resolvidas)
    resolved = {g["id"]: g for g in gaps_doc["gaps"]}
    by_gap: dict[str, list[str]] = {}
    for d in docs:
        for gid in [x.strip() for x in d_meta(d).get("resolves", "").split(",") if x.strip()]:
            if gid in resolved:
                by_gap.setdefault(gid, []).append(d.title)
    for gid, titles in by_gap.items():
        resolved[gid]["resolved"] = True
        resolved[gid]["resolution"] = ("Complemento MentorIA: " if len(titles) == 1 else "Complementos MentorIA: ") + "; ".join(titles)
    gaps_doc["gaps"] = list(resolved.values())
    catalog["gaps"] = gaps_doc["gaps"]
    mc = {k: v for k, v in gaps_doc.get("materialCompleteness", {}).items() if k.startswith("_")}
    gaps_doc["materialCompleteness"] = mc
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    gaps_path.write_text(json.dumps(gaps_doc, ensure_ascii=False, indent=2), encoding="utf-8")


_META: dict[str, dict[str, str]] = {}


def d_meta(d: Doc) -> dict[str, str]:
    return _META.get(d.id, {})


def load_meta(path: Path) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    out: dict[str, str] = {}
    for line in (m.group(1) if m else "").splitlines():
        if ":" in line and not line.startswith("#"):
            k, v = line.split(":", 1)
            out[k.strip()] = unquote(v)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--no-merge", action="store_true", help="só gera PDFs (não toca catálogo/estrutura/segmentos/gaps): seguro com vários autores em paralelo")
    args = ap.parse_args()
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    (ROOT / "pipeline" / ".cache").mkdir(exist_ok=True)
    files = sorted(SRC_DIR.glob("*.md"))
    docs: list[Doc] = []
    for f in files:
        d = parse(f)
        _META[d.id] = load_meta(f)
        build_pdf(d, None if args.no_pdf or (args.only and d.id != args.only) else PDF_DIR / f"{d.id}.pdf")
        docs.append(d)
        words = len(re.findall(r"\w+", d.body))
        sys.stdout.buffer.write(f"{d.id:34s} {d.pages:3d} págs  {words:5d} palavras  {len(segments_for(d))} segmento(s)\n".encode("utf-8"))
    if args.no_merge:
        print(f"{len(docs)} complemento(s) lidos (sem mesclar no catálogo)")
        return 0
    merge(docs)
    print(f"{len(docs)} complemento(s) mesclados no catálogo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
