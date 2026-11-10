"""Nota automática de COBERTURA dos resumos: que fração dos termos específicos do texto-fonte do trecho aparece no resumo.

É uma triagem, não um juiz: mede OMISSÃO (assunto que a fonte trata e o resumo não menciona), não acerto (um conceito errado
passa). Serve para apontar onde um agente ou uma pessoa deve ler primeiro. Como a nota depende da disciplina (Inglês e Espanhol
têm exemplos em outra língua, Matemática tem fórmulas), o veredito combina a posição entre os resumos DA MESMA DISCIPLINA
(com menos de 20 de referência vale o conjunto de todas) e uma nota absoluta (não vale em Inglês e Espanhol):
  REFAÇÃO  = cobertura baixa (10% piores da disciplina ou nota < 0,40) E analítico com menos de 30% do alvo de palavras
  REVISAR  = cobertura baixa
  ATENÇÃO  = 25% piores da disciplina ou nota < 0,45
  OK       = o resto
Termo específico = palavra (ou número) rara na disciplina e repetida (2+ vezes) no trecho; peso = raridade × repetição. O resumo "cobre" um
termo se o contém, inclusive no singular/plural (mesmos 6 primeiros caracteres).

Uso:  python pipeline/summary_coverage.py [--subject <disc>] [--top N] [--csv caminho] [--md caminho]
        (sem args: pontua todos os resumos de content/summaries e imprime os piores de cada disciplina)
      Usado também por validate_summaries.py (aviso por trecho). Só leitura, exceto --csv/--md.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import math
import os
import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SUMMARIES_DIR = CONTENT_DIR / "summaries"
MIN_SALIENT = 15  # trecho com menos termos específicos que isso não é pontuado (texto curto demais para medir)
STOP = set(
    """para como mais pelo pela pelos pelas entre sobre quando onde qual quais essa esse essas esses esta este estas estes
