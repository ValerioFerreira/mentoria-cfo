"""Extrator geométrico dos cadernos "imprimir caderno" do TecConcursos.

A especificação completa (zonas da página, assinaturas de fonte/posição, marcação emitida,
recortes, gabarito e invariantes) está em pipeline/questoes/EXTRACAO.md. Este módulo só lê o
PDF e devolve as questões cruas; classificação e gravação ficam em classify.py e importar.py.
"""
from __future__ import annotations

import hashlib
import io
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf

# Muda quando a lógica de extração muda: o importador reextrai os cadernos de versão anterior.
EXTRACTOR_VERSION = "2026.10.14-1"

URL_RE = re.compile(r"^www\.tecconcursos\.com\.br/questoes/(\d+)\s*$")
LABEL_RE = re.compile(r"^(\d+)\)\s*$")
OPT_RE = re.compile(r"^([a-e])\)\s*")
GAB_ENTRY_RE = re.compile(r"(\d+)\)\s*([A-Za-zÀ-ú]+)")
YEAR_TAIL_RE = re.compile(r"/(\d{4})\s*$")

HEAD_SIZE = (8.4, 9.2)  # Tahoma 8.8: cabeçalho (banca/cargo/órgão/ano e matéria - assunto)
GAB_TITLE_SIZE = (10.5, 11.5)  # "Gabarito" Tahoma 11.0
X_LABEL_MAX = 40  # número "NNNN)" fica em x≈28
X_OPT = (40.0, 50.0)  # alternativas "a)" e "Certo"/"Errado" em x≈46
BODY_SIZE = 7.2
OPT_LABEL_W = 7.0  # largura de "a)" em Tahoma 7,2
BULLET_MIN_H = 1.5  # marcador de lista tem altura; traço curto mais fino que isso é sublinhado de letra
PARA_GAP = 3.0  # espaço vertical (pt) entre linhas que indica novo parágrafo
CROP_DPI = 200
CROP_PAD = 2.0
MAX_IMG_SIDE = 1600

GAB_VALUES = {"A", "B", "C", "D", "E", "Certo", "Errado", "Anulada"}


@dataclass
class Span:
    text: str
    font: str
    size: float
    flags: int
    bbox: tuple[float, float, float, float]
    origin_y: float
    color: int = 0
    chars: list[tuple[str, float, float]] = field(default_factory=list)  # (caractere, x0, x1)
    ul: set[int] = field(default_factory=set)  # índices de caracteres sublinhados

    @property
    def is_mono(self) -> bool:
        return self.font.startswith(("Courier", "Consolas"))

    @property
    def is_math(self) -> bool:
        return self.font.startswith("Type3")

    @property
    def is_bold(self) -> bool:
        return "Bold" in self.font or bool(self.flags & 16)


@dataclass
class Frag:
    """Uma linha do PyMuPDF (texto), uma imagem embutida ou um traço vetorial."""

    kind: str  # text | image | draw
    page: int
    bbox: tuple[float, float, float, float]
    spans: list[Span] = field(default_factory=list)
    xref: int = 0

    @property
    def text(self) -> str:
        return "".join(s.text for s in self.spans)

    @property
    def y0(self) -> float:
        return self.bbox[1]

    @property
    def y1(self) -> float:
        return self.bbox[3]

    @property
    def x0(self) -> float:
        return self.bbox[0]

    @property
    def x1(self) -> float:
        return self.bbox[2]

    @property
    def h(self) -> float:
        return max(0.1, self.bbox[3] - self.bbox[1])

    @property
    def has_math(self) -> bool:
        return any(s.is_math for s in self.spans)


@dataclass
class Asset:
    """Figura extraída ou recorte renderizado (PNG)."""

    sha: str
    data: bytes
    width: int
    height: int
    kind: str  # figura | recorte


@dataclass
class RawQuestion:
    tec_id: str
    numero: int | None = None
    banca_line: str = ""
    materia_line: str = ""
    page: int = 0
    frags: list[Frag] = field(default_factory=list)
    head_frags: list[Frag] = field(default_factory=list)


@dataclass
class Question:
    tecId: str
    numero: int | None
    bancaRaw: str
    banca: str
    cargo: str
    orgao: str
    area: str
    ano: int | None
    materia: str
    assunto: str
    support: str
    statement: str
    options: list[dict]
    kind: str  # MULTIPLA_ESCOLHA | CERTO_ERRADO
    answer: str | None  # rótulo correto ("A".."E", "C"/"E" no C/E)
    anulada: bool
    gabaritoRaw: str | None
    page: int
    assets: list[str]
    problems: list[str]
    warnings: list[str]


# ───────────────────────── leitura da página ─────────────────────────


def _is_control(ch: str) -> bool:
    o = ord(ch) if len(ch) == 1 else 32
    return o < 32 or 0x7F <= o <= 0x9F


def _is_chrome(span: dict) -> bool:
    """Cabeçalho/rodapé do navegador (ArialMT 8) e capa (SourceSansPro)."""
    f = span["font"]
    return f.startswith("ArialMT") or f.startswith("SourceSansPro")


