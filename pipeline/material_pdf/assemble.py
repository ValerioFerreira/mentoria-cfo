"""Monta o HTML do volume (capa, sumário, apresentação, capítulos, fixação, mapa, encerramento) com o template Jinja2."""
from __future__ import annotations

import datetime as dt
import json
import re

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from .load import ALTA_SCORE, DESIGN_DIR, Volume
from .render_md import inline, md, mascot, question_html, render_chapter

# Geometria fixa do rodapé (mm, a partir da borda inferior da folha A4). A faixa do titular fica no centro, vazia.
PAGE_W, PAGE_H = 210.0, 297.0
BAND_W, BAND_H, BAND_BOTTOM = 95.0, 6.0, 7.0
RULE_BOTTOM = 14.5
SIDE_MARGIN = 18.0
MM = 72 / 25.4

SITE = "www.missaomentoria.com.br"
LOGO_DIR = DESIGN_DIR / "logo"
RED, LIGHT, WHITE = "#d4301f", "#f3f5f8", "#ffffff"


def tape_svg(w_mm: float, h_mm: float, stripe_mm: float, colors: tuple[str, str] = (RED, LIGHT)) -> Markup:
    """Faixa refletiva em SVG com polígonos de cor sólida (o gradiente CSS vira mancha rosa em alguns leitores de PDF)."""
    a, b = colors
    pitch = stripe_mm * 2
    polys = []
    x = -h_mm
    while x < w_mm + h_mm:
        polys.append(f'<polygon points="{x + h_mm:.2f},0 {x + h_mm + stripe_mm:.2f},0 {x + stripe_mm:.2f},{h_mm:.2f} {x:.2f},{h_mm:.2f}"/>')
        x += pitch
    return Markup(f'<svg class="tape-svg" viewBox="0 0 {w_mm:.2f} {h_mm:.2f}" preserveAspectRatio="none" aria-hidden="true">'
                  f'<rect width="{w_mm:.2f}" height="{h_mm:.2f}" fill="{b}"/><g fill="{a}">{"".join(polys)}</g></svg>')


def band_rect_pt() -> list[float]:
    """Retângulo da faixa do titular em pontos PDF, origem no canto superior esquerdo (como o PyMuPDF)."""
    x0 = (PAGE_W - BAND_W) / 2
    y1 = PAGE_H - BAND_BOTTOM
    return [round(x0 * MM, 2), round((y1 - BAND_H) * MM, 2), round((x0 + BAND_W) * MM, 2), round(y1 * MM, 2)]


def brand(dark: bool) -> Markup:
    """Marca: mascote do logo (sem o nome) num selo branco + nome MentorIA em SVG (o "IA" com o gradiente vermelho-dourado)."""
    color = WHITE if dark else "#0e1b2e"
    gid = "wmg-d" if dark else "wmg-l"
    wm = (f'<svg class="wm-svg" viewBox="0 0 112 30" aria-label="MentorIA"><defs><linearGradient id="{gid}" x1="0" x2="1">'
          f'<stop offset=".1" stop-color="#d4301f"/><stop offset=".95" stop-color="#e9a90c"/></linearGradient></defs>'
          f'<text x="0" y="24" font-family="Barlow Condensed" font-weight="700" font-size="28" fill="{color}">Mentor'
          f'<tspan fill="url(#{gid})" dx="0.6">IA</tspan></text></svg>')
    logo = LOGO_DIR / "logo-mascote.png"
    badge = f'<span class="logo-badge"><img src="{logo.as_uri()}" alt=""></span>' if logo.exists() else ""
    return Markup(f'<div class="brand">{badge}{wm}</div>')


def updated_on(v: Volume) -> str:
    """Data da última alteração do volume (content/material/atualizacao/datas.json; sem ela, o REVISAO.md), em dd/mm/aaaa."""
    f = DESIGN_DIR.parents[2] / "content" / "material" / "atualizacao" / "datas.json"
    iso = json.loads(f.read_text(encoding="utf-8")).get(v.id) if f.exists() else None
    if not iso:
        rev = v.dir / "REVISAO.md"
        found = re.findall(r"20\d\d-\d\d-\d\d", rev.read_text(encoding="utf-8")) if rev.exists() else []
        iso = max(found) if found else dt.date.today().isoformat()
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


def _strip_p(h: str) -> str:
    h = h.strip()
    m = re.fullmatch(r"<p>(.*)</p>", h, re.S)
    return m.group(1) if m and "<p>" not in m.group(1) else h