isso isto aquele aquela cujo cuja podem pode deve devem sendo sera serao foram seria cada outro outra outros outras tambem apenas
assim ainda mesmo mesma desde ate sem sob apos antes depois porque porem contudo todavia entao logo portanto""".split()
)
STEM = 6


def _ascii(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def tokens(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", _ascii(s))


@lru_cache(maxsize=None)
def _doc_freq(subject: str) -> tuple[collections.Counter, int]:
    """Em quantas páginas da disciplina cada termo aparece (para saber o que é específico do trecho)."""
    df: collections.Counter = collections.Counter()
    n = 0
    for aula, key in aula_key_map().items():
        if aula.split("/")[0] != subject:
            continue
        for p in load_pages(key)["pages"]:
            n += 1
            df.update(set(tokens(p["text"])))
    return df, n


def salient_terms(subject: str, aula: str, start: int, end: int) -> dict[str, float]:
    """Termos específicos do trecho (páginas start..end) com seus pesos; vazio se a aula não tem texto-fonte em cache."""
    key = aula_key_map().get(aula)
    if not key:
        return {}
    df, n = _doc_freq(subject)
    count: collections.Counter = collections.Counter()
    for p in load_pages(key)["pages"]:
        if start <= p["n"] <= end:
            count.update(tokens(p["text"]))
    out: dict[str, float] = {}
    for w, c in count.items():
        if w in STOP or (len(w) < 4 and not w.isdigit()) or (w.isdigit() and len(w) < 2):
            continue
        idf = math.log((n + 1) / (df[w] + 1))
        # só conta o que o trecho repete: palavra solta de um exemplo ou enunciado (nome próprio, número de conta) é ruído
        if idf > 2.2 and c >= 2:
            out[w] = idf * (1 + math.log(c))
    return out


def coverage_of(text: str, salient: dict[str, float]) -> tuple[float, list[str]]:
    """(fração do peso coberta, termos mais pesados que faltam)."""
    have = set(tokens(text))
    stems = {w[:STEM] for w in have}
    total = sum(salient.values())
    if not total:
        return 1.0, []
    got = 0.0
    missing: list[tuple[float, str]] = []
    for w, v in salient.items():
        if w in have or w[:STEM] in stems:
            got += v
        else:
            missing.append((v, w))
    missing.sort(reverse=True)
    return got / total, [w for _, w in missing]


def segment_score(seg: dict, ref: dict) -> dict | None:
    """Nota de um trecho (`seg` do arquivo de resumo, `ref` de content/segments). None se não dá para medir."""
    aula = ref["aula"]
    subject = aula.split("/")[0]
    sal = salient_terms(subject, aula, ref["startPage"], ref["endPage"])
    if len(sal) < MIN_SALIENT:
        return None
    score, missing = coverage_of(seg.get("analytic", "") + "\n" + "\n".join(seg.get("synthetic", [])), sal)
    return {"score": score, "salient": len(sal), "missing": missing}


def _percentile(sorted_vals: list[float], v: float) -> float:
    """Fração dos valores estritamente menores que v (0 = o pior da lista)."""
    if not sorted_vals:
        return 1.0
    return sum(1 for x in sorted_vals if x < v) / len(sorted_vals)


@lru_cache(maxsize=None)
def baseline_all() -> list[float]:
    vals: list[float] = []
    for d in sorted(p for p in SUMMARIES_DIR.iterdir() if p.is_dir()):
        vals += baseline(d.name)
    return sorted(vals)


ALGORITHM = 2  # mude ao alterar a escolha dos termos específicos ou a nota (invalida o cache de referência)
CACHE_DIR = CONTENT_DIR.parent / "pipeline" / ".cache"


@lru_cache(maxsize=None)
def baseline(subject: str) -> list[float]:
    """Notas de todos os resumos já existentes da disciplina (referência para comparar um resumo novo). Cache em disco, invalidado
    quando os arquivos de resumo da disciplina mudam."""
    files = sorted((SUMMARIES_DIR / subject).glob("*.json"))
    sig = [ALGORITHM] + [[f.name, f.stat().st_mtime_ns, f.stat().st_size] for f in files]
    cache = CACHE_DIR / f"cov_baseline_{subject}.json"
    try:
        saved = json.loads(cache.read_text(encoding="utf-8"))
        if saved.get("sig") == sig:
            return saved["vals"]
    except (OSError, ValueError):
        pass
    segs = {s["id"]: s for s in json.loads((CONTENT_DIR / "segments" / f"{subject}.json").read_text(encoding="utf-8"))["segments"]}
    vals: list[float] = []
    for f in files:
        for s in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
            ref = segs.get(s["id"])
            if ref and s.get("analytic") and s.get("synthetic"):
                r = segment_score(s, ref)
                if r:
                    vals.append(r["score"])
    vals.sort()
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps({"sig": sig, "vals": vals}), encoding="utf-8")
    except OSError:
        pass
    return vals


# Inglês e Espanhol: a fonte traz muitos exemplos na língua estudada, que o resumo traduz ou resume; a nota absoluta é baixa por
# construção e só vale a posição dentro da disciplina.
RELATIVE_ONLY = {"lingua-inglesa", "lingua-espanhola"}
ABS_REVIEW = 0.40  # abaixo disto, cobertura baixa em qualquer disciplina (exceto RELATIVE_ONLY)
ABS_ATTENTION = 0.45


def verdict(subject: str, score: float, pct: float, size_ratio: float | None) -> str:
    """Triagem. A posição na disciplina sozinha esconde um lote inteiro fraco (todos baixos = nenhum é "o pior"): por isso há
    também a nota absoluta, calibrada nos resumos que os avaliadores mandaram refazer/complementar (0,17 a 0,39) × os aprovados (0,50 a 0,67)."""
    absolute = subject not in RELATIVE_ONLY
    low = pct <= 0.10 or (absolute and score < ABS_REVIEW) or score < 0.15
    if low:
        return "REFAÇÃO" if size_ratio is not None and size_ratio < 0.30 else "REVISAR"
    if pct <= 0.25 or (absolute and score < ABS_ATTENTION):
        return "ATENÇÃO"
    return "OK"


def rate(seg: dict, ref: dict, size_ratio: float | None = None) -> dict | None:
    """Nota + posição na disciplina + veredito de triagem (None se não dá para medir)."""
    r = segment_score(seg, ref)
    if not r:
        return None
    subject = ref["aula"].split("/")[0]
    base = baseline(subject)
    # comparação com a distribuição da disciplina; com menos de 20 resumos de referência usa-se o conjunto de todas as disciplinas
    scope = subject
    if len(base) < 20:
        base, scope = baseline_all(), "geral"
    pct = _percentile(base, r["score"])
    return {**r, "pct": pct, "scope": scope, "verdict": verdict(subject, r["score"], pct, size_ratio)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject")
    ap.add_argument("--top", type=int, default=8, help="quantos mostrar por disciplina (os piores)")
    ap.add_argument("--csv")
    ap.add_argument("--md")
    args = ap.parse_args()

    colab = CONTENT_DIR.parent / "resumos-colaboradores" / "indice.json"
    index = {r["trecho"]: r for r in json.loads(colab.read_text(encoding="utf-8"))["rows"]} if colab.exists() else {}
    rows: list[dict] = []
    for sdir in sorted(p for p in SUMMARIES_DIR.iterdir() if p.is_dir()):
        subject = sdir.name
        if args.subject and subject != args.subject:
            continue
        segs = {s["id"]: s for s in json.loads((CONTENT_DIR / "segments" / f"{subject}.json").read_text(encoding="utf-8"))["segments"]}
        for f in sorted(sdir.glob("*.json")):
            for s in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
                ref = segs.get(s["id"])
                if not ref or not (s.get("analytic") and s.get("synthetic")):
                    continue
                idx = index.get(s["id"], {})
                words = len(re.findall(r"\w+", re.sub(r"[|*#>`_-]+", " ", s["analytic"])))
                ratio = words / idx["targetWords"] if idx.get("targetWords") else None
                r = rate(s, ref, ratio)
                if not r:
                    continue
                rows.append(
                    {
                        "id": idx.get("id", ""), "trecho": s["id"], "disciplina": subject, "agente": s.get("agent", ""),
                        "cobertura": round(r["score"], 3), "posicao": round(r["pct"], 3), "palavras": words,
                        "razao_do_alvo": round(ratio, 2) if ratio is not None else "", "veredito": r["verdict"],
                        "faltam": " ".join(r["missing"][:12]),
                    }
                )
    by = collections.defaultdict(list)
    for r in rows:
        by[r["disciplina"]].append(r)
    print(f"{len(rows)} resumos pontuados\n")
    counts = collections.Counter(r["veredito"] for r in rows)
    print("veredito:", dict(counts), "\n")
    for subject, rs in sorted(by.items()):
        rs.sort(key=lambda r: r["cobertura"])
        c = collections.Counter(r["veredito"] for r in rs)
        med = rs[len(rs) // 2]["cobertura"]
        print(f"{subject} — {len(rs)} resumos, mediana {med:.2f}; REFAÇÃO {c['REFAÇÃO']}, REVISAR {c['REVISAR']}, ATENÇÃO {c['ATENÇÃO']}")
        for r in rs[: args.top]:
            print(f"   {r['id'] or '?':<6} {r['trecho']:<28} cob {r['cobertura']:.2f}  {r['veredito']:<8} razão {r['razao_do_alvo']}  faltam: {r['faltam'][:70]}")
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter=";")
            w.writeheader()
            w.writerows(sorted(rows, key=lambda r: (r["disciplina"], r["cobertura"])))
    if args.md:
        write_md(Path(args.md), rows, by)
    return 0


def write_md(path: Path, rows: list[dict], by: dict) -> None:
    out = [
        "# Cobertura automática dos resumos (triagem)",
        "",
        "Gerado por `pipeline/summary_coverage.py`. Mede omissão de termos específicos do texto-fonte; **não** detecta conceito errado. "
        "O veredito compara cada resumo com os da mesma disciplina. REFAÇÃO/REVISAR vão para leitura por agente ou pessoa, com a lista "
        "de termos que faltam como ponto de partida.",
        "",
    ]
    for v in ("REFAÇÃO", "REVISAR"):
        sel = sorted((r for r in rows if r["veredito"] == v), key=lambda r: (r["disciplina"], r["cobertura"]))
        out += [f"## {v} ({len(sel)})", "", "| ID | Trecho | Agente | Cobertura | % do alvo | Termos que faltam (mais pesados) |", "| --- | --- | --- | --- | --- | --- |"]
        for r in sel:
            pct = f"{round(float(r['razao_do_alvo']) * 100)}%" if r["razao_do_alvo"] != "" else "—"
            out.append(f"| {r['id']} | {r['trecho']} | {r['agente']} | {r['cobertura']:.2f} | {pct} | {r['faltam']} |")
        out.append("")
    path.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