def page_frags(page: pymupdf.Page, pno: int) -> list[Frag]:
    out: list[Frag] = []
    d = page.get_text("rawdict")
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for ln in b["lines"]:
            spans = []
            for s in ln["spans"]:
                # caracteres de controle (NUL etc.) aparecem em alguns glifos e o Postgres recusa
                chars = [(c["c"], c["bbox"][0], c["bbox"][2]) for c in s["chars"] if not _is_control(c["c"])]
                text = "".join(c[0] for c in chars)
                if text == "" or _is_chrome(s):
                    continue
                spans.append(
                    Span(
                        text=text,
                        font=s["font"],
                        size=round(s["size"], 1),
                        flags=s["flags"],
                        bbox=tuple(s["bbox"]),
                        origin_y=s["origin"][1],
                        color=s.get("color", 0) or 0,
                        chars=chars,
                    )
                )
            if not spans or not "".join(s.text for s in spans).strip():
                # linhas só de espaço não carregam informação (mas espaços em math são ignorados)
                continue
            x0 = min(s.bbox[0] for s in spans)
            y0 = min(s.bbox[1] for s in spans)
            x1 = max(s.bbox[2] for s in spans)
            y1 = max(s.bbox[3] for s in spans)
            out.append(Frag("text", pno, (x0, y0, x1, y1), spans))
    for im in page.get_image_info(xrefs=True):
        x0, y0, x1, y1 = im["bbox"]
        if x1 - x0 < 2 or y1 - y0 < 2:
            continue
        out.append(Frag("image", pno, (x0, y0, x1, y1), xref=im.get("xref", 0)))
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.width <= 1.6 and r.height <= 1.6:
            continue  # pontilhado separador de questões (quadradinhos 1×1)
        if is_invisible_fill(dr):
            continue  # fundo branco sem contorno atrás do texto: invisível, não é tabela nem figura
        if r.width <= 4.5 and BULLET_MIN_H <= r.height <= 4.5 and dr.get("fill") is not None:
            # marcador de lista desenhado (bolinha/quadradinho): vira "•"
            sp = Span("•", "Tahoma", BODY_SIZE, 0, (r.x0, r.y0, r.x1, r.y1), r.y1 + 1.5, chars=[("•", r.x0, r.x1)])
            out.append(Frag("text", pno, (r.x0, r.y0 - 2.5, r.x1, r.y1 + 2.5), [sp]))
            continue
        out.append(Frag("draw", pno, (r.x0, r.y0, r.x1, r.y1)))
    return out


def is_invisible_fill(dr: dict) -> bool:
    """Retângulo preenchido de branco e sem traço: fundo de texto copiado da página web. Tratá-lo como
    desenho transformava parágrafos comuns em imagem."""
    fill = dr.get("fill")
    return dr.get("color") is None and fill is not None and min(fill) >= 0.98


def _is_url(f: Frag) -> re.Match | None:
    if f.kind != "text":
        return None
    return URL_RE.match(f.text.strip())


def _is_head(f: Frag) -> bool:
    return (
        f.kind == "text"
        and all(not s.is_math for s in f.spans)
        and HEAD_SIZE[0] <= f.spans[0].size <= HEAD_SIZE[1]
        and f.spans[0].font.startswith("Tahoma")
    )


def _is_label(f: Frag) -> re.Match | None:
    if f.kind != "text" or f.x0 > X_LABEL_MAX:
        return None
    s = f.spans[0]
    if not s.is_bold:
        return None
    return LABEL_RE.match(f.text.strip())


def _split_label(f: Frag) -> tuple[int, Frag | None] | None:
    """"NNNN)" em negrito como primeiro span de uma linha de texto: (número, resto da linha)."""
    if f.kind != "text" or f.x0 > X_LABEL_MAX or not f.spans or not f.spans[0].is_bold:
        return None
    m = LABEL_RE.match(f.spans[0].text.strip())
    if not m:
        return None
    rest = [s for s in f.spans[1:] if s.text.strip()]
    if not rest:
        return int(m.group(1)), None
    bbox = (min(s.bbox[0] for s in rest), min(s.bbox[1] for s in rest), max(s.bbox[2] for s in rest), max(s.bbox[3] for s in rest))
    return int(m.group(1)), Frag("text", f.page, bbox, rest)


def _is_gab_title(f: Frag) -> bool:
    return (
        f.kind == "text"
        and f.text.strip() == "Gabarito"
        and GAB_TITLE_SIZE[0] <= f.spans[0].size <= GAB_TITLE_SIZE[1]
    )


# ───────────────────────── caderno → questões cruas ─────────────────────────


@dataclass
class Caderno:
    path: Path
    title: str
    questions: list[Question]
    gabarito: dict[int, str]
    assets: dict[str, Asset]
    anomalies: list[str]
    pages: int


def _ycenter(f: Frag) -> float:
    return (f.bbox[1] + f.bbox[3]) / 2


def split_questions(doc: pymupdf.Document) -> tuple[list[RawQuestion], dict[int, str], list[str], str]:
    raws: list[RawQuestion] = []
    gabarito: dict[int, str] = {}
    anomalies: list[str] = []
    title = ""
    cur: RawQuestion | None = None
    in_gab = False
    gab_text: list[str] = []
    for pno, page in enumerate(doc):
        frags = page_frags(page, pno)
        if pno == 0:
            for b in page.get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    for s in ln["spans"]:
                        if s["font"].startswith("SourceSansPro") and not title:
                            title = s["text"].strip()
        frags.sort(key=lambda f: (_ycenter(f), f.x0))
        for f in frags:
            if in_gab:
                if f.kind == "text":
                    gab_text.append(f.text)
                continue
            if _is_gab_title(f):
                in_gab = True
                continue
            m = _is_url(f)
            if m:
                cur = RawQuestion(tec_id=m.group(1), page=pno + 1)
                raws.append(cur)
                continue
            if cur is None:
                continue  # capa (logo, título, link do caderno, ordenação)
            if f.kind == "text" and not cur.frags and _is_head(f):
                cur.head_frags.append(f)
                continue
            lab = _is_label(f)
            if lab and cur.numero is None:
                cur.numero = int(lab.group(1))
                continue
            if cur.numero is None and not cur.frags:
                # número colado ao enunciado na mesma linha (acontece no topo de página): separa o span
                split = _split_label(f)
                if split:
                    cur.numero, f = split
            if f is None:
                continue
            cur.frags.append(f)
    for t in gab_text:
        for m in GAB_ENTRY_RE.finditer(t):
            n, v = int(m.group(1)), m.group(2)
            if n in gabarito and gabarito[n] != v:
                anomalies.append(f"gabarito: número {n} aparece duas vezes ({gabarito[n]} / {v})")
            gabarito[n] = v
    if not in_gab:
        anomalies.append("caderno sem a seção 'Gabarito'")
    return raws, gabarito, anomalies, title


