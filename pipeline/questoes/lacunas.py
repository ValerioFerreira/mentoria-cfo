"""Assuntos do edital sem nenhuma questão nos PDFs (após a classificação atual). Saída em Markdown.
    pipeline/.venv/Scripts/python pipeline/questoes/lacunas.py > docs/questoes/relatorios/lacunas.md"""
import csv, json, sys, glob
from collections import Counter, defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline")); sys.stdout.reconfigure(encoding="utf-8")
from questoes.classify import Classifier, load_catalog, load_map

man = json.loads((ROOT / "docs/questoes/.importadas.json").read_text(encoding="utf-8"))
ac = {}
for sha in man["cadernos"]:
    for q in json.loads((ROOT / f"docs/questoes/.extraidas/{sha}.json").read_text(encoding="utf-8"))["questoes"]:
        ac[q["tecId"]] = q
clf = Classifier(load_catalog(), load_map())
ap, dr = Counter(), Counter()
for q in ac.values():
    if q["problems"] or q["anulada"]:
        continue
    r = clf.classify(q)
    if r.status == "APPROVED" and r.editalItemId: ap[r.editalItemId] += 1
    elif r.status == "DRAFT" and r.editalItemId: dr[r.editalItemId] += 1
items = defaultdict(list)
for f in sorted(glob.glob(str(ROOT / "content/edital/*.json"))):
    d = json.loads(Path(f).read_text(encoding="utf-8"))
    for it in d["items"]:
        items[d["subject"]].append((f"{d['subject']}/e{it['id']}", it["item"]))
print("# Assuntos do edital (sistema) sem nenhuma questão nos PDFs\n")
print("Aprovada = vai ao aluno; rascunho = só após revisão. 'Sem nenhuma' = 0 aprovadas e 0 rascunhos.\n")
tot0 = 0
for s, its in items.items():
    z = [(i, t) for i, t in its if ap[i] + dr[i] == 0]
    only_draft = [(i, t) for i, t in its if ap[i] == 0 and dr[i] > 0]
    tot0 += len(z)
    print(f"## {s}: {len(z)} sem nenhuma / {len(only_draft)} só rascunho / {len(its)} assuntos\n")
    for i, t in z: print(f"- `{i.split('/')[1]}` {t}")
    print()
print(f"**Total sem nenhuma questão: {tot0}**\n")
print("# Disciplinas dos editais PMPE ausentes do sistema (0 questões por definição)\n")
for n, k in [("Direito Penal", 8), ("Direito Processual Penal", 15), ("Direitos e Garantias Fundamentais", 19), ("Direito Processual Penal Militar", 18), ("Direitos Humanos e Legislação Extravagante (Soldado)", 17)]:
    print(f"- {n}: {k} tópicos no edital")
print("\n# PMPE Oficial, Direito Administrativo: tópicos do edital cujas questões foram baixadas mas não têm assunto no sistema\n")
rows = list(csv.DictReader(open(ROOT / "docs/questoes/auditoria/2026-10-14/mapa_correspondencia.csv", encoding="utf-8-sig"), delimiter=";"))
c = Counter()
for r in rows:
    if r["materiaTEC"].startswith("Direito Administrativo") and r["PMPE_OFICIAL"] in ("sim", "parcial") and r["tipo"] in ("SEM_CORRESPONDENCIA", "PARCIAL"):
        c[(r["PMPE_OFICIAL_edital"] or "?")[:70]] += int(r["questoes"])
for k, v in c.most_common(): print(f"- {k}: {v} questões")
