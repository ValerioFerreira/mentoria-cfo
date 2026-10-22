"""Questões INÉDITAS MentorIA (padrão Cebraspe, certo/errado) para assuntos do edital sem questão real no banco.

Fonte: `content/questoes/ineditas/<disciplina>.txt` (autorais, escritas a partir dos resumos do curso). Provisório: quando
as questões reais do TecConcursos forem importadas para o assunto, as inéditas dele podem ser aposentadas
(`web/scripts/questoes-ineditas.ts --aposentar`).

Formato de cada questão (blocos separados por linhas `@@`):

    @@ <aula>/<trecho> | <C|E> [| item=<código do assunto>]   (item só quando o trecho serve a mais de um assunto)
    Frase de abertura ("Em relação a ..., julgue o item a seguir.")

    Assertiva única.
    // Comentário/justificativa do gabarito (1 a 3 frases).

Uso:
    python pipeline/questoes/ineditas.py --check            # valida tudo (formato, trecho, equilíbrio C/E)
    python pipeline/questoes/ineditas.py --json SAIDA.json  # lote para o gravador (web/scripts/questoes-ineditas.ts)
    python pipeline/questoes/ineditas.py --resumo           # contagem por disciplina, assunto e gabarito
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
DIR = CONTENT / "questoes" / "ineditas"
BATCH = "mentoria-inedita-2026-10-19"
BANCA = "Inédita MentorIA"
# disciplinas do PCPE com mapa próprio (`content/edital/pcpe/`): itens `<disciplina>/p<código>`; as demais usam `/e<código>`
OWN_EDITAL = {"direito-administrativo", "direito-constitucional", "estatistica", "informatica", "lingua-portuguesa", "matematica", "raciocinio-logico"}
MIN_WORDS, MAX_WORDS = 14, 140


def segments(subject: str) -> dict[str, dict]:
    doc = json.loads((CONTENT / "segments" / f"{subject}.json").read_text(encoding="utf-8"))
    return {g["id"]: g for g in doc["segments"]}


def edital_items(subject: str) -> list[dict]:
    path = CONTENT / "edital" / ("pcpe" if subject in OWN_EDITAL else "") / f"{subject}.json"
    return json.loads(path.read_text(encoding="utf-8"))["items"]


def item_for_segment(subject: str, seg: str, code: str | None = None) -> str | None:
    """Assunto do edital (id no banco) mais específico que lista o trecho (ou o código informado em `item=`)."""
    if code:
        return f"{subject}/{'p' if subject in OWN_EDITAL else 'e'}{code}"
    best = None
    for it in edital_items(subject):
        ids = {s for w in it.get("where", []) for s in w.get("segments", [])}
        if seg in ids and (best is None or len(ids) < best[0]):
            best = (len(ids), it["id"])
    if not best and subject in OWN_EDITAL:
        # trecho que o edital do PCPE não lista (só existe nos concursos CBMPE/PMPE): usa o mapa padrão da disciplina
        std = json.loads((CONTENT / "edital" / f"{subject}.json").read_text(encoding="utf-8"))["items"]
        for it in std:
            ids = {s for w in it.get("where", []) for s in w.get("segments", [])}
            if seg in ids and (best is None or len(ids) < best[0]):
                best = (len(ids), it["id"])
        return f"{subject}/e{best[1]}" if best else None
    if not best:
        return None
    return f"{subject}/{'p' if subject in OWN_EDITAL else 'e'}{best[1]}"


def parse(path: Path) -> list[dict]:
    subject = path.stem
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    out = []
    for n, block in enumerate(re.split(r"(?m)^@@ ", text)[1:], 1):
        head, _, body = block.partition("\n")
        m = re.fullmatch(r"\s*(\S+)\s*\|\s*([CE])\s*(?:\|\s*item=(\S+)\s*)?", head)
        if not m:
            raise SystemExit(f"{path.name} bloco {n}: cabeçalho inválido: {head!r}")
        seg, ans, item = m.groups()
        stmt, _, expl = body.partition("\n//")
        out.append({"subject": subject, "n": n, "segment": f"{subject}/{seg}", "answer": ans, "item": item,
                    "statement": stmt.strip(), "explanation": " ".join(expl.split())})
    return out


def check(qs: list[dict]) -> list[str]:
    errs: list[str] = []
    seen: dict[str, str] = {}
    for q in qs:
        tag = f"{q['subject']} #{q['n']} ({q['segment']})"
        segs = segments(q["subject"])
        if q["segment"] not in segs:
            errs.append(f"{tag}: trecho inexistente")
        elif not item_for_segment(q["subject"], q["segment"], q.get("item")):
            errs.append(f"{tag}: trecho sem assunto do edital do PCPE")
        parts = [p for p in q["statement"].split("\n\n") if p.strip()]
        if len(parts) < 2 or not re.search(r"julgue|assinale|julgar", parts[0], re.I):
            errs.append(f"{tag}: falta frase de abertura com 'julgue o item ...' separada por linha em branco")
        words = len(q["statement"].split())
        if not MIN_WORDS <= words <= MAX_WORDS:
            errs.append(f"{tag}: {words} palavras (esperado {MIN_WORDS}-{MAX_WORDS})")
        if not q["explanation"] or len(q["explanation"].split()) < 3:
            errs.append(f"{tag}: comentário ausente ou curto")
        key = re.sub(r"\W+", " ", parts[-1].lower()).strip()
        if key in seen:
            errs.append(f"{tag}: assertiva repetida (igual à de {seen[key]})")
        seen[key] = tag
    return errs


def qid(q: dict) -> str:
    h = hashlib.sha1(q["statement"].encode()).hexdigest()[:6]
    return f"mentoria_{q['subject']}_{q['n']:03d}_{h}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = [Path(f) for f in a.files] or sorted(DIR.glob("*.txt"))
    qs = [q for f in files for q in parse(f)]
    errs = check(qs)
    for e in errs:
        print("ERRO", e)
    if a.resumo or a.check:
        by = defaultdict(Counter)
        for q in qs:
            by[q["subject"]][q["answer"]] += 1
        for s, c in by.items():
            print(f"{s}: {sum(c.values())} questões · C {c['C']} · E {c['E']}")
        tot = Counter(q["answer"] for q in qs)
        print(f"TOTAL {len(qs)} · C {tot['C']} · E {tot['E']} · erros {len(errs)}")
    if a.json:
        rows = []
        for q in qs:
            parts = [p for p in q["statement"].split("\n\n") if p.strip()]
            rows.append({"id": qid(q), "subjectId": q["subject"], "segmentId": q["segment"], "aulaId": "/".join(q["segment"].split("/")[:2]),
                         "editalItemId": item_for_segment(q["subject"], q["segment"], q.get("item")), "statement": q["statement"], "answer": q["answer"],
                         "explanation": q["explanation"], "banca": BANCA, "batch": BATCH, "n": q["n"], "lead": parts[0]})
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(rows)} questões -> {a.json}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
