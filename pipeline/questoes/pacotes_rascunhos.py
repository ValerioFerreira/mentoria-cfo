"""Monta pacotes de trabalho para agentes classificarem os RASCUNHOS (questões em que o classificador
automático não teve segurança): um JSON por lote com as questões e a taxonomia da disciplina.

    pipeline/.venv/Scripts/python pipeline/questoes/pacotes_rascunhos.py [--lote 70] [--saida DIR]

Saída: docs/questoes/classificacao-agentes/<data>/pacotes/<disciplina>-NN.json e taxonomia/<disciplina>.md.
Resultado esperado dos agentes (um JSON por linha em ../resultados/<mesmo nome>.jsonl):
  {"tecId", "segment", "itemEdital", "confianca": "alta|media|baixa", "acao": "classificar|skip", "motivo"}
`aplicar_agentes.py` transforma isso em content/questoes/overrides-questoes.json.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))
sys.stdout.reconfigure(encoding="utf-8")
from questoes.classify import Classifier, load_catalog, load_map  # noqa: E402

MD_IMG = re.compile(r"!\[([^\]]*)\]\(/q-img/([0-9a-f]{64})\)")
IMG = ROOT / "docs" / "questoes" / ".extraidas" / "img"


def img(md: str) -> str:
    return MD_IMG.sub(lambda m: f"[{m.group(1)}: {IMG / (m.group(2) + '.png')}]", md or "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=int, default=70)
    ap.add_argument("--saida")
    args = ap.parse_args()
    out = Path(args.saida) if args.saida else ROOT / "docs" / "questoes" / "classificacao-agentes" / date.today().isoformat()
    (out / "pacotes").mkdir(parents=True, exist_ok=True)
    (out / "taxonomia").mkdir(exist_ok=True)
    (out / "resultados").mkdir(exist_ok=True)

    man = json.loads((ROOT / "docs/questoes/.importadas.json").read_text(encoding="utf-8"))
    ac: dict[str, dict] = {}
    for sha in man["cadernos"]:
        for q in json.loads((ROOT / f"docs/questoes/.extraidas/{sha}.json").read_text(encoding="utf-8"))["questoes"]:
            ac[q["tecId"]] = q
    cat = load_catalog()
    clf = Classifier(cat, load_map())
    valid = {k: q for k, q in ac.items() if not q["problems"] and not q["anulada"]}
    clf.vote_assuntos(list(valid.values()))

    drafts: dict[str, list[dict]] = defaultdict(list)
    for t, q in valid.items():
        r = clf.classify(q)
        if r.status != "DRAFT":
            continue
        # taxonomia da disciplina: a do classificador, ou a das aulas candidatas
        subj = r.subjectId
        if not subj:
            continue
        sup = img(q.get("support") or "")
        drafts[subj].append(
            {
                "tecId": t,
                "ano": q.get("ano"),
                "materiaTEC": q["materia"],
                "assuntoTEC": q["assunto"],
                "tipo": q["kind"],
                "textoBase": sup[:900] + (" […]" if len(sup) > 900 else ""),
                "enunciado": img(q["statement"]),
                "alternativas": [f"{o['label']}) {img(o['text'])}" for o in q["options"]],
                "gabarito": q.get("answer"),
                "sugestaoAutomatica": {"trecho": r.segmentId, "score": r.score, "nota": r.reason},
            }
        )

    # taxonomia por disciplina (itens do edital + aulas/trechos com tópicos)
    segs: dict[str, dict] = {}
    for f in glob.glob(str(ROOT / "content/segments/*.json")):
        for s in json.loads(Path(f).read_text(encoding="utf-8"))["segments"]:
            segs[s["id"]] = s
    for subj in drafts:
        L = [f"# Taxonomia de {subj}\n", "## Itens do edital (editalItemId)"]
        for eid, it in cat.edital_items.items():
            if it["subject"] == subj:
                L.append(f"- `{eid}` {it['title']} (aulas: {', '.join(sorted(set(it['aulas'])))})")
        L.append("\n## Aulas e trechos (segmentId). Cada trecho = uma atividade de Teoria; a questão vai para o trecho que ENSINA o que ela exige")
        for aid, a in cat.aulas.items():
            if a["subject"] != subj:
                continue
            L.append(f"- `{aid}` {a['title']}")
            for sid in a["segments"]:
                s = segs.get(sid, {})
                tops = [x for x in [s.get("startTopic")] + (s.get("topicsCovered") or []) if x]
                L.append(f"  - `{sid}`: {'; '.join(dict.fromkeys(tops))[:420]}")
        (out / "taxonomia" / f"{subj}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    n = 0
    for subj, qs in sorted(drafts.items()):
        qs.sort(key=lambda x: (x["assuntoTEC"], x["tecId"]))
        for i in range(0, len(qs), args.lote):
            n += 1
            name = f"{subj}-{i // args.lote + 1:02d}"
            (out / "pacotes" / f"{name}.json").write_text(json.dumps(qs[i : i + args.lote], ensure_ascii=False, indent=1), encoding="utf-8")
    print({s: len(v) for s, v in sorted(drafts.items())}, "| pacotes:", n, "|", out)


if __name__ == "__main__":
    main()
