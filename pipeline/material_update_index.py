"""Índice de atualização do material próprio: o que pode mudar (normas, jurisprudência, pontos sensíveis) e onde está.

Gera, em content/material/atualizacao/:
  indice.json   por volume e capítulo: normas (lei + artigo + impressão digital sha256 do texto vigente do artigo no cache de
                pipeline/leis.py), jurisprudência (tribunal, tipo, número), pontos sensíveis (pendências, redação nova) e a
                volatilidade da disciplina; mais o resumo por norma (artigos citados e em que volumes);
  INDICE.md     o mesmo, para leitura, por disciplina;
  datas.json    data da última alteração de cada volume ("Material atualizado em", na última página do PDF): a mais recente
                registrada no REVISAO.md do volume (cada revisão, correção ou atualização acrescenta uma seção datada).

O agente mensal (pipeline/briefs/atualizacao.md) usa este índice com pipeline/material_watch.py, que só aponta o que mudou.
Disciplinas de volatilidade BAIXA (exatas, línguas, Biologia, História) entram só com a data: conhecimento fixado.

Uso: python pipeline/material_update_index.py [--sem-hash]   (--sem-hash: não lê o cache das leis)
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_citations import FORM1, FORM2, law_key  # noqa: E402
from leis import LEIS, LEIS_DIR, load  # noqa: E402
from validate_material import MATERIAL_DIR, parse_front_matter  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = MATERIAL_DIR / "atualizacao"
ALTA = {"direito-administrativo", "direito-constitucional", "direito-penal", "direito-penal-militar", "direito-processual-penal",
        "direito-processual-penal-militar", "direitos-humanos", "legislacoes-pe", "legislacao-pcpe", "legislacao-penal-especial"}
MEDIA = {"informatica", "administracao", "atualidades", "contabilidade-geral"}
TRIB = r"(STF|STJ|STM|TST|TSE|TCU|TJPE|TJM\w*)"
JURIS = [
    re.compile(r"S[úu]mula\s+(Vinculante\s+)?n?[º°o.]*\s*(\d+)\s+(?:do|da)\s+" + TRIB),
    re.compile(TRIB + r",?\s+S[úu]mula\s+(Vinculante\s+)?n?[º°o.]*\s*(\d+)"),
    re.compile(r"\b(Tema)\s+(?:n[º°o.]*\s*)?(\d{1,5})\b"),
    re.compile(r"\b(ADI|ADPF|ADC|ADO|RE|REsp|HC|RHC|MS|Rcl|IRDR|ARE)\s+(?:n[º°o.]*\s*)?(\d[\d.]*)"),
]
SENSIVEL = re.compile(
    r"[^.\n]*\b(?:pendentes?|em julgamento|aguarda(?:m)? julgamento|ainda n[ãa]o (?:foi )?julgad\w*|liminar(?:mente)?|recentemente|nova reda[çc][ãa]o|"
    r"reda[çc][ãa]o dada pela|altera(?:da|do|ções) (?:pela|recentes)|Lei (?:Complementar )?(?:n[º°o.]*\s*)?[\d.]+/20(?:2[3-9]|3\d)|"
    r"LC (?:n[º°o.]*\s*)?[\d.]+/20(?:2[3-9]|3\d)|EC (?:n[º°o.]*\s*)?\d+/20(?:2[3-9]|3\d)|vacatio|entra(?:rá)? em vigor)\b[^.\n]*", re.I)
DATE = re.compile(r"(20\d\d-\d\d-\d\d)")


def volatility(subject: str) -> str:
    return "ALTA" if subject in ALTA else "MEDIA" if subject in MEDIA else "BAIXA"


_ART_CACHE: dict[tuple[str, str], str | None] = {}


def article_text(key: str, num: str) -> str | None:
    """Texto vigente do artigo (até o próximo 'Art.'), sem a redação revogada; None se a norma não está no cache."""
    k = (key, num)
    if k in _ART_CACHE:
        return _ART_CACHE[k]
    if not (LEIS_DIR / f"{key}.clean.txt").exists() and not (LEIS_DIR / f"{key}.htm").exists():
        _ART_CACHE[k] = None
        return None
    text = load(key)
    cut = text.find("ATO DAS DISPOSIÇÕES CONSTITUCIONAIS TRANSITÓRIAS")
    if cut > 0:
        text = text[:cut]
    vig = re.sub(r"\[REVOGADO:[^\]]*\]", " ", text)
    pat = re.compile(r"Art\.?\s*" + re.escape(num) + r"(º|o|°)?(?![\d])(?!-[A-Za-z]{1,2}\b)[-–.\s]")
    hits = [m.start() for m in pat.finditer(vig)]
    if not hits:
        _ART_CACHE[k] = ""
        return ""
    start = hits[-1]
    nxt = re.search(r"\sArt\.?\s*\d", vig[start + 5:])
    body = vig[start: start + 5 + nxt.start()] if nxt else vig[start: start + 4000]
    _ART_CACHE[k] = re.sub(r"\s+", " ", body).strip()
    return _ART_CACHE[k]


def sha(s: str | None) -> str | None:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16] if s else None


def chapter_items(text: str, with_hash: bool) -> dict:
    meta, body, _ = parse_front_matter(text)
    normas: dict[tuple[str, str], dict] = {}
    lei_titles = {m.group(1) for m in re.finditer(r"^>\s*\[!lei\]\s*(.+)$", body, re.M)}
    for rx, law_g, art_g in ((FORM1, 1, 2), (FORM2, 2, 1)):
        for m in rx.finditer(body):
            key = law_key(m.group(law_g))
            if not key:
                continue
            num = m.group(art_g)
            origem = "lei" if any(m.group(0) in t or (key and num in t) for t in lei_titles) else "texto"
            item = normas.setdefault((key, num), {"lei": key, "art": num, "origem": origem})
            if origem == "lei":
                item["origem"] = "lei"
    for it in normas.values():
        if with_hash:
            t = article_text(it["lei"], it["art"])
            it["cache"] = t is not None
            it["sha"] = sha(t)
            if t == "":
                it["obs"] = "artigo não encontrado no texto vigente"
    juris = {}
    for rx in JURIS:
        for m in rx.finditer(body):
            g = [x for x in m.groups() if x]
            label = re.sub(r"\s+", " ", m.group(0)).strip()
            juris.setdefault(label, {"citacao": label, "grupos": g})
    sens = []
    for m in SENSIVEL.finditer(body):
        s = m.group(0).strip()
        if 25 <= len(s) <= 400 and s not in sens:
            sens.append(s)
    return {"titulo": meta.get("titulo", ""), "normas": sorted(normas.values(), key=lambda x: (x["lei"], x["art"])),
            "jurisprudencia": [v["citacao"] for v in juris.values()], "sensiveis": sens[:12]}


def last_change(vdir: Path) -> str | None:
    rev = vdir / "REVISAO.md"
    dates = DATE.findall(rev.read_text(encoding="utf-8")) if rev.exists() else []
    return max(dates) if dates else None


def build(with_hash: bool = True) -> tuple[dict, dict]:
    vols, datas = {}, {}
    by_law: dict[str, dict] = defaultdict(lambda: {"artigos": defaultdict(set)})
    for f in sorted((MATERIAL_DIR / "volumes").glob("*.json")):
        for v in json.loads(f.read_text(encoding="utf-8"))["volumes"]:
            vdir = MATERIAL_DIR / v["id"]
            if not vdir.is_dir():
                continue
            subj = v["id"].split("/")[0]
            vol = volatility(subj)
            date = last_change(vdir)
            if date:
                datas[v["id"]] = date
            entry = {"titulo": v["title"], "onda": v.get("wave"), "volatilidade": vol, "atualizadoEm": date, "capitulos": {}}
            if vol != "BAIXA":
                for t in v["trechos"]:
                    aula, seg = t.split("/")[1:]
                    p = vdir / f"{aula}-{seg}.md"
                    if not p.exists():
                        continue
                    it = chapter_items(p.read_text(encoding="utf-8"), with_hash)
                    it["arquivo"] = p.relative_to(MATERIAL_DIR.parent.parent).as_posix()
                    entry["capitulos"][t] = it
                    for n in it["normas"]:
                        by_law[n["lei"]]["artigos"][n["art"]].add(v["id"])
            vols[v["id"]] = entry
    normas = {k: {"descricao": LEIS.get(k, ("", k))[1], "url": LEIS.get(k, ("",))[0],
                  "artigos": {a: sorted(vs) for a, vs in sorted(d["artigos"].items(), key=lambda x: (len(x[0]), x[0]))}}
              for k, d in sorted(by_law.items())}
    idx = {"versao": 1, "geradoEm": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
           "_comentario": "Gerado por pipeline/material_update_index.py. 'sha' = impressão digital do texto vigente do artigo no cache das leis.",
           "volumes": vols, "normas": normas}
    return idx, datas


def write_md(idx: dict) -> str:
    lines = ["# Índice de atualização do material próprio", "",
             f"Gerado em {idx['geradoEm'][:10]} por `pipeline/material_update_index.py`. Use com `pipeline/material_watch.py` "
             "e o briefing `pipeline/briefs/atualizacao.md`.", "",
             "Volatilidade ALTA = jurídicas e legislações (catalogadas item a item); MÉDIA = Informática, Administração, Atualidades, "
             "Contabilidade; BAIXA = conhecimento fixado (só a data).", ""]
    by_subj: dict[str, list] = defaultdict(list)
    for vid, v in idx["volumes"].items():
        by_subj[vid.split("/")[0]].append((vid, v))
    for subj in sorted(by_subj):
        vols = by_subj[subj]
        lines += [f"## {subj} ({vols[0][1]['volatilidade']})", ""]
        for vid, v in vols:
            lines.append(f"### {vid} · {v['titulo']} · atualizado em {v['atualizadoEm'] or '—'}")
            for t, c in v["capitulos"].items():
                norms = ", ".join(f"{n['lei']} art. {n['art']}{' [quadro]' if n['origem'] == 'lei' else ''}" for n in c["normas"])
                parts = [f"- **{t}** {c['titulo']}"]
                if norms:
                    parts.append(f"  - Normas: {norms}")
                if c["jurisprudencia"]:
                    parts.append(f"  - Jurisprudência: {'; '.join(c['jurisprudencia'])}")
                for s in c["sensiveis"]:
                    parts.append(f"  - Sensível: {s[:220]}")
                if len(parts) > 1:
                    lines += parts
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sem-hash", action="store_true")
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    idx, datas = build(not args.sem_hash)
    (OUT_DIR / "indice.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (OUT_DIR / "INDICE.md").write_text(write_md(idx), encoding="utf-8")
    (OUT_DIR / "datas.json").write_text(json.dumps(dict(sorted(datas.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_norm = sum(len(c["normas"]) for v in idx["volumes"].values() for c in v["capitulos"].values())
    n_jur = sum(len(c["jurisprudencia"]) for v in idx["volumes"].values() for c in v["capitulos"].values())
    n_sen = sum(len(c["sensiveis"]) for v in idx["volumes"].values() for c in v["capitulos"].values())
    print(f"{len(idx['volumes'])} volumes · {len(idx['normas'])} normas · {n_norm} citações de artigo · {n_jur} de jurisprudência · "
          f"{n_sen} pontos sensíveis · {len(datas)} datas -> {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
