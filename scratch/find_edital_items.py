import json
from pathlib import Path

# Inspect a07 and a09 of direito-administrativo
ed_da = json.loads(Path("content/edital/pcpe/direito-administrativo.json").read_text(encoding="utf-8"))
for it in ed_da["items"]:
    for w in it.get("where", []):
        if "a07" in w.get("aula", ""):
            print(f"DA a07 -> item {it['id']}")
        if "a09" in w.get("aula", ""):
            print(f"DA a09 -> item {it['id']}")

# Inspect estatistica a05
ed_est = json.loads(Path("content/edital/pcpe/estatistica.json").read_text(encoding="utf-8"))
for it in ed_est["items"]:
    for w in it.get("where", []):
        if "a05" in w.get("aula", ""):
            print(f"EST a05 -> item {it['id']}")

# Inspect informatica a06
ed_inf = json.loads(Path("content/edital/pcpe/informatica.json").read_text(encoding="utf-8"))
for it in ed_inf["items"]:
    for w in it.get("where", []):
        if "a06" in w.get("aula", ""):
            print(f"INF a06 -> item {it['id']}")
