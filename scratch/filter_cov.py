import csv
import json
from pathlib import Path

PCPE_SUBJECTS = {
    "lingua-portuguesa", "informatica", "raciocinio-logico", "matematica", "estatistica", "contabilidade-geral",
    "legislacao-pcpe", "direito-constitucional", "direito-administrativo", "direito-penal",
    "legislacao-penal-especial", "direito-processual-penal",
}

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

print(f"Total PCPE segments in test plans: {len(planos_segs)}")

# Read cov.csv
cov_path = Path("pipeline/.cache/cov.csv")
with open(cov_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    rows = list(reader)

refacao = []
revisar = []
baixo_60 = []

for r in rows:
    trecho = r["trecho"]
    disc = trecho.split("/")[0]
    if disc not in PCPE_SUBJECTS:
        continue
    if trecho not in planos_segs:
        continue
        
    veredicto = r["veredito"].strip()
    cob = float(r["cobertura"]) if r["cobertura"] else 0.0
    
    if veredicto == "REFAÇÃO":
        refacao.append((trecho, cob, r))
    elif veredicto == "REVISAR":
        revisar.append((trecho, cob, r))
    elif cob < 0.60:
        baixo_60.append((trecho, cob, r))

print(f"PCPE (planos) REFAÇÃO: {len(refacao)}")
print(f"PCPE (planos) REVISAR: {len(revisar)}")
print(f"PCPE (planos) Total REVISAR/REFAÇÃO: {len(refacao) + len(revisar)}")
print(f"PCPE (planos) Baixa cobertura (<0.60) mas OK/ATENÇÃO: {len(baixo_60)}")

by_disc = {}
for t, c, r in refacao + revisar:
    disc = t.split("/")[0]
    by_disc[disc] = by_disc.get(disc, 0) + 1

print("\nPor disciplina (REVISAR/REFAÇÃO nos 662 trechos dos planos):")
for d, count in sorted(by_disc.items()):
    print(f"  {d}: {count}")

# Check what briefing said:
# "Os 662 resumos usados nos planos de teste estão em DRAFT. A triagem automática (pipeline/summary_coverage.py --csv ...) marca
# 76 como REVISAR/REFAÇÃO para os trechos do PCPE (11 disciplinas; mais Raciocínio Lógico, que tem muitos exemplos com nomes), e 24 têm menos de 60% dos tópicos do trecho citados."
