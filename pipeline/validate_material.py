"""Validador do material próprio MentorIA (content/material/<disciplina>/mNN/).

Cada volume é uma pasta com:
  volume.md       apresentação do volume (front matter + texto)
  aNN-sNN.md      um capítulo por trecho do volume (= 1 atividade de Teoria), na ordem de content/material/volumes
  fixacao.json    questões comentadas da Fixação do volume

Regras completas e o porquê de cada uma: pipeline/briefs/material.md. ERRO bloqueia a entrega; AVISO vai para o revisor.

Uso:  python pipeline/validate_material.py content/material/<disc>/mNN          (um volume)
      python pipeline/validate_material.py content/material/<disc>/mNN/a00-s01.md (um capítulo)
      python pipeline/validate_material.py --all                                   (tudo o que existe)
      python pipeline/validate_material.py --status [--wave N]                     (andamento por volume)
"""
from __future__ import annotations

import argparse
import ast
import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from summary_coverage import coverage_of, salient_terms, tokens  # noqa: E402
from validate_content import SHINGLE_N, is_authored, load_segments, load_source_shingles, words  # noqa: E402
from validate_summaries import FORBIDDEN as SUMMARY_FORBIDDEN, check_markdown, copied_runs, is_trivial_run  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = CONTENT_DIR.parent
MATERIAL_DIR = CONTENT_DIR / "material"
QUESTIONS_DIR = ROOT / "pipeline" / ".cache" / "material" / "questoes"

AGENT_STATUS = {"RASCUNHO", "PRONTO_PARA_REVISAO"}
REVIEW_STATUS = {"EM_REVISAO", "DEVOLVIDO", "APROVADO"}
CALLOUTS = {"objetivos", "atencao", "bizu", "exemplo", "lei", "jurisprudencia", "pegadinha", "esquema", "resolvido"}
FIGURE_LANGS = {"mermaid", "svg", "grafico", "molecula"}
LEGAL = {"direito-administrativo", "direito-constitucional", "direito-penal", "direito-penal-militar", "direito-processual-penal",
         "direito-processual-penal-militar", "direitos-humanos", "legislacoes-pe", "legislacao-pcpe", "legislacao-penal-especial"}
EXACT = {"matematica", "estatistica", "fisica", "quimica", "raciocinio-logico", "contabilidade-geral"}
NO_SOURCE_COVERAGE = {"atualidades"}  # conteúdo vem do noticiário, não da régua

# Originalidade (fora dos quadros [!lei], que podem citar a norma literalmente)
COPY_RUN_ERROR = 16
COPY_TOTAL_ERROR = 60
# Cobertura dos termos específicos da fonte (o capítulo tem ~75% do volume da fonte: espera-se cobrir quase tudo)
COVERAGE_ERROR = 0.50
COVERAGE_WARN = 0.60  # calibrado no piloto (29/10/2026): capítulos completos e corretos ficaram entre 0,65 e 0,84
LEI_BLOCK_MAX_WORDS = 160
LEI_SHARE_MAX = 0.20
# [!lei] é transcrição literal: fração mínima de sequências de 6 palavras do quadro presentes na norma em cache (pipeline/leis.py).
# Recortes com "(...)" e incisos em lista ficam acima de 0,7; paráfrase fica abaixo de 0,3. O quadro sai da checagem de
# originalidade, então paráfrase dentro dele também esconderia cópia do material-base.
LEI_LITERAL_MIN = 0.6
LEI_TITLE_KEYS = [
    (r"constitui[çc][ãa]o federal|\bCF\b|CF/88|CRFB", "cf"),
    (r"processo penal militar|\bCPPM\b|1\.002/1969", "cppm"),
    (r"penal militar|\bCPM\b|1\.001/1969", "cpm"),
    (r"processo penal|\bCPP\b|3\.689/1941", "cpp"),
    (r"c[óo]digo penal|\bCP\b|2\.848/1940", "cp"),
    (r"\bECA\b", "l8069"),
]
LEAD_MIN, LEAD_MAX = 50, 200
FIXAR_MIN, FIXAR_MAX = 6, 10
SECTION_MIN_WORDS = 120
# Estilo (calibrado no piloto de 29/10/2026): texto de concurso para quem estuda sozinho, não peça jurídica.
JARGON = ["castrense", "consubstanci", "hígid", "celeuma", "de escol", "alienígena", "precípu", "plexo", "axiológic", "vigas mestras",
          "nada obstante", "insta salientar", "cumpre assinalar", "cumpre analisar", "outrossim", "destarte", "mister se faz", "deveras",
          "sobremaneira", "hodiern", "mormente", "conquanto", "vetor normativo", "dialétic", "expungi", "balizas"]
JARGON_WHOLE = {"de escol", "plexo", "celeuma", "deveras", "balizas", "outrossim", "destarte", "conquanto", "mormente"}
JARGON_MAX = 3
SENTENCE_WORDS_WARN = 28
CALLOUT_WORDS_MIN = 250  # mais de 1 quadro a cada 250 palavras fragmenta a leitura

FORBIDDEN = SUMMARY_FORBIDDEN + [
    "estratégia", "estrategia", "professor", "professora", "neste curso", "do curso", "nosso curso", "no material", "nossa aula",
    "na aula", "nesta página", "na página anterior", "na próxima página", "página seguinte", "olá, pessoal", "galera", "pessoal,",
    "aluno(a)", "chatgpt", "inteligência artificial gerou", "como modelo de linguagem", "não tenho acesso", "[citation",
    "wikipedia", "wikipédia", "segundo o texto-fonte", "texto-fonte", "material-base", "material base",
    "texto de apoio", "material de apoio", "texto-base",
]
# Remissão ao material-base por página, aula ou "material de referência" (frente C, 01/11/2026)
REMISSAO = re.compile(
    r"\b(?:na|exemplo\s+da|aten[çc][ãa]o\s+d[ao]s?)\s+p[áa]ginas?\s+\d+"            # "Na página 9", "Ponto de Atenção da Página 22"
    r"|\(\s*(?:fonte\s*,\s*)?p[áa]g(?:ina|s?\.)\s*\d+(?!\s*,)"                             # "(Página 53)", "(Fonte, pág. 36)", "(pág. 32)"
    r"|\bp[áa]g(?:inas?|s?\.)\s*\d+(?:\s*(?:a|e)\s*\d+)?\s+d[ao]s?\s+(?:material|manual|apostila|fonte|livro|texto)"
    r"|\baulas?\s+\d{1,2}\b|\bfonte\s+te[óo]rica|\bda\s+apostila\b"
    r"|\b(?:material|manual|texto)(?:\s+did[áa]tico)?\s+de\s+refer[êe]ncia|\(fonte\s*,", re.I)
