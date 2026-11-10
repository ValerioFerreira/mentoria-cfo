"""Régua do material próprio: mede cada trecho do material-base e fixa as metas do capítulo MentorIA correspondente.

O material-base só serve de régua (volume, densidade, pontos de atenção). Nada de texto dele é gravado aqui: só números,
os títulos de tópico que já estão em content/structure e rótulos curtos de quadro ("Atenção", "Esquematizando"...).

Por trecho (= 1 capítulo do volume MentorIA):
  source.words      palavras das páginas de teoria (pageMap = T) no cache de texto
  source.figures    figuras reais (imagens com área ≥ 6.000 pt², sem as que se repetem em > 20% das páginas do PDF: logotipos,
                    cabeçalhos, ícones)
  source.tables     tabelas (PyMuPDF find_tables)
  source.boxes      quadros de destaque (retângulos preenchidos largos, com texto, fora de tabelas)
  targets           metas do capítulo: palavras (75% da fonte, piso 900; aceita −15%/+20%), elementos visuais, quadros
  attention         pontos de atenção da fonte: página, rótulo do quadro/marcador e tópico em que aparece (checklist)
  edital            itens de edital ligados ao trecho (geral, cfoa, pcpe), importância e onda de produção

Saídas: content/material/metrics/<disciplina>.json e content/material/_queue.json (fila de volumes na ordem das ondas).
A leitura dos PDFs é guardada em pipeline/.cache/material/pdfstats/<chave>.json (rode de novo com --force para refazer).

Uso:  python pipeline/material_metrics.py [--subject <disc>] [--force] [--workers 4]
Requer `content/material/volumes/*.json` (pipeline/material_volumes.py).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, DOCS_DIR  # noqa: E402
from material_volumes import WAVES, load_importance, load_segments, wave_of  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = CONTENT_DIR.parent
MATERIAL_DIR = CONTENT_DIR / "material"
STATS_DIR = ROOT / "pipeline" / ".cache" / "material" / "pdfstats"
STATS_VERSION = 1

# metas (ver pipeline/briefs/material.md, seção 3)
WORDS_RATIO = 0.75
WORDS_FLOOR = 900
WORDS_MIN_FACTOR = 0.85
WORDS_MAX_FACTOR = 1.20
VISUAL_RATIO = 0.5
WORDS_PER_VISUAL_CAP = 400  # no máximo 1 elemento visual exigido a cada 400 palavras
WORDS_PER_CALLOUT = 600  # no mínimo 1 quadro a cada 600 palavras
MIN_IMG_AREA = 6000.0
REPEATED_SHARE = 0.2

LABEL = re.compile(
    r"^\s*(aten[cç][aã]o|cuidado|importante|esquematizando|esquema|resumindo|resumo|jurisprud[eê]ncia|s[uú]mula|dica|"
    r"exemplo|observa[cç][aã]o|obs\b|lembre-se|fique atento|pegadinha|decore|memorize|tome nota|caiu em prova|"
    r"caiu na prova|curiosidade|n[aã]o confunda|aprofundando|para fixar|em s[ií]ntese|quadro|tabela)",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------------------------- leitura dos PDFs
def pdf_path(key: str, file: str) -> Path | None:
    prefix = key.split("_")[0]
    for folder in DOCS_DIR.iterdir():
        if folder.is_dir() and folder.name.split(" ")[0] == prefix:
            p = folder / file
            if p.exists():
                return p
    hits = list(DOCS_DIR.rglob(file))
    return hits[0] if hits else None


def _merge_boxes(rects: list) -> list:
    rects = sorted(rects, key=lambda r: (r.y0, r.x0))
    out: list = []
    for r in rects:
        if out and r.y0 <= out[-1].y1 + 4 and r.x0 < out[-1].x1 and r.x1 > out[-1].x0:
            out[-1] = out[-1] | r
        else:
            out.append(r)
    return out


def page_stats(key: str) -> dict:
    """Lê o PDF de uma aula (lento: ~0,1 s por página) e devolve, por página, imagens, tabelas e quadros."""
    import pymupdf  # noqa: PLC0415

    cache = STATS_DIR / f"{key}.json"
    meta = load_pages(key)
    path = pdf_path(key, meta["file"])
    if path is None:
        return {"key": key, "missing": True, "pages": []}
    doc = pymupdf.open(path)
    pages = []
    for pg in doc:
        W, H = pg.rect.width, pg.rect.height
        imgs = []
        for im in pg.get_image_info(xrefs=True):
            x0, y0, x1, y1 = im["bbox"]
            area = (x1 - x0) * (y1 - y0)
            if area >= MIN_IMG_AREA:
                imgs.append([im.get("xref", 0), round(area)])
        try:
            tabs = pg.find_tables().tables
        except Exception:  # noqa: BLE001
            tabs = []
        tab_rects = [pymupdf.Rect(t.bbox) for t in tabs]
        fills = []
        for dr in pg.get_drawings():
            f = dr.get("fill")
            r = dr["rect"]
            if not f or min(f) > 0.97:
                continue
            if r.width < W * 0.4 or r.height < 18 or r.y1 < H * 0.1 or r.y0 > H * 0.92:
                continue
            if any(r.intersects(t) for t in tab_rects):
                continue
            fills.append(r)
        boxes = []
        for r in _merge_boxes(fills):
            txt = clean(pg.get_textbox(r)).strip()
            if len(txt) < 40:
                continue
            first = txt.splitlines()[0].strip()
            m = LABEL.match(first)
            boxes.append(m.group(1).strip().capitalize() if m else "")
        pages.append({"n": pg.number + 1, "imgs": imgs, "tables": len(tabs), "boxes": boxes})
    out = {"key": key, "version": STATS_VERSION, "file": meta["file"], "pages": pages}
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return out


def load_stats(keys: list[str], force: bool, workers: int) -> dict[str, dict]:
    out: dict[str, dict] = {}
    todo: list[str] = []
    for k in keys:
        f = STATS_DIR / f"{k}.json"
        if f.exists() and not force:
            d = json.loads(f.read_text(encoding="utf-8"))
            if d.get("version") == STATS_VERSION:
                out[k] = d
                continue
        todo.append(k)
    if todo:
        print(f"lendo {len(todo)} PDFs (imagens, tabelas, quadros)…", flush=True)
        with ProcessPoolExecutor(max_workers=workers) as ex:
            for i, d in enumerate(ex.map(page_stats, todo), start=1):
                out[d["key"]] = d
                if i % 10 == 0:
                    print(f"  {i}/{len(todo)}", flush=True)
    return out


# --------------------------------------------------------------------------------------------- dados do conteúdo
def load_structure(subject: str) -> dict[str, dict]:
    d = json.loads((CONTENT_DIR / "structure" / f"{subject}.json").read_text(encoding="utf-8"))
    return {a["id"]: a for a in d["aulas"]}


def load_catalog() -> dict[str, dict]:
    cat = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    return {a["id"]: a for s in cat["subjects"] for a in s["aulas"]}


def load_edital() -> dict[str, list[dict]]:
    """trecho -> itens de edital que apontam para ele."""
    out: dict[str, list[dict]] = defaultdict(list)
    for f in sorted((CONTENT_DIR / "edital").rglob("*.json")):
        scope = f.parent.name if f.parent.name in ("cfoa", "pcpe") else "geral"
        d = json.loads(f.read_text(encoding="utf-8"))
        if d.get("contest") and scope == "geral":
            scope = d["contest"]
        for it in d.get("items", []):
            title = it.get("item") or it.get("title") or ""
            for w in it.get("where", []) or []:
                for sid in w.get("segments", []) or []:
                    ref = f"{scope}:{it['id']}"
                    if all(e["ref"] != ref for e in out[sid]):
                        out[sid].append({"ref": ref, "title": title, "status": it.get("status", "")})
    return out


def load_exam_weights() -> dict[str, dict[str, int]]:
    c = json.loads((CONTENT_DIR / "contests.json").read_text(encoding="utf-8"))
    return {k: v.get("exam", {}) for k, v in c.items() if isinstance(v, dict)}


def tier(score: int | None) -> str:
    if score is None:
        return "BASE"
    return "ALTA" if score >= 67 else "MEDIA" if score >= 34 else "BASE"


def complement_md(aula: dict) -> str:
    name = os.path.basename(aula.get("materialPath", "")).rsplit(".", 1)[0]
    f = CONTENT_DIR / "complements" / f"{name}.md"
    return f.read_text(encoding="utf-8") if f.exists() else ""


BIDI = re.compile(r"[\u200b-\u200f\u202a-\u202e\u2066-\u2069\ufeff]")


def clean(text: str) -> str:
    """O texto extraído de alguns PDFs separa as palavras com marcas invisíveis de direção (U+202C/U+202D) em vez de espaço."""
    return BIDI.sub(" ", text)


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", text))


# --------------------------------------------------------------------------------------------- régua por trecho
def measure(subject: str, segs: list[dict], stats: dict[str, dict], keymap: dict[str, str], catalog: dict, edital: dict,
            imp: dict, volume_of: dict[str, dict]) -> list[dict]:
    struct = load_structure(subject)
    rows = []
    repeated_cache: dict[str, set] = {}
    for s in segs:
        sid = s["id"]
        if sid not in volume_of:
            continue
        aula = catalog.get(s["aula"], {})
        authored = aula.get("source") == "authored"
        contests = imp.get(sid, {}).get("contests", {})
        scores = [v["score"] for v in contests.values() if v.get("appears") and v.get("score") is not None]
        score = max(scores) if scores else None
        st = struct.get(s["aula"], {})
        topics = [t for t in st.get("topics", []) if s["startPage"] <= (t.get("pdfPage") or 0) <= s["endPage"]]
        attention: list[dict] = []
        if authored:
            md = complement_md(aula)
            share = s["pages"] / max(aula.get("theoryPages") or s["pages"], 1)
            words = round(word_count(md) * min(share, 1.0))
            figures = 0
            tables = round(len(re.findall(r"^\|\s*-{3,}", md, re.M)) * min(share, 1.0))
            boxes = round(len(re.findall(r"^>\s", md, re.M)) * min(share, 1.0))
            theory_pages = s["pages"]
        else:
            key = keymap.get(s["aula"])
            pm = st.get("pageMap", "")
            pnums = [n for n in range(s["startPage"], s["endPage"] + 1) if n - 1 < len(pm) and pm[n - 1] == "T"] or list(
                range(s["startPage"], s["endPage"] + 1))
            theory_pages = len(pnums)
            text = {p["n"]: clean(p["text"]) for p in load_pages(key)["pages"]} if key else {}
            words = sum(word_count(text.get(n, "")) for n in pnums)
            ps = stats.get(key, {}) if key else {}
            plist = {p["n"]: p for p in ps.get("pages", [])}
            if key not in repeated_cache:
                cnt: dict[int, int] = defaultdict(int)
                for p in ps.get("pages", []):
                    for x in {i[0] for i in p["imgs"]}:
                        cnt[x] += 1
                total = max(len(ps.get("pages", [])), 1)
                repeated_cache[key] = {x for x, c in cnt.items() if c > REPEATED_SHARE * total}
            rep = repeated_cache[key]
            figures = tables = boxes = 0
            for n in pnums:
                p = plist.get(n)
                if not p:
                    continue
                figures += sum(1 for i in p["imgs"] if i[0] not in rep)
                tables += p["tables"]
                boxes += len(p["boxes"])
                labels = [b for b in p["boxes"] if b]
                for line in text.get(n, "").splitlines():
                    m = LABEL.match(line)
                    if m and len(line.strip()) <= 60:
                        labels.append(m.group(1).strip().capitalize())
                if labels:
                    cur = None
                    for t in st.get("topics", []):
                        if (t.get("pdfPage") or 0) <= n:
                            cur = t["title"]
                    for lb in dict.fromkeys(labels):
                        attention.append({"page": n, "label": lb, "topic": cur})
        target = max(WORDS_FLOOR, round(words * (1.0 if authored else WORDS_RATIO)))
        visuals = max(2, min(math.ceil(VISUAL_RATIO * (figures + tables)), max(2, target // WORDS_PER_VISUAL_CAP)))
        callouts = min(14, max(math.ceil(target / WORDS_PER_CALLOUT), round(0.8 * boxes)))
        vol = volume_of[sid]
        rows.append({
            "id": sid,
            "aula": s["aula"],
            "volume": vol["id"],
            "chapter": vol["trechos"].index(sid) + 1,
            "wave": wave_of(contests),
            "contests": [k for k, _ in WAVES if contests.get(k, {}).get("appears")],
            "importance": {"score": score, "tier": tier(score)},
            "authored": authored,
            "fingerprint": {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s.get("startTopic")},
            "minutes": s.get("minutes", 60),
            "source": {"pages": s["pages"], "theoryPages": theory_pages, "words": words, "figures": figures, "tables": tables,
                       "boxes": boxes, "wordsPerPage": round(words / max(theory_pages, 1))},
            "targets": {"words": target, "wordsMin": round(target * WORDS_MIN_FACTOR), "wordsMax": round(target * WORDS_MAX_FACTOR),
                        "visuals": visuals, "callouts": callouts},
            "topics": s.get("topicsCovered") or [t["title"] for t in topics],
            "edital": edital.get(sid, []),
            "attention": attention,
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    vols_dir = MATERIAL_DIR / "volumes"
    if not vols_dir.exists():
        raise SystemExit("rode antes: python pipeline/material_volumes.py")
    volumes = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(vols_dir.glob("*.json"))}
    volume_of = {t: v for d in volumes.values() for v in d["volumes"] for t in v["trechos"]}
    segs = load_segments()
    imp = load_importance()
    catalog = load_catalog()
    edital = load_edital()
    keymap = aula_key_map()
    subjects = [args.subject] if args.subject else sorted(volumes)
    keys = sorted({keymap[s["aula"]] for sub in subjects for s in segs[sub] if s["id"] in volume_of and s["aula"] in keymap})
    stats = load_stats(keys, args.force, args.workers)

    out_dir = MATERIAL_DIR / "metrics"
    out_dir.mkdir(parents=True, exist_ok=True)
    for sub in subjects:
        rows = measure(sub, segs[sub], stats, keymap, catalog, edital, imp, volume_of)
        (out_dir / f"{sub}.json").write_text(json.dumps({"subject": sub, "_comment": "Gerado por pipeline/material_metrics.py.",
                                                         "trechos": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        tw = sum(r["targets"]["words"] for r in rows)
        print(f"{sub:34s} {len(rows):4d} capítulos  meta {tw/1000:6.0f} mil palavras  figuras-fonte {sum(r['source']['figures'] for r in rows):5d}"
              f"  tabelas {sum(r['source']['tables'] for r in rows):4d}  quadros {sum(r['source']['boxes'] for r in rows):4d}")
    write_queue(volumes)
    return 0


def write_queue(volumes: dict[str, dict]) -> None:
    """Fila de volumes: onda → peso da disciplina na prova do concurso da onda → número do volume."""
    metrics = {}
    for f in (MATERIAL_DIR / "metrics").glob("*.json"):
        for r in json.loads(f.read_text(encoding="utf-8"))["trechos"]:
            metrics[r["id"]] = r
    weights = load_exam_weights()
    rows = []
    for sub, d in volumes.items():
        for v in d["volumes"]:
            wave_key = WAVES[v["wave"] - 1][0] if v["wave"] else None
            weight = weights.get(wave_key, {}).get(sub, 0) if wave_key else 0
            ms = [metrics[t] for t in v["trechos"] if t in metrics]
            rows.append({
                "volume": v["id"], "title": v["title"], "wave": v["wave"], "waveName": WAVES[v["wave"] - 1][1] if v["wave"] else "",
                "subjectWeight": weight, "chapters": v["chapters"],
                "targetWords": sum(m["targets"]["words"] for m in ms),
                "maxImportance": max((m["importance"]["score"] or 0 for m in ms), default=0),
                "pares": [p for p in d.get("pares", []) if v["id"] in p["volumes"]],
            })
    rows.sort(key=lambda r: (r["wave"] or 99, -r["subjectWeight"], r["volume"].split("/")[0], r["volume"]))
    for i, r in enumerate(rows, start=1):
        r["rank"] = i
    total = sum(r["targetWords"] for r in rows)
    (MATERIAL_DIR / "_queue.json").write_text(json.dumps({"_comment": "Gerado por pipeline/material_metrics.py. Ordem de produção dos volumes.",
                                                          "count": len(rows), "totalTargetWords": total, "queue": rows},
                                                         ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"fila: {len(rows)} volumes, meta total {total/1e6:.2f} mi de palavras")


if __name__ == "__main__":
    raise SystemExit(main())
