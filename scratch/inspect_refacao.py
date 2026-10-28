import json
from pathlib import Path

# Load segments
segs = {}
for f in Path("content/segments").glob("*.json"):
    data = json.loads(f.read_text(encoding="utf-8"))
    for s in data["segments"]:
        segs[s["id"]] = s

t3_list = json.loads(Path("scratch/t3_pcpe_76.json").read_text(encoding="utf-8"))

print("=== 9 REFAÇÃO ===")
for x in t3_list:
    if x["veredito"] == "REFAÇÃO":
        s = segs.get(x["trecho"], {})
        print(f"{x['trecho']} | págs {s.get('startPage')}-{s.get('endPage')} | tópicos: {s.get('topicsCovered')}")

print("\n=== REVISAR (amostra) ===")
for x in t3_list[:15]:
    if x["veredito"] == "REVISAR":
        s = segs.get(x["trecho"], {})
        print(f"{x['trecho']} | cob={x['cobertura']} | págs {s.get('startPage')}-{s.get('endPage')} | tópicos: {s.get('topicsCovered')}")
