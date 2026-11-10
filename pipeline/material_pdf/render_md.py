"""Markdown do material próprio -> HTML do modelo Prontidão (quadros, tabelas, figuras, seções numeradas).

Os blocos ``` e os quadros '> [!tipo]' saem do texto como marcadores antes do markdown e voltam já renderizados;
a leitura usa o mesmo parser do validador (fences, CALLOUT_HEAD).
"""
from __future__ import annotations

import html
import os
import re
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from validate_material import CALLOUT_HEAD, FENCE, FIGURE_LANGS

from . import figures
from .load import DESIGN_DIR, QIMG_DIR, ContentError

MD = MarkdownIt("commonmark", {"html": False}).enable("table")
MDQ = MarkdownIt("commonmark", {"html": True}).enable("table")

# tipo -> (rótulo impresso, leva mascote)
CALLOUTS = {
    "atencao": ("Fique atento!", True),
    "pegadinha": ("Pegadinha da banca", True),
    "bizu": ("Bizu!", True),
    "exemplo": ("Exemplificando", True),
    "jurisprudencia": ("Jurisprudência", True),
    "resolvido": ("Passo a passo", True),
    "lei": ("Letra da lei", False),
    "esquema": ("Esquema", False),
    "objetivos": ("Ao final do capítulo, você vai saber", False),
}
TITLE_INLINE = {"lei", "jurisprudencia"}  # título vai no rótulo ("LETRA DA LEI · CF, art. 5º")
MASCOT_DIR = DESIGN_DIR / "mascote"
MASCOT_COLOR = {"atencao": "#d4301f", "pegadinha": "#d9640f", "bizu": "#e9a90c", "exemplo": "#2563eb", "jurisprudencia": "#0e1b2e",
                "resolvido": "#059669", "missao": "#d4301f", "cai-na-prova": "#d4301f", "praticar": "#d9640f", "gabarito": "#059669",
                "revisao": "#7c3aed", "missao-cumprida": "#e9a90c"}
FLAME = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#e9a90c" d="M12 2.2c.4 3-1.4 4.7-2.9 6.6C7.6 10.6 6 12.4 6 15.4 6 '
         '19.3 8.6 22 12 22s6-2.7 6-6.6c0-2.2-.9-3.7-2-5-.1 1.5-.8 2.6-1.8 3.1.6-3.5-.2-7.5-2.2-11.3Z"/><path fill="#f6c244" d="M12 '
         '21.4c-2.4 0-4.1-1.8-4.1-4.2 0-1.7.9-2.8 1.9-3.8.7-.7 1.3-1.4 1.5-2.4 1.8 1.5 3.7 3.2 3.7 6.2 0 2.5-1.2 4.2-3 4.2Z"/><path '
         'fill="#fff4d1" d="M12 21.4c-1.3 0-2.1-1-2.1-2.3 0-1.3.7-1.9 1.4-2.6.4-.4.6-.7.7-1.2 1 .9 2.1 1.7 2.1 3.2 0 1.6-.9 2.9-2.1 '
         '2.9Z"/></svg>')
ALLOWED_Q_TAGS = {"p", "u", "b", "strong", "i", "em", "br", "sup", "sub", "ol", "ul", "li", "table", "thead", "tbody", "tr", "td", "th",
                  "img", "blockquote"}


def mascot(slug: str, dark: bool = False) -> str:
    """Imagem do mascote (pipeline/material_mascote.py); sem ela, o marcador provisório (chama num círculo).

    Páginas claras: a FOCO (corpo escuro; decisão do dono, 02/11/2026), ou a de MASCOTE (build_material.py --mascote).
    Fundo escuro (faixa de abertura): sempre a CHAMA, que é a que aparece sobre o azul-marinho."""
    variant = "chama" if dark else os.environ.get("MASCOTE", "foco")
    names = [f"{variant}/{slug}.png"] + ([f"{slug}-escuro.png"] if dark else []) + [f"{slug}.png", f"{slug}.svg"]
    for name in names:
        p = MASCOT_DIR / name
        if p.exists():
            cls = "masc-img" + (" outline" if dark and "escuro" not in name else "")
            return f'<img class="{cls}" src="{p.as_uri()}" alt="">'
    return f'<span class="masc-ph" style="--mc:{MASCOT_COLOR.get(slug, "#d4301f")}">{FLAME}</span>'