# ───────────────────────── linhas visuais e recortes ─────────────────────────


@dataclass
class Row:
    page: int
    frags: list[Frag]
    crop: bool = False
    reason: str = ""
    clip_x0: float | None = None  # recorte começa depois do rótulo "a)" quando ele divide o span
    inline: bool = False  # texto com fórmulas MathJax recortadas no meio da frase

    @property
    def bbox(self) -> tuple[float, float, float, float]:
        fs = self.frags
        return (min(f.x0 for f in fs), min(f.y0 for f in fs), max(f.x1 for f in fs), max(f.y1 for f in fs))

    @property
    def texts(self) -> list[Frag]:
        return [f for f in self.frags if f.kind == "text"]


def _overlap(a: Frag | tuple, b: Frag | tuple) -> float:
    ay0, ay1 = (a.y0, a.y1) if isinstance(a, Frag) else a
    by0, by1 = (b.y0, b.y1) if isinstance(b, Frag) else b
    inter = min(ay1, by1) - max(ay0, by0)
    if inter <= 0:
        return 0.0
    return inter / max(0.1, min(ay1 - ay0, by1 - by0))


def _band(r: list[Frag]) -> tuple[float, float]:
    return (min(x.y0 for x in r), max(x.y1 for x in r))


LINE_START_X = 56.0  # texto que começa linha (x 28–52); fórmulas e continuações ficam à direita


def _starts_line(r: list[Frag]) -> bool:
    return any(f.kind == "text" and not all(s.is_math for s in f.spans) and f.x0 <= LINE_START_X for f in r)


def build_rows(frags: list[Frag]) -> list[Row]:
    """Agrupa os fragmentos de uma página em linhas visuais.

    1. Linhas-âncora: fragmentos de texto comum (Tahoma), agrupados por sobreposição vertical.
    2. Fórmulas (só Type3) e figuras entram na âncora com maior sobreposição; sem sobreposição,
       formam linhas próprias (fórmula em bloco).
    3. Linhas que passaram a se sobrepor se fundem, exceto quando as duas começam linha de texto
       (ex.: alternativas a) e b) com frações altas continuam separadas).
    """
    draws = [f for f in frags if f.kind == "draw"]
    anchors_src = [f for f in frags if f.kind == "text" and not all(s.is_math for s in f.spans)]
    floats = [f for f in frags if f.kind == "image" or (f.kind == "text" and all(s.is_math for s in f.spans))]
    anchors_src.sort(key=lambda f: f.y0)
    rows: list[list[Frag]] = []
    for f in anchors_src:
        for r in reversed(rows[-4:]):
            if _overlap(f, _band(r)) >= 0.4:
                r.append(f)
                break
        else:
            rows.append([f])
    base_bands = [_band(r) for r in rows]
    loose: list[Frag] = []
    for f in sorted(floats, key=lambda f: f.y0):
        best, best_ov = None, 0.0
        for i, b in enumerate(base_bands):
            ov = _overlap(f, b)
            if ov > best_ov:
                best, best_ov = i, ov
        if best is not None and (best_ov >= 0.25 or f.kind == "text"):
            if f.kind == "image" and best_ov < 0.4:
                loose.append(f)
            else:
                rows[best].append(f)
        else:
            loose.append(f)
    for f in loose:
        for r in rows:
            if r and all(x.kind != "text" or all(s.is_math for s in x.spans) for x in r) and _overlap(f, _band(r)) > 0:
                r.append(f)
                break
        else:
            rows.append([f])
    rows.sort(key=lambda r: _band(r)[0])
    merged: list[list[Frag]] = []
    for r in rows:
        if merged:
            pb = _band(merged[-1])
            if _overlap(_band(r), pb) >= 0.4 and not (_starts_line(r) and _starts_line(merged[-1])):
                merged[-1].extend(r)
                continue
        merged.append(r)
    out = [Row(page=r[0].page, frags=sorted(r, key=lambda f: f.x0)) for r in merged]
    _attach_draws(out, draws)
    return out


def _attach_draws(rows: list[Row], draws: list[Frag]) -> None:
    """Sublinhado vira <u>; qualquer outro traço (tabela, fração, moldura) força recorte."""
    for d in draws:
        dh = d.y1 - d.y0
        hit = [r for r in rows if r.bbox[1] - 3 <= d.y1 and d.y0 <= r.bbox[3] + 3]
        if not hit:
            # borda de tabela um pouco acima/abaixo do texto da célula
            hit = [r for r in rows if r.bbox[1] - 7 <= d.y1 and d.y0 <= r.bbox[3] + 7 and r.crop][:1]
        if not hit:
            continue
        if dh <= 1.3 and len(hit) <= 2:
            # traço horizontal fino: sublinhado se estiver logo abaixo do texto de uma linha sem fórmula
            for r in hit:
                for f in r.texts:
                    if f.has_math:
                        continue
                    marked = False
                    for s in f.spans:
                        base = s.origin_y
                        if base - 1.5 <= d.y0 <= base + 3.0 and s.bbox[0] < d.x1 - 1 and d.x0 < s.bbox[2] - 1:
                            for k, (_, cx0, cx1) in enumerate(s.chars):
                                if d.x0 - 0.5 <= (cx0 + cx1) / 2 <= d.x1 + 0.5:
                                    s.ul.add(k)
                                    marked = True
                    if marked:
                        break
                else:
                    continue
                break
            else:
                for r in hit:
                    r.crop, r.reason = True, "traço"
                    r.frags.append(d)
            continue
        for r in hit:
            r.crop, r.reason = True, "tabela/figura vetorial"
            r.frags.append(d)




def _bad_chars(t: str) -> bool:
    return any(0xE000 <= ord(c) <= 0xF8FF or c == "�" for c in t)


