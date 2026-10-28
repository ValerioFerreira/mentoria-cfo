import csv
import json
from pathlib import Path

# Load test plans segments
planos_path = Path("pipeline/.cache/pcpe-planos.json")
planos_segs = set()
if planos_path.exists():
    planos_data = json.loads(planos_path.read_text(encoding="utf-8"))
    for plan in planos_data:
        for act in plan.get("acts", []):
            if act.get("type") == "TEORIA":
                for s in act.get("segmentIds", []):
                    planos_segs.add(s)

cov_path = Path("pipeline/.cache/cov.csv")
with open(cov_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    rows = list(reader)

pcpe_revisar = []
for r in rows:
    trecho = r["trecho"]
    if trecho in planos_segs:
        veredicto = r["veredito"].strip()
        if veredicto in ("REFAÇÃO", "REVISAR"):
            pcpe_revisar.append(r)

print(f"Total nos planos com REVISAR/REFAÇÃO: {len(pcpe_revisar)}")
for r in pcpe_revisar[:15]:
    print(f"{r['trecho']} | {r['veredito']} | cob={r['cobertura']} | palavras={r['palavras']} | faltam={r['faltam'][:50]}")

# Save full list
Path("scratch/t3_pcpe_76.json").write_text(json.dumps(pcpe_revisar, indent=2, ensure_ascii=False), encoding="utf-8")
