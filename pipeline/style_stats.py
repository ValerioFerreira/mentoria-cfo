"""Etapa M2b — Perfil quantitativo do estilo AOCP (comparado às demais bancas) a partir do corpus local.

Saída versionável (somente números e padrões, sem texto de questões): content/style/aocp-profile.json
Uso:  python pipeline/style_stats.py
"""
from __future__ import annotations

import collections
import json
import os
import re
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, CONTENT_DIR  # noqa: E402

ROMAN = re.compile(r"(?m)^\s*(I{1,3}|IV|V)\s*[.\-–):]\s+\S")
COMBO = re.compile(r"\b(apenas|somente|s[óo])\s+(I{1,3}|IV)\b|\bI{1,3}\s*(,|e)\s*(I{1,3}|IV)\b", re.IGNORECASE)
NEG = re.compile(r"\b(incorret[ao]s?|n[ãa]o (?:\w+ ){0,3}(?:correta|verdadeira|adequada)|exceto|falsa|inadequad[ao]|errad[ao])\b", re.IGNORECASE)
TEXTO = re.compile(r"\b(de acordo com o texto|segundo o texto|conforme o texto|no texto|texto[- ]base|considerando o texto)\b", re.IGNORECASE)
LACUNA = re.compile(r"lacuna|_{3,}|preencha", re.IGNORECASE)
LEI = re.compile(r"\b(art\.|artigo|lei n|constitui[çc][ãa]o|segundo a lei|de acordo com a lei|c[óo]digo|decreto)\b", re.IGNORECASE)
CALC = re.compile(r"\d+[,.]?\d*\s*(mol|g\b|kg|m/s|n\b|j\b|w\b|%|v\b|a\b|l\b|ml|°c|k\b)|calcul|determine|quantos|qual o valor", re.IGNORECASE)


def words(s: str) -> int:
    return len(re.findall(r"\w+", s))


def quant(xs: list[float]) -> dict:
    if not xs:
        return {}
    xs = sorted(xs)
    q = lambda p: xs[min(len(xs) - 1, int(p * len(xs)))]  # noqa: E731
    return {"p25": q(0.25), "median": q(0.5), "p75": q(0.75), "mean": round(st.mean(xs), 1)}


def opening(stmt: str, n: int = 4) -> str:
    # última frase do enunciado costuma conter o comando ("Assinale a alternativa que…")
    sents = re.split(r"(?<=[.:?!])\s+", stmt.strip())
    last = sents[-1] if sents else stmt
    w = re.findall(r"\w+", last.lower())
    return " ".join(w[:n])


def profile(rows: list[dict]) -> dict:
    mc = [r for r in rows if r["kind"] in ("mc5", "mc4")]
    n = len(rows) or 1
    letters = collections.Counter(r["answer"] for r in mc if r["answer"] in list("ABCDE"))
    lens_stmt = [words(r["statement"]) for r in rows]
    lens_alt = [st.mean([words(v) for v in r["options"].values()]) for r in mc if r["options"]]
    longest = 0
    sorted_num = 0
    tested = 0
    for r in mc:
        if not r["answer"] or r["answer"] not in r["options" if False else "answer"] and False:
            pass
        opts = {k.upper(): v for k, v in r["options"].items()}
        if r["answer"] in opts:
            tested += 1
            if max(opts, key=lambda k: len(opts[k])) == r["answer"]:
                longest += 1
    last_cmd = collections.Counter(opening(r["statement"]) for r in mc)
    roman = sum(1 for r in mc if ROMAN.search(r["statement"]))
    combo_alts = sum(1 for r in mc if sum(1 for v in r["options"].values() if COMBO.search(v)) >= 3)
    return {
        "n": len(rows),
        "kinds": dict(collections.Counter(r["kind"] for r in rows)),
        "pctAssertivasRomanas": round(100 * roman / max(len(mc), 1), 1),
        "pctAlternativasCombinadas": round(100 * combo_alts / max(len(mc), 1), 1),
        "pctNegativa": round(100 * sum(1 for r in rows if NEG.search(r["statement"][-250:])) / n, 1),
        "pctTextoBase": round(100 * sum(1 for r in rows if TEXTO.search(r["statement"])) / n, 1),
        "pctLacuna": round(100 * sum(1 for r in rows if LACUNA.search(r["statement"])) / n, 1),
        "pctLeiSeca": round(100 * sum(1 for r in rows if LEI.search(r["statement"])) / n, 1),
        "pctCalculo": round(100 * sum(1 for r in rows if CALC.search(r["statement"])) / n, 1),
        "wordsEnunciado": quant(lens_stmt),
        "wordsAlternativa": quant(lens_alt),
        "gabaritoLetras": {k: round(100 * v / max(sum(letters.values()), 1), 1) for k, v in sorted(letters.items())},
        "pctGabaritoMaisLonga": round(100 * longest / max(tested, 1), 1),
        "comandosFrequentes": [{"comando": k, "n": v} for k, v in last_cmd.most_common(12) if k],
        "anos": dict(sorted(collections.Counter(r["ano"] for r in rows if r.get("ano")).items())),
    }


def main() -> int:
    rows = [json.loads(l) for l in (CACHE_DIR / "corpus" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    aocp = [r for r in rows if r["banca"] == "AOCP"]
    others = [r for r in rows if r["banca"] != "AOCP"]
    by_subject = collections.defaultdict(list)
    for r in aocp:
        by_subject[r["subject"]].append(r)
    out = {
        "_comment": "Perfil numérico do estilo AOCP extraído do material (sem texto de questões). Gerado por pipeline/style_stats.py.",
        "aocp": profile(aocp),
        "outrasBancas": profile(others),
        "aocpPorDisciplina": {k: profile(v) for k, v in sorted(by_subject.items()) if len(v) >= 10},
        "aocpPorDisciplinaN": {k: len(v) for k, v in sorted(by_subject.items())},
        "aocpOrgaos": [{"orgao": k, "n": v} for k, v in collections.Counter(r["orgao"].split(" / ")[0][:40] for r in aocp).most_common(25)],
    }
    dest = CONTENT_DIR / "style"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "aocp-profile.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    a, o = out["aocp"], out["outrasBancas"]
    print(f"AOCP n={a['n']} | outras n={o['n']}")
    for k in ("kinds", "pctAssertivasRomanas", "pctAlternativasCombinadas", "pctNegativa", "pctTextoBase", "pctLacuna", "pctLeiSeca", "pctCalculo", "pctGabaritoMaisLonga", "gabaritoLetras", "wordsEnunciado", "wordsAlternativa"):
        print(f"  {k:28s} AOCP={a[k]}   outras={o[k]}")
    print("comandos AOCP:", [(c['comando'], c['n']) for c in a['comandosFrequentes'][:8]])
    print("por disciplina:", out["aocpPorDisciplinaN"])
    print("órgãos:", [(x['orgao'], x['n']) for x in out['aocpOrgaos'][:12]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