def classify_row(row: Row) -> None:
    """Decide o modo da linha: texto, texto com fórmulas embutidas (recortes inline) ou recorte."""
    imgs = [f for f in row.frags if f.kind == "image"]
    texts = row.texts
    spans = [s for f in texts for s in f.spans if s.text.strip()]
    math = [s for s in spans if s.is_math]
    plain = [s for s in spans if not s.is_math]
    draws = [f for f in row.frags if f.kind == "draw"]
    if imgs:
        if texts:
            row.crop, row.reason = True, "figura com texto"
        return
    x0, y0, x1, y1 = row.bbox
    if row.crop:
        # traço de fração dentro de uma linha de texto: só a fórmula vira recorte inline
        if math and plain and _starts_line(list(texts)) and y1 - y0 <= 30:
            mx0 = min(s.bbox[0] for s in math) - 3
            mx1 = max(s.bbox[2] for s in math) + 3
            if all(mx0 <= d.x0 and d.x1 <= mx1 for d in draws):
                row.crop, row.inline, row.reason = False, True, "fórmula com traço"
        return
    if any(_bad_chars(s.text) for s in plain):
        row.crop, row.reason = True, "glifo sem texto"
        return
    if not math:
        return
    if not plain:
        row.crop, row.reason = True, "fórmula em bloco"
        return
    if y1 - y0 > 30:
        row.crop, row.reason = True, "fórmula alta"
        return
    sizes = [s.size for s in math]
    bases = [s.origin_y for s in math]
    simple = (
        max(sizes) <= min(sizes) * 1.1
        and max(bases) - min(bases) <= 1.6
        and not any(_bad_chars(s.text) for s in math)
    )
    if not simple:
        row.inline, row.reason = True, "fórmula embutida"


def split_crop_row(row: Row) -> list[Row]:
    """Tira do recorte as linhas de texto comum que só encostam na fórmula/tabela (ex.: a frase antes
    de uma chave alta ou logo abaixo de uma fração). Elas voltam a ser texto, antes ou depois."""
    if not row.crop:
        return [row]
    heavy = [f for f in row.frags if f.kind in ("image", "draw") or (f.kind == "text" and f.has_math)]
    if not heavy:
        return [row]
    plain = []
    for f in row.frags:
        if f.kind != "text" or f.has_math or (f.x1 - f.x0) < 120:
            continue
        if max(_overlap(f, h) for h in heavy) < 0.5:
            plain.append(f)
    if not plain:
        return [row]
    core = [f for f in row.frags if f not in plain]
    cy0 = min(f.y0 for f in heavy)
    cy1 = max(f.y1 for f in heavy)
    above = [f for f in plain if (f.y0 + f.y1) / 2 < (cy0 + cy1) / 2]
    below = [f for f in plain if f not in above]
    out: list[Row] = []
    for grp in _group_lines(above):
        out.append(Row(row.page, grp))
    out.append(Row(row.page, core, True, row.reason))
    for grp in _group_lines(below):
        out.append(Row(row.page, grp))
    return out


def _group_lines(fs: list[Frag]) -> list[list[Frag]]:
    groups: list[list[Frag]] = []
    for f in sorted(fs, key=lambda f: f.y0):
        if groups and _overlap(f, _band(groups[-1])) >= 0.4:
            groups[-1].append(f)
        else:
            groups.append([f])
    return [sorted(g, key=lambda f: f.x0) for g in groups]


# ───────────────────────── marcação ─────────────────────────


def _escape(t: str) -> str:
    return t.replace("\\", "\\\\").replace("*", "\\*").replace("`", "\\`")


# linha que começa item de lista dentro do enunciado: sempre em linha nova
ITEM_START_RE = re.compile(
    r"^(?:\*\*)?(?:[•▪◦·\-–]|\(\s*[VF]?\s*\)|(?:I|II|III|IV|V|VI|VII|VIII|IX|X)(?:\*\*)?\s*[.\-–)]|\d{1,2}(?:\*\*)?[.)]|[a-e]\))(?:\*\*)?\s"
)
URL_TEXT_RE = re.compile(r"(https?://|www\.|<http)")


def _char_style(s: Span, k: int, big: float, base: float) -> tuple[str, ...]:
    st: list[str] = []
    ch = s.chars[k][0] if s.chars else s.text
    if ch.strip() and s.size < big * 0.85 and abs(s.origin_y - base) > 0.8:
        st.append("sup" if s.origin_y < base else "sub")
    elif s.is_bold and not s.is_math:
        st.append("b")
    if s.is_mono:
        st.append("code")
    if s.color not in (0,) and not s.is_math and not URL_TEXT_RE.search(s.text):
        st.append("mark")
    if k in s.ul:
        st.append("u")
    return tuple(st)


def _math_clusters(row: Row) -> list[tuple[list[Span], list[Frag]]]:
    """Fórmulas MathJax contíguas (spans Type3 + traços) de uma linha com texto."""
    items: list[tuple[float, object]] = [(s.bbox[0], s) for f in row.texts for s in f.spans]
    items += [(d.x0, d) for d in row.frags if d.kind == "draw"]
    items.sort(key=lambda t: t[0])
    clusters: list[tuple[list[Span], list[Frag]]] = []
    cur: tuple[list[Span], list[Frag]] | None = None
    last_x1 = -1e9
    for _, it in items:
        if isinstance(it, Span) and not it.text.strip() and not it.is_math:
            continue
        is_m = isinstance(it, Frag) or it.is_math
        if is_m:
            x0 = it.x0 if isinstance(it, Frag) else it.bbox[0]
            x1 = it.x1 if isinstance(it, Frag) else it.bbox[2]
            if cur is None or x0 - last_x1 > 4:
                cur = ([], [])
                clusters.append(cur)
                last_x1 = x1
            (cur[1] if isinstance(it, Frag) else cur[0]).append(it)
            last_x1 = max(last_x1, x1)
        else:
            cur = None
            last_x1 = it.bbox[2]
    return [c for c in clusters if any(sp.text.strip() for sp in c[0])]


