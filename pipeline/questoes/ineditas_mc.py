"""Versão de múltipla escolha (5 alternativas, A–E) das questões inéditas MentorIA.

O edital do PCPE (item 8.2) diz que as questões da prova objetiva são de múltipla escolha, com cinco opções. Esta rotina
compõe, a partir das assertivas certo/errado de `content/questoes/ineditas/*.txt`, questões de múltipla escolha do mesmo
assunto do edital:
  - tipo A: 1 assertiva certa + 4 erradas ("assinale a alternativa correta");
  - tipo B: 4 assertivas certas + 1 errada ("assinale a alternativa INCORRETA").
Só entram assertivas que se entendem sozinhas (sem cenário numérico ou referência ao enunciado) e disciplinas sem contas
(Raciocínio Lógico, Matemática e Estatística ficam de fora). A posição do gabarito é distribuída por sorteio fixo.

Uso:
    python pipeline/questoes/ineditas_mc.py --json SAIDA.json [--mostrar N]   # lote para web/scripts/questoes-ineditas.ts
    python pipeline/questoes/ineditas_mc.py --resumo
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ineditas import DIR, BANCA, edital_items, item_for_segment, parse  # noqa: E402

BATCH_MC = "mentoria-inedita-mc-2026-10-20"
SKIP_SUBJECTS = {"raciocinio-logico", "matematica", "estatistica"}
SCENARIO = re.compile(r"\b(Considere|considere|situação hipotética|Suponha|suponha|Imagine|hipotética|Em um grupo|Uma urna|Duas|Dois|Um agente|Uma empresa|Uma entidade|Uma loja)\b")
ANAPHORA = re.compile(r"^(Nessa|Nesse|Nesta|Neste|Tal\b|Essa|Esse|Isso|Ele\b|Ela\b|Eles\b|Elas\b|Nele|Nela|Naquela|Naquele|Após esse|Após essa)")
LETTERS = "ABCDE"


def standalone(q: dict) -> bool:
    parts = [p.strip() for p in q["statement"].split("\n\n") if p.strip()]
    if len(parts) != 2:
        return False
    lead, asr = parts
    words = len(asr.split())
    return not SCENARIO.search(lead) and not ANAPHORA.match(asr) and 8 <= words <= 60 and "item anterior" not in asr


def assertion(q: dict) -> str:
    return [p.strip() for p in q["statement"].split("\n\n") if p.strip()][-1]


def topic(title: str) -> str:
    t = re.sub(r"\s+", " ", title).strip().rstrip(".")
    return t[0].lower() + t[1:] if len(t) > 1 and t[1].islower() else t


def build() -> list[dict]:
    qs = [q for f in sorted(DIR.glob("*.txt")) if f.stem not in SKIP_SUBJECTS for q in parse(f)]
    titles = {}
    groups: dict[str, dict[str, list[dict]]] = defaultdict(lambda: {"C": [], "E": []})
    for q in qs:
        if not standalone(q):
            continue
        item = item_for_segment(q["subject"], q["segment"], q.get("item"))
        if not item:
            continue
        subj, code = item.split("/", 1)[0], item.split("/", 1)[1][1:]
        for it in edital_items(subj):
            if it["id"] == code:
                titles[item] = it["item"]
        groups[item][q["answer"]].append(q)
    rows = []
    counter: dict[str, int] = defaultdict(int)
    for item in sorted(groups):
        T, F = list(groups[item]["C"]), list(groups[item]["E"])
        subject = item.split("/")[0]
        while len(T) + len(F) >= 5:
            if len(F) >= 4 and (len(T) < 4 or len(F) >= len(T)) and T:
                right, wrong, style = [T.pop(0)], [F.pop(0) for _ in range(4)], "A"
            elif len(T) >= 4 and F:
                right, wrong, style = [T.pop(0) for _ in range(4)], [F.pop(0)], "B"
            else:
                break
            correct_pool = right if style == "A" else wrong
            others = wrong if style == "A" else right
            counter[subject] += 1
            n = counter[subject]
            rnd = random.Random(f"{subject}-{n}")
            pos = (n * 2 + len(subject)) % 5  # posição do gabarito, espalhada entre A e E
            texts = [assertion(q) for q in others]
            rnd.shuffle(texts)
            correct_text = assertion(correct_pool[0])
            texts.insert(pos, correct_text)
            stem = f"No que se refere a {topic(titles[item])}, assinale a alternativa {'correta' if style == 'A' else 'INCORRETA'}."
            expl_lines = []
            if style == "A":
                expl_lines.append(f"Alternativa {LETTERS[pos]}: {right[0]['explanation']}")
                for q in wrong:
                    expl_lines.append(f"Incorreta ({assertion(q)[:70]}…): {q['explanation']}")
            else:
                expl_lines.append(f"Alternativa {LETTERS[pos]} (incorreta): {wrong[0]['explanation']}")
            seg = (right + wrong)[0]["segment"]
            h = hashlib.sha1((stem + correct_text).encode()).hexdigest()[:6]
            rows.append({
                "id": f"mentoria_mc_{subject}_{n:03d}_{h}", "subjectId": subject, "segmentId": seg,
                "aulaId": "/".join(seg.split("/")[:2]), "editalItemId": item, "kind": "MULTIPLA_ESCOLHA",
                "statement": stem, "banca": BANCA, "batch": BATCH_MC, "explanation": " ".join(expl_lines),
                "options": [{"label": LETTERS[i], "text": t, "isCorrect": i == pos} for i, t in enumerate(texts)],
            })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("--mostrar", type=int, default=0)
    a = ap.parse_args()
    rows = build()
    by = defaultdict(int)
    for r in rows:
        by[r["subjectId"]] += 1
    if a.resumo or a.mostrar:
        for s, n in sorted(by.items()):
            print(f"{s}: {n} questões de múltipla escolha")
        print("TOTAL", len(rows))
    for r in rows[: a.mostrar]:
        print("\n" + r["id"], r["editalItemId"], "\n" + r["statement"])
        for o in r["options"]:
            print(f"  {o['label']}) {'*' if o['isCorrect'] else ' '} {o['text']}")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(rows)} questões -> {a.json}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
