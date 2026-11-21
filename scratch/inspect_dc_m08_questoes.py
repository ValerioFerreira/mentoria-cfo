import json

with open('pipeline/.cache/material/questoes/direito-constitucional__m08.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questoes = data['questoes']
by_cap = {}
for q in questoes:
    cap = q['capitulo']
    by_cap.setdefault(cap, []).append(q)

for cap, qlist in by_cap.items():
    print(f"\n=== {cap} ({len(qlist)} questoes) ===")
    for q in qlist:
        banca = q.get('banca', 'N/A')
        ano = q.get('ano', 'N/A')
        gab = q.get('gabarito', 'N/A')
        enunc = q.get('enunciado', '').replace('\n', ' ')[:75]
        print(f"  {q['id']} | {banca} ({ano}) | Gab: {gab} | {enunc}")