def row_markup(row: Row, inline_cb=None) -> str:
    """Texto da linha com **negrito**, <u>, <mark>, <sup>, <sub>, `código`; espaços pela geometria.
    Em linhas `inline`, cada fórmula vira o texto devolvido por `inline_cb(spans, traços)`."""
    spans = [s for f in row.texts for s in f.spans]
    spans.sort(key=lambda s: s.bbox[0])
    cluster_of: dict[int, int] = {}
    tokens: dict[int, str] = {}
    if row.inline and inline_cb is not None:
        for ci, (cs, cd) in enumerate(_math_clusters(row)):
            for sp in cs:
                cluster_of[id(sp)] = ci
            tokens[ci] = inline_cb(cs, cd)
        spans = [sp for sp in spans if not (sp.is_math and id(sp) not in cluster_of)]
    if not spans:
        return ""
    vis = [s for s in spans if s.text.strip()]
    if row.inline:
        vis = [s for s in vis if not s.is_math] or vis  # sobrescritos medidos contra o texto, não contra a fórmula
    big = max(s.size for s in vis) if vis else spans[0].size
    main = [s for s in vis if s.size >= big * 0.85] or vis
    base = sorted(s.origin_y for s in main)[len(main) // 2] if main else 0
    runs: list[list] = []  # [estilos, texto]
    prev_x1 = None
    emitted: set[int] = set()
    for s in spans:
        if id(s) in cluster_of:
            ci = cluster_of[id(s)]
            if ci in emitted:
                prev_x1 = max(prev_x1 or 0, s.bbox[2])
                continue
            emitted.add(ci)
            last = runs[-1][1] if runs else ""
            if runs and not last.endswith(" "):
                runs.append([(), " "])
            runs.append([("raw",), tokens[ci]])
            runs.append([(), " "])
            prev_x1 = s.bbox[2]
            continue
        chars = s.chars or [(s.text, s.bbox[0], s.bbox[2])]
        blanks = _blank_chars(s, chars)
        for k, (ch, cx0, cx1) in enumerate(chars):
            if s.is_math:
                ch = ch.replace("\xa0", " ")
            if k in blanks:
                ch = "_"  # lacuna "______" (espaços sublinhados) das questões de preencher
            st = _char_style(s, k, big, base) if k not in blanks else ()
            if k == 0 and prev_x1 is not None and cx0 - prev_x1 > 1.2 and "sup" not in st and "sub" not in st:
                last = runs[-1][1] if runs else ""
                if not last.endswith((" ", "\xa0")) and not ch.startswith((" ", "\xa0")):
                    runs.append([(), " "])
            if not ch.strip() and runs:
                # espaço herda o estilo anterior só se o próximo caractere mantiver o estilo
                st = tuple(x for x in st if x in runs[-1][0])
            if runs and runs[-1][0] == st:
                runs[-1][1] += ch
            else:
                runs.append([st, ch])
        prev_x1 = s.bbox[2]
    out = []
    for st, t in runs:
        if st == ("raw",):
            out.append(t)
            continue
        e = t if "code" in st else _escape(t)
        if not st or not t.strip():
            out.append(e)
            continue
        lead = e[: len(e) - len(e.lstrip())]
        trail = e[len(e.rstrip()):]
        core = e.strip()
        for part in ("code", "sup", "sub", "u", "mark", "b"):
            if part not in st:
                continue
            if part == "b":
                core = f"**{core}**"
            elif part == "code":
                core = f"`{core}`"
            else:
                core = f"<{part}>{core}</{part}>"
        out.append(lead + core + trail)
    text = "".join(out).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    for tag in ("u", "mark", "sup", "sub"):
        text = text.replace(f"</{tag}> <{tag}>", " ").replace(f"</{tag}><{tag}>", "")
    text = text.replace("** **", " ").replace("****", "")
    text = re.sub(r"(!\[[^\]]*\]\([^)]*\)) ([.,;:!?)])", r"\1\2", text)
    # lacunas vizinhas (sublinhado partido) viram uma só, sempre separada das palavras
    text = re.sub(r" ?_{3,}(?: ?_{3,})* ?", " ______ ", text).replace("  ", " ")
    return text.strip()


def _blank_chars(s: Span, chars: list) -> set[int]:
    """Índices de espaços sublinhados em sequência (≥ 3): no PDF, a lacuna de preencher é uma série de
    espaços com sublinhado. Um espaço sublinhado isolado (entre palavras destacadas) não é lacuna."""
    out: set[int] = set()
    run: list[int] = []
    for k, (ch, _, _) in enumerate(chars + [("x", 0, 0)]):
        if k < len(chars) and k in s.ul and not ch.strip():
            run.append(k)
            continue
        if len(run) >= 3:
            out.update(run)
        run = []
    return out


def _join_lines(lines: list[str]) -> str:
    out = ""
    for ln in lines:
        if not out:
            out = ln
        elif re.search(r"[A-Za-zÀ-ú]-$", out) and re.match(r"[a-zà-ú]", ln):
            out += ln  # "tornou-" + "se" e quebras silábicas
        else:
            out += " " + ln
    # lacuna que continua na linha seguinte é uma só
    return re.sub(r"______(?: ______)+", "______", out)


# ───────────────────────── figuras ─────────────────────────


def _png_asset(pix: pymupdf.Pixmap, kind: str) -> Asset:
    if pix.n - pix.alpha >= 4:  # CMYK
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    if max(pix.width, pix.height) > MAX_IMG_SIDE:
        f = max(pix.width, pix.height) / MAX_IMG_SIDE
        shrink = 1
        while f > 2 ** shrink:
            shrink += 1
        pix.shrink(shrink)
    data = pix.tobytes("png")
    sha = hashlib.sha256(data).hexdigest()
    return Asset(sha=sha, data=data, width=pix.width, height=pix.height, kind=kind)


def _frag_rects(f: Frag) -> list[tuple[float, float, float, float]]:
    if f.kind == "text":
        return [s.bbox for s in f.spans if s.text.strip()]
    return [f.bbox]


def _ink_rects(f: Frag) -> list[tuple[float, float, float, float]]:
    """Caixa provável da tinta: da altura das maiúsculas acima da baseline até as descendentes."""
    if f.kind != "text":
        return [f.bbox]
    return [
        (s.bbox[0], max(s.bbox[1], s.origin_y - 0.72 * s.size), s.bbox[2], min(s.bbox[3], s.origin_y + 0.24 * s.size))
        for s in f.spans
        if s.text.strip()
    ]


def render_crop(
    page: pymupdf.Page,
    bbox: tuple[float, float, float, float],
    own: list[Frag] | None = None,
    others: list[Frag] | None = None,
    pad_x: float = CROP_PAD,
    tighten: bool = True,
) -> Asset:
    """Renderiza a região em PNG. Tinta de linhas vizinhas que invade o recorte (frações empilhadas,
    linhas muito próximas) é apagada: pinta-se de branco a caixa do vizinho, encolhida para não
    cobrir as caixas da própria linha."""
    x0, y0, x1, y1 = bbox
    if tighten and own and all(f.kind == "text" for f in own):
        ink = [r for f in own for r in _ink_rects(f)]
        if ink:
            y0 = max(y0, min(r[1] for r in ink))
            y1 = min(y1, max(r[3] for r in ink))
    clip = pymupdf.Rect(x0 - pad_x, y0 - CROP_PAD / 2, x1 + pad_x, y1 + CROP_PAD / 2) & page.rect
    pix = page.get_pixmap(clip=clip, dpi=CROP_DPI, alpha=False)
    if others:
        own_rects = [r for f in (own or []) for r in _ink_rects(f)]
        scale = CROP_DPI / 72
        for f in others:
            for r in _frag_rects(f):
                rx0, ry0, rx1, ry1 = r
                if rx1 <= clip.x0 or rx0 >= clip.x1 or ry1 <= clip.y0 or ry0 >= clip.y1:
                    continue
                for o in own_rects:
                    if o[0] < rx1 and rx0 < o[2] and o[1] < ry1 and ry0 < o[3]:
                        if (ry0 + ry1) / 2 > (o[1] + o[3]) / 2:
                            ry0 = max(ry0, o[3])
                        else:
                            ry1 = min(ry1, o[1])
                if ry1 - ry0 <= 0.2:
                    continue
                # coordenadas do pixmap são absolutas (pix.irect começa em clip × escala)
                ir = pymupdf.IRect(int(rx0 * scale), int(ry0 * scale), int(rx1 * scale) + 1, int(ry1 * scale) + 1) & pix.irect
                if not ir.is_empty:
                    pix.set_rect(ir, (255, 255, 255))
    return _png_asset(pix, "recorte")


def extract_image(doc: pymupdf.Document, page: pymupdf.Page, f: Frag) -> Asset:
    if f.xref:
        try:
            pix = pymupdf.Pixmap(doc, f.xref)
            if pix.alpha or pix.n not in (1, 3):
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix) if pix.n - pix.alpha >= 3 or pix.n == 1 else pix
            # imagem com máscara/transparência ou muito reduzida na página: renderiza o recorte
            shown_w = f.x1 - f.x0
            if pix.width >= shown_w * 0.9 and not _has_smask(doc, f.xref):
                return _png_asset(pix, "figura")
        except Exception:  # noqa: BLE001 - qualquer falha cai no recorte renderizado
            pass
    a = render_crop(page, f.bbox)
    a.kind = "figura"
    return a


