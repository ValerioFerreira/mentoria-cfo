"""Figuras dos capítulos: grafico (matplotlib -> SVG), molecula (RDKit -> SVG), svg autoral (sanitizado) e mermaid
(marcado para o navegador renderizar antes da paginação)."""
from __future__ import annotations

import html
import io
import json
import math
import re

from validate_material import check_grafico, check_molecula, check_svg, eval_expr

from .load import DESIGN_DIR, ContentError

PALETTE = ["#2563eb", "#d4301f", "#059669", "#d9640f", "#7c3aed", "#e9a90c"]
INK, MUTED, LINE = "#0e1b2e", "#5b6778", "#dce2ea"

_mpl_ready = False


def _mpl():
    global _mpl_ready
    import logging

    import matplotlib

    matplotlib.use("Agg")
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
    import matplotlib.pyplot as plt
    from matplotlib import font_manager

    if not _mpl_ready:
        for f in ("PublicSans-VF.ttf", "PublicSans-Italic-VF.ttf"):
            font_manager.fontManager.addfont(str(DESIGN_DIR / "fonts" / f))
        plt.rcParams.update({
            "svg.fonttype": "none", "svg.hashsalt": "mentoria", "font.family": "Public Sans", "font.size": 9,
            "axes.edgecolor": MUTED, "axes.labelcolor": INK, "axes.titlecolor": INK, "axes.titleweight": "bold",
            "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": LINE, "grid.linewidth": 0.6,
            "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK, "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
            "legend.frameon": False, "figure.dpi": 100,
        })
        _mpl_ready = True
    return plt


def _svg_text(fig) -> str:
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True, metadata={"Date": None})
    s = buf.getvalue()
    s = s[s.index("<svg"):]
    s = re.sub(r"font-family:[^;\"']*", "font-family:'Public Sans','Noto Sans','Noto Sans Math'", s)
    return re.sub(r'\s(width|height)="[\d.]+pt"', "", s, count=2)


def grafico(spec: str) -> str:
    errs = check_grafico(spec)
    if errs:
        raise ContentError("; ".join(errs))
    g = json.loads(spec)
    plt = _mpl()
    fig, ax = plt.subplots(figsize=(6.3, 3.4))
    tipo = g["tipo"]
    if tipo == "funcao":
        a, b = g["dominio"]
        xs = [a + (b - a) * k / 400 for k in range(401)]
        for f in g["funcoes"]:
            ys = []
            for x in xs:
                try:
                    v = eval_expr(str(f["expr"]), x)
                    ys.append(v if math.isfinite(v) and abs(v) < 1e6 else float("nan"))
                except (ZeroDivisionError, OverflowError, ValueError):
                    ys.append(float("nan"))
            ax.plot(xs, ys, linewidth=1.8, label=f.get("rotulo"))
        ax.axhline(0, color=MUTED, linewidth=0.8)
        ax.axvline(0, color=MUTED, linewidth=0.8)
        for p in g.get("pontos", []) or []:
            ax.plot([p["x"]], [p["y"]], "o", color=INK, markersize=4)
            if p.get("rotulo"):
                ax.annotate(p["rotulo"], (p["x"], p["y"]), textcoords="offset points", xytext=(5, 6), fontsize=8, color=INK)
    elif tipo in {"linhas", "dispersao"}:
        for s in g["series"]:
            if tipo == "linhas":
                ax.plot(s["x"], s["y"], marker="o", markersize=3, linewidth=1.8, label=s.get("rotulo"))
            else:
                ax.scatter(s["x"], s["y"], s=16, label=s.get("rotulo"))
    elif tipo == "barras":
        cats = g["categorias"]
        n = len(g["series"])
        w = 0.8 / n
        for i, s in enumerate(g["series"]):
            ax.bar([k + (i - (n - 1) / 2) * w for k in range(len(cats))], s["valores"], width=w, label=s.get("rotulo"))
        ax.set_xticks(range(len(cats)), cats)
        ax.grid(axis="x", visible=False)
    elif tipo == "setores":
        ax.grid(False)
        ax.pie(g["valores"], labels=g["categorias"], colors=PALETTE, autopct="%1.0f%%", startangle=90,
               wedgeprops={"linewidth": 1, "edgecolor": "white"}, textprops={"color": INK, "fontsize": 8.5})
        ax.axis("equal")
    elif tipo == "histograma":
        for (a, b), fq in zip(g["classes"], g["frequencias"]):
            ax.bar(a, fq, width=b - a, align="edge", color=PALETTE[0], edgecolor="white", linewidth=1)
        ax.grid(axis="x", visible=False)
    ax.set_title(g.get("titulo", ""), fontsize=10, loc="left")
    if g.get("eixoX"):
        ax.set_xlabel(g["eixoX"])
    if g.get("eixoY"):
        ax.set_ylabel(g["eixoY"])
    handles, labels = ax.get_legend_handles_labels()
    if tipo not in {"setores", "histograma"} and any(labels) and len(handles) > 1:
        ax.legend(fontsize=8)
    svg = _svg_text(fig)
    plt.close(fig)
    return svg