# Neutralidade (decisão do dono, 02/11/2026): o material serve a qualquer concurso; nada de direcionar a preparação para um
# concurso, órgão, cargo ou banca. Exemplo ambientado numa instituição é permitido (AVISO só para o revisor conferir).
DIRECIONA = re.compile(
    r"\bse\s+voc[eê]\s+(?:est[aá]|vai|for)\b[^.\n]{0,40}\bprepar"
    r"|\bpara\s+quem\s+(?:presta|faz|vai\s+prestar|se\s+prepara|estuda\s+para)\b"
    r"|\bvoltad[oa]s?\s+(?:para|ao|à|aos|às)\s+(?:o\s+|a\s+|os\s+|as\s+)?(?:concursos?|provas?|certames?|candidat\w*|carreiras?\s+(?:de|da|do))"
    r"|\bconcursos?\s+(?:de|do|da|dos|das|para|ao|à)\s+(?:o\s+|a\s+)?(?:oficia\w*|soldad\w*|bombeir\w*|pol[ií]cia\w*|agente\s+de\s+pol|delegad\w*|escriv\w*|pra[çc]as?\b|cfoa?\b|cfhp\b|cbm|pmpe|pcpe|corpo\s+de\s+bombeiros|forças?\s+de\s+segurança)"
    r"|\b(?:provas?|editais?|edital|certames?)\s+(?:do|da|de|para|dos|das)\s+(?:o\s+|a\s+)?(?:cbmpe|pmpe|pcpe|cfoa|cfhp|cfo\b|oficia\w*|soldad\w*|bombeir\w*|agente\s+de\s+pol|corpo\s+de\s+bombeiros|pol[ií]cia\s+(?:militar|civil))"
    r"|\bcandidat[oa]s?\s+(?:a|ao|à|aos|às)\s+(?:oficial|soldado|bombeiro|agente|cfoa|cfhp|cfo\b|pmpe|cbmpe|pcpe)"
    r"|\bCFOA\b",
    re.I)
BANCA = re.compile(r"\b(?:Instituto\s+)?AOCP\b|\bCebraspe\b|\bCespe\b|\bVunesp\b|\bIBFC\b|\bIAUPE\b|\bUPENET\b|\bFGV\b|\bFCC\b|\bIDECAN\b|\bQuadrix\b|\bConsulplan\b")
INSTITUICAO = re.compile(r"\b(?:CBMPE|PMPE|PCPE|CFHP|CFO)\b|Corpo\s+de\s+Bombeiros\s+Militar\s+de\s+Pernambuco|Pol[ií]cia\s+(?:Militar|Civil)\s+de\s+Pernambuco", re.I)


def neutrality(text: str, where: str = "") -> tuple[list[str], list[str]]:
    """(erros, avisos) de direcionamento a concurso, banca ou instituição. Ignora o texto dos quadros [!lei]."""
    t = strip_lei(text)
    errs = [f"{where}direciona a um concurso: “{m}”; escreva para qualquer concurso" for m in sorted({x.group(0) for x in DIRECIONA.finditer(t)})]
    errs += [f"{where}nome de banca: “{m}”; escreva 'a banca' / 'as bancas'" for m in sorted({x.group(0) for x in BANCA.finditer(t)})]
    warns = [f"{where}cita a instituição “{m}”: confirme que é só exemplo ou conteúdo legal" for m in sorted({x.group(0) for x in INSTITUICAO.finditer(t)})]
    return errs, warns


REMISSAO_FONTE = re.compile(r"\bapostila\b|\baula\s+\d|material(?:\s+did[áa]tico)?\s+de\s+refer[êe]ncia|estrat[ée]gia", re.I)
# Matemática escrita em ASCII (x_barra, mu_0, sigma^2, raiz(n), chi2, "37 por cento"): estatística e exatas (31/10 e 01/11/2026)
ASCII_MATH = re.compile(r"\b\w+_barra\b|\bx_bar\b|\b\w+_chapeu\b|\bmu_\w+|\b(?:sigma|lambda|chi2)\b|[A-Za-z0-9)\]₀-₉]\^[0-9]|raiz\(|\d por cento\b")
LATEX = re.compile(r"\$[^$\n]+\$|\\(?:frac|sqrt|cdot|times|alpha|beta|sum|int|left|right|begin)\b|\\\(|\\\[")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿]")
BIDI = re.compile(r"[​-‏‪-‮⁦-⁩﻿]")
FENCE = re.compile(r"^```([a-z]*)[ \t]*(.*?)\n(.*?)^```[ \t]*$", re.M | re.S)
CALLOUT_HEAD = re.compile(r"^>\s*\[!([a-zçãéí]+)\]\s*(.*)$")
H2 = re.compile(r"^##\s+(.+?)\s*$", re.M)
H3 = re.compile(r"^###\s+(.+?)\s*$", re.M)
ITEM = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+\S", re.M)
SMILES = re.compile(r"^[A-Za-z0-9@+\-\[\]\(\)=#$/\\%.:*]+$")
STOP = {"de", "da", "do", "das", "dos", "e", "a", "o", "as", "os", "em", "no", "na", "nos", "nas", "para", "por", "com", "sem",
        "um", "uma", "ao", "aos", "à", "às", "que", "se", "sua", "seu", "lei", "art", "arts", "noções", "conceito", "conceitos"}


# ------------------------------------------------------------------------------------------------- utilidades
def word_count(text: str) -> int:
    return len(re.findall(r"\w+", re.sub(r"[|*#>`_-]+", " ", text)))


def parse_front_matter(text: str) -> tuple[dict, str, list[str]]:
    """Front matter entre linhas '---'; cada linha 'chave: <valor JSON>' (texto entre aspas, listas e objetos em JSON)."""
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["o arquivo deve começar com o front matter (linha '---')"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["front matter sem a linha '---' de fechamento"]
    meta: dict = {}
    for n, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            errors.append(f"front matter, linha {n}: use 'chave: valor'")
            continue
        try:
            meta[m.group(1)] = json.loads(m.group(2))
        except json.JSONDecodeError:
            errors.append(f"front matter, linha {n}: o valor de '{m.group(1)}' deve ser JSON (texto entre aspas duplas, listas com [ ])")
    return meta, text[end + 5:], errors


def fences(body: str) -> tuple[str, list[dict]]:
    """Remove os blocos ``` do texto (não contam como palavras) e devolve a lista de blocos."""
    blocks = []
    for m in FENCE.finditer(body):
        blocks.append({"lang": m.group(1), "caption": m.group(2).strip(), "content": m.group(3), "line": body[: m.start()].count("\n") + 1})
    return FENCE.sub("\n", body), blocks


def callouts(body: str) -> list[dict]:
    """Quadros: linha '> [!tipo] Título' seguida de linhas '>'."""
    out = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        m = CALLOUT_HEAD.match(lines[i])
        if m:
            j = i + 1
            content = []
            while j < len(lines) and lines[j].startswith(">"):
                content.append(lines[j][1:].strip())
                j += 1
            out.append({"type": m.group(1), "title": m.group(2).strip(), "text": "\n".join(content), "line": i + 1})
            i = j
        else:
            i += 1
    return out


def strip_lei(body: str) -> str:
    """Texto sem os quadros [!lei] (citação literal de norma é permitida e não entra na checagem de originalidade)."""
    out, skip = [], False
    for ln in body.splitlines():
        m = CALLOUT_HEAD.match(ln)
        if m:
            skip = m.group(1) == "lei"
            if skip:
                continue
        elif skip and ln.startswith(">"):
            continue
        else:
            skip = False
        out.append(ln)
    return "\n".join(out)


_LAW_GRAMS: dict[str, set[str] | None] = {}


def _law_words(s: str) -> list[str]:
    import unicodedata
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\[revogado[^\]]*\]", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).split()