def _has_smask(doc: pymupdf.Document, xref: int) -> bool:
    try:
        return bool(doc.xref_get_key(xref, "SMask")[1] not in ("null", ""))
    except Exception:  # noqa: BLE001
        return False


def asset_md(a: Asset, alt: str) -> str:
    return f"![{alt}](/q-img/{a.sha})"


# ───────────────────────── montagem da questão ─────────────────────────


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


def parse_header(q: RawQuestion) -> tuple[str, str, list[str]]:
    lines = [_clean(f.text) for f in sorted(q.head_frags, key=lambda f: (f.page, f.y0))]
    banca_parts: list[str] = []
    rest: list[str] = []
    probs: list[str] = []
    done = False
    for ln in lines:
        if not done:
            banca_parts.append(ln)
            if YEAR_TAIL_RE.search(ln):
                done = True
        else:
            rest.append(ln)
    if not done:
        probs.append("cabeçalho sem ano (linha banca/órgão/ano)")
    return " ".join(banca_parts), " ".join(rest), probs


def normalize_banca(raw: str) -> str:
    r = raw.strip()
    if r.lower() in ("instituto aocp", "aocp"):
        return "AOCP"
    return r


def parse_banca_line(line: str) -> dict:
    banca, _, rest = line.partition(" - ")
    parts = [p.strip() for p in rest.split("/")]
    ano = None
    if parts and re.fullmatch(r"\d{4}", parts[-1]):
        ano = int(parts.pop())
    cargo = parts[0] if parts else ""
    orgao = parts[1] if len(parts) > 1 else ""
    area = "/".join(parts[2:])
    return {"bancaRaw": banca.strip(), "cargo": cargo, "orgao": orgao, "area": area, "ano": ano}


def is_source_row(row: Row) -> bool:
    """Linha de fonte do texto-base: Tahoma pequena (≤ 6.7 pt), em geral alinhada à direita."""
    ts = [s for f in row.texts for s in f.spans if s.text.strip()]
    if not ts or row.crop:
        return False
    return all(s.size <= 6.7 for s in ts)


