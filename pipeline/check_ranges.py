"""Valida bizus e diretrizes contra as páginas do PDF (precisa do cache de `extract.py`).

Para cada trecho de teoria com bizu em content/items:
  1. PONTEIROS  — o `pageRef` de cada ponteiro leva à página onde o tópico aparece?
        * fora do intervalo do trecho -> "fora";
        * o tópico (todos os radicais das palavras) aparece inteiro na página anterior e não na indicada -> "deslocado"
          (só sugestão: a correção automática não é confiável);
  2. RESUMO     — termos em **negrito** e números do resumo que só existem FORA das páginas do trecho ("fora do intervalo");
  3. DIRETRIZ   — "parando antes do tópico Z": Z abre no meio da pág. fim+1? ("titulo-no-meio", informativo: o texto da
        diretriz já orienta a ler essa parte) e segmentos que declaram "encerra a teoria" mas a página seguinte ainda traz
        muita teoria antes de "Principais pontos" ("teoria-continua").

Uso:
  python pipeline/check_ranges.py [--subject quimica] [--out relatorio.md]
O relatório fica em pipeline/.cache/reports/ranges-check.md (ignorado pelo git). É heurístico e só LISTA: tudo o que for
apontado vai para revisão humana (em amostra manual, a correção automática de ponteiros errava mais da metade dos casos).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import CACHE_DIR, CONTENT_DIR, PAGES_DIR  # noqa: E402

# só se corrige sozinho quando o tópico quase não aparece na página indicada (em amostra manual, limiares maiores erravam)
FIX_MAX_HERE = 0.34
STOP = {"para", "como", "entre", "sobre", "quando", "pelo", "pela", "pelos", "pelas", "mais", "menos", "seus", "suas", "dois", "duas", "esse", "essa", "este", "esta", "cada", "outros", "outras"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def stems(s: str) -> list[str]:
    return sorted({w[:5] for w in norm(s).split() if len(w) >= 4 and w not in STOP})


def topic_variants(topic: str) -> list[tuple[list[str], bool]]:
    """Radicais do tópico inteiro e, se o tópico for composto ("A, B e C; D"), só os da primeira cláusula (onde ele começa)."""
    out = [(stems(topic), False)]
    head = re.split(r"[;:,(]", topic, maxsplit=1)[0]
    if head.strip() and norm(head) != norm(topic) and stems(head):
        out.append((stems(head), True))
    return [(st, h) for st, h in out if st]


class Pages:
    """Texto normalizado por página de uma aula."""

    def __init__(self, raw: dict[int, str]):
        self.raw = raw
        self.norm = {n: norm(t) for n, t in raw.items()}
        self.stems = {n: {w[:5] for w in t.split() if len(w) >= 4} for n, t in self.norm.items()}

    def score(self, topic_stems: list[str], n: int) -> float:
        if not topic_stems or n not in self.stems:
            return 0.0
        return sum(1 for s in topic_stems if s in self.stems[n]) / len(topic_stems)

    def has_phrase(self, phrase: str, lo: int, hi: int) -> list[int]:
        p = f" {phrase} "
        return [n for n in range(lo, hi + 1) if n in self.norm and p in f" {self.norm[n]} "]


def load_pages() -> dict[str, Pages]:
    out: dict[str, Pages] = {}
    for f in PAGES_DIR.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["aula"]] = Pages({p["n"]: p["text"] for p in d["pages"]})
    return out


BOLD = re.compile(r"\*\*(.+?)\*\*")
NUM = re.compile(r"(?<![\w.,])\d{1,3}(?:[.,]\d+)+|(?<![\w.,])\d{3,}(?![\w.,])")


def check_segment(seg: dict, bizu: dict, pg: Pages) -> dict:
    lo, hi = seg["startPage"], seg["endPage"]
    hi0 = hi  # fim declarado do trecho (a diretriz usa este)
    res: dict = {"pointers": [], "summary": [], "directive": []}

    # 1. ponteiros
    for p in bizu.get("pointers", []):
        ref, topic = p["pageRef"], p["topic"]
        if ref < lo or ref > hi:
            res["pointers"].append({"topic": topic, "ref": ref, "kind": "fora", "fix": None})
            continue
        verdict = None
        for st, head in topic_variants(topic):
            full = [n for n in range(lo, hi + 1) if pg.score(st, n) >= 1.0]
            if not full or ref in full:
                if ref in full and not head:
                    verdict = "ok"
                    break
                continue
            if head and (len(st) < 2 and len(full) > 3):
                continue  # radical único e comum no trecho: não localiza o tópico
            here = pg.score(st, ref)
            if (ref - 1) in full and here <= FIX_MAX_HERE and (len(st) >= 3 or head):
                verdict = ("deslocado", ref - 1)
                break
            if (ref + 1) in full and here == 0 and len(st) >= 3:
                verdict = ("deslocado", ref + 1)
                break
            if (ref - 1) in full and here < 0.75:
                verdict = ("revisar", [ref - 1])
            if min(abs(n - ref) for n in full) >= 1 and here < 0.5 and not head:
                verdict = ("revisar", full[:3])
        if isinstance(verdict, tuple) and verdict[0] == "deslocado":
            res["pointers"].append({"topic": topic, "ref": ref, "kind": "deslocado", "fix": verdict[1]})
        elif isinstance(verdict, tuple):
            res["pointers"].append({"topic": topic, "ref": ref, "kind": "revisar", "fix": None, "where": verdict[1]})

    # 3. diretriz
    if seg.get("stopBeforeTopic"):
        st = stems(seg["stopBeforeTopic"])
        nxt = hi + 1
        if st and pg.score(st, nxt) >= 1.0 and pg.score(st, hi) < 1.0:
            text = pg.raw.get(nxt, "")
            idx = _first_stem_pos(text, st)
            if idx is not None and idx > 300:
                res["directive"].append({"kind": "titulo-no-meio", "page": nxt, "pos": idx})
    if seg.get("endsTheory"):
        text = pg.raw.get(hi + 1, "")
        m = re.search(r"principais pontos", norm_keep(text))
        if m and m.start() > 700:
            res["directive"].append({"kind": "teoria-continua", "page": hi + 1, "chars": m.start()})
    # a diretriz manda ler, na pág. fim+1, a parte anterior ao título seguinte: essa página conta como parte do trecho
    if any(d["kind"] == "titulo-no-meio" for d in res["directive"]):
        hi += 1

    # 2. resumo: termos em negrito e números que só aparecem fora do intervalo
    inside = " ".join(pg.norm.get(n, "") for n in range(lo, hi + 1))
    inside_p = f" {inside} "
    near_lo, near_hi = max(1, lo - 4), hi + 4
    raw_inside = "\n".join(pg.raw.get(n, "") for n in range(lo, hi + 1))
    for par in bizu.get("summary", []):
        for term in BOLD.findall(par):
            t = norm(term)
            if len(t) < 4 or f" {t} " in inside_p:
                continue
            ts = [w[:5] for w in t.split() if len(w) >= 4 and w not in STOP]
            if ts and all(s in {w[:5] for w in inside.split()} for s in ts):
                continue  # as palavras existem no trecho (reordenadas/flexionadas)
            outside = [n for n in pg.has_phrase(t, near_lo, near_hi) if n < lo or n > hi]
            if outside:
                res["summary"].append({"what": term, "kind": "fora", "pages": outside[:3]})
        for num in NUM.findall(par):
            if num in raw_inside:
                continue
            outside = [n for n in range(near_lo, near_hi + 1) if (n < lo or n > hi) and num in pg.raw.get(n, "")]
            if outside:
                res["summary"].append({"what": num, "kind": "fora", "pages": outside[:3]})

    return res


def norm_keep(s: str) -> str:
    """Normaliza sem alterar os índices de caractere (para medir posição no texto original)."""
    s2 = unicodedata.normalize("NFD", s)
    out = []
    for c in s2:
        if unicodedata.category(c) == "Mn":
            continue
        out.append(c.lower())
    return "".join(out)


def _first_stem_pos(text: str, st: list[str]) -> int | None:
    low = norm_keep(text)
    pos = [low.find(s) for s in st]
    pos = [p for p in pos if p >= 0]
    return min(pos) if pos else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject")
    ap.add_argument("--out", default=str(CACHE_DIR / "reports" / "ranges-check.md"))
    args = ap.parse_args()
    if not PAGES_DIR.exists() or not any(PAGES_DIR.glob("*.json")):
        print("cache de páginas ausente: rode pipeline/extract.py antes")
        return 2
    pages = load_pages()
    totals: Counter = Counter()
    by_subject: dict[str, Counter] = defaultdict(Counter)
    lines: list[str] = []
    for seg_file in sorted((CONTENT_DIR / "segments").glob("*.json")):
        subject = seg_file.stem
        if args.subject and subject != args.subject:
            continue
        segs = {s["id"]: s for s in json.loads(seg_file.read_text(encoding="utf-8"))["segments"]}
        for items_file in sorted((CONTENT_DIR / "items" / subject).glob("a*.json")):
            doc = json.loads(items_file.read_text(encoding="utf-8"))
            for it in doc["segments"]:
                seg, bizu = segs.get(it["id"]), it.get("bizu")
                pg = pages.get(seg["aula"]) if seg else None
                if not seg or not bizu or not pg:
                    continue
                r = check_segment(seg, bizu, pg)
                totals["trechos"] += 1
                by_subject[subject]["trechos"] += 1
                flagged = False
                for p in r["pointers"]:
                    totals[f"ponteiro-{p['kind']}"] += 1
                    by_subject[subject][f"ponteiro-{p['kind']}"] += 1
                    flagged = True
                    lines.append(f"- `{it['id']}` ponteiro **{p['kind']}**: “{p['topic']}” pág. {p['ref']}" + (f" → {p['fix']}" if p.get("fix") else "") + (f" (aparece em {p['where']})" if p.get("where") else ""))
                if r["summary"]:
                    totals["resumo-fora"] += 1
                    by_subject[subject]["resumo-fora"] += 1
                    flagged = True
                    lines.append(f"- `{it['id']}` resumo com {len(r['summary'])} termo(s) só fora do intervalo {seg['startPage']}-{seg['endPage']}: " + "; ".join(f"“{x['what']}” (págs. {x['pages']})" for x in r["summary"][:5]))
                for d in r["directive"]:
                    totals[f"diretriz-{d['kind']}"] += 1
                    by_subject[subject][f"diretriz-{d['kind']}"] += 1
                    if d["kind"] == "teoria-continua":
                        flagged = True
                        lines.append(f"- `{it['id']}` diretriz diz que a teoria acaba na pág. {seg['endPage']}, mas a pág. {d['page']} traz ~{d['chars']} caracteres de teoria antes de “Principais pontos”")
                if flagged:
                    totals["trechos-com-alerta"] += 1
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    head = ["# Validação de bizus e diretrizes contra o PDF", "", f"Trechos verificados: {totals['trechos']}", ""]
    head += [f"- {k}: {v}" for k, v in sorted(totals.items()) if k != "trechos"]
    head += ["", "## Por disciplina", ""]
    for s, c in by_subject.items():
        head.append(f"- {s}: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))
    head += ["", "## Alertas", ""]
    out.write_text("\n".join(head + lines) + "\n", encoding="utf-8")
    print("\n".join(head[:12]))
    print(f"relatório: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