def lei_literal_score(title: str, text: str) -> tuple[str, float] | None:
    """(norma, fração de 6-gramas do quadro achados na norma em cache) ou None se a norma não está no cache."""
    from check_citations import NUM2KEY
    from leis import LEIS_DIR
    key = None
    m = re.search(r"([\d.]+)/(\d{4})", title)
    if m:
        key = NUM2KEY.get((m.group(1).replace(".", ""), m.group(2)))
    if not key:
        key = next((k for rx, k in LEI_TITLE_KEYS if re.search(rx, title, re.I)), None)
    if not key:
        return None
    if key not in _LAW_GRAMS:
        p = LEIS_DIR / f"{key}.clean.txt"
        if p.exists():
            w = _law_words(p.read_text(encoding="utf-8"))
            _LAW_GRAMS[key] = {" ".join(w[i:i + 6]) for i in range(len(w) - 5)}
        else:
            _LAW_GRAMS[key] = None
    grams_law = _LAW_GRAMS[key]
    if grams_law is None:
        return None
    w = _law_words(re.sub(r"\*\*|\(\.\.\.\)|\[\.\.\.\]|…", " ", text))
    grams = [" ".join(w[i:i + 6]) for i in range(len(w) - 5)]
    if len(grams) < 3:
        return None
    return key, sum(g in grams_law for g in grams) / len(grams)


def tables(body: str) -> list[list[str]]:
    res, cur = [], []
    for ln in body.splitlines():
        if ln.strip().startswith("|"):
            cur.append(ln)
        elif cur:
            res.append(cur)
            cur = []
    if cur:
        res.append(cur)
    return res


def key_terms(title: str) -> list[str]:
    return [w for w in tokens(title) if len(w) >= 5 and w not in STOP][:8]


def has_terms(text_tokens: set[str], terms: list[str]) -> float:
    if not terms:
        return 1.0
    stems = {w[:6] for w in text_tokens}
    return sum(1 for t in terms if t in text_tokens or t[:6] in stems) / len(terms)


# ------------------------------------------------------------------------------------------------- figuras
SAFE_FUN = {"sin", "cos", "tan", "exp", "log", "log10", "sqrt", "abs"}
SAFE_NODES = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd,
              ast.Constant, ast.Name, ast.Load, ast.Call)


