"""Lista, por aula de uma disciplina, os trechos (páginas, tópicos cobertos) para mapear itens do edital."""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
subj = sys.argv[1]
only = sys.argv[2:] 
cat = json.load(open("content/catalog.json", encoding="utf-8"))
s = next(x for x in cat["subjects"] if x["id"] == subj)
seg = json.load(open(f"content/segments/{subj}.json", encoding="utf-8"))["segments"]
by = {}
for g in seg: by.setdefault(g["aula"], []).append(g)
for a in s["aulas"]:
    if only and a["id"].split("/")[1] not in only: continue
    print(f"## {a['id']} | {a['title']} | only={a.get('onlyContests')} excl={a.get('excludeContests')} sel={a.get('selectable')}")
    for g in by.get(a["id"], []):
        tc = "; ".join(t[:45] for t in g.get("topicsCovered", [])[:4])
        print(f"   {g['id']} pp{g['startPage']}-{g['endPage']} | {tc}")