def inline(text: str) -> str:
    """Markdown de uma linha (negrito/itálico), sem <p>."""
    return MD.renderInline(text)


def md(text: str) -> str:
    out = MD.render(text)
    out = re.sub(r"<pre><code>(.*?)</code></pre>", lambda m: f'<div class="formula">{m.group(1).rstrip()}</div>', out, flags=re.S)
    return out.replace("<table>", '<table class="tb">')


def question_html(text: str) -> str:
    """Enunciado/alternativa do banco: **negrito**, <u>sublinhado</u> e ![Figura](/q-img/<sha256>)."""
    out = MDQ.render((text or "").replace("⌃", "∧").replace("⌵", "∨"))  # símbolos que as fontes do modelo não têm
    out = re.sub(r"</?([a-zA-Z0-9]+)[^>]*>", lambda m: m.group(0) if m.group(1).lower() in ALLOWED_Q_TAGS else "", out)

    def img(m: re.Match) -> str:
        sha = m.group(1)
        found = sorted(QIMG_DIR.glob(f"{sha}.*")) if QIMG_DIR.exists() else []
        if not found:
            raise ContentError(f"figura de questão {sha} não exportada; rode (em web/) npx tsx scripts/material-qimg.ts")
        return f'<img class="qimg" src="{found[0].as_uri()}" alt="Figura">'

    out = re.sub(r'<img[^>]*src="/q-img/([0-9a-f]{64})"[^>]*>', img, out)
    if re.search(r"<img(?![^>]*class=\"qimg\")", out):
        raise ContentError("imagem fora de /q-img/ no enunciado")
    return out.replace("<table>", '<table class="tb">')


@dataclass
class RenderedChapter:
    lead_html: str
    objectives: list[str]
    sections: list[tuple[str, str, str]]  # (número N.k, título, âncora)
    body_html: str
    fixar: list[str]  # itens do "Para fixar" (HTML inline)
    figures: int = 0
    errors: list[str] = field(default_factory=list)


class _Ctx:
    def __init__(self, chap_no: int, anchor: str):
        self.chap_no = chap_no
        self.anchor = anchor
        self.fig = 0
        self.blocks: dict[str, str] = {}
        self.last_type_in_section: str | None = None

    def put(self, html_: str) -> str:
        key = f"XQBLOCK{len(self.blocks)}X"
        self.blocks[key] = html_
        return f"\n\n{key}\n\n"


def _figure(ctx: _Ctx, lang: str, caption: str, content: str, line: int, path) -> str:
    ctx.fig += 1
    fid = f"{ctx.anchor}-f{ctx.fig}"
    try:
        inner = figures.render(lang, content, fid)
    except ContentError as e:
        raise ContentError(f"{path.name}, linha {line}: {e}") from e
    cap = f'<figcaption><b>Figura {ctx.chap_no}.{ctx.fig}</b> — {inline(caption)}</figcaption>' if caption else ""
    return f'<figure class="fig fig-{lang}">{inner}{cap}</figure>'


def _callout(ctx: _Ctx, ctype: str, title: str, lines: list[str]) -> str:
    if ctype not in CALLOUTS:
        raise ContentError(f"quadro [!{ctype}] desconhecido")
    label, has_m = CALLOUTS[ctype]
    body = "\n".join(lines)
    inner = md(body)
    if ctype in TITLE_INLINE and title:
        head = f'<div class="co-k">{html.escape(label)} · <span class="co-ref">{inline(title)}</span></div>'
    else:
        head = f'<div class="co-k">{html.escape(label)}</div>' + (f'<div class="co-t">{inline(title)}</div>' if title else "")
    show_m = has_m and ctx.last_type_in_section != ctype
    ctx.last_type_in_section = ctype
    m = f'<div class="masc">{mascot(ctype)}</div>' if show_m else ""
    return f'<div class="co {ctype}{" has-m" if show_m else ""}">{m}{head}<div class="co-b">{inner}</div></div>'