def eval_expr(expr: str, x: float) -> float:
    tree = ast.parse(expr, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, SAFE_NODES):
            raise ValueError(f"elemento não permitido na expressão: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id not in SAFE_FUN | {"x", "pi", "e"}:
            raise ValueError(f"nome não permitido: {node.id}")
        if isinstance(node, ast.Call) and not (isinstance(node.func, ast.Name) and node.func.id in SAFE_FUN):
            raise ValueError("só as funções sin, cos, tan, exp, log, log10, sqrt, abs")
    env = {f: getattr(math, f) for f in SAFE_FUN if f != "abs"} | {"abs": abs, "x": x, "pi": math.pi, "e": math.e}
    return float(eval(compile(tree, "<expr>", "eval"), {"__builtins__": {}}, env))  # noqa: S307 (árvore validada acima)


def check_grafico(spec: str) -> list[str]:
    try:
        g = json.loads(spec)
    except json.JSONDecodeError as e:
        return [f"grafico: JSON inválido ({e.msg})"]
    errs = []
    tipo = g.get("tipo")
    if tipo not in {"funcao", "linhas", "barras", "setores", "dispersao", "histograma"}:
        return [f"grafico: tipo {tipo!r} inválido (funcao, linhas, barras, setores, dispersao, histograma)"]
    if tipo == "funcao":
        dom = g.get("dominio")
        fs = g.get("funcoes")
        if not (isinstance(dom, list) and len(dom) == 2 and dom[0] < dom[1]):
            errs.append("grafico funcao: 'dominio' deve ser [inicio, fim]")
        elif not isinstance(fs, list) or not fs:
            errs.append("grafico funcao: 'funcoes' deve ser uma lista de {\"expr\", \"rotulo\"}")
        else:
            for f in fs:
                try:
                    ok = 0
                    for k in range(21):
                        try:
                            v = eval_expr(str(f.get("expr", "")), dom[0] + (dom[1] - dom[0]) * k / 20)
                            ok += math.isfinite(v)
                        except (ZeroDivisionError, OverflowError, ValueError) as e:
                            if "permitid" in str(e) or "só as" in str(e):
                                raise
                    if ok < 10:
                        errs.append(f"grafico funcao: '{f.get('expr')}' indefinida na maior parte do domínio")
                except (SyntaxError, ValueError) as e:
                    errs.append(f"grafico funcao: expressão '{f.get('expr')}' inválida ({e})")
    elif tipo in {"linhas", "dispersao"}:
        for s in g.get("series", []) or [None]:
            if not s or len(s.get("x", [])) != len(s.get("y", [])) or not s.get("x"):
                errs.append(f"grafico {tipo}: cada série precisa de 'x' e 'y' do mesmo tamanho")
    elif tipo == "barras":
        cats = g.get("categorias", [])
        for s in g.get("series", []) or [None]:
            if not s or len(s.get("valores", [])) != len(cats) or not cats:
                errs.append("grafico barras: 'categorias' e 'valores' de cada série com o mesmo tamanho")
    elif tipo == "setores":
        if len(g.get("categorias", [])) != len(g.get("valores", [])) or not g.get("valores"):
            errs.append("grafico setores: 'categorias' e 'valores' do mesmo tamanho")
    elif tipo == "histograma":
        if len(g.get("classes", [])) != len(g.get("frequencias", [])) or not g.get("classes"):
            errs.append("grafico histograma: 'classes' ([inicio, fim]) e 'frequencias' do mesmo tamanho")
    if not str(g.get("titulo", "")).strip():
        errs.append("grafico: falta 'titulo'")
    return errs


def check_svg(src: str) -> list[str]:
    errs = []
    if len(src.encode("utf-8")) > 20000:
        errs.append("svg: maior que 20 KB (simplifique o desenho)")
    low = src.lower()
    for bad in ("<script", "foreignobject", "<image", "href=\"http", "xlink:href=\"http", "@import", "url(http"):
        if bad in low:
            errs.append(f"svg: elemento proibido ({bad})")
    try:
        root = ET.fromstring(src)
    except ET.ParseError as e:
        return errs + [f"svg: XML inválido ({e})"]
    if not root.tag.endswith("svg"):
        errs.append("svg: o elemento raiz deve ser <svg>")
    if "viewBox" not in root.attrib:
        errs.append("svg: falta o atributo viewBox")
    if not any(el.tag.endswith("text") for el in root.iter()):
        errs.append("svg: sem nenhum <text> (figura sem rótulos não ensina)")
    return errs


def check_mermaid(src: str) -> list[str]:
    first = next((ln.strip() for ln in src.splitlines() if ln.strip() and not ln.strip().startswith("%%")), "")
    if not re.match(r"^(flowchart|graph|mindmap|timeline|sequenceDiagram|stateDiagram(-v2)?|classDiagram|pie|quadrantChart)\b", first):
        return ["mermaid: comece com flowchart, mindmap, timeline, sequenceDiagram, stateDiagram, classDiagram, pie ou quadrantChart"]
    errs = []
    if re.search(r"^\s*(click|href)\b", src, re.M) or "http" in src:
        errs.append("mermaid: sem links (click/href/http)")
    if len(src.splitlines()) > 45:
        errs.append("mermaid: mais de 45 linhas (divida em dois diagramas)")
    return errs


def check_molecula(src: str) -> list[str]:
    try:
        d = json.loads(src)
    except json.JSONDecodeError as e:
        return [f"molecula: JSON inválido ({e.msg})"]
    items = d if isinstance(d, list) else [d]
    errs = []
    for it in items:
        if not isinstance(it, dict) or not SMILES.match(str(it.get("smiles", ""))) or not str(it.get("rotulo", "")).strip():
            errs.append("molecula: cada item precisa de 'smiles' válido e 'rotulo'")
    return errs


# ------------------------------------------------------------------------------------------------- capítulo
def load_metrics(subject: str) -> dict[str, dict]:
    f = MATERIAL_DIR / "metrics" / f"{subject}.json"
    if not f.exists():
        return {}
    return {r["id"]: r for r in json.loads(f.read_text(encoding="utf-8"))["trechos"]}


def load_volume(volume_id: str) -> dict | None:
    subject = volume_id.split("/")[0]
    f = MATERIAL_DIR / "volumes" / f"{subject}.json"
    if not f.exists():
        return None
    return next((v for v in json.loads(f.read_text(encoding="utf-8"))["volumes"] if v["id"] == volume_id), None)


def chapter_file(volume_dir: Path, trecho: str) -> Path:
    aula, seg = trecho.split("/")[1:]
    return volume_dir / f"{aula}-{seg}.md"


_SHINGLES: dict[str, set | None] = {}


def validate_chapter(path: Path) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warns: list[str] = []
    text = path.read_text(encoding="utf-8")
    meta, body, fm_err = parse_front_matter(text.replace("\r\n", "\n"))
    errors += fm_err
    sid = meta.get("id", "")
    subject = sid.split("/")[0] if sid else path.parent.parent.name
    stats: dict = {"id": sid}
    for k in ("id", "volume", "capitulo", "titulo", "fingerprint", "status", "autor", "edital", "fontes", "notas"):
        if k not in meta:
            errors.append(f"front matter sem '{k}'")
    if errors and not sid:
        return errors, warns, stats
    metrics = load_metrics(subject).get(sid)
    segs = load_segments(subject) if (CONTENT_DIR / "segments" / f"{subject}.json").exists() else {}
    ref = segs.get(sid)
    if not ref or not metrics:
        return errors + [f"trecho {sid!r} inexistente ou sem régua (content/material/metrics)"], warns, stats
    if path.name != f"{sid.split('/')[1]}-{sid.split('/')[2]}.md":
        errors.append(f"nome do arquivo deve ser {sid.split('/')[1]}-{sid.split('/')[2]}.md")
    if meta.get("volume") != metrics["volume"]:
        errors.append(f"volume {meta.get('volume')!r} diferente do previsto ({metrics['volume']})")
    if meta.get("capitulo") != metrics["chapter"]:
        errors.append(f"capitulo {meta.get('capitulo')!r} diferente do previsto ({metrics['chapter']})")
    if meta.get("fingerprint") != metrics["fingerprint"]:
        errors.append(f"impressão digital diferente da atual ({metrics['fingerprint']}) — o trecho foi resegmentado?")
    status = meta.get("status")
    if status not in AGENT_STATUS | REVIEW_STATUS:
        errors.append(f"status {status!r} inválido (RASCUNHO ou PRONTO_PARA_REVISAO)")
    titulo = str(meta.get("titulo", ""))
    if not 8 <= len(titulo) <= 90:
        errors.append("titulo deve ter de 8 a 90 caracteres")
    fontes = meta.get("fontes")
    if not isinstance(fontes, list) or not all(isinstance(f, str) and len(f) > 15 for f in fontes or []):
        errors.append("fontes deve ser uma lista de textos ('Título — onde — consultado em AAAA-MM-DD')")
    elif subject in LEGAL and not any(re.search(r"planalto\.gov\.br|alepe|legis|stf\.jus|stj\.jus|in\.gov\.br|pe\.gov\.br", f, re.I) for f in fontes):
        errors.append("disciplina jurídica: cite o texto oficial da norma (planalto.gov.br, legis.alepe.pe.gov.br…) em 'fontes'")
    elif not fontes:
        errors.append("fontes vazia: registre as fontes consultadas")
    want_ed = {e["ref"] for e in metrics["edital"]}
    got_ed = set(meta.get("edital") or [])
    if want_ed - got_ed:
        errors.append(f"edital: faltam os itens {sorted(want_ed - got_ed)} (copie todos de material_ficha.py)")

    body_nofence, blocks = fences(body)
    stats["words"] = n = word_count(body_nofence)
    tg = metrics["targets"]
    stats["target"] = tg["words"]
    if n < tg["wordsMin"]:
        errors.append(f"{n} palavras: abaixo do mínimo ({tg['wordsMin']}; meta {tg['words']})")
    elif n > tg["words"] * 1.35:
        errors.append(f"{n} palavras: muito acima da meta ({tg['words']}; teto {int(tg['words'] * 1.35)})")
    elif n > tg["wordsMax"]:
        warns.append(f"{n} palavras: acima da faixa ({tg['wordsMax']}); confira se não há repetição")

    # estrutura
    if re.search(r"^#\s", body, re.M):
        errors.append("não use título '# ' (o título vem do front matter)")
    if re.search(r"^####", body, re.M):
        errors.append("use só '##' (seção) e '###' (subseção)")
    for h in H2.findall(body) + H3.findall(body):
        if re.match(r"^\d+(\.\d+)*[\s.)–-]", h):
            errors.append(f"título numerado à mão: '{h}' (a numeração é automática)")
        if len(h) > 80:
            warns.append(f"título longo (> 80 caracteres): '{h[:50]}…'")
    first_h = H2.search(body_nofence)
    lead_txt = body_nofence[: first_h.start()] if first_h else body_nofence
    lead = "\n".join(ln for ln in lead_txt.splitlines() if not ln.startswith(">"))
    lw = word_count(lead)
    if not LEAD_MIN <= lw <= LEAD_MAX:
        errors.append(f"abertura com {lw} palavras antes da primeira seção (use {LEAD_MIN} a {LEAD_MAX})")
    cos = callouts(body_nofence)
    objs = [c for c in cos if c["type"] == "objetivos"]
    if len(objs) != 1 or (first_h and objs and body_nofence.find("[!objetivos]") > first_h.start()):
        errors.append("um único quadro > [!objetivos] logo após a abertura, antes da primeira seção")
    elif not 3 <= len(ITEM.findall(objs[0]["text"])) <= 5:
        errors.append("[!objetivos] com 3 a 5 itens em lista")
    sections = H2.findall(body_nofence)
    if not sections or sections[-1].strip().lower() != "mapa do capítulo":
        errors.append("a última seção deve ser '## Mapa do capítulo'")
    content_sections = [s for s in sections if s.strip().lower() != "mapa do capítulo"]
    if len(content_sections) < 3:
        errors.append(f"{len(content_sections)} seções de conteúdo (mínimo 3, normalmente uma por tópico do trecho)")
    parts = re.split(r"^##\s+.+$", body_nofence, flags=re.M)[1:]
    for name, part in zip(sections, parts):
        if name.strip().lower() != "mapa do capítulo" and word_count(part) < SECTION_MIN_WORDS:
            warns.append(f"seção '{name}' com menos de {SECTION_MIN_WORDS} palavras: junte com outra ou desenvolva")
    mapa = parts[-1] if parts and sections and sections[-1].strip().lower() == "mapa do capítulo" else ""
    mapa_full = body[body.rfind("## Mapa do capítulo"):] if "## Mapa do capítulo" in body else ""
    if mapa_full and not (tables(mapa_full) or re.search(r"^```(mermaid|svg)", mapa_full, re.M) or "[!esquema]" in mapa_full):
        errors.append("o Mapa do capítulo precisa de uma tabela ou de um esquema que resuma o capítulo")
    fx = re.search(r"^###\s*Para fixar\s*$", mapa, re.M)
    if not fx:
        errors.append("o Mapa do capítulo termina com '### Para fixar'")
    else:
        k = len(ITEM.findall(mapa[fx.end():]))
        if not FIXAR_MIN <= k <= FIXAR_MAX:
            errors.append(f"'Para fixar' com {k} itens (use {FIXAR_MIN} a {FIXAR_MAX}, um por linha com '- ')")

    # quadros
    for c in cos:
        if c["type"] not in CALLOUTS:
            errors.append(f"quadro [!{c['type']}] desconhecido (linha {c['line']}); use: {', '.join(sorted(CALLOUTS))}")
        if not c["text"].strip() and c["type"] != "esquema":
            errors.append(f"quadro [!{c['type']}] vazio (linha {c['line']})")
        if c["type"] == "lei":
            if not re.search(r"(art\.|arts\.|§|súmula|lei|decreto|cf|cpm|cppm|cp\b|cpp|constitui)", c["title"], re.I):
                errors.append(f"[!lei] sem a referência no título (ex.: '> [!lei] CF, art. 5º, LXIX'), linha {c['line']}")
            if word_count(c["text"]) > LEI_BLOCK_MAX_WORDS:
                errors.append(f"[!lei] com mais de {LEI_BLOCK_MAX_WORDS} palavras (linha {c['line']}): cite só o essencial e explique")
            lit = lei_literal_score(c["title"], c["text"])
            if lit is not None and lit[1] < LEI_LITERAL_MIN:
                errors.append(f"[!lei] '{c['title']}' (linha {c['line']}) não confere com o texto oficial ({lit[1]:.0%} igual em "
                              f"'{lit[0]}'): o quadro é a letra da lei; transcreva o dispositivo vigente ou tire a paráfrase do quadro")
        if c["type"] == "jurisprudencia" and not re.search(r"\b(STF|STJ|STM|TST|TSE|TJ\w*|TCU)\b", c["title"]):
            errors.append(f"[!jurisprudencia] sem o tribunal no título (ex.: 'STF, Súmula 629'), linha {c['line']}")
    real = [c for c in cos if c["type"] in CALLOUTS - {"objetivos"}]
    stats["callouts"] = len(real)
    if len(real) > max(2 * tg["callouts"], n // CALLOUT_WORDS_MIN + 1):
        warns.append(f"{len(real)} quadros: excesso fragmenta a leitura (até ~1 a cada {CALLOUT_WORDS_MIN} palavras); deixe no texto o que não é destaque")
    if len(real) < tg["callouts"]:
        errors.append(f"{len(real)} quadros de destaque (meta mínima {tg['callouts']})")
    kinds = {c["type"] for c in real}
    if metrics["importance"]["tier"] == "ALTA" and "pegadinha" not in kinds:
        errors.append("trecho de importância ALTA: inclua ao menos um [!pegadinha]")
    if subject in LEGAL and "lei" not in kinds:
        warns.append("disciplina jurídica sem nenhum [!lei]: confira se não falta a letra da norma central")
    if subject in EXACT and "resolvido" not in kinds:
        errors.append("disciplina de cálculo: inclua ao menos um [!resolvido] (exercício resolvido passo a passo)")
    lei_words = sum(word_count(c["text"]) for c in cos if c["type"] == "lei")
    if n and lei_words / n > LEI_SHARE_MAX:
        errors.append(f"citações literais ([!lei]) somam {lei_words} palavras ({lei_words / n:.0%}); o limite é {LEI_SHARE_MAX:.0%}")

    # elementos visuais
    data_tables = [t for t in tables(body_nofence) if len(t) >= 4]
    figs = [b for b in blocks if b["lang"] in FIGURE_LANGS]
    for b in blocks:
        where = f"bloco ```{b['lang']} (linha {b['line']})"
        if b["lang"] not in FIGURE_LANGS:
            errors.append(f"{where}: linguagem não permitida (use mermaid, svg, grafico ou molecula)")
            continue
        if len(re.findall(r"\w+", b["caption"])) < 3:
            errors.append(f"{where}: falta a legenda na mesma linha (ex.: ```svg Forças no plano inclinado)")
        chk = {"svg": check_svg, "grafico": check_grafico, "mermaid": check_mermaid, "molecula": check_molecula}[b["lang"]]
        errors += [f"{where}: {e}" for e in chk(b["content"])]
    esquemas = [c for c in cos if c["type"] == "esquema" and (ITEM.search(c["text"]) or tables(c["text"]))]
    stats["visuals"] = vis = len(data_tables) + len(figs) + len(esquemas)
    if vis < tg["visuals"]:
        errors.append(f"{vis} elementos visuais (tabelas com 3+ linhas, figuras, esquemas); meta mínima {tg['visuals']}")
    if metrics["source"]["figures"] >= 4 and not figs:
        warns.append(f"a fonte tem {metrics['source']['figures']} figuras e o capítulo nenhuma figura (só tabelas): avalie um diagrama")

    # higiene
    low = body.lower()
    for bad in FORBIDDEN:
        if bad in low:
            errors.append(f"expressão proibida: “{bad}”")
    for m in sorted(set(x.group(0) for x in REMISSAO.finditer(body))):
        errors.append(f"remissão ao material-base (página, aula, 'material de referência'): “{m}”; afirme a regra sem citar a origem")
    ne, nw = neutrality(body)
    errors += ne
    warns += nw
    for f in meta.get("fontes") or []:
        if isinstance(f, str) and REMISSAO_FONTE.search(f):
            errors.append(f"fonte que remete ao material-base: “{f[:70]}”; cite só fontes primárias (lei, tribunal, órgão oficial, obra publicada)")
    if "�" in body or BIDI.search(body):
        errors.append("caracteres inválidos (� ou marcas invisíveis): corrija a codificação")
    for k, line in enumerate(body_nofence.split("\n"), 1):
        if re.search(r"\S.* > \[!\w+\]", line) and not line.lstrip().startswith(">"):
            errors.append(f"quadro colado ao fim de um parágrafo (o '> [!...]' precisa começar a linha, após linha em branco): “{line.strip()[:60]}…”")
    if LATEX.search(re.sub(r"R\$", "R", body_nofence)):  # "R$ 10 … R$ 20" é dinheiro, não LaTeX
        errors.append("não use LaTeX ($…$, \\frac…): escreva a fórmula em texto (x², √x, a·b, ≤, ≥, Δ)")
    if subject in EXACT:
        ascii_math = sorted(set(m.group(0) for m in ASCII_MATH.finditer(body_nofence)))
        if ascii_math:
            errors.append(f"matemática em ASCII ({', '.join(ascii_math[:6])}): use Unicode (x̄, μ₀, σ², √n, χ², p̂, ×, %)")
    if EMOJI.search(body_nofence):
        errors.append("não use emoji (os ícones dos quadros vêm do layout)")
    check_markdown(sid, body_nofence, errors)
    prose = "\n".join(ln for ln in body_nofence.splitlines() if ln.strip() and not ln.lstrip().startswith(("|", ">", "#", "-", "1.", "2.", "3.")))
    sentences = [x for x in re.split(r"(?<=[.!?])\s+", prose) if word_count(x) >= 3]
    if sentences:
        avg = sum(word_count(x) for x in sentences) / len(sentences)
        stats["sentenceWords"] = round(avg, 1)
        if avg > SENTENCE_WORDS_WARN:
            warns.append(f"frases longas (média de {avg:.0f} palavras): divida as frases; o aluno estuda sozinho e cansado")
    # início de palavra sempre; fim de palavra só nos termos inteiros ("de escol" não pode casar com "de escolha")
    jar_hits = {j: len(re.findall(r"(?<!\w)" + re.escape(j) + (r"(?!\w)" if j in JARGON_WHOLE else ""), low)) for j in JARGON}
    jar = [j for j, n in jar_hits.items() if n]
    jar_n = sum(jar_hits.values())
    stats["jargon"] = jar_n
    if jar_n > JARGON_MAX:
        warns.append(f"linguagem rebuscada ({jar_n} ocorrências: {', '.join(jar)}): troque por palavras simples (militar, conter, válido, polêmica...)")

    # originalidade (fora dos quadros [!lei])
    aula = ref["aula"]
    if not is_authored(aula):
        if aula not in _SHINGLES:
            _SHINGLES[aula] = load_source_shingles(aula)
        source = _SHINGLES[aula]
        if source is None:
            warns.append("cache do texto-fonte ausente: originalidade NÃO verificada")
        else:
            runs = [r for r in copied_runs(strip_lei(body_nofence), source) if not is_trivial_run(r)]
            total = sum(len(r) for r in runs)
            stats["copied"] = total
            for r in runs:
                snippet = f"“{' '.join(r[:14])}{'…' if len(r) > 14 else ''}” ({len(r)} palavras)"
                if len(r) >= COPY_RUN_ERROR:
                    errors.append(f"trecho copiado da fonte: {snippet}")
                else:
                    warns.append(f"coincidência com a fonte (definição/norma? reescreva se puder): {snippet}")
            if total >= COPY_TOTAL_ERROR:
                errors.append(f"coincidências com a fonte somam {total} palavras (limite {COPY_TOTAL_ERROR}): reescreva com suas palavras")

    # cobertura: termos específicos da fonte, tópicos e itens do edital
    toks = set(tokens(body))
    if subject not in NO_SOURCE_COVERAGE and not is_authored(aula):
        sal = salient_terms(subject, aula, ref["startPage"], ref["endPage"])
        if len(sal) >= 15:
            score, missing = coverage_of(body, sal)
            stats["coverage"] = round(score, 2)
            if score < COVERAGE_ERROR:
                errors.append(f"cobertura da fonte {score:.2f} (mínimo {COVERAGE_ERROR}); termos que faltam: {', '.join(missing[:15])}")
            elif score < COVERAGE_WARN:
                warns.append(f"cobertura da fonte {score:.2f} (esperado ≥ {COVERAGE_WARN}); faltam: {', '.join(missing[:12])}")
    for t in metrics["topics"]:
        if has_terms(toks, key_terms(t)) < 0.5:
            warns.append(f"tópico da fonte pouco presente no texto: “{t}”")
    for e in metrics["edital"]:
        if has_terms(toks, key_terms(e["title"])) < 0.5:
            warns.append(f"item do edital {e['ref']} pouco presente no texto: “{e['title'][:90]}”")
    return errors, warns, stats


# ------------------------------------------------------------------------------------------------- volume
def validate_intro(path: Path, volume: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    meta, body, fm = parse_front_matter(path.read_text(encoding="utf-8").replace("\r\n", "\n"))
    errors += fm
    for k in ("volume", "titulo", "subtitulo", "status", "autor", "notas"):
        if k not in meta:
            errors.append(f"volume.md: front matter sem '{k}'")
    if meta.get("volume") != volume["id"]:
        errors.append(f"volume.md: volume deve ser {volume['id']!r}")
    if meta.get("status") not in AGENT_STATUS | REVIEW_STATUS:
        errors.append("volume.md: status inválido")
    if len(str(meta.get("subtitulo", ""))) > 160:
        errors.append("volume.md: subtitulo com mais de 160 caracteres")
    secs = [s.strip().lower() for s in H2.findall(body)]
    for need in ("apresentação", "o que você vai aprender"):
        if need not in secs:
            errors.append(f"volume.md: falta a seção '## {need.capitalize()}'")
    n = word_count(body)
    if not 150 <= n <= 450:
        errors.append(f"volume.md: {n} palavras (use 150 a 450)")
    low = body.lower()
    for bad in FORBIDDEN:
        if bad in low:
            errors.append(f"volume.md: expressão proibida “{bad}”")
    for m in sorted(set(x.group(0) for x in REMISSAO.finditer(body))):
        errors.append(f"volume.md: remissão ao material-base “{m}”")
    ne, nw = neutrality(body, "volume.md: ")
    errors += ne
    warns += nw
    return errors, warns


def fixacao_target(chapters: int) -> tuple[int, int]:
    lo = min(20, max(12, 3 * chapters))
    return lo, 20


def fixacao_range(volume: dict, no_banco: dict[str, int] | None) -> tuple[int, int, dict[str, int]]:
    """Faixa de questões do volume pela média do material-base (metrics/_fixacao.json, de material_fixacao_meta.py), limitada
    ao que o banco tem por capítulo. Sem a meta, cai na regra antiga (12 a 20)."""
    f = MATERIAL_DIR / "metrics" / "_fixacao.json"
    meta = json.loads(f.read_text(encoding="utf-8"))["volumes"].get(volume["id"]) if f.exists() else None
    if not meta:
        lo, hi = fixacao_target(volume["chapters"])
        return lo, hi, {}
    caps = {t: min(n, (no_banco or {}).get(t, n)) for t, n in meta["porCapitulo"].items()}
    lo = sum(caps.values())
    return lo, meta["meta"] + max(2, round(meta["meta"] * 0.1)), caps


def validate_fixacao(path: Path, volume: dict) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warns: list[str] = []
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"fixacao.json inválido: {e}"], warns, {}
    exp_f = QUESTIONS_DIR / (volume["id"].replace("/", "__") + ".json")
    bank = {q["id"]: q for q in json.loads(exp_f.read_text(encoding="utf-8"))["questoes"]} if exp_f.exists() else {}
    ref_f = exp_f.with_suffix(".ref.json")
    old = json.loads(ref_f.read_text(encoding="utf-8")) if ref_f.exists() else {}
    if not bank:
        warns.append("exportação das questões ausente: rode web/scripts/material-questoes.ts --volume " + volume["id"])
    if d.get("volume") != volume["id"]:
        errors.append(f"fixacao.json: volume deve ser {volume['id']!r}")
    if d.get("status") not in AGENT_STATUS | REVIEW_STATUS:
        errors.append("fixacao.json: status inválido")
    qs = d.get("questoes", []) or []
    ins = d.get("ineditas", []) or []
    total = len(qs) + len(ins)
    no_banco = json.loads(exp_f.read_text(encoding="utf-8")).get("noBanco") if exp_f.exists() else None
    lo, hi, _caps = fixacao_range(volume, no_banco)
    if d.get("bancoEsgotado"):
        # o seletor não achou mais candidata aproveitável para a meta (decisão do dono, 03/11/2026): aceita abaixo da meta
        lo = min(lo, total)
    if bank:
        # banco esgotado: aceita abaixo da meta quando já entraram todas as candidatas aproveitáveis (decisão do dono, 03/11/2026)
        descartadas = {(x.get("id") if isinstance(x, dict) else x) for x in (d.get("descartes") or [])}
        lo = min(lo, len([i for i in bank if i not in descartadas]))
    if not lo <= total <= hi:
        errors.append(f"fixacao.json: {total} questões (use {lo} a {hi}: média do material-base, metrics/_fixacao.json)")
    per: dict[str, int] = {t: 0 for t in volume["trechos"]}
    seen: set[str] = set()
    aocp = 0
    for q in qs:
        qid = q.get("id", "?")
        if qid in seen:
            errors.append(f"{qid}: repetida")
        seen.add(qid)
        b = bank.get(qid)
        if bank and not b:
            errors.append(f"{qid}: não está entre as questões aprovadas deste volume (exportação)")
            continue
        cap = q.get("capitulo")
        if cap not in per:
            errors.append(f"{qid}: capitulo {cap!r} não é trecho do volume")
        else:
            per[cap] += 1
        if b:
            if b["capitulo"] != cap:
                warns.append(f"{qid}: classificada no banco em {b['capitulo']}, você pôs em {cap}")
            if str(q.get("gabarito")) != str(b["gabarito"]):
                errors.append(f"{qid}: gabarito {q.get('gabarito')!r} diferente do banco ({b['gabarito']!r}); se o banco estiver errado, explique em 'notas'")
            if "AOCP" in str(b["banca"]).upper():
                aocp += 1
            if b.get("temFigura"):
                warns.append(f"{qid}: questão com figura (confira se o comentário não depende de vê-la)")
            if b["tipo"] == "MULTIPLA_ESCOLHA":
                letters = {a["letra"] for a in b["alternativas"]}
                alts = q.get("alternativas") or {}
                if set(alts) != letters:
                    errors.append(f"{qid}: comente cada alternativa ({', '.join(sorted(letters))}) em 'alternativas'")
        errors += check_comment(qid, q, old.get(qid, ""))
    for q in ins:
        qid = q.get("id", "?")
        if not re.match(r"^mentoria_mat_[a-z0-9_]+$", qid):
            errors.append(f"{qid}: id de inédita deve ser mentoria_mat_<disciplina>_<mNN>_<nn>")
        cap = q.get("capitulo")
        if cap in per:
            per[cap] += 1
        else:
            errors.append(f"{qid}: capitulo {cap!r} não é trecho do volume")
        tipo = q.get("tipo")
        if tipo == "MULTIPLA_ESCOLHA":
            txt = q.get("alternativas_texto") or {}
            if sorted(txt) not in (list("ABCD"), list("ABCDE")) or q.get("gabarito") not in txt:
                errors.append(f"{qid}: alternativas_texto A–E (ou A–D) e gabarito entre elas")
            if set(q.get("alternativas") or {}) != set(txt):
                errors.append(f"{qid}: comente cada alternativa em 'alternativas'")
        elif tipo == "CERTO_ERRADO":
            if q.get("gabarito") not in ("C", "E"):
                errors.append(f"{qid}: gabarito C ou E")
        else:
            errors.append(f"{qid}: tipo MULTIPLA_ESCOLHA ou CERTO_ERRADO")
        if word_count(q.get("enunciado", "")) < 12:
            errors.append(f"{qid}: enunciado curto demais")
        errors += check_comment(qid, q, "")
    # comentário de modelo (lote C1, 29/10/2026): o mesmo texto colado em várias questões não explica nenhuma
    starts: dict[str, list[str]] = {}
    sents: dict[str, set[str]] = {}
    for q in qs + ins:
        com = re.sub(r"\s+", " ", str(q.get("comentario", ""))).strip()
        starts.setdefault(" ".join(words(com)[:20]), []).append(q.get("id", "?"))
        for s in {x.strip() for x in com.split(".") if word_count(x) >= 8}:
            sents.setdefault(s, set()).add(q.get("id", "?"))
    for ids in starts.values():
        if len(ids) > 1:
            errors.append(f"fixacao.json: comentário igual em {len(ids)} questões ({', '.join(ids[:4])}...): comente cada questão")
    rep = [s for s, ids in sents.items() if len(ids) >= 3]
    if rep:
        warns.append(f"fixacao.json: {len(rep)} frase(s) repetida(s) em 3 ou mais comentários (ex.: “{rep[0][:80]}”)")
    for t, k in per.items():
        if k < 2:
            errors.append(f"fixacao.json: capítulo {t} com {k} questão(ões) (mínimo 2 por capítulo)")
    avail = len(bank)
    if ins and avail >= lo and len(ins) > 0.25 * total:
        errors.append(f"fixacao.json: {len(ins)} inéditas, mas há {avail} questões no banco; use as do banco (inéditas ≤ 25%)")
    aocp_avail = sum(1 for b in bank.values() if "AOCP" in str(b["banca"]).upper())
    if qs and aocp_avail >= total // 2 and aocp < total // 2:
        warns.append(f"fixacao.json: só {aocp} questões AOCP, havendo {aocp_avail} no banco (prefira AOCP)")
    return errors, warns, {"questoes": total, "ineditas": len(ins)}


def check_comment(qid: str, q: dict, old: str) -> list[str]:
    errs = []
    com = str(q.get("comentario", ""))
    n = word_count(com)
    if not 50 <= n <= 250:
        errs.append(f"{qid}: comentário com {n} palavras (use 50 a 250)")
    for k, v in (q.get("alternativas") or {}).items():
        if not 6 <= word_count(str(v)) <= 70:
            errs.append(f"{qid}: explicação da alternativa {k} com {word_count(str(v))} palavras (use 6 a 70)")
    if old and not q.get("id", "").startswith("mentoria_"):
        src = {tuple(words(old)[i:i + SHINGLE_N]) for i in range(max(0, len(words(old)) - SHINGLE_N + 1))}
        mine = words(com + " " + " ".join(str(v) for v in (q.get("alternativas") or {}).values()))
        if any(tuple(mine[i:i + SHINGLE_N]) in src for i in range(max(0, len(mine) - SHINGLE_N + 1))):
            errs.append(f"{qid}: comentário repete o comentário existente; escreva o seu")
    low = com.lower()
    for bad in ("estratégia", "tec concursos", "tecconcursos", "qconcursos", "gabarito oficial diz", "professor"):
        if bad in low:
            errs.append(f"{qid}: expressão proibida no comentário: “{bad}”")
    for m in sorted(set(x.group(0) for x in REMISSAO.finditer(com))):
        errs.append(f"{qid}: remissão ao material-base no comentário: “{m}”")
    allc = com + " " + " ".join(str(v) for v in (q.get("alternativas") or {}).values())
    errs += neutrality(allc, f"{qid}: ")[0]
    return errs


def validate_volume(vdir: Path) -> tuple[list[str], list[str], dict]:
    subject, m = vdir.parent.name, vdir.name
    volume = load_volume(f"{subject}/{m}")
    if not volume:
        return [f"{vdir}: volume inexistente em content/material/volumes"], [], {}
    errors: list[str] = []
    warns: list[str] = []
    stats: dict = {"volume": volume["id"], "chapters": {}}
    intro = vdir / "volume.md"
    if intro.exists():
        e, w = validate_intro(intro, volume)
        errors += e
        warns += w
    else:
        errors.append("falta volume.md")
    expected = {chapter_file(vdir, t).name for t in volume["trechos"]}
    for f in sorted(vdir.glob("*.md")):
        if f.name != "volume.md" and f.name not in expected and f.name != "REVISAO.md":
            errors.append(f"{f.name}: arquivo que não corresponde a nenhum capítulo do volume")
    for t in volume["trechos"]:
        f = chapter_file(vdir, t)
        if not f.exists():
            errors.append(f"falta o capítulo {f.name} ({t})")
            continue
        e, w, s = validate_chapter(f)
        errors += [f"{f.name}: {x}" for x in e]
        warns += [f"{f.name}: {x}" for x in w]
        stats["chapters"][t] = s
    fx = vdir / "fixacao.json"
    if fx.exists():
        e, w, s = validate_fixacao(fx, volume)
        errors += e
        warns += w
        stats["fixacao"] = s
    else:
        errors.append("falta fixacao.json")
    return errors, warns, stats


def status_table(wave: int | None) -> int:
    queue = json.loads((MATERIAL_DIR / "_queue.json").read_text(encoding="utf-8"))["queue"]
    counts: dict[str, int] = {}
    for r in queue:
        if wave and r["wave"] != wave:
            continue
        vdir = MATERIAL_DIR / r["volume"].split("/")[0] / r["volume"].split("/")[1]
        vol = load_volume(r["volume"])
        done = 0
        states = []
        for t in vol["trechos"]:
            f = chapter_file(vdir, t)
            if f.exists():
                meta, _, _ = parse_front_matter(f.read_text(encoding="utf-8").replace("\r\n", "\n"))
                states.append(meta.get("status", "?"))
                done += 1
        st = "PENDENTE" if not done else ("APROVADO" if states and all(s == "APROVADO" for s in states) else
                                          "PRONTO_PARA_REVISAO" if all(s in ("PRONTO_PARA_REVISAO", "APROVADO") for s in states) and done == len(vol["trechos"])
                                          else "EM_PRODUCAO")
        counts[st] = counts.get(st, 0) + 1
        print(f"{r['rank']:4d}  onda {r['wave']}  {r['volume']:40s} {done:2d}/{len(vol['trechos']):<2d}  {st}")
    print(" · ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 0


def write_report(path: Path, vdirs: list[Path]) -> None:
    """Relatório de lote em markdown (tabela por capítulo, avisos e Fixação), para o coordenador não montar à mão."""
    lines = [f"## Validação ({len(vdirs)} volumes)", ""]
    for vdir in vdirs:
        e, w, s = validate_volume(vdir)
        vid = s.get("volume", str(vdir))
        lines += [f"### {vid} — {len(e)} erro(s), {len(w)} aviso(s)", "",
                  "| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        metrics = load_metrics(vid.split("/")[0])
        for t, st in s.get("chapters", {}).items():
            mt = metrics.get(t, {})
            tg = mt.get("targets", {})
            imp = mt.get("importance", {})
            lines.append(f"| {t.split('/', 1)[1]} | {imp.get('tier', '?')} ({imp.get('score')}) | {st.get('words', '?')}/{tg.get('words', '?')} | "
                         f"{st.get('visuals', '?')}/{tg.get('visuals', '?')} | {st.get('callouts', '?')}/{tg.get('callouts', '?')} | "
                         f"{st.get('coverage', '—')} | {st.get('copied', 0)} | {st.get('sentenceWords', '?')} | {st.get('jargon', 0)} |")
        fx = vdir / "fixacao.json"
        if fx.exists():
            d = json.loads(fx.read_text(encoding="utf-8"))
            exp_f = QUESTIONS_DIR / (vid.replace("/", "__") + ".json")
            bank = {q["id"]: q for q in json.loads(exp_f.read_text(encoding="utf-8"))["questoes"]} if exp_f.exists() else {}
            qs = d.get("questoes", []) or []
            aocp = sum(1 for q in qs if "AOCP" in str(bank.get(q.get("id"), {}).get("banca", "")).upper())
            ined_bank = sum(1 for q in qs if str(q.get("id", "")).startswith("mentoria_"))
            lines += ["", f"Fixação: {len(qs) + len(d.get('ineditas') or [])} questões · AOCP {aocp} · inéditas do banco {ined_bank} · "
                          f"inéditas novas {len(d.get('ineditas') or [])}"]
        for x in e:
            lines.append(f"- ERRO {x}")
        for x in w:
            lines.append(f"- AVISO {x}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    marker = "## Validação ("
    keep = old.split(marker)[0].rstrip() + "\n\n" if old and marker in old else (old.rstrip() + "\n\n" if old else "")
    path.write_text(keep + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"relatório gravado em {path}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--wave", type=int)
    ap.add_argument("--json", action="store_true", help="imprime estatísticas em JSON (para o revisor)")
    ap.add_argument("--relatorio", metavar="ARQUIVO", help="grava (ou atualiza) a seção 'Validação' do relatório de lote em markdown")
    args = ap.parse_args()
    if args.status:
        return status_table(args.wave)
    if args.relatorio:
        dirs = [Path(p) for p in args.paths if Path(p).is_dir()]
        write_report(Path(args.relatorio), dirs)
        return 1 if any(validate_volume(d)[0] for d in dirs) else 0
    paths = [Path(p) for p in args.paths]
    if args.all:
        paths = sorted(p for p in MATERIAL_DIR.glob("*/m[0-9][0-9]") if p.is_dir())
    if not paths:
        ap.print_help()
        return 2
    bad = 0
    for p in paths:
        if p.is_dir():
            e, w, s = validate_volume(p)
        elif p.name == "fixacao.json":
            vol = load_volume(f"{p.parent.parent.name}/{p.parent.name}")
            e, w, s = validate_fixacao(p, vol) if vol else ([f"{p}: volume desconhecido"], [], {})
        else:
            e, w, s = validate_chapter(p)
        print(f"== {p}: {len(e)} erro(s), {len(w)} aviso(s)")
        for x in e:
            print("  ERRO ", x)
        for x in w:
            print("  AVISO", x)
        if args.json:
            print(json.dumps(s, ensure_ascii=False, indent=1))
        bad += bool(e)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