def assemble(doc: pymupdf.Document, raw: RawQuestion, gabarito: dict[int, str], assets: dict[str, Asset]) -> Question:
    probs: list[str] = []
    warns: list[str] = []
    banca_line, materia_line, hp = parse_header(raw)
    probs += hp
    meta = parse_banca_line(banca_line)
    materia, _, assunto = materia_line.partition(" - ")
    if not materia_line:
        probs.append("cabeçalho sem 'Matéria - Assunto'")
    if raw.numero is None:
        probs.append("número da questão (NNNN)) não encontrado")

    # linhas visuais por página, em ordem
    rows: list[Row] = []
    by_page: dict[int, list[Frag]] = {}
    for f in raw.frags:
        by_page.setdefault(f.page, []).append(f)
    for pno in sorted(by_page):
        prs = build_rows(by_page[pno])
        for r in prs:
            classify_row(r)
        prs = [x for r in prs for x in split_crop_row(r)]
        rows.extend(r for r in prs if r.texts or any(f.kind == "image" for f in r.frags))

    # zona das alternativas: última sequência a), b), c), d)[, e)] em x≈46 ou "Certo"/"Errado"
    def row_first_text(r: Row) -> tuple[float, str]:
        ts = r.texts
        if not ts:
            return (999.0, "")
        f = min(ts, key=lambda x: x.x0)
        return (f.x0, _clean(f.text))

    kind = "MULTIPLA_ESCOLHA"
    opt_start = None
    starts: list[tuple[int, str]] = []
    for i, r in enumerate(rows):
        x, t = row_first_text(r)
        if X_OPT[0] <= x <= X_OPT[1]:
            m = OPT_RE.match(t)
            if m:
                starts.append((i, m.group(1)))
    # procura a última sequência válida que começa em "a"
    for k in range(len(starts) - 1, -1, -1):
        if starts[k][1] != "a":
            continue
        seq = starts[k:]
        letters = "".join(s[1] for s in seq)
        if letters in ("abcde", "abcd"):
            opt_start = starts[k][0]
            break
    ce_rows = None
    if opt_start is None and len(rows) >= 2:
        x1_, t1 = row_first_text(rows[-2])
        x2_, t2 = row_first_text(rows[-1])
        if t1 == "Certo" and t2 == "Errado":
            kind = "CERTO_ERRADO"
            ce_rows = len(rows) - 2
    body_end = opt_start if opt_start is not None else (ce_rows if ce_rows is not None else len(rows))
    if opt_start is None and ce_rows is None:
        probs.append("alternativas não encontradas (nem a)…e) nem Certo/Errado)")

    q_assets: list[str] = []

    def render_rows(rs: list[Row], alt: str) -> list[tuple[str, bool]]:
        """Converte linhas em (texto, quebra_de_parágrafo_antes). Recortes consecutivos viram uma imagem."""
        out: list[tuple[str, bool]] = []
        i = 0
        prev_y1 = None
        prev_page = None
        while i < len(rs):
            r = rs[i]
            x0, y0, x1, y1 = r.bbox
            gap_break = prev_y1 is not None and prev_page == r.page and (y0 - prev_y1) > PARA_GAP
            # na virada de página não há espaço a medir: frase encerrada + maiúscula abre parágrafo
            page_break = prev_page is not None and prev_page != r.page and bool(out) and out[-1][0].rstrip().endswith((".", ":", "?", "!"))
            imgs = [f for f in r.frags if f.kind == "image"]
            if r.crop or imgs:
                if imgs and not r.crop:
                    for f in imgs:
                        a = extract_image(doc, doc[f.page], f)
                        assets[a.sha] = a
                        q_assets.append(a.sha)
                        out.append((asset_md(a, "Figura"), True))
                    prev_y1, prev_page = y1, r.page
                    i += 1
                    continue
                # junta recortes consecutivos na mesma página
                bx0, by0, bx1, by1 = r.bbox
                if r.clip_x0 is not None:
                    bx0 = r.clip_x0
                j = i + 1
                while j < len(rs) and rs[j].page == r.page and (rs[j].crop) and rs[j].bbox[1] - by1 < 8:
                    b = rs[j].bbox
                    bx0, by0, bx1, by1 = min(bx0, b[0]), min(by0, b[1]), max(bx1, b[2]), max(by1, b[3])
                    j += 1
                own = [f for k in range(i, j) for f in rs[k].frags]
                own_ids = {id(f) for f in own}
                others = [f for f in by_page.get(r.page, []) if id(f) not in own_ids and f.kind == "text"]
                a = render_crop(doc[r.page], (bx0, by0, bx1, by1), own, others)
                assets[a.sha] = a
                q_assets.append(a.sha)
                out.append((asset_md(a, alt), True))
                prev_y1, prev_page = by1, r.page
                i = j
                continue
            def inline_cb(cs: list[Span], cd: list[Frag], r: Row = r) -> str:
                fr = Frag(
                    "text",
                    r.page,
                    (
                        min(x.bbox[0] for x in cs),
                        min(x.bbox[1] for x in cs),
                        max(x.bbox[2] for x in cs),
                        max(x.bbox[3] for x in cs),
                    ),
                    cs,
                )
                bx0 = min([fr.x0] + [d.x0 for d in cd])
                bx1 = max([fr.x1] + [d.x1 for d in cd])
                ink = _ink_rects(fr) + [d.bbox for d in cd]
                by0 = min(i[1] for i in ink)
                by1 = max(i[3] for i in ink)
                row_ids = {id(f) for f in r.frags}
                others = [f for f in by_page.get(r.page, []) if f.kind == "text" and id(f) not in row_ids]
                a = render_crop(doc[r.page], (bx0, by0, bx1, by1), [fr, *cd], others, pad_x=1.6, tighten=False)
                assets[a.sha] = a
                q_assets.append(a.sha)
                em = max(0.9, round((by1 - by0 + 1.0) / BODY_SIZE, 2))
                return f"![fórmula:{em}](/q-img/{a.sha})"

            t = row_markup(r, inline_cb)
            if t:
                starts_upper = bool(re.match(r"^(?:\*\*|<u>|<mark>|[“\"(])*[A-ZÀ-Ý]", t))
                out.append((t, gap_break or (page_break and starts_upper) or bool(ITEM_START_RE.match(t))))
            prev_y1, prev_page = y1, r.page
            i += 1
        return out

    def paragraphs(items: list[tuple[str, bool]]) -> str:
        paras: list[list[str]] = []
        for t, brk in items:
            is_img = t.startswith("![")
            if not paras or brk or is_img or (paras[-1] and paras[-1][-1].startswith("![")):
                paras.append([t])
            else:
                paras[-1].append(t)
        return "\n\n".join(_join_lines(p) for p in paras).strip()

    body = rows[:body_end]
    # texto-base: tudo até a última linha de fonte (Tahoma ≤ 6.7) que ainda tem enunciado depois
    support = ""
    src_idx = None
    for i in range(len(body) - 1, -1, -1):
        if is_source_row(body[i]):
            if any(not is_source_row(r) for r in body[i + 1:]):
                src_idx = i
            break
    if src_idx is not None:
        support = paragraphs(render_rows(body[: src_idx + 1], "Figura"))
        statement = paragraphs(render_rows(body[src_idx + 1:], "Fórmula"))
    else:
        statement = paragraphs(render_rows(body, "Fórmula"))
    if not statement and not support:
        probs.append("enunciado vazio")

    options: list[dict] = []
    if kind == "CERTO_ERRADO":
        options = [{"label": "C", "text": "Certo"}, {"label": "E", "text": "Errado"}]
    elif opt_start is not None:
        cur_label = None
        cur_rows: list[Row] = []
        groups: list[tuple[str, list[Row]]] = []
        for r in rows[opt_start:]:
            x, t = row_first_text(r)
            m = OPT_RE.match(t) if X_OPT[0] <= x <= X_OPT[1] else None
            if m and (cur_label is None or ord(m.group(1)) == ord(cur_label) + 1):
                if cur_label is not None:
                    groups.append((cur_label, cur_rows))
                cur_label, cur_rows = m.group(1), [r]
            else:
                if x < X_OPT[0] - 2 and r.texts:
                    warns.append(f"linha fora do recuo dentro da alternativa {cur_label}")
                cur_rows.append(r)
        if cur_label is not None:
            groups.append((cur_label, cur_rows))
        for label, rs in groups:
            first = rs[0]
            if first.crop:
                # recorta só o que vem depois do rótulo "a)"
                lab = min(first.texts, key=lambda f: f.x0)
                lab_span = lab.spans[0]
                m = OPT_RE.match(lab_span.text.strip())
                if m and lab_span.text.strip() == m.group(0).strip():
                    first = Row(first.page, [f for f in first.frags if f is not lab], True, first.reason)
                    if len(lab.spans) > 1:
                        first.frags.append(Frag("text", lab.page, lab.bbox, lab.spans[1:]))
                else:
                    # rótulo e início da fórmula no mesmo span: corta a largura de "a)" (≈ 7 pt em Tahoma 7,2)
                    first = Row(first.page, list(first.frags), True, first.reason, clip_x0=lab.x0 + OPT_LABEL_W)
                rs = [first] + rs[1:]
                text = paragraphs(render_rows(rs, "Fórmula"))
            else:
                items = render_rows(rs, "Fórmula")
                text = paragraphs(items)
                # tira o rótulo "a)", inclusive quando ele está dentro do negrito/sublinhado da alternativa
                text = re.sub(r"^((?:\*\*|<(?:u|mark)>)*)\s*[a-e]\)\s*", r"\1", text, count=1)
                text = text.replace("****", "").strip()
            options.append({"label": label.upper(), "text": text.strip()})
        if any(not o["text"] for o in options):
            probs.append("alternativa vazia")

    # gabarito
    gab = gabarito.get(raw.numero) if raw.numero is not None else None
    anulada = gab == "Anulada"
    answer = None
    if gab is None:
        probs.append("sem entrada no gabarito")
    elif gab not in GAB_VALUES:
        probs.append(f"gabarito desconhecido: {gab}")
    elif not anulada:
        if kind == "CERTO_ERRADO":
            if gab not in ("Certo", "Errado"):
                probs.append(f"gabarito {gab} em questão Certo/Errado")
            else:
                answer = "C" if gab == "Certo" else "E"
        else:
            if gab not in "ABCDE":
                probs.append(f"gabarito {gab} em questão de múltipla escolha")
            elif gab not in {o["label"] for o in options}:
                probs.append(f"gabarito {gab} sem alternativa correspondente")
            else:
                answer = gab
    return Question(
        tecId=raw.tec_id,
        numero=raw.numero,
        bancaRaw=meta["bancaRaw"],
        banca=normalize_banca(meta["bancaRaw"]),
        cargo=meta["cargo"],
        orgao=meta["orgao"],
        area=meta["area"],
        ano=meta["ano"],
        materia=_clean(materia),
        assunto=_clean(assunto),
        support=support,
        statement=statement,
        options=options,
        kind=kind,
        answer=answer,
        anulada=anulada,
        gabaritoRaw=gab,
        page=raw.page,
        assets=q_assets,
        problems=probs,
        warnings=warns,
    )


def read_caderno(path: str | Path) -> Caderno:
    path = Path(path)
    doc = pymupdf.open(path)
    raws, gabarito, anomalies, title = split_questions(doc)
    assets: dict[str, Asset] = {}
    qs = [assemble(doc, r, gabarito, assets) for r in raws]
    nums = [q.numero for q in qs if q.numero is not None]
    if len(nums) != len(set(nums)):
        anomalies.append("números de questão repetidos no caderno")
    missing = set(gabarito) - set(nums)
    if missing:
        anomalies.append(f"{len(missing)} entradas do gabarito sem questão: {sorted(missing)[:10]}")
    return Caderno(path=path, title=title, questions=qs, gabarito=gabarito, assets=assets, anomalies=anomalies, pages=doc.page_count)


def content_hash(q: Question) -> str:
    h = hashlib.sha256()
    for part in (q.support, q.statement, *(o["label"] + o["text"] for o in q.options), q.answer or ""):
        h.update(unicodedata.normalize("NFC", part).encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()
