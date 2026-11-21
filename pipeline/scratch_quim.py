import sys, json
sys.stdout.reconfigure(encoding="utf-8")

with open("pipeline/.cache/material/questoes/quimica__m01.json", encoding="utf-8") as f:
    data = json.load(f)

print("Total questoes:", len(data["questoes"]))
for q in data["questoes"]:
    banca = q.get("banca", "")
    cap = q.get("capitulo")
    print(f"ID: {q['id']} | Cap: {cap} | Banca: {banca} | Gab: {q.get('gabarito')} | Enunc: {q['enunciado'][:60]}...")