def molecula(spec: str) -> str:
    errs = check_molecula(spec)
    if errs:
        raise ContentError("; ".join(errs))
    try:
        from rdkit import Chem
        from rdkit.Chem.Draw import rdMolDraw2D
    except ImportError as e:  # pragma: no cover - depende da instalação
        raise ContentError("molecula ainda não suportada (RDKit não instalado)") from e
    d = json.loads(spec)
    items = d if isinstance(d, list) else [d]
    parts = []
    for it in items:
        mol = Chem.MolFromSmiles(it["smiles"])
        if mol is None:
            raise ContentError(f"molecula: SMILES inválido {it['smiles']!r}")
        dr = rdMolDraw2D.MolDraw2DSVG(260, 200)
        o = dr.drawOptions()
        o.clearBackground = False
        o.fontFile = str(DESIGN_DIR / "fonts" / "PublicSans-VF.ttf")
        dr.DrawMolecule(mol)
        dr.FinishDrawing()
        s = dr.GetDrawingText()
        s = s[s.index("<svg"):]
        parts.append(f'<div class="mol"><div class="mol-svg">{s}</div><div class="mol-l">{html.escape(it["rotulo"])}</div></div>')
    return f'<div class="mols">{"".join(parts)}</div>'


def svg_autoral(src: str, prefix: str) -> str:
    errs = check_svg(src)
    if errs:
        raise ContentError("; ".join(errs))
    s = src.strip()
    s = re.sub(r"<\?xml[^>]*>", "", s)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"\son\w+\s*=\s*(\"[^\"]*\"|'[^']*')", "", s)  # sem handlers de evento
    s = re.sub(r'\sid="([^"]+)"', lambda m: f' id="{prefix}-{m.group(1)}"', s)
    s = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{prefix}-{m.group(1)})", s)
    s = re.sub(r'(xlink:href|href)="#([^"]+)"', lambda m: f'{m.group(1)}="#{prefix}-{m.group(2)}"', s)
    s = re.sub(r"<svg\b", '<svg class="svg-a"', s, count=1)
    return s


def mermaid(src: str, fid: str) -> str:
    """O texto vai em JSON num atributo; o template chama mermaid.render() antes do Paged.js. Rótulos com '\\n' viram <br>."""
    text = src.replace("\\n", "<br>")
    return f'<div class="mmd" id="{fid}" data-src="{html.escape(json.dumps(text, ensure_ascii=False), quote=True)}"></div>'


def render(lang: str, content: str, fid: str) -> str:
    if lang == "grafico":
        return grafico(content)
    if lang == "molecula":
        return molecula(content)
    if lang == "svg":
        return svg_autoral(content, fid)
    if lang == "mermaid":
        return mermaid(content, fid)
    raise ContentError(f"bloco ```{lang} não é figura")
