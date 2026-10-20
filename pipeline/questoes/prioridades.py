"""Lista priorizada de assuntos para a próxima rodada de download de questões.

    pipeline/.venv/Scripts/python pipeline/questoes/prioridades.py > docs/questoes/relatorios/prioridades-download.md

Déficit de um assunto do edital = max(0, META − questões aprovadas). Prioridade = déficit × peso da
disciplina na prova do CBMPE Oficial (contests.json). Só o CBMPE Oficial tem edital estruturado no sistema.
"""
import glob
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))
sys.stdout.reconfigure(encoding="utf-8")
from questoes.classify import Classifier, load_catalog, load_map  # noqa: E402

META = 10
contests = json.loads((ROOT / "content/contests.json").read_text(encoding="utf-8"))
W = contests["CBMPE_OFICIAL"]["exam"]
DISC = [s for s in W]
man = json.loads((ROOT / "docs/questoes/.importadas.json").read_text(encoding="utf-8"))
ac = {}
for sha in man["cadernos"]:
    for q in json.loads((ROOT / f"docs/questoes/.extraidas/{sha}.json").read_text(encoding="utf-8"))["questoes"]:
        ac[q["tecId"]] = q
cat = load_catalog()
clf = Classifier(cat, load_map())
valid = {k: q for k, q in ac.items() if not q["problems"] and not q["anulada"]}
clf.vote_assuntos(list(valid.values()))
item_n, seg_n = Counter(), Counter()
for q in valid.values():
    r = clf.classify(q)
    if r.status == "APPROVED":
        if r.editalItemId:
            item_n[r.editalItemId] += 1
        seg_n[r.segmentId] += 1
segs = {s["id"]: s for f in glob.glob(str(ROOT / "content/segments/*.json")) for s in json.loads(Path(f).read_text(encoding="utf-8"))["segments"]}
items = defaultdict(list)
for eid, it in cat.edital_items.items():
    if it["subject"] in W:
        items[it["subject"]].append((eid, it["title"]))

rows = []
for s in DISC:
    its = items.get(s, [])
    d_items = [(e, t, item_n[e]) for e, t in its if item_n[e] < META]
    d_tot = sum(META - n for _, _, n in d_items)
    s_ids = [i for i in segs if i.startswith(s + "/")]
    s_low = sum(1 for i in s_ids if seg_n[i] < 5)
    rows.append((d_tot * W[s], s, d_tot, len(d_items), len(its), s_low, len(s_ids), d_items))
rows.sort(reverse=True)

print("# Prioridades para a próxima rodada de download\n")
print(f"Meta: {META} questões AOCP aprovadas por assunto do edital. Prioridade = déficit × peso da disciplina na prova do CBMPE Oficial.")
print("Filtre sempre por **Instituto AOCP**. Os nomes de assunto abaixo são os do sistema; no TecConcursos procure pelo tema equivalente.\n")
print("## Ranking das disciplinas\n")
print("| # | Disciplina | Peso na prova | Assuntos abaixo da meta | Déficit (questões) | Trechos com < 5 questões | Sugestão de download |")
print("|---|---|---:|---:|---:|---:|---:|")
for i, (p, s, d, n, tot, sl, st, _) in enumerate(rows, 1):
    print(f"| {i} | {s} | {W[s]} | {n} de {tot} | {d} | {sl} de {st} | {min(d, int(d * 0.6) + 20)} |")
print("\n(\"Sugestão\" = 60% do déficit, pois parte dele é de assuntos que o TEC quase não tem com a banca AOCP.)\n")
for p, s, d, n, tot, sl, st, d_items in rows:
    if not d_items:
        continue
    print(f"\n## {s}: {d} questões faltando em {n} assuntos\n")
    zero = [x for x in d_items if x[2] == 0]
    few = [x for x in d_items if x[2] > 0]
    if zero:
        print(f"**Sem nenhuma questão ({len(zero)})**\n")
        for e, t, _ in zero:
            print(f"- `{e.split('/')[1]}` {t[:110]}")
    if few:
        print(f"\n**Com poucas ({len(few)})**\n")
        for e, t, k in sorted(few, key=lambda x: x[2]):
            print(f"- `{e.split('/')[1]}` {t[:110]}: {k} de {META}")