def build_html(v: Volume) -> tuple[str, dict]:
    """Devolve (HTML, info) — info traz as âncoras dos capítulos e seções para o índice e os marcadores."""
    chapters = []
    for c in v.chapters:
        anchor = f"cap{c.number}"
        r = render_chapter(c.body, c.number, anchor, c.path)
        support = " · ".join(t for _, t, _ in r.sections if not t.lower().startswith("mapa do cap"))
        if len(support) > 110:
            support = support[:107].rsplit(" ", 1)[0] + "…"
        chapters.append({
            "number": c.number, "title": c.title, "anchor": anchor, "trecho": c.trecho, "r": r, "support": support,
            "cai": c.importance >= ALTA_SCORE or c.tier == "ALTA",
            "m_missao": Markup(mascot("missao", dark=True)), "m_cai": Markup(mascot("cai-na-prova", dark=True)),
        })
        r.lead_html = Markup(r.lead_html)
        r.body_html = Markup(r.body_html)
        r.objectives = [Markup(o) for o in r.objectives]
        r.fixar = [Markup(f) for f in r.fixar]
        r.sections = [(n, Markup(inline(t)), a) for n, t, a in r.sections]

    titles = {c.trecho: (c.number, c.title) for c in v.chapters}
    groups: dict[str, dict] = {}
    qs = []
    for q in v.questions:
        num, title = titles.get(q.chapter, (0, "Outros assuntos"))
        g = groups.setdefault(q.chapter, {"number": num, "title": title, "anchor": f"cap{num}", "qs": []})
        alt_comments = []
        if q.kind != "CERTO_ERRADO":
            for L, _ in q.options:
                t = q.option_comments.get(L)
                if t:
                    alt_comments.append((L, Markup(_strip_p(md(t))), L == q.answer))
        item = {
            "number": q.number, "origin": q.origin, "kind": q.kind, "answer": q.answer,
            "base_html": Markup(question_html(q.base_text)) if q.base_text else "",
            "st_html": Markup(question_html(q.statement)),
            "opts_html": [(L, Markup(_strip_p(question_html(t)))) for L, t in q.options],
            "comment_html": Markup(md(q.comment)), "alt_comments": alt_comments,
        }
        g["qs"].append(item)
        qs.append(item)
    qgroups = sorted(groups.values(), key=lambda g: g["number"])

    env = Environment(loader=FileSystemLoader(str(DESIGN_DIR)), autoescape=select_autoescape(["html", "j2"]))
    tpl = env.get_template("template.html.j2")
    today = dt.date.today()
    side_w = (PAGE_W - 2 * SIDE_MARGIN - BAND_W) / 2
    html_ = tpl.render(
        v=v, chapters=chapters, questions=qs, qgroups=qgroups,
        intro={
            "apresentacao": Markup(md(v.intro.get("Apresentação", ""))),
            "aprender": Markup(md(v.intro.get("O que você vai aprender", ""))),
            "prereq": Markup(md(v.intro.get("Pré-requisitos", ""))),
        },
        fonts=(DESIGN_DIR / "fonts").as_uri(), vendor=(DESIGN_DIR / "vendor").as_uri(), css=(DESIGN_DIR / "prontidao.css").as_uri(),
        brand_dark=brand(True), site=SITE,
        logo_full=(LOGO_DIR / "logo-completo.png").as_uri(),
        tape_cover=tape_svg(272, 12.4, 4.4), tape_band=tape_svg(210, 2.3, 2.0), tape_rule=tape_svg(174, 1.4, 1.3, (RED, WHITE)),
        m_praticar=Markup(mascot("praticar")), m_gabarito=Markup(mascot("gabarito")), m_revisao=Markup(mascot("revisao")),
        m_fim=Markup(mascot("missao-cumprida")),
        head_left=f"{v.subject_name} · {v.label}", foot_left=f"MentorIA · {v.label}",
        g={"band_bottom": BAND_BOTTOM, "band_h": BAND_H, "rule_bottom": RULE_BOTTOM, "side_w": round(side_w, 2)},
        year=today.year, edition=today.strftime("%m/%Y"), updated=updated_on(v),
    )
    info = {
        "chapters": [{"trecho": c["trecho"], "number": c["number"], "title": c["title"], "anchor": c["anchor"],
                      "sections": [(n, re.sub(r"<[^>]+>", "", str(t)), a) for n, t, a in c["r"].sections]} for c in chapters],
        "questions": [(q.number, q.answer) for q in v.questions],
        "updated": updated_on(v),
    }
    return html_, info