def _blocks(ctx: _Ctx, text: str, path) -> str:
    """Troca fences e quadros por marcadores; devolve o markdown restante."""
    def fence(m: re.Match) -> str:
        lang, cap, content = m.group(1), m.group(2).strip(), m.group(3)
        line = text[: m.start()].count("\n") + 1
        if lang in FIGURE_LANGS:
            return ctx.put(_figure(ctx, lang, cap, content, line, path))
        return ctx.put(f'<pre class="code">{html.escape(content)}</pre>')

    text = FENCE.sub(fence, text)
    out: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"^##\s", ln):
            ctx.last_type_in_section = None
        mh = CALLOUT_HEAD.match(ln)
        if mh:
            j = i + 1
            content = []
            while j < len(lines) and lines[j].startswith(">"):
                content.append(re.sub(r"^>\s?", "", lines[j]))
                j += 1
            out.append(ctx.put(_callout(ctx, mh.group(1), mh.group(2).strip(), content)))
            i = j
            continue
        out.append(ln)
        i += 1
    return "\n".join(out)


def _fill(ctx: _Ctx, html_: str) -> str:
    html_ = re.sub(r"<p>(XQBLOCK\d+X)</p>", lambda m: ctx.blocks[m.group(1)], html_)
    left = re.findall(r"XQBLOCK\d+X", html_)
    if left:
        html_ = re.sub(r"XQBLOCK\d+X", lambda m: ctx.blocks[m.group(0)], html_)
    return html_


def render_chapter(body: str, chap_no: int, anchor: str, path) -> RenderedChapter:
    ctx = _Ctx(chap_no, anchor)
    # objetivos: o primeiro quadro [!objetivos] vai para a abertura
    objectives: list[str] = []
    m = re.search(r"^>\s*\[!objetivos\][^\n]*\n((?:>[^\n]*\n?)*)", body, re.M)
    if m:
        for ln in m.group(1).splitlines():
            t = re.sub(r"^>\s?", "", ln).strip()
            t = re.sub(r"^(?:[-*]|\d+[.)])\s+", "", t)
            if t:
                objectives.append(inline(t))
        body = body[: m.start()] + body[m.end():]
    first_h2 = re.search(r"^##\s", body, re.M)
    lead_src, rest = (body[: first_h2.start()], body[first_h2.start():]) if first_h2 else (body, "")

    lead_html = _fill(ctx, md(_blocks(ctx, lead_src, path)))
    sections: list[tuple[str, str, str]] = []
    parts: list[str] = []
    fixar: list[str] = []
    chunks = re.split(r"^##\s+(.+?)\s*$", rest, flags=re.M)
    # chunks = ['', título1, texto1, título2, texto2, ...]
    for k in range(1, len(chunks), 2):
        title, text = chunks[k], chunks[k + 1]
        num = f"{chap_no}.{len(sections) + 1}"
        sid = f"{anchor}-s{len(sections) + 1}"
        sections.append((num, title, sid))
        ctx.last_type_in_section = None
        inner = _fill(ctx, md(_blocks(ctx, text, path)))
        is_map = title.lower().startswith("mapa do cap")
        if is_map:
            fm = re.search(r"^###\s+Para fixar\s*$\n(.*?)(?=^###?\s|\Z)", text, re.M | re.S)
            if fm:
                for ln in fm.group(1).splitlines():
                    mm = re.match(r"^\s*(?:[-*]|\d+[.)])\s+(.*)$", ln)
                    if mm:
                        fixar.append(inline(mm.group(1).strip()))
            head = (f'<div class="map-h"><div class="masc masc-sec">{mascot("revisao")}</div>'
                    f'<div><div class="sec-k">Hora da revisão</div><h2 id="{sid}"><span class="n">{num}</span>{inline(title)}</h2></div></div>')
            parts.append(f'<section class="sec mapa">{head}{inner}</section>')
        else:
            parts.append(f'<section class="sec"><h2 id="{sid}"><span class="n">{num}</span>{inline(title)}</h2>{inner}</section>')
    return RenderedChapter(lead_html=lead_html, objectives=objectives, sections=sections, body_html="".join(parts), fixar=fixar,
                           figures=ctx.fig)
