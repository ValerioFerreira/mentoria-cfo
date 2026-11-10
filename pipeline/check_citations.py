"""Confere as citações de artigos do material próprio contra as leis em cache (pipeline/leis.py).

Acusa artigo que NÃO EXISTE na norma citada (ex.: "CPPM, art. 799") e lista, para leitura rápida, o início de cada artigo citado.
Não prova que o conteúdo atribuído ao artigo está certo: isso continua sendo leitura do autor e do revisor. Ela fica muito
mais rápida com a lista de "artigo → primeiras palavras".

Formas reconhecidas: "CF, art. 5º", "art. 9º do CPM", "Lei 12.016/2009, art. 23", "art. 23 da Lei nº 12.016/2009",
"LC 470/2021", "Decreto 50.014/2020". Citação solta "(art. 81)" usa a norma mais citada no arquivo.

Uso:  python pipeline/check_citations.py content/material/<disc>/mNN [--lista]   (pasta ou arquivos .md / fixacao.json)
      Código de saída 1 quando há artigo inexistente.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from leis import LEIS, LEIS_DIR, load  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ALIASES = {
    "cf": "cf", "cf/88": "cf", "constituição": "cf", "constituição federal": "cf", "carta magna": "cf",
    "cpm": "cpm", "código penal militar": "cpm", "cppm": "cppm", "código de processo penal militar": "cppm",
    "cp": "cp", "código penal": "cp", "cpp": "cpp", "código de processo penal": "cpp", "eca": "l8069", "ctb": "l9503",
}
NUM2KEY = {}
for _k, (_url, _desc) in LEIS.items():
    m = re.search(r"(\d[\d.]*)/(\d{4})", _desc)
    if m:
        NUM2KEY[(m.group(1).replace(".", ""), m.group(2))] = _k

LAW = (r"(CF/88|CF|Constituição Federal|Constituição|CPPM|CPM|CPP|CP|ECA|CTB|Código de Processo Penal Militar|Código Penal Militar|"
       r"Código de Processo Penal|Código Penal|(?:Lei|LC|Decreto|Decreto-Lei)(?: Complementar)?(?: Estadual| Federal)?(?: n[º°o.]*)? ?[\d.]+/\d{4})")
ART = r"arts?\.\s?(\d+(?:-[A-Z]{1,2})?)"
FORM1 = re.compile(LAW + r",?\s*" + ART)  # "CF, art. 5º"
FORM2 = re.compile(ART + r"[º°o]?(?:[^.;()\n]{0,40}?)\s(?:da|do)\s" + LAW)  # "art. 9º, II, do CPM"
BARE = re.compile(r"\(\s*" + ART + r"[º°o]?")


def law_key(ref: str) -> str | None:
    r = ref.strip().lower()
    if r in ALIASES:
        return ALIASES[r]
    m = re.search(r"([\d.]+)/(\d{4})", ref)
    if m:
        return NUM2KEY.get((m.group(1).replace(".", ""), m.group(2)))
    return None


def article_start(text: str, num: str) -> str | None:
    # o ADCT reinicia a numeração: na CF, só o corpo permanente conta
    cut = text.find("ATO DAS DISPOSIÇÕES CONSTITUCIONAIS TRANSITÓRIAS")
    if cut > 0:
        text = text[:cut]
    # "Art. 2º" não pode casar com "Art. 2º-C" (artigo acrescentado)
    pat = re.compile(r"Art\.?\s*" + re.escape(num) + r"(º|o|°)?(?![\d])(?!-[A-Za-z]{1,2}\b)[-–.\s]")
    vigente = re.sub(r"\[REVOGADO:[^\]]*\]", " ", text)
    hits = [m.start() for m in pat.finditer(vigente)]
    if hits:
        h = hits[-1]  # o texto compilado traz a redação revogada antes da vigente
        return re.sub(r"\s+", " ", vigente[h: h + 160]).strip()
    # artigo inteiro revogado (a marcação pode vir partida: "[REVOGADO: Art.] [REVOGADO: 78.")
    unwrapped = re.sub(r"\[REVOGADO:\s*([^\]]*)\]", r"\1", text)
    hits = [m.start() for m in pat.finditer(unwrapped)]
    if hits:
        return "REVOGADO: " + re.sub(r"\s+", " ", unwrapped[hits[-1]: hits[-1] + 140]).strip()
    return None


def texts(path: Path) -> list[tuple[str, str]]:
    if path.is_dir():
        out = []
        for f in sorted(path.iterdir()):
            if f.suffix == ".md" and f.name != "REVISAO.md" or f.name == "fixacao.json":
                out += texts(f)
        return out
    if path.name == "fixacao.json":
        d = json.loads(path.read_text(encoding="utf-8"))
        blob = []
        for q in (d.get("questoes") or []) + (d.get("ineditas") or []):
            blob.append(str(q.get("comentario", "")))
            blob += [str(v) for v in (q.get("alternativas") or {}).values()]
        return [(str(path), "\n".join(blob))]
    return [(str(path), path.read_text(encoding="utf-8"))]


def check(name: str, text: str, show: bool) -> int:
    cites: list[tuple[str, str]] = []
    for m in FORM1.finditer(text):
        cites.append((m.group(1), m.group(2)))
    for m in FORM2.finditer(text):
        cites.append((m.group(2), m.group(1)))
    keys = [law_key(l) for l, _ in cites]
    default = collections.Counter(k for k in keys if k).most_common(1)
    default_key = default[0][0] if default else None
    seen_spans = {(m.start(), m.end()) for m in FORM1.finditer(text)} | {(m.start(), m.end()) for m in FORM2.finditer(text)}
    for m in BARE.finditer(text):
        if default_key and not any(a <= m.start() < b for a, b in seen_spans):
            cites.append(("(norma mais citada)", m.group(1)))
    bad = 0
    unknown = collections.Counter()
    rows = []
    for law, num in dict.fromkeys(cites):
        key = law_key(law) if law != "(norma mais citada)" else default_key
        if not key:
            unknown[law] += 1
            continue
        if not (LEIS_DIR / f"{key}.clean.txt").exists() and not (LEIS_DIR / f"{key}.htm").exists():
            unknown[f"{law} (não está no cache)"] += 1
            continue
        start = article_start(load(key), num)
        if start is None:
            bad += 1
            rows.append(f"  INEXISTENTE  {law} art. {num}  (procurado em '{key}')")
        elif start.startswith("REVOGADO"):
            rows.append(f"  REVOGADO     {law} art. {num}: confira se o texto o trata como revogado")
        elif show:
            rows.append(f"  ok  {key} art. {num}: {start[:120]}")
    print(f"== {name}: {len(set(cites))} citações, {bad} inexistente(s)" + (f", sem norma reconhecida: {dict(unknown)}" if unknown else ""))
    for r in rows:
        print(r)
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--lista", action="store_true", help="mostra o início de cada artigo citado (para conferência rápida)")
    args = ap.parse_args()
    bad = 0
    for p in args.paths:
        for name, text in texts(Path(p)):
            bad += check(name, text, args.lista)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
