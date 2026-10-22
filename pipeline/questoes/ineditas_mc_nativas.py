"""Questões INÉDITAS MentorIA de MÚLTIPLA ESCOLHA escritas diretamente (5 alternativas, A–E), o formato da prova do PCPE.

Fonte: `content/questoes/ineditas/mc/<disciplina>.txt`. Formato de cada questão (blocos separados por linhas `@@`):

    @@ <aula>/<trecho> | <A|B|C|D|E> [| item=<código do assunto>]     (a letra é o GABARITO)
    Enunciado (ex.: "Acerca de ..., assinale a opção correta." / "...assinale a opção INCORRETA.")
    A) texto
    B) texto
    C) texto
    D) texto
    E) texto
    // Comentário: por que a alternativa do gabarito está certa e (resumidamente) por que as outras não.

Uso:
    python pipeline/questoes/ineditas_mc_nativas.py --check
    python pipeline/questoes/ineditas_mc_nativas.py --json SAIDA.json   # lote para web/scripts/questoes-ineditas.ts
    python pipeline/questoes/ineditas_mc_nativas.py --resumo
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ineditas import DIR, BANCA, item_for_segment, segments  # noqa: E402

MC_DIR = DIR / "mc"
BATCH_MCN = "mentoria-inedita-mcn-2026-10-20"
LETTERS = "ABCDE"
AVISOS: list[str] = []


def parse(path: Path) -> list[dict]:
    subject = path.stem
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    out = []
    for n, block in enumerate(re.split(r"(?m)^@@ ", text)[1:], 1):
        head, _, body = block.partition("\n")
        m = re.fullmatch(r"\s*(\S+)\s*\|\s*([A-E])\s*(?:\|\s*item=(\S+)\s*)?", head)
        if not m:
            raise SystemExit(f"{path.name} bloco {n}: cabeçalho inválido: {head!r}")
        seg, ans, item = m.groups()
        main, _, expl = body.partition("\n//")
        parts = re.split(r"(?m)^([A-E])\)\s*", main.strip())
        stem = parts[0].strip()
        opts = [(parts[i], " ".join(parts[i + 1].split())) for i in range(1, len(parts) - 1, 2)]
        out.append({"subject": subject, "n": n, "segment": f"{subject}/{seg}", "answer": ans, "item": item,
                    "stem": stem, "options": opts, "explanation": " ".join(expl.split())})
    return out


def check(qs: list[dict]) -> list[str]:
    errs: list[str] = []
    seen: dict[str, str] = {}
    for q in qs:
        tag = f"{q['subject']} #{q['n']} ({q['segment']})"
        if q["segment"] not in segments(q["subject"]):
            errs.append(f"{tag}: trecho inexistente")
        elif not item_for_segment(q["subject"], q["segment"], q.get("item")):
            # trecho de concurso sem esse assunto no mapa do edital (ex.: CBMPE): a questão entra só no caderno do plano,
            # com editalItemId nulo; não é erro
            AVISOS.append(f"{tag}: trecho sem assunto do edital (editalItemId nulo)")
        if [l for l, _ in q["options"]] != list(LETTERS):
            errs.append(f"{tag}: precisa de exatamente 5 alternativas A) a E) em ordem")
            continue
        if not re.search(r"assinale|julgue|indique", q["stem"], re.I):
            errs.append(f"{tag}: enunciado sem comando ('assinale a opção ...')")
        w = len(q["stem"].split())
        if not 6 <= w <= 140:
            errs.append(f"{tag}: enunciado com {w} palavras (esperado 6-140)")
        texts = [t for _, t in q["options"]]
        if any(len(t.split()) < 1 for t in texts) or len({t.lower() for t in texts}) < 5:
            errs.append(f"{tag}: alternativas vazias ou repetidas")
        if len(q["explanation"].split()) < 5:
            errs.append(f"{tag}: comentário ausente ou curto")
        key = re.sub(r"\W+", " ", q["stem"].lower()).strip() + "|" + "|".join(sorted(texts))
        if key in seen:
            errs.append(f"{tag}: questão repetida (igual à de {seen[key]})")
        seen[key] = tag
        # alternativa correta muito mais longa que as demais denuncia o gabarito
        ln = [len(t) for t in texts]
        right = ln[LETTERS.index(q["answer"])]
        if right > 1.8 * (sum(ln) - right) / 4 and right > 80:
            errs.append(f"{tag}: alternativa do gabarito bem mais longa que as outras (equilibre os tamanhos)")
    # comentário não pode citar a letra do gabarito como se fosse alternativa errada (ex.: "As alternativas A, B e D erram" com D correta)
    ref = re.compile(r"(?:[Aa]s?\s+)?(?:alternativas?|op[çc][ãa]o|op[çc][õo]es)\s+((?:[A-E](?:,\s*|\s+e\s+|\s+ou\s+))*[A-E])")
    for q in qs:
        e = q["explanation"]
        for m in ref.finditer(e):
            letras = re.findall(r"[A-E]", m.group(1))
            if q["answer"] in letras and not re.match(r"\s*(?:est[áa]\s+correta|[ée]\s+(?:a\s+)?correta|correta)", e[m.end():m.end() + 25]):
                errs.append(f"{q['subject']} #{q['n']}: o comentário cita a alternativa correta ({q['answer']}) entre as erradas")
                break
    # gabaritos em sequência previsível (A,B,C,D,E,A,...) por disciplina
    seq = defaultdict(list)
    for q in qs:
        seq[q["subject"]].append("ABCDE".index(q["answer"]))
    for sbj, l in seq.items():
        if len(l) >= 20 and sum((l[i + 1] - l[i]) % 5 == 1 for i in range(len(l) - 1)) > 0.5 * (len(l) - 1):
            errs.append(f"{sbj}: gabaritos em sequência cíclica; sorteie as posições (nada de A,B,C,D,E em ordem)")
    by = defaultdict(Counter)
    for q in qs:
        by[q["subject"]][q["answer"]] += 1
    for s, c in by.items():
        tot = sum(c.values())
        if tot >= 20 and max(c.values()) > 0.32 * tot:
            errs.append(f"{s}: gabaritos desequilibrados {dict(c)} (nenhuma letra deve passar de ~30%)")
    return errs


def qid(q: dict) -> str:
    h = hashlib.sha1((q["stem"] + "".join(t for _, t in q["options"])).encode()).hexdigest()[:6]
    return f"mentoria_mcn_{q['subject']}_{q['n']:03d}_{h}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = [Path(f) for f in a.files] or sorted(MC_DIR.glob("*.txt"))
    qs = [q for f in files for q in parse(f)]
    errs = check(qs)
    for e in errs:
        print("ERRO", e)
    if AVISOS and (a.resumo or a.check):
        print(f"AVISO {len(AVISOS)} questões em trechos sem assunto do edital (ok para o CBMPE)")
    if a.resumo or a.check:
        by = defaultdict(Counter)
        for q in qs:
            by[q["subject"]][q["answer"]] += 1
        for s, c in by.items():
            print(f"{s}: {sum(c.values())} questões · " + " ".join(f"{l} {c[l]}" for l in LETTERS))
        print(f"TOTAL {len(qs)} · erros {len(errs)}")
    if a.json and not errs:
        rows = [{
            "id": qid(q), "subjectId": q["subject"], "segmentId": q["segment"], "aulaId": "/".join(q["segment"].split("/")[:2]),
            "editalItemId": item_for_segment(q["subject"], q["segment"], q.get("item")), "kind": "MULTIPLA_ESCOLHA",
            "statement": q["stem"], "banca": BANCA, "batch": BATCH_MCN, "explanation": q["explanation"],
            "options": [{"label": l, "text": t, "isCorrect": l == q["answer"]} for l, t in q["options"]],
        } for q in qs]
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(rows)} questões -> {a.json}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
