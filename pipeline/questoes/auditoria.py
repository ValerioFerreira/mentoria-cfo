"""Auditoria SOMENTE LEITURA do acervo de questões (extração, figuras, classificação e banco).

    pipeline/.venv/Scripts/python pipeline/questoes/auditoria.py [--backup DIR] [--saida DIR] [--so CADERNO]

Nada é gravado em banco nem no manifesto do importador. Saída (fora do git, contém texto de questões):
docs/questoes/auditoria/<AAAA-MM-DD>/
    inventario.csv      um caderno por linha: páginas, links, números, gabarito, extraídas, anomalias
    extracao.csv        uma questão por linha: páginas inicial/final, cobertura de palavras PDF × texto,
                        figuras na região × figuras vinculadas, desenhos vetoriais, contaminação, alternativas
    imagens.json        relatório de figuras (exigidas, vinculadas, ausentes, referências quebradas)
    taxonomia_tec.csv   matéria|assunto do TEC: questões, cadernos, anos, curadoria atual
    classificacao.csv   classificação recalculada agora × produção (backup) por questão
    reconciliacao.json  contagens: acervo × banco (ausentes, órfãs, status, trecho, conteúdo)
    resumo.json         números consolidados para o relatório

O validador de extração é independente do extrator (tec_pdf.py): relê cada PDF por `get_text("dict")`
(spans, não caracteres), recorta a região de cada questão entre os links `.../questoes/<id>` e compara o
multiconjunto de palavras do PDF com o texto extraído (enunciado + texto-base + alternativas).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

DOCS = ROOT / "docs" / "questoes"
URL_RE = re.compile(r"^\s*www\.tecconcursos\.com\.br/questoes/(\d+)\s*$")
LABEL_RE = re.compile(r"^\s*(\d{1,5})\)\s*$")
GAB_RE = re.compile(r"(\d+)\)\s*(Certo|Errado|Anulada|[A-E])\b")
OPT_LABEL_RE = re.compile(r"^\s*([a-e])\)\s*")
MD_IMG = re.compile(r"!\[([^\]]*)\]\(/q-img/([0-9a-f]{64})\)")
TAGS = re.compile(r"</?(?:u|mark)>")
SUPSUB = re.compile(r"</?(?:sup|sub)>")
WORD = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+")
# metadados de impressão que nunca podem estar no texto de uma questão
CHROME_PATTERNS = [
    ("url_caderno", re.compile(r"tecconcursos\.com\.br/questoes/cadernos", re.I)),
    ("url_questao", re.compile(r"www\.tecconcursos\.com\.br/questoes/\d+", re.I)),
    ("data_impressao", re.compile(r"\b\d{2}/\d{2}/\d{4},\s*\d{2}:\d{2}\b")),
    ("cabecalho_banca", re.compile(r"Instituto AOCP\s+-\s+\S+.*?/\d{4}\b")),
    ("titulo_caderno", re.compile(r"\bCaderno (Direito|Estat|Inform|Matem|PMPE|Racioc)", re.I)),
    ("gabarito", re.compile(r"(^|\n)\s*Gabarito\s*($|\n)")),
]
FIG_WORDS = re.compile(
    r"\b(?:(?:a|na|da|pela|observe a|conforme a|segundo a|de acordo com a)\s+(?:figura|imagem|tirinha|charge|ilustra[cç][aã]o|fotografia|foto|tabela|planilha)"
    r"|(?:o|no|do|pelo|observe o|conforme o|segundo o|de acordo com o)\s+(?:gr[aá]fico|quadro|mapa|esquema|diagrama|cartum|quadrinho|circuito))"
    r"\s+(?:a seguir|abaixo|acima|seguinte|apresentad[ao]|mostrad[ao]|ilustrad[ao])",
    re.I,
)


def fold(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c)).lower()


def words(text: str) -> Counter:
    out: Counter = Counter()
    for w in WORD.findall(fold(text)):
        if len(w) >= 2 or w.isdigit():
            out[w] += 1
    return out


def plain(md: str) -> str:
    t = MD_IMG.sub(" ", md or "")
    t = SUPSUB.sub(" ", TAGS.sub("", t)).replace("**", "").replace("`", "")
    return t.replace("\\*", "*").replace("\\\\", "\\")


# ───────────────────────── leitura independente do PDF ─────────────────────────


def pdf_regions(path: Path) -> tuple[list[dict], dict[int, str], int]:
    """Regiões de questão relidas do PDF. Cada região: tecId, número, páginas, palavras do corpo,
    figuras embutidas, desenhos vetoriais significativos."""
    doc = pymupdf.open(path)
    items = []  # (page, y, x, kind, payload)
    for pno, page in enumerate(doc):
        d = page.get_text("dict")
        for b in d["blocks"]:
            if b["type"] == 1:
                x0, y0, x1, y1 = b["bbox"]
                if (x1 - x0) > 6 and (y1 - y0) > 6:
                    items.append((pno, y0, x0, "img", (x1 - x0, y1 - y0, (x0, y0, x1, y1))))
                continue
            for ln in b["lines"]:
                prev_x1 = prev_sz = prev_base = None
                for s in ln["spans"]:
                    t = s["text"]
                    font = s["font"]
                    if font.startswith("ArialMT") or font.startswith("SourceSansPro"):
                        continue  # cabeçalho/rodapé do navegador e capa
                    if not t.strip():
                        prev_x1 = None  # espaço explícito: a próxima palavra começa separada
                        continue
                    # palavra partida em spans (letra colorida, negrito parcial): cola sem espaço
                    same_style = prev_sz is not None and abs(s["size"] - prev_sz) < 0.5 and abs(s["origin"][1] - prev_base) < 1.0
                    glue = prev_x1 is not None and same_style and s["bbox"][0] - prev_x1 <= 1.2 and not t[:1].isspace()
                    prev_x1, prev_sz, prev_base = s["bbox"][2], s["size"], s["origin"][1]
                    y = s["bbox"][1]
                    items.append((pno, y, s["bbox"][0], "span", (t, font, round(s["size"], 1), tuple(s["bbox"]), tuple(ln["bbox"]), glue)))
        for dr in page.get_drawings():
            r = dr["rect"]
            if r.width <= 1.6 and r.height <= 1.6:
                continue  # separador pontilhado
            if r.width <= 4.5 and r.height <= 4.5:
                continue  # marcador de lista
            if r.height <= 1.4 and r.width < 400:
                continue  # sublinhado
            fill = dr.get("fill")
            invisible = dr.get("color") is None and fill is not None and min(fill) >= 0.98
            # retângulo branco sem contorno (fundo de texto da página web): invisível no PDF
            items.append((pno, r.y0, r.x0, "white" if invisible else "draw", (r.width, r.height, (r.x0, r.y0, r.x1, r.y1))))
    pages = doc.page_count
    doc.close()
    items.sort(key=lambda t: (t[0], t[1], t[2]))
    regions: list[dict] = []
    cur = None
    gab_text: list[str] = []
    in_gab = False
    for pno, y, x, kind, payload in items:
        if in_gab:
            if kind == "span":
                gab_text.append(payload[0])
            continue
        if kind == "span":
            t, font, size, bbox, lbox, glue = payload
            if t.strip() == "Gabarito" and size >= 10:
                in_gab = True
                continue
            m = URL_RE.match(t)
            if m and "Bold" in font:
                cur = {"tecId": m.group(1), "pageStart": pno + 1, "pageEnd": pno + 1, "numero": None, "head": [], "body": [], "imgs": [], "draws": 0, "drawRects": [], "whiteRects": [], "math": 0, "mathText": [], "mathLines": set()}
                regions.append(cur)
                continue
            if cur is None:
                continue
            cur["pageEnd"] = pno + 1
            if 8.4 <= size <= 9.2 and font.startswith("Tahoma") and not cur["body"]:
                cur["head"].append(t)
                continue
            lm = LABEL_RE.match(t)
            if lm and "Bold" in font and x < 40 and cur["numero"] is None:
                cur["numero"] = int(lm.group(1))
                continue
            if font.startswith("Type3") or "Type3" in font:
                cur["math"] += 1
                cur["mathText"].append(t)
                cur["mathLines"].add((pno, round(lbox[1]), round(lbox[3])))
                continue
            cur["body"].append((t, pno, bbox, lbox, glue))
        elif cur is not None:
            cur["pageEnd"] = pno + 1
            if kind == "img":
                cur["imgs"].append(payload[:2])
                cur["drawRects"].append((pno, payload[2]))
            elif kind == "white":
                cur["whiteRects"].append((pno, payload[2]))
            else:
                cur["draws"] += 1
                cur["drawRects"].append((pno, payload[2]))
    gab: dict[int, str] = {}
    for m in GAB_RE.finditer(" ".join(gab_text)):
        gab[int(m.group(1))] = m.group(2)
    return regions, gab, pages


def _near(b: tuple, r: tuple, pad: float = 3.0) -> bool:
    return not (b[2] < r[0] - pad or b[0] > r[2] + pad or b[3] < r[1] - pad or b[1] > r[3] + pad)


def body_words(region: dict) -> tuple[Counter, Counter, Counter]:
    """(todas as palavras do corpo, palavras em zona visual — tabela/figura vetorial ou linha com fórmula —,
    palavras sobre retângulo branco invisível). Zona visual pode legitimamente ter virado recorte."""
    # junta os spans colados (palavra partida) antes de contar
    pieces: list[list] = []
    for t, pno, bbox, lbox, glue in region["body"]:
        if glue and pieces and pieces[-1][1] == pno and pieces[-1][3] == lbox:
            pieces[-1][0] += t
            b0 = pieces[-1][2]
            pieces[-1][2] = (min(b0[0], bbox[0]), min(b0[1], bbox[1]), max(b0[2], bbox[2]), max(b0[3], bbox[3]))
        else:
            pieces.append([t, pno, bbox, lbox])
    allw: Counter = Counter()
    vis: Counter = Counter()
    white: Counter = Counter()
    for t, pno, bbox, lbox in pieces:
        t2 = re.sub(r"^\s*[a-e]\)\s*", " ", t)
        w = words(t2)
        allw.update(w)
        on_math_line = any(p == pno and not (lbox[3] < y0 - 2 or lbox[1] > y1 + 2) for p, y0, y1 in region["mathLines"])
        in_draw = any(p == pno and _near(bbox, r) for p, r in region["drawRects"])
        if on_math_line or in_draw:
            vis.update(w)
        elif any(p == pno and _near(bbox, r, 0.5) for p, r in region["whiteRects"]):
            white.update(w)
    return allw, vis, white


# ───────────────────────── acervo extraído ─────────────────────────


def load_acervo(ext_dir: Path | None = None) -> tuple[dict[str, dict], list[dict], dict[str, list[str]]]:
    man = json.loads((DOCS / ".importadas.json").read_text(encoding="utf-8"))
    cadernos = []
    for sha, e in man["cadernos"].items():
        p = (ext_dir or DOCS / ".extraidas") / f"{sha}.json"
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            d["_ordem"] = e.get("extraidoEm", "")
            cadernos.append(d)
    cadernos.sort(key=lambda d: d["_ordem"])
    acervo: dict[str, dict] = {}
    em: dict[str, list[str]] = defaultdict(list)
    for d in cadernos:
        for q in d["questoes"]:
            q["_arquivo"] = d["arquivo"]
            acervo[q["tecId"]] = q
            em[q["tecId"]].append(d["arquivo"])
    return acervo, cadernos, em


def ext_text(q: dict) -> str:
    return " ".join([q.get("support") or "", q.get("statement") or ""] + [o.get("text", "") for o in q.get("options", [])])


def check_question(q: dict, reg: dict | None) -> dict:
    """Checagens de uma ocorrência (questão extraída de um caderno × região relida do mesmo PDF)."""
    md = ext_text(q)
    figs = [a for a, _ in MD_IMG.findall(md)]
    n_fig = sum(1 for a in figs if a == "Figura")
    n_crop = len(figs) - n_fig
    flags: list[str] = []
    res = {"figurasVinculadas": n_fig, "recortes": n_crop}
    # contaminação por metadados
    for name, rx in CHROME_PATTERNS:
        if rx.search(plain(md)):
            flags.append(f"contaminacao:{name}")
    # alternativas
    labels = [o["label"] for o in q.get("options", [])]
    texts = [plain(o.get("text", "")).strip() for o in q.get("options", [])]
    if q["kind"] == "CERTO_ERRADO":
        if labels != ["C", "E"]:
            flags.append("alternativas:CE_invalido")
    else:
        if labels not in (list("ABCD"), list("ABCDE")):
            flags.append(f"alternativas:rotulos_{''.join(labels)}")
        if any(not t and not MD_IMG.search(o.get("text", "")) for t, o in zip(texts, q.get("options", []))):
            flags.append("alternativas:vazia")
        raw = [o.get("text", "").strip() for o in q.get("options", [])]
        if len(set(raw)) < len(raw):
            flags.append("alternativas:duplicada")
        if q.get("answer") not in labels and not q.get("anulada"):
            flags.append("gabarito:sem_alternativa")
    if not plain(q.get("statement") or "").strip() and not plain(q.get("support") or "").strip():
        flags.append("enunciado:vazio")
    if reg is None:
        flags.append("regiao:nao_encontrada_no_pdf")
        res.update(flags=flags)
        return res
    res["pageStart"], res["pageEnd"] = reg["pageStart"], reg["pageEnd"]
    if reg["numero"] != q.get("numero"):
        flags.append(f"numero:pdf={reg['numero']}_extraido={q.get('numero')}")
    pdfw = body_words(reg)
    extw = words(plain(md))
    pdfw, visw, whitew = pdfw
    mathw = words(" ".join(reg["mathText"]))
    missing = pdfw - extw
    extra = extw - pdfw - mathw  # fórmula simples (Type3) pode ter virado texto
    missing_real = missing - visw - whitew  # o que falta fora de tabelas/figuras/fórmulas/fundos
    missing_white = (missing - visw) - missing_real  # texto comum que virou imagem por causa do fundo branco
    tot = sum(pdfw.values()) or 1
    res["palavrasPdf"] = sum(pdfw.values())
    res["faltando"] = sum(missing.values())
    res["sobrando"] = sum(extra.values())
    res["coberturaPct"] = round(100 * (1 - res["faltando"] / tot), 2)
    res["faltandoForaDeZonaVisual"] = sum(missing_real.values())
    res["faltandoEmFundoInvisivel"] = sum(missing_white.values())
    res["faltandoAmostra"] = " ".join(w for w, _ in (missing_real or missing).most_common(12))
    res["sobrandoAmostra"] = " ".join(w for w, _ in extra.most_common(12))
    # figuras embutidas na região (ignorando ícones minúsculos)
    big_imgs = [wh for wh in reg["imgs"] if wh[0] * wh[1] >= 400]
    res["figurasNoPdf"] = len(big_imgs)
    res["desenhosNoPdf"] = reg["draws"]
    res["glifosFormula"] = reg["math"]
    if res["faltandoForaDeZonaVisual"] >= 2:
        flags.append("texto:perda")
    if res["faltandoEmFundoInvisivel"] >= 2:
        # o extrator tratou o fundo branco (invisível) como figura vetorial: o parágrafo virou imagem
        flags.append("texto:virou_imagem_fundo_invisivel" if (n_fig or n_crop) else "texto:perda_fundo_invisivel")
    vis_missing = res["faltando"] - res["faltandoForaDeZonaVisual"] - res["faltandoEmFundoInvisivel"]
    if vis_missing > 0 and vis_missing / tot > 0.02:
        flags.append("texto:em_recorte" if (n_crop or n_fig) else "texto:zona_visual_sem_recorte")
    if res["sobrando"] > 3 and res["sobrando"] / tot > 0.02:
        flags.append("texto:sobra")
    if len(big_imgs) > n_fig + n_crop:
        flags.append("figura:ausente")
    if reg["draws"] >= 4 and n_crop == 0 and n_fig == 0:
        flags.append("vetorial:sem_recorte")
    if reg["math"] and n_crop == 0 and "<sup>" not in md and "<sub>" not in md:
        # fórmula simples pode virar texto; só sinaliza quando há muitos glifos e nenhum recorte
        if reg["math"] >= 6:
            flags.append("formula:sem_recorte")
    if FIG_WORDS.search(plain(md)) and n_fig == 0 and n_crop == 0 and not big_imgs and reg["draws"] < 4:
        flags.append("referencia_visual:sem_figura_na_regiao")
    res["flags"] = flags
    return res


# ───────────────────────── banco (backup) ─────────────────────────


def load_backup(d: Path) -> tuple[dict[str, dict], dict[str, list[dict]], set[str], dict[str, int]]:
    qs = {}
    for ln in (d / "Question.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            r = json.loads(ln)
            qs[r["id"]] = r
    opts: dict[str, list[dict]] = defaultdict(list)
    for ln in (d / "QuestionOption.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            r = json.loads(ln)
            opts[r["questionId"]].append(r)
    imgs = set()
    for ln in (d / "QuestionImage.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            imgs.add(json.loads(ln)["id"])
    answers: dict[str, int] = Counter()
    for ln in (d / "QuizAnswer.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            answers[json.loads(ln)["questionId"]] += 1
    return qs, opts, imgs, answers


def latest_backup() -> Path | None:
    cands = sorted((ROOT / "backups").glob("questoes-remoto-*"))
    return cands[-1] if cands else None


# ───────────────────────── principal ─────────────────────────


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", delimiter=";")
        w.writeheader()
        for r in rows:
            w.writerow({k: (", ".join(v) if isinstance(v, list) else v) for k, v in r.items()})


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backup", help="pasta do backup (scripts/questoes-backup.ts); padrão: o mais recente do remoto")
    ap.add_argument("--saida")
    ap.add_argument("--so", help="só o caderno cujo nome contém este texto (extração)")
    ap.add_argument("--sem-classificacao", action="store_true")
    ap.add_argument("--extraidas", help="pasta alternativa com a extração (<sha>.json e img/), ex.: reextração de teste")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    out = Path(args.saida) if args.saida else DOCS / "auditoria" / date.today().isoformat()
    out.mkdir(parents=True, exist_ok=True)

    ext_dir = Path(args.extraidas) if args.extraidas else None
    acervo, cadernos, em = load_acervo(ext_dir)
    by_file = {d["arquivo"]: d for d in cadernos}

    # 1. inventário + extração (cada ocorrência, em cada caderno)
    inv, ext_rows = [], []
    occ_flags: dict[str, list[str]] = defaultdict(list)
    for pdf in sorted(DOCS.glob("*.pdf")):
        if args.so and args.so not in pdf.name:
            continue
        sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        regions, gab, pages = pdf_regions(pdf)
        d = by_file.get(pdf.name)
        extracted = d["questoes"] if d else []
        reg_by_id = {r["tecId"]: r for r in regions}
        nums = [r["numero"] for r in regions if r["numero"] is not None]
        inv.append(
            {
                "arquivo": pdf.name,
                "sha256": sha,
                "paginas": pages,
                "links": len(regions),
                "linksUnicos": len(reg_by_id),
                "numeros": len(nums),
                "numerosUnicos": len(set(nums)),
                "gabarito": len(gab),
                "anuladasGabarito": sum(1 for v in gab.values() if v == "Anulada"),
                "extraidas": len(extracted),
                "extraidoMesmoSha": bool(d and d["sha256"] == sha),
                "anomaliasExtrator": "; ".join(d["anomalias"]) if d else "NÃO EXTRAÍDO",
                "linksSemExtracao": len(set(reg_by_id) - {q["tecId"] for q in extracted}),
                "extraidasSemLink": len({q["tecId"] for q in extracted} - set(reg_by_id)),
                "materias": "; ".join(f"{m} ({n})" for m, n in Counter(q["materia"] for q in extracted).most_common()),
            }
        )
        for q in extracted:
            r = check_question(q, reg_by_id.get(q["tecId"]))
            gv = gab.get(q.get("numero")) if q.get("numero") is not None else None
            if gv is not None and gv != q.get("gabaritoRaw"):
                r["flags"].append(f"gabarito:pdf={gv}_extraido={q.get('gabaritoRaw')}")
            row = {
                "tecId": q["tecId"],
                "url": f"https://www.tecconcursos.com.br/questoes/{q['tecId']}",
                "arquivo": pdf.name,
                "numero": q.get("numero"),
                "materia": q["materia"],
                "assunto": q["assunto"],
                "ano": q.get("ano"),
                "kind": q["kind"],
                "anulada": q["anulada"],
                "quarentena": "; ".join(q.get("problems") or []),
                **r,
            }
            row["flags"] = "|".join(r["flags"])
            ext_rows.append(row)
            if r["flags"]:
                occ_flags[q["tecId"]].extend(r["flags"])
        print(f"{pdf.name}: {len(regions)} regiões, {len(extracted)} extraídas", flush=True)

    write_csv(out / "inventario.csv", inv, list(inv[0].keys()))
    ext_fields = [
        "tecId", "url", "arquivo", "numero", "pageStart", "pageEnd", "materia", "assunto", "ano", "kind", "anulada", "quarentena",
        "palavrasPdf", "faltando", "faltandoForaDeZonaVisual", "faltandoEmFundoInvisivel", "sobrando", "coberturaPct", "faltandoAmostra", "sobrandoAmostra", "figurasNoPdf",
        "figurasVinculadas", "recortes", "desenhosNoPdf", "glifosFormula", "flags",
    ]
    write_csv(out / "extracao.csv", ext_rows, ext_fields)

    # 2. figuras: arquivos locais e banco
    img_dir = (ext_dir or DOCS / ".extraidas") / "img"
    backup_dir = Path(args.backup) if args.backup else latest_backup()
    db_q, db_opts, db_imgs, db_answers = load_backup(backup_dir) if backup_dir else ({}, {}, set(), Counter())
    img_report = {"questoesComFigura": 0, "referencias": 0, "arquivoLocalAusente": [], "ausenteNoBanco": [], "questoesSemFiguraNaRegiao": []}
    for tid, q in acervo.items():
        refs = [s for _, s in MD_IMG.findall(ext_text(q))]
        if not refs:
            continue
        img_report["questoesComFigura"] += 1
        img_report["referencias"] += len(refs)
        for s in refs:
            if not (img_dir / f"{s}.png").exists():
                img_report["arquivoLocalAusente"].append([tid, s])
            dbq = db_q.get(f"tec_{tid}")
            if dbq and dbq["status"] != "RETIRED" and s not in db_imgs:
                img_report["ausenteNoBanco"].append([tid, s])
    # referências quebradas no próprio banco (texto aponta para figura inexistente)
    broken = []
    for qid, r in db_q.items():
        txt = " ".join([r.get("statement") or "", r.get("support") or ""] + [o["text"] for o in db_opts.get(qid, [])])
        for s in re.findall(r"/q-img/([0-9a-f]{64})", txt):
            if s not in db_imgs:
                broken.append([qid, s, r["status"]])
    img_report["referenciasQuebradasNoBanco"] = broken
    flagged_fig = sorted({t for t, fl in occ_flags.items() if any(f.startswith(("figura:", "vetorial:", "referencia_visual:", "formula:")) for f in fl)})
    img_report["questoesComAlertaVisual"] = flagged_fig
    (out / "imagens.json").write_text(json.dumps(img_report, ensure_ascii=False, indent=1), encoding="utf-8")

    # 3. taxonomia do TEC (questões únicas)
    from questoes.classify import Classifier, assunto_key, load_catalog, load_map

    mapa = load_map()
    tax: dict[str, dict] = {}
    for tid, q in acervo.items():
        k = assunto_key(q["materia"], q["assunto"])
        t = tax.setdefault(k, {"materia": q["materia"], "assunto": q["assunto"], "questoes": 0, "anuladas": 0, "arquivos": Counter(), "anos": Counter(), "ce": 0})
        t["questoes"] += 1
        t["anuladas"] += int(q["anulada"])
        t["ce"] += int(q["kind"] == "CERTO_ERRADO")
        t["anos"][q.get("ano")] += 1
        for f in set(em[tid]):
            t["arquivos"][f] += 1
    tax_rows = []
    for k, t in sorted(tax.items(), key=lambda kv: (kv[1]["materia"], -kv[1]["questoes"])):
        entry = mapa.get("assuntos", {}).get(k)
        mat = mapa.get("materias", {}).get(t["materia"])
        if entry is None:
            cur = "SEM CURADORIA (automático)" if mat else "MATÉRIA SEM MAPA"
        elif "skip" in entry:
            cur = f"skip: {entry['skip']}"
        elif "segments" in entry:
            cur = "trechos: " + ", ".join(entry["segments"])
        else:
            cur = (f"{entry['subject']} · " if entry.get("subject") else "") + "aulas: " + ", ".join(entry.get("aulas", []))
        anos = sorted(a for a in t["anos"] if a)
        tax_rows.append(
            {
                "materia": t["materia"],
                "assunto": t["assunto"] or "(vazio)",
                "disciplinaSite": (mat if isinstance(mat, str) else (mat or {}).get("subject")) or "",
                "questoes": t["questoes"],
                "anuladas": t["anuladas"],
                "certoErrado": t["ce"],
                "anos": f"{anos[0]}–{anos[-1]}" if anos else "",
                "arquivos": "; ".join(f"{f} ({n})" for f, n in t["arquivos"].most_common()),
                "curadoriaAtual": cur,
            }
        )
    write_csv(out / "taxonomia_tec.csv", tax_rows, list(tax_rows[0].keys()))

    # 4. classificação recalculada × produção
    cls_rows, recon = [], Counter()
    status_matrix: Counter = Counter()
    if not args.sem_classificacao:
        print("carregando índice do classificador …", flush=True)
        clf = Classifier(load_catalog(), mapa)
        valid = {k: q for k, q in acervo.items() if not q["problems"] and not q["anulada"]}
        clf.vote_assuntos(list(valid.values()))
        for tid, q in acervo.items():
            qid = f"tec_{tid}"
            dbq = db_q.get(qid)
            if q["problems"]:
                exp = {"status": "QUARENTENA"}
            elif q["anulada"]:
                exp = {"status": "ANULADA"}
            else:
                r = clf.classify(q)
                exp = {"status": r.status, "subjectId": r.subjectId, "aulaId": r.aulaId, "segmentId": r.segmentId, "editalItemId": r.editalItemId, "reason": r.reason, "score": r.score}
            db_status = dbq["status"] if dbq else "AUSENTE"
            status_matrix[(exp["status"], db_status)] += 1
            row = {
                "tecId": tid,
                "materia": q["materia"],
                "assunto": q["assunto"],
                "ano": q.get("ano"),
                "esperado": exp["status"],
                "esperadoDisciplina": exp.get("subjectId"),
                "esperadoTrecho": exp.get("segmentId"),
                "esperadoItemEdital": exp.get("editalItemId"),
                "motivo": exp.get("reason", ""),
                "banco": db_status,
                "bancoDisciplina": dbq["subjectId"] if dbq else "",
                "bancoTrecho": dbq["segmentId"] if dbq else "",
                "bancoItemEdital": (dbq or {}).get("editalItemId") or "",
                "bancoClassifiedBy": dbq["classifiedBy"] if dbq else "",
                "respostas": db_answers.get(qid, 0),
                "conteudoDivergente": bool(dbq and dbq.get("contentHash") != q.get("contentHash")),
            }
            if dbq and exp["status"] in ("APPROVED", "DRAFT") and db_status != "RETIRED":
                row["trechoDivergente"] = dbq["segmentId"] != exp.get("segmentId")
                row["disciplinaDivergente"] = dbq["subjectId"] != exp.get("subjectId")
                recon["trecho_divergente"] += int(row["trechoDivergente"])
                recon["disciplina_divergente"] += int(row["disciplinaDivergente"])
            recon["conteudo_divergente"] += int(row["conteudoDivergente"])
            cls_rows.append(row)
        write_csv(out / "classificacao.csv", cls_rows, list(cls_rows[0].keys()) + ["trechoDivergente", "disciplinaDivergente"])
    orphans = sorted(set(db_q) - {f"tec_{t}" for t in acervo})
    recon_out = {
        "backup": str(backup_dir) if backup_dir else None,
        "acervoUnico": len(acervo),
        "ocorrencias": sum(len(v) for v in em.values()),
        "duplicadasEntreCadernos": sum(len(v) - 1 for v in em.values() if len(v) > 1),
        "questoesNoBanco": len(db_q),
        "noBancoForaDoAcervo": orphans,
        "matrizEsperadoXBanco": {f"{a} → {b}": n for (a, b), n in sorted(status_matrix.items())},
        **recon,
        "respostasDeAlunosEmQuestoes": dict(db_answers),
    }
    (out / "reconciliacao.json").write_text(json.dumps(recon_out, ensure_ascii=False, indent=1), encoding="utf-8")

    flag_count: Counter = Counter()
    for r in ext_rows:
        for f in filter(None, r["flags"].split("|")):
            flag_count[f.split("_pdf=")[0] if f.startswith(("numero:", "gabarito:pdf")) else f] += 1
    resumo = {
        "cadernos": len(inv),
        "paginas": sum(r["paginas"] for r in inv),
        "links": sum(r["links"] for r in inv),
        "extraidas": sum(r["extraidas"] for r in inv),
        "linksSemExtracao": sum(r["linksSemExtracao"] for r in inv),
        "unicas": len(acervo),
        "alertasExtracao": dict(flag_count.most_common()),
        "ocorrenciasComAlerta": sum(1 for r in ext_rows if r["flags"]),
        "imagens": {k: (len(v) if isinstance(v, list) else v) for k, v in img_report.items()},
        "reconciliacao": {k: (len(v) if isinstance(v, (list, dict)) and k != "matrizEsperadoXBanco" else v) for k, v in recon_out.items()},
    }
    (out / "resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resumo, ensure_ascii=False, indent=1))
    print(f"saída: {out}")


if __name__ == "__main__":
    main()
