import json, sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('scratch/trechos_fracos/direito-penal.json', encoding='utf-8'))
print('Count of segments:', len(data))
total_faltam = sum(d['faltam'] for d in data)
print('Total faltam:', total_faltam)
for i, d in enumerate(data, 1):
    print(f"{i:02d}. {d['trecho']} ({d['seg']}): faltam {d['faltam']} (atuais={d['atuais']}, alvo={d['alvo']}) - {d['aula']} | {d['topicos'][:60]}...")
